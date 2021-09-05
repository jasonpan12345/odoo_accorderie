from odoo import _, api, models, fields


class AccorderieDmdAdhesion(models.Model):
    _name = "accorderie.dmd.adhesion"
    _description = "Accorderie Dmd Adhesion"

    courriel = fields.Char()

    datemaj = fields.Datetime()

    enattente = fields.Integer()

    name = fields.Char()

    noaccorderie = fields.Many2one(
        comodel_name="accorderie.accorderie",
        required=True,
    )

    nom = fields.Char()

    poste = fields.Char()

    prenom = fields.Char()

    supprimer = fields.Integer()

    telephone = fields.Char()

    transferer = fields.Integer()
