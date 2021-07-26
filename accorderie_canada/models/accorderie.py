# -*- coding: utf-8 -*-

from odoo import api, models, fields


class Accorderie(models.Model):
    _name = "accorderie"
    _description = "Model Accorderie belonging to Module Tbl"

    adresseaccorderie = fields.Char(
        string="Field Adresseaccorderie",
        copy=False,
    )

    codepostalaccorderie = fields.Char(
        string="Field Codepostalaccorderie",
        copy=False,
    )

    courrielaccorderie = fields.Char(
        string="Field Courrielaccorderie",
        copy=False,
    )

    datemaj_accorderie = fields.Datetime(
        string="Field Datemaj_accorderie",
        copy=False,
    )

    grpachat_accordeur = fields.Integer(
        string="Field Grpachat_accordeur",
        copy=False,
    )

    grpachat_admin = fields.Integer(
        string="Field Grpachat_admin",
        copy=False,
    )

    messageaccueil = fields.Text(
        string="Field Messageaccueil",
        copy=False,
    )

    messagegrpachat = fields.Text(
        string="Field Messagegrpachat",
        copy=False,
    )

    name = fields.Char(
        string="Field Name",
        copy=False,
    )

    noaccorderie = fields.Integer(
        string="Field Noaccorderie",
        required=True,
        copy=False,
    )

    noarrondissement = fields.Integer(
        string="Field Noarrondissement",
        copy=False,
    )

    nocartier = fields.Integer(
        string="Field Nocartier",
        copy=False,
    )

    nom = fields.Char(
        string="Field Nom",
        copy=False,
    )

    nomcomplet = fields.Char(
        string="Field Nomcomplet",
        required=True,
        copy=False,
    )

    nonvisible = fields.Integer(
        string="Field Nonvisible",
        required=True,
        copy=False,
    )

    noregion = fields.Integer(
        string="Field Noregion",
        required=True,
        copy=False,
    )

    noville = fields.Integer(
        string="Field Noville",
        required=True,
        copy=False,
    )

    telaccorderie = fields.Char(
        string="Field Telaccorderie",
        copy=False,
    )

    telecopieuraccorderie = fields.Char(
        string="Field Telecopieuraccorderie",
        copy=False,
    )

    url_logoaccorderie = fields.Char(
        string="Field Url_logoaccorderie",
        copy=False,
    )

    url_public_accorderie = fields.Char(
        string="Field Url_public_accorderie",
        copy=False,
    )

    url_transac_accorderie = fields.Char(
        string="Field Url_transac_accorderie",
        copy=False,
    )
