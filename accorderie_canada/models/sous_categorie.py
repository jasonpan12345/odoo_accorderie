# -*- coding: utf-8 -*-

from odoo import api, models, fields


class SousCategorie(models.Model):
    _name = "sous.categorie"
    _description = "Model Sous_categorie belonging to Module Tbl"

    approuver = fields.Integer(
        string="Field Approuver",
        copy=False,
    )

    name = fields.Char(
        string="Field Name",
        copy=False,
    )

    nocategorie = fields.Integer(
        string="Field Nocategorie",
        required=True,
        copy=False,
    )

    nosouscategorie = fields.Char(
        string="Field Nosouscategorie",
        required=True,
        copy=False,
    )

    supprimer = fields.Integer(
        string="Field Supprimer",
        copy=False,
    )

    titresouscategorie = fields.Char(
        string="Field Titresouscategorie",
        copy=False,
    )
