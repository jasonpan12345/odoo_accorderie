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

    nodemandeservice = fields.Many2one(comodel_name="demande.service")

    nomcomite = fields.Char()

    nomembresource = fields.Many2one(
        comodel_name="membre",
        required=True,
    )

    nomembreviser = fields.Many2one(comodel_name="membre")

    nomemployer = fields.Char()

    nooffreservicemembre = fields.Many2one(comodel_name="offre.service.membre")

    nopointservice = fields.Many2one(
        comodel_name="pointservice",
        required=True,
    )

    noteadministrative = fields.Text()

    resumersituation = fields.Text()

    satisfactioninsatisfaction = fields.Integer()

    siconfidentiel = fields.Integer()

    situation_impliquant = fields.Integer(string="Situation impliquant")

    solutionpourregler = fields.Text()

    typeoffre = fields.Integer()
