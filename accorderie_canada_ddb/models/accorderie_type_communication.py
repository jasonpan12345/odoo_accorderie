from odoo import _, api, models, fields


class AccorderieTypeCommunication(models.Model):
    _name = "accorderie.type.communication"
    _description = "Accorderie Type Communication"
    _rec_name = "nom"

    membre = fields.One2many(
        comodel_name="accorderie.membre",
        inverse_name="type_communication",
        help="Membre relation",
    )

    nom = fields.Char(string="Typecommunication")
