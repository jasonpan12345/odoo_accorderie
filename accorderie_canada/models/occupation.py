# -*- coding: utf-8 -*-

from odoo import api, models, fields


class Occupation(models.Model):
    _name = 'occupation'
    _description = 'Model Occupation belonging to Module Tbl'

    name = fields.Char(
        string='Field Name',
        copy=False,
    )

    nooccupation = fields.Integer(
        string='Field Nooccupation',
        required=True,
        copy=False,
    )

    occupation = fields.Char(
        string='Field Occupation',
        copy=False,
    )
