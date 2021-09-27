from odoo import _, api, models, fields


class Titre(models.Model):
    _name = "titre"
    _description = "Model Titre belonging to Module Tbl"

    datemaj_titre = fields.Datetime(string="Field Datemaj_titre")

    name = fields.Char(string="Field Name")

    notitre = fields.Integer(
        string="Field Notitre",
        required=True,
    )

    titre = fields.Char(string="Field Titre")

    visible_titre = fields.Integer(string="Field Visible_titre")
