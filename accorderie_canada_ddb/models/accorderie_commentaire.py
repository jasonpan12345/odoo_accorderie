from odoo import _, api, models, fields


class AccorderieCommentaire(models.Model):
    _name = "accorderie.commentaire"
    _description = (
        "Les commentaires des membres envers d'autres membres sur des services"
        " et demandes"
    )

    autre_commentaire = fields.Text(string="Autres commentaires")

    autre_situation = fields.Char(string="Autre situation")

    confidentiel = fields.Integer(string="Confidentialité")

    consulter_accorderie = fields.Boolean(string="Consulté par une Accorderie")

    consulter_reseau = fields.Boolean(string="Consulté par le Réseau")

    date_incident = fields.Date(string="Date de l'indicent")

    date_mise_a_jour = fields.Datetime(
        string="Dernière mise à jour",
        help="Date de la dernière mise à jour",
    )

    datetime_creation = fields.Datetime(string="Date et heure de création")

    degre_satisfaction = fields.Integer(string="Degré de satisfaction")

    demande_service_id = fields.Many2one(
        string="Demande de services",
        comodel_name="accorderie.demande.service",
        help="La demande de services qui est visée par ce commentaire.",
    )

    demarche = fields.Text(
        string="Démarche",
        help="Démarche entreprise avant de faire le commentaire",
    )

    membre_source = fields.Many2one(
        string="Membre source",
        comodel_name="accorderie.membre",
        required=True,
        help="Membre duquel provient le commentaire",
    )

    membre_viser = fields.Many2one(
        string="Membre visé",
        comodel_name="accorderie.membre",
        help="Membre visé par le commentaire",
    )

    name = fields.Char()

    nom_comite = fields.Char(string="Nom du comité")

    note_administrative = fields.Text(
        string="Note administrative",
        help=(
            "Suivi du commentaire, visible par le Réseau et les"
            " administrateurs-chefs seulement."
        ),
    )

    offre_service_id = fields.Many2one(
        string="Offre de services",
        comodel_name="accorderie.offre.service",
        help="L'offre de services qui est visée par ce commentaire.",
    )

    point_service = fields.Many2one(
        string="Point de services",
        comodel_name="accorderie.pointservice",
        required=True,
    )

    resumer_situation = fields.Text(string="Résumé de la situation")

    situation_impliquant = fields.Integer(
        string="Situation impliquant",
        help="Choisir un type de groupe visé par ce commentaire.",
    )

    solution_pour_regler = fields.Text(
        string="Solution pour régler la situation",
        help=(
            "Indiquer quels seraient la meilleur solution, selon vous, pour"
            " régler la situation."
        ),
    )

    type_offre = fields.Integer(string="Type de l'offre")
