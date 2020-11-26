# -*- coding: utf-8 -*-

from odoo import api, models, fields


class Fichier(models.Model):
    _name = 'fichier'
    _description = 'Model Fichier belonging to Module Tbl'

    datemaj_fichier = fields.Datetime(
        string='Field Datemaj_fichier',
        copy=False,
    )

    id_fichier = fields.Integer(
        string='Field Id_fichier',
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

    noaccorderie = fields.Integer(
        string='Field Noaccorderie',
        required=True,
        copy=False,
    )

    nomfichieroriginal = fields.Char(
        string='Field Nomfichieroriginal',
        required=True,
        copy=False,
    )

    nomfichierstokage = fields.Char(
        string='Field Nomfichierstokage',
        required=True,
        copy=False,
    )

    si_accorderielocalseulement = fields.Integer(
        string='Field Si_accorderielocalseulement',
        copy=False,
    )

    si_admin = fields.Integer(
        string='Field Si_admin',
        copy=False,
    )

    si_disponible = fields.Integer(
        string='Field Si_disponible',
        copy=False,
    )
