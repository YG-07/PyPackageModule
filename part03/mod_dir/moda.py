
nameA = 'aaa'
print(nameA)
print('当前模块名：', __name__)

# 包内导入
from . import modb
print(modb.nameB)

from .sub_mods import modc
print(modc.nameC)