from odoo import models, fields, api

class AccountMove(models.Model):
    _inherit = "account.move"

    x_studio_fecha_de_cobro = fields.Date(string='Fecha de cobro')
