from odoo import _, api, models, fields


class AccorderieRegion(models.Model):
    _name = "accorderie.region"
    _description = "Accorderie Region"
    _rec_name = "nom"

    code = fields.Integer(
        string="Code de région",
        required=True,
        help="Code de la région administrative",
    )

    nom = fields.Char()
