from odoo import _, api, models, fields


class AchatPonctuel(models.Model):
    _name = "achat.ponctuel"
    _description = "Model Achat_ponctuel belonging to Module Tbl"

    achatponcfacturer = fields.Integer()

    dateachatponctuel = fields.Date()

    datemaj_achantponct = fields.Datetime(string="Datemaj achantponct")

    majoration_achatponct = fields.Float(string="Majoration achatponct")

    montantpaiementachatponct = fields.Float()

    name = fields.Char()

    noachatponctuel = fields.Integer(required=True)

    nomembre = fields.Many2one(
        comodel_name="membre",
        required=True,
    )

    taxef_achatponct = fields.Float(string="Taxef achatponct")

    taxep_achatponct = fields.Float(string="Taxep achatponct")
