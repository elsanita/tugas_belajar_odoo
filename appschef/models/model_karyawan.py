# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AppschefKaryawan(models.Model):
    _name = "karyawan"
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
    manager = fields.Many2one(comodel_name="karyawan")
    jenis_kelamin = fields.Selection(
        [
            ("lakilaki", "Laki-laki"),
            ("perempuan", "Perempuan"),
        ]
    )
    tanggal_lahir = fields.Date("Tanggal Lahir")
    project = fields.Many2many(
        comodel_name="project",
        relation="karyawan_project_relation",
    )
