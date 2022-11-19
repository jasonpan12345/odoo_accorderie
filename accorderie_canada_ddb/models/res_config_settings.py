from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    accorderie_auto_accept_adhesion = fields.Boolean(
        "Auto accept adhesion",
        config_parameter=(
            "accorderie_canada_ddb.accorderie_auto_accept_adhesion"
        ),
    )
