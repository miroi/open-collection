#!/usr/bin/env amspython

"""
This is a scripting version of the ReaxFF H2O fitting task.
The goal is to demonstrate ParAMS' low-level functionality, highlighting the fundamental interplay between core classes.
Users are encouraged to extend this script to their own liking.

Running the script a second time will remove all generated files from disk
"""

from scm.params.common.helpers import _cleanup_example_folder as clean
import numpy as np
from scm.plams import from_smiles, Settings
from scm.params import *

def main():
    clean(['opt', 'pes_results.png','training_set.yaml', 'job_collection.yaml', 'parameter_interface.yaml'])
    jc, pes_points = create_job_collection()
    reference_results = run_reference_calculations(jc)
    ds = create_training_set()
    update_training_set_with_reference_results(ds, reference_results)
    pi = create_parameter_interface()
    store_files(jc, ds, pi)
    optimization = run_optimization(jc, ds, pi)
    create_plots(optimization.workdir, pes_points)


def create_job_collection():
    # Create a Job Collection, holding all jobs needed for the parametrization:
    jc = JobCollection()
    # Create a single Job Collection Entry with a H2O system:
    jce = JCEntry(molecule=from_smiles('O'))
    # The task is a PESScan with a H-O bond stretch, ranged [0.85, 1.35] angstrom:
    jce.settings.input.ams.task = 'pesscan'
    pes_points = np.linspace(0.85, 1.35, 11)
    jce.settings.input.ams.pesscan.scancoordinate.npoints = len(pes_points)
    jce.settings.input.ams.pesscan.scancoordinate.distance = f"1 2 {pes_points[0]} {pes_points[-1]}" # atom1 atom2 start end
    # Add the Entry to the Collection:
    jc.add_entry('water', jce)

    return jc, pes_points

def create_training_set():
    # Define the training set. Here, we will just add one entry: The PES of the H-O bond scan of water:
    ds = DataSet()
    ds.add_entry("pes('water')")
    return ds

def run_reference_calculations(jc : JobCollection):
    # The data set is missing reference values. Lets calculate them with PBE:
    pbe = Settings()
    pbe.input.adf.xc.gga = 'pbe'
    # Run all jobs in the Job Collection with the same settings:
    print('Running the reference calculation. This will take a moment ...')
    results = jc.run(pbe)

    return results

def update_training_set_with_reference_results(ds : DataSet, results : dict):
    # Extract the relevant results and populate all reference values in the Data Set:
    ds.calculate_reference(results)

def store_files(jc : JobCollection, ds : DataSet, pi : ReaxFFParameters):
    # Store the Data Set, Job Collection, and Parameter Interface
    # Once stored, the above steps do not need to be reproduced when re-starting an optimization.
    # Instead, the data can be easily loaded from the yaml files.
    # This way possibly expensive reference calculations only need to run once.
    ds.store('training_set.yaml')
    jc.store('job_collection.yaml')
    pi.yaml_store('parameter_interface.yaml')

def create_parameter_interface():
    # Load the ReaxFF force field we want to optimize:
    parameter_interface = ReaxFFParameters('Water2017.ff')
    # First line of the output ffield.ff file
    parameter_interface.header['head'] = "Reparametrization of Water2017.ff"
    # Mark only parameters from the H-O Bonds block for optimization:
    for parameter in parameter_interface:
        parameter.is_active = parameter.metadata['block'] == 'BND' and \
                              (parameter.metadata['atoms'] == ['H', 'O'] or parameter.metadata['atoms'] == ['O', 'H'])

    return parameter_interface

def run_optimization(jc : JobCollection, ds : DataSet, pi : ReaxFFParameters):
    # Choose an optimization algorthm:
    o = CMAOptimizer(sigma=0.1) # sigma range: (0, 1). smaller sigma -> more local sampling

    # Piece it all together and run:
    O = Optimization(
        job_collection=jc,
        data_sets=ds,
        optimizer=o,
        parameter_interface=pi,
        callbacks=[MaxIter(100)], # The MaxIter callback stops an optimization after N evaluations
        )
    O.optimize()
    return O

def create_plots(workdir, pes_points):
    # At this point the optimization is done.
    # All relevant optimization data is stored in `O.workdir`
    # Data with the best parameters is stored in `training_set_results/best`
    # For more information on what is logged, refer to the `Logger()` callback documentation
    # Lets visualize some of it:
    from os.path import join as opj
    import matplotlib.pyplot as plt

    initial_ffield_ds     = DataSet( opj(workdir, 'training_set_results', 'initial', 'data_set_predictions.yaml') )
    initial_predictions   = initial_ffield_ds["pes('water')"].metadata['Prediction']
    optimized_ffield_ds   = DataSet( opj(workdir, 'training_set_results', 'best', 'data_set_predictions.yaml') )
    optimized_predictions = optimized_ffield_ds["pes('water')"].metadata['Prediction']
    reference             = initial_ffield_ds["pes('water')"].reference

    plt.rcParams['font.size'] = 16
    plt.figure(figsize=(8,6))
    plt.plot(pes_points, 2.6255e+03*reference, color='k', label='Reference') # convert hartree to kj/mol
    plt.plot(pes_points, 2.6255e+03*initial_predictions, label='Initial FF')
    plt.plot(pes_points, 2.6255e+03*optimized_predictions, label='Optimized FF')
    plt.ylabel('ΔE [kJ/mol]')
    plt.xlabel('H-O distance [Å]')
    plt.legend()
    plt.savefig('pes_results.png')

if __name__ == '__main__':
    main()
