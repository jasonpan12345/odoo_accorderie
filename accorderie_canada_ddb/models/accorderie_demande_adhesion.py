from odoo import _, api, models, fields


class AccorderieDemandeAdhesion(models.Model):
    _name = "accorderie.demande.adhesion"
    _inherit = "portal.mixin"
    _description = "Accorderie Demande Adhesion"
    _rec_name = "nom_complet"

    accorderie = fields.Many2one(
        comodel_name="accorderie.accorderie",
        required=True,
    )

    active = fields.Boolean(
        string="Actif",
        default=True,
        help=(
            "Lorsque non actif, cet demande d'adhésion n'est plus en fonction,"
            " mais demeure accessible."
        ),
    )

    courriel = fields.Char()

    date_mise_a_jour = fields.Datetime(
        string="Dernière mise à jour",
        help="Date de la dernière mise à jour",
    )

    en_attente = fields.Boolean(
        string="En attente",
        default=True,
    )

    nom = fields.Char()

    nom_complet = fields.Char(
        string="Nom complet",
        compute="_compute_nom_complet",
        store=True,
    )

    poste = fields.Char()

    prenom = fields.Char(string="Prénom")

    telephone = fields.Char(string="Téléphone")

    transferer = fields.Boolean(
        string="Transféré",
        default=False,
    )

    @api.depends("nom", "prenom")
    def _compute_nom_complet(self):
        for rec in self:
            if rec.nom and rec.prenom:
                rec.nom_complet = f"{rec.prenom} {rec.nom}"
            elif rec.nom:
                rec.nom_complet = f"{rec.nom}"
            elif rec.prenom:
                rec.nom_complet = f"{rec.prenom}"
            else:
                rec.nom_complet = False
