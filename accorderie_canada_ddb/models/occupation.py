from odoo import _, api, models, fields


class Occupation(models.Model):
    _name = "occupation"
    _description = "Model Occupation belonging to Module Tbl"
    _rec_name = "nom"

    nom = fields.Char(string="Occupation")
