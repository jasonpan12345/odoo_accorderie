from odoo import _, api, models, fields


class TypeCompte(models.Model):
    _name = "type.compte"
    _description = "Model Type_compte belonging to Module Tbl"

    accodeursimple = fields.Integer(string="Field Accodeursimple")

    admin = fields.Integer(string="Field Admin")

    adminchef = fields.Integer(string="Field Adminchef")

    adminordpointservice = fields.Integer(string="Field Adminordpointservice")

    adminpointservice = fields.Integer(string="Field Adminpointservice")

    name = fields.Char(string="Field Name")

    nomembre = fields.Integer(
        string="Field Nomembre",
        required=True,
    )

    reseau = fields.Integer(string="Field Reseau")

    spip = fields.Integer(string="Field Spip")
