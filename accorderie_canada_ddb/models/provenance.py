from odoo import _, api, models, fields


class Provenance(models.Model):
    _name = "provenance"
    _description = "Model Provenance belonging to Module Tbl"
    _rec_name = "nom"

    nom = fields.Char(string="Provenance")
