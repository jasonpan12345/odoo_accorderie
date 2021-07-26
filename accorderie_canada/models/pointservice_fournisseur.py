# -*- coding: utf-8 -*-

from odoo import api, models, fields


class PointserviceFournisseur(models.Model):
    _name = "pointservice.fournisseur"
    _description = "Model Pointservice_fournisseur belonging to Module Tbl"

    datemaj_pointservicefournisseur = fields.Datetime(
        string="Field Datemaj_pointservicefournisseur",
        copy=False,
    )

    name = fields.Char(
        string="Field Name",
        copy=False,
    )

    nofournisseur = fields.Integer(
        string="Field Nofournisseur",
        required=True,
        copy=False,
    )

    nopointservice = fields.Integer(
        string="Field Nopointservice",
        required=True,
        copy=False,
    )

    nopointservicefournisseur = fields.Integer(
        string="Field Nopointservicefournisseur",
        required=True,
        copy=False,
    )
