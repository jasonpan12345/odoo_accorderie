from odoo import _, api, models, fields


class AccorderieTypeCompte(models.Model):
    _name = "accorderie.type.compte"
    _inherit = "portal.mixin"
    _description = "Accorderie Type Compte"
    _rec_name = "nom_complet"

    accordeur_simple = fields.Boolean(string="Accordeur simple")

    admin = fields.Boolean()

    admin_chef = fields.Boolean(string="Admin chef")

    admin_ord_point_service = fields.Boolean(
        string="Administrateur ordinaire point service"
    )

    admin_point_service = fields.Boolean(string="Administrateur point service")

    membre = fields.Many2one(comodel_name="accorderie.membre")

    nom_complet = fields.Char(
        string="Nom complet",
        compute="_compute_nom_complet",
        store=True,
    )

    reseau = fields.Boolean(string="Réseau")

    spip = fields.Boolean()

    def _compute_access_url(self):
        super(AccorderieTypeCompte, self)._compute_access_url()
        for accorderie_type_compte in self:
            accorderie_type_compte.access_url = (
                "/my/accorderie_type_compte/%s" % accorderie_type_compte.id
            )

    @api.depends(
        "membre",
    )
    def _compute_nom_complet(self):
        for rec in self:
            value = ""
            if rec.membre:
                value += rec.membre.nom_complet
            if not value:
                value = False
            rec.nom_complet = value
