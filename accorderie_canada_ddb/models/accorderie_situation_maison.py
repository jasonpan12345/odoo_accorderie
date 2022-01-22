from odoo import _, api, fields, models


class AccorderieSituationMaison(models.Model):
    _name = "accorderie.situation.maison"
    _inherit = "portal.mixin"
    _description = "Accorderie Situation Maison"
    _rec_name = "nom"

    nom = fields.Char(string="Situation")

    membre = fields.One2many(
        comodel_name="accorderie.membre",
        inverse_name="situation_maison",
        help="Membre relation",
    )

    def _compute_access_url(self):
        super(AccorderieSituationMaison, self)._compute_access_url()
        for accorderie_situation_maison in self:
            accorderie_situation_maison.access_url = (
                "/my/accorderie_situation_maison/%s"
                % accorderie_situation_maison.id
            )
