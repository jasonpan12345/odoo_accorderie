# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging
from datetime import datetime

from pytz import timezone

from odoo import SUPERUSER_ID, _, api, tools

_logger = logging.getLogger(__name__)
tz_montreal = timezone("America/Montreal")


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


def post_init_hook(cr, e):
    with api.Environment.manage():
        env = api.Environment(cr, SUPERUSER_ID, {})

        # All demo user is already accepted from list
        adhesion_ids = env["accorderie.demande.adhesion"].search([])
        for adhesion_id in adhesion_ids:
            adhesion_id.en_attente = False

        website_accueil = env["ir.ui.view"].search(
            [("key", "=", "website.accueil")]
        )
        arch = website_accueil.arch
        last_index = arch.find("</h1>") + 6
        html_message = f"""                    <div class="s_alert s_alert_md alert-delta w-100 clearfix">
                      <i class="fa fa-2x fa-info-circle s_alert_icon"/>
                      <div class="s_alert_content">
                        <p data-original-title="" title="" aria-describedby="tooltip23978">Ceci est une démonstration, les données sont fictives et toutes les données seront purgées à la prochaine mise à jour. Dernière mise à jour le {datetime.now(tz_montreal).strftime('%d %B %Y')}.<br/></p>
                      </div>
                    </div>"""
        arch = arch[:last_index] + html_message + arch[last_index:]
        website_accueil.arch = arch
        website_accueil.arch_base = arch

        # TODO can move this in data
        env.ref(
            "demo_accorderie_canada_ddb.accorderie_membre_administrateur_mathieu_benoit"
        ).write(
            {
                "membre_favoris_ids": [
                    (
                        4,
                        env.ref(
                            "demo_accorderie_canada_ddb.accorderie_membre_favoris_martin_petit"
                        ).id,
                    ),
                    (
                        4,
                        env.ref(
                            "demo_accorderie_canada_ddb.accorderie_membre_favoris_administrateur_mathieu_benoit"
                        ).id,
                    ),
                    (
                        4,
                        env.ref(
                            "demo_accorderie_canada_ddb.accorderie_membre_favoris_alice_poitier"
                        ).id,
                    ),
                ]
            }
        )

        env.ref(
            "demo_accorderie_canada_ddb.accorderie_membre_denis_lemarchand"
        ).write(
            {
                "membre_favoris_ids": [
                    (
                        4,
                        env.ref(
                            "demo_accorderie_canada_ddb.accorderie_membre_favoris_martin_petit"
                        ).id,
                    ),
                    (
                        4,
                        env.ref(
                            "demo_accorderie_canada_ddb.accorderie_membre_favoris_administrateur_mathieu_benoit"
                        ).id,
                    ),
                ]
            }
        )

        # General configuration
        values = {
            "accorderie_auto_accept_adhesion": True,
        }
        event_config = env["res.config.settings"].sudo().create(values)
        event_config.execute()
