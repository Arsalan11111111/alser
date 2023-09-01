from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = "res.partner"

    x_studio_revisado = fields.Boolean(string='Revisado')
