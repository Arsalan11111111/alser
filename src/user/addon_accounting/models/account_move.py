# -*- coding: utf-8 -*-
from odoo import api, models, fields, _
from odoo.exceptions import UserError

class AccountMove(models.Model):
    _inherit = ['account.move']

    def write(self, values):
        if 'x_studio_fecha_documento' in values.keys():
            values['date'] = values['x_studio_fecha_documento']
        res = super().write(values)
        return res

    @api.model
    def create(self, values):
        if 'x_studio_fecha_documento' in values.keys():
            values['date'] = values['x_studio_fecha_documento']
        res = super().create(values)
        return res

    # we override this method to avoid to be able to delete records that have been published.
    def unlink(self):
        for move in self:
            if move.state == 'posted':
                raise UserError(_("You cannot delete a posted entry."))
            else:
                move.line_ids.unlink()
        return models.Model.unlink(self)
