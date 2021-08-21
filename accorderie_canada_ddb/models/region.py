from odoo import _, api, models, fields


class Region(models.Model):
    _name = "region"
    _description = "Model Region belonging to Module Tbl"
    _rec_name = "nom"

    code = fields.Integer(
        string="Code de région",
        required=True,
        help="Code de la région administrative",
    )

    nom = fields.Char()
