from odoo import _, api, models, fields


class Categorie(models.Model):
    _name = "categorie"
    _description = "Model Categorie belonging to Module Tbl"
    _rec_name = "nom"

    approuve = fields.Boolean(
        string="Approuvé",
        help="Permet d'approuver cette entrée",
    )

    archive = fields.Boolean(
        string="Archivé",
        help="Permet d'archiver cette entrée",
    )

    nom = fields.Char(help="Le nom de la catégorie")
