import sys
'''
python解释器会搜索当前目录,所有已安装的内置模块和第三方模块
搜索路径放在sys模块的path变量中
'''
print (sys.path)
'''
有两种方法添加搜索目录:
	直接修改sys.path, 
'''
import sys
sys.path.append('./python_learning')
import Get_Ob_Info
print(Get_Ob_Info)


