from odoo import _, api, models, fields


class FournisseurProduit(models.Model):
    _name = "fournisseur.produit"
    _description = "Model Fournisseur_produit belonging to Module Tbl"

    codeproduit = fields.Char()

    datemaj_fournproduit = fields.Datetime(string="Datemaj fournproduit")

    name = fields.Char()

    nofournisseur = fields.Integer()

    nofournisseurproduit = fields.Integer(required=True)

    noproduit = fields.Integer(required=True)

    visible_fournisseurproduit = fields.Integer(
        string="Visible fournisseurproduit"
    )

    zcoutunitaire = fields.Float()

    zqtestokeacc = fields.Integer()
