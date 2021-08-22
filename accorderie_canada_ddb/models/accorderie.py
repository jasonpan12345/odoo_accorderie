from odoo import _, api, models, fields


class Accorderie(models.Model):
    _name = "accorderie"
    _description = (
        "Gestion des entitées Accorderie, contient les informations et les"
        " messages d'une Accorderie."
    )
    _rec_name = "nom"

    adresse = fields.Char()

    archive = fields.Boolean(string="Archivé")

    arrondissement = fields.Many2one(comodel_name="arrondissement")

    code_postal = fields.Char(string="Code postal")

    courriel = fields.Char()

    date_mise_a_jour = fields.Datetime(string="Dernière mise à jour")

    grp_achat_administrateur = fields.Boolean(
        string="Groupe d'achat pour administrateur",
        help="Rend accessible les achats pour les Accordeurs.",
    )

    grp_achat_membre = fields.Boolean(
        string="Groupe d'achat membre",
        help="Rend accessible les achats pour les Accordeurs.",
    )

    logo = fields.Binary()

    message_accueil = fields.Html(
        string="Message accueil",
        help="Message à afficher pour l'Accueil des membres.",
    )

    message_grp_achat = fields.Html(
        string="Message groupe achat",
        help="Message à afficher pour les groupes d'achat.",
    )

    nom = fields.Char()

    region = fields.Many2one(comodel_name="region")

    telecopieur = fields.Char(string="Télécopieur")

    telephone = fields.Char(string="Téléphone")

    url_public = fields.Char(string="Lien site web public")

    url_transactionnel = fields.Char(string="Lien site web transactionnel")

    ville = fields.Many2one(comodel_name="ville")
