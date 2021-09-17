from odoo import _, api, models, fields


class AccorderieMembre(models.Model):
    _name = "accorderie.membre"
    _description = "Accorderie Membre"
    _rec_name = "nom_complet"

    accorderie = fields.Many2one(
        comodel_name="accorderie.accorderie",
        required=True,
        help="Accorderie associée",
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

    estunpointservice = fields.Integer()

    etatcomptecourriel = fields.Integer()

    membreactif = fields.Integer()

    membreca = fields.Integer()

    membreconjoint = fields.Integer()

    membreprinc = fields.Integer()

    memo = fields.Text()

    noarrondissement = fields.Many2one(
        comodel_name="accorderie.arrondissement"
    )

    nom = fields.Char()

    nom_complet = fields.Char(
        string="Nom complet",
        compute="_compute_nom_complet",
        store=True,
    )

    nomaccorderie = fields.Char()

    nomembreconjoint = fields.Integer()

    nomutilisateur = fields.Char()

    nooccupation = fields.Many2one(comodel_name="accorderie.occupation")

    noorigine = fields.Many2one(comodel_name="accorderie.origine")

    noprovenance = fields.Many2one(comodel_name="accorderie.provenance")

    noregion = fields.Many2one(
        comodel_name="accorderie.region",
        required=True,
    )

    norevenufamilial = fields.Many2one(
        comodel_name="accorderie.revenu.familial"
    )

    nosituationmaison = fields.Many2one(
        comodel_name="accorderie.situation.maison"
    )

    notypecommunication = fields.Many2one(
        comodel_name="accorderie.type.communication"
    )

    notypetel1 = fields.Integer()

    notypetel2 = fields.Integer()

    notypetel3 = fields.Integer()

    noville = fields.Many2one(
        comodel_name="accorderie.ville",
        required=True,
    )

    partsocialpaye = fields.Integer()

    pascommunication = fields.Integer()

    point_service = fields.Many2one(
        string="Point de service",
        comodel_name="accorderie.pointservice",
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

    quartier = fields.Many2one(
        string="Nocartier",
        comodel_name="accorderie.quartier",
    )

    recevoircourrielgrp = fields.Integer()

    sexe = fields.Integer()

    telephone1 = fields.Char()

    telephone2 = fields.Char()

    telephone3 = fields.Char()

    transferede = fields.Integer()

    @api.depends("nom", "prenom")
    def _compute_nom_complet(self):
        for rec in self:
            if rec.nom and rec.prenom:
                rec.nom_complet = f"{rec.prenom} {rec.nom}"
            elif rec.nom:
                rec.nom_complet = f"{rec.nom}"
            elif rec.prenom:
                rec.nom_complet = f"{rec.prenom}"
            else:
                rec.nom_complet = False
