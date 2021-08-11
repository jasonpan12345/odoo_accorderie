from odoo import _, api, models, fields


class FournisseurProduitPointservice(models.Model):
    _name = "fournisseur.produit.pointservice"
    _description = (
        "Model Fournisseur_produit_pointservice belonging to Module Tbl"
    )

    coutunitaire = fields.Float()

    datemaj_fournprodptserv = fields.Datetime(string="Datemaj fournprodptserv")

    name = fields.Char()

    nofournisseurproduit = fields.Integer(required=True)

    nofournisseurproduitpointservice = fields.Integer(required=True)

    nopointservice = fields.Integer(required=True)

    qtestokeacc = fields.Integer()