from odoo import _, api, models, fields


class CommandeMembreProduit(models.Model):
    _name = "commande.membre.produit"
    _description = "Model Commande_membre_produit belonging to Module Tbl"

    ajustement = fields.Float()

    coutunitaire_facture = fields.Float(string="Coutunitaire facture")

    datemaj_cmdmembreprod = fields.Datetime(string="Datemaj cmdmembreprod")

    name = fields.Char()

    nocmdmbproduit = fields.Integer(required=True)

    nocommandemembre = fields.Integer(required=True)

    nofournisseurproduitcommande = fields.Integer(required=True)

    prixfacturer_manuel = fields.Float(string="Prixfacturer manuel")

    qte = fields.Float()

    qtedeplus = fields.Float()

    sitaxablef_facture = fields.Integer(string="Sitaxablef facture")

    sitaxablep_facture = fields.Integer(string="Sitaxablep facture")
