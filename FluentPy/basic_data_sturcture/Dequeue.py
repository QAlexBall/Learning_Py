# 双向队列和其他形式的队列
"""
利用.append和.pop方法,可以把列表当做栈或者队列来使用.
但是删除列表的地铁一个元素(亦或是在第一个元素之前添加一个元素)之类的操作是很耗时的,因为这些操作会牵扯到移动列表里的所有元素

collections.deque类(双向队列)是一个线程安全,可以快速从两端添加或者删除元素的数据类型.
"""
from collections import deque
dq = deque(range(10), maxlen=10) # maxlen是一个可选参数, 代表这个队列可以容纳的元素的数量,而且一旦设定,这个属性就不能修改了
print(dq)
# output: deque([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], maxlen=10)

dq.rotate(3) 			# 队列的旋转操作接受一个参数n,当n > 0时,队列的最右边的n个元素会被移动到队列的左边.
						# 						 当n < 0时,队列的最左边的n个元素会被移动到队列的右边.
print(dq)
# output: deque([7, 8, 9, 0, 1, 2, 3, 4, 5, 6], maxlen=10)	
dq.rotate(-4)
print(dq)
# output: deque([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], maxlen=10)

dq.appendleft(-1) 	# 当试图对一个已满(len(d) == d.maxlen)的队列做尾部添加操作的时候,它头部的元素会被删除掉
print(dq)
# output: deque([-1, 1, 2, 3, 4, 5, 6, 7, 8, 9], maxlen=10)

dq.extend([11, 22, 33])
print(dq)
# output: deque([3, 4, 5, 6, 7, 8, 9, 11, 22, 33], maxlen=10)

dq.extendleft([10, 20, 30, 40])	# extendleft(iter)方法会把迭代器里的元素逐个添加到双向队列的左边,因此迭代器里元素会逆序得出现在队列里
print(dq)
# output: deque([40, 30, 20, 10, 3, 4, 5, 6, 7, 8], maxlen=10)

dq1 = deque([1, 2, 3])
dq2 = deque([1, 3, 5])
print(dq1 + dq2)