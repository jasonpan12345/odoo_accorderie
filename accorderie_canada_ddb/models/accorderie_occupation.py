from odoo import _, api, models, fields


class AccorderieOccupation(models.Model):
    _name = "accorderie.occupation"
    _inherit = "portal.mixin"
    _description = "Accorderie Occupation"
    _rec_name = "nom"

    membre = fields.One2many(
        comodel_name="accorderie.membre",
        inverse_name="occupation",
        help="Membre relation",
    )

    nom = fields.Char(string="Occupation")
