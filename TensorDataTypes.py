import torch

float_32_tensor = torch.tensor([1,2,3,4,5], 
                               # float32 by default
                               dtype=None,
                               # cpu by default
                               device=None,
                               # False by default
                               requires_grad=False)

float_16_tensor = float_32_tensor.type(torch.float16) # converts float32 to float16

print(float_32_tensor * float_16_tensor)