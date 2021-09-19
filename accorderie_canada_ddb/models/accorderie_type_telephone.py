from odoo import _, api, models, fields


class AccorderieTypeTelephone(models.Model):
    _name = "accorderie.type.telephone"
    _description = "Accorderie Type Telephone"
    _rec_name = "nom"

    nom = fields.Char()
