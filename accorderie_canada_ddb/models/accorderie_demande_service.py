from odoo import _, api, fields, models


class AccorderieDemandeService(models.Model):
    _name = "accorderie.demande.service"
    _inherit = "portal.mixin"
    _description = "Accorderie Demande Service"
    _rec_name = "titre"

    titre = fields.Char()

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

    type_service_id = fields.Many2one(
        comodel_name="accorderie.type.service",
        string="Type de services",
    )

    def _compute_access_url(self):
        super(AccorderieDemandeService, self)._compute_access_url()
        for accorderie_demande_service in self:
            accorderie_demande_service.access_url = (
                "/my/accorderie_demande_service/%s"
                % accorderie_demande_service.id
            )
