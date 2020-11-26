# -*- coding: utf-8 -*-

from odoo import api, models, fields


class Provenance(models.Model):
    _name = 'provenance'
    _description = 'Model Provenance belonging to Module Tbl'

    name = fields.Char(
        string='Field Name',
        copy=False,
    )

    noprovenance = fields.Integer(
        string='Field Noprovenance',
        required=True,
        copy=False,
    )

    provenance = fields.Char(
        string='Field Provenance',
        copy=False,
    )
