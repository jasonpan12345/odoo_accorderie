from odoo import _, api, fields, models


class AccorderieVille(models.Model):
    _name = "accorderie.ville"
    _inherit = "portal.mixin"
    _description = "Accorderie Ville"
    _rec_name = "nom"

    nom = fields.Char()

    accorderie = fields.One2many(
        comodel_name="accorderie.accorderie",
        inverse_name="ville",
        help="Accorderie relation",
    )

    arrondissement = fields.One2many(
        comodel_name="accorderie.arrondissement",
        inverse_name="ville",
        help="Arrondissement relation",
    )

    code = fields.Integer(
        required=True,
        help="Code de la ville",
    )

    membre = fields.One2many(
        comodel_name="accorderie.membre",
        inverse_name="ville",
        help="Membre relation",
    )

    region = fields.Many2one(
        comodel_name="accorderie.region",
        string="Région",
    )

    def _compute_access_url(self):
        super(AccorderieVille, self)._compute_access_url()
        for accorderie_ville in self:
            accorderie_ville.access_url = (
                "/my/accorderie_ville/%s" % accorderie_ville.id
            )
