# -*- coding: utf-8 -*-

from odoo import api, models, fields


class Region(models.Model):
    _name = "region"
    _description = "Model Region belonging to Module Tbl"

    name = fields.Char(
        string="Field Name",
        copy=False,
    )

    noregion = fields.Integer(
        string="Field Noregion",
        required=True,
        copy=False,
    )

    region = fields.Char(
        string="Field Region",
        copy=False,
    )
