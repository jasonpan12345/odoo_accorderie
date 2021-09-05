from odoo import _, api, models, fields


class AccorderieArrondissement(models.Model):
    _name = "accorderie.arrondissement"
    _description = "Ensemble des arrondissement des Accorderies"
    _rec_name = "nom"

    nom = fields.Char()

    ville = fields.Many2one(comodel_name="accorderie.ville")
