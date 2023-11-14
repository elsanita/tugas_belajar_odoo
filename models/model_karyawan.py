# -*- coding: utf-8 -*-

from odoo import models, fields, api


class appschef_karyawan(models.Model):
    _name = "appschef.appschef_karyawan"
    _description = "model for karyawan"

    name = fields.Char("Name")
    jabatan = fields.Selection(
        [
            ("ceo", "CEO"),
            ("cto", "CTO"),
            ("hr", "HR"),
            ("account", "Accounting"),
            ("em", "Engineer Manager"),
            ("dev", "Developer"),
        ]
    )
    manager = fields.Many2one(comodel_name="appschef.appschef_karyawan")
    jenis_kelamin = fields.Selection(
        [
            ("lakilaki", "Laki-laki"),
            ("perempuan", "Perempuan"),
        ]
    )
    tanggal_lahir = fields.Date("Tanggal Lahir")
    project = fields.Many2many(
        comodel_name="appschef.appschef_project",
        relation="karyawan_project_relation",
    )
