from odoo import _, api, fields, models


class AchatPonctuel(models.Model):
    _name = "achat.ponctuel"
    _description = "Model Achat_ponctuel belonging to Module Tbl"

    achatponcfacturer = fields.Integer(string="Field Achatponcfacturer")

    dateachatponctuel = fields.Date(string="Field Dateachatponctuel")

    datemaj_achantponct = fields.Datetime(string="Field Datemaj_achantponct")

    majoration_achatponct = fields.Float(string="Field Majoration_achatponct")

    montantpaiementachatponct = fields.Float(
        string="Field Montantpaiementachatponct"
    )

    name = fields.Char(string="Field Name")

    noachatponctuel = fields.Integer(
        string="Field Noachatponctuel",
        required=True,
    )

    nomembre = fields.Integer(
        string="Field Nomembre",
        required=True,
    )

    taxef_achatponct = fields.Float(string="Field Taxef_achatponct")

    taxep_achatponct = fields.Float(string="Field Taxep_achatponct")
