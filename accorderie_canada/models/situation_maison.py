# -*- coding: utf-8 -*-

from odoo import api, models, fields


class SituationMaison(models.Model):
    _name = "situation.maison"
    _description = "Model Situation_maison belonging to Module Tbl"

    name = fields.Char(
        string="Field Name",
        copy=False,
    )

    nosituationmaison = fields.Integer(
        string="Field Nosituationmaison",
        required=True,
        copy=False,
    )

    situation = fields.Char(
        string="Field Situation",
        copy=False,
    )
