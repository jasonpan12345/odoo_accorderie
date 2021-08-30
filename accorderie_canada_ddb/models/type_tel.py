from odoo import _, api, models, fields


class TypeTel(models.Model):
    _name = "type.tel"
    _description = "Model Type_tel belonging to Module Tbl"
    _rec_name = "nom"

    name = fields.Char()

    nom = fields.Char(string="Typetel")
