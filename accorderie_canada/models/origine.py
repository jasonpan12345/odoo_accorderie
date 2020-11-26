# -*- coding: utf-8 -*-

from odoo import api, models, fields


class Origine(models.Model):
    _name = 'origine'
    _description = 'Model Origine belonging to Module Tbl'

    name = fields.Char(
        string='Field Name',
        copy=False,
    )

    noorigine = fields.Integer(
        string='Field Noorigine',
        required=True,
        copy=False,
    )

    origine = fields.Char(
        string='Field Origine',
        copy=False,
    )
