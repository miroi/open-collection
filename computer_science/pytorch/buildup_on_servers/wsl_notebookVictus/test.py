import torch
from torch import nn # Import the nn sub-module from PyTorch

class NeuralNetwork(nn.Module):  # Neural networks are defined as classes
    def __init__(self):  # Layers and variables are defined in the __init__ method
        super().__init__()  # Must be in every network.
        self.flatten = nn.Flatten()   # Construct a flattening layer.
        self.linear_relu_stack = nn.Sequential(  # Construct a stack of layers.
            nn.Linear(28*28, 512),  # Linear Layers have an input and output shape
            nn.ReLU(),  # ReLU is one of many activation functions provided by nn
            nn.Linear(512, 512),
            nn.ReLU(),
            nn.Linear(512, 10), 
        )

    def forward(self, x):  # This function defines the forward pass.
        x = self.flatten(x)
        logits = self.linear_relu_stack(x)
        return logits
