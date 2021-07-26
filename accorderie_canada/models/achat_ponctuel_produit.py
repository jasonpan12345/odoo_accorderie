# -*- coding: utf-8 -*-

from odoo import api, models, fields


class AchatPonctuelProduit(models.Model):
    _name = "achat.ponctuel.produit"
    _description = "Model Achat_ponctuel_produit belonging to Module Tbl"

    coutunit_achatponctprod = fields.Float(
        string="Field Coutunit_achatponctprod",
        copy=False,
    )

    datemaj_achatponcproduit = fields.Datetime(
        string="Field Datemaj_achatponcproduit",
        copy=False,
    )

    name = fields.Char(
        string="Field Name",
        copy=False,
    )

    noachatponctuel = fields.Integer(
        string="Field Noachatponctuel",
        required=True,
        copy=False,
    )

    noachatponctuelproduit = fields.Integer(
        string="Field Noachatponctuelproduit",
        required=True,
        copy=False,
    )

    nofournisseurproduit = fields.Integer(
        string="Field Nofournisseurproduit",
        required=True,
        copy=False,
    )

    prixfacturer_achatponctprod = fields.Float(
        string="Field Prixfacturer_achatponctprod",
        copy=False,
    )

    qteacheter = fields.Float(
        string="Field Qteacheter",
        copy=False,
    )

    sitaxablef_achatponctprod = fields.Integer(
        string="Field Sitaxablef_achatponctprod",
        copy=False,
    )

    sitaxablep_achatponctprod = fields.Integer(
        string="Field Sitaxablep_achatponctprod",
        copy=False,
    )
