# -*- coding: utf-8 -*-

from odoo import models, fields, api


class tugas_belajar_project(models.Model):
    _name = 'tugas_belajar.tugas_belajar_project'
    _description = 'tugas_belajar.tugas_belajar_project'

    name = fields.Char()
    teknologi = fields.Selection([('java', 'Java'), ('python', 'Python'), ('swift', 'Swift')], required=True, default='java')
    tipe_project = fields.Selection([('fixed_bid', 'Fixed Bid'), ('dedicated_team', 'Dedicated Team')], required=True, default='fixed_bid')

    # @api.depends('value')
    # def _value_pc(self):
    #     for record in self:
    #         record.value2 = float(record.value) / 100
