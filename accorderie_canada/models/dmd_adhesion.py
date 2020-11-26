# -*- coding: utf-8 -*-

from odoo import api, models, fields


class DmdAdhesion(models.Model):
    _name = 'dmd.adhesion'
    _description = 'Model Dmd_adhesion belonging to Module Tbl'

    courriel = fields.Char(
        string='Field Courriel',
        copy=False,
    )

    datemaj = fields.Datetime(
        string='Field Datemaj',
        copy=False,
    )

    enattente = fields.Integer(
        string='Field Enattente',
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

    nodmdadhesion = fields.Integer(
        string='Field Nodmdadhesion',
        required=True,
        copy=False,
    )

    nom = fields.Char(
        string='Field Nom',
        copy=False,
    )

    poste = fields.Char(
        string='Field Poste',
        copy=False,
    )

    prenom = fields.Char(
        string='Field Prenom',
        copy=False,
    )

    supprimer = fields.Integer(
        string='Field Supprimer',
        copy=False,
    )

    telephone = fields.Char(
        string='Field Telephone',
        copy=False,
    )

    transferer = fields.Integer(
        string='Field Transferer',
        copy=False,
    )
