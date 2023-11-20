# -*- coding: utf-8 -*-

from odoo import models, fields


class tugas_belajar_history_komisi_karyawan(models.Model):
    _name = 'tugas_belajar.tugas_belajar_history_komisi_karyawan'
    _description = 'tugas_belajar.tugas_belajar_history_komisi_karyawan'

    date = fields.Date(string="Tanggal")
    karyawan = fields.Char(string="Nama Karyawan")
    so = fields.Char(string="SO Sumber")
    currency_id = fields.Many2one('res.currency', 'Currency', default=lambda self: self.env.user.company_id.currency_id.id, required=True)
    jumlah_komisi = fields.Float()
