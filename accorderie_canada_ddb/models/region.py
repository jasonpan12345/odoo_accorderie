from odoo import _, api, models, fields


class Region(models.Model):
    _name = "region"
    _description = "Model Region belonging to Module Tbl"

    name = fields.Char()

    noregion = fields.Integer(required=True)

    region = fields.Char()
