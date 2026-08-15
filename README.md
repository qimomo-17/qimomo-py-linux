## Author
**七魔陌** 
- Email: qimomo.17@qq.com
- 0.1.7 ：
-使用0.1.3版本: from pythonlinux.pythonlinux import *
-本模块是在Python中执行简单Linux命令(实现方法)

主要是作者不会Windows上cmd命令而制作的一个模块
里面有一个su  :
      su qi  #登录用户qi
用之前使用命令
pythonlinux-file-path you_path_file
设置su与histort.txt的位置
比如在 /data/data/pythonlinux/里面有su与histort.txt
命令就是:
pythonlinux-file-path /data/data/pythonlinux/


import pythonlinux
a=linux(linux_file_path='/data/data/pythonlinux/')
a.run('pythonlinux-file-path /data/data/pythonlinux/')
'''
'''python    
import pylinux
a=linux()
a.run('pylinux-file-path /data/data/pythonlinux/')
'''
su文件：(json文件)
{
"用户名":{"密码":"xxx","路径":["xxx","xxx"]}
}
比如:
     用户名： qi
     密码 ：  123
     访问路径： /data/data/pythonlinux/和/data/data/py/app/
就写成
{
"qi":{"密码":"123","路径":["/data/data/pythonlinux/","/data/data/py/app/"]}
}
没密码：
{
"qi":{"密码":"0","路径":["/data/data/pythonlinux/","/data/data/py/app/"]}
}
程序最高访问权限:
{
"qi":{"密码":"123","路径":["0"]}
}
多个：
{
"qi":{"密码":"123","路径":["/data/data/pythonlinux/","/data/data/py/app/"]},
"ii":{"密码":"123","路径":["/data/","/data/data/"]}
}