from odoo import _, api, models, fields


class Ville(models.Model):
    _name = "ville"
    _description = "Model Ville belonging to Module Tbl"

    name = fields.Char()

    noregion = fields.Many2one(comodel_name="region")

    noville = fields.Integer(required=True)

    ville = fields.Char()
