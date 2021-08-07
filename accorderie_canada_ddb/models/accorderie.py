from odoo import _, api, models, fields


class Accorderie(models.Model):
    _name = "accorderie"
    _description = "Model Accorderie belonging to Module Tbl"

    adresseaccorderie = fields.Char()

    codepostalaccorderie = fields.Char()

    courrielaccorderie = fields.Char()

    datemaj_accorderie = fields.Datetime(string="Datemaj accorderie")

    grpachat_accordeur = fields.Integer(string="Grpachat accordeur")

    grpachat_admin = fields.Integer(string="Grpachat admin")

    messageaccueil = fields.Text()

    messagegrpachat = fields.Text()

    name = fields.Char()

    noaccorderie = fields.Integer(required=True)

    noarrondissement = fields.Integer()

    nocartier = fields.Integer()

    nom = fields.Char()

    nomcomplet = fields.Char(required=True)

    nonvisible = fields.Integer()

    noregion = fields.Integer(required=True)

    noville = fields.Integer(required=True)

    telaccorderie = fields.Char()

    telecopieuraccorderie = fields.Char()

    url_logoaccorderie = fields.Char(string="Url logoaccorderie")

    url_public_accorderie = fields.Char(string="Url public accorderie")

    url_transac_accorderie = fields.Char(string="Url transac accorderie")
