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

    noaccorderie = fields.Many2one(
        comodel_name="accorderie",
        required=True,
    )

    noarrondissement = fields.Many2one(comodel_name="arrondissement")

    nocartier = fields.Many2one(comodel_name="cartier")

    nom = fields.Char()

    nomaccorderie = fields.Char()

    nomembre = fields.Integer(required=True)

    nomembreconjoint = fields.Integer()

    nomutilisateur = fields.Char()

    nooccupation = fields.Many2one(comodel_name="occupation")

    noorigine = fields.Many2one(comodel_name="origine")

    nopointservice = fields.Many2one(comodel_name="pointservice")

    noprovenance = fields.Many2one(comodel_name="provenance")

    noregion = fields.Many2one(
        comodel_name="region",
        required=True,
    )

    norevenufamilial = fields.Many2one(comodel_name="revenu.familial")

    nosituationmaison = fields.Many2one(comodel_name="situation.maison")

    notypecommunication = fields.Many2one(comodel_name="type.communication")

    notypetel1 = fields.Integer()

    notypetel2 = fields.Integer()

    notypetel3 = fields.Integer()

    noville = fields.Many2one(
        comodel_name="ville",
        required=True,
    )

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
