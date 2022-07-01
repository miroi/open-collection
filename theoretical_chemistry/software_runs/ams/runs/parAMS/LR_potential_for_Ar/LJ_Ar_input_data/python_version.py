#!/usr/bin/env amspython
from scm.params import *

# Load the parameter interface for LJ
params = LennardJonesParameters()

# Load the Job Collection
jc = JobCollection('job_collection.yaml')

# Load the training set
ts = DataSet('training_set.yaml')

# Set the optimizer, parallel levels and timeout
optimizer = Scipy('Nelder-Mead')
parallel = ParallelLevels(parametervectors=1, jobs=1)
callbacks = [Timeout(60*2)] # 2 min

# Run the example
O = Optimization(
    job_collection=jc,
    data_sets=ts,
    parameter_interface=params,
    optimizer=optimizer,
    callbacks=callbacks,
    parallel=parallel,
    workdir='optimization',
)
O.optimize()
