# -*- coding: utf-8 -*-

from odoo import api, models, fields


class Produit(models.Model):
    _name = "produit"
    _description = "Model Produit belonging to Module Tbl"

    datemaj_produit = fields.Datetime(
        string="Field Datemaj_produit",
        copy=False,
    )

    name = fields.Char(
        string="Field Name",
        copy=False,
    )

    noaccorderie = fields.Integer(
        string="Field Noaccorderie",
        required=True,
        copy=False,
    )

    nomproduit = fields.Char(
        string="Field Nomproduit",
        copy=False,
    )

    noproduit = fields.Integer(
        string="Field Noproduit",
        required=True,
        copy=False,
    )

    notitre = fields.Integer(
        string="Field Notitre",
        required=True,
        copy=False,
    )

    taxablef = fields.Integer(
        string="Field Taxablef",
        copy=False,
    )

    taxablep = fields.Integer(
        string="Field Taxablep",
        copy=False,
    )

    visible_produit = fields.Integer(
        string="Field Visible_produit",
        copy=False,
    )
