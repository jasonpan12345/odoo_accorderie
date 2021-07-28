from odoo import _, api, models, fields


class Cartier(models.Model):
    _name = "cartier"
    _description = "Model Cartier belonging to Module Tbl"

    cartier = fields.Char(string="Field Cartier")

    name = fields.Char(string="Field Name")

    noarrondissement = fields.Integer(
        string="Field Noarrondissement",
        required=True,
    )

    nocartier = fields.Integer(
        string="Field Nocartier",
        required=True,
    )
