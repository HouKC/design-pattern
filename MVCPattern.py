# coding:utf8

# # 简单示例：通信服务
# class Model(object):
#     services = {
#         'email': {'number': 1000, 'price': 2, },
#         'sms': {'number': 1000, 'price': 10, },
#         'voice': {'number': 1000, 'price': 15, },
#     }
#
# class View(object):
#     def list_services(self, services):
#         for svc in services:
#             print(svc, ' ')
#
#     def list_pricing(self, services):
#         for svc in services:
#             print("For", Model.services[svc]['number'], svc, "message you pay $", Model.services[svc]['price'])
#
# class Controller(object):
#     def __init__(self):
#         self.model = Model()
#         self.view = View()
#
#     def get_services(self):
#         services = self.model.services.keys()
#         return self.view.list_services(services)
#
#     def get_pricing(self):
#         services = self.model.services.keys()
#         return self.view.list_pricing(services)
#
# class Client(object):
#     controller = Controller()
#     print("Services Provided:")
#     controller.get_services()
#     print("Pricing for Services:")
#     controller.get_pricing()

# MCV模式实例：Tornado web应用程序
import tornado
import tornado.web
import tornado.ioloop
import tornado.httpserver
import sqlite3

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        query = "select * from task"
        todos = _execute(query)
        self.render('index.html', todos=todos)

class NewHandler(tornado.web.RequestHandler):
    def post(self):
        name = self.get_argument('name', None)
        query = "create table if not exists task (id INTEGER PRIMARY KEY, name TEXT, status NUMERIC)"
        _execute(query)
        query = "insert into task (name, status) values ('%s, %d) " % (name, 1)
        _execute(query)
        self.redirect('/')

    def get(self):
        self.render('new.html')

class UpdateHandler(tornado.web.RequestHandler):
    def get(self, id, status):
        query = "update task set status=%d where id=%s" % (int(status), id)
        _execute(query)
        self.redirect('/')

class DeleteHandler(tornado.web.RequestHandler):
    def get(self, id):
        query = "delete from task where id=%s" % id
        _execute(query)
        self.redirect('/')
