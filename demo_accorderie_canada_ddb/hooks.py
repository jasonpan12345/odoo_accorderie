# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

from odoo import SUPERUSER_ID, _, api, tools

_logger = logging.getLogger(__name__)


def pre_init_hook(cr):
    with api.Environment.manage():
        env = api.Environment(cr, SUPERUSER_ID, {})

        # Update all partner
        partners = env["res.partner"].search([("name", "=", "My Company")])
        for partner in partners:
            partner.website = "https://accorderie.ca"
            partner.name = "Accorderie"
            partner.email = "info@accorderie.ca"
            # partner.street = "850, rue St-Denis"
            # partner.street2 = "porte S03.900"
            partner.city = "Montréal"
            # partner.zip = "H2X 0A9"
            partner.country_id = env.ref("base.ca")
            partner.state_id = env["res.country.state"].search(
                [("code", "ilike", "QC")], limit=1
            )
            # partner.phone = "514 890-8000 poste 15488"

        partners = env["res.partner"].search([("name", "=", "Administrator")])
        for partner in partners:
            partner.website = "https://cimarlab.ca"
            partner.name = "Mathieu Benoit"
            partner.email = "mathieu.benoit@cimarlab.ca"
            partner.country_id = env.ref("base.ca")
            partner.state_id = env["res.country.state"].search(
                [("code", "ilike", "QC")], limit=1
            )
