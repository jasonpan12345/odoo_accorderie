from odoo import _, api, models, fields


class AccorderieCategorieService(models.Model):
    _name = "accorderie.categorie.service"
    _description = "Les catégories de services des Accorderies"
    _rec_name = "nom"

    actif = fields.Boolean(
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

    nom = fields.Char(help="Le nom de la catégorie des services")
