from odoo import _, api, models, fields


class AccorderieTypeTel(models.Model):
    _name = "accorderie.type.tel"
    _description = "Accorderie Type Tel"
    _rec_name = "nom"

    nom = fields.Char()
