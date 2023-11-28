# -*- coding: utf-8 -*-

from odoo import models, fields


class tugas_belajar_rule_komisi_karyawan(models.Model):
    _name = 'tugas_belajar.tugas_belajar_rule_komisi_karyawan'
    _description = 'tugas_belajar.tugas_belajar_rule_komisi_karyawan'

    name = fields.Char(required=True, string="Nama Komisi")

    products = fields.One2many('tugas_belajar.tugas_belajar_rule_komisi_karyawan_product', 'rule_komisi_id')

    def add_rule(self):
        view_id = self.env.ref('tugas_belajar.tugas_belajar_rule_komisi_karyawan_wizard').id
        
        return {
            'name': "Wizard Rule Komisi Karyawan",
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'tugas_belajar.tugas_belajar_rule_komisi_karyawan_wizard',
            'views': [(view_id, 'form')],
            'view_id': view_id,
            'target': 'new',
        }
    
class tugas_belajar_rule_komisi_karyawan_product(models.Model):
    _name = 'tugas_belajar.tugas_belajar_rule_komisi_karyawan_product'
    _description = 'tugas_belajar.tugas_belajar_rule_komisi_karyawan_product'

    rule_komisi_id = fields.Many2one('tugas_belajar.tugas_belajar_rule_komisi_karyawan', readonly=True)
    product = fields.Many2one('product.template', readonly=True)
    persentase = fields.Float(readonly=True)
