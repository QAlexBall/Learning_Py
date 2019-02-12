### Flask-Migrate
1. 采用`db.create_all`在后期修改字段时,不会自动映射到数据库中,需要drop表,然后重新运行,不符合需求.
flask-migrate就是为了解决这个问题,它可以再每次修改模型后,将修改的模型映射到数据库中.
2. 使用`flask_migrate`必须借助`flask_scripts`,这个包的`MigrateCommand`中包含了所有和数据库相关的命令.
3. `flask_migrate`相关命令
* `python manage.py db init`: 初始化一个迁移脚本的环境,只需要执行一次
* `python manage.py db migrate`: 将模型生成迁移文件,只要模型修改,执行此命令
* `python manage.py db upgrate`: 将迁移文件映射到数据库中,生成迁移文件后都需要映射一次.
