# -*- coding: utf-8 -*-

from odoo import api, models, fields


class InfoLogicielBd(models.Model):
    _name = 'info.logiciel.bd'
    _description = 'Model Info_logiciel_bd belonging to Module Tbl'

    datecreation = fields.Datetime(
        string='Field Datecreation',
        copy=False,
    )

    derniereversionlogiciel = fields.Integer(
        string='Field Derniereversionlogiciel',
        copy=False,
    )

    lienweb = fields.Char(
        string='Field Lienweb',
        copy=False,
    )

    majoblig = fields.Integer(
        string='Field Majoblig',
        copy=False,
    )

    name = fields.Char(
        string='Field Name',
        copy=False,
    )

    noinfologicielbd = fields.Integer(
        string='Field Noinfologicielbd',
        required=True,
        copy=False,
    )
