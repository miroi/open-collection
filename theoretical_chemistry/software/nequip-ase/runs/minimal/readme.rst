nequip minimal example
=======================

https://github.com/mir-group/nequip?tab=readme-ov-file#basic-network-training

training
~~~~~~~~

nequip-train -h

nequip-train minimal.yaml  

see  nequip-train_minima.logfile
milias@DESKTOP-7OTLCGO:~/work/git-projects/open-collection/theoretical_chemistry/software/nequip-ase/runs/minimal/.ls
benchmark_data/  minimal.yaml  nequip-train_minima.logfile  readme.rst  results/


evaluating
~~~~~~~~~~~
nequip-evaluate --help

milias@DESKTOP-7OTLCGO:~/work/git-projects/open-collection/theoretical_chemistry/software/nequip-ase/runs/minimal/.nequip-evaluate --train-dir  results/aspirin/minimal
Using device: cuda
Please note that _all_ machine learning models running on CUDA hardware are generally somewhat nondeterministic and that this can manifest in small, generally unimportant variation in the final test errors.
Loading model...
    loaded model
Loading original dataset...
Loaded dataset specified in config.yaml.
Using origial training dataset (1000 frames) minus training (5 frames) and validation frames (5 frames), yielding a test set size of 990 frames.
Starting...
100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 990/990 [00:04<00:00, 207.94it/s]
f_mae = 14.2858 | f_rmse = 20.5197

--- Final result: ---
               f_mae =  14.285797
              f_rmse =  20.519672
               f_mae =  14.285797
              f_rmse =  20.519672

deploying
~~~~~~~~~
nequip-deploy --help

milias@DESKTOP-7OTLCGO:~/work/git-projects/open-collection/theoretical_chemistry/software/nequip-ase/runs/minimal/.nequip-deploy build --train-dir results/aspirin/minimal   deployed_model.pth

milias@DESKTOP-7OTLCGO:~/work/git-projects/open-collection/theoretical_chemistry/software/nequip-ase/runs/minimal/.ls -lt deployed_model.pth
-rw-r--r-- 1 milias milias 610146 Nov 15 17:01 deployed_model.pth




