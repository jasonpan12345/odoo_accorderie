from odoo import _, api, models, fields


class CommandeMembre(models.Model):
    _name = "commande.membre"
    _description = "Model Commande_membre belonging to Module Tbl"

    archivesoustotal = fields.Float()

    archivetotmajoration = fields.Float()

    archivetottxfed = fields.Float()

    archivetottxprov = fields.Float()

    cmdconfirmer = fields.Integer()

    coutunitaireajour = fields.Integer()

    datecmdmb = fields.Datetime()

    datefacture = fields.Date()

    datemaj_cmdmembre = fields.Datetime(string="Datemaj cmdmembre")

    facturer = fields.Integer()

    montantpaiement = fields.Float()

    name = fields.Char()

    nocommande = fields.Many2one(comodel_name="commande")

    nomembre = fields.Many2one(comodel_name="membre")

    numrefmembre = fields.Integer()
