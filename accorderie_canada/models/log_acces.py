from odoo import _, api, fields, models


class LogAcces(models.Model):
    _name = "log.acces"
    _description = "Model Log_acces belonging to Module Tbl"

    dateheure_deconnexion = fields.Datetime(
        string="Field Dateheure_deconnexion"
    )

    dateheureconnexion = fields.Datetime(string="Field Dateheureconnexion")

    id_log_acces = fields.Integer(
        string="Field Id_log_acces",
        required=True,
    )

    ip_client_v4 = fields.Char(string="Field Ip_client_v4")

    name = fields.Char(string="Field Name")

    navigateur = fields.Char(string="Field Navigateur")

    nomembre = fields.Integer(string="Field Nomembre")

    nomusageressayer = fields.Char(string="Field Nomusageressayer")

    referer = fields.Char(string="Field Referer")

    resolution_h = fields.Integer(string="Field Resolution_h")

    resolution_w = fields.Integer(string="Field Resolution_w")

    statut = fields.Char(string="Field Statut")
