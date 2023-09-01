from odoo import models, fields, api

class ProductSupplierInfo(models.Model):
    _inherit = "product.supplierinfo"

    x_studio_obs_2 = fields.Text(string='Obs. 2')
    x_studio_obs_2_1 = fields.Text(string='Obs. 2')
    x_studio_obs_2_2 = fields.Text(string='Obs. 2')
    x_minimo_notas = fields.Text(string='Obs. 2')
