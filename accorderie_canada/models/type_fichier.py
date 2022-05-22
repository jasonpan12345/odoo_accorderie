from odoo import _, api, fields, models


class TypeFichier(models.Model):
    _name = "type.fichier"
    _description = "Model Type_fichier belonging to Module Tbl"

    datemaj_typefichier = fields.Datetime(
        string="Field Datemaj_typefichier",
        required=True,
    )

    id_typefichier = fields.Integer(
        string="Field Id_typefichier",
        required=True,
    )

    name = fields.Char(string="Field Name")

    typefichier = fields.Char(string="Field Typefichier")
