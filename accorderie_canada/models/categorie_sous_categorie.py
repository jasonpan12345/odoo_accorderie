# -*- coding: utf-8 -*-

from odoo import api, models, fields


class CategorieSousCategorie(models.Model):
    _name = 'categorie.sous.categorie'
    _description = 'Model Categorie_sous_categorie belonging to Module Tbl'

    approuver = fields.Integer(
        string='Field Approuver',
        copy=False,
    )

    description = fields.Char(
        string='Field Description',
        copy=False,
    )

    name = fields.Char(
        string='Field Name',
        copy=False,
    )

    nocategorie = fields.Integer(
        string='Field Nocategorie',
        copy=False,
    )

    nocategoriesouscategorie = fields.Integer(
        string='Field Nocategoriesouscategorie',
        required=True,
        copy=False,
    )

    nooffre = fields.Integer(
        string='Field Nooffre',
        copy=False,
    )

    nosouscategorie = fields.Char(
        string='Field Nosouscategorie',
        copy=False,
    )

    supprimer = fields.Integer(
        string='Field Supprimer',
        copy=False,
    )

    titreoffre = fields.Char(
        string='Field Titreoffre',
        copy=False,
    )
