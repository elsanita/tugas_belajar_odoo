from odoo import models, fields

class PosOrderLine(models.Model):
    _inherit = "pos.order.line"

    cashier_name = fields.Char('Cashier Name')
