# -*- coding: utf-8 -*-

from odoo import api, models, fields


class RevenuFamilial(models.Model):
    _name = "revenu.familial"
    _description = "Model Revenu_familial belonging to Module Tbl"

    name = fields.Char(
        string="Field Name",
        copy=False,
    )

    norevenufamilial = fields.Integer(
        string="Field Norevenufamilial",
        required=True,
        copy=False,
    )

    revenu = fields.Char(
        string="Field Revenu",
        copy=False,
    )
