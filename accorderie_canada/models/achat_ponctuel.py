# -*- coding: utf-8 -*-

from odoo import api, models, fields


class AchatPonctuel(models.Model):
    _name = 'achat.ponctuel'
    _description = 'Model Achat_ponctuel belonging to Module Tbl'

    achatponcfacturer = fields.Integer(
        string='Field Achatponcfacturer',
        copy=False,
    )

    dateachatponctuel = fields.Date(
        string='Field Dateachatponctuel',
        copy=False,
    )

    datemaj_achantponct = fields.Datetime(
        string='Field Datemaj_achantponct',
        copy=False,
    )

    majoration_achatponct = fields.Float(
        string='Field Majoration_achatponct',
        copy=False,
    )

    montantpaiementachatponct = fields.Float(
        string='Field Montantpaiementachatponct',
        copy=False,
    )

    name = fields.Char(
        string='Field Name',
        copy=False,
    )

    noachatponctuel = fields.Integer(
        string='Field Noachatponctuel',
        required=True,
        copy=False,
    )

    nomembre = fields.Integer(
        string='Field Nomembre',
        required=True,
        copy=False,
    )

    taxef_achatponct = fields.Float(
        string='Field Taxef_achatponct',
        copy=False,
    )

    taxep_achatponct = fields.Float(
        string='Field Taxep_achatponct',
        copy=False,
    )
