# -*- coding: utf-8 -*-
from odoo import http


class TugasBelajar(http.Controller):
    @http.route('/tugas_belajar/tugas_belajar_project', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/tugas_belajar/tugas_belajar_project/objects', auth='public')
    def list(self, **kw):
        return http.request.render('tugas_belajar_project.listing', {
            'root': '/tugas_belajar/tugas_belajar_project',
            'objects': http.request.env['tugas_belajar.tugas_belajar_project'].search([]),
        })

    @http.route('/tugas_belajar/tugas_belajar_project/objects/<model("tugas_belajar.tugas_belajar_project"):obj>', auth='public')
    def object(self, obj, **kw):
        return http.request.render('tugas_belajar_project.object', {
            'object': obj
        })
    
    #KARYAWAN
    @http.route('/tugas_belajar/tugas_belajar_karyawan', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/tugas_belajar/tugas_belajar_karyawan/objects', auth='public')
    def list(self, **kw):
        return http.request.render('tugas_belajar_karyawan.listing', {
            'root': '/tugas_belajar/tugas_belajar_karyawan',
            'objects': http.request.env['tugas_belajar.tugas_belajar_karyawan'].search([]),
        })

    @http.route('/tugas_belajar/tugas_belajar_karyawan/objects/<model("tugas_belajar.tugas_belajar_karyawan"):obj>', auth='public')
    def object(self, obj, **kw):
        return http.request.render('tugas_belajar_karyawan.object', {
            'object': obj
        })
