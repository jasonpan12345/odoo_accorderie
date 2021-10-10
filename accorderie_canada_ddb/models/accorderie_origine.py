from odoo import _, api, models, fields


class AccorderieOrigine(models.Model):
    _name = "accorderie.origine"
    _inherit = "portal.mixin"
    _description = "Accorderie Origine"
    _rec_name = "nom"

    membre = fields.One2many(
        comodel_name="accorderie.membre",
        inverse_name="origine",
        help="Membre relation",
    )

    nom = fields.Char(string="Origine")
