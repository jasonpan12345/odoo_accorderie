from odoo import _, api, models, fields


class AccorderieEchangeService(models.Model):
    _name = "accorderie.echange.service"
    _description = "Accorderie Echange Service"

    commentaire = fields.Char()

    dateechange = fields.Date()

    name = fields.Char()

    nb_heure = fields.Float(
        string="Nombre d'heure",
        help="Nombre d'heure effectué au moment de l'échange.",
    )

    nodemandeservice = fields.Many2one(
        comodel_name="accorderie.demande.service"
    )

    nomembreacheteur = fields.Many2one(comodel_name="accorderie.membre")

    nomembrevendeur = fields.Many2one(comodel_name="accorderie.membre")

    nooffreservicemembre = fields.Many2one(
        comodel_name="accorderie.offre.service"
    )

    nopointservice = fields.Many2one(comodel_name="accorderie.pointservice")

    remarque = fields.Char()

    typeechange = fields.Integer()
