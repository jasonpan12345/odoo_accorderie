from odoo import _, api, models, fields


class DroitsAdmin(models.Model):
    _name = "droits.admin"
    _description = "Model Droits_admin belonging to Module Tbl"

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

    nomembre = fields.Integer()

    saisieechange = fields.Integer()

    validation = fields.Integer()
