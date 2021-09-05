from odoo import _, api, models, fields


class AccorderieSituationMaison(models.Model):
    _name = "accorderie.situation.maison"
    _description = "Accorderie Situation Maison"
    _rec_name = "nom"

    nom = fields.Char(string="Situation")
