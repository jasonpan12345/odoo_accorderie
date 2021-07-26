# -*- coding: utf-8 -*-

from odoo import api, models, fields


class Mensualite(models.Model):
    _name = "mensualite"
    _description = "Model Mensualite belonging to Module Tbl"

    id_mensualite = fields.Integer(
        string="Field Id_mensualite",
        required=True,
        copy=False,
    )

    id_pret = fields.Integer(
        string="Field Id_pret",
        required=True,
        copy=False,
    )

    name = fields.Char(
        string="Field Name",
        copy=False,
    )
