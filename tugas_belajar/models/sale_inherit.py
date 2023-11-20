# -*- coding: utf-8 -*-

from odoo import models, fields, api


class tugas_belajar_sale_inherit(models.Model):
    _inherit = 'sale.order'
    
    penjual = fields.Many2one('tugas_belajar.tugas_belajar_karyawan', required=True)

    jumlah_komisi = fields.Monetary(string="Jumlah Komisi", store=True, compute='_compute_commisions', tracking=4, default=0.0)


    @api.depends('order_line.price_subtotal', 'order_line.price_tax', 'order_line.price_total')
    def _compute_commisions(self):
        rule_komisi_karyawan_product_records = self.env['tugas_belajar.tugas_belajar_rule_komisi_karyawan_product'].search([])
        
        order_lines = self.order_line

        self.jumlah_komisi = 0.0

        for product in order_lines:
            for komisi_product in rule_komisi_karyawan_product_records:
                if komisi_product.product.id == product.product_template_id.id:
                    self.jumlah_komisi = self.jumlah_komisi + (product.price_unit * komisi_product.persentase/100)

    def write(self, vals):
        res = super(tugas_belajar_sale_inherit, self).write(vals)
        self.env['tugas_belajar.tugas_belajar_history_komisi_karyawan'].create({
            'so': self.name,
            'karyawan': self.penjual.name,
            'jumlah_komisi': self.jumlah_komisi,
            'date': self.create_date
        })

        return res
