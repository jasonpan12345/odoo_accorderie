from odoo import _, api, models, fields


class AccorderieDemandeService(models.Model):
    _name = "accorderie.demande.service"
    _description = "Accorderie Demande Service"

    approuve = fields.Integer()

    datedebut = fields.Date()

    datefin = fields.Date()

    description = fields.Char()

    name = fields.Char()

    noaccorderie = fields.Many2one(comodel_name="accorderie.accorderie")

    nomembre = fields.Many2one(comodel_name="accorderie.membre")

    supprimer = fields.Integer()

    titredemande = fields.Char()

    transmit = fields.Integer()
