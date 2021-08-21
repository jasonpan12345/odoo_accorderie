from odoo import _, api, models, fields


class AchatPonctuel(models.Model):
    _name = "achat.ponctuel"
    _description = "Model Achat_ponctuel belonging to Module Tbl"

    date_achat = fields.Date(string="Date d'achat")

    date_mise_a_jour = fields.Datetime(string="Dernière mise à jour")

    est_facture = fields.Integer(string="Facturé")

    majoration = fields.Float()

    membre = fields.Many2one(
        comodel_name="membre",
        required=True,
    )

    name = fields.Char()

    paiement_effectue = fields.Float(string="Paiement effectué")

    taxe_federal = fields.Float(string="Taxe fédéral")

    taxe_provincial = fields.Float(string="Taxe provincial")
