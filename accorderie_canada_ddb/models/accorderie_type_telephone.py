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
        string="Membre 1",
        help="Membre 1 relation",
    )

    membre_2_ids = fields.One2many(
        comodel_name="accorderie.membre",
        inverse_name="telephone_type_3",
        string="Membre 3",
        help="Membre 3 relation",
    )

    membre_ids = fields.One2many(
        comodel_name="accorderie.membre",
        inverse_name="telephone_type_2",
        string="Membre 2",
        help="Membre 2 relation",
    )

    def _compute_access_url(self):
        super(AccorderieTypeTelephone, self)._compute_access_url()
        for accorderie_type_telephone in self:
            accorderie_type_telephone.access_url = (
                "/my/accorderie_type_telephone/%s"
                % accorderie_type_telephone.id
            )
