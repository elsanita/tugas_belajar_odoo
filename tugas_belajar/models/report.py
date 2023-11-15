# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class tugas_belajar_report(models.Model):
    _name = 'tugas_belajar.tugas_belajar_report'
    _description = 'tugas_belajar.tugas_belajar_report'

    name = fields.Char(readonly=True, default='New')
    tanggal = fields.Date(required=True)
    karyawan = fields.Many2one('tugas_belajar.tugas_belajar_karyawan', required=True)
    status = fields.Selection([
        ('draft', 'Draft'),
        ('validated', 'Validated')
    ], default='draft', required=True)
    list_report = fields.One2many('tugas_belajar.tugas_belajar_project_report_line', 'report_id')
    
    def action_validate_report(self):
        self.status = 'validated'

    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('tugas_belajar.tugas_belajar_report') or _('New')
        res = super(tugas_belajar_report, self).create(vals)
        return res
    
    def count_projects(self):
        return len(self.list_report)
    
    def get_manager(self):
        return self.karyawan.manager.name
