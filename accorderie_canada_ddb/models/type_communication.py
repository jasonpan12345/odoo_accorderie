from odoo import _, api, models, fields


class TypeCommunication(models.Model):
    _name = "type.communication"
    _description = "Model Type_communication belonging to Module Tbl"
    _rec_name = "nom"

    name = fields.Char()

    nom = fields.Char(string="Typecommunication")
