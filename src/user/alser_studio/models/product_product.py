from odoo import models, fields, api

class ProductProduct(models.Model):
    _inherit = "product.product"

    x_studio_revisado = fields.Boolean(string='Revisado')
    x_descripcion_corta = fields.Text(string=u'Descripción corta')