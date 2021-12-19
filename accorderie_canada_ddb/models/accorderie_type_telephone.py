from odoo import _, api, fields, models


class AccorderieTypeTelephone(models.Model):
    _name = "accorderie.type.telephone"
    _inherit = "portal.mixin"
    _description = "Accorderie Type Telephone"
    _rec_name = "nom"

    nom = fields.Char()

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

    def _compute_access_url(self):
        super(AccorderieTypeTelephone, self)._compute_access_url()
        for accorderie_type_telephone in self:
            accorderie_type_telephone.access_url = (
                "/my/accorderie_type_telephone/%s"
                % accorderie_type_telephone.id
            )
