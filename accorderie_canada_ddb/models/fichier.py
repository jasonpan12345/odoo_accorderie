from odoo import _, api, models, fields


class Fichier(models.Model):
    _name = "fichier"
    _description = "Model Fichier belonging to Module Tbl"

    datemaj_fichier = fields.Datetime(string="Datemaj fichier")

    id_fichier = fields.Integer(
        string="Id fichier",
        required=True,
    )

    id_typefichier = fields.Integer(
        string="Id typefichier",
        required=True,
    )

    name = fields.Char()

    noaccorderie = fields.Integer(required=True)

    nomfichieroriginal = fields.Char(required=True)

    nomfichierstokage = fields.Char(required=True)

    si_accorderielocalseulement = fields.Integer(
        string="Si accorderielocalseulement"
    )

    si_admin = fields.Integer(string="Si admin")

    si_disponible = fields.Integer(string="Si disponible")
