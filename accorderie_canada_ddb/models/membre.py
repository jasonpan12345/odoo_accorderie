from odoo import _, api, models, fields


class Membre(models.Model):
    _name = "membre"
    _description = "Model Membre belonging to Module Tbl"

    achatregrouper = fields.Integer()

    adresse = fields.Char()

    anneenaissance = fields.Integer()

    bottincourriel = fields.Integer()

    bottintel = fields.Integer()

    codepostal = fields.Char()

    courriel = fields.Char()

    date_maj_membre = fields.Datetime(string="Date maj membre")

    dateadhesion = fields.Date()

    descriptionaccordeur = fields.Char()

    etatcomptecourriel = fields.Integer()

    membreactif = fields.Integer()

    membreca = fields.Integer()

    membreconjoint = fields.Integer()

    membreprinc = fields.Integer()

    memo = fields.Text()

    motdepasse = fields.Char()

    name = fields.Char()

    noaccorderie = fields.Integer(required=True)

    noarrondissement = fields.Integer()

    nocartier = fields.Integer()

    nom = fields.Char()

    nomaccorderie = fields.Char()

    nomembre = fields.Integer(required=True)

    nomembreconjoint = fields.Integer()

    nomutilisateur = fields.Char()

    nooccupation = fields.Integer(required=True)

    noorigine = fields.Integer(required=True)

    nopointservice = fields.Integer()

    noprovenance = fields.Integer(required=True)

    noregion = fields.Integer(required=True)

    norevenufamilial = fields.Integer(required=True)

    nosituationmaison = fields.Integer(required=True)

    notypecommunication = fields.Integer(required=True)

    notypetel1 = fields.Integer()

    notypetel2 = fields.Integer()

    notypetel3 = fields.Integer()

    noville = fields.Integer(required=True)

    partsocialpaye = fields.Integer()

    pascommunication = fields.Integer()

    postetel1 = fields.Char()

    postetel2 = fields.Char()

    postetel3 = fields.Char()

    precisezorigine = fields.Char()

    prenom = fields.Char()

    pretactif = fields.Integer()

    pretpayer = fields.Integer()

    pretradier = fields.Integer()

    profilapprouver = fields.Integer()

    recevoircourrielgrp = fields.Integer()

    sexe = fields.Integer()

    telephone1 = fields.Char()

    telephone2 = fields.Char()

    telephone3 = fields.Char()

    transferede = fields.Integer()
