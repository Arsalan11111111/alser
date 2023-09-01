# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Alser - Modulos Studio',
    'version': '13.0',
    'category': 'Sale',
    'license': 'OPL-1',
    'author': 'Process Control',
    'website': 'https://www.processcontrol.es/',
    'maintainer': 'Process Control',
    'description': """Modulo que guarda los campos creados por odoo studio""",
    'depends': ['account','purchase','sale','stock','product'],
    'data': [
             'views/account_move_view.xml',
             'views/sale_order_view.xml',
             'views/stock_picking_view.xml',
             'views/product_template_view.xml',
            # 'views/menu_view.xml'
],
    'installable': True,
}
