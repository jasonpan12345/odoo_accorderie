# -*- coding: utf-8 -*-

from odoo import api, models, fields


class OffreServiceMembre(models.Model):
    _name = 'offre.service.membre'
    _description = 'Model Offre_service_membre belonging to Module Tbl'

    approuve = fields.Integer(
        string='Field Approuve',
        copy=False,
    )

    conditionoffre = fields.Char(
        string='Field Conditionoffre',
        copy=False,
    )

    conditionx = fields.Char(
        string='Field Conditionx',
        copy=False,
    )

    dateaffichage = fields.Date(
        string='Field Dateaffichage',
        copy=False,
    )

    datedebut = fields.Date(
        string='Field Datedebut',
        copy=False,
    )

    datefin = fields.Date(
        string='Field Datefin',
        copy=False,
    )

    datemaj_servicemembre = fields.Datetime(
        string='Field Datemaj_servicemembre',
        required=True,
        copy=False,
    )

    description = fields.Char(
        string='Field Description',
        copy=False,
    )

    disponibilite = fields.Char(
        string='Field Disponibilite',
        copy=False,
    )

    fait = fields.Integer(
        string='Field Fait',
        copy=False,
    )

    name = fields.Char(
        string='Field Name',
        copy=False,
    )

    nbfoisconsulteroffremembre = fields.Integer(
        string='Field Nbfoisconsulteroffremembre',
        copy=False,
    )

    noaccorderie = fields.Integer(
        string='Field Noaccorderie',
        copy=False,
    )

    nocategoriesouscategorie = fields.Integer(
        string='Field Nocategoriesouscategorie',
        copy=False,
    )

    nomembre = fields.Integer(
        string='Field Nomembre',
        copy=False,
    )

    nooffreservicemembre = fields.Integer(
        string='Field Nooffreservicemembre',
        required=True,
        copy=False,
    )

    offrespecial = fields.Integer(
        string='Field Offrespecial',
        copy=False,
    )

    supprimer = fields.Integer(
        string='Field Supprimer',
        copy=False,
    )

    tarif = fields.Char(
        string='Field Tarif',
        copy=False,
    )

    titreoffrespecial = fields.Char(
        string='Field Titreoffrespecial',
        copy=False,
    )
