from odoo import _, api, models, fields


class SituationMaison(models.Model):
    _name = "situation.maison"
    _description = "Model Situation_maison belonging to Module Tbl"
    _rec_name = "nom"

    name = fields.Char()

    nom = fields.Char(string="Situation")
