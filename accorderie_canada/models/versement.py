# -*- coding: utf-8 -*-

from odoo import api, models, fields


class Versement(models.Model):
    _name = 'versement'
    _description = 'Model Versement belonging to Module Tbl'

    datemaj_versement = fields.Datetime(
        string='Field Datemaj_versement',
        copy=False,
    )

    id_mensualite = fields.Integer(
        string='Field Id_mensualite',
        required=True,
        copy=False,
    )

    id_versement = fields.Integer(
        string='Field Id_versement',
        required=True,
        copy=False,
    )

    montantversement = fields.Float(
        string='Field Montantversement',
        copy=False,
    )

    name = fields.Char(
        string='Field Name',
        copy=False,
    )
