========================
Build the Neural Network
========================

https://docs.pytorch.org/tutorials/beginner/basics/buildmodel_tutorial.html#build-the-neural-network

(myenv) miroi@MIRO:~/work/projects/open-collection/computer_science/pytorch/buildup_on_servers/wsl_notebookVictus/tests/build_nn/.pip install torchvision
.
.
Successfully installed torch-2.9.1 torchvision-0.24.1 triton-3.5.1


(myenv) miroi@MIRO:~/work/projects/open-collection/computer_science/pytorch/buildup_on_servers/wsl_notebookVictus/tests/build_nn/.python build_nn.py
Using cuda device



run
~~~

(myenv) miroi@MIRO:~/work/projects/open-collection/computer_science/pytorch/buildup_on_servers/wsl_notebookVictus/tests/build_nn/.python build_nn.py
Using cuda device
NeuralNetwork(
  (flatten): Flatten(start_dim=1, end_dim=-1)
  (linear_relu_stack): Sequential(
    (0): Linear(in_features=784, out_features=512, bias=True)
    (1): ReLU()
    (2): Linear(in_features=512, out_features=512, bias=True)
    (3): ReLU()
    (4): Linear(in_features=512, out_features=10, bias=True)
  )
)
Predicted class: tensor([9], device='cuda:0')

