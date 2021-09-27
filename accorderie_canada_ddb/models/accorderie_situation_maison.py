from odoo import _, api, models, fields


class AccorderieSituationMaison(models.Model):
    _name = "accorderie.situation.maison"
    _description = "Accorderie Situation Maison"
    _rec_name = "nom"

    membre = fields.One2many(
        comodel_name="accorderie.membre",
        inverse_name="situation_maison",
        help="Membre relation",
    )

    nom = fields.Char(string="Situation")
