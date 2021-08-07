from odoo import _, api, models, fields


class SituationMaison(models.Model):
    _name = "situation.maison"
    _description = "Model Situation_maison belonging to Module Tbl"

    name = fields.Char()

    nosituationmaison = fields.Integer(required=True)

    situation = fields.Char()
