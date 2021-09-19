from odoo import _, api, models, fields


class AccorderiePointService(models.Model):
    _name = "accorderie.point.service"
    _description = "Accorderie Point Service"
    _rec_name = "nom"

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

    nom = fields.Char(help="Nom du point de service")

    sequence = fields.Integer(
        string="Séquence",
        help="Séquence d'affichage",
    )
