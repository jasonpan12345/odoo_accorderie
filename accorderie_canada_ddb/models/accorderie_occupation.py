from odoo import _, api, models, fields


class AccorderieOccupation(models.Model):
    _name = "accorderie.occupation"
    _description = "Accorderie Occupation"
    _rec_name = "nom"

    nom = fields.Char(string="Occupation")
