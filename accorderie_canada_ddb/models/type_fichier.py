from odoo import _, api, models, fields


class TypeFichier(models.Model):
    _name = "type.fichier"
    _description = "Model Type_fichier belonging to Module Tbl"
    _rec_name = "nom"

    datemaj_typefichier = fields.Datetime(
        string="Datemaj typefichier",
        required=True,
    )

    name = fields.Char()

    nom = fields.Char(string="Typefichier")
