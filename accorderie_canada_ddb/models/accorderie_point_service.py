from odoo import _, api, fields, models


class AccorderiePointService(models.Model):
    _name = "accorderie.point.service"
    _inherit = "portal.mixin"
    _description = "Accorderie Point Service"
    _rec_name = "nom"

    nom = fields.Char(help="Nom du point de service")

    accorderie = fields.Many2one(
        comodel_name="accorderie.accorderie",
        required=True,
    )

    commentaire = fields.One2many(
        comodel_name="accorderie.commentaire",
        inverse_name="point_service",
        help="Commentaire relation",
    )

    date_mise_a_jour = fields.Datetime(
        string="Dernière mise à jour",
        help="Date de la dernière mise à jour",
    )

    membre = fields.One2many(
        comodel_name="accorderie.membre",
        inverse_name="point_service",
        help="Membre relation",
    )

    sequence = fields.Integer(
        string="Séquence",
        help="Séquence d'affichage",
    )

    def _compute_access_url(self):
        super(AccorderiePointService, self)._compute_access_url()
        for accorderie_point_service in self:
            accorderie_point_service.access_url = (
                "/my/accorderie_point_service/%s" % accorderie_point_service.id
            )
