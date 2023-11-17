# -*- coding: utf-8 -*-

from odoo import models, fields, api


class tugas_belajar_sale_inherit(models.Model):
    _inherit = 'sale.order'
    
    karyawan = fields.Many2one('tugas_belajar.tugas_belajar_karyawan', required=True)

    total_komisi = fields.Monetary(string="Total Komisi", store=True, compute='_compute_commisions', tracking=4)


    @api.depends('order_line.price_subtotal', 'order_line.price_tax', 'order_line.price_total')
    def _compute_commisions(self):
        """Compute the total amounts of the SO."""
        for order in self:
            order_lines = order.order_line.filtered(lambda x: not x.display_type)
            
            order.total_komisi = (order.amount_total * 20/100) #TODO: change to multiply with persentase komisi product
