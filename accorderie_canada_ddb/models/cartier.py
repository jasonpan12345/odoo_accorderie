from odoo import _, api, models, fields


class Cartier(models.Model):
    _name = "cartier"
    _description = "Model Cartier belonging to Module Tbl"

    cartier = fields.Char()

    name = fields.Char()

    noarrondissement = fields.Many2one(
        comodel_name="arrondissement",
        required=True,
    )

    nocartier = fields.Integer(required=True)
