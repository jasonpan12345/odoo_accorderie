from odoo import _, api, models, fields


class EchangeService(models.Model):
    _name = "echange.service"
    _description = "Model Echange_service belonging to Module Tbl"

    commentaire = fields.Char()

    dateechange = fields.Date()

    name = fields.Char()

    nbheure = fields.Float()

    nodemandeservice = fields.Integer()

    noechangeservice = fields.Integer(required=True)

    nomembreacheteur = fields.Integer()

    nomembrevendeur = fields.Integer()

    nooffreservicemembre = fields.Integer()

    nopointservice = fields.Integer()

    remarque = fields.Char()

    typeechange = fields.Integer()
