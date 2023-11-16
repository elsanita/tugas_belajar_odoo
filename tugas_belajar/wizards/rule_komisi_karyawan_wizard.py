# -*- coding: utf-8 -*-

from odoo import models, fields


class tugas_belajar_rule_komisi_karyawan_wizard(models.TransientModel):
    _name = 'tugas_belajar.tugas_belajar_rule_komisi_karyawan_wizard'
    _description = 'tugas_belajar.tugas_belajar_rule_komisi_karyawan_wizard'

    rule_komisi_id = fields.Many2one('tugas_belajar.tugas_belajar_rule_komisi_karyawan', readonly=True)
    product = fields.Many2one('product.template')
    persentase = fields.Float()

    def save(self):
        rule_komisi_id = self.env['tugas_belajar.tugas_belajar_rule_komisi_karyawan'].browse(self.env.context.get('active_id'))
        self.env['tugas_belajar.tugas_belajar_rule_komisi_karyawan_product'].create({
            'rule_komisi_id': rule_komisi_id,
            'product': self.product,
            'persentase': self.persentase,
        })
