from odoo import _, api, fields, models


class TypeTel(models.Model):
    _name = "type.tel"
    _description = "Model Type_tel belonging to Module Tbl"

    name = fields.Char(string="Field Name")

    notypetel = fields.Integer(
        string="Field Notypetel",
        required=True,
    )

    typetel = fields.Char(string="Field Typetel")
