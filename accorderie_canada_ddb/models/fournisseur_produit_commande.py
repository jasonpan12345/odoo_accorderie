from odoo import _, api, models, fields


class FournisseurProduitCommande(models.Model):
    _name = "fournisseur.produit.commande"
    _description = "Model Fournisseur_produit_commande belonging to Module Tbl"

    coutunitprevu = fields.Float()

    datemaj_fournprodcommande = fields.Datetime(
        string="Datemaj fournprodcommande"
    )

    disponible = fields.Integer()

    name = fields.Char()

    nbboiteminfournisseur = fields.Integer()

    nocommande = fields.Integer()

    nofournisseurproduit = fields.Integer(required=True)

    nofournisseurproduitcommande = fields.Integer(required=True)

    qteparboiteprevu = fields.Float()
