from odoo import _, api, models, fields


class Commentaire(models.Model):
    _name = "commentaire"
    _description = "Model Commentaire belonging to Module Tbl"

    autrecommentaire = fields.Text(string="Field Autrecommentaire")

    autresituation = fields.Char(string="Field Autresituation")

    consulteraccorderie = fields.Integer(string="Field Consulteraccorderie")

    consulterreseau = fields.Integer(string="Field Consulterreseau")

    dateheureajout = fields.Datetime(string="Field Dateheureajout")

    dateincident = fields.Date(string="Field Dateincident")

    datemaj_commentaire = fields.Datetime(string="Field Datemaj_commentaire")

    demarche = fields.Text(string="Field Demarche")

    name = fields.Char(string="Field Name")

    nocommentaire = fields.Integer(
        string="Field Nocommentaire",
        required=True,
    )

    nodemandeservice = fields.Integer(string="Field Nodemandeservice")

    nomcomite = fields.Char(string="Field Nomcomite")

    nomembresource = fields.Integer(
        string="Field Nomembresource",
        required=True,
    )

    nomembreviser = fields.Integer(string="Field Nomembreviser")

    nomemployer = fields.Char(string="Field Nomemployer")

    nooffreservicemembre = fields.Integer(string="Field Nooffreservicemembre")

    nopointservice = fields.Integer(
        string="Field Nopointservice",
        required=True,
    )

    noteadministrative = fields.Text(string="Field Noteadministrative")

    resumersituation = fields.Text(string="Field Resumersituation")

    satisfactioninsatisfaction = fields.Integer(
        string="Field Satisfactioninsatisfaction"
    )

    siconfidentiel = fields.Integer(string="Field Siconfidentiel")

    situation_impliquant = fields.Integer(string="Field Situation_impliquant")

    solutionpourregler = fields.Text(string="Field Solutionpourregler")

    typeoffre = fields.Integer(string="Field Typeoffre")
