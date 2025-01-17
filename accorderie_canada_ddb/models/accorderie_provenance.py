from odoo import _, api, fields, models


class AccorderieProvenance(models.Model):
    _name = "accorderie.provenance"
    _inherit = "portal.mixin"
    _description = "Accorderie Provenance"
    _rec_name = "nom"

    nom = fields.Char(string="Provenance")

    membre = fields.One2many(
        comodel_name="accorderie.membre",
        inverse_name="provenance",
        help="Membre relation",
    )

    def _compute_access_url(self):
        super(AccorderieProvenance, self)._compute_access_url()
        for accorderie_provenance in self:
            accorderie_provenance.access_url = (
                "/my/accorderie_provenance/%s" % accorderie_provenance.id
            )
