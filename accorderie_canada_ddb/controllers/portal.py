from collections import OrderedDict
from operator import itemgetter

from odoo import _, http
from odoo.addons.portal.controllers.portal import CustomerPortal
from odoo.addons.portal.controllers.portal import pager as portal_pager
from odoo.exceptions import AccessError, MissingError
from odoo.http import request
from odoo.osv.expression import OR
from odoo.tools import groupby as groupbyelem


class CustomerPortal(CustomerPortal):
    def _prepare_portal_layout_values(self):
        values = super(CustomerPortal, self)._prepare_portal_layout_values()
        values["accorderie_accorderie_count"] = request.env[
            "accorderie.accorderie"
        ].search_count([])
        values["accorderie_arrondissement_count"] = request.env[
            "accorderie.arrondissement"
        ].search_count([])
        values["accorderie_commentaire_count"] = request.env[
            "accorderie.commentaire"
        ].search_count([])
        values["accorderie_demande_adhesion_count"] = request.env[
            "accorderie.demande.adhesion"
        ].search_count([])
        values["accorderie_demande_service_count"] = request.env[
            "accorderie.demande.service"
        ].search_count([])
        values["accorderie_droits_admin_count"] = request.env[
            "accorderie.droits.admin"
        ].search_count([])
        values["accorderie_echange_service_count"] = request.env[
            "accorderie.echange.service"
        ].search_count([])
        values["accorderie_fichier_count"] = request.env[
            "accorderie.fichier"
        ].search_count([])
        values["accorderie_membre_count"] = request.env[
            "accorderie.membre"
        ].search_count([])
        values["accorderie_occupation_count"] = request.env[
            "accorderie.occupation"
        ].search_count([])
        values["accorderie_offre_service_count"] = request.env[
            "accorderie.offre.service"
        ].search_count([])
        values["accorderie_origine_count"] = request.env[
            "accorderie.origine"
        ].search_count([])
        values["accorderie_point_service_count"] = request.env[
            "accorderie.point.service"
        ].search_count([])
        values["accorderie_provenance_count"] = request.env[
            "accorderie.provenance"
        ].search_count([])
        values["accorderie_quartier_count"] = request.env[
            "accorderie.quartier"
        ].search_count([])
        values["accorderie_region_count"] = request.env[
            "accorderie.region"
        ].search_count([])
        values["accorderie_revenu_familial_count"] = request.env[
            "accorderie.revenu.familial"
        ].search_count([])
        values["accorderie_situation_maison_count"] = request.env[
            "accorderie.situation.maison"
        ].search_count([])
        values["accorderie_type_communication_count"] = request.env[
            "accorderie.type.communication"
        ].search_count([])
        values["accorderie_type_compte_count"] = request.env[
            "accorderie.type.compte"
        ].search_count([])
        values["accorderie_type_fichier_count"] = request.env[
            "accorderie.type.fichier"
        ].search_count([])
        values["accorderie_type_service_count"] = request.env[
            "accorderie.type.service"
        ].search_count([])
        values["accorderie_type_service_categorie_count"] = request.env[
            "accorderie.type.service.categorie"
        ].search_count([])
        values["accorderie_type_service_sous_categorie_count"] = request.env[
            "accorderie.type.service.sous.categorie"
        ].search_count([])
        values["accorderie_type_telephone_count"] = request.env[
            "accorderie.type.telephone"
        ].search_count([])
        values["accorderie_ville_count"] = request.env[
            "accorderie.ville"
        ].search_count([])
        return values

    # ------------------------------------------------------------
    # My Accorderie Accorderie
    # ------------------------------------------------------------
    def _accorderie_accorderie_get_page_view_values(
        self, accorderie_accorderie, access_token, **kwargs
    ):
        values = {
            "page_name": "accorderie_accorderie",
            "accorderie_accorderie": accorderie_accorderie,
            "user": request.env.user,
        }
        return self._get_page_view_values(
            accorderie_accorderie,
            access_token,
            values,
            "my_accorderie_accorderies_history",
            False,
            **kwargs,
        )

    @http.route(
        [
            "/my/accorderie_accorderies",
            "/my/accorderie_accorderies/page/<int:page>",
        ],
        type="http",
        auth="user",
        website=True,
    )
    def portal_my_accorderie_accorderies(
        self,
        page=1,
        date_begin=None,
        date_end=None,
        sortby=None,
        filterby=None,
        search=None,
        search_in="content",
        **kw,
    ):
        values = self._prepare_portal_layout_values()
        AccorderieAccorderie = request.env["accorderie.accorderie"]
        domain = []

        searchbar_sortings = {
            "date": {"label": _("Newest"), "order": "create_date desc"},
            "name": {"label": _("Name"), "order": "name"},
        }
        searchbar_filters = {
            "all": {"label": _("All"), "domain": []},
        }
        searchbar_inputs = {}
        searchbar_groupby = {}

        # default sort by value
        if not sortby:
            sortby = "date"
        order = searchbar_sortings[sortby]["order"]
        # default filter by value
        if not filterby:
            filterby = "all"
        domain = searchbar_filters[filterby]["domain"]

        # search
        if search and search_in:
            search_domain = []
            domain += search_domain
        # archive groups - Default Group By 'create_date'
        archive_groups = self._get_archive_groups(
            "accorderie.accorderie", domain
        )
        if date_begin and date_end:
            domain += [
                ("create_date", ">", date_begin),
                ("create_date", "<=", date_end),
            ]
        # accorderie_accorderies count
        accorderie_accorderie_count = AccorderieAccorderie.search_count(domain)
        # pager
        pager = portal_pager(
            url="/my/accorderie_accorderies",
            url_args={
                "date_begin": date_begin,
                "date_end": date_end,
                "sortby": sortby,
                "filterby": filterby,
                "search_in": search_in,
                "search": search,
            },
            total=accorderie_accorderie_count,
            page=page,
            step=self._items_per_page,
        )

        # content according to pager and archive selected
        accorderie_accorderies = AccorderieAccorderie.search(
            domain,
            order=order,
            limit=self._items_per_page,
            offset=pager["offset"],
        )
        request.session[
            "my_accorderie_accorderies_history"
        ] = accorderie_accorderies.ids[:100]

        values.update(
            {
                "date": date_begin,
                "date_end": date_end,
                "accorderie_accorderies": accorderie_accorderies,
                "page_name": "accorderie_accorderie",
                "archive_groups": archive_groups,
                "default_url": "/my/accorderie_accorderies",
                "pager": pager,
                "searchbar_sortings": searchbar_sortings,
                "searchbar_groupby": searchbar_groupby,
                "searchbar_inputs": searchbar_inputs,
                "search_in": search_in,
                "searchbar_filters": OrderedDict(
                    sorted(searchbar_filters.items())
                ),
                "sortby": sortby,
                "filterby": filterby,
            }
        )
        return request.render(
            "accorderie_canada_ddb.portal_my_accorderie_accorderies", values
        )

    @http.route(
        ["/my/accorderie_accorderie/<int:accorderie_accorderie_id>"],
        type="http",
        auth="public",
        website=True,
    )
    def portal_my_accorderie_accorderie(
        self, accorderie_accorderie_id=None, access_token=None, **kw
    ):
        try:
            accorderie_accorderie_sudo = self._document_check_access(
                "accorderie.accorderie", accorderie_accorderie_id, access_token
            )
        except (AccessError, MissingError):
            return request.redirect("/my")

        values = self._accorderie_accorderie_get_page_view_values(
            accorderie_accorderie_sudo, access_token, **kw
        )
        return request.render(
            "accorderie_canada_ddb.portal_my_accorderie_accorderie", values
        )

    # ------------------------------------------------------------
    # My Accorderie Arrondissement
    # ------------------------------------------------------------
    def _accorderie_arrondissement_get_page_view_values(
        self, accorderie_arrondissement, access_token, **kwargs
    ):
        values = {
            "page_name": "accorderie_arrondissement",
            "accorderie_arrondissement": accorderie_arrondissement,
            "user": request.env.user,
        }
        return self._get_page_view_values(
            accorderie_arrondissement,
            access_token,
            values,
            "my_accorderie_arrondissements_history",
            False,
            **kwargs,
        )

    @http.route(
        [
            "/my/accorderie_arrondissements",
            "/my/accorderie_arrondissements/page/<int:page>",
        ],
        type="http",
        auth="user",
        website=True,
    )
    def portal_my_accorderie_arrondissements(
        self,
        page=1,
        date_begin=None,
        date_end=None,
        sortby=None,
        filterby=None,
        search=None,
        search_in="content",
        **kw,
    ):
        values = self._prepare_portal_layout_values()
        AccorderieArrondissement = request.env["accorderie.arrondissement"]
        domain = []

        searchbar_sortings = {
            "date": {"label": _("Newest"), "order": "create_date desc"},
            "name": {"label": _("Name"), "order": "name"},
        }
        searchbar_filters = {
            "all": {"label": _("All"), "domain": []},
        }
        searchbar_inputs = {}
        searchbar_groupby = {}

        # default sort by value
        if not sortby:
            sortby = "date"
        order = searchbar_sortings[sortby]["order"]
        # default filter by value
        if not filterby:
            filterby = "all"
        domain = searchbar_filters[filterby]["domain"]

        # search
        if search and search_in:
            search_domain = []
            domain += search_domain
        # archive groups - Default Group By 'create_date'
        archive_groups = self._get_archive_groups(
            "accorderie.arrondissement", domain
        )
        if date_begin and date_end:
            domain += [
                ("create_date", ">", date_begin),
                ("create_date", "<=", date_end),
            ]
        # accorderie_arrondissements count
        accorderie_arrondissement_count = (
            AccorderieArrondissement.search_count(domain)
        )
        # pager
        pager = portal_pager(
            url="/my/accorderie_arrondissements",
            url_args={
                "date_begin": date_begin,
                "date_end": date_end,
                "sortby": sortby,
                "filterby": filterby,
                "search_in": search_in,
                "search": search,
            },
            total=accorderie_arrondissement_count,
            page=page,
            step=self._items_per_page,
        )

        # content according to pager and archive selected
        accorderie_arrondissements = AccorderieArrondissement.search(
            domain,
            order=order,
            limit=self._items_per_page,
            offset=pager["offset"],
        )
        request.session[
            "my_accorderie_arrondissements_history"
        ] = accorderie_arrondissements.ids[:100]

        values.update(
            {
                "date": date_begin,
                "date_end": date_end,
                "accorderie_arrondissements": accorderie_arrondissements,
                "page_name": "accorderie_arrondissement",
                "archive_groups": archive_groups,
                "default_url": "/my/accorderie_arrondissements",
                "pager": pager,
                "searchbar_sortings": searchbar_sortings,
                "searchbar_groupby": searchbar_groupby,
                "searchbar_inputs": searchbar_inputs,
                "search_in": search_in,
                "searchbar_filters": OrderedDict(
                    sorted(searchbar_filters.items())
                ),
                "sortby": sortby,
                "filterby": filterby,
            }
        )
        return request.render(
            "accorderie_canada_ddb.portal_my_accorderie_arrondissements",
            values,
        )

    @http.route(
        ["/my/accorderie_arrondissement/<int:accorderie_arrondissement_id>"],
        type="http",
        auth="public",
        website=True,
    )
    def portal_my_accorderie_arrondissement(
        self, accorderie_arrondissement_id=None, access_token=None, **kw
    ):
        try:
            accorderie_arrondissement_sudo = self._document_check_access(
                "accorderie.arrondissement",
                accorderie_arrondissement_id,
                access_token,
            )
        except (AccessError, MissingError):
            return request.redirect("/my")

        values = self._accorderie_arrondissement_get_page_view_values(
            accorderie_arrondissement_sudo, access_token, **kw
        )
        return request.render(
            "accorderie_canada_ddb.portal_my_accorderie_arrondissement", values
        )

    # ------------------------------------------------------------
    # My Accorderie Commentaire
    # ------------------------------------------------------------
    def _accorderie_commentaire_get_page_view_values(
        self, accorderie_commentaire, access_token, **kwargs
    ):
        values = {
            "page_name": "accorderie_commentaire",
            "accorderie_commentaire": accorderie_commentaire,
            "user": request.env.user,
        }
        return self._get_page_view_values(
            accorderie_commentaire,
            access_token,
            values,
            "my_accorderie_commentaires_history",
            False,
            **kwargs,
        )

    @http.route(
        [
            "/my/accorderie_commentaires",
            "/my/accorderie_commentaires/page/<int:page>",
        ],
        type="http",
        auth="user",
        website=True,
    )
    def portal_my_accorderie_commentaires(
        self,
        page=1,
        date_begin=None,
        date_end=None,
        sortby=None,
        filterby=None,
        search=None,
        search_in="content",
        **kw,
    ):
        values = self._prepare_portal_layout_values()
        AccorderieCommentaire = request.env["accorderie.commentaire"]
        domain = []

        searchbar_sortings = {
            "date": {"label": _("Newest"), "order": "create_date desc"},
            "name": {"label": _("Name"), "order": "name"},
        }
        searchbar_filters = {
            "all": {"label": _("All"), "domain": []},
        }
        searchbar_inputs = {}
        searchbar_groupby = {}

        # default sort by value
        if not sortby:
            sortby = "date"
        order = searchbar_sortings[sortby]["order"]
        # default filter by value
        if not filterby:
            filterby = "all"
        domain = searchbar_filters[filterby]["domain"]

        # search
        if search and search_in:
            search_domain = []
            domain += search_domain
        # archive groups - Default Group By 'create_date'
        archive_groups = self._get_archive_groups(
            "accorderie.commentaire", domain
        )
        if date_begin and date_end:
            domain += [
                ("create_date", ">", date_begin),
                ("create_date", "<=", date_end),
            ]
        # accorderie_commentaires count
        accorderie_commentaire_count = AccorderieCommentaire.search_count(
            domain
        )
        # pager
        pager = portal_pager(
            url="/my/accorderie_commentaires",
            url_args={
                "date_begin": date_begin,
                "date_end": date_end,
                "sortby": sortby,
                "filterby": filterby,
                "search_in": search_in,
                "search": search,
            },
            total=accorderie_commentaire_count,
            page=page,
            step=self._items_per_page,
        )

        # content according to pager and archive selected
        accorderie_commentaires = AccorderieCommentaire.search(
            domain,
            order=order,
            limit=self._items_per_page,
            offset=pager["offset"],
        )
        request.session[
            "my_accorderie_commentaires_history"
        ] = accorderie_commentaires.ids[:100]

        values.update(
            {
                "date": date_begin,
                "date_end": date_end,
                "accorderie_commentaires": accorderie_commentaires,
                "page_name": "accorderie_commentaire",
                "archive_groups": archive_groups,
                "default_url": "/my/accorderie_commentaires",
                "pager": pager,
                "searchbar_sortings": searchbar_sortings,
                "searchbar_groupby": searchbar_groupby,
                "searchbar_inputs": searchbar_inputs,
                "search_in": search_in,
                "searchbar_filters": OrderedDict(
                    sorted(searchbar_filters.items())
                ),
                "sortby": sortby,
                "filterby": filterby,
            }
        )
        return request.render(
            "accorderie_canada_ddb.portal_my_accorderie_commentaires", values
        )

    @http.route(
        ["/my/accorderie_commentaire/<int:accorderie_commentaire_id>"],
        type="http",
        auth="public",
        website=True,
    )
    def portal_my_accorderie_commentaire(
        self, accorderie_commentaire_id=None, access_token=None, **kw
    ):
        try:
            accorderie_commentaire_sudo = self._document_check_access(
                "accorderie.commentaire",
                accorderie_commentaire_id,
                access_token,
            )
        except (AccessError, MissingError):
            return request.redirect("/my")

        values = self._accorderie_commentaire_get_page_view_values(
            accorderie_commentaire_sudo, access_token, **kw
        )
        return request.render(
            "accorderie_canada_ddb.portal_my_accorderie_commentaire", values
        )

    # ------------------------------------------------------------
    # My Accorderie Demande Adhesion
    # ------------------------------------------------------------
    def _accorderie_demande_adhesion_get_page_view_values(
        self, accorderie_demande_adhesion, access_token, **kwargs
    ):
        values = {
            "page_name": "accorderie_demande_adhesion",
            "accorderie_demande_adhesion": accorderie_demande_adhesion,
            "user": request.env.user,
        }
        return self._get_page_view_values(
            accorderie_demande_adhesion,
            access_token,
            values,
            "my_accorderie_demande_adhesions_history",
            False,
            **kwargs,
        )

    @http.route(
        [
            "/my/accorderie_demande_adhesions",
            "/my/accorderie_demande_adhesions/page/<int:page>",
        ],
        type="http",
        auth="user",
        website=True,
    )
    def portal_my_accorderie_demande_adhesions(
        self,
        page=1,
        date_begin=None,
        date_end=None,
        sortby=None,
        filterby=None,
        search=None,
        search_in="content",
        **kw,
    ):
        values = self._prepare_portal_layout_values()
        AccorderieDemandeAdhesion = request.env["accorderie.demande.adhesion"]
        domain = []

        searchbar_sortings = {
            "date": {"label": _("Newest"), "order": "create_date desc"},
            "name": {"label": _("Name"), "order": "name"},
        }
        searchbar_filters = {
            "all": {"label": _("All"), "domain": []},
        }
        searchbar_inputs = {}
        searchbar_groupby = {}

        # default sort by value
        if not sortby:
            sortby = "date"
        order = searchbar_sortings[sortby]["order"]
        # default filter by value
        if not filterby:
            filterby = "all"
        domain = searchbar_filters[filterby]["domain"]

        # search
        if search and search_in:
            search_domain = []
            domain += search_domain
        # archive groups - Default Group By 'create_date'
        archive_groups = self._get_archive_groups(
            "accorderie.demande.adhesion", domain
        )
        if date_begin and date_end:
            domain += [
                ("create_date", ">", date_begin),
                ("create_date", "<=", date_end),
            ]
        # accorderie_demande_adhesions count
        accorderie_demande_adhesion_count = (
            AccorderieDemandeAdhesion.search_count(domain)
        )
        # pager
        pager = portal_pager(
            url="/my/accorderie_demande_adhesions",
            url_args={
                "date_begin": date_begin,
                "date_end": date_end,
                "sortby": sortby,
                "filterby": filterby,
                "search_in": search_in,
                "search": search,
            },
            total=accorderie_demande_adhesion_count,
            page=page,
            step=self._items_per_page,
        )

        # content according to pager and archive selected
        accorderie_demande_adhesions = AccorderieDemandeAdhesion.search(
            domain,
            order=order,
            limit=self._items_per_page,
            offset=pager["offset"],
        )
        request.session[
            "my_accorderie_demande_adhesions_history"
        ] = accorderie_demande_adhesions.ids[:100]

        values.update(
            {
                "date": date_begin,
                "date_end": date_end,
                "accorderie_demande_adhesions": accorderie_demande_adhesions,
                "page_name": "accorderie_demande_adhesion",
                "archive_groups": archive_groups,
                "default_url": "/my/accorderie_demande_adhesions",
                "pager": pager,
                "searchbar_sortings": searchbar_sortings,
                "searchbar_groupby": searchbar_groupby,
                "searchbar_inputs": searchbar_inputs,
                "search_in": search_in,
                "searchbar_filters": OrderedDict(
                    sorted(searchbar_filters.items())
                ),
                "sortby": sortby,
                "filterby": filterby,
            }
        )
        return request.render(
            "accorderie_canada_ddb.portal_my_accorderie_demande_adhesions",
            values,
        )

    @http.route(
        [
            "/my/accorderie_demande_adhesion/<int:accorderie_demande_adhesion_id>"
        ],
        type="http",
        auth="public",
        website=True,
    )
    def portal_my_accorderie_demande_adhesion(
        self, accorderie_demande_adhesion_id=None, access_token=None, **kw
    ):
        try:
            accorderie_demande_adhesion_sudo = self._document_check_access(
                "accorderie.demande.adhesion",
                accorderie_demande_adhesion_id,
                access_token,
            )
        except (AccessError, MissingError):
            return request.redirect("/my")

        values = self._accorderie_demande_adhesion_get_page_view_values(
            accorderie_demande_adhesion_sudo, access_token, **kw
        )
        return request.render(
            "accorderie_canada_ddb.portal_my_accorderie_demande_adhesion",
            values,
        )

    # ------------------------------------------------------------
    # My Accorderie Demande Service
    # ------------------------------------------------------------
    def _accorderie_demande_service_get_page_view_values(
        self, accorderie_demande_service, access_token, **kwargs
    ):
        values = {
            "page_name": "accorderie_demande_service",
            "accorderie_demande_service": accorderie_demande_service,
            "user": request.env.user,
        }
        return self._get_page_view_values(
            accorderie_demande_service,
            access_token,
            values,
            "my_accorderie_demande_services_history",
            False,
            **kwargs,
        )

    @http.route(
        [
            "/my/accorderie_demande_services",
            "/my/accorderie_demande_services/page/<int:page>",
        ],
        type="http",
        auth="user",
        website=True,
    )
    def portal_my_accorderie_demande_services(
        self,
        page=1,
        date_begin=None,
        date_end=None,
        sortby=None,
        filterby=None,
        search=None,
        search_in="content",
        **kw,
    ):
        values = self._prepare_portal_layout_values()
        AccorderieDemandeService = request.env["accorderie.demande.service"]
        domain = []

        searchbar_sortings = {
            "date": {"label": _("Newest"), "order": "create_date desc"},
            "name": {"label": _("Name"), "order": "name"},
        }
        searchbar_filters = {
            "all": {"label": _("All"), "domain": []},
        }
        searchbar_inputs = {}
        searchbar_groupby = {}

        # default sort by value
        if not sortby:
            sortby = "date"
        order = searchbar_sortings[sortby]["order"]
        # default filter by value
        if not filterby:
            filterby = "all"
        domain = searchbar_filters[filterby]["domain"]

        # search
        if search and search_in:
            search_domain = []
            domain += search_domain
        # archive groups - Default Group By 'create_date'
        archive_groups = self._get_archive_groups(
            "accorderie.demande.service", domain
        )
        if date_begin and date_end:
            domain += [
                ("create_date", ">", date_begin),
                ("create_date", "<=", date_end),
            ]
        # accorderie_demande_services count
        accorderie_demande_service_count = (
            AccorderieDemandeService.search_count(domain)
        )
        # pager
        pager = portal_pager(
            url="/my/accorderie_demande_services",
            url_args={
                "date_begin": date_begin,
                "date_end": date_end,
                "sortby": sortby,
                "filterby": filterby,
                "search_in": search_in,
                "search": search,
            },
            total=accorderie_demande_service_count,
            page=page,
            step=self._items_per_page,
        )

        # content according to pager and archive selected
        accorderie_demande_services = AccorderieDemandeService.search(
            domain,
            order=order,
            limit=self._items_per_page,
            offset=pager["offset"],
        )
        request.session[
            "my_accorderie_demande_services_history"
        ] = accorderie_demande_services.ids[:100]

        values.update(
            {
                "date": date_begin,
                "date_end": date_end,
                "accorderie_demande_services": accorderie_demande_services,
                "page_name": "accorderie_demande_service",
                "archive_groups": archive_groups,
                "default_url": "/my/accorderie_demande_services",
                "pager": pager,
                "searchbar_sortings": searchbar_sortings,
                "searchbar_groupby": searchbar_groupby,
                "searchbar_inputs": searchbar_inputs,
                "search_in": search_in,
                "searchbar_filters": OrderedDict(
                    sorted(searchbar_filters.items())
                ),
                "sortby": sortby,
                "filterby": filterby,
            }
        )
        return request.render(
            "accorderie_canada_ddb.portal_my_accorderie_demande_services",
            values,
        )

    @http.route(
        ["/my/accorderie_demande_service/<int:accorderie_demande_service_id>"],
        type="http",
        auth="public",
        website=True,
    )
    def portal_my_accorderie_demande_service(
        self, accorderie_demande_service_id=None, access_token=None, **kw
    ):
        try:
            accorderie_demande_service_sudo = self._document_check_access(
                "accorderie.demande.service",
                accorderie_demande_service_id,
                access_token,
            )
        except (AccessError, MissingError):
            return request.redirect("/my")

        values = self._accorderie_demande_service_get_page_view_values(
            accorderie_demande_service_sudo, access_token, **kw
        )
        return request.render(
            "accorderie_canada_ddb.portal_my_accorderie_demande_service",
            values,
        )

    # ------------------------------------------------------------
    # My Accorderie Droits Admin
    # ------------------------------------------------------------
    def _accorderie_droits_admin_get_page_view_values(
        self, accorderie_droits_admin, access_token, **kwargs
    ):
        values = {
            "page_name": "accorderie_droits_admin",
            "accorderie_droits_admin": accorderie_droits_admin,
            "user": request.env.user,
        }
        return self._get_page_view_values(
            accorderie_droits_admin,
            access_token,
            values,
            "my_accorderie_droits_admins_history",
            False,
            **kwargs,
        )

    @http.route(
        [
            "/my/accorderie_droits_admins",
            "/my/accorderie_droits_admins/page/<int:page>",
        ],
        type="http",
        auth="user",
        website=True,
    )
    def portal_my_accorderie_droits_admins(
        self,
        page=1,
        date_begin=None,
        date_end=None,
        sortby=None,
        filterby=None,
        search=None,
        search_in="content",
        **kw,
    ):
        values = self._prepare_portal_layout_values()
        AccorderieDroitsAdmin = request.env["accorderie.droits.admin"]
        domain = []

        searchbar_sortings = {
            "date": {"label": _("Newest"), "order": "create_date desc"},
            "name": {"label": _("Name"), "order": "name"},
        }
        searchbar_filters = {
            "all": {"label": _("All"), "domain": []},
        }
        searchbar_inputs = {}
        searchbar_groupby = {}

        # default sort by value
        if not sortby:
            sortby = "date"
        order = searchbar_sortings[sortby]["order"]
        # default filter by value
        if not filterby:
            filterby = "all"
        domain = searchbar_filters[filterby]["domain"]

        # search
        if search and search_in:
            search_domain = []
            domain += search_domain
        # archive groups - Default Group By 'create_date'
        archive_groups = self._get_archive_groups(
            "accorderie.droits.admin", domain
        )
        if date_begin and date_end:
            domain += [
                ("create_date", ">", date_begin),
                ("create_date", "<=", date_end),
            ]
        # accorderie_droits_admins count
        accorderie_droits_admin_count = AccorderieDroitsAdmin.search_count(
            domain
        )
        # pager
        pager = portal_pager(
            url="/my/accorderie_droits_admins",
            url_args={
                "date_begin": date_begin,
                "date_end": date_end,
                "sortby": sortby,
                "filterby": filterby,
                "search_in": search_in,
                "search": search,
            },
            total=accorderie_droits_admin_count,
            page=page,
            step=self._items_per_page,
        )

        # content according to pager and archive selected
        accorderie_droits_admins = AccorderieDroitsAdmin.search(
            domain,
            order=order,
            limit=self._items_per_page,
            offset=pager["offset"],
        )
        request.session[
            "my_accorderie_droits_admins_history"
        ] = accorderie_droits_admins.ids[:100]

        values.update(
            {
                "date": date_begin,
                "date_end": date_end,
                "accorderie_droits_admins": accorderie_droits_admins,
                "page_name": "accorderie_droits_admin",
                "archive_groups": archive_groups,
                "default_url": "/my/accorderie_droits_admins",
                "pager": pager,
                "searchbar_sortings": searchbar_sortings,
                "searchbar_groupby": searchbar_groupby,
                "searchbar_inputs": searchbar_inputs,
                "search_in": search_in,
                "searchbar_filters": OrderedDict(
                    sorted(searchbar_filters.items())
                ),
                "sortby": sortby,
                "filterby": filterby,
            }
        )
        return request.render(
            "accorderie_canada_ddb.portal_my_accorderie_droits_admins", values
        )

    @http.route(
        ["/my/accorderie_droits_admin/<int:accorderie_droits_admin_id>"],
        type="http",
        auth="public",
        website=True,
    )
    def portal_my_accorderie_droits_admin(
        self, accorderie_droits_admin_id=None, access_token=None, **kw
    ):
        try:
            accorderie_droits_admin_sudo = self._document_check_access(
                "accorderie.droits.admin",
                accorderie_droits_admin_id,
                access_token,
            )
        except (AccessError, MissingError):
            return request.redirect("/my")

        values = self._accorderie_droits_admin_get_page_view_values(
            accorderie_droits_admin_sudo, access_token, **kw
        )
        return request.render(
            "accorderie_canada_ddb.portal_my_accorderie_droits_admin", values
        )

    # ------------------------------------------------------------
    # My Accorderie Echange Service
    # ------------------------------------------------------------
    def _accorderie_echange_service_get_page_view_values(
        self, accorderie_echange_service, access_token, **kwargs
    ):
        values = {
            "page_name": "accorderie_echange_service",
            "accorderie_echange_service": accorderie_echange_service,
            "user": request.env.user,
        }
        return self._get_page_view_values(
            accorderie_echange_service,
            access_token,
            values,
            "my_accorderie_echange_services_history",
            False,
            **kwargs,
        )

    @http.route(
        [
            "/my/accorderie_echange_services",
            "/my/accorderie_echange_services/page/<int:page>",
        ],
        type="http",
        auth="user",
        website=True,
    )
    def portal_my_accorderie_echange_services(
        self,
        page=1,
        date_begin=None,
        date_end=None,
        sortby=None,
        filterby=None,
        search=None,
        search_in="content",
        **kw,
    ):
        values = self._prepare_portal_layout_values()
        AccorderieEchangeService = request.env["accorderie.echange.service"]
        domain = []

        searchbar_sortings = {
            "date": {"label": _("Newest"), "order": "create_date desc"},
            "name": {"label": _("Name"), "order": "name"},
        }
        searchbar_filters = {
            "all": {"label": _("All"), "domain": []},
        }
        searchbar_inputs = {}
        searchbar_groupby = {}

        # default sort by value
        if not sortby:
            sortby = "date"
        order = searchbar_sortings[sortby]["order"]
        # default filter by value
        if not filterby:
            filterby = "all"
        domain = searchbar_filters[filterby]["domain"]

        # search
        if search and search_in:
            search_domain = []
            domain += search_domain
        # archive groups - Default Group By 'create_date'
        archive_groups = self._get_archive_groups(
            "accorderie.echange.service", domain
        )
        if date_begin and date_end:
            domain += [
                ("create_date", ">", date_begin),
                ("create_date", "<=", date_end),
            ]
        # accorderie_echange_services count
        accorderie_echange_service_count = (
            AccorderieEchangeService.search_count(domain)
        )
        # pager
        pager = portal_pager(
            url="/my/accorderie_echange_services",
            url_args={
                "date_begin": date_begin,
                "date_end": date_end,
                "sortby": sortby,
                "filterby": filterby,
                "search_in": search_in,
                "search": search,
            },
            total=accorderie_echange_service_count,
            page=page,
            step=self._items_per_page,
        )

        # content according to pager and archive selected
        accorderie_echange_services = AccorderieEchangeService.search(
            domain,
            order=order,
            limit=self._items_per_page,
            offset=pager["offset"],
        )
        request.session[
            "my_accorderie_echange_services_history"
        ] = accorderie_echange_services.ids[:100]

        values.update(
            {
                "date": date_begin,
                "date_end": date_end,
                "accorderie_echange_services": accorderie_echange_services,
                "page_name": "accorderie_echange_service",
                "archive_groups": archive_groups,
                "default_url": "/my/accorderie_echange_services",
                "pager": pager,
                "searchbar_sortings": searchbar_sortings,
                "searchbar_groupby": searchbar_groupby,
                "searchbar_inputs": searchbar_inputs,
                "search_in": search_in,
                "searchbar_filters": OrderedDict(
                    sorted(searchbar_filters.items())
                ),
                "sortby": sortby,
                "filterby": filterby,
            }
        )
        return request.render(
            "accorderie_canada_ddb.portal_my_accorderie_echange_services",
            values,
        )

    @http.route(
        ["/my/accorderie_echange_service/<int:accorderie_echange_service_id>"],
        type="http",
        auth="public",
        website=True,
    )
    def portal_my_accorderie_echange_service(
        self, accorderie_echange_service_id=None, access_token=None, **kw
    ):
        try:
            accorderie_echange_service_sudo = self._document_check_access(
                "accorderie.echange.service",
                accorderie_echange_service_id,
                access_token,
            )
        except (AccessError, MissingError):
            return request.redirect("/my")

        values = self._accorderie_echange_service_get_page_view_values(
            accorderie_echange_service_sudo, access_token, **kw
        )
        return request.render(
            "accorderie_canada_ddb.portal_my_accorderie_echange_service",
            values,
        )

    # ------------------------------------------------------------
    # My Accorderie Fichier
    # ------------------------------------------------------------
    def _accorderie_fichier_get_page_view_values(
        self, accorderie_fichier, access_token, **kwargs
    ):
        values = {
            "page_name": "accorderie_fichier",
            "accorderie_fichier": accorderie_fichier,
            "user": request.env.user,
        }
        return self._get_page_view_values(
            accorderie_fichier,
            access_token,
            values,
            "my_accorderie_fichiers_history",
            False,
            **kwargs,
        )

    @http.route(
        ["/my/accorderie_fichiers", "/my/accorderie_fichiers/page/<int:page>"],
        type="http",
        auth="user",
        website=True,
    )
    def portal_my_accorderie_fichiers(
        self,
        page=1,
        date_begin=None,
        date_end=None,
        sortby=None,
        filterby=None,
        search=None,
        search_in="content",
        **kw,
    ):
        values = self._prepare_portal_layout_values()
        AccorderieFichier = request.env["accorderie.fichier"]
        domain = []

        searchbar_sortings = {
            "date": {"label": _("Newest"), "order": "create_date desc"},
            "name": {"label": _("Name"), "order": "name"},
        }
        searchbar_filters = {
            "all": {"label": _("All"), "domain": []},
        }
        searchbar_inputs = {}
        searchbar_groupby = {}

        # default sort by value
        if not sortby:
            sortby = "date"
        order = searchbar_sortings[sortby]["order"]
        # default filter by value
        if not filterby:
            filterby = "all"
        domain = searchbar_filters[filterby]["domain"]

        # search
        if search and search_in:
            search_domain = []
            domain += search_domain
        # archive groups - Default Group By 'create_date'
        archive_groups = self._get_archive_groups("accorderie.fichier", domain)
        if date_begin and date_end:
            domain += [
                ("create_date", ">", date_begin),
                ("create_date", "<=", date_end),
            ]
        # accorderie_fichiers count
        accorderie_fichier_count = AccorderieFichier.search_count(domain)
        # pager
        pager = portal_pager(
            url="/my/accorderie_fichiers",
            url_args={
                "date_begin": date_begin,
                "date_end": date_end,
                "sortby": sortby,
                "filterby": filterby,
                "search_in": search_in,
                "search": search,
            },
            total=accorderie_fichier_count,
            page=page,
            step=self._items_per_page,
        )

        # content according to pager and archive selected
        accorderie_fichiers = AccorderieFichier.search(
            domain,
            order=order,
            limit=self._items_per_page,
            offset=pager["offset"],
        )
        request.session[
            "my_accorderie_fichiers_history"
        ] = accorderie_fichiers.ids[:100]

        values.update(
            {
                "date": date_begin,
                "date_end": date_end,
                "accorderie_fichiers": accorderie_fichiers,
                "page_name": "accorderie_fichier",
                "archive_groups": archive_groups,
                "default_url": "/my/accorderie_fichiers",
                "pager": pager,
                "searchbar_sortings": searchbar_sortings,
                "searchbar_groupby": searchbar_groupby,
                "searchbar_inputs": searchbar_inputs,
                "search_in": search_in,
                "searchbar_filters": OrderedDict(
                    sorted(searchbar_filters.items())
                ),
                "sortby": sortby,
                "filterby": filterby,
            }
        )
        return request.render(
            "accorderie_canada_ddb.portal_my_accorderie_fichiers", values
        )

    @http.route(
        ["/my/accorderie_fichier/<int:accorderie_fichier_id>"],
        type="http",
        auth="public",
        website=True,
    )
    def portal_my_accorderie_fichier(
        self, accorderie_fichier_id=None, access_token=None, **kw
    ):
        try:
            accorderie_fichier_sudo = self._document_check_access(
                "accorderie.fichier", accorderie_fichier_id, access_token
            )
        except (AccessError, MissingError):
            return request.redirect("/my")

        values = self._accorderie_fichier_get_page_view_values(
            accorderie_fichier_sudo, access_token, **kw
        )
        return request.render(
            "accorderie_canada_ddb.portal_my_accorderie_fichier", values
        )

    # ------------------------------------------------------------
    # My Accorderie Membre
    # ------------------------------------------------------------
    def _accorderie_membre_get_page_view_values(
        self, accorderie_membre, access_token, **kwargs
    ):
        values = {
            "page_name": "accorderie_membre",
            "accorderie_membre": accorderie_membre,
            "user": request.env.user,
        }
        return self._get_page_view_values(
            accorderie_membre,
            access_token,
            values,
            "my_accorderie_membres_history",
            False,
            **kwargs,
        )

    @http.route(
        ["/my/accorderie_membres", "/my/accorderie_membres/page/<int:page>"],
        type="http",
        auth="user",
        website=True,
    )
    def portal_my_accorderie_membres(
        self,
        page=1,
        date_begin=None,
        date_end=None,
        sortby=None,
        filterby=None,
        search=None,
        search_in="content",
        **kw,
    ):
        values = self._prepare_portal_layout_values()
        AccorderieMembre = request.env["accorderie.membre"]
        domain = []

        searchbar_sortings = {
            "date": {"label": _("Newest"), "order": "create_date desc"},
            "name": {"label": _("Name"), "order": "name"},
        }
        searchbar_filters = {
            "all": {"label": _("All"), "domain": []},
        }
        searchbar_inputs = {}
        searchbar_groupby = {}

        # default sort by value
        if not sortby:
            sortby = "date"
        order = searchbar_sortings[sortby]["order"]
        # default filter by value
        if not filterby:
            filterby = "all"
        domain = searchbar_filters[filterby]["domain"]

        # search
        if search and search_in:
            search_domain = []
            domain += search_domain
        # archive groups - Default Group By 'create_date'
        archive_groups = self._get_archive_groups("accorderie.membre", domain)
        if date_begin and date_end:
            domain += [
                ("create_date", ">", date_begin),
                ("create_date", "<=", date_end),
            ]
        # accorderie_membres count
        accorderie_membre_count = AccorderieMembre.search_count(domain)
        # pager
        pager = portal_pager(
            url="/my/accorderie_membres",
            url_args={
                "date_begin": date_begin,
                "date_end": date_end,
                "sortby": sortby,
                "filterby": filterby,
                "search_in": search_in,
                "search": search,
            },
            total=accorderie_membre_count,
            page=page,
            step=self._items_per_page,
        )

        # content according to pager and archive selected
        accorderie_membres = AccorderieMembre.search(
            domain,
            order=order,
            limit=self._items_per_page,
            offset=pager["offset"],
        )
        request.session[
            "my_accorderie_membres_history"
        ] = accorderie_membres.ids[:100]

        values.update(
            {
                "date": date_begin,
                "date_end": date_end,
                "accorderie_membres": accorderie_membres,
                "page_name": "accorderie_membre",
                "archive_groups": archive_groups,
                "default_url": "/my/accorderie_membres",
                "pager": pager,
                "searchbar_sortings": searchbar_sortings,
                "searchbar_groupby": searchbar_groupby,
                "searchbar_inputs": searchbar_inputs,
                "search_in": search_in,
                "searchbar_filters": OrderedDict(
                    sorted(searchbar_filters.items())
                ),
                "sortby": sortby,
                "filterby": filterby,
            }
        )
        return request.render(
            "accorderie_canada_ddb.portal_my_accorderie_membres", values
        )

    @http.route(
        ["/my/accorderie_membre/<int:accorderie_membre_id>"],
        type="http",
        auth="public",
        website=True,
    )
    def portal_my_accorderie_membre(
        self, accorderie_membre_id=None, access_token=None, **kw
    ):
        try:
            accorderie_membre_sudo = self._document_check_access(
                "accorderie.membre", accorderie_membre_id, access_token
            )
        except (AccessError, MissingError):
            return request.redirect("/my")

        values = self._accorderie_membre_get_page_view_values(
            accorderie_membre_sudo, access_token, **kw
        )
        return request.render(
            "accorderie_canada_ddb.portal_my_accorderie_membre", values
        )

    # ------------------------------------------------------------
    # My Accorderie Occupation
    # ------------------------------------------------------------
    def _accorderie_occupation_get_page_view_values(
        self, accorderie_occupation, access_token, **kwargs
    ):
        values = {
            "page_name": "accorderie_occupation",
            "accorderie_occupation": accorderie_occupation,
            "user": request.env.user,
        }
        return self._get_page_view_values(
            accorderie_occupation,
            access_token,
            values,
            "my_accorderie_occupations_history",
            False,
            **kwargs,
        )

    @http.route(
        [
            "/my/accorderie_occupations",
            "/my/accorderie_occupations/page/<int:page>",
        ],
        type="http",
        auth="user",
        website=True,
    )
    def portal_my_accorderie_occupations(
        self,
        page=1,
        date_begin=None,
        date_end=None,
        sortby=None,
        filterby=None,
        search=None,
        search_in="content",
        **kw,
    ):
        values = self._prepare_portal_layout_values()
        AccorderieOccupation = request.env["accorderie.occupation"]
        domain = []

        searchbar_sortings = {
            "date": {"label": _("Newest"), "order": "create_date desc"},
            "name": {"label": _("Name"), "order": "name"},
        }
        searchbar_filters = {
            "all": {"label": _("All"), "domain": []},
        }
        searchbar_inputs = {}
        searchbar_groupby = {}

        # default sort by value
        if not sortby:
            sortby = "date"
        order = searchbar_sortings[sortby]["order"]
        # default filter by value
        if not filterby:
            filterby = "all"
        domain = searchbar_filters[filterby]["domain"]

        # search
        if search and search_in:
            search_domain = []
            domain += search_domain
        # archive groups - Default Group By 'create_date'
        archive_groups = self._get_archive_groups(
            "accorderie.occupation", domain
        )
        if date_begin and date_end:
            domain += [
                ("create_date", ">", date_begin),
                ("create_date", "<=", date_end),
            ]
        # accorderie_occupations count
        accorderie_occupation_count = AccorderieOccupation.search_count(domain)
        # pager
        pager = portal_pager(
            url="/my/accorderie_occupations",
            url_args={
                "date_begin": date_begin,
                "date_end": date_end,
                "sortby": sortby,
                "filterby": filterby,
                "search_in": search_in,
                "search": search,
            },
            total=accorderie_occupation_count,
            page=page,
            step=self._items_per_page,
        )

        # content according to pager and archive selected
        accorderie_occupations = AccorderieOccupation.search(
            domain,
            order=order,
            limit=self._items_per_page,
            offset=pager["offset"],
        )
        request.session[
            "my_accorderie_occupations_history"
        ] = accorderie_occupations.ids[:100]

        values.update(
            {
                "date": date_begin,
                "date_end": date_end,
                "accorderie_occupations": accorderie_occupations,
                "page_name": "accorderie_occupation",
                "archive_groups": archive_groups,
                "default_url": "/my/accorderie_occupations",
                "pager": pager,
                "searchbar_sortings": searchbar_sortings,
                "searchbar_groupby": searchbar_groupby,
                "searchbar_inputs": searchbar_inputs,
                "search_in": search_in,
                "searchbar_filters": OrderedDict(
                    sorted(searchbar_filters.items())
                ),
                "sortby": sortby,
                "filterby": filterby,
            }
        )
        return request.render(
            "accorderie_canada_ddb.portal_my_accorderie_occupations", values
        )

    @http.route(
        ["/my/accorderie_occupation/<int:accorderie_occupation_id>"],
        type="http",
        auth="public",
        website=True,
    )
    def portal_my_accorderie_occupation(
        self, accorderie_occupation_id=None, access_token=None, **kw
    ):
        try:
            accorderie_occupation_sudo = self._document_check_access(
                "accorderie.occupation", accorderie_occupation_id, access_token
            )
        except (AccessError, MissingError):
            return request.redirect("/my")

        values = self._accorderie_occupation_get_page_view_values(
            accorderie_occupation_sudo, access_token, **kw
        )
        return request.render(
            "accorderie_canada_ddb.portal_my_accorderie_occupation", values
        )

    # ------------------------------------------------------------
    # My Accorderie Offre Service
    # ------------------------------------------------------------
    def _accorderie_offre_service_get_page_view_values(
        self, accorderie_offre_service, access_token, **kwargs
    ):
        values = {
            "page_name": "accorderie_offre_service",
            "accorderie_offre_service": accorderie_offre_service,
            "user": request.env.user,
        }
        return self._get_page_view_values(
            accorderie_offre_service,
            access_token,
            values,
            "my_accorderie_offre_services_history",
            False,
            **kwargs,
        )

    @http.route(
        [
            "/my/accorderie_offre_services",
            "/my/accorderie_offre_services/page/<int:page>",
        ],
        type="http",
        auth="user",
        website=True,
    )
    def portal_my_accorderie_offre_services(
        self,
        page=1,
        date_begin=None,
        date_end=None,
        sortby=None,
        filterby=None,
        search=None,
        search_in="content",
        **kw,
    ):
        values = self._prepare_portal_layout_values()
        AccorderieOffreService = request.env["accorderie.offre.service"]
        domain = []

        searchbar_sortings = {
            "date": {"label": _("Newest"), "order": "create_date desc"},
            "name": {"label": _("Name"), "order": "name"},
        }
        searchbar_filters = {
            "all": {"label": _("All"), "domain": []},
        }
        searchbar_inputs = {}
        searchbar_groupby = {}

        # default sort by value
        if not sortby:
            sortby = "date"
        order = searchbar_sortings[sortby]["order"]
        # default filter by value
        if not filterby:
            filterby = "all"
        domain = searchbar_filters[filterby]["domain"]

        # search
        if search and search_in:
            search_domain = []
            domain += search_domain
        # archive groups - Default Group By 'create_date'
        archive_groups = self._get_archive_groups(
            "accorderie.offre.service", domain
        )
        if date_begin and date_end:
            domain += [
                ("create_date", ">", date_begin),
                ("create_date", "<=", date_end),
            ]
        # accorderie_offre_services count
        accorderie_offre_service_count = AccorderieOffreService.search_count(
            domain
        )
        # pager
        pager = portal_pager(
            url="/my/accorderie_offre_services",
            url_args={
                "date_begin": date_begin,
                "date_end": date_end,
                "sortby": sortby,
                "filterby": filterby,
                "search_in": search_in,
                "search": search,
            },
            total=accorderie_offre_service_count,
            page=page,
            step=self._items_per_page,
        )

        # content according to pager and archive selected
        accorderie_offre_services = AccorderieOffreService.search(
            domain,
            order=order,
            limit=self._items_per_page,
            offset=pager["offset"],
        )
        request.session[
            "my_accorderie_offre_services_history"
        ] = accorderie_offre_services.ids[:100]

        values.update(
            {
                "date": date_begin,
                "date_end": date_end,
                "accorderie_offre_services": accorderie_offre_services,
                "page_name": "accorderie_offre_service",
                "archive_groups": archive_groups,
                "default_url": "/my/accorderie_offre_services",
                "pager": pager,
                "searchbar_sortings": searchbar_sortings,
                "searchbar_groupby": searchbar_groupby,
                "searchbar_inputs": searchbar_inputs,
                "search_in": search_in,
                "searchbar_filters": OrderedDict(
                    sorted(searchbar_filters.items())
                ),
                "sortby": sortby,
                "filterby": filterby,
            }
        )
        return request.render(
            "accorderie_canada_ddb.portal_my_accorderie_offre_services", values
        )

    @http.route(
        ["/my/accorderie_offre_service/<int:accorderie_offre_service_id>"],
        type="http",
        auth="public",
        website=True,
    )
    def portal_my_accorderie_offre_service(
        self, accorderie_offre_service_id=None, access_token=None, **kw
    ):
        try:
            accorderie_offre_service_sudo = self._document_check_access(
                "accorderie.offre.service",
                accorderie_offre_service_id,
                access_token,
            )
        except (AccessError, MissingError):
            return request.redirect("/my")

        values = self._accorderie_offre_service_get_page_view_values(
            accorderie_offre_service_sudo, access_token, **kw
        )
        return request.render(
            "accorderie_canada_ddb.portal_my_accorderie_offre_service", values
        )

    # ------------------------------------------------------------
    # My Accorderie Origine
    # ------------------------------------------------------------
    def _accorderie_origine_get_page_view_values(
        self, accorderie_origine, access_token, **kwargs
    ):
        values = {
            "page_name": "accorderie_origine",
            "accorderie_origine": accorderie_origine,
            "user": request.env.user,
        }
        return self._get_page_view_values(
            accorderie_origine,
            access_token,
            values,
            "my_accorderie_origines_history",
            False,
            **kwargs,
        )

    @http.route(
        ["/my/accorderie_origines", "/my/accorderie_origines/page/<int:page>"],
        type="http",
        auth="user",
        website=True,
    )
    def portal_my_accorderie_origines(
        self,
        page=1,
        date_begin=None,
        date_end=None,
        sortby=None,
        filterby=None,
        search=None,
        search_in="content",
        **kw,
    ):
        values = self._prepare_portal_layout_values()
        AccorderieOrigine = request.env["accorderie.origine"]
        domain = []

        searchbar_sortings = {
            "date": {"label": _("Newest"), "order": "create_date desc"},
            "name": {"label": _("Name"), "order": "name"},
        }
        searchbar_filters = {
            "all": {"label": _("All"), "domain": []},
        }
        searchbar_inputs = {}
        searchbar_groupby = {}

        # default sort by value
        if not sortby:
            sortby = "date"
        order = searchbar_sortings[sortby]["order"]
        # default filter by value
        if not filterby:
            filterby = "all"
        domain = searchbar_filters[filterby]["domain"]

        # search
        if search and search_in:
            search_domain = []
            domain += search_domain
        # archive groups - Default Group By 'create_date'
        archive_groups = self._get_archive_groups("accorderie.origine", domain)
        if date_begin and date_end:
            domain += [
                ("create_date", ">", date_begin),
                ("create_date", "<=", date_end),
            ]
        # accorderie_origines count
        accorderie_origine_count = AccorderieOrigine.search_count(domain)
        # pager
        pager = portal_pager(
            url="/my/accorderie_origines",
            url_args={
                "date_begin": date_begin,
                "date_end": date_end,
                "sortby": sortby,
                "filterby": filterby,
                "search_in": search_in,
                "search": search,
            },
            total=accorderie_origine_count,
            page=page,
            step=self._items_per_page,
        )

        # content according to pager and archive selected
        accorderie_origines = AccorderieOrigine.search(
            domain,
            order=order,
            limit=self._items_per_page,
            offset=pager["offset"],
        )
        request.session[
            "my_accorderie_origines_history"
        ] = accorderie_origines.ids[:100]

        values.update(
            {
                "date": date_begin,
                "date_end": date_end,
                "accorderie_origines": accorderie_origines,
                "page_name": "accorderie_origine",
                "archive_groups": archive_groups,
                "default_url": "/my/accorderie_origines",
                "pager": pager,
                "searchbar_sortings": searchbar_sortings,
                "searchbar_groupby": searchbar_groupby,
                "searchbar_inputs": searchbar_inputs,
                "search_in": search_in,
                "searchbar_filters": OrderedDict(
                    sorted(searchbar_filters.items())
                ),
                "sortby": sortby,
                "filterby": filterby,
            }
        )
        return request.render(
            "accorderie_canada_ddb.portal_my_accorderie_origines", values
        )

    @http.route(
        ["/my/accorderie_origine/<int:accorderie_origine_id>"],
        type="http",
        auth="public",
        website=True,
    )
    def portal_my_accorderie_origine(
        self, accorderie_origine_id=None, access_token=None, **kw
    ):
        try:
            accorderie_origine_sudo = self._document_check_access(
                "accorderie.origine", accorderie_origine_id, access_token
            )
        except (AccessError, MissingError):
            return request.redirect("/my")

        values = self._accorderie_origine_get_page_view_values(
            accorderie_origine_sudo, access_token, **kw
        )
        return request.render(
            "accorderie_canada_ddb.portal_my_accorderie_origine", values
        )

    # ------------------------------------------------------------
    # My Accorderie Point Service
    # ------------------------------------------------------------
    def _accorderie_point_service_get_page_view_values(
        self, accorderie_point_service, access_token, **kwargs
    ):
        values = {
            "page_name": "accorderie_point_service",
            "accorderie_point_service": accorderie_point_service,
            "user": request.env.user,
        }
        return self._get_page_view_values(
            accorderie_point_service,
            access_token,
            values,
            "my_accorderie_point_services_history",
            False,
            **kwargs,
        )

    @http.route(
        [
            "/my/accorderie_point_services",
            "/my/accorderie_point_services/page/<int:page>",
        ],
        type="http",
        auth="user",
        website=True,
    )
    def portal_my_accorderie_point_services(
        self,
        page=1,
        date_begin=None,
        date_end=None,
        sortby=None,
        filterby=None,
        search=None,
        search_in="content",
        **kw,
    ):
        values = self._prepare_portal_layout_values()
        AccorderiePointService = request.env["accorderie.point.service"]
        domain = []

        searchbar_sortings = {
            "date": {"label": _("Newest"), "order": "create_date desc"},
            "name": {"label": _("Name"), "order": "name"},
        }
        searchbar_filters = {
            "all": {"label": _("All"), "domain": []},
        }
        searchbar_inputs = {}
        searchbar_groupby = {}

        # default sort by value
        if not sortby:
            sortby = "date"
        order = searchbar_sortings[sortby]["order"]
        # default filter by value
        if not filterby:
            filterby = "all"
        domain = searchbar_filters[filterby]["domain"]

        # search
        if search and search_in:
            search_domain = []
            domain += search_domain
        # archive groups - Default Group By 'create_date'
        archive_groups = self._get_archive_groups(
            "accorderie.point.service", domain
        )
        if date_begin and date_end:
            domain += [
                ("create_date", ">", date_begin),
                ("create_date", "<=", date_end),
            ]
        # accorderie_point_services count
        accorderie_point_service_count = AccorderiePointService.search_count(
            domain
        )
        # pager
        pager = portal_pager(
            url="/my/accorderie_point_services",
            url_args={
                "date_begin": date_begin,
                "date_end": date_end,
                "sortby": sortby,
                "filterby": filterby,
                "search_in": search_in,
                "search": search,
            },
            total=accorderie_point_service_count,
            page=page,
            step=self._items_per_page,
        )

        # content according to pager and archive selected
        accorderie_point_services = AccorderiePointService.search(
            domain,
            order=order,
            limit=self._items_per_page,
            offset=pager["offset"],
        )
        request.session[
            "my_accorderie_point_services_history"
        ] = accorderie_point_services.ids[:100]

        values.update(
            {
                "date": date_begin,
                "date_end": date_end,
                "accorderie_point_services": accorderie_point_services,
                "page_name": "accorderie_point_service",
                "archive_groups": archive_groups,
                "default_url": "/my/accorderie_point_services",
                "pager": pager,
                "searchbar_sortings": searchbar_sortings,
                "searchbar_groupby": searchbar_groupby,
                "searchbar_inputs": searchbar_inputs,
                "search_in": search_in,
                "searchbar_filters": OrderedDict(
                    sorted(searchbar_filters.items())
                ),
                "sortby": sortby,
                "filterby": filterby,
            }
        )
        return request.render(
            "accorderie_canada_ddb.portal_my_accorderie_point_services", values
        )

    @http.route(
        ["/my/accorderie_point_service/<int:accorderie_point_service_id>"],
        type="http",
        auth="public",
        website=True,
    )
    def portal_my_accorderie_point_service(
        self, accorderie_point_service_id=None, access_token=None, **kw
    ):
        try:
            accorderie_point_service_sudo = self._document_check_access(
                "accorderie.point.service",
                accorderie_point_service_id,
                access_token,
            )
        except (AccessError, MissingError):
            return request.redirect("/my")

        values = self._accorderie_point_service_get_page_view_values(
            accorderie_point_service_sudo, access_token, **kw
        )
        return request.render(
            "accorderie_canada_ddb.portal_my_accorderie_point_service", values
        )

    # ------------------------------------------------------------
    # My Accorderie Provenance
    # ------------------------------------------------------------
    def _accorderie_provenance_get_page_view_values(
        self, accorderie_provenance, access_token, **kwargs
    ):
        values = {
            "page_name": "accorderie_provenance",
            "accorderie_provenance": accorderie_provenance,
            "user": request.env.user,
        }
        return self._get_page_view_values(
            accorderie_provenance,
            access_token,
            values,
            "my_accorderie_provenances_history",
            False,
            **kwargs,
        )

    @http.route(
        [
            "/my/accorderie_provenances",
            "/my/accorderie_provenances/page/<int:page>",
        ],
        type="http",
        auth="user",
        website=True,
    )
    def portal_my_accorderie_provenances(
        self,
        page=1,
        date_begin=None,
        date_end=None,
        sortby=None,
        filterby=None,
        search=None,
        search_in="content",
        **kw,
    ):
        values = self._prepare_portal_layout_values()
        AccorderieProvenance = request.env["accorderie.provenance"]
        domain = []

        searchbar_sortings = {
            "date": {"label": _("Newest"), "order": "create_date desc"},
            "name": {"label": _("Name"), "order": "name"},
        }
        searchbar_filters = {
            "all": {"label": _("All"), "domain": []},
        }
        searchbar_inputs = {}
        searchbar_groupby = {}

        # default sort by value
        if not sortby:
            sortby = "date"
        order = searchbar_sortings[sortby]["order"]
        # default filter by value
        if not filterby:
            filterby = "all"
        domain = searchbar_filters[filterby]["domain"]

        # search
        if search and search_in:
            search_domain = []
            domain += search_domain
        # archive groups - Default Group By 'create_date'
        archive_groups = self._get_archive_groups(
            "accorderie.provenance", domain
        )
        if date_begin and date_end:
            domain += [
                ("create_date", ">", date_begin),
                ("create_date", "<=", date_end),
            ]
        # accorderie_provenances count
        accorderie_provenance_count = AccorderieProvenance.search_count(domain)
        # pager
        pager = portal_pager(
            url="/my/accorderie_provenances",
            url_args={
                "date_begin": date_begin,
                "date_end": date_end,
                "sortby": sortby,
                "filterby": filterby,
                "search_in": search_in,
                "search": search,
            },
            total=accorderie_provenance_count,
            page=page,
            step=self._items_per_page,
        )

        # content according to pager and archive selected
        accorderie_provenances = AccorderieProvenance.search(
            domain,
            order=order,
            limit=self._items_per_page,
            offset=pager["offset"],
        )
        request.session[
            "my_accorderie_provenances_history"
        ] = accorderie_provenances.ids[:100]

        values.update(
            {
                "date": date_begin,
                "date_end": date_end,
                "accorderie_provenances": accorderie_provenances,
                "page_name": "accorderie_provenance",
                "archive_groups": archive_groups,
                "default_url": "/my/accorderie_provenances",
                "pager": pager,
                "searchbar_sortings": searchbar_sortings,
                "searchbar_groupby": searchbar_groupby,
                "searchbar_inputs": searchbar_inputs,
                "search_in": search_in,
                "searchbar_filters": OrderedDict(
                    sorted(searchbar_filters.items())
                ),
                "sortby": sortby,
                "filterby": filterby,
            }
        )
        return request.render(
            "accorderie_canada_ddb.portal_my_accorderie_provenances", values
        )

    @http.route(
        ["/my/accorderie_provenance/<int:accorderie_provenance_id>"],
        type="http",
        auth="public",
        website=True,
    )
    def portal_my_accorderie_provenance(
        self, accorderie_provenance_id=None, access_token=None, **kw
    ):
        try:
            accorderie_provenance_sudo = self._document_check_access(
                "accorderie.provenance", accorderie_provenance_id, access_token
            )
        except (AccessError, MissingError):
            return request.redirect("/my")

        values = self._accorderie_provenance_get_page_view_values(
            accorderie_provenance_sudo, access_token, **kw
        )
        return request.render(
            "accorderie_canada_ddb.portal_my_accorderie_provenance", values
        )

    # ------------------------------------------------------------
    # My Accorderie Quartier
    # ------------------------------------------------------------
    def _accorderie_quartier_get_page_view_values(
        self, accorderie_quartier, access_token, **kwargs
    ):
        values = {
            "page_name": "accorderie_quartier",
            "accorderie_quartier": accorderie_quartier,
            "user": request.env.user,
        }
        return self._get_page_view_values(
            accorderie_quartier,
            access_token,
            values,
            "my_accorderie_quartiers_history",
            False,
            **kwargs,
        )

    @http.route(
        [
            "/my/accorderie_quartiers",
            "/my/accorderie_quartiers/page/<int:page>",
        ],
        type="http",
        auth="user",
        website=True,
    )
    def portal_my_accorderie_quartiers(
        self,
        page=1,
        date_begin=None,
        date_end=None,
        sortby=None,
        filterby=None,
        search=None,
        search_in="content",
        **kw,
    ):
        values = self._prepare_portal_layout_values()
        AccorderieQuartier = request.env["accorderie.quartier"]
        domain = []

        searchbar_sortings = {
            "date": {"label": _("Newest"), "order": "create_date desc"},
            "name": {"label": _("Name"), "order": "name"},
        }
        searchbar_filters = {
            "all": {"label": _("All"), "domain": []},
        }
        searchbar_inputs = {}
        searchbar_groupby = {}

        # default sort by value
        if not sortby:
            sortby = "date"
        order = searchbar_sortings[sortby]["order"]
        # default filter by value
        if not filterby:
            filterby = "all"
        domain = searchbar_filters[filterby]["domain"]

        # search
        if search and search_in:
            search_domain = []
            domain += search_domain
        # archive groups - Default Group By 'create_date'
        archive_groups = self._get_archive_groups(
            "accorderie.quartier", domain
        )
        if date_begin and date_end:
            domain += [
                ("create_date", ">", date_begin),
                ("create_date", "<=", date_end),
            ]
        # accorderie_quartiers count
        accorderie_quartier_count = AccorderieQuartier.search_count(domain)
        # pager
        pager = portal_pager(
            url="/my/accorderie_quartiers",
            url_args={
                "date_begin": date_begin,
                "date_end": date_end,
                "sortby": sortby,
                "filterby": filterby,
                "search_in": search_in,
                "search": search,
            },
            total=accorderie_quartier_count,
            page=page,
            step=self._items_per_page,
        )

        # content according to pager and archive selected
        accorderie_quartiers = AccorderieQuartier.search(
            domain,
            order=order,
            limit=self._items_per_page,
            offset=pager["offset"],
        )
        request.session[
            "my_accorderie_quartiers_history"
        ] = accorderie_quartiers.ids[:100]

        values.update(
            {
                "date": date_begin,
                "date_end": date_end,
                "accorderie_quartiers": accorderie_quartiers,
                "page_name": "accorderie_quartier",
                "archive_groups": archive_groups,
                "default_url": "/my/accorderie_quartiers",
                "pager": pager,
                "searchbar_sortings": searchbar_sortings,
                "searchbar_groupby": searchbar_groupby,
                "searchbar_inputs": searchbar_inputs,
                "search_in": search_in,
                "searchbar_filters": OrderedDict(
                    sorted(searchbar_filters.items())
                ),
                "sortby": sortby,
                "filterby": filterby,
            }
        )
        return request.render(
            "accorderie_canada_ddb.portal_my_accorderie_quartiers", values
        )

    @http.route(
        ["/my/accorderie_quartier/<int:accorderie_quartier_id>"],
        type="http",
        auth="public",
        website=True,
    )
    def portal_my_accorderie_quartier(
        self, accorderie_quartier_id=None, access_token=None, **kw
    ):
        try:
            accorderie_quartier_sudo = self._document_check_access(
                "accorderie.quartier", accorderie_quartier_id, access_token
            )
        except (AccessError, MissingError):
            return request.redirect("/my")

        values = self._accorderie_quartier_get_page_view_values(
            accorderie_quartier_sudo, access_token, **kw
        )
        return request.render(
            "accorderie_canada_ddb.portal_my_accorderie_quartier", values
        )

    # ------------------------------------------------------------
    # My Accorderie Region
    # ------------------------------------------------------------
    def _accorderie_region_get_page_view_values(
        self, accorderie_region, access_token, **kwargs
    ):
        values = {
            "page_name": "accorderie_region",
            "accorderie_region": accorderie_region,
            "user": request.env.user,
        }
        return self._get_page_view_values(
            accorderie_region,
            access_token,
            values,
            "my_accorderie_regions_history",
            False,
            **kwargs,
        )

    @http.route(
        ["/my/accorderie_regions", "/my/accorderie_regions/page/<int:page>"],
        type="http",
        auth="user",
        website=True,
    )
    def portal_my_accorderie_regions(
        self,
        page=1,
        date_begin=None,
        date_end=None,
        sortby=None,
        filterby=None,
        search=None,
        search_in="content",
        **kw,
    ):
        values = self._prepare_portal_layout_values()
        AccorderieRegion = request.env["accorderie.region"]
        domain = []

        searchbar_sortings = {
            "date": {"label": _("Newest"), "order": "create_date desc"},
            "name": {"label": _("Name"), "order": "name"},
        }
        searchbar_filters = {
            "all": {"label": _("All"), "domain": []},
        }
        searchbar_inputs = {}
        searchbar_groupby = {}

        # default sort by value
        if not sortby:
            sortby = "date"
        order = searchbar_sortings[sortby]["order"]
        # default filter by value
        if not filterby:
            filterby = "all"
        domain = searchbar_filters[filterby]["domain"]

        # search
        if search and search_in:
            search_domain = []
            domain += search_domain
        # archive groups - Default Group By 'create_date'
        archive_groups = self._get_archive_groups("accorderie.region", domain)
        if date_begin and date_end:
            domain += [
                ("create_date", ">", date_begin),
                ("create_date", "<=", date_end),
            ]
        # accorderie_regions count
        accorderie_region_count = AccorderieRegion.search_count(domain)
        # pager
        pager = portal_pager(
            url="/my/accorderie_regions",
            url_args={
                "date_begin": date_begin,
                "date_end": date_end,
                "sortby": sortby,
                "filterby": filterby,
                "search_in": search_in,
                "search": search,
            },
            total=accorderie_region_count,
            page=page,
            step=self._items_per_page,
        )

        # content according to pager and archive selected
        accorderie_regions = AccorderieRegion.search(
            domain,
            order=order,
            limit=self._items_per_page,
            offset=pager["offset"],
        )
        request.session[
            "my_accorderie_regions_history"
        ] = accorderie_regions.ids[:100]

        values.update(
            {
                "date": date_begin,
                "date_end": date_end,
                "accorderie_regions": accorderie_regions,
                "page_name": "accorderie_region",
                "archive_groups": archive_groups,
                "default_url": "/my/accorderie_regions",
                "pager": pager,
                "searchbar_sortings": searchbar_sortings,
                "searchbar_groupby": searchbar_groupby,
                "searchbar_inputs": searchbar_inputs,
                "search_in": search_in,
                "searchbar_filters": OrderedDict(
                    sorted(searchbar_filters.items())
                ),
                "sortby": sortby,
                "filterby": filterby,
            }
        )
        return request.render(
            "accorderie_canada_ddb.portal_my_accorderie_regions", values
        )

    @http.route(
        ["/my/accorderie_region/<int:accorderie_region_id>"],
        type="http",
        auth="public",
        website=True,
    )
    def portal_my_accorderie_region(
        self, accorderie_region_id=None, access_token=None, **kw
    ):
        try:
            accorderie_region_sudo = self._document_check_access(
                "accorderie.region", accorderie_region_id, access_token
            )
        except (AccessError, MissingError):
            return request.redirect("/my")

        values = self._accorderie_region_get_page_view_values(
            accorderie_region_sudo, access_token, **kw
        )
        return request.render(
            "accorderie_canada_ddb.portal_my_accorderie_region", values
        )

    # ------------------------------------------------------------
    # My Accorderie Revenu Familial
    # ------------------------------------------------------------
    def _accorderie_revenu_familial_get_page_view_values(
        self, accorderie_revenu_familial, access_token, **kwargs
    ):
        values = {
            "page_name": "accorderie_revenu_familial",
            "accorderie_revenu_familial": accorderie_revenu_familial,
            "user": request.env.user,
        }
        return self._get_page_view_values(
            accorderie_revenu_familial,
            access_token,
            values,
            "my_accorderie_revenu_familials_history",
            False,
            **kwargs,
        )

    @http.route(
        [
            "/my/accorderie_revenu_familials",
            "/my/accorderie_revenu_familials/page/<int:page>",
        ],
        type="http",
        auth="user",
        website=True,
    )
    def portal_my_accorderie_revenu_familials(
        self,
        page=1,
        date_begin=None,
        date_end=None,
        sortby=None,
        filterby=None,
        search=None,
        search_in="content",
        **kw,
    ):
        values = self._prepare_portal_layout_values()
        AccorderieRevenuFamilial = request.env["accorderie.revenu.familial"]
        domain = []

        searchbar_sortings = {
            "date": {"label": _("Newest"), "order": "create_date desc"},
            "name": {"label": _("Name"), "order": "name"},
        }
        searchbar_filters = {
            "all": {"label": _("All"), "domain": []},
        }
        searchbar_inputs = {}
        searchbar_groupby = {}

        # default sort by value
        if not sortby:
            sortby = "date"
        order = searchbar_sortings[sortby]["order"]
        # default filter by value
        if not filterby:
            filterby = "all"
        domain = searchbar_filters[filterby]["domain"]

        # search
        if search and search_in:
            search_domain = []
            domain += search_domain
        # archive groups - Default Group By 'create_date'
        archive_groups = self._get_archive_groups(
            "accorderie.revenu.familial", domain
        )
        if date_begin and date_end:
            domain += [
                ("create_date", ">", date_begin),
                ("create_date", "<=", date_end),
            ]
        # accorderie_revenu_familials count
        accorderie_revenu_familial_count = (
            AccorderieRevenuFamilial.search_count(domain)
        )
        # pager
        pager = portal_pager(
            url="/my/accorderie_revenu_familials",
            url_args={
                "date_begin": date_begin,
                "date_end": date_end,
                "sortby": sortby,
                "filterby": filterby,
                "search_in": search_in,
                "search": search,
            },
            total=accorderie_revenu_familial_count,
            page=page,
            step=self._items_per_page,
        )

        # content according to pager and archive selected
        accorderie_revenu_familials = AccorderieRevenuFamilial.search(
            domain,
            order=order,
            limit=self._items_per_page,
            offset=pager["offset"],
        )
        request.session[
            "my_accorderie_revenu_familials_history"
        ] = accorderie_revenu_familials.ids[:100]

        values.update(
            {
                "date": date_begin,
                "date_end": date_end,
                "accorderie_revenu_familials": accorderie_revenu_familials,
                "page_name": "accorderie_revenu_familial",
                "archive_groups": archive_groups,
                "default_url": "/my/accorderie_revenu_familials",
                "pager": pager,
                "searchbar_sortings": searchbar_sortings,
                "searchbar_groupby": searchbar_groupby,
                "searchbar_inputs": searchbar_inputs,
                "search_in": search_in,
                "searchbar_filters": OrderedDict(
                    sorted(searchbar_filters.items())
                ),
                "sortby": sortby,
                "filterby": filterby,
            }
        )
        return request.render(
            "accorderie_canada_ddb.portal_my_accorderie_revenu_familials",
            values,
        )

    @http.route(
        ["/my/accorderie_revenu_familial/<int:accorderie_revenu_familial_id>"],
        type="http",
        auth="public",
        website=True,
    )
    def portal_my_accorderie_revenu_familial(
        self, accorderie_revenu_familial_id=None, access_token=None, **kw
    ):
        try:
            accorderie_revenu_familial_sudo = self._document_check_access(
                "accorderie.revenu.familial",
                accorderie_revenu_familial_id,
                access_token,
            )
        except (AccessError, MissingError):
            return request.redirect("/my")

        values = self._accorderie_revenu_familial_get_page_view_values(
            accorderie_revenu_familial_sudo, access_token, **kw
        )
        return request.render(
            "accorderie_canada_ddb.portal_my_accorderie_revenu_familial",
            values,
        )

    # ------------------------------------------------------------
    # My Accorderie Situation Maison
    # ------------------------------------------------------------
    def _accorderie_situation_maison_get_page_view_values(
        self, accorderie_situation_maison, access_token, **kwargs
    ):
        values = {
            "page_name": "accorderie_situation_maison",
            "accorderie_situation_maison": accorderie_situation_maison,
            "user": request.env.user,
        }
        return self._get_page_view_values(
            accorderie_situation_maison,
            access_token,
            values,
            "my_accorderie_situation_maisons_history",
            False,
            **kwargs,
        )

    @http.route(
        [
            "/my/accorderie_situation_maisons",
            "/my/accorderie_situation_maisons/page/<int:page>",
        ],
        type="http",
        auth="user",
        website=True,
    )
    def portal_my_accorderie_situation_maisons(
        self,
        page=1,
        date_begin=None,
        date_end=None,
        sortby=None,
        filterby=None,
        search=None,
        search_in="content",
        **kw,
    ):
        values = self._prepare_portal_layout_values()
        AccorderieSituationMaison = request.env["accorderie.situation.maison"]
        domain = []

        searchbar_sortings = {
            "date": {"label": _("Newest"), "order": "create_date desc"},
            "name": {"label": _("Name"), "order": "name"},
        }
        searchbar_filters = {
            "all": {"label": _("All"), "domain": []},
        }
        searchbar_inputs = {}
        searchbar_groupby = {}

        # default sort by value
        if not sortby:
            sortby = "date"
        order = searchbar_sortings[sortby]["order"]
        # default filter by value
        if not filterby:
            filterby = "all"
        domain = searchbar_filters[filterby]["domain"]

        # search
        if search and search_in:
            search_domain = []
            domain += search_domain
        # archive groups - Default Group By 'create_date'
        archive_groups = self._get_archive_groups(
            "accorderie.situation.maison", domain
        )
        if date_begin and date_end:
            domain += [
                ("create_date", ">", date_begin),
                ("create_date", "<=", date_end),
            ]
        # accorderie_situation_maisons count
        accorderie_situation_maison_count = (
            AccorderieSituationMaison.search_count(domain)
        )
        # pager
        pager = portal_pager(
            url="/my/accorderie_situation_maisons",
            url_args={
                "date_begin": date_begin,
                "date_end": date_end,
                "sortby": sortby,
                "filterby": filterby,
                "search_in": search_in,
                "search": search,
            },
            total=accorderie_situation_maison_count,
            page=page,
            step=self._items_per_page,
        )

        # content according to pager and archive selected
        accorderie_situation_maisons = AccorderieSituationMaison.search(
            domain,
            order=order,
            limit=self._items_per_page,
            offset=pager["offset"],
        )
        request.session[
            "my_accorderie_situation_maisons_history"
        ] = accorderie_situation_maisons.ids[:100]

        values.update(
            {
                "date": date_begin,
                "date_end": date_end,
                "accorderie_situation_maisons": accorderie_situation_maisons,
                "page_name": "accorderie_situation_maison",
                "archive_groups": archive_groups,
                "default_url": "/my/accorderie_situation_maisons",
                "pager": pager,
                "searchbar_sortings": searchbar_sortings,
                "searchbar_groupby": searchbar_groupby,
                "searchbar_inputs": searchbar_inputs,
                "search_in": search_in,
                "searchbar_filters": OrderedDict(
                    sorted(searchbar_filters.items())
                ),
                "sortby": sortby,
                "filterby": filterby,
            }
        )
        return request.render(
            "accorderie_canada_ddb.portal_my_accorderie_situation_maisons",
            values,
        )

    @http.route(
        [
            "/my/accorderie_situation_maison/<int:accorderie_situation_maison_id>"
        ],
        type="http",
        auth="public",
        website=True,
    )
    def portal_my_accorderie_situation_maison(
        self, accorderie_situation_maison_id=None, access_token=None, **kw
    ):
        try:
            accorderie_situation_maison_sudo = self._document_check_access(
                "accorderie.situation.maison",
                accorderie_situation_maison_id,
                access_token,
            )
        except (AccessError, MissingError):
            return request.redirect("/my")

        values = self._accorderie_situation_maison_get_page_view_values(
            accorderie_situation_maison_sudo, access_token, **kw
        )
        return request.render(
            "accorderie_canada_ddb.portal_my_accorderie_situation_maison",
            values,
        )

    # ------------------------------------------------------------
    # My Accorderie Type Communication
    # ------------------------------------------------------------
    def _accorderie_type_communication_get_page_view_values(
        self, accorderie_type_communication, access_token, **kwargs
    ):
        values = {
            "page_name": "accorderie_type_communication",
            "accorderie_type_communication": accorderie_type_communication,
            "user": request.env.user,
        }
        return self._get_page_view_values(
            accorderie_type_communication,
            access_token,
            values,
            "my_accorderie_type_communications_history",
            False,
            **kwargs,
        )

    @http.route(
        [
            "/my/accorderie_type_communications",
            "/my/accorderie_type_communications/page/<int:page>",
        ],
        type="http",
        auth="user",
        website=True,
    )
    def portal_my_accorderie_type_communications(
        self,
        page=1,
        date_begin=None,
        date_end=None,
        sortby=None,
        filterby=None,
        search=None,
        search_in="content",
        **kw,
    ):
        values = self._prepare_portal_layout_values()
        AccorderieTypeCommunication = request.env[
            "accorderie.type.communication"
        ]
        domain = []

        searchbar_sortings = {
            "date": {"label": _("Newest"), "order": "create_date desc"},
            "name": {"label": _("Name"), "order": "name"},
        }
        searchbar_filters = {
            "all": {"label": _("All"), "domain": []},
        }
        searchbar_inputs = {}
        searchbar_groupby = {}

        # default sort by value
        if not sortby:
            sortby = "date"
        order = searchbar_sortings[sortby]["order"]
        # default filter by value
        if not filterby:
            filterby = "all"
        domain = searchbar_filters[filterby]["domain"]

        # search
        if search and search_in:
            search_domain = []
            domain += search_domain
        # archive groups - Default Group By 'create_date'
        archive_groups = self._get_archive_groups(
            "accorderie.type.communication", domain
        )
        if date_begin and date_end:
            domain += [
                ("create_date", ">", date_begin),
                ("create_date", "<=", date_end),
            ]
        # accorderie_type_communications count
        accorderie_type_communication_count = (
            AccorderieTypeCommunication.search_count(domain)
        )
        # pager
        pager = portal_pager(
            url="/my/accorderie_type_communications",
            url_args={
                "date_begin": date_begin,
                "date_end": date_end,
                "sortby": sortby,
                "filterby": filterby,
                "search_in": search_in,
                "search": search,
            },
            total=accorderie_type_communication_count,
            page=page,
            step=self._items_per_page,
        )

        # content according to pager and archive selected
        accorderie_type_communications = AccorderieTypeCommunication.search(
            domain,
            order=order,
            limit=self._items_per_page,
            offset=pager["offset"],
        )
        request.session[
            "my_accorderie_type_communications_history"
        ] = accorderie_type_communications.ids[:100]

        values.update(
            {
                "date": date_begin,
                "date_end": date_end,
                "accorderie_type_communications": accorderie_type_communications,
                "page_name": "accorderie_type_communication",
                "archive_groups": archive_groups,
                "default_url": "/my/accorderie_type_communications",
                "pager": pager,
                "searchbar_sortings": searchbar_sortings,
                "searchbar_groupby": searchbar_groupby,
                "searchbar_inputs": searchbar_inputs,
                "search_in": search_in,
                "searchbar_filters": OrderedDict(
                    sorted(searchbar_filters.items())
                ),
                "sortby": sortby,
                "filterby": filterby,
            }
        )
        return request.render(
            "accorderie_canada_ddb.portal_my_accorderie_type_communications",
            values,
        )

    @http.route(
        [
            "/my/accorderie_type_communication/<int:accorderie_type_communication_id>"
        ],
        type="http",
        auth="public",
        website=True,
    )
    def portal_my_accorderie_type_communication(
        self, accorderie_type_communication_id=None, access_token=None, **kw
    ):
        try:
            accorderie_type_communication_sudo = self._document_check_access(
                "accorderie.type.communication",
                accorderie_type_communication_id,
                access_token,
            )
        except (AccessError, MissingError):
            return request.redirect("/my")

        values = self._accorderie_type_communication_get_page_view_values(
            accorderie_type_communication_sudo, access_token, **kw
        )
        return request.render(
            "accorderie_canada_ddb.portal_my_accorderie_type_communication",
            values,
        )

    # ------------------------------------------------------------
    # My Accorderie Type Compte
    # ------------------------------------------------------------
    def _accorderie_type_compte_get_page_view_values(
        self, accorderie_type_compte, access_token, **kwargs
    ):
        values = {
            "page_name": "accorderie_type_compte",
            "accorderie_type_compte": accorderie_type_compte,
            "user": request.env.user,
        }
        return self._get_page_view_values(
            accorderie_type_compte,
            access_token,
            values,
            "my_accorderie_type_comptes_history",
            False,
            **kwargs,
        )

    @http.route(
        [
            "/my/accorderie_type_comptes",
            "/my/accorderie_type_comptes/page/<int:page>",
        ],
        type="http",
        auth="user",
        website=True,
    )
    def portal_my_accorderie_type_comptes(
        self,
        page=1,
        date_begin=None,
        date_end=None,
        sortby=None,
        filterby=None,
        search=None,
        search_in="content",
        **kw,
    ):
        values = self._prepare_portal_layout_values()
        AccorderieTypeCompte = request.env["accorderie.type.compte"]
        domain = []

        searchbar_sortings = {
            "date": {"label": _("Newest"), "order": "create_date desc"},
            "name": {"label": _("Name"), "order": "name"},
        }
        searchbar_filters = {
            "all": {"label": _("All"), "domain": []},
        }
        searchbar_inputs = {}
        searchbar_groupby = {}

        # default sort by value
        if not sortby:
            sortby = "date"
        order = searchbar_sortings[sortby]["order"]
        # default filter by value
        if not filterby:
            filterby = "all"
        domain = searchbar_filters[filterby]["domain"]

        # search
        if search and search_in:
            search_domain = []
            domain += search_domain
        # archive groups - Default Group By 'create_date'
        archive_groups = self._get_archive_groups(
            "accorderie.type.compte", domain
        )
        if date_begin and date_end:
            domain += [
                ("create_date", ">", date_begin),
                ("create_date", "<=", date_end),
            ]
        # accorderie_type_comptes count
        accorderie_type_compte_count = AccorderieTypeCompte.search_count(
            domain
        )
        # pager
        pager = portal_pager(
            url="/my/accorderie_type_comptes",
            url_args={
                "date_begin": date_begin,
                "date_end": date_end,
                "sortby": sortby,
                "filterby": filterby,
                "search_in": search_in,
                "search": search,
            },
            total=accorderie_type_compte_count,
            page=page,
            step=self._items_per_page,
        )

        # content according to pager and archive selected
        accorderie_type_comptes = AccorderieTypeCompte.search(
            domain,
            order=order,
            limit=self._items_per_page,
            offset=pager["offset"],
        )
        request.session[
            "my_accorderie_type_comptes_history"
        ] = accorderie_type_comptes.ids[:100]

        values.update(
            {
                "date": date_begin,
                "date_end": date_end,
                "accorderie_type_comptes": accorderie_type_comptes,
                "page_name": "accorderie_type_compte",
                "archive_groups": archive_groups,
                "default_url": "/my/accorderie_type_comptes",
                "pager": pager,
                "searchbar_sortings": searchbar_sortings,
                "searchbar_groupby": searchbar_groupby,
                "searchbar_inputs": searchbar_inputs,
                "search_in": search_in,
                "searchbar_filters": OrderedDict(
                    sorted(searchbar_filters.items())
                ),
                "sortby": sortby,
                "filterby": filterby,
            }
        )
        return request.render(
            "accorderie_canada_ddb.portal_my_accorderie_type_comptes", values
        )

    @http.route(
        ["/my/accorderie_type_compte/<int:accorderie_type_compte_id>"],
        type="http",
        auth="public",
        website=True,
    )
    def portal_my_accorderie_type_compte(
        self, accorderie_type_compte_id=None, access_token=None, **kw
    ):
        try:
            accorderie_type_compte_sudo = self._document_check_access(
                "accorderie.type.compte",
                accorderie_type_compte_id,
                access_token,
            )
        except (AccessError, MissingError):
            return request.redirect("/my")

        values = self._accorderie_type_compte_get_page_view_values(
            accorderie_type_compte_sudo, access_token, **kw
        )
        return request.render(
            "accorderie_canada_ddb.portal_my_accorderie_type_compte", values
        )

    # ------------------------------------------------------------
    # My Accorderie Type Fichier
    # ------------------------------------------------------------
    def _accorderie_type_fichier_get_page_view_values(
        self, accorderie_type_fichier, access_token, **kwargs
    ):
        values = {
            "page_name": "accorderie_type_fichier",
            "accorderie_type_fichier": accorderie_type_fichier,
            "user": request.env.user,
        }
        return self._get_page_view_values(
            accorderie_type_fichier,
            access_token,
            values,
            "my_accorderie_type_fichiers_history",
            False,
            **kwargs,
        )

    @http.route(
        [
            "/my/accorderie_type_fichiers",
            "/my/accorderie_type_fichiers/page/<int:page>",
        ],
        type="http",
        auth="user",
        website=True,
    )
    def portal_my_accorderie_type_fichiers(
        self,
        page=1,
        date_begin=None,
        date_end=None,
        sortby=None,
        filterby=None,
        search=None,
        search_in="content",
        **kw,
    ):
        values = self._prepare_portal_layout_values()
        AccorderieTypeFichier = request.env["accorderie.type.fichier"]
        domain = []

        searchbar_sortings = {
            "date": {"label": _("Newest"), "order": "create_date desc"},
            "name": {"label": _("Name"), "order": "name"},
        }
        searchbar_filters = {
            "all": {"label": _("All"), "domain": []},
        }
        searchbar_inputs = {}
        searchbar_groupby = {}

        # default sort by value
        if not sortby:
            sortby = "date"
        order = searchbar_sortings[sortby]["order"]
        # default filter by value
        if not filterby:
            filterby = "all"
        domain = searchbar_filters[filterby]["domain"]

        # search
        if search and search_in:
            search_domain = []
            domain += search_domain
        # archive groups - Default Group By 'create_date'
        archive_groups = self._get_archive_groups(
            "accorderie.type.fichier", domain
        )
        if date_begin and date_end:
            domain += [
                ("create_date", ">", date_begin),
                ("create_date", "<=", date_end),
            ]
        # accorderie_type_fichiers count
        accorderie_type_fichier_count = AccorderieTypeFichier.search_count(
            domain
        )
        # pager
        pager = portal_pager(
            url="/my/accorderie_type_fichiers",
            url_args={
                "date_begin": date_begin,
                "date_end": date_end,
                "sortby": sortby,
                "filterby": filterby,
                "search_in": search_in,
                "search": search,
            },
            total=accorderie_type_fichier_count,
            page=page,
            step=self._items_per_page,
        )

        # content according to pager and archive selected
        accorderie_type_fichiers = AccorderieTypeFichier.search(
            domain,
            order=order,
            limit=self._items_per_page,
            offset=pager["offset"],
        )
        request.session[
            "my_accorderie_type_fichiers_history"
        ] = accorderie_type_fichiers.ids[:100]

        values.update(
            {
                "date": date_begin,
                "date_end": date_end,
                "accorderie_type_fichiers": accorderie_type_fichiers,
                "page_name": "accorderie_type_fichier",
                "archive_groups": archive_groups,
                "default_url": "/my/accorderie_type_fichiers",
                "pager": pager,
                "searchbar_sortings": searchbar_sortings,
                "searchbar_groupby": searchbar_groupby,
                "searchbar_inputs": searchbar_inputs,
                "search_in": search_in,
                "searchbar_filters": OrderedDict(
                    sorted(searchbar_filters.items())
                ),
                "sortby": sortby,
                "filterby": filterby,
            }
        )
        return request.render(
            "accorderie_canada_ddb.portal_my_accorderie_type_fichiers", values
        )

    @http.route(
        ["/my/accorderie_type_fichier/<int:accorderie_type_fichier_id>"],
        type="http",
        auth="public",
        website=True,
    )
    def portal_my_accorderie_type_fichier(
        self, accorderie_type_fichier_id=None, access_token=None, **kw
    ):
        try:
            accorderie_type_fichier_sudo = self._document_check_access(
                "accorderie.type.fichier",
                accorderie_type_fichier_id,
                access_token,
            )
        except (AccessError, MissingError):
            return request.redirect("/my")

        values = self._accorderie_type_fichier_get_page_view_values(
            accorderie_type_fichier_sudo, access_token, **kw
        )
        return request.render(
            "accorderie_canada_ddb.portal_my_accorderie_type_fichier", values
        )

    # ------------------------------------------------------------
    # My Accorderie Type Service
    # ------------------------------------------------------------
    def _accorderie_type_service_get_page_view_values(
        self, accorderie_type_service, access_token, **kwargs
    ):
        values = {
            "page_name": "accorderie_type_service",
            "accorderie_type_service": accorderie_type_service,
            "user": request.env.user,
        }
        return self._get_page_view_values(
            accorderie_type_service,
            access_token,
            values,
            "my_accorderie_type_services_history",
            False,
            **kwargs,
        )

    @http.route(
        [
            "/my/accorderie_type_services",
            "/my/accorderie_type_services/page/<int:page>",
        ],
        type="http",
        auth="user",
        website=True,
    )
    def portal_my_accorderie_type_services(
        self,
        page=1,
        date_begin=None,
        date_end=None,
        sortby=None,
        filterby=None,
        search=None,
        search_in="content",
        **kw,
    ):
        values = self._prepare_portal_layout_values()
        AccorderieTypeService = request.env["accorderie.type.service"]
        domain = []

        searchbar_sortings = {
            "date": {"label": _("Newest"), "order": "create_date desc"},
            "name": {"label": _("Name"), "order": "name"},
        }
        searchbar_filters = {
            "all": {"label": _("All"), "domain": []},
        }
        searchbar_inputs = {}
        searchbar_groupby = {}

        # default sort by value
        if not sortby:
            sortby = "date"
        order = searchbar_sortings[sortby]["order"]
        # default filter by value
        if not filterby:
            filterby = "all"
        domain = searchbar_filters[filterby]["domain"]

        # search
        if search and search_in:
            search_domain = []
            domain += search_domain
        # archive groups - Default Group By 'create_date'
        archive_groups = self._get_archive_groups(
            "accorderie.type.service", domain
        )
        if date_begin and date_end:
            domain += [
                ("create_date", ">", date_begin),
                ("create_date", "<=", date_end),
            ]
        # accorderie_type_services count
        accorderie_type_service_count = AccorderieTypeService.search_count(
            domain
        )
        # pager
        pager = portal_pager(
            url="/my/accorderie_type_services",
            url_args={
                "date_begin": date_begin,
                "date_end": date_end,
                "sortby": sortby,
                "filterby": filterby,
                "search_in": search_in,
                "search": search,
            },
            total=accorderie_type_service_count,
            page=page,
            step=self._items_per_page,
        )

        # content according to pager and archive selected
        accorderie_type_services = AccorderieTypeService.search(
            domain,
            order=order,
            limit=self._items_per_page,
            offset=pager["offset"],
        )
        request.session[
            "my_accorderie_type_services_history"
        ] = accorderie_type_services.ids[:100]

        values.update(
            {
                "date": date_begin,
                "date_end": date_end,
                "accorderie_type_services": accorderie_type_services,
                "page_name": "accorderie_type_service",
                "archive_groups": archive_groups,
                "default_url": "/my/accorderie_type_services",
                "pager": pager,
                "searchbar_sortings": searchbar_sortings,
                "searchbar_groupby": searchbar_groupby,
                "searchbar_inputs": searchbar_inputs,
                "search_in": search_in,
                "searchbar_filters": OrderedDict(
                    sorted(searchbar_filters.items())
                ),
                "sortby": sortby,
                "filterby": filterby,
            }
        )
        return request.render(
            "accorderie_canada_ddb.portal_my_accorderie_type_services", values
        )

    @http.route(
        ["/my/accorderie_type_service/<int:accorderie_type_service_id>"],
        type="http",
        auth="public",
        website=True,
    )
    def portal_my_accorderie_type_service(
        self, accorderie_type_service_id=None, access_token=None, **kw
    ):
        try:
            accorderie_type_service_sudo = self._document_check_access(
                "accorderie.type.service",
                accorderie_type_service_id,
                access_token,
            )
        except (AccessError, MissingError):
            return request.redirect("/my")

        values = self._accorderie_type_service_get_page_view_values(
            accorderie_type_service_sudo, access_token, **kw
        )
        return request.render(
            "accorderie_canada_ddb.portal_my_accorderie_type_service", values
        )

    # ------------------------------------------------------------
    # My Accorderie Type Service Categorie
    # ------------------------------------------------------------
    def _accorderie_type_service_categorie_get_page_view_values(
        self, accorderie_type_service_categorie, access_token, **kwargs
    ):
        values = {
            "page_name": "accorderie_type_service_categorie",
            "accorderie_type_service_categorie": accorderie_type_service_categorie,
            "user": request.env.user,
        }
        return self._get_page_view_values(
            accorderie_type_service_categorie,
            access_token,
            values,
            "my_accorderie_type_service_categories_history",
            False,
            **kwargs,
        )

    @http.route(
        [
            "/my/accorderie_type_service_categories",
            "/my/accorderie_type_service_categories/page/<int:page>",
        ],
        type="http",
        auth="user",
        website=True,
    )
    def portal_my_accorderie_type_service_categories(
        self,
        page=1,
        date_begin=None,
        date_end=None,
        sortby=None,
        filterby=None,
        search=None,
        search_in="content",
        **kw,
    ):
        values = self._prepare_portal_layout_values()
        AccorderieTypeServiceCategorie = request.env[
            "accorderie.type.service.categorie"
        ]
        domain = []

        searchbar_sortings = {
            "date": {"label": _("Newest"), "order": "create_date desc"},
            "name": {"label": _("Name"), "order": "name"},
        }
        searchbar_filters = {
            "all": {"label": _("All"), "domain": []},
        }
        searchbar_inputs = {}
        searchbar_groupby = {}

        # default sort by value
        if not sortby:
            sortby = "date"
        order = searchbar_sortings[sortby]["order"]
        # default filter by value
        if not filterby:
            filterby = "all"
        domain = searchbar_filters[filterby]["domain"]

        # search
        if search and search_in:
            search_domain = []
            domain += search_domain
        # archive groups - Default Group By 'create_date'
        archive_groups = self._get_archive_groups(
            "accorderie.type.service.categorie", domain
        )
        if date_begin and date_end:
            domain += [
                ("create_date", ">", date_begin),
                ("create_date", "<=", date_end),
            ]
        # accorderie_type_service_categories count
        accorderie_type_service_categorie_count = (
            AccorderieTypeServiceCategorie.search_count(domain)
        )
        # pager
        pager = portal_pager(
            url="/my/accorderie_type_service_categories",
            url_args={
                "date_begin": date_begin,
                "date_end": date_end,
                "sortby": sortby,
                "filterby": filterby,
                "search_in": search_in,
                "search": search,
            },
            total=accorderie_type_service_categorie_count,
            page=page,
            step=self._items_per_page,
        )

        # content according to pager and archive selected
        accorderie_type_service_categories = (
            AccorderieTypeServiceCategorie.search(
                domain,
                order=order,
                limit=self._items_per_page,
                offset=pager["offset"],
            )
        )
        request.session[
            "my_accorderie_type_service_categories_history"
        ] = accorderie_type_service_categories.ids[:100]

        values.update(
            {
                "date": date_begin,
                "date_end": date_end,
                "accorderie_type_service_categories": accorderie_type_service_categories,
                "page_name": "accorderie_type_service_categorie",
                "archive_groups": archive_groups,
                "default_url": "/my/accorderie_type_service_categories",
                "pager": pager,
                "searchbar_sortings": searchbar_sortings,
                "searchbar_groupby": searchbar_groupby,
                "searchbar_inputs": searchbar_inputs,
                "search_in": search_in,
                "searchbar_filters": OrderedDict(
                    sorted(searchbar_filters.items())
                ),
                "sortby": sortby,
                "filterby": filterby,
            }
        )
        return request.render(
            "accorderie_canada_ddb.portal_my_accorderie_type_service_categories",
            values,
        )

    @http.route(
        [
            "/my/accorderie_type_service_categorie/<int:accorderie_type_service_categorie_id>"
        ],
        type="http",
        auth="public",
        website=True,
    )
    def portal_my_accorderie_type_service_categorie(
        self,
        accorderie_type_service_categorie_id=None,
        access_token=None,
        **kw,
    ):
        try:
            accorderie_type_service_categorie_sudo = (
                self._document_check_access(
                    "accorderie.type.service.categorie",
                    accorderie_type_service_categorie_id,
                    access_token,
                )
            )
        except (AccessError, MissingError):
            return request.redirect("/my")

        values = self._accorderie_type_service_categorie_get_page_view_values(
            accorderie_type_service_categorie_sudo, access_token, **kw
        )
        return request.render(
            "accorderie_canada_ddb.portal_my_accorderie_type_service_categorie",
            values,
        )

    # ------------------------------------------------------------
    # My Accorderie Type Service Sous Categorie
    # ------------------------------------------------------------
    def _accorderie_type_service_sous_categorie_get_page_view_values(
        self, accorderie_type_service_sous_categorie, access_token, **kwargs
    ):
        values = {
            "page_name": "accorderie_type_service_sous_categorie",
            "accorderie_type_service_sous_categorie": accorderie_type_service_sous_categorie,
            "user": request.env.user,
        }
        return self._get_page_view_values(
            accorderie_type_service_sous_categorie,
            access_token,
            values,
            "my_accorderie_type_service_sous_categories_history",
            False,
            **kwargs,
        )

    @http.route(
        [
            "/my/accorderie_type_service_sous_categories",
            "/my/accorderie_type_service_sous_categories/page/<int:page>",
        ],
        type="http",
        auth="user",
        website=True,
    )
    def portal_my_accorderie_type_service_sous_categories(
        self,
        page=1,
        date_begin=None,
        date_end=None,
        sortby=None,
        filterby=None,
        search=None,
        search_in="content",
        **kw,
    ):
        values = self._prepare_portal_layout_values()
        AccorderieTypeServiceSousCategorie = request.env[
            "accorderie.type.service.sous.categorie"
        ]
        domain = []

        searchbar_sortings = {
            "date": {"label": _("Newest"), "order": "create_date desc"},
            "name": {"label": _("Name"), "order": "name"},
        }
        searchbar_filters = {
            "all": {"label": _("All"), "domain": []},
        }
        searchbar_inputs = {}
        searchbar_groupby = {}

        # default sort by value
        if not sortby:
            sortby = "date"
        order = searchbar_sortings[sortby]["order"]
        # default filter by value
        if not filterby:
            filterby = "all"
        domain = searchbar_filters[filterby]["domain"]

        # search
        if search and search_in:
            search_domain = []
            domain += search_domain
        # archive groups - Default Group By 'create_date'
        archive_groups = self._get_archive_groups(
            "accorderie.type.service.sous.categorie", domain
        )
        if date_begin and date_end:
            domain += [
                ("create_date", ">", date_begin),
                ("create_date", "<=", date_end),
            ]
        # accorderie_type_service_sous_categories count
        accorderie_type_service_sous_categorie_count = (
            AccorderieTypeServiceSousCategorie.search_count(domain)
        )
        # pager
        pager = portal_pager(
            url="/my/accorderie_type_service_sous_categories",
            url_args={
                "date_begin": date_begin,
                "date_end": date_end,
                "sortby": sortby,
                "filterby": filterby,
                "search_in": search_in,
                "search": search,
            },
            total=accorderie_type_service_sous_categorie_count,
            page=page,
            step=self._items_per_page,
        )

        # content according to pager and archive selected
        accorderie_type_service_sous_categories = (
            AccorderieTypeServiceSousCategorie.search(
                domain,
                order=order,
                limit=self._items_per_page,
                offset=pager["offset"],
            )
        )
        request.session[
            "my_accorderie_type_service_sous_categories_history"
        ] = accorderie_type_service_sous_categories.ids[:100]

        values.update(
            {
                "date": date_begin,
                "date_end": date_end,
                "accorderie_type_service_sous_categories": accorderie_type_service_sous_categories,
                "page_name": "accorderie_type_service_sous_categorie",
                "archive_groups": archive_groups,
                "default_url": "/my/accorderie_type_service_sous_categories",
                "pager": pager,
                "searchbar_sortings": searchbar_sortings,
                "searchbar_groupby": searchbar_groupby,
                "searchbar_inputs": searchbar_inputs,
                "search_in": search_in,
                "searchbar_filters": OrderedDict(
                    sorted(searchbar_filters.items())
                ),
                "sortby": sortby,
                "filterby": filterby,
            }
        )
        return request.render(
            "accorderie_canada_ddb.portal_my_accorderie_type_service_sous_categories",
            values,
        )

    @http.route(
        [
            "/my/accorderie_type_service_sous_categorie/<int:accorderie_type_service_sous_categorie_id>"
        ],
        type="http",
        auth="public",
        website=True,
    )
    def portal_my_accorderie_type_service_sous_categorie(
        self,
        accorderie_type_service_sous_categorie_id=None,
        access_token=None,
        **kw,
    ):
        try:
            accorderie_type_service_sous_categorie_sudo = (
                self._document_check_access(
                    "accorderie.type.service.sous.categorie",
                    accorderie_type_service_sous_categorie_id,
                    access_token,
                )
            )
        except (AccessError, MissingError):
            return request.redirect("/my")

        values = (
            self._accorderie_type_service_sous_categorie_get_page_view_values(
                accorderie_type_service_sous_categorie_sudo, access_token, **kw
            )
        )
        return request.render(
            "accorderie_canada_ddb.portal_my_accorderie_type_service_sous_categorie",
            values,
        )

    # ------------------------------------------------------------
    # My Accorderie Type Telephone
    # ------------------------------------------------------------
    def _accorderie_type_telephone_get_page_view_values(
        self, accorderie_type_telephone, access_token, **kwargs
    ):
        values = {
            "page_name": "accorderie_type_telephone",
            "accorderie_type_telephone": accorderie_type_telephone,
            "user": request.env.user,
        }
        return self._get_page_view_values(
            accorderie_type_telephone,
            access_token,
            values,
            "my_accorderie_type_telephones_history",
            False,
            **kwargs,
        )

    @http.route(
        [
            "/my/accorderie_type_telephones",
            "/my/accorderie_type_telephones/page/<int:page>",
        ],
        type="http",
        auth="user",
        website=True,
    )
    def portal_my_accorderie_type_telephones(
        self,
        page=1,
        date_begin=None,
        date_end=None,
        sortby=None,
        filterby=None,
        search=None,
        search_in="content",
        **kw,
    ):
        values = self._prepare_portal_layout_values()
        AccorderieTypeTelephone = request.env["accorderie.type.telephone"]
        domain = []

        searchbar_sortings = {
            "date": {"label": _("Newest"), "order": "create_date desc"},
            "name": {"label": _("Name"), "order": "name"},
        }
        searchbar_filters = {
            "all": {"label": _("All"), "domain": []},
        }
        searchbar_inputs = {}
        searchbar_groupby = {}

        # default sort by value
        if not sortby:
            sortby = "date"
        order = searchbar_sortings[sortby]["order"]
        # default filter by value
        if not filterby:
            filterby = "all"
        domain = searchbar_filters[filterby]["domain"]

        # search
        if search and search_in:
            search_domain = []
            domain += search_domain
        # archive groups - Default Group By 'create_date'
        archive_groups = self._get_archive_groups(
            "accorderie.type.telephone", domain
        )
        if date_begin and date_end:
            domain += [
                ("create_date", ">", date_begin),
                ("create_date", "<=", date_end),
            ]
        # accorderie_type_telephones count
        accorderie_type_telephone_count = AccorderieTypeTelephone.search_count(
            domain
        )
        # pager
        pager = portal_pager(
            url="/my/accorderie_type_telephones",
            url_args={
                "date_begin": date_begin,
                "date_end": date_end,
                "sortby": sortby,
                "filterby": filterby,
                "search_in": search_in,
                "search": search,
            },
            total=accorderie_type_telephone_count,
            page=page,
            step=self._items_per_page,
        )

        # content according to pager and archive selected
        accorderie_type_telephones = AccorderieTypeTelephone.search(
            domain,
            order=order,
            limit=self._items_per_page,
            offset=pager["offset"],
        )
        request.session[
            "my_accorderie_type_telephones_history"
        ] = accorderie_type_telephones.ids[:100]

        values.update(
            {
                "date": date_begin,
                "date_end": date_end,
                "accorderie_type_telephones": accorderie_type_telephones,
                "page_name": "accorderie_type_telephone",
                "archive_groups": archive_groups,
                "default_url": "/my/accorderie_type_telephones",
                "pager": pager,
                "searchbar_sortings": searchbar_sortings,
                "searchbar_groupby": searchbar_groupby,
                "searchbar_inputs": searchbar_inputs,
                "search_in": search_in,
                "searchbar_filters": OrderedDict(
                    sorted(searchbar_filters.items())
                ),
                "sortby": sortby,
                "filterby": filterby,
            }
        )
        return request.render(
            "accorderie_canada_ddb.portal_my_accorderie_type_telephones",
            values,
        )

    @http.route(
        ["/my/accorderie_type_telephone/<int:accorderie_type_telephone_id>"],
        type="http",
        auth="public",
        website=True,
    )
    def portal_my_accorderie_type_telephone(
        self, accorderie_type_telephone_id=None, access_token=None, **kw
    ):
        try:
            accorderie_type_telephone_sudo = self._document_check_access(
                "accorderie.type.telephone",
                accorderie_type_telephone_id,
                access_token,
            )
        except (AccessError, MissingError):
            return request.redirect("/my")

        values = self._accorderie_type_telephone_get_page_view_values(
            accorderie_type_telephone_sudo, access_token, **kw
        )
        return request.render(
            "accorderie_canada_ddb.portal_my_accorderie_type_telephone", values
        )

    # ------------------------------------------------------------
    # My Accorderie Ville
    # ------------------------------------------------------------
    def _accorderie_ville_get_page_view_values(
        self, accorderie_ville, access_token, **kwargs
    ):
        values = {
            "page_name": "accorderie_ville",
            "accorderie_ville": accorderie_ville,
            "user": request.env.user,
        }
        return self._get_page_view_values(
            accorderie_ville,
            access_token,
            values,
            "my_accorderie_villes_history",
            False,
            **kwargs,
        )

    @http.route(
        ["/my/accorderie_villes", "/my/accorderie_villes/page/<int:page>"],
        type="http",
        auth="user",
        website=True,
    )
    def portal_my_accorderie_villes(
        self,
        page=1,
        date_begin=None,
        date_end=None,
        sortby=None,
        filterby=None,
        search=None,
        search_in="content",
        **kw,
    ):
        values = self._prepare_portal_layout_values()
        AccorderieVille = request.env["accorderie.ville"]
        domain = []

        searchbar_sortings = {
            "date": {"label": _("Newest"), "order": "create_date desc"},
            "name": {"label": _("Name"), "order": "name"},
        }
        searchbar_filters = {
            "all": {"label": _("All"), "domain": []},
        }
        searchbar_inputs = {}
        searchbar_groupby = {}

        # default sort by value
        if not sortby:
            sortby = "date"
        order = searchbar_sortings[sortby]["order"]
        # default filter by value
        if not filterby:
            filterby = "all"
        domain = searchbar_filters[filterby]["domain"]

        # search
        if search and search_in:
            search_domain = []
            domain += search_domain
        # archive groups - Default Group By 'create_date'
        archive_groups = self._get_archive_groups("accorderie.ville", domain)
        if date_begin and date_end:
            domain += [
                ("create_date", ">", date_begin),
                ("create_date", "<=", date_end),
            ]
        # accorderie_villes count
        accorderie_ville_count = AccorderieVille.search_count(domain)
        # pager
        pager = portal_pager(
            url="/my/accorderie_villes",
            url_args={
                "date_begin": date_begin,
                "date_end": date_end,
                "sortby": sortby,
                "filterby": filterby,
                "search_in": search_in,
                "search": search,
            },
            total=accorderie_ville_count,
            page=page,
            step=self._items_per_page,
        )

        # content according to pager and archive selected
        accorderie_villes = AccorderieVille.search(
            domain,
            order=order,
            limit=self._items_per_page,
            offset=pager["offset"],
        )
        request.session[
            "my_accorderie_villes_history"
        ] = accorderie_villes.ids[:100]

        values.update(
            {
                "date": date_begin,
                "date_end": date_end,
                "accorderie_villes": accorderie_villes,
                "page_name": "accorderie_ville",
                "archive_groups": archive_groups,
                "default_url": "/my/accorderie_villes",
                "pager": pager,
                "searchbar_sortings": searchbar_sortings,
                "searchbar_groupby": searchbar_groupby,
                "searchbar_inputs": searchbar_inputs,
                "search_in": search_in,
                "searchbar_filters": OrderedDict(
                    sorted(searchbar_filters.items())
                ),
                "sortby": sortby,
                "filterby": filterby,
            }
        )
        return request.render(
            "accorderie_canada_ddb.portal_my_accorderie_villes", values
        )

    @http.route(
        ["/my/accorderie_ville/<int:accorderie_ville_id>"],
        type="http",
        auth="public",
        website=True,
    )
    def portal_my_accorderie_ville(
        self, accorderie_ville_id=None, access_token=None, **kw
    ):
        try:
            accorderie_ville_sudo = self._document_check_access(
                "accorderie.ville", accorderie_ville_id, access_token
            )
        except (AccessError, MissingError):
            return request.redirect("/my")

        values = self._accorderie_ville_get_page_view_values(
            accorderie_ville_sudo, access_token, **kw
        )
        return request.render(
            "accorderie_canada_ddb.portal_my_accorderie_ville", values
        )
