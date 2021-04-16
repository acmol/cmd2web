# cmd2web

generate a webserver from cmdline tools

## guide

1. install requirements

    `pip install -r requirements.txt`

2. write a json file as config like this into config.json

        {
            "fs":{
                "ls": {
                    "cmd": "ls {path} -l"
                },
                "du": {
                    "cmd": "du {dir} -sh"
                }
            },
            "process": {
                "ps": {
                    "cmd": "ps ux"
                }
            }
        }

3. run cmd2web.py:
    
    `python cmd2web.py`


4. access your server

        curl 'http://localhost:8080/fs/ls/?path=/'
        curl 'http://localhost:8080/fs/du/?dir=./'
        curl 'http://localhost:8080/process/ps/'


# cmd2web

使用命令行工具生成一个webserver

## 使用方法

1. 安装依赖

    `pip install -r requirements.txt`

2. 写一个配置文件，内容类似下边这个，写到config.json里

        {
            "fs":{
                "ls": {
                    "cmd": "ls {path} -l"
                },
                "du": {
                    "cmd": "du {dir} -sh"
                }
            },
            "process": {
                "ps": {
                    "cmd": "ps ux"
                }
            }
        }

3. 用Python执行cmd2web.py:
    
    `python cmd2web.py`


4. 访问你的服务：

        curl 'http://localhost:8080/fs/ls/?path=/'
        curl 'http://localhost:8080/fs/du/?dir=./'
        curl 'http://localhost:8080/process/ps/'


# 未来计划

当前完成的部分是该工具第一部分，通过简单配置，将命令行转化为一个后端服务。

后续计划将会通过简单配置的方式，生成一个方便易用的交互式前端页面，其中具体的功能将调用现成已经完成的后端来实现。

例如，用户进行如下配置（markdown语法）：

        ## 文件服务
        ### 列出文件
            
        cmd: `ls <path> [-a : 显示隐藏文件]` 
        desc: 用来列出path目录下的文件

        ### 计算文件大小

        cmd: `du <dir> -sh`

        ## 进程服务
        ### 查看进程

        cmd:  `ps ux` 

就可以生成一个网页，有二级选择菜单，选择完之后，例如选择了“列出文件”子菜单， 网页正文位置就会显示出一个输入框，让用户输入path的值，还有一个复选框，让用户选择是否“列出隐藏文件”，并有一个提交按钮，用户提交后就会在下方显示出命令的执行结果。

* 可以定义一些更复杂一些的语法来支持默认值。
* 可以定义语法来支持某参数显示为单选框，选项来源于另一个命令的输出结果。
* 可以定义输出内容如果满足某些格式，则会生成为一种特殊可点击的格式，点击后执行另一个配置好的命令。可配置多个，右击会显示全部待选命令。