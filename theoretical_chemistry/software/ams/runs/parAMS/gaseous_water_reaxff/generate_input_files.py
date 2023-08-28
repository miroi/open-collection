#!/usr/bin/env amspython
"""
    This scripts runs a bond scan for a water molecule using ADF, and adds the bond scan to a ParAMS training set.
    If you do not have an ADF license, you can choose a different reference engine like DFTB or ForceField.

    Copy this file to an empty directory and run it like this:
    $AMSBIN/amspython generate_input_files.py

    That will produce the training_set.yaml, job_collection.yaml, job_collection_engines.yaml, and parameter_interface.yaml files.
    It will also produce a directory called plams_workdir, which contains the results of the ADF calculation.
"""

from scm.plams import *
from scm.params import *

def run_reference():
    # choose a reference engine. If you do not have a license for ADF, use DFTB, ForceField, or another engine for which you have the license.
    # from_smiles('O') creates an H2O molecule
    job = AMSJob.from_input(name='H2O_pesscan', molecule=from_smiles('O'), text_input='''
    Task PESScan
    PESScan
        # Scan O-H bond length between 0.85 and 1.35 angstrom (11 points)
        ScanCoordinate
            nPoints 11
            Distance 1 2 0.85 1.35
        End
    End
    Engine ADF
        XC
            GGA PBE
        End
    EndEngine
    #Engine ForceField
    #EndEngine
    #Engine DFTB
    #EndEngine
    ''')
    job.run()
    return job

def import_results():
    # If you ran the PESScan job via the graphical user interface, set
    #pesscan_job = '/path/to/ams.rkf'
    # Otherwise, the below line runs the reference job
    pesscan_job = run_reference()
    ri = ResultsImporter(settings={'units': {'energy': 'kcal/mol'}})
    ri.add_singlejob(pesscan_job, task='PESScan', properties={
        'pes': {
            # apply a weights scheme (optional). 
            # This sets the weight for the larger energies (very short or very long bond distance) to smaller numbers.
            # stdev is the standard deviation of the Gaussian in energy units (here kcal/mol)
            'weights_scheme': WeightsSchemeGaussian(normalization=11.0, stdev=20.0)
        }
    })
    ri.store(binary=False, backup=False, store_settings=False)

def create_parameter_interface():
    # start from the Water2017.ff force field
    parameter_interface = ReaxFFParameters('Water2017.ff', bounds_scale=1.2)
    parameter_interface.header['head'] = "Reparametrization of Water2017.ff"
    # only activate the "Standard" bond parameters for O-H
    for p in parameter_interface:
        p.is_active = (p.metadata['block'] == 'BND') and \
                      (p.metadata['category'] == 'Standard') and \
                      (p.metadata['atoms'] == ['H', 'O'] or p.metadata['atoms'] == ['O', 'H'])
    parameter_interface.yaml_store('parameter_interface.yaml')

def main():
    init()
    import_results()
    create_parameter_interface()
    finish()

if __name__ == '__main__':
    main()

