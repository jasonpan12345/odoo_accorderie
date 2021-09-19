from odoo import _, api, models, fields


class AccorderieFichier(models.Model):
    _name = "accorderie.fichier"
    _description = "Accorderie Fichier"
    _rec_name = "nom"

    accorderie = fields.Many2one(
        comodel_name="accorderie.accorderie",
        required=True,
    )

    date_mise_a_jour = fields.Datetime(
        string="Dernière mise à jour",
        help="Date de la dernière mise à jour",
    )

    fichier_binaire = fields.Binary(
        string="fichier_binaire",
        required=True,
    )

    nom = fields.Char(required=True)

    si_accorderie_local_seulement = fields.Boolean(
        string="Accorderie local seulement"
    )

    si_admin = fields.Boolean(string="Admin")

    si_disponible = fields.Boolean(string="Disponible")

    type_fichier = fields.Many2one(
        string="Type fichier",
        comodel_name="accorderie.type.fichier",
        required=True,
    )
