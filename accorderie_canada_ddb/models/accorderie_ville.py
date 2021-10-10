from odoo import _, api, models, fields


class AccorderieVille(models.Model):
    _name = "accorderie.ville"
    _inherit = "portal.mixin"
    _description = "Accorderie Ville"
    _rec_name = "nom"

    accorderie = fields.One2many(
        comodel_name="accorderie.accorderie",
        inverse_name="ville",
        help="Accorderie relation",
    )

    arrondissement = fields.One2many(
        comodel_name="accorderie.arrondissement",
        inverse_name="ville",
        help="Arrondissement relation",
    )

    code = fields.Integer(
        required=True,
        help="Code de la ville",
    )

    membre = fields.One2many(
        comodel_name="accorderie.membre",
        inverse_name="ville",
        help="Membre relation",
    )

    nom = fields.Char()

    region = fields.Many2one(
        string="Région",
        comodel_name="accorderie.region",
    )
