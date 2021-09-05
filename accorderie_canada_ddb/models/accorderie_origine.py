from odoo import _, api, models, fields


class AccorderieOrigine(models.Model):
    _name = "accorderie.origine"
    _description = "Accorderie Origine"
    _rec_name = "nom"

    nom = fields.Char(string="Origine")
