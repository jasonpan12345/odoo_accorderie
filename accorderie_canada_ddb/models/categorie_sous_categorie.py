from odoo import _, api, models, fields


class CategorieSousCategorie(models.Model):
    _name = "categorie.sous.categorie"
    _description = "Model Categorie_sous_categorie belonging to Module Tbl"
    _rec_name = "nom_complet"

    approuver = fields.Integer()

    description = fields.Char()

    nocategorie = fields.Integer()

    nocategoriesouscategorie = fields.Integer(required=True)

    nom_complet = fields.Char(
        string="Nom complet",
        compute="_compute_nom_complet",
        store=True,
    )

    nooffre = fields.Integer()

    nosouscategorie = fields.Char()

    nosouscategorieid = fields.Many2one(comodel_name="sous.categorie")

    supprimer = fields.Integer()

    titreoffre = fields.Char()

    @api.depends("description", "nosouscategorie", "nocategorie")
    def _compute_nom_complet(self):
        for rec in self:
            value = ""
            if self.nosouscategorie:
                value += self.nosouscategorie
            if self.nocategorie:
                value += str(self.nocategorie)
            if (self.nosouscategorie or self.nocategorie) and self.description:
                value += " - "
            if self.description:
                value += self.description
            rec.nom_complet = value
