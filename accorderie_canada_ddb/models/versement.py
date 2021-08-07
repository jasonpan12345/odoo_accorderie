from odoo import _, api, models, fields


class Versement(models.Model):
    _name = "versement"
    _description = "Model Versement belonging to Module Tbl"

    datemaj_versement = fields.Datetime(string="Datemaj versement")

    id_mensualite = fields.Integer(
        string="Id mensualite",
        required=True,
    )

    id_versement = fields.Integer(
        string="Id versement",
        required=True,
    )

    montantversement = fields.Float()

    name = fields.Char()
