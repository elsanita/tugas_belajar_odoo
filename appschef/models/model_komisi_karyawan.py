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

    def tambah_rule(self):
        view_id = self.env.ref("appschef.form_rule_komisi_karyawan_wizard").id
        context = {
            "rule_id": self.id,
        }

        return {
            "name": "Rule Komisi Karyawan Wizard",
            "type": "ir.actions.act_window",
            "view_type": "form",
            "view_mode": "form",
            "res_model": "rule.komisi.karyawan.wizard",
            "views": [(view_id, "form")],
            "view_id": view_id,
            "target": "new",
            "context": context,
        }


class RuleKomisiKaryawan(models.Model):
    _name = "rule.komisi.karyawan"
    _description = "model for rule of employee comission"

    rule_id = fields.Many2one(
        "komisi.karyawan",
        readonly=True,
    )
    produk = fields.Many2one(
        "product.template",
    )
    persentase_komisi = fields.Float(
        required=True,
        string="Persentase Komisi",
        default="0.0",
    )
