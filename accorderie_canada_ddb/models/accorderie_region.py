from odoo import _, api, models, fields


class AccorderieRegion(models.Model):
    _name = "accorderie.region"
    _inherit = "portal.mixin"
    _description = "Accorderie Region"
    _rec_name = "nom"

    accorderie = fields.One2many(
        comodel_name="accorderie.accorderie",
        inverse_name="region",
        help="Accorderie relation",
    )

    code = fields.Integer(
        string="Code de région",
        required=True,
        help="Code de la région administrative",
    )

    membre = fields.One2many(
        comodel_name="accorderie.membre",
        inverse_name="region",
        help="Membre relation",
    )

    nom = fields.Char()

    ville = fields.One2many(
        comodel_name="accorderie.ville",
        inverse_name="region",
        help="Ville relation",
    )
