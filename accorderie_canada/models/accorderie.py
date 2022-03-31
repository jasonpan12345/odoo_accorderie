from odoo import _, api, fields, models


class Accorderie(models.Model):
    _name = "accorderie"
    _description = "Model Accorderie belonging to Module Tbl"

    adresseaccorderie = fields.Char(string="Field Adresseaccorderie")

    codepostalaccorderie = fields.Char(string="Field Codepostalaccorderie")

    courrielaccorderie = fields.Char(string="Field Courrielaccorderie")

    datemaj_accorderie = fields.Datetime(string="Field Datemaj_accorderie")

    grpachat_accordeur = fields.Integer(string="Field Grpachat_accordeur")

    grpachat_admin = fields.Integer(string="Field Grpachat_admin")

    messageaccueil = fields.Text(string="Field Messageaccueil")

    messagegrpachat = fields.Text(string="Field Messagegrpachat")

    name = fields.Char(string="Field Name")

    noaccorderie = fields.Integer(
        string="Field Noaccorderie",
        required=True,
    )

    noarrondissement = fields.Integer(string="Field Noarrondissement")

    nocartier = fields.Integer(string="Field Nocartier")

    nom = fields.Char(string="Field Nom")

    nomcomplet = fields.Char(
        string="Field Nomcomplet",
        required=True,
    )

    nonvisible = fields.Integer(string="Field Nonvisible")

    noregion = fields.Integer(
        string="Field Noregion",
        required=True,
    )

    noville = fields.Integer(
        string="Field Noville",
        required=True,
    )

    telaccorderie = fields.Char(string="Field Telaccorderie")

    telecopieuraccorderie = fields.Char(string="Field Telecopieuraccorderie")

    url_logoaccorderie = fields.Char(string="Field Url_logoaccorderie")

    url_public_accorderie = fields.Char(string="Field Url_public_accorderie")

    url_transac_accorderie = fields.Char(string="Field Url_transac_accorderie")
