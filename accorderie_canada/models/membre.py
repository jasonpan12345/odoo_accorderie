# -*- coding: utf-8 -*-

from odoo import api, models, fields


class Membre(models.Model):
    _name = 'membre'
    _description = 'Model Membre belonging to Module Tbl'

    achatregrouper = fields.Integer(
        string='Field Achatregrouper',
        copy=False,
    )

    adresse = fields.Char(
        string='Field Adresse',
        copy=False,
    )

    anneenaissance = fields.Integer(
        string='Field Anneenaissance',
        copy=False,
    )

    bottincourriel = fields.Integer(
        string='Field Bottincourriel',
        copy=False,
    )

    bottintel = fields.Integer(
        string='Field Bottintel',
        copy=False,
    )

    codepostal = fields.Char(
        string='Field Codepostal',
        copy=False,
    )

    courriel = fields.Char(
        string='Field Courriel',
        copy=False,
    )

    date_maj_membre = fields.Datetime(
        string='Field Date_maj_membre',
        copy=False,
    )

    dateadhesion = fields.Date(
        string='Field Dateadhesion',
        copy=False,
    )

    descriptionaccordeur = fields.Char(
        string='Field Descriptionaccordeur',
        copy=False,
    )

    etatcomptecourriel = fields.Integer(
        string='Field Etatcomptecourriel',
        copy=False,
    )

    membreactif = fields.Integer(
        string='Field Membreactif',
        copy=False,
    )

    membreca = fields.Integer(
        string='Field Membreca',
        copy=False,
    )

    membreconjoint = fields.Integer(
        string='Field Membreconjoint',
        copy=False,
    )

    membreprinc = fields.Integer(
        string='Field Membreprinc',
        copy=False,
    )

    memo = fields.Text(
        string='Field Memo',
        copy=False,
    )

    motdepasse = fields.Char(
        string='Field Motdepasse',
        copy=False,
    )

    name = fields.Char(
        string='Field Name',
        copy=False,
    )

    noaccorderie = fields.Integer(
        string='Field Noaccorderie',
        required=True,
        copy=False,
    )

    noarrondissement = fields.Integer(
        string='Field Noarrondissement',
        copy=False,
    )

    nocartier = fields.Integer(
        string='Field Nocartier',
        copy=False,
    )

    nom = fields.Char(
        string='Field Nom',
        copy=False,
    )

    nomaccorderie = fields.Char(
        string='Field Nomaccorderie',
        copy=False,
    )

    nomembre = fields.Integer(
        string='Field Nomembre',
        required=True,
        copy=False,
    )

    nomembreconjoint = fields.Integer(
        string='Field Nomembreconjoint',
        copy=False,
    )

    nomutilisateur = fields.Char(
        string='Field Nomutilisateur',
        copy=False,
    )

    nooccupation = fields.Integer(
        string='Field Nooccupation',
        required=True,
        copy=False,
    )

    noorigine = fields.Integer(
        string='Field Noorigine',
        required=True,
        copy=False,
    )

    nopointservice = fields.Integer(
        string='Field Nopointservice',
        copy=False,
    )

    noprovenance = fields.Integer(
        string='Field Noprovenance',
        required=True,
        copy=False,
    )

    noregion = fields.Integer(
        string='Field Noregion',
        required=True,
        copy=False,
    )

    norevenufamilial = fields.Integer(
        string='Field Norevenufamilial',
        required=True,
        copy=False,
    )

    nosituationmaison = fields.Integer(
        string='Field Nosituationmaison',
        required=True,
        copy=False,
    )

    notypecommunication = fields.Integer(
        string='Field Notypecommunication',
        required=True,
        copy=False,
    )

    notypetel1 = fields.Integer(
        string='Field Notypetel1',
        copy=False,
    )

    notypetel2 = fields.Integer(
        string='Field Notypetel2',
        copy=False,
    )

    notypetel3 = fields.Integer(
        string='Field Notypetel3',
        copy=False,
    )

    noville = fields.Integer(
        string='Field Noville',
        required=True,
        copy=False,
    )

    partsocialpaye = fields.Integer(
        string='Field Partsocialpaye',
        copy=False,
    )

    pascommunication = fields.Integer(
        string='Field Pascommunication',
        copy=False,
    )

    postetel1 = fields.Char(
        string='Field Postetel1',
        copy=False,
    )

    postetel2 = fields.Char(
        string='Field Postetel2',
        copy=False,
    )

    postetel3 = fields.Char(
        string='Field Postetel3',
        copy=False,
    )

    precisezorigine = fields.Char(
        string='Field Precisezorigine',
        copy=False,
    )

    prenom = fields.Char(
        string='Field Prenom',
        copy=False,
    )

    pretactif = fields.Integer(
        string='Field Pretactif',
        copy=False,
    )

    pretpayer = fields.Integer(
        string='Field Pretpayer',
        copy=False,
    )

    pretradier = fields.Integer(
        string='Field Pretradier',
        copy=False,
    )

    profilapprouver = fields.Integer(
        string='Field Profilapprouver',
        copy=False,
    )

    recevoircourrielgrp = fields.Integer(
        string='Field Recevoircourrielgrp',
        copy=False,
    )

    sexe = fields.Integer(
        string='Field Sexe',
        copy=False,
    )

    telephone1 = fields.Char(
        string='Field Telephone1',
        copy=False,
    )

    telephone2 = fields.Char(
        string='Field Telephone2',
        copy=False,
    )

    telephone3 = fields.Char(
        string='Field Telephone3',
        copy=False,
    )

    transferede = fields.Integer(
        string='Field Transferede',
        copy=False,
    )
