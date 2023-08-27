### The training_set, job_collection, and parameter_interface variables contain paths to the corresponding .yaml files
training_set = 'training_set.yaml'   
job_collection = 'job_collection.yaml'
parameter_interface = 'parameter_interface.yaml'

### Define an optimizer for the optimization task. Use either a CMAOptimizer or Scipy
#optimizer = CMAOptimizer(sigma=0.1, popsize=10, minsigma=5e-4) 
optimizer = Scipy(method='Nelder-Mead')

### run the optimization in serial
parallel = ParallelLevels(parametervectors=1, jobs=1, processes=1)

### Stop the optimization after 2 minutes if it has not finished with the timeout variable.
timeout = 120
