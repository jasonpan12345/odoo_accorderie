# -*- coding: utf-8 -*-

from odoo import api, models, fields


class FournisseurProduitCommande(models.Model):
    _name = "fournisseur.produit.commande"
    _description = "Model Fournisseur_produit_commande belonging to Module Tbl"

    coutunitprevu = fields.Float(
        string="Field Coutunitprevu",
        copy=False,
    )

    datemaj_fournprodcommande = fields.Datetime(
        string="Field Datemaj_fournprodcommande",
        copy=False,
    )

    disponible = fields.Integer(
        string="Field Disponible",
        copy=False,
    )

    name = fields.Char(
        string="Field Name",
        copy=False,
    )

    nbboiteminfournisseur = fields.Integer(
        string="Field Nbboiteminfournisseur",
        copy=False,
    )

    nocommande = fields.Integer(
        string="Field Nocommande",
        required=True,
        copy=False,
    )

    nofournisseurproduit = fields.Integer(
        string="Field Nofournisseurproduit",
        required=True,
        copy=False,
    )

    nofournisseurproduitcommande = fields.Integer(
        string="Field Nofournisseurproduitcommande",
        required=True,
        copy=False,
    )

    qteparboiteprevu = fields.Float(
        string="Field Qteparboiteprevu",
        copy=False,
    )
