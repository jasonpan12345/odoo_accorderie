from odoo import _, api, models, fields


class LogAcces(models.Model):
    _name = "log.acces"
    _description = "Model Log_acces belonging to Module Tbl"

    dateheure_deconnexion = fields.Datetime(string="Dateheure deconnexion")

    dateheureconnexion = fields.Datetime()

    id_log_acces = fields.Integer(
        string="Id log acces",
        required=True,
    )

    ip_client_v4 = fields.Char(string="Ip client v4")

    name = fields.Char()

    navigateur = fields.Char()

    nomembre = fields.Many2one(comodel_name="membre")

    nomusageressayer = fields.Char()

    referer = fields.Char()

    resolution_h = fields.Integer(string="Resolution h")

    resolution_w = fields.Integer(string="Resolution w")

    statut = fields.Char()
