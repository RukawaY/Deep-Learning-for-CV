import torch

x = torch.tensor([[2,3], [1,4]])

x_another = x.view(4, 1)

print(x)