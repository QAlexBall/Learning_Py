import tornado.web

class IndexHandler(tornado.web.RequestHandler):

    def get(self):
        query = "select * from task"
        todos = super._execute(query)
        self.render('index.html', todos=todos)

class NewHandler(tornado.web.RequestHandler):

    def post(self):
        name = self.get_argument('name', None)
        query = "create table if not exists task (id INTEGER PRIMARY KEY, name TEXT, status NUMERIC) "
        super._execute(query)
        query = "insert into task (name, status) values ('%s', %d) " % (name, 1)
        super._execute(query)
        self.redirect('/')

    def get(self):
        self.render('new.html')

class UpdateHandler(tornado.web.RequestHandler):

    def get(self, id, status):
        query = "update task set status=% where id=%s" % (int(status), id)
        super._execute(query)
        self.redirect('/')

class DeleteHandler(tornado.web.RequestHandler):

    def get(self, id):
        query = "delete from task where id=%s" % id
        super._execute(query)
        self.redirect('/')





