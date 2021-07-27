from odoo import _, api, models, fields


class Taxe(models.Model):
    _name = "taxe"
    _description = "Model Taxe belonging to Module Tbl"

    name = fields.Char(string="Field Name")

    notaxe = fields.Integer(
        string="Field Notaxe",
        required=True,
    )

    notaxefed = fields.Char(string="Field Notaxefed")

    notaxepro = fields.Char(string="Field Notaxepro")

    tauxmajoration = fields.Float(string="Field Tauxmajoration")

    tauxtaxefed = fields.Float(string="Field Tauxtaxefed")

    tauxtaxepro = fields.Float(string="Field Tauxtaxepro")
