from odoo import _, api, models, fields


class Mensualite(models.Model):
    _name = "mensualite"
    _description = "Model Mensualite belonging to Module Tbl"

    id_mensualite = fields.Integer(
        string="Id mensualite",
        required=True,
    )

    id_pret = fields.Integer(
        string="Id pret",
        required=True,
    )

    name = fields.Char()
