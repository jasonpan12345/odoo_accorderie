# -*- coding: utf-8 -*-

from odoo import api, models, fields


class TypeCommunication(models.Model):
    _name = "type.communication"
    _description = "Model Type_communication belonging to Module Tbl"

    name = fields.Char(
        string="Field Name",
        copy=False,
    )

    notypecommunication = fields.Integer(
        string="Field Notypecommunication",
        required=True,
        copy=False,
    )

    typecommunication = fields.Char(
        string="Field Typecommunication",
        copy=False,
    )
