from odoo import _, api, models, fields


class Taxe(models.Model):
    _name = "taxe"
    _description = "Model Taxe belonging to Module Tbl"

    name = fields.Char()

    notaxe = fields.Integer(required=True)

    notaxefed = fields.Char()

    notaxepro = fields.Char()

    tauxmajoration = fields.Float()

    tauxtaxefed = fields.Float()

    tauxtaxepro = fields.Float()
