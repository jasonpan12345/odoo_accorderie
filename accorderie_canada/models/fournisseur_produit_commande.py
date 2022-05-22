from odoo import _, api, fields, models


class FournisseurProduitCommande(models.Model):
    _name = "fournisseur.produit.commande"
    _description = "Model Fournisseur_produit_commande belonging to Module Tbl"

    coutunitprevu = fields.Float(string="Field Coutunitprevu")

    datemaj_fournprodcommande = fields.Datetime(
        string="Field Datemaj_fournprodcommande"
    )

    disponible = fields.Integer(string="Field Disponible")

    name = fields.Char(string="Field Name")

    nbboiteminfournisseur = fields.Integer(
        string="Field Nbboiteminfournisseur"
    )

    nocommande = fields.Integer(
        string="Field Nocommande",
        required=True,
    )

    nofournisseurproduit = fields.Integer(
        string="Field Nofournisseurproduit",
        required=True,
    )

    nofournisseurproduitcommande = fields.Integer(
        string="Field Nofournisseurproduitcommande",
        required=True,
    )

    qteparboiteprevu = fields.Float(string="Field Qteparboiteprevu")
