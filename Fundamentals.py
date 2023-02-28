import torch

# torch.tensor()

## scalar
scalar = torch.tensor(5)
print(scalar) # prints tensor(5)
print(scalar.ndim) # ndim is similar to the array dimensions in programming. prints 0 because tensor(5) is just a number
print(scalar.item()) # prints 5

## vector
vector = torch.tensor([4, 2])
print(vector) # prints tensor([4, 2])
print(vector.ndim) # prints 1
print(vector.shape) # prints torch.Size([2])

## MATRIX
MATRIX = torch.tensor([[5, 1], [4, 2]])
print(MATRIX) # prints tensor([[5, 1],
              #                [4, 2]])
print(MATRIX.ndim) # prints 2
print(MATRIX[0]) # prints tensor([5, 1])
print(MATRIX.shape) # prints torch.Size([2, 2])

# TENSOR
TENSOR = torch.tensor([[[1, 2, 3],
                        [3, 6, 9],
                        [2, 5, 4]]])
print(TENSOR[0][1]) # prints tensor([3, 6, 9])
print(TENSOR.shape) # prints torch.Size([1, 3, 3])

