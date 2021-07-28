from odoo import _, api, models, fields


class Versement(models.Model):
    _name = "versement"
    _description = "Model Versement belonging to Module Tbl"

    datemaj_versement = fields.Datetime(string="Field Datemaj_versement")

    id_mensualite = fields.Integer(
        string="Field Id_mensualite",
        required=True,
    )

    id_versement = fields.Integer(
        string="Field Id_versement",
        required=True,
    )

    montantversement = fields.Float(string="Field Montantversement")

    name = fields.Char(string="Field Name")
