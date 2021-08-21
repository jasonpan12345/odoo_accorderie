from odoo import _, api, models, fields


class Arrondissement(models.Model):
    _name = "arrondissement"
    _description = "Model Arrondissement belonging to Module Tbl"
    _rec_name = "nom"

    nom = fields.Char()

    ville = fields.Many2one(comodel_name="ville")
