# -*- coding: utf-8 -*-
# from odoo import http


# class Appschef(http.Controller):
#     @http.route('/appschef/karyawan', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/appschef/karyawan/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('appschef.listing', {
#             'root': '/appschef/karyawan',
#             'objects': http.request.env['appschef.karyawan'].search([]),
#         })

#     @http.route('/appschef/karyawan/objects/<model("appschef.karyawan"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('appschef.object', {
#             'object': obj
#         })
