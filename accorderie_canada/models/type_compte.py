# -*- coding: utf-8 -*-

from odoo import api, models, fields


class TypeCompte(models.Model):
    _name = 'type.compte'
    _description = 'Model Type_compte belonging to Module Tbl'

    accodeursimple = fields.Integer(
        string='Field Accodeursimple',
        copy=False,
    )

    admin = fields.Integer(
        string='Field Admin',
        copy=False,
    )

    adminchef = fields.Integer(
        string='Field Adminchef',
        copy=False,
    )

    adminordpointservice = fields.Integer(
        string='Field Adminordpointservice',
        copy=False,
    )

    adminpointservice = fields.Integer(
        string='Field Adminpointservice',
        copy=False,
    )

    name = fields.Char(
        string='Field Name',
        copy=False,
    )

    nomembre = fields.Integer(
        string='Field Nomembre',
        required=True,
        copy=False,
    )

    reseau = fields.Integer(
        string='Field Reseau',
        copy=False,
    )

    spip = fields.Integer(
        string='Field Spip',
        copy=False,
    )
