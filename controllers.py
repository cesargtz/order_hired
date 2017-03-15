# -*- coding: utf-8 -*-
from openerp import http

# class OrderHired(http.Controller):
#     @http.route('/order_hired/order_hired/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/order_hired/order_hired/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('order_hired.listing', {
#             'root': '/order_hired/order_hired',
#             'objects': http.request.env['order_hired.order_hired'].search([]),
#         })

#     @http.route('/order_hired/order_hired/objects/<model("order_hired.order_hired"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('order_hired.object', {
#             'object': obj
#         })