from odoo import _, api, models, fields


class Commande(models.Model):
    _name = "commande"
    _description = "Model Commande belonging to Module Tbl"

    commandetermine = fields.Integer()

    datecmddebut = fields.Date()

    datecmdfin = fields.Date()

    datecueillette = fields.Date()

    datemaj_cmd = fields.Datetime(string="Datemaj cmd")

    majoration = fields.Float()

    name = fields.Char()

    nocommande = fields.Integer()

    nopointservice = fields.Integer(required=True)

    norefcommande = fields.Integer()

    taxefcommande = fields.Float()

    taxepcommande = fields.Float()
