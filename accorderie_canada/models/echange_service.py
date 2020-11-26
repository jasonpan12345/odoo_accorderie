# -*- coding: utf-8 -*-

from odoo import api, models, fields


class EchangeService(models.Model):
    _name = 'echange.service'
    _description = 'Model Echange_service belonging to Module Tbl'

    commentaire = fields.Char(
        string='Field Commentaire',
        copy=False,
    )

    dateechange = fields.Date(
        string='Field Dateechange',
        copy=False,
    )

    name = fields.Char(
        string='Field Name',
        copy=False,
    )

    nbheure = fields.Datetime(
        string='Field Nbheure',
        copy=False,
    )

    nodemandeservice = fields.Integer(
        string='Field Nodemandeservice',
        copy=False,
    )

    noechangeservice = fields.Integer(
        string='Field Noechangeservice',
        required=True,
        copy=False,
    )

    nomembreacheteur = fields.Integer(
        string='Field Nomembreacheteur',
        copy=False,
    )

    nomembrevendeur = fields.Integer(
        string='Field Nomembrevendeur',
        copy=False,
    )

    nooffreservicemembre = fields.Integer(
        string='Field Nooffreservicemembre',
        copy=False,
    )

    nopointservice = fields.Integer(
        string='Field Nopointservice',
        copy=False,
    )

    remarque = fields.Char(
        string='Field Remarque',
        copy=False,
    )

    typeechange = fields.Integer(
        string='Field Typeechange',
        copy=False,
    )
