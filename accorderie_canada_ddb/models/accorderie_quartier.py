from odoo import _, api, models, fields


class AccorderieQuartier(models.Model):
    _name = "accorderie.quartier"
    _inherit = "portal.mixin"
    _description = "Accorderie Quartier"
    _rec_name = "nom"

    arrondissement = fields.Many2one(
        comodel_name="accorderie.arrondissement",
        required=True,
        help="Arrondissement associé au quartier",
    )

    membre = fields.One2many(
        comodel_name="accorderie.membre",
        inverse_name="quartier",
        help="Membre relation",
    )

    nom = fields.Char(
        string="Nom du quartier",
        help="Nom du quartier",
    )

    def _compute_access_url(self):
        super(AccorderieQuartier, self)._compute_access_url()
        for accorderie_quartier in self:
            accorderie_quartier.access_url = (
                "/my/accorderie_quartier/%s" % accorderie_quartier.id
            )
