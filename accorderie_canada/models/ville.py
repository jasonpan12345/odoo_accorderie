# -*- coding: utf-8 -*-

from odoo import api, models, fields


class Ville(models.Model):
    _name = 'ville'
    _description = 'Model Ville belonging to Module Tbl'

    name = fields.Char(
        string='Field Name',
        copy=False,
    )

    noregion = fields.Integer(
        string='Field Noregion',
        copy=False,
    )

    noville = fields.Integer(
        string='Field Noville',
        required=True,
        copy=False,
    )

    ville = fields.Char(
        string='Field Ville',
        copy=False,
    )
