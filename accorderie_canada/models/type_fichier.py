# -*- coding: utf-8 -*-

from odoo import api, models, fields


class TypeFichier(models.Model):
    _name = 'type.fichier'
    _description = 'Model Type_fichier belonging to Module Tbl'

    datemaj_typefichier = fields.Datetime(
        string='Field Datemaj_typefichier',
        required=True,
        copy=False,
    )

    id_typefichier = fields.Integer(
        string='Field Id_typefichier',
        required=True,
        copy=False,
    )

    name = fields.Char(
        string='Field Name',
        copy=False,
    )

    typefichier = fields.Char(
        string='Field Typefichier',
        copy=False,
    )
