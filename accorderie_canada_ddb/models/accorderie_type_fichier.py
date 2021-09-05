from odoo import _, api, models, fields


class AccorderieTypeFichier(models.Model):
    _name = "accorderie.type.fichier"
    _description = "Accorderie Type Fichier"
    _rec_name = "nom"

    datemaj_typefichier = fields.Datetime(
        string="Datemaj typefichier",
        required=True,
    )

    nom = fields.Char(string="Typefichier")
