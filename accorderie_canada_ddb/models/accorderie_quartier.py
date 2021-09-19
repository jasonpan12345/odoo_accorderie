from odoo import _, api, models, fields


class AccorderieQuartier(models.Model):
    _name = "accorderie.quartier"
    _description = "Accorderie Quartier"
    _rec_name = "nom"

    arrondissement = fields.Many2one(
        comodel_name="accorderie.arrondissement",
        required=True,
        help="Arrondissement associé au quartier",
    )

    membre = fields.One2many(
        comodel_name="accorderie.membre",
        inverse_name="quartier",
        help="Membre relation",
    )

    nom = fields.Char(
        string="Nom du quartier",
        help="Nom du quartier",
    )
