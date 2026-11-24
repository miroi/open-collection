import torch
print("torch version:", torch.__version__)          # should show 2.5.1+cu121
print("CUDA available:", torch.cuda.is_available()) # needs to be True
print("CUDA build version:", torch.version.cuda)    # should be 12.1
print("CUDA device:", torch.cuda.get_device_name(0) if torch.cuda.is_available() else "none")
