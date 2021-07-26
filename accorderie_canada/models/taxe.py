# -*- coding: utf-8 -*-

from odoo import api, models, fields


class Taxe(models.Model):
    _name = "taxe"
    _description = "Model Taxe belonging to Module Tbl"

    name = fields.Char(
        string="Field Name",
        copy=False,
    )

    notaxe = fields.Integer(
        string="Field Notaxe",
        required=True,
        copy=False,
    )

    notaxefed = fields.Char(
        string="Field Notaxefed",
        copy=False,
    )

    notaxepro = fields.Char(
        string="Field Notaxepro",
        copy=False,
    )

    tauxmajoration = fields.Float(
        string="Field Tauxmajoration",
        copy=False,
    )

    tauxtaxefed = fields.Float(
        string="Field Tauxtaxefed",
        copy=False,
    )

    tauxtaxepro = fields.Float(
        string="Field Tauxtaxepro",
        copy=False,
    )
