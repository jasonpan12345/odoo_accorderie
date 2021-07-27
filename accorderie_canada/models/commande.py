from odoo import _, api, models, fields


class Commande(models.Model):
    _name = "commande"
    _description = "Model Commande belonging to Module Tbl"

    commandetermine = fields.Integer(string="Field Commandetermine")

    datecmddebut = fields.Date(string="Field Datecmddebut")

    datecmdfin = fields.Date(string="Field Datecmdfin")

    datecueillette = fields.Date(string="Field Datecueillette")

    datemaj_cmd = fields.Datetime(string="Field Datemaj_cmd")

    majoration = fields.Float(string="Field Majoration")

    name = fields.Char(string="Field Name")

    nocommande = fields.Integer(
        string="Field Nocommande",
        required=True,
    )

    nopointservice = fields.Integer(
        string="Field Nopointservice",
        required=True,
    )

    norefcommande = fields.Integer(string="Field Norefcommande")

    taxefcommande = fields.Float(string="Field Taxefcommande")

    taxepcommande = fields.Float(string="Field Taxepcommande")
