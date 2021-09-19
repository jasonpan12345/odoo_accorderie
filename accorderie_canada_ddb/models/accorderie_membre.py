from odoo import _, api, models, fields


class AccorderieMembre(models.Model):
    _name = "accorderie.membre"
    _description = "Accorderie Membre"
    _rec_name = "nom_complet"

    accorderie = fields.Many2one(
        comodel_name="accorderie.accorderie",
        required=True,
        help="Accorderie associée",
    )

    achat_regrouper = fields.Boolean(string="Achat regroupé")

    active = fields.Boolean(
        string="Actif",
        default=True,
        help=(
            "Lorsque non actif, ce membre n'est plus en fonction, mais demeure"
            " accessible."
        ),
    )

    adresse = fields.Char()

    annee_naissance = fields.Integer(string="Année de naissance")

    arrondissement = fields.Many2one(comodel_name="accorderie.arrondissement")

    bottin_courriel = fields.Boolean(string="Bottin courriel")

    bottin_tel = fields.Boolean(string="Bottin téléphone")

    codepostal = fields.Char()

    courriel = fields.Char()

    date_adhesion = fields.Date(string="Date de l'adhésion")

    date_mise_a_jour = fields.Datetime(
        string="Dernière mise à jour",
        help="Date de la dernière mise à jour",
    )

    description_membre = fields.Boolean(string="Description du membre")

    est_un_point_service = fields.Boolean(string="Est un point de service")

    membre_ca = fields.Boolean(string="Membre du CA")

    membre_conjoint = fields.Boolean(string="A un membre conjoint")

    membre_conjoint_id = fields.Integer(string="Membre conjoint")

    membre_principal = fields.Boolean(string="Membre principal")

    memo = fields.Text(string="Mémo")

    nom = fields.Char()

    nom_complet = fields.Char(
        string="Nom complet",
        compute="_compute_nom_complet",
        store=True,
    )

    nom_utilisateur = fields.Char(string="Nom du compte")

    occupation = fields.Many2one(comodel_name="accorderie.occupation")

    origine = fields.Many2one(comodel_name="accorderie.origine")

    part_social_paye = fields.Boolean(string="Part social payé")

    pas_communication = fields.Boolean(string="Pas de communication")

    point_service = fields.Many2one(
        string="Point de service",
        comodel_name="accorderie.point.service",
        help="Point de service associé",
    )

    prenom = fields.Char(string="Prénom")

    pret_actif = fields.Boolean(string="Prêt actif")

    profil_approuver = fields.Boolean(string="Profil approuvé")

    provenance = fields.Many2one(comodel_name="accorderie.provenance")

    quartier = fields.Many2one(comodel_name="accorderie.quartier")

    recevoir_courriel_groupe = fields.Boolean(
        string="Veut recevoir courriel de groupes"
    )

    region = fields.Many2one(
        string="Région",
        comodel_name="accorderie.region",
        required=True,
    )

    revenu_familial = fields.Many2one(
        string="Revenu familial",
        comodel_name="accorderie.revenu.familial",
    )

    sexe = fields.Selection(
        selection=[("femme", "Femme"), ("homme", "Homme"), ("autre", "Autre")]
    )

    situation_maison = fields.Many2one(
        string="Situation maison",
        comodel_name="accorderie.situation.maison",
    )

    telephone_1 = fields.Char(string="1er téléphone")

    telephone_2 = fields.Char(string="2e téléphone")

    telephone_3 = fields.Char(string="3e téléphone")

    telephone_poste_1 = fields.Char(string="1er poste téléphone")

    telephone_poste_2 = fields.Char(string="2 poste téléphone")

    telephone_poste_3 = fields.Char(string="3 poste téléphone")

    telephone_type_1 = fields.Many2one(
        string="1er type de téléphones",
        comodel_name="accorderie.type.telephone",
    )

    telephone_type_2 = fields.Many2one(
        string="2e type de téléphones",
        comodel_name="accorderie.type.telephone",
    )

    telephone_type_3 = fields.Many2one(
        string="3e type de téléphones",
        comodel_name="accorderie.type.telephone",
    )

    transfert_accorderie = fields.Many2one(
        string="Transfert d'une Accorderie",
        comodel_name="accorderie.accorderie",
    )

    type_communication = fields.Many2one(
        string="Type de communications",
        comodel_name="accorderie.type.communication",
    )

    ville = fields.Many2one(
        comodel_name="accorderie.ville",
        required=True,
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
