from odoo import _, api, fields, models


class DemandeService(models.Model):
    _name = "demande.service"
    _description = "Model Demande_service belonging to Module Tbl"

    approuve = fields.Integer(string="Field Approuve")

    datedebut = fields.Date(string="Field Datedebut")

    datefin = fields.Date(string="Field Datefin")

    description = fields.Char(string="Field Description")

    name = fields.Char(string="Field Name")

    noaccorderie = fields.Integer(string="Field Noaccorderie")

    nodemandeservice = fields.Integer(
        string="Field Nodemandeservice",
        required=True,
    )

    nomembre = fields.Integer(string="Field Nomembre")

    supprimer = fields.Integer(string="Field Supprimer")

    titredemande = fields.Char(string="Field Titredemande")

    transmit = fields.Integer(string="Field Transmit")
