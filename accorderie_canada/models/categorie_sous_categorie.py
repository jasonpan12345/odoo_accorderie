from odoo import _, api, models, fields


class CategorieSousCategorie(models.Model):
    _name = "categorie.sous.categorie"
    _description = "Model Categorie_sous_categorie belonging to Module Tbl"

    approuver = fields.Integer(string="Field Approuver")

    description = fields.Char(string="Field Description")

    name = fields.Char(string="Field Name")

    nocategorie = fields.Integer(string="Field Nocategorie")

    nocategoriesouscategorie = fields.Integer(
        string="Field Nocategoriesouscategorie",
        required=True,
    )

    nooffre = fields.Integer(string="Field Nooffre")

    nosouscategorie = fields.Char(string="Field Nosouscategorie")

    supprimer = fields.Integer(string="Field Supprimer")

    titreoffre = fields.Char(string="Field Titreoffre")
