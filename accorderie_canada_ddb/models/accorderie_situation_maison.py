from odoo import _, api, models, fields


class AccorderieSituationMaison(models.Model):
    _name = "accorderie.situation.maison"
    _inherit = "portal.mixin"
    _description = "Accorderie Situation Maison"
    _rec_name = "nom"

    membre = fields.One2many(
        comodel_name="accorderie.membre",
        inverse_name="situation_maison",
        help="Membre relation",
    )

    nom = fields.Char(string="Situation")

    def _compute_access_url(self):
        super(AccorderieSituationMaison, self)._compute_access_url()
        for accorderie_situation_maison in self:
            accorderie_situation_maison.access_url = (
                "/my/accorderie_situation_maison/%s"
                % accorderie_situation_maison.id
            )
