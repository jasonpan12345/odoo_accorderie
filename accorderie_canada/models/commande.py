# -*- coding: utf-8 -*-

from odoo import api, models, fields


class Commande(models.Model):
    _name = 'commande'
    _description = 'Model Commande belonging to Module Tbl'

    commandetermine = fields.Integer(
        string='Field Commandetermine',
        copy=False,
    )

    datecmddebut = fields.Date(
        string='Field Datecmddebut',
        copy=False,
    )

    datecmdfin = fields.Date(
        string='Field Datecmdfin',
        copy=False,
    )

    datecueillette = fields.Date(
        string='Field Datecueillette',
        copy=False,
    )

    datemaj_cmd = fields.Datetime(
        string='Field Datemaj_cmd',
        copy=False,
    )

    majoration = fields.Float(
        string='Field Majoration',
        copy=False,
    )

    name = fields.Char(
        string='Field Name',
        copy=False,
    )

    nocommande = fields.Integer(
        string='Field Nocommande',
        required=True,
        copy=False,
    )

    nopointservice = fields.Integer(
        string='Field Nopointservice',
        required=True,
        copy=False,
    )

    norefcommande = fields.Integer(
        string='Field Norefcommande',
        copy=False,
    )

    taxefcommande = fields.Float(
        string='Field Taxefcommande',
        copy=False,
    )

    taxepcommande = fields.Float(
        string='Field Taxepcommande',
        copy=False,
    )
