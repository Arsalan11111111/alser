from odoo import models, fields, api

class ProductTemplate(models.Model):
    _inherit = "product.template"

    x_studio_revisado = fields.Boolean(string='Revisado')