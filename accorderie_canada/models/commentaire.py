# -*- coding: utf-8 -*-

from odoo import api, models, fields


class Commentaire(models.Model):
    _name = 'commentaire'
    _description = 'Model Commentaire belonging to Module Tbl'

    autrecommentaire = fields.Text(
        string='Field Autrecommentaire',
        copy=False,
    )

    autresituation = fields.Char(
        string='Field Autresituation',
        copy=False,
    )

    consulteraccorderie = fields.Integer(
        string='Field Consulteraccorderie',
        copy=False,
    )

    consulterreseau = fields.Integer(
        string='Field Consulterreseau',
        copy=False,
    )

    dateheureajout = fields.Datetime(
        string='Field Dateheureajout',
        copy=False,
    )

    dateincident = fields.Date(
        string='Field Dateincident',
        copy=False,
    )

    datemaj_commentaire = fields.Datetime(
        string='Field Datemaj_commentaire',
        copy=False,
    )

    demarche = fields.Text(
        string='Field Demarche',
        copy=False,
    )

    name = fields.Char(
        string='Field Name',
        copy=False,
    )

    nocommentaire = fields.Integer(
        string='Field Nocommentaire',
        required=True,
        copy=False,
    )

    nodemandeservice = fields.Integer(
        string='Field Nodemandeservice',
        copy=False,
    )

    nomcomite = fields.Char(
        string='Field Nomcomite',
        copy=False,
    )

    nomembresource = fields.Integer(
        string='Field Nomembresource',
        required=True,
        copy=False,
    )

    nomembreviser = fields.Integer(
        string='Field Nomembreviser',
        copy=False,
    )

    nomemployer = fields.Char(
        string='Field Nomemployer',
        copy=False,
    )

    nooffreservicemembre = fields.Integer(
        string='Field Nooffreservicemembre',
        copy=False,
    )

    nopointservice = fields.Integer(
        string='Field Nopointservice',
        required=True,
        copy=False,
    )

    noteadministrative = fields.Text(
        string='Field Noteadministrative',
        copy=False,
    )

    resumersituation = fields.Text(
        string='Field Resumersituation',
        copy=False,
    )

    satisfactioninsatisfaction = fields.Integer(
        string='Field Satisfactioninsatisfaction',
        copy=False,
    )

    siconfidentiel = fields.Integer(
        string='Field Siconfidentiel',
        copy=False,
    )

    situation_impliquant = fields.Integer(
        string='Field Situation_impliquant',
        copy=False,
    )

    solutionpourregler = fields.Text(
        string='Field Solutionpourregler',
        copy=False,
    )

    typeoffre = fields.Integer(
        string='Field Typeoffre',
        copy=False,
    )
