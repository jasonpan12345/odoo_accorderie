from odoo import _, api, models, fields


class AccorderieTitre(models.Model):
    _name = "accorderie.titre"
    _description = "Accorderie Titre"
    _rec_name = "nom"

    datemaj_titre = fields.Datetime(string="Datemaj titre")

    nom = fields.Char(string="Titre")

    visible_titre = fields.Integer(string="Visible titre")
