# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = "sale.order"

    penjual = fields.Many2one("karyawan", required=True)
    jumlah_komisi = fields.Monetary(
        string="Jumlah Komisi",
        store=True,
        compute="compute_commision",
        tracking=4,
        defailt=0,
    )

    @api.depends(
        "order_line.price_subtotal",
        "penjual",
    )
    def compute_commision(self):
        for order in self:
            rules_komisi_karyawan = self.env["rule.komisi.karyawan"].search(
                [("rule_id", "=", self.penjual.komisi.id)]
            )

            order_lines = order.order_line.filtered(lambda x: not x.display_type)

            order.jumlah_komisi = 0.0

            for product in order_lines:
                for komisi_product in rules_komisi_karyawan:
                    if komisi_product.produk.id == product.product_template_id.id:
                        self.jumlah_komisi = self.jumlah_komisi + (
                            product.price_subtotal
                            * (komisi_product.persentase_komisi / 100)
                        )

    def action_confirm(self):
        data = super(SaleOrder, self).action_confirm()
        self.env["history.komisi.karyawan"].create(
            {
                "tanggal": self.date_order,
                "nama_karyawan": self.penjual.name,
                "so": self.name,
                "jumlah_komisi": self.jumlah_komisi,
            }
        )
        return data
