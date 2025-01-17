from odoo import _, api, fields, models


class AccorderieEchangeService(models.Model):
    _name = "accorderie.echange.service"
    _inherit = "portal.mixin"
    _description = "Accorderie Echange Service"
    _rec_name = "nom_complet"

    nom_complet = fields.Char(
        string="Nom complet",
        compute="_compute_nom_complet",
        store=True,
    )

    commentaire = fields.Char()

    date_echange = fields.Date(string="Date de l'échange")

    demande_service = fields.Many2one(
        comodel_name="accorderie.demande.service",
        string="Demande de services",
    )

    membre_acheteur = fields.Many2one(
        comodel_name="accorderie.membre",
        string="Membre acheteur",
    )

    membre_vendeur = fields.Many2one(
        comodel_name="accorderie.membre",
        string="Membre vendeur",
    )

    nb_heure = fields.Float(
        string="Nombre d'heure",
        help="Nombre d'heure effectué au moment de l'échange.",
    )

    offre_service = fields.Many2one(
        comodel_name="accorderie.offre.service",
        string="Offre de services",
    )

    point_service = fields.Many2one(
        comodel_name="accorderie.point.service",
        string="Point de services",
    )

    remarque = fields.Char()

    type_echange = fields.Selection(
        selection=[
            ("offre_ordinaire", "Offre ordinaire"),
            ("offre_special", "Offre spéciale"),
            ("demande", "Demande"),
            ("offre_ponctuel", "Offre ponctuelle"),
        ],
        string="Type d'échange",
    )

    def _compute_access_url(self):
        super(AccorderieEchangeService, self)._compute_access_url()
        for accorderie_echange_service in self:
            accorderie_echange_service.access_url = (
                "/my/accorderie_echange_service/%s"
                % accorderie_echange_service.id
            )

    @api.depends("type_echange", "point_service")
    def _compute_nom_complet(self):
        for rec in self:
            value = ""
            if rec.type_echange:
                value += rec.type_echange
            if rec.point_service and rec.point_service.nom:
                if rec.type_echange:
                    value += " - "
                value += rec.point_service.nom
            if not value:
                value = False
            rec.nom_complet = value
