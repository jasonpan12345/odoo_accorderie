from odoo import _, api, models, fields


class FournisseurProduitPointservice(models.Model):
    _name = "fournisseur.produit.pointservice"
    _description = (
        "Model Fournisseur_produit_pointservice belonging to Module Tbl"
    )

    coutunitaire = fields.Float(string="Field Coutunitaire")

    datemaj_fournprodptserv = fields.Datetime(
        string="Field Datemaj_fournprodptserv"
    )

    name = fields.Char(string="Field Name")

    nofournisseurproduit = fields.Integer(
        string="Field Nofournisseurproduit",
        required=True,
    )

    nofournisseurproduitpointservice = fields.Integer(
        string="Field Nofournisseurproduitpointservice",
        required=True,
    )

    nopointservice = fields.Integer(
        string="Field Nopointservice",
        required=True,
    )

    qtestokeacc = fields.Integer(string="Field Qtestokeacc")
