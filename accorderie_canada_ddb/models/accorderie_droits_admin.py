from odoo import _, api, models, fields


class AccorderieDroitsAdmin(models.Model):
    _name = "accorderie.droits.admin"
    _description = "Accorderie Droits Admin"

    consulteretatcompte = fields.Integer()

    consulterprofil = fields.Integer()

    gestioncatsouscat = fields.Integer()

    gestiondmd = fields.Integer()

    gestionfichier = fields.Integer()

    gestionoffre = fields.Integer()

    gestionoffremembre = fields.Integer()

    gestionprofil = fields.Integer()

    groupeachat = fields.Integer()

    name = fields.Char()

    nomembre = fields.Many2one(comodel_name="accorderie.membre")

    saisieechange = fields.Integer()

    validation = fields.Integer()
