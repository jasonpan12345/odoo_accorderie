from odoo import _, api, models, fields


class PointserviceFournisseur(models.Model):
    _name = "pointservice.fournisseur"
    _description = "Model Pointservice_fournisseur belonging to Module Tbl"

    datemaj_pointservicefournisseur = fields.Datetime(
        string="Field Datemaj_pointservicefournisseur"
    )

    name = fields.Char(string="Field Name")

    nofournisseur = fields.Integer(
        string="Field Nofournisseur",
        required=True,
    )

    nopointservice = fields.Integer(
        string="Field Nopointservice",
        required=True,
    )

    nopointservicefournisseur = fields.Integer(
        string="Field Nopointservicefournisseur",
        required=True,
    )
