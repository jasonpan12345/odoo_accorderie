# -*- coding: utf-8 -*-

from odoo import api, models, fields


class CommandeMembre(models.Model):
    _name = "commande.membre"
    _description = "Model Commande_membre belonging to Module Tbl"

    archivesoustotal = fields.Float(
        string="Field Archivesoustotal",
        copy=False,
    )

    archivetotmajoration = fields.Float(
        string="Field Archivetotmajoration",
        copy=False,
    )

    archivetottxfed = fields.Float(
        string="Field Archivetottxfed",
        copy=False,
    )

    archivetottxprov = fields.Float(
        string="Field Archivetottxprov",
        copy=False,
    )

    cmdconfirmer = fields.Integer(
        string="Field Cmdconfirmer",
        copy=False,
    )

    coutunitaireajour = fields.Integer(
        string="Field Coutunitaireajour",
        copy=False,
    )

    datecmdmb = fields.Datetime(
        string="Field Datecmdmb",
        copy=False,
    )

    datefacture = fields.Date(
        string="Field Datefacture",
        copy=False,
    )

    datemaj_cmdmembre = fields.Datetime(
        string="Field Datemaj_cmdmembre",
        copy=False,
    )

    facturer = fields.Integer(
        string="Field Facturer",
        copy=False,
    )

    montantpaiement = fields.Float(
        string="Field Montantpaiement",
        copy=False,
    )

    name = fields.Char(
        string="Field Name",
        copy=False,
    )

    nocommande = fields.Integer(
        string="Field Nocommande",
        required=True,
        copy=False,
    )

    nocommandemembre = fields.Integer(
        string="Field Nocommandemembre",
        required=True,
        copy=False,
    )

    nomembre = fields.Integer(
        string="Field Nomembre",
        required=True,
        copy=False,
    )

    numrefmembre = fields.Integer(
        string="Field Numrefmembre",
        copy=False,
    )
