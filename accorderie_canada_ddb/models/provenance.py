from odoo import _, api, models, fields


class Provenance(models.Model):
    _name = "provenance"
    _description = "Model Provenance belonging to Module Tbl"

    name = fields.Char()

    provenance = fields.Char()
