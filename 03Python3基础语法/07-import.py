import sys
print('=================Python import mode===============')
print('命令行参数：')
for i in sys.argv:
	print(i)
print('\n python 路径为',sys.path)


'''
在 python 用 import 或者 from...import 来导入相应的模块。

将整个模块(somemodule)导入，格式为： import somemodule
'''
