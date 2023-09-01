from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = "sale.order"

    x_ObservacionesPedido = fields.Char(string='Observaciones Pedido',tracking=True)
    x_studio_servido_parcialmente = fields.Selection([('Si','Servido parcialmente'),('No servido','No servido'),('No','Completado'),(u'Preparar envío',u'Preparar envío'),('Perdido','Perdido'),('Reembolsado','Reembolsado'),('Servido fungible','Completado fungible'),('Aplazado por cliente','Aplazado por cliente')],string='Estado Pedido',tracking=True)