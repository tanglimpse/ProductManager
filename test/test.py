from PIL import Image
import os
import string


for filename in os.listdir(iconpath):              #listdir的参数是文件夹的路径
    img = Image.open(iconpath+filename)
    img.show()

    iconpath="\guest\好"
a=os.getcwd()+iconpath
os.startfile(str(a))

import subprocess
cmd=r'"D:\pythonn\pj\untitled\ItemManager\guest.py" "-h"'
ps = subprocess.run(r"python guest.py"); # 执行cmd命令
ps.wait();#让程序阻塞
