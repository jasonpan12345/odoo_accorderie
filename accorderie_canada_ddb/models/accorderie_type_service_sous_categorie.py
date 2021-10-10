from odoo import _, api, models, fields


class AccorderieTypeServiceSousCategorie(models.Model):
    _name = "accorderie.type.service.sous.categorie"
    _inherit = "portal.mixin"
    _description = "Type de services sous-catégorie"
    _rec_name = "nom"

    active = fields.Boolean(
        string="Actif",
        default=True,
        help=(
            "Lorsque non actif, cette sous-catégorie n'est plus en fonction,"
            " mais demeure accessible."
        ),
    )

    approuver = fields.Boolean(
        string="Approuvé",
        help="Permet d'approuver cette sous-catégorie.",
    )

    categorie = fields.Many2one(
        string="Catégorie",
        comodel_name="accorderie.type.service.categorie",
        required=True,
    )

    nom = fields.Char()

    sous_categorie_service = fields.Char(
        string="Sous-catégorie",
        required=True,
    )

    type_service = fields.One2many(
        comodel_name="accorderie.type.service",
        inverse_name="sous_categorie_id",
        help="Type Service relation",
    )
