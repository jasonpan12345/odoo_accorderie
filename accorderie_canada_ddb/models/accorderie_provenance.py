from odoo import _, api, models, fields


class AccorderieProvenance(models.Model):
    _name = "accorderie.provenance"
    _description = "Accorderie Provenance"
    _rec_name = "nom"

    membre = fields.One2many(
        comodel_name="accorderie.membre",
        inverse_name="provenance",
        help="Membre relation",
    )

    nom = fields.Char(string="Provenance")
