from odoo import _, api, models, fields


class EchangeService(models.Model):
    _name = "echange.service"
    _description = "Model Echange_service belonging to Module Tbl"

    commentaire = fields.Char(string="Field Commentaire")

    dateechange = fields.Date(string="Field Dateechange")

    name = fields.Char(string="Field Name")

    nbheure = fields.Float(string="Field Nbheure")

    nodemandeservice = fields.Integer(string="Field Nodemandeservice")

    noechangeservice = fields.Integer(
        string="Field Noechangeservice",
        required=True,
    )

    nomembreacheteur = fields.Integer(string="Field Nomembreacheteur")

    nomembrevendeur = fields.Integer(string="Field Nomembrevendeur")

    nooffreservicemembre = fields.Integer(string="Field Nooffreservicemembre")

    nopointservice = fields.Integer(string="Field Nopointservice")

    remarque = fields.Char(string="Field Remarque")

    typeechange = fields.Integer(string="Field Typeechange")
