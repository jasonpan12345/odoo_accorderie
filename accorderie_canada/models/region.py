from odoo import _, api, models, fields


class Region(models.Model):
    _name = "region"
    _description = "Model Region belonging to Module Tbl"

    name = fields.Char(string="Field Name")

    noregion = fields.Integer(
        string="Field Noregion",
        required=True,
    )

    region = fields.Char(string="Field Region")
