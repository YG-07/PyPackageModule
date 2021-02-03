
# 包内导入
# 绝对导入和相对导入

# 1.绝对
# import moda
# from moda import nameA

# 2.相对
# 在包内 from .xxx import xxx

# 最外层包叫：顶级包(top-level package)

from mod_dir import moda

# 不是模块，当前文件的__name__是__main__
# if __name__=="__main__": 因此这算是入口函数
print(__name__)
