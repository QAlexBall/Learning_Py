from __future__ import print_function
import torch

x = torch.empty(5, 3)

x = torch.rand(5, 3)
#
x = torch.zeros(5, 3, dtype=torch.long)

x = torch.tensor([5.5, 3])

x = x.new_ones(5, 3, dtype=torch.double)

x = torch.rand_like(x, dtype=torch.float)
print(x)
#  print(x.size())

# add
y = torch.rand(5, 3)
#  print(x + y)

result = torch.empty(5, 3)
torch.add(x, y, out=result)
#  print(result)

y.add_(x)
#  print(y)

print(x[:, 1])

# change shape use torch.view
x = torch.randn(4, 4)
y = x.view(16)
z = x.view(-1, 2) # tht size -1 is inferred from other dimensions
print(x.size(), y.size(), z.size())

# 如果是仅包含一个元素的tensor，可以使用.item()来得到对应的python数值
x = torch.randn(1)
print(x)
print(x.item())

# bridge to numpy
# change torch.tensor to numpy
a = torch.ones(5)
print(a)

b = a.numpy()
print(b)

a.add_(1)
print(a)
print(b)

# change numpy to torch.tensor
import numpy as np
a = np.ones(5)
b = torch.from_numpy(a)
np.add(a, 1, out=a)
print(a)
print(b)

# tensor in cuda
# tensor could use .to move to any device
if torch.cuda.is_available():
    device = torch.device("cuda")
    y = torch.onse_like(x, device=device)
    x = x.to(device)
    z = x + y
    print(z)
    print(z.to("cpu", torch.double))


