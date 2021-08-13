from odoo import _, api, models, fields


class SousCategorie(models.Model):
    _name = "sous.categorie"
    _description = "Model Sous_categorie belonging to Module Tbl"

    approuver = fields.Integer()

    name = fields.Char()

    nocategorie = fields.Many2one(
        comodel_name="categorie",
        required=True,
    )

    nosouscategorie = fields.Char(required=True)

    nosouscategorieid = fields.Integer()

    supprimer = fields.Integer()

    titresouscategorie = fields.Char()
