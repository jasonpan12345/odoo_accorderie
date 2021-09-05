from odoo import _, api, models, fields


class AccorderieRevenuFamilial(models.Model):
    _name = "accorderie.revenu.familial"
    _description = "Accorderie Revenu Familial"
    _rec_name = "nom"

    nom = fields.Char(string="Revenu")
