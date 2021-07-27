from odoo import _, api, models, fields


class Membre(models.Model):
    _name = "membre"
    _description = "Model Membre belonging to Module Tbl"

    achatregrouper = fields.Integer(string="Field Achatregrouper")

    adresse = fields.Char(string="Field Adresse")

    anneenaissance = fields.Integer(string="Field Anneenaissance")

    bottincourriel = fields.Integer(string="Field Bottincourriel")

    bottintel = fields.Integer(string="Field Bottintel")

    codepostal = fields.Char(string="Field Codepostal")

    courriel = fields.Char(string="Field Courriel")

    date_maj_membre = fields.Datetime(string="Field Date_maj_membre")

    dateadhesion = fields.Date(string="Field Dateadhesion")

    descriptionaccordeur = fields.Char(string="Field Descriptionaccordeur")

    etatcomptecourriel = fields.Integer(string="Field Etatcomptecourriel")

    membreactif = fields.Integer(string="Field Membreactif")

    membreca = fields.Integer(string="Field Membreca")

    membreconjoint = fields.Integer(string="Field Membreconjoint")

    membreprinc = fields.Integer(string="Field Membreprinc")

    memo = fields.Text(string="Field Memo")

    motdepasse = fields.Char(string="Field Motdepasse")

    name = fields.Char(string="Field Name")

    noaccorderie = fields.Integer(
        string="Field Noaccorderie",
        required=True,
    )

    noarrondissement = fields.Integer(string="Field Noarrondissement")

    nocartier = fields.Integer(string="Field Nocartier")

    nom = fields.Char(string="Field Nom")

    nomaccorderie = fields.Char(string="Field Nomaccorderie")

    nomembre = fields.Integer(
        string="Field Nomembre",
        required=True,
    )

    nomembreconjoint = fields.Integer(string="Field Nomembreconjoint")

    nomutilisateur = fields.Char(string="Field Nomutilisateur")

    nooccupation = fields.Integer(
        string="Field Nooccupation",
        required=True,
    )

    noorigine = fields.Integer(
        string="Field Noorigine",
        required=True,
    )

    nopointservice = fields.Integer(string="Field Nopointservice")

    noprovenance = fields.Integer(
        string="Field Noprovenance",
        required=True,
    )

    noregion = fields.Integer(
        string="Field Noregion",
        required=True,
    )

    norevenufamilial = fields.Integer(
        string="Field Norevenufamilial",
        required=True,
    )

    nosituationmaison = fields.Integer(
        string="Field Nosituationmaison",
        required=True,
    )

    notypecommunication = fields.Integer(
        string="Field Notypecommunication",
        required=True,
    )

    notypetel1 = fields.Integer(string="Field Notypetel1")

    notypetel2 = fields.Integer(string="Field Notypetel2")

    notypetel3 = fields.Integer(string="Field Notypetel3")

    noville = fields.Integer(
        string="Field Noville",
        required=True,
    )

    partsocialpaye = fields.Integer(string="Field Partsocialpaye")

    pascommunication = fields.Integer(string="Field Pascommunication")

    postetel1 = fields.Char(string="Field Postetel1")

    postetel2 = fields.Char(string="Field Postetel2")

    postetel3 = fields.Char(string="Field Postetel3")

    precisezorigine = fields.Char(string="Field Precisezorigine")

    prenom = fields.Char(string="Field Prenom")

    pretactif = fields.Integer(string="Field Pretactif")

    pretpayer = fields.Integer(string="Field Pretpayer")

    pretradier = fields.Integer(string="Field Pretradier")

    profilapprouver = fields.Integer(string="Field Profilapprouver")

    recevoircourrielgrp = fields.Integer(string="Field Recevoircourrielgrp")

    sexe = fields.Integer(string="Field Sexe")

    telephone1 = fields.Char(string="Field Telephone1")

    telephone2 = fields.Char(string="Field Telephone2")

    telephone3 = fields.Char(string="Field Telephone3")

    transferede = fields.Integer(string="Field Transferede")
