from odoo import models, fields, api


class appschef_reports(models.Model):
    _name = "appschef.appschef_reports"
    _description = "model for reports"

    tanggal = fields.Date("Tanggal")
    karyawan = fields.Many2one(comodel_name="appschef.appschef_karyawan")
    status = fields.Selection(
        [
            ("draft", "Draft"),
            ("valid", "Validated"),
        ],
        default="draft",
    )
    projects = fields.One2many(
        comodel_name="appschef.reports_line",
        inverse_name="project_name",
        string="Reports",
    )

    def validate_report(self):
        self.status = "valid"


class ReportsLine(models.Model):
    _name = "appschef.reports_line"
    _description = "model for reports line"

    project_name = fields.Many2one(
        comodel_name="appschef.appschef_project",
        string="Nama Project",
    )
    report = fields.Many2one(comodel_name="appschef.appschef_reports")
    keterangan = fields.Char("Keterangan")
