from odoo import _, api, models, fields


class AccorderieProvenance(models.Model):
    _name = "accorderie.provenance"
    _description = "Accorderie Provenance"
    _rec_name = "nom"

    nom = fields.Char(string="Provenance")
