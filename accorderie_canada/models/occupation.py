from odoo import _, api, models, fields


class Occupation(models.Model):
    _name = "occupation"
    _description = "Model Occupation belonging to Module Tbl"

    name = fields.Char(string="Field Name")

    nooccupation = fields.Integer(
        string="Field Nooccupation",
        required=True,
    )

    occupation = fields.Char(string="Field Occupation")
