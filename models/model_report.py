from odoo import models, fields, api

class appschef_reports(models.Model):
    _name = 'appschef.appschef_reports'
    _description = 'model for reports'

    tanggal = fields.Date('Tanggal')
    karyawan = fields.Many2one(comodel_name='appschef.appschef_karyawan')
    status = fields.Selection([('draft', 'Draft'), ('valid', 'Validated')])
