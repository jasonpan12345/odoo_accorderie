# -*- coding: utf-8 -*-

from odoo import api, models, fields


class Categorie(models.Model):
    _name = 'categorie'
    _description = 'Model Categorie belonging to Module Tbl'

    approuver = fields.Integer(
        string='Field Approuver',
        copy=False,
    )

    name = fields.Char(
        string='Field Name',
        copy=False,
    )

    nocategorie = fields.Integer(
        string='Field Nocategorie',
        required=True,
        copy=False,
    )

    supprimer = fields.Integer(
        string='Field Supprimer',
        copy=False,
    )

    titrecategorie = fields.Char(
        string='Field Titrecategorie',
        copy=False,
    )
