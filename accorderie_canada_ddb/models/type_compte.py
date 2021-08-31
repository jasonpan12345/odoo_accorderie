from odoo import _, api, models, fields


class TypeCompte(models.Model):
    _name = "type.compte"
    _description = "Model Type_compte belonging to Module Tbl"
    _rec_name = "nom_complet"

    accodeursimple = fields.Integer()

    admin = fields.Integer()

    adminchef = fields.Integer()

    adminordpointservice = fields.Integer()

    adminpointservice = fields.Integer()

    nom_complet = fields.Char(
        string="Nom complet",
        compute="_compute_nom_complet",
        store=True,
    )

    nomembre = fields.Many2one(comodel_name="membre")

    reseau = fields.Integer()

    spip = fields.Integer()

    @api.depends(
        "accodeursimple",
        "admin",
        "adminchef",
        "reseau",
        "spip",
        "adminpointservice",
        "adminordpointservice",
    )
    def _compute_nom_complet(self):
        for rec in self:
            value = ""
            value += str(self.accodeursimple)
            value += str(self.admin)
            value += str(self.adminchef)
            value += str(self.reseau)
            value += str(self.spip)
            value += str(self.adminpointservice)
            value += str(self.adminordpointservice)
            rec.nom_complet = value
