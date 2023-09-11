from odoo import models, fields, api

class PurchaseOrderLine(models.Model):
    _inherit = "purchase.order.line"

    x_studio_referencia_interna = fields.Char(string='Referencia interna')