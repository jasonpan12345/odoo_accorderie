from odoo import _, api, models, fields


class AccorderieEchangeService(models.Model):
    _name = "accorderie.echange.service"
    _description = "Accorderie Echange Service"
    _rec_name = "nom_complet"

    commentaire = fields.Char()

    date_echange = fields.Date(string="Date de l'échange")

    demande_service = fields.Many2one(
        string="Demande de services",
        comodel_name="accorderie.demande.service",
    )

    membre_acheteur = fields.Many2one(
        string="Membre acheteur",
        comodel_name="accorderie.membre",
    )

    membre_vendeur = fields.Many2one(
        string="Membre vendeur",
        comodel_name="accorderie.membre",
    )

    nb_heure = fields.Float(
        string="Nombre d'heure",
        help="Nombre d'heure effectué au moment de l'échange.",
    )

    nom_complet = fields.Char(
        string="Nom complet",
        compute="_compute_nom_complet",
        store=True,
    )

    offre_service = fields.Many2one(
        string="Offre de services",
        comodel_name="accorderie.offre.service",
    )

    point_service = fields.Many2one(
        string="Point de services",
        comodel_name="accorderie.point.service",
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

    @api.depends("type_echange", "point_service")
    def _compute_nom_complet(self):
        for rec in self:
            value = ""
            if rec.type_echange:
                value += rec.type_echange
            if rec.type_echange and rec.point_service:
                value += " - "
            if rec.point_service:
                value += rec.point_service.nom
            if not value:
                value = False
            rec.nom_complet = value
