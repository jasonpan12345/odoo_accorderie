from odoo import _, api, models, fields


class Categorie(models.Model):
    _name = "categorie"
    _description = "Model Categorie belonging to Module Tbl"

    approuver = fields.Integer()

    name = fields.Char()

    nocategorie = fields.Integer(required=True)

    supprimer = fields.Integer()

    titrecategorie = fields.Char()
