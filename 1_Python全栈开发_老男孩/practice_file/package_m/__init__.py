print("这是即将要导入的包".center(100, '='))

# 绝对导入
# from practice_file.package_m.mm1 import func1
# from practice_file.package_m.mm2 import func2
# from practice_file.package_m.mm3 import func3
# from practice_file.package_m.son_m.mm4 import func4, func5


# 相对导入
from .mm1 import func1
from .mm2 import func2
from .mm3 import func3
from .son_m.mm4 import func4,func5