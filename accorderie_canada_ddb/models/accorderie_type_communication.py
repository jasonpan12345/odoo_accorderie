from odoo import _, api, models, fields


class AccorderieTypeCommunication(models.Model):
    _name = "accorderie.type.communication"
    _inherit = "portal.mixin"
    _description = "Accorderie Type Communication"
    _rec_name = "nom"

    membre = fields.One2many(
        comodel_name="accorderie.membre",
        inverse_name="type_communication",
        help="Membre relation",
    )

    nom = fields.Char(string="Typecommunication")

    def _compute_access_url(self):
        super(AccorderieTypeCommunication, self)._compute_access_url()
        for accorderie_type_communication in self:
            accorderie_type_communication.access_url = (
                "/my/accorderie_type_communication/%s"
                % accorderie_type_communication.id
            )
