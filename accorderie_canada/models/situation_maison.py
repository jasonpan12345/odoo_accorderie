from odoo import _, api, fields, models


class SituationMaison(models.Model):
    _name = "situation.maison"
    _description = "Model Situation_maison belonging to Module Tbl"

    name = fields.Char(string="Field Name")

    nosituationmaison = fields.Integer(
        string="Field Nosituationmaison",
        required=True,
    )

    situation = fields.Char(string="Field Situation")
