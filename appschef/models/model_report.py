# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AppschefReports(models.Model):
    _name = "reports"
    _description = "model for reports"

    name = fields.Char(related="karyawan.name")
    tanggal = fields.Date("Tanggal")
    karyawan = fields.Many2one("karyawan")
    status = fields.Selection(
        [
            ("draft", "Draft"),
            ("valid", "Validated"),
        ],
        default="draft",
    )
    projects = fields.One2many(
        "reports.line",
        "report",
        string="Reports",
    )

    def validate_report(self):
        self.status = "valid"


class ReportsLine(models.Model):
    _name = "reports.line"
    _description = "model for reports line"

    project_name = fields.Many2one(
        "project",
        string="Nama Project",
    )
    report = fields.Many2one("reports")
    keterangan = fields.Char("Keterangan")
