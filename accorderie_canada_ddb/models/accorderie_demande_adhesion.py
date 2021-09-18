from odoo import _, api, models, fields


class AccorderieDemandeAdhesion(models.Model):
    _name = "accorderie.demande.adhesion"
    _description = "Accorderie Demande Adhesion"

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

    name = fields.Char()

    nom = fields.Char()

    poste = fields.Char()

    prenom = fields.Char(string="Prénom")

    telephone = fields.Char(string="Téléphone")

    transferer = fields.Boolean(
        string="Transféré",
        default=False,
    )
