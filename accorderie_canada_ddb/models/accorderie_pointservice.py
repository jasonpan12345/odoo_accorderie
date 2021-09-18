from odoo import _, api, models, fields


class AccorderiePointservice(models.Model):
    _name = "accorderie.pointservice"
    _description = "Accorderie Pointservice"
    _rec_name = "nom"

    date_mise_a_jour = fields.Datetime(
        string="Dernière mise à jour",
        help="Date de la dernière mise à jour",
    )

    membre = fields.One2many(
        comodel_name="accorderie.membre",
        inverse_name="point_service",
        help="Membre relation",
    )

    noaccorderie = fields.Many2one(
        comodel_name="accorderie.accorderie",
        required=True,
    )

    nom = fields.Char(help="Nom du point de service")

    sequence = fields.Integer(
        string="Séquence",
        help="Séquence d'affichage",
    )
