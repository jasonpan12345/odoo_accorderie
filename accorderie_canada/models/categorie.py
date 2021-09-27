from odoo import _, api, models, fields


class Categorie(models.Model):
    _name = "categorie"
    _description = "Model Categorie belonging to Module Tbl"

    approuver = fields.Integer(string="Field Approuver")

    name = fields.Char(string="Field Name")

    nocategorie = fields.Integer(
        string="Field Nocategorie",
        required=True,
    )

    supprimer = fields.Integer(string="Field Supprimer")

    titrecategorie = fields.Char(string="Field Titrecategorie")
