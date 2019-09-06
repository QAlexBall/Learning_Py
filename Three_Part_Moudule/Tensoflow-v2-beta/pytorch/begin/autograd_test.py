# 所有神经网络的核心是autograd包
# tensor
# torch.Tensor是这个包的核心.ifrequires_grad is True,那么它会追踪对于该张量的所有操作。
# 当完成计算后可以通过调用.backend()，来自动计算所有梯度。这个张量的所有梯度将会自动累加到.grad属性
#  为了防止跟踪历史记录（和使用内存），可以将代码块包装在 with torch.no_grad(): 中。
#  在评估模型时特别有用，因为模型可能具有 requires_grad = True 的可训练的参数，但是我们不需要在此过程中对他们进行梯度计算。
#  还有一个类对于autograd的实现非常重要：Function。
#  Tensor 和 Function 互相连接生成了一个无圈图(acyclic graph)，它编码了完整的计算历史。
#  每个张量都有一个 .grad_fn 属性，该属性引用了创建 Tensor 自身的Function（除非这个张量是用户手动创建的，即这个张量的 grad_fn 是 None ）。
#  如果需要计算导数，可以在 Tensor 上调用 .backward()。如果 Tensor 是一个标量（即它包含一个元素的数据），
#  则不需要为 backward() 指定任何参数，但是如果它有更多的元素，则需要指定一个 gradient 参数，该参数是形状匹配的张量。


import torch
x = torch.ones(2, 2, requires_grad=True)
print(x)

y = x + 2
print(y)
print(y.grad_fn)

z = y * y * 3
out = z.mean()
print(z, out)

a = torch.randn(2, 2)
a = ((a * 3) / (a - 1))
print(a.requires_grad)
a.requires_grad_(True)  # requires_grad_ could change tensor's requires_grad flag
print(a.requires_grad)

b = (a * a).sum()
print(b.grad_fn)

# gradient
out.backward()
print(x.grad)

x = torch.randn(3, requires_grad=True)
y = x * 2
while y.data.norm() < 1000:
    y = y * 2
print(y)

v = torch.tensor([0.1, 1.0, 0.0001], dtype=torch.float)
y.backward(v)
print(x.grad)


print(x.requires_grad)
print(( x ** 2).requires_grad)

with torch.no_grad():
    print((x ** 2).requires_grad)

