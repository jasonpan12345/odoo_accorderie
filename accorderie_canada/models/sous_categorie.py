from odoo import _, api, fields, models


class SousCategorie(models.Model):
    _name = "sous.categorie"
    _description = "Model Sous_categorie belonging to Module Tbl"

    approuver = fields.Integer(string="Field Approuver")

    name = fields.Char(string="Field Name")

    nocategorie = fields.Integer(
        string="Field Nocategorie",
        required=True,
    )

    nosouscategorie = fields.Char(
        string="Field Nosouscategorie",
        required=True,
    )

    supprimer = fields.Integer(string="Field Supprimer")

    titresouscategorie = fields.Char(string="Field Titresouscategorie")
