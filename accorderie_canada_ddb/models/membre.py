from odoo import _, api, models, fields


class Membre(models.Model):
    _name = "membre"
    _description = "Model Membre belonging to Module Tbl"
    _rec_name = "nom_complet"

    accorderie = fields.Many2one(
        comodel_name="accorderie",
        required=True,
        help="Accorderie associé",
    )

    achatregrouper = fields.Integer()

    adresse = fields.Char()

    anneenaissance = fields.Integer()

    bottincourriel = fields.Integer()

    bottintel = fields.Integer()

    codepostal = fields.Char()

    courriel = fields.Char()

    date_maj_membre = fields.Datetime(string="Date maj membre")

    dateadhesion = fields.Date()

    descriptionaccordeur = fields.Char()

    etatcomptecourriel = fields.Integer()

    membreactif = fields.Integer()

    membreca = fields.Integer()

    membreconjoint = fields.Integer()

    membreprinc = fields.Integer()

    memo = fields.Text()

    motdepasse = fields.Char()

    noarrondissement = fields.Many2one(comodel_name="arrondissement")

    nocartier = fields.Many2one(comodel_name="cartier")

    nom = fields.Char(required=True)

    nom_complet = fields.Char(
        string="Nom complet",
        compute="_compute_nom_complet",
        store=True,
    )

    nomaccorderie = fields.Char()

    nomembre = fields.Integer(required=True)

    nomembreconjoint = fields.Integer()

    nomutilisateur = fields.Char()

    nooccupation = fields.Many2one(comodel_name="occupation")

    noorigine = fields.Many2one(comodel_name="origine")

    noprovenance = fields.Many2one(comodel_name="provenance")

    noregion = fields.Many2one(
        comodel_name="region",
        required=True,
    )

    norevenufamilial = fields.Many2one(comodel_name="revenu.familial")

    nosituationmaison = fields.Many2one(comodel_name="situation.maison")

    notypecommunication = fields.Many2one(comodel_name="type.communication")

    notypetel1 = fields.Integer()

    notypetel2 = fields.Integer()

    notypetel3 = fields.Integer()

    noville = fields.Many2one(
        comodel_name="ville",
        required=True,
    )

    partsocialpaye = fields.Integer()

    pascommunication = fields.Integer()

    point_service = fields.Many2one(
        string="Point de service",
        comodel_name="pointservice",
        help="Point de service associé",
    )

    postetel1 = fields.Char()

    postetel2 = fields.Char()

    postetel3 = fields.Char()

    precisezorigine = fields.Char()

    prenom = fields.Char()

    pretactif = fields.Integer()

    pretpayer = fields.Integer()

    pretradier = fields.Integer()

    profilapprouver = fields.Integer()

    recevoircourrielgrp = fields.Integer()

    sexe = fields.Integer()

    telephone1 = fields.Char()

    telephone2 = fields.Char()

    telephone3 = fields.Char()

    transferede = fields.Integer()

    @api.depends("nom", "prenom")
    def _compute_nom_complet(self):
        for rec in self:
            if self.nom and self.prenom:
                rec.nom_complet = f"{self.prenom} {self.nom}"
            elif self.nom:
                rec.nom_complet = f"{self.nom}"
            elif self.prenom:
                rec.nom_complet = f"{self.prenom}"
            else:
                rec.nom_complet = False
