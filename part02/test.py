
import sys
import os

_dir = os.getcwd()

# 追加路径的方式
# 一、修改sys.path
# 不用append，避免sys前面的path有重名的
# sys.path.append(_dir+'\\test_mods')

# sys.path.insert(0, _dir+'\\test_mods')
# print(sys.path)
# import mod1
# print(mod1.Aname)

# 二、修改环境变量  名字 PYTHONPATH

# 三、添加.pth文件，在这些路径里添加
import site
print(site.getsitepackages())