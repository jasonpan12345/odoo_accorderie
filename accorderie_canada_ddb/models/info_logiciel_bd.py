from odoo import _, api, models, fields


class InfoLogicielBd(models.Model):
    _name = "info.logiciel.bd"
    _description = "Model Info_logiciel_bd belonging to Module Tbl"

    datecreation = fields.Datetime()

    derniereversionlogiciel = fields.Integer()

    lienweb = fields.Char()

    majoblig = fields.Integer()

    name = fields.Char()

    noinfologicielbd = fields.Integer(required=True)
