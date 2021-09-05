from odoo import _, api, models, fields


class AccorderieVille(models.Model):
    _name = "accorderie.ville"
    _description = "Accorderie Ville"
    _rec_name = "nom"

    code = fields.Integer(
        required=True,
        help="Code de la ville",
    )

    nom = fields.Char()

    region = fields.Many2one(
        string="Région",
        comodel_name="accorderie.region",
    )
