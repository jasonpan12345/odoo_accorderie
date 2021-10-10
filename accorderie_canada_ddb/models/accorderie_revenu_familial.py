from odoo import _, api, models, fields


class AccorderieRevenuFamilial(models.Model):
    _name = "accorderie.revenu.familial"
    _inherit = "portal.mixin"
    _description = "Accorderie Revenu Familial"
    _rec_name = "nom"

    membre = fields.One2many(
        comodel_name="accorderie.membre",
        inverse_name="revenu_familial",
        help="Membre relation",
    )

    nom = fields.Char(string="Revenu")
