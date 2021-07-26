# -*- coding: utf-8 -*-

from odoo import api, models, fields


class Pointservice(models.Model):
    _name = "pointservice"
    _description = "Model Pointservice belonging to Module Tbl"

    datemaj_pointservice = fields.Datetime(
        string="Field Datemaj_pointservice",
        copy=False,
    )

    name = fields.Char(
        string="Field Name",
        copy=False,
    )

    noaccorderie = fields.Integer(
        string="Field Noaccorderie",
        required=True,
        copy=False,
    )

    nomembre = fields.Integer(
        string="Field Nomembre",
        copy=False,
    )

    nompointservice = fields.Char(
        string="Field Nompointservice",
        copy=False,
    )

    nopointservice = fields.Integer(
        string="Field Nopointservice",
        required=True,
        copy=False,
    )

    notegrpachatpageclient = fields.Text(
        string="Field Notegrpachatpageclient",
        copy=False,
    )

    ordrepointservice = fields.Integer(
        string="Field Ordrepointservice",
        copy=False,
    )
