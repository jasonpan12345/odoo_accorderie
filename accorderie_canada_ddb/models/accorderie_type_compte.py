from odoo import _, api, models, fields


class AccorderieTypeCompte(models.Model):
    _name = "accorderie.type.compte"
    _description = "Accorderie Type Compte"
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

    nomembre = fields.Many2one(comodel_name="accorderie.membre")

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
            value += str(rec.accodeursimple)
            value += str(rec.admin)
            value += str(rec.adminchef)
            value += str(rec.reseau)
            value += str(rec.spip)
            value += str(rec.adminpointservice)
            value += str(rec.adminordpointservice)
            rec.nom_complet = value
