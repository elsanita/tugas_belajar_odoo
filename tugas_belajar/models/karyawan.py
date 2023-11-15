# -*- coding: utf-8 -*-

from odoo import models, fields


class tugas_belajar_karyawan(models.Model):
    _name = 'tugas_belajar.tugas_belajar_karyawan'
    _description = 'tugas_belajar.tugas_belajar_karyawan'

    name = fields.Char(required=True)
    jabatan = fields.Selection([
        ('manajer_pemasaran', 'Manajer Pemasaran'),
        ('manajer_ti', 'Manajer Teknologi Informasi'),
        ('manajer_sumber_daya', 'Manajer Sumber Daya')
    ], default='manajer_pemasaran', required=True)
    manager = fields.Many2one('tugas_belajar.tugas_belajar_karyawan')
    jenis_kelamin = fields.Selection([
        ('pria', 'Pria'),
        ('wanita', 'Wanita')
    ], default='pria', required=True)
    tanggal_lahir = fields.Date()
    project = fields.Many2many('tugas_belajar.tugas_belajar_project', 'project_karyawan_rel')
