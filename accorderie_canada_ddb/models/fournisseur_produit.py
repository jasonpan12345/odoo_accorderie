from odoo import _, api, models, fields


class FournisseurProduit(models.Model):
    _name = "fournisseur.produit"
    _description = "Model Fournisseur_produit belonging to Module Tbl"

    codeproduit = fields.Char(string="Field Codeproduit")

    datemaj_fournproduit = fields.Datetime(string="Field Datemaj_fournproduit")

    name = fields.Char(string="Field Name")

    nofournisseur = fields.Integer(
        string="Field Nofournisseur",
    )

    nofournisseurproduit = fields.Integer(
        string="Field Nofournisseurproduit",
        required=True,
    )

    noproduit = fields.Integer(
        string="Field Noproduit",
        required=True,
    )

    visible_fournisseurproduit = fields.Integer(
        string="Field Visible_fournisseurproduit"
    )

    zcoutunitaire = fields.Float(string="Field Zcoutunitaire")

    zqtestokeacc = fields.Integer(string="Field Zqtestokeacc")
