from odoo import models, fields, api

class StockPicking(models.Model):
    _inherit = "stock.picking"


    x_studio_transportista = fields.Selection([('STI','STI'),('Alser Esport','Alser Esport')], string='Transportista',tracking=True)