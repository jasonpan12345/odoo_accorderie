import logging

from odoo import _, api, fields, models

_logger = logging.getLogger(__name__)


class AccorderieEchangeServiceNotification(models.Model):
    _name = "accorderie.echange.service.notification"
    _description = "Accorderie Echange Service Notification"

    name = fields.Char()

    active = fields.Boolean(default=True)

    is_read = fields.Boolean(
        string="Is read", help="La notification a été lu par le membre."
    )

    type_notification = fields.Selection(
        [
            ("Nouvelle demande de service", "Nouvelle demande de service"),
            ("Réponse à votre demande", "Réponse à votre demande"),
            # ("Réponse à votre offre", "Réponse à votre offre"),
            ("Transaction validée", "Transaction validée"),
        ]
    )

    echange_service_id = fields.Many2one(
        comodel_name="accorderie.echange.service",
        string="Échange de service",
    )

    membre_id = fields.Many2one(
        comodel_name="accorderie.membre",
        string="Membre notifié",
    )
