from odoo import _, api, models, fields


class Ville(models.Model):
    _name = "ville"
    _description = "Model Ville belonging to Module Tbl"

    name = fields.Char(string="Field Name")

    noregion = fields.Integer(string="Field Noregion")

    noville = fields.Integer(
        string="Field Noville",
        required=True,
    )

    ville = fields.Char(string="Field Ville")
