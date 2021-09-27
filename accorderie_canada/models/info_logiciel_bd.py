from odoo import _, api, models, fields


class InfoLogicielBd(models.Model):
    _name = "info.logiciel.bd"
    _description = "Model Info_logiciel_bd belonging to Module Tbl"

    datecreation = fields.Datetime(string="Field Datecreation")

    derniereversionlogiciel = fields.Integer(
        string="Field Derniereversionlogiciel"
    )

    lienweb = fields.Char(string="Field Lienweb")

    majoblig = fields.Integer(string="Field Majoblig")

    name = fields.Char(string="Field Name")

    noinfologicielbd = fields.Integer(
        string="Field Noinfologicielbd",
        required=True,
    )
