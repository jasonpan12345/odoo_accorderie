from odoo import _, api, models, fields


class AccorderieOffreService(models.Model):
    _name = "accorderie.offre.service"
    _description = "Accorderie Offre Service"
    _rec_name = "description"

    accompli = fields.Boolean(
        string="Accomplie",
        help="Cette offre de service est réalisée.",
    )

    accorderie = fields.Many2one(
        comodel_name="accorderie.accorderie",
        help="Accorderie associée",
    )

    approuve = fields.Boolean(
        string="Approuvé",
        help="Permet d'approuver ce type de services.",
    )

    archive = fields.Boolean(
        string="Archivé",
        help="Permet d'archiver cette offre de services.",
    )

    condition = fields.Char(
        string="Conditions",
        help="Conditions inhérentes à l'offre",
    )

    condition_autre = fields.Char(
        string="Condition autres",
        help="Autres conditions à informer",
    )

    date_affichage = fields.Date(string="Date d'affichage")

    date_debut = fields.Date(
        string="Date de début",
        help="Date à partir de laquelle l'offre est valide.",
    )

    date_fin = fields.Date(
        string="Date de fin",
        help="Date jusqu'à laquelle l'offre est valide.",
    )

    date_mise_a_jour = fields.Datetime(
        string="Dernière mise à jour",
        required=True,
        help="Date de la dernière mise à jour",
    )

    description = fields.Char()

    disponibilite = fields.Char(string="Disponibilité")

    membre = fields.Many2one(
        comodel_name="accorderie.membre",
        help="Membre qui offre le service",
    )

    nb_consultation = fields.Integer(string="Nombre de consultations")

    nom_offre_special = fields.Char(
        string="Nom de l'offre spéciale",
        help="Nom ou brève description de l'offre spéciale",
    )

    offre_special = fields.Boolean(string="Offre spéciale")

    tarif = fields.Char()

    type_service_id = fields.Many2one(
        string="Type de services",
        comodel_name="accorderie.type.service",
    )
