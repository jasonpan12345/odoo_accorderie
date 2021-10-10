from odoo import _, api, models, fields


class AccorderieTypeFichier(models.Model):
    _name = "accorderie.type.fichier"
    _inherit = "portal.mixin"
    _description = "Accorderie Type Fichier"
    _rec_name = "nom"

    date_mise_a_jour = fields.Datetime(
        string="Dernière mise à jour",
        required=True,
        help="Date de la dernière mise à jour",
    )

    fichier = fields.One2many(
        comodel_name="accorderie.fichier",
        inverse_name="type_fichier",
        help="Fichier relation",
    )

    nom = fields.Char()
