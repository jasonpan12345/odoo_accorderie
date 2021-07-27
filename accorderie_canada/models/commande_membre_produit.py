from odoo import _, api, models, fields


class CommandeMembreProduit(models.Model):
    _name = "commande.membre.produit"
    _description = "Model Commande_membre_produit belonging to Module Tbl"

    ajustement = fields.Float(string="Field Ajustement")

    coutunitaire_facture = fields.Float(string="Field Coutunitaire_facture")

    datemaj_cmdmembreprod = fields.Datetime(
        string="Field Datemaj_cmdmembreprod"
    )

    name = fields.Char(string="Field Name")

    nocmdmbproduit = fields.Integer(
        string="Field Nocmdmbproduit",
        required=True,
    )

    nocommandemembre = fields.Integer(
        string="Field Nocommandemembre",
        required=True,
    )

    nofournisseurproduitcommande = fields.Integer(
        string="Field Nofournisseurproduitcommande",
        required=True,
    )

    prixfacturer_manuel = fields.Float(string="Field Prixfacturer_manuel")

    qte = fields.Float(string="Field Qte")

    qtedeplus = fields.Float(string="Field Qtedeplus")

    sitaxablef_facture = fields.Integer(string="Field Sitaxablef_facture")

    sitaxablep_facture = fields.Integer(string="Field Sitaxablep_facture")
