# -*- coding: utf-8 -*-

from odoo import api, models, fields


class LogAcces(models.Model):
    _name = 'log.acces'
    _description = 'Model Log_acces belonging to Module Tbl'

    dateheure_deconnexion = fields.Datetime(
        string='Field Dateheure_deconnexion',
        copy=False,
    )

    dateheureconnexion = fields.Datetime(
        string='Field Dateheureconnexion',
        copy=False,
    )

    id_log_acces = fields.Integer(
        string='Field Id_log_acces',
        required=True,
        copy=False,
    )

    ip_client_v4 = fields.Char(
        string='Field Ip_client_v4',
        copy=False,
    )

    name = fields.Char(
        string='Field Name',
        copy=False,
    )

    navigateur = fields.Char(
        string='Field Navigateur',
        copy=False,
    )

    nomembre = fields.Integer(
        string='Field Nomembre',
        copy=False,
    )

    nomusageressayer = fields.Char(
        string='Field Nomusageressayer',
        copy=False,
    )

    referer = fields.Char(
        string='Field Referer',
        copy=False,
    )

    resolution_h = fields.Integer(
        string='Field Resolution_h',
        copy=False,
    )

    resolution_w = fields.Integer(
        string='Field Resolution_w',
        copy=False,
    )

    statut = fields.Char(
        string='Field Statut',
        copy=False,
    )
