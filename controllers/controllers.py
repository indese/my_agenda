# -*- coding: utf-8 -*-
from odoo import http

# class MyAgenda(http.Controller):
#     @http.route('/my_agenda/my_agenda/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/my_agenda/my_agenda/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('my_agenda.listing', {
#             'root': '/my_agenda/my_agenda',
#             'objects': http.request.env['my_agenda.my_agenda'].search([]),
#         })

#     @http.route('/my_agenda/my_agenda/objects/<model("my_agenda.my_agenda"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('my_agenda.object', {
#             'object': obj
#         })