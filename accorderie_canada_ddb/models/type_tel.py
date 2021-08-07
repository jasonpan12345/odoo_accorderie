from odoo import _, api, models, fields


class TypeTel(models.Model):
    _name = "type.tel"
    _description = "Model Type_tel belonging to Module Tbl"

    name = fields.Char()

    notypetel = fields.Integer(required=True)

    typetel = fields.Char()
