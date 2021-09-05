from odoo import _, api, models, fields


class AccorderieTypeCommunication(models.Model):
    _name = "accorderie.type.communication"
    _description = "Accorderie Type Communication"
    _rec_name = "nom"

    nom = fields.Char(string="Typecommunication")
