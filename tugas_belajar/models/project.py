# -*- coding: utf-8 -*-

from odoo import models, fields


class tugas_belajar_project(models.Model):
    _name = 'tugas_belajar.tugas_belajar_project'
    _description = 'tugas_belajar.tugas_belajar_project'

    name = fields.Char()
    teknologi = fields.Selection([
        ('java', 'Java'),
        ('python', 'Python'),
        ('swift', 'Swift')
    ], default='java', required=True)
    tipe_project = fields.Selection([
        ('fixed_bid', 'Fixed Bid'),
        ('dedicated_team', 'Dedicated Team')
    ], default='fixed_bid', required=True)
