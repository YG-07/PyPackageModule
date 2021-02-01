#-*- coding:utf-8 -*-

# import Tool
# # 导入包会自动调用init
# import package1
# import package1.Amod
# # 使用as对包或模块取别名
# import package1.subpack.Submod as sub1


# # 使用from导入一个包的多个模块，注意：最后尽量是最后一个包第一层能看见的
# from package1 import Amod, Bmod
# # from package1 import subpack
# from package1.subpack import sub2
# # from还能从模块里导入部分资源（变量、函数等等）
# from Tool import run as TRun
# # from package1.Amod import aaa

# 包和模块里可以使用__all__ = []指定导出的模块和变量
from package1 import *
from Tool import *

# print(Tool.num)
# print(package1.Amod.aaa)
# print(sub1.subname)
# print(dir(package1))
# print(package1.name_mod.name)
# print(Bmod.bbb, Amod.aaa)
# print(sub2.name)
# TRun()

print(num)
run()
a=Person()
a.eat()