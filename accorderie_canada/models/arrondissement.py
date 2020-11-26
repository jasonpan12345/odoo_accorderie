# -*- coding: utf-8 -*-

from odoo import api, models, fields


class Arrondissement(models.Model):
    _name = 'arrondissement'
    _description = 'Model Arrondissement belonging to Module Tbl'

    arrondissement = fields.Char(
        string='Field Arrondissement',
        copy=False,
    )

    name = fields.Char(
        string='Field Name',
        copy=False,
    )

    noarrondissement = fields.Integer(
        string='Field Noarrondissement',
        required=True,
        copy=False,
    )

    noville = fields.Integer(
        string='Field Noville',
        copy=False,
    )
