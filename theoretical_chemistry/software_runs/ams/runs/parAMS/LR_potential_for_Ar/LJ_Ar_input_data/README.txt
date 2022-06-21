This example illustrates how to fit a Lennard-Jones potential.

To run this example, open a terminal and run

"$AMSBIN/params" optimize

which uses the settings in params.conf.py, *or*

"$AMSBIN/amspython" ./python_version.py

which uses the settings in python_version.py.

It should finish in less than a minute. The best parameters are stored in
optimization/trainingset_results/best/lj_parameters.txt

You can also plot some results. Go to the
optimization/trainingset_results/best/scatter_plots directory, and run

$AMSBIN/params plot forces.txt

This creates a correlation plot between the predicted forces and reference forces.

For more information about this example, see the online documentation.
