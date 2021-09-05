from odoo import _, api, models, fields


class AccorderieCategorieService(models.Model):
    _name = "accorderie.categorie.service"
    _description = "Les catégories de services des Accorderies"
    _rec_name = "nom"

    approuve = fields.Boolean(
        string="Approuvé",
        help="Permet d'approuver cette catégorie.",
    )

    archive = fields.Boolean(
        string="Archivé",
        help="Permet d'archiver cette catégorie.",
    )

    nom = fields.Char(help="Le nom de la catégorie des services")
