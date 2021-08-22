from odoo import _, api, models, fields


class Cartier(models.Model):
    _name = "cartier"
    _description = "Model Cartier belonging to Module Tbl"
    _rec_name = "nom"

    arrondissement = fields.Many2one(
        comodel_name="arrondissement",
        required=True,
        help="Arrondissement associé au quartier",
    )

    nom = fields.Char(
        string="Nom du quartier",
        help="Nom du quartier",
    )
