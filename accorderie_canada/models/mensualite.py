from odoo import _, api, fields, models


class Mensualite(models.Model):
    _name = "mensualite"
    _description = "Model Mensualite belonging to Module Tbl"

    id_mensualite = fields.Integer(
        string="Field Id_mensualite",
        required=True,
    )

    id_pret = fields.Integer(
        string="Field Id_pret",
        required=True,
    )

    name = fields.Char(string="Field Name")
