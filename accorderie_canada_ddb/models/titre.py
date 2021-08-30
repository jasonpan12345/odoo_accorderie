from odoo import _, api, models, fields


class Titre(models.Model):
    _name = "titre"
    _description = "Model Titre belonging to Module Tbl"
    _rec_name = "nom"

    datemaj_titre = fields.Datetime(string="Datemaj titre")

    nom = fields.Char(string="Titre")

    visible_titre = fields.Integer(string="Visible titre")
