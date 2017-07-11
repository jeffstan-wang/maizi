#coding=utf-8
import os
if os.geteuid()==0:
    pass
else:
    print("当前用户非root,请切换到root用户执行此程序！")
    sys.exit()