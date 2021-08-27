from odoo import _, api, models, fields


class Titre(models.Model):
    _name = "titre"
    _description = "Model Titre belonging to Module Tbl"

    datemaj_titre = fields.Datetime(string="Datemaj titre")

    name = fields.Char()

    titre = fields.Char()

    visible_titre = fields.Integer(string="Visible titre")
