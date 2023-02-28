import torch

### Creating Tensors in Pytorch ###

# something like tensor([0.2763, 0.8352, 0.7327])
x = torch.rand(3) 

# something like tensor([[0.8887, 0.4721, 0.1790],
#                        [0.9012, 0.6621, 0.6375]])
x = torch.rand(2, 3) 

img_size_tensor = torch.rand(size=(3, 100, 100)) # 3 => (R, G, B)

# tensor([[0., 0., 0.],
#        [0., 0., 0.]])
zeros = torch.zeros(size=(2, 3))

# tensor([[1., 1., 1., 1.],
#        [1., 1., 1., 1.],
#        [1., 1., 1., 1.]])
ones = torch.ones(size=(3, 4))

# random tensor with range eg. tensor([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
x = torch.arange(0, 10) 

# zeros-like eg. tensor([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
zeros_like = torch.zeros_like(input=x)
