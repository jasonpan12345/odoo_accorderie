# -*- coding: utf-8 -*-

from odoo import api, models, fields


class FournisseurProduitPointservice(models.Model):
    _name = "fournisseur.produit.pointservice"
    _description = (
        "Model Fournisseur_produit_pointservice belonging to Module Tbl"
    )

    coutunitaire = fields.Float(
        string="Field Coutunitaire",
        copy=False,
    )

    datemaj_fournprodptserv = fields.Datetime(
        string="Field Datemaj_fournprodptserv",
        copy=False,
    )

    name = fields.Char(
        string="Field Name",
        copy=False,
    )

    nofournisseurproduit = fields.Integer(
        string="Field Nofournisseurproduit",
        required=True,
        copy=False,
    )

    nofournisseurproduitpointservice = fields.Integer(
        string="Field Nofournisseurproduitpointservice",
        required=True,
        copy=False,
    )

    nopointservice = fields.Integer(
        string="Field Nopointservice",
        required=True,
        copy=False,
    )

    qtestokeacc = fields.Integer(
        string="Field Qtestokeacc",
        copy=False,
    )
