# -*- coding: utf-8 -*-

from odoo import api, models, fields


class CommandeMembreProduit(models.Model):
    _name = "commande.membre.produit"
    _description = "Model Commande_membre_produit belonging to Module Tbl"

    ajustement = fields.Float(
        string="Field Ajustement",
        copy=False,
    )

    coutunitaire_facture = fields.Float(
        string="Field Coutunitaire_facture",
        copy=False,
    )

    datemaj_cmdmembreprod = fields.Datetime(
        string="Field Datemaj_cmdmembreprod",
        copy=False,
    )

    name = fields.Char(
        string="Field Name",
        copy=False,
    )

    nocmdmbproduit = fields.Integer(
        string="Field Nocmdmbproduit",
        required=True,
        copy=False,
    )

    nocommandemembre = fields.Integer(
        string="Field Nocommandemembre",
        required=True,
        copy=False,
    )

    nofournisseurproduitcommande = fields.Integer(
        string="Field Nofournisseurproduitcommande",
        required=True,
        copy=False,
    )

    prixfacturer_manuel = fields.Float(
        string="Field Prixfacturer_manuel",
        copy=False,
    )

    qte = fields.Float(
        string="Field Qte",
        copy=False,
    )

    qtedeplus = fields.Float(
        string="Field Qtedeplus",
        copy=False,
    )

    sitaxablef_facture = fields.Integer(
        string="Field Sitaxablef_facture",
        copy=False,
    )

    sitaxablep_facture = fields.Integer(
        string="Field Sitaxablep_facture",
        copy=False,
    )
