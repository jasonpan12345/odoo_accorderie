from odoo import _, api, models, fields


class Ville(models.Model):
    _name = "ville"
    _description = "Model Ville belonging to Module Tbl"
    _rec_name = "nom"

    code = fields.Integer(
        required=True,
        help="Code de la ville",
    )

    nom = fields.Char()

    region = fields.Many2one(
        string="Région",
        comodel_name="region",
    )
