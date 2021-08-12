from odoo import _, api, models, fields


class TypeCompte(models.Model):
    _name = "type.compte"
    _description = "Model Type_compte belonging to Module Tbl"

    accodeursimple = fields.Integer()

    admin = fields.Integer()

    adminchef = fields.Integer()

    adminordpointservice = fields.Integer()

    adminpointservice = fields.Integer()

    name = fields.Char()

    nomembre = fields.Many2one(comodel_name="membre")

    reseau = fields.Integer()

    spip = fields.Integer()
