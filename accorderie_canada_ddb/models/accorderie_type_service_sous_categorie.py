from odoo import _, api, fields, models


class AccorderieTypeServiceSousCategorie(models.Model):
    _name = "accorderie.type.service.sous.categorie"
    _inherit = "portal.mixin"
    _description = "Type de services sous-catégorie"
    _rec_name = "nom"

    nom = fields.Char()

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
        comodel_name="accorderie.type.service.categorie",
        string="Catégorie",
        required=True,
    )

    sous_categorie_service = fields.Char(
        string="Sous-catégorie",
        required=True,
    )

    type_service = fields.One2many(
        comodel_name="accorderie.type.service",
        inverse_name="sous_categorie_id",
        help="Type Service relation",
    )

    def _compute_access_url(self):
        super(AccorderieTypeServiceSousCategorie, self)._compute_access_url()
        for accorderie_type_service_sous_categorie in self:
            accorderie_type_service_sous_categorie.access_url = (
                "/my/accorderie_type_service_sous_categorie/%s"
                % accorderie_type_service_sous_categorie.id
            )
