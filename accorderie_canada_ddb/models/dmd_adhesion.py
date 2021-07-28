from odoo import _, api, models, fields


class DmdAdhesion(models.Model):
    _name = "dmd.adhesion"
    _description = "Model Dmd_adhesion belonging to Module Tbl"

    courriel = fields.Char(string="Field Courriel")

    datemaj = fields.Datetime(string="Field Datemaj")

    enattente = fields.Integer(string="Field Enattente")

    name = fields.Char(string="Field Name")

    noaccorderie = fields.Integer(
        string="Field Noaccorderie",
        required=True,
    )

    nodmdadhesion = fields.Integer(
        string="Field Nodmdadhesion",
        required=True,
    )

    nom = fields.Char(string="Field Nom")

    poste = fields.Char(string="Field Poste")

    prenom = fields.Char(string="Field Prenom")

    supprimer = fields.Integer(string="Field Supprimer")

    telephone = fields.Char(string="Field Telephone")

    transferer = fields.Integer(string="Field Transferer")
