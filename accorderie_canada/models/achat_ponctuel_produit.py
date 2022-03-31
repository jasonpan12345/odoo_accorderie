from odoo import _, api, fields, models


class AchatPonctuelProduit(models.Model):
    _name = "achat.ponctuel.produit"
    _description = "Model Achat_ponctuel_produit belonging to Module Tbl"

    coutunit_achatponctprod = fields.Float(
        string="Field Coutunit_achatponctprod"
    )

    datemaj_achatponcproduit = fields.Datetime(
        string="Field Datemaj_achatponcproduit"
    )

    name = fields.Char(string="Field Name")

    noachatponctuel = fields.Integer(
        string="Field Noachatponctuel",
        required=True,
    )

    noachatponctuelproduit = fields.Integer(
        string="Field Noachatponctuelproduit",
        required=True,
    )

    nofournisseurproduit = fields.Integer(
        string="Field Nofournisseurproduit",
        required=True,
    )

    prixfacturer_achatponctprod = fields.Float(
        string="Field Prixfacturer_achatponctprod"
    )

    qteacheter = fields.Float(string="Field Qteacheter")

    sitaxablef_achatponctprod = fields.Integer(
        string="Field Sitaxablef_achatponctprod"
    )

    sitaxablep_achatponctprod = fields.Integer(
        string="Field Sitaxablep_achatponctprod"
    )
