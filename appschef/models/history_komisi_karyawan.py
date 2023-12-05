# -*- coding: utf-8 -*-

from odoo import models, fields, api


class HistoryKomisiKaryawan(models.Model):
    _name = "history.komisi.karyawan"
    _description = "Model for history of employee commission"

    tanggal = fields.Date()
    nama_karyawan = fields.Char("Nama Karyawan")
    so = fields.Char("SO Sumber")
    currency_id = fields.Many2one(
        "res.currency",
        "Currency",
        default=lambda self: self.env.company.currency_id,
    )
    jumlah_komisi = fields.Monetary(
        string="Jumlah Komisi",
        currency_field="currency_id",
    )
