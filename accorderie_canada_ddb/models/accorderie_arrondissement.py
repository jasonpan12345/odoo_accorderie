from odoo import _, api, models, fields


class AccorderieArrondissement(models.Model):
    _name = "accorderie.arrondissement"
    _inherit = "portal.mixin"
    _description = "Ensemble des arrondissement des Accorderies"
    _rec_name = "nom"

    membre = fields.One2many(
        comodel_name="accorderie.membre",
        inverse_name="arrondissement",
        help="Membre relation",
    )

    nom = fields.Char()

    ville = fields.Many2one(comodel_name="accorderie.ville")
