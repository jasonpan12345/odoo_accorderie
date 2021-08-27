from odoo import _, api, models, fields


class Occupation(models.Model):
    _name = "occupation"
    _description = "Model Occupation belonging to Module Tbl"

    name = fields.Char()

    occupation = fields.Char()
