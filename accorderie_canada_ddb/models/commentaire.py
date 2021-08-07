from odoo import _, api, models, fields


class Commentaire(models.Model):
    _name = "commentaire"
    _description = "Model Commentaire belonging to Module Tbl"

    autrecommentaire = fields.Text()

    autresituation = fields.Char()

    consulteraccorderie = fields.Integer()

    consulterreseau = fields.Integer()

    dateheureajout = fields.Datetime()

    dateincident = fields.Date()

    datemaj_commentaire = fields.Datetime(string="Datemaj commentaire")

    demarche = fields.Text()

    name = fields.Char()

    nocommentaire = fields.Integer(required=True)

    nodemandeservice = fields.Integer()

    nomcomite = fields.Char()

    nomembresource = fields.Integer(required=True)

    nomembreviser = fields.Integer()

    nomemployer = fields.Char()

    nooffreservicemembre = fields.Integer()

    nopointservice = fields.Integer(required=True)

    noteadministrative = fields.Text()

    resumersituation = fields.Text()

    satisfactioninsatisfaction = fields.Integer()

    siconfidentiel = fields.Integer()

    situation_impliquant = fields.Integer(string="Situation impliquant")

    solutionpourregler = fields.Text()

    typeoffre = fields.Integer()
