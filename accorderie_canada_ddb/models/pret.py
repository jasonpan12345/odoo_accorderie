from odoo import _, api, models, fields


class Pret(models.Model):
    _name = "pret"
    _description = "Model Pret belonging to Module Tbl"

    datecomitepret = fields.Datetime()

    datedemandepret = fields.Datetime()

    datemaj_pret = fields.Datetime(string="Datemaj pret")

    datepret = fields.Datetime()

    id_pret = fields.Integer(
        string="Id pret",
        required=True,
    )

    montantaccorder = fields.Float()

    montantdemande = fields.Float()

    name = fields.Char()

    nbremois = fields.Integer()

    nbrepaiement = fields.Integer()

    nomembre = fields.Many2one(
        comodel_name="membre",
        required=True,
    )

    nomembre_intermediaire = fields.Many2one(
        string="Nomembre intermediaire",
        comodel_name="membre",
    )

    nomembre_responsable = fields.Many2one(
        string="Nomembre responsable",
        comodel_name="membre",
        required=True,
    )

    note = fields.Text()

    raisonemprunt = fields.Text()

    recommandation = fields.Text()

    si_pretaccorder = fields.Integer(string="Si pretaccorder")

    tautinteretannuel = fields.Float()
