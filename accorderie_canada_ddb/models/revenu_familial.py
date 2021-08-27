from odoo import _, api, models, fields


class RevenuFamilial(models.Model):
    _name = "revenu.familial"
    _description = "Model Revenu_familial belonging to Module Tbl"

    name = fields.Char()

    revenu = fields.Char()
