from odoo import _, api, fields, models


class Fichier(models.Model):
    _name = "fichier"
    _description = "Model Fichier belonging to Module Tbl"

    datemaj_fichier = fields.Datetime(string="Field Datemaj_fichier")

    id_fichier = fields.Integer(
        string="Field Id_fichier",
        required=True,
    )

    id_typefichier = fields.Integer(
        string="Field Id_typefichier",
        required=True,
    )

    name = fields.Char(string="Field Name")

    noaccorderie = fields.Integer(
        string="Field Noaccorderie",
        required=True,
    )

    nomfichieroriginal = fields.Char(
        string="Field Nomfichieroriginal",
        required=True,
    )

    nomfichierstokage = fields.Char(
        string="Field Nomfichierstokage",
        required=True,
    )

    si_accorderielocalseulement = fields.Integer(
        string="Field Si_accorderielocalseulement"
    )

    si_admin = fields.Integer(string="Field Si_admin")

    si_disponible = fields.Integer(string="Field Si_disponible")
