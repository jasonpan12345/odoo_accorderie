from odoo import _, api, models, fields


class AccorderieProvenance(models.Model):
    _name = "accorderie.provenance"
    _inherit = "portal.mixin"
    _description = "Accorderie Provenance"
    _rec_name = "nom"

    membre = fields.One2many(
        comodel_name="accorderie.membre",
        inverse_name="provenance",
        help="Membre relation",
    )

    nom = fields.Char(string="Provenance")

    def _compute_access_url(self):
        super(AccorderieProvenance, self)._compute_access_url()
        for accorderie_provenance in self:
            accorderie_provenance.access_url = (
                "/my/accorderie_provenance/%s" % accorderie_provenance.id
            )
