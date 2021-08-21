from odoo import _, api, models, fields


class EchangeService(models.Model):
    _name = "echange.service"
    _description = "Model Echange_service belonging to Module Tbl"

    commentaire = fields.Char()

    dateechange = fields.Date()

    name = fields.Char()

    nb_heure = fields.Float(
        string="Nombre d'heure",
        help="Nombre d'heure effectué au moment de l'échange.",
    )

    nodemandeservice = fields.Many2one(comodel_name="demande.service")

    noechangeservice = fields.Integer(required=True)

    nomembreacheteur = fields.Many2one(comodel_name="membre")

    nomembrevendeur = fields.Many2one(comodel_name="membre")

    nooffreservicemembre = fields.Many2one(comodel_name="offre.service.membre")

    nopointservice = fields.Many2one(comodel_name="pointservice")

    remarque = fields.Char()

    typeechange = fields.Integer()
