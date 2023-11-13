# -*- coding: utf-8 -*-

from odoo import models, fields


class tugas_belajar_report(models.Model):
    _name = 'tugas_belajar.tugas_belajar_report'
    _description = 'tugas_belajar.tugas_belajar_report'

    tanggal = fields.Date()
    karyawan = fields.Many2one('tugas_belajar.tugas_belajar_karyawan')
    status = fields.Selection([
        ('draft', 'Draft'),
        ('validated', 'Validated')
    ], default='draft', required=True)
    list_report = fields.One2many('tugas_belajar.tugas_belajar_project_report_line', 'report_id')
    
    def action_validate_report(self):
        self.status = 'validated'
