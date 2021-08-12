from odoo import _, api, models, fields


class Mensualite(models.Model):
    _name = "mensualite"
    _description = "Model Mensualite belonging to Module Tbl"

    id_mensualite = fields.Integer(
        string="Id mensualite",
        required=True,
    )

    id_pret = fields.Many2one(
        string="Id pret",
        comodel_name="pret",
        required=True,
    )

    name = fields.Char()
