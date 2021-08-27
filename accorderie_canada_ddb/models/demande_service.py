from odoo import _, api, models, fields


class DemandeService(models.Model):
    _name = "demande.service"
    _description = "Model Demande_service belonging to Module Tbl"

    approuve = fields.Integer()

    datedebut = fields.Date()

    datefin = fields.Date()

    description = fields.Char()

    name = fields.Char()

    noaccorderie = fields.Many2one(comodel_name="accorderie")

    nomembre = fields.Many2one(comodel_name="membre")

    supprimer = fields.Integer()

    titredemande = fields.Char()

    transmit = fields.Integer()
