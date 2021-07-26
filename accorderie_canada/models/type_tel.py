# -*- coding: utf-8 -*-

from odoo import api, models, fields


class TypeTel(models.Model):
    _name = "type.tel"
    _description = "Model Type_tel belonging to Module Tbl"

    name = fields.Char(
        string="Field Name",
        copy=False,
    )

    notypetel = fields.Integer(
        string="Field Notypetel",
        required=True,
        copy=False,
    )

    typetel = fields.Char(
        string="Field Typetel",
        copy=False,
    )
