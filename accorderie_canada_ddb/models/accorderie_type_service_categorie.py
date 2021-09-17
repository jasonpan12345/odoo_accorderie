from odoo import _, api, models, fields


class AccorderieTypeServiceCategorie(models.Model):
    _name = "accorderie.type.service.categorie"
    _description = "Les catégories de types de services des Accorderies"
    _rec_name = "nom"

    active = fields.Boolean(
        string="Actif",
        default=True,
        help=(
            "Lorsque non actif, cette catégorie n'est plus en fonction, mais"
            " demeure accessible."
        ),
    )

    approuve = fields.Boolean(
        string="Approuvé",
        help="Permet d'approuver cette catégorie.",
    )

    nocategorie = fields.Integer(required=True)

    nom = fields.Char(help="Le nom de la catégorie des services")

    type_service_sous_categorie = fields.One2many(
        comodel_name="accorderie.type.service.sous.categorie",
        inverse_name="categorie",
        help="Type Service Sous Categorie relation",
    )
