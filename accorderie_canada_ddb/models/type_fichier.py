from odoo import _, api, models, fields


class TypeFichier(models.Model):
    _name = "type.fichier"
    _description = "Model Type_fichier belonging to Module Tbl"

    datemaj_typefichier = fields.Datetime(
        string="Datemaj typefichier",
        required=True,
    )

    id_typefichier = fields.Integer(
        string="Id typefichier",
        required=True,
    )

    name = fields.Char()

    typefichier = fields.Char()
