from odoo import _, api, models, fields


class TypeCommunication(models.Model):
    _name = "type.communication"
    _description = "Model Type_communication belonging to Module Tbl"

    name = fields.Char(string="Field Name")

    notypecommunication = fields.Integer(
        string="Field Notypecommunication",
        required=True,
    )

    typecommunication = fields.Char(string="Field Typecommunication")
