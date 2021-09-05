from odoo import _, api, models, fields


class AccorderieTypeService(models.Model):
    _name = "accorderie.type.service"
    _description = "Type de services des Accorderies"
    _rec_name = "nom"

    actif = fields.Boolean(
        default=True,
        help=(
            "Lorsque non actif, ce type de service n'est plus en fonction,"
            " mais demeure accessible."
        ),
    )

    approuve = fields.Boolean(
        string="Approuvé",
        help="Permet d'approuver ce type de services.",
    )

    description = fields.Char(help="Description du type de services")

    nom = fields.Char(help="Nom du type de services")

    numero = fields.Integer(
        string="Numéro",
        help="Numéro du type de services",
    )

    sous_categorie_id = fields.Many2one(
        string="Sous-catégorie",
        comodel_name="accorderie.sous.categorie.service",
        help="Sous-catégorie de services",
    )
