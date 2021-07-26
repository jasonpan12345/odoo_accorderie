# -*- coding: utf-8 -*-

from odoo import api, models, fields


class DemandeService(models.Model):
    _name = "demande.service"
    _description = "Model Demande_service belonging to Module Tbl"

    approuve = fields.Integer(
        string="Field Approuve",
        copy=False,
    )

    datedebut = fields.Date(
        string="Field Datedebut",
        copy=False,
    )

    datefin = fields.Date(
        string="Field Datefin",
        copy=False,
    )

    description = fields.Char(
        string="Field Description",
        copy=False,
    )

    name = fields.Char(
        string="Field Name",
        copy=False,
    )

    noaccorderie = fields.Integer(
        string="Field Noaccorderie",
        copy=False,
    )

    nodemandeservice = fields.Integer(
        string="Field Nodemandeservice",
        required=True,
        copy=False,
    )

    nomembre = fields.Integer(
        string="Field Nomembre",
        copy=False,
    )

    supprimer = fields.Integer(
        string="Field Supprimer",
        copy=False,
    )

    titredemande = fields.Char(
        string="Field Titredemande",
        copy=False,
    )

    transmit = fields.Integer(
        string="Field Transmit",
        copy=False,
    )
