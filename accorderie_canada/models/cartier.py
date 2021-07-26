# -*- coding: utf-8 -*-

from odoo import api, models, fields


class Cartier(models.Model):
    _name = "cartier"
    _description = "Model Cartier belonging to Module Tbl"

    cartier = fields.Char(
        string="Field Cartier",
        copy=False,
    )

    name = fields.Char(
        string="Field Name",
        copy=False,
    )

    noarrondissement = fields.Integer(
        string="Field Noarrondissement",
        required=True,
        copy=False,
    )

    nocartier = fields.Integer(
        string="Field Nocartier",
        required=True,
        copy=False,
    )
