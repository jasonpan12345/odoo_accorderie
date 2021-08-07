from odoo import _, api, models, fields


class PointserviceFournisseur(models.Model):
    _name = "pointservice.fournisseur"
    _description = "Model Pointservice_fournisseur belonging to Module Tbl"

    datemaj_pointservicefournisseur = fields.Datetime(
        string="Datemaj pointservicefournisseur"
    )

    name = fields.Char()

    nofournisseur = fields.Integer(required=True)

    nopointservice = fields.Integer(required=True)

    nopointservicefournisseur = fields.Integer(required=True)
