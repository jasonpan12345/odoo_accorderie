from odoo import _, api, fields, models


class AccorderieOrigine(models.Model):
    _name = "accorderie.origine"
    _inherit = "portal.mixin"
    _description = "Accorderie Origine"
    _rec_name = "nom"

    nom = fields.Char(string="Origine")

    membre = fields.One2many(
        comodel_name="accorderie.membre",
        inverse_name="origine",
        help="Membre relation",
    )

    def _compute_access_url(self):
        super(AccorderieOrigine, self)._compute_access_url()
        for accorderie_origine in self:
            accorderie_origine.access_url = (
                "/my/accorderie_origine/%s" % accorderie_origine.id
            )
