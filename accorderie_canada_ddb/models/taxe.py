from odoo import _, api, models, fields


class Taxe(models.Model):
    _name = "taxe"
    _description = "Model Taxe belonging to Module Tbl"
    _rec_name = "nom_complet"

    nom_complet = fields.Char(
        string="Nom complet",
        compute="_compute_nom_complet",
        store=True,
    )

    notaxefed = fields.Char()

    notaxepro = fields.Char()

    tauxmajoration = fields.Float()

    tauxtaxefed = fields.Float()

    tauxtaxepro = fields.Float()

    @api.depends("tauxtaxepro", "tauxtaxefed")
    def _compute_nom_complet(self):
        for rec in self:
            value = ""
            if self.tauxtaxepro:
                value += str(self.tauxtaxepro)
            if self.tauxtaxepro and self.tauxtaxefed:
                value += " - "
            if self.tauxtaxefed:
                value += str(self.tauxtaxefed)
            rec.nom_complet = value
