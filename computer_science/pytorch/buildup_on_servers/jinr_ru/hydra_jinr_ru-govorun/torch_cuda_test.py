#
# test on torch cuda 
#
import torch

print("torch.cuda.get_device_name() ?",torch.cuda.get_device_name() )
print("torch.cuda.is_available ?", torch.cuda.is_available())

print(" torch.version.cuda ?", torch.version.cuda  )

print("torch.tensor([1.0, 2.0]) ? ",torch.tensor([1.0, 2.0]))
print("torch.tensor([1.0, 2.0]).cuda() ?", torch.tensor([1.0, 2.0]).cuda())

# matric mult

x = torch.randn(1024, 1024).cuda()
y = torch.matmul(x, x)
print(" y=x*x, y.shape ? ", y.shape)
print(" y=x*x, y.device ? ", y.device)
