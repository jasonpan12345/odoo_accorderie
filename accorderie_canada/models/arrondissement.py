from odoo import _, api, fields, models


class Arrondissement(models.Model):
    _name = "arrondissement"
    _description = "Model Arrondissement belonging to Module Tbl"

    arrondissement = fields.Char(string="Field Arrondissement")

    name = fields.Char(string="Field Name")

    noarrondissement = fields.Integer(
        string="Field Noarrondissement",
        required=True,
    )

    noville = fields.Integer(string="Field Noville")
