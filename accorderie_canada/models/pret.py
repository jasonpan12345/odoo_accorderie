# -*- coding: utf-8 -*-

from odoo import api, models, fields


class Pret(models.Model):
    _name = "pret"
    _description = "Model Pret belonging to Module Tbl"

    datecomitepret = fields.Datetime(
        string="Field Datecomitepret",
        copy=False,
    )

    datedemandepret = fields.Datetime(
        string="Field Datedemandepret",
        copy=False,
    )

    datemaj_pret = fields.Datetime(
        string="Field Datemaj_pret",
        copy=False,
    )

    datepret = fields.Datetime(
        string="Field Datepret",
        copy=False,
    )

    id_pret = fields.Integer(
        string="Field Id_pret",
        required=True,
        copy=False,
    )

    montantaccorder = fields.Float(
        string="Field Montantaccorder",
        copy=False,
    )

    montantdemande = fields.Float(
        string="Field Montantdemande",
        copy=False,
    )

    name = fields.Char(
        string="Field Name",
        copy=False,
    )

    nbremois = fields.Integer(
        string="Field Nbremois",
        copy=False,
    )

    nbrepaiement = fields.Integer(
        string="Field Nbrepaiement",
        copy=False,
    )

    nomembre = fields.Integer(
        string="Field Nomembre",
        required=True,
        copy=False,
    )

    nomembre_intermediaire = fields.Integer(
        string="Field Nomembre_intermediaire",
        copy=False,
    )

    nomembre_responsable = fields.Integer(
        string="Field Nomembre_responsable",
        required=True,
        copy=False,
    )

    note = fields.Text(
        string="Field Note",
        copy=False,
    )

    raisonemprunt = fields.Text(
        string="Field Raisonemprunt",
        copy=False,
    )

    recommandation = fields.Text(
        string="Field Recommandation",
        copy=False,
    )

    si_pretaccorder = fields.Integer(
        string="Field Si_pretaccorder",
        copy=False,
    )

    tautinteretannuel = fields.Float(
        string="Field Tautinteretannuel",
        copy=False,
    )
