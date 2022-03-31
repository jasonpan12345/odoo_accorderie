from odoo import _, api, fields, models


class CommandeMembre(models.Model):
    _name = "commande.membre"
    _description = "Model Commande_membre belonging to Module Tbl"

    archivesoustotal = fields.Float(string="Field Archivesoustotal")

    archivetotmajoration = fields.Float(string="Field Archivetotmajoration")

    archivetottxfed = fields.Float(string="Field Archivetottxfed")

    archivetottxprov = fields.Float(string="Field Archivetottxprov")

    cmdconfirmer = fields.Integer(string="Field Cmdconfirmer")

    coutunitaireajour = fields.Integer(string="Field Coutunitaireajour")

    datecmdmb = fields.Datetime(string="Field Datecmdmb")

    datefacture = fields.Date(string="Field Datefacture")

    datemaj_cmdmembre = fields.Datetime(string="Field Datemaj_cmdmembre")

    facturer = fields.Integer(string="Field Facturer")

    montantpaiement = fields.Float(string="Field Montantpaiement")

    name = fields.Char(string="Field Name")

    nocommande = fields.Integer(
        string="Field Nocommande",
        required=True,
    )

    nocommandemembre = fields.Integer(
        string="Field Nocommandemembre",
        required=True,
    )

    nomembre = fields.Integer(
        string="Field Nomembre",
        required=True,
    )

    numrefmembre = fields.Integer(string="Field Numrefmembre")
