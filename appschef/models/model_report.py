# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AppschefReports(models.Model):
    _name = "reports"
    _description = "model for reports"

    name = fields.Char(related="report_number")
    report_number = fields.Char(readonly=True, default="DR - XXXX")
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

    @api.model
    def create(self, vals):
        vals["report_number"] = self.env["ir.sequence"].next_by_code("report.number")
        res = super(AppschefReports, self).create(vals)
        return res

    def total_project(self):
        existing_project = []
        for data in self.projects:
            existing_project.append(data.project_name)
        projects = {data for data in existing_project}

        return len(projects)

    def get_manager_name(self):
        return self.karyawan.manager.name


class ReportsLine(models.Model):
    _name = "reports.line"
    _description = "model for reports line"

    project_name = fields.Many2one(
        "project",
        string="Nama Project",
    )
    report = fields.Many2one("reports")
    keterangan = fields.Char("Keterangan")
