# -*- coding: utf-8 -*-
from odoo import http

# class A18alejandrodvInmo(http.Controller):
#     @http.route('/a18alejandrodv_inmo/a18alejandrodv_inmo/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/a18alejandrodv_inmo/a18alejandrodv_inmo/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('a18alejandrodv_inmo.listing', {
#             'root': '/a18alejandrodv_inmo/a18alejandrodv_inmo',
#             'objects': http.request.env['a18alejandrodv_inmo.a18alejandrodv_inmo'].search([]),
#         })

#     @http.route('/a18alejandrodv_inmo/a18alejandrodv_inmo/objects/<model("a18alejandrodv_inmo.a18alejandrodv_inmo"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('a18alejandrodv_inmo.object', {
#             'object': obj
#         })