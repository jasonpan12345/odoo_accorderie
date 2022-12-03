import logging
from datetime import datetime

from odoo import _, api, fields, models

_logger = logging.getLogger(__name__)


class AccorderieChatMessage(models.Model):
    _name = "accorderie.chat.message"
    _description = "Accorderie chat message"

    name = fields.Char()

    active = fields.Boolean(default=True)

    is_read = fields.Boolean(
        string="Is read", help="La notification a été lu par le membre."
    )

    membre_writer_id = fields.Many2one(
        comodel_name="accorderie.membre",
        string="Membre writer",
        help="Membre qui écrit ce message.",
    )

    msg_group_id = fields.Many2one(
        comodel_name="accorderie.chat.group",
        string="Groupe",
    )

    def first_to_json(self):
        obj = self[0]
        data = {
            "id": obj.id,
            "name": obj.name,
            "is_read": obj.is_read,
            "m_id": obj.membre_writer_id.id,
        }
        return data

    @api.model_create_multi
    def create(self, vals_list):
        res = super().create(vals_list)
        for rec in res:
            data = rec.first_to_json()
            data["group_id"] = rec.msg_group_id.id
            for membre_id in rec.msg_group_id.membre_ids:
                # Update value for the other member
                other_membre_id = [
                    a
                    for a in rec.msg_group_id.membre_ids
                    if a.id != membre_id.id
                ][0]
                data["membre_id"] = other_membre_id.id
                data["membre_name"] = other_membre_id.nom_complet

                self.env["bus.bus"].sendone(
                    # f'["{self._cr.dbname}","{self._name}",{rec.id}]',
                    "accorderie.notification.message",
                    {
                        "timestamp": str(datetime.now()),
                        "data": data,
                        "field_id": rec.id,
                        "canal": f'["{self._cr.dbname}","{self._name}",{membre_id.id}]',
                    },
                )
        return res
