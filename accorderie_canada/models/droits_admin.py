from odoo import _, api, models, fields


class DroitsAdmin(models.Model):
    _name = "droits.admin"
    _description = "Model Droits_admin belonging to Module Tbl"

    consulteretatcompte = fields.Integer(string="Field Consulteretatcompte")

    consulterprofil = fields.Integer(string="Field Consulterprofil")

    gestioncatsouscat = fields.Integer(string="Field Gestioncatsouscat")

    gestiondmd = fields.Integer(string="Field Gestiondmd")

    gestionfichier = fields.Integer(string="Field Gestionfichier")

    gestionoffre = fields.Integer(string="Field Gestionoffre")

    gestionoffremembre = fields.Integer(string="Field Gestionoffremembre")

    gestionprofil = fields.Integer(string="Field Gestionprofil")

    groupeachat = fields.Integer(string="Field Groupeachat")

    name = fields.Char(string="Field Name")

    nomembre = fields.Integer(
        string="Field Nomembre",
        required=True,
    )

    saisieechange = fields.Integer(string="Field Saisieechange")

    validation = fields.Integer(string="Field Validation")
