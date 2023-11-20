# -*- coding: utf-8 -*-

from odoo import models, fields, api


class KomisiKaryawan(models.Model):
    _name = "komisi.karyawan"
    _description = "model for employee comission"

    name = fields.Char(related="nama_komisi")
    nama_komisi = fields.Char(string="Nama Komisi", required=True)
    products = fields.One2many(
        "rule.komisi.karyawan",
        "rule_id",
    )


class RuleKomisiKaryawan(models.Model):
    _name = "rule.komisi.karyawan"
    _description = "model for rule of employee comission"

    rule_id = fields.Many2one(
        "komisi.karyawan",
        readonly=True,
    )
    produk = fields.Many2one(
        "product.template",
        readonly=True,
    )
    persentase_komisi = fields.Integer(
        required=True,
        string="Persentase Komisi",
        default="0",
    )
