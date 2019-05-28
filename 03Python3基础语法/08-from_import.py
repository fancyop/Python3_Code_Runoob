from sys import argv,path	#导入特定的成员

print('=================Python from import=============')
print('path:',path)	#因为已经导入了path成员，所以此处引用是不需要加sys.path



'''
从某个模块中导入某个函数,格式为： from somemodule import somefunction

从某个模块中导入多个函数,格式为： from somemodule import firstfunc, secondfunc, thirdfunc

将某个模块中的全部函数导入，格式为： from somemodule import *
'''
