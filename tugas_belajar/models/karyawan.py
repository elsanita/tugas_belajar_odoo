# -*- coding: utf-8 -*-

from odoo import models, fields, api


class tugas_belajar_karyawan(models.Model):
    _name = 'tugas_belajar.tugas_belajar_karyawan'
    _description = 'tugas_belajar.tugas_belajar_karyawan'

    name = fields.Char()
    jabatan = fields.Selection([('manajer_pemasaran', 'Manajer Pemasaran'), ('manajer_ti', 'Manajer Teknologi Informasi'), ('manajer_sumber_daya', 'Manajer Sumber Daya')], required=True, default='manajer_pemasaran')
    manager = fields.Many2one(comodel_name='tugas_belajar.tugas_belajar_karyawan')
    jenis_kelamin = fields.Selection([('pria', 'Pria'), ('wanita', 'Wanita')], required=True, default='pria')
    tanggal_lahir = fields.Date()
    project = fields.Many2many(
        comodel_name='tugas_belajar.tugas_belajar_project',
        relation='project_karyawan_rel',
    )

    # @api.depends('value')
    # def _value_pc(self):
    #     for record in self:
    #         record.value2 = float(record.value) / 100
