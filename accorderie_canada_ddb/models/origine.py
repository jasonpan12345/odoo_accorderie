from odoo import _, api, models, fields


class Origine(models.Model):
    _name = "origine"
    _description = "Model Origine belonging to Module Tbl"

    name = fields.Char(string="Field Name")

    noorigine = fields.Integer(
        string="Field Noorigine",
        required=True,
    )

    origine = fields.Char(string="Field Origine")
