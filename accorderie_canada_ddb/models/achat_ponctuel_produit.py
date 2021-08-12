from odoo import _, api, models, fields


class AchatPonctuelProduit(models.Model):
    _name = "achat.ponctuel.produit"
    _description = "Model Achat_ponctuel_produit belonging to Module Tbl"

    coutunit_achatponctprod = fields.Float(string="Coutunit achatponctprod")

    datemaj_achatponcproduit = fields.Datetime(
        string="Datemaj achatponcproduit"
    )

    name = fields.Char()

    noachatponctuel = fields.Many2one(
        comodel_name="achat.ponctuel",
        required=True,
    )

    noachatponctuelproduit = fields.Integer(required=True)

    nofournisseurproduit = fields.Many2one(
        comodel_name="fournisseur.produit",
        required=True,
    )

    prixfacturer_achatponctprod = fields.Float(
        string="Prixfacturer achatponctprod"
    )

    qteacheter = fields.Float()

    sitaxablef_achatponctprod = fields.Integer(
        string="Sitaxablef achatponctprod"
    )

    sitaxablep_achatponctprod = fields.Integer(
        string="Sitaxablep achatponctprod"
    )
