from odoo import _, api, fields, models


class Pointservice(models.Model):
    _name = "pointservice"
    _description = "Model Pointservice belonging to Module Tbl"

    datemaj_pointservice = fields.Datetime(string="Field Datemaj_pointservice")

    name = fields.Char(string="Field Name")

    noaccorderie = fields.Integer(
        string="Field Noaccorderie",
        required=True,
    )

    nomembre = fields.Integer(string="Field Nomembre")

    nompointservice = fields.Char(string="Field Nompointservice")

    nopointservice = fields.Integer(
        string="Field Nopointservice",
        required=True,
    )

    notegrpachatpageclient = fields.Text(string="Field Notegrpachatpageclient")

    ordrepointservice = fields.Integer(string="Field Ordrepointservice")
