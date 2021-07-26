# -*- coding: utf-8 -*-

from odoo import api, models, fields


class DroitsAdmin(models.Model):
    _name = "droits.admin"
    _description = "Model Droits_admin belonging to Module Tbl"

    consulteretatcompte = fields.Integer(
        string="Field Consulteretatcompte",
        copy=False,
    )

    consulterprofil = fields.Integer(
        string="Field Consulterprofil",
        copy=False,
    )

    gestioncatsouscat = fields.Integer(
        string="Field Gestioncatsouscat",
        copy=False,
    )

    gestiondmd = fields.Integer(
        string="Field Gestiondmd",
        copy=False,
    )

    gestionfichier = fields.Integer(
        string="Field Gestionfichier",
        copy=False,
    )

    gestionoffre = fields.Integer(
        string="Field Gestionoffre",
        copy=False,
    )

    gestionoffremembre = fields.Integer(
        string="Field Gestionoffremembre",
        copy=False,
    )

    gestionprofil = fields.Integer(
        string="Field Gestionprofil",
        copy=False,
    )

    groupeachat = fields.Integer(
        string="Field Groupeachat",
        copy=False,
    )

    name = fields.Char(
        string="Field Name",
        copy=False,
    )

    nomembre = fields.Integer(
        string="Field Nomembre",
        required=True,
        copy=False,
    )

    saisieechange = fields.Integer(
        string="Field Saisieechange",
        copy=False,
    )

    validation = fields.Integer(
        string="Field Validation",
        copy=False,
    )
