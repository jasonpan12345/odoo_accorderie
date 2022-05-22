from odoo import _, api, fields, models


class Provenance(models.Model):
    _name = "provenance"
    _description = "Model Provenance belonging to Module Tbl"

    name = fields.Char(string="Field Name")

    noprovenance = fields.Integer(
        string="Field Noprovenance",
        required=True,
    )

    provenance = fields.Char(string="Field Provenance")
