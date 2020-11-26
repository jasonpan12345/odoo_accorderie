# -*- coding: utf-8 -*-

from odoo import api, models, fields


class FournisseurProduit(models.Model):
    _name = 'fournisseur.produit'
    _description = 'Model Fournisseur_produit belonging to Module Tbl'

    codeproduit = fields.Char(
        string='Field Codeproduit',
        copy=False,
    )

    datemaj_fournproduit = fields.Datetime(
        string='Field Datemaj_fournproduit',
        copy=False,
    )

    name = fields.Char(
        string='Field Name',
        copy=False,
    )

    nofournisseur = fields.Integer(
        string='Field Nofournisseur',
        required=True,
        copy=False,
    )

    nofournisseurproduit = fields.Integer(
        string='Field Nofournisseurproduit',
        required=True,
        copy=False,
    )

    noproduit = fields.Integer(
        string='Field Noproduit',
        required=True,
        copy=False,
    )

    visible_fournisseurproduit = fields.Integer(
        string='Field Visible_fournisseurproduit',
        copy=False,
    )

    zcoutunitaire = fields.Float(
        string='Field Zcoutunitaire',
        copy=False,
    )

    zqtestokeacc = fields.Integer(
        string='Field Zqtestokeacc',
        copy=False,
    )
