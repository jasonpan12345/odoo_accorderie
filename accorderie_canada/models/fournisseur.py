# -*- coding: utf-8 -*-

from odoo import api, models, fields


class Fournisseur(models.Model):
    _name = 'fournisseur'
    _description = 'Model Fournisseur belonging to Module Tbl'

    adresse = fields.Char(
        string='Field Adresse',
        copy=False,
    )

    codepostalfournisseur = fields.Char(
        string='Field Codepostalfournisseur',
        copy=False,
    )

    courrielcontact = fields.Char(
        string='Field Courrielcontact',
        copy=False,
    )

    courrielfournisseur = fields.Char(
        string='Field Courrielfournisseur',
        copy=False,
    )

    datemaj_fournisseur = fields.Datetime(
        string='Field Datemaj_fournisseur',
        copy=False,
    )

    faxfounisseur = fields.Char(
        string='Field Faxfounisseur',
        copy=False,
    )

    name = fields.Char(
        string='Field Name',
        copy=False,
    )

    noaccorderie = fields.Integer(
        string='Field Noaccorderie',
        required=True,
        copy=False,
    )

    nofournisseur = fields.Integer(
        string='Field Nofournisseur',
        required=True,
        copy=False,
    )

    nomcontact = fields.Char(
        string='Field Nomcontact',
        copy=False,
    )

    nomfournisseur = fields.Char(
        string='Field Nomfournisseur',
        copy=False,
    )

    noregion = fields.Integer(
        string='Field Noregion',
        required=True,
        copy=False,
    )

    notefournisseur = fields.Text(
        string='Field Notefournisseur',
        copy=False,
    )

    noville = fields.Integer(
        string='Field Noville',
        required=True,
        copy=False,
    )

    postecontact = fields.Char(
        string='Field Postecontact',
        copy=False,
    )

    telfournisseur = fields.Char(
        string='Field Telfournisseur',
        copy=False,
    )

    visible_fournisseur = fields.Integer(
        string='Field Visible_fournisseur',
        copy=False,
    )
