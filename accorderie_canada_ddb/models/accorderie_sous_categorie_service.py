from odoo import _, api, models, fields


class AccorderieSousCategorieService(models.Model):
    _name = "accorderie.sous.categorie.service"
    _description = "Sous-catégorie de services"
    _rec_name = "nom"

    approuver = fields.Boolean(
        string="Approuvé",
        help="Permet d'approuver cette sous-catégorie.",
    )

    archive = fields.Boolean(
        string="Archivé",
        help=(
            "Lorsque archivé, cette sous-catégorie n'est plus en fonction,"
            " mais demeure accessible."
        ),
    )

    categorie = fields.Many2one(
        string="Catégorie",
        comodel_name="accorderie.categorie.service",
        required=True,
    )

    nom = fields.Char()

    sous_categorie_service = fields.Char(
        string="Sous-catégorie",
        required=True,
    )
