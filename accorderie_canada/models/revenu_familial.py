from odoo import _, api, fields, models


class RevenuFamilial(models.Model):
    _name = "revenu.familial"
    _description = "Model Revenu_familial belonging to Module Tbl"

    name = fields.Char(string="Field Name")

    norevenufamilial = fields.Integer(
        string="Field Norevenufamilial",
        required=True,
    )

    revenu = fields.Char(string="Field Revenu")
