
import torch

print("\n hello, torch.cuda.is_available ?", torch.cuda.is_available() )

print("\n hello, torch.cuda.get_device_name ?", torch.cuda.get_device_name() )

print("\n hello, torch.cuda.get_arch_list ?", torch.cuda.get_arch_list() )

#  https://pytorch.org/get-started/locally/#windows-verification
print("\n torch.rand(5, 3) :"); x = torch.rand(5, 3); print (x)
