# Flask

1.自动发现程序实例
一般来说,在执行flask run命令运行程序前,我们需要提供程序实例所在模块的位置.我们在上面可以
直接运行,是因为Flask会自动探测程序实例,自动探测存在下面这些规则.
* 从当前目录寻找app.py和wsgi.py模块,并从中寻找名为app或application的程序实例
* 从环境变量FLASK_APP对应的值寻找名为app或application的程序实例.
因为我们的程序主模块命名为app.py,所以flask run命令会自动在其中寻找程序实例。如果你的程序主模块是其他名称,比如hello.py,
那么需要设置环境变量FLASK_APP,将包含程序实例的模块名赋值给这个变量.
```bash
$ export FLASK_APP=hello
```