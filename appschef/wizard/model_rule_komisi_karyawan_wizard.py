# -*- coding: utf-8 -*-

from odoo import models, fields, api


class RuleKomisiKaryawanWizard(models.TransientModel):
    _name = "rule.komisi.karyawan.wizard"
    _description = "model for wizard of employee comission"

    rule_id = fields.Many2one(
        "komisi.karyawan",
        readonly=True,
    )
    produk = fields.Many2one(
        "product.template",
        required=True,
    )
    persentase_komisi = fields.Integer(
        required=True,
        string="Persentase Komisi",
        default="0",
    )

    def add_rule(self):
        rule_id = self.env["komisi.karyawan"].browse(self.env.context.get("active_id"))
        # rule_komisi = self.env["rule.komisi.karyawan"].create(
        #     {
        #         "rule_id": rule_id.id,
        #         "produk": self.produk.id,
        #         "persentase_komisi": self.persentase_komisi,
        #     }
        # )

        # self.env["komisi.karyawan"].write({"products": [(4, rule_komisi.id)]})
        rule_id.write(
            {
                "products": [
                    (
                        0,
                        0,
                        {
                            "rule_id": rule_id.id,
                            "produk": self.produk.id,
                            "persentase_komisi": self.persentase_komisi,
                        },
                    )
                ]
            }
        )
