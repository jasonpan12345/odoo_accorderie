# -*- coding: utf-8 -*-

from odoo import api, models, fields


class Titre(models.Model):
    _name = "titre"
    _description = "Model Titre belonging to Module Tbl"

    datemaj_titre = fields.Datetime(
        string="Field Datemaj_titre",
        copy=False,
    )

    name = fields.Char(
        string="Field Name",
        copy=False,
    )

    notitre = fields.Integer(
        string="Field Notitre",
        required=True,
        copy=False,
    )

    titre = fields.Char(
        string="Field Titre",
        copy=False,
    )

    visible_titre = fields.Integer(
        string="Field Visible_titre",
        copy=False,
    )
