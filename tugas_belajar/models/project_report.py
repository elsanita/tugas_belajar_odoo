# -*- coding: utf-8 -*-

from odoo import models, fields


class tugas_belajar_project_report_line(models.Model):
    _name = 'tugas_belajar.tugas_belajar_project_report_line'
    _description = 'tugas_belajar.tugas_belajar_project_report_line'

    report_id = fields.Many2one('tugas_belajar.tugas_belajar_report')
    projects = fields.Many2one('tugas_belajar.tugas_belajar_project')
    keterangan = fields.Char()
