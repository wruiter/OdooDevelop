# -*- coding: utf-8 -*-
# from odoo import http


# class Ftpimages(http.Controller):
#     @http.route('/ftpimages/ftpimages/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ftpimages/ftpimages/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('ftpimages.listing', {
#             'root': '/ftpimages/ftpimages',
#             'objects': http.request.env['ftpimages.ftpimages'].search([]),
#         })

#     @http.route('/ftpimages/ftpimages/objects/<model("ftpimages.ftpimages"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ftpimages.object', {
#             'object': obj
#         })
