from odoo import _, api, models, fields


class TypeCommunication(models.Model):
    _name = "type.communication"
    _description = "Model Type_communication belonging to Module Tbl"

    name = fields.Char()

    typecommunication = fields.Char()
