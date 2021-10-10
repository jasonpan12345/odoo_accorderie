from odoo import _, api, models, fields


class AccorderieTypeTelephone(models.Model):
    _name = "accorderie.type.telephone"
    _inherit = "portal.mixin"
    _description = "Accorderie Type Telephone"
    _rec_name = "nom"

    membre = fields.One2many(
        comodel_name="accorderie.membre",
        inverse_name="telephone_type_1",
        help="Membre relation",
    )

    membre_2_ids = fields.One2many(
        comodel_name="accorderie.membre",
        inverse_name="telephone_type_3",
        help="Membre 2 Ids relation",
    )

    membre_ids = fields.One2many(
        comodel_name="accorderie.membre",
        inverse_name="telephone_type_2",
        help="Membre Ids relation",
    )

    nom = fields.Char()
