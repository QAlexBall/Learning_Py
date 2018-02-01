s = '1'
n = int(s)
print(10 / n)

# python -m pdb debugging_pdb_test.py 
# 命令l查看代码
# 命令n可以单步执行代码输入命令 p + 变量名 查看变量
# 输入q结束调试, 退出程序


# pdb.set_trace()
import pdb
s = '0'
n = int(s)
pdb.set_trace()
print(10 / n)