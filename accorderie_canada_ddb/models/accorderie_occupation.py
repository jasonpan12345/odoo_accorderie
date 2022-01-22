from odoo import _, api, fields, models


class AccorderieOccupation(models.Model):
    _name = "accorderie.occupation"
    _inherit = "portal.mixin"
    _description = "Accorderie Occupation"
    _rec_name = "nom"

    nom = fields.Char(string="Occupation")

    membre = fields.One2many(
        comodel_name="accorderie.membre",
        inverse_name="occupation",
        help="Membre relation",
    )

    def _compute_access_url(self):
        super(AccorderieOccupation, self)._compute_access_url()
        for accorderie_occupation in self:
            accorderie_occupation.access_url = (
                "/my/accorderie_occupation/%s" % accorderie_occupation.id
            )
