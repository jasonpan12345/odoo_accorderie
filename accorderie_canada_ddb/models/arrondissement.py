from odoo import _, api, models, fields


class Arrondissement(models.Model):
    _name = "arrondissement"
    _description = "Model Arrondissement belonging to Module Tbl"

    arrondissement = fields.Char()

    name = fields.Char()

    noarrondissement = fields.Integer(required=True)

    noville = fields.Integer()
