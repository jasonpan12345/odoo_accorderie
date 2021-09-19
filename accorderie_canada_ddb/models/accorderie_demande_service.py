from odoo import _, api, models, fields


class AccorderieDemandeService(models.Model):
    _name = "accorderie.demande.service"
    _description = "Accorderie Demande Service"
    _rec_name = "titre"

    accorderie = fields.Many2one(comodel_name="accorderie.accorderie")

    active = fields.Boolean(
        string="Actif",
        default=True,
        help=(
            "Lorsque non actif, cet demande de services n'est plus en"
            " fonction, mais demeure accessible."
        ),
    )

    approuver = fields.Boolean(
        string="Approuvé",
        help="Permet d'approuver cette demande de service.",
    )

    commentaire = fields.One2many(
        comodel_name="accorderie.commentaire",
        inverse_name="demande_service_id",
        help="Commentaire relation",
    )

    date_debut = fields.Date(string="Date début")

    date_fin = fields.Date(string="Date fin")

    description = fields.Char()

    membre = fields.Many2one(comodel_name="accorderie.membre")

    titre = fields.Char()
