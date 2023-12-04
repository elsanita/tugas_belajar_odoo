# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AccountMove(models.Model):
    _inherit = "account.move"

    offers = fields.One2many(
        "account.move.penawaran",
        "invoice_id",
    )

    @api.model
    def save_offer(self, invoice_id, data_offering):
        invoiceId = self.env["account.move"].browse(invoice_id)
        arrayOffer = []
        for data in data_offering:
            arrayOffer.append(
                (
                    0,
                    0,
                    {
                        "invoice_id": invoiceId,
                        "produk": data["productId"],
                        "offer": data["offering"],
                    },
                )
            )

        invoiceId.write({"offers": arrayOffer})

        # invoiceId.write(
        #     {
        #         "offers": [
        #             (
        #                 0,
        #                 0,
        #                 {
        #                     "invoice_id": invoice_id,
        #                     "produk": produk,
        #                     "offer": offer,
        #                 },
        #             )
        #         ]
        #     }
        # )


class AccountMovePenawaran(models.Model):
    _name = "account.move.penawaran"

    invoice_id = fields.Many2one("account.move")
    produk = fields.Many2one(
        "product.product",
        string="Product",
    )
    currency_id = fields.Many2one(
        "res.currency",
        "Currency",
        default=lambda self: self.env.company.currency_id,
    )
    offer = fields.Monetary(
        string="Offer",
        currency_field="currency_id",
    )
