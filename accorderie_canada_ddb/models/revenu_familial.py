from odoo import _, api, models, fields


class RevenuFamilial(models.Model):
    _name = "revenu.familial"
    _description = "Model Revenu_familial belonging to Module Tbl"
    _rec_name = "nom"

    name = fields.Char()

    nom = fields.Char(string="Revenu")
