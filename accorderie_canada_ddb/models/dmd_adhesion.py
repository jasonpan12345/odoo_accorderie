from odoo import _, api, models, fields


class DmdAdhesion(models.Model):
    _name = "dmd.adhesion"
    _description = "Model Dmd_adhesion belonging to Module Tbl"

    courriel = fields.Char()

    datemaj = fields.Datetime()

    enattente = fields.Integer()

    name = fields.Char()

    noaccorderie = fields.Integer(required=True)

    nodmdadhesion = fields.Integer(required=True)

    nom = fields.Char()

    poste = fields.Char()

    prenom = fields.Char()

    supprimer = fields.Integer()

    telephone = fields.Char()

    transferer = fields.Integer()
