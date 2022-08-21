from odoo import http
from odoo.addons.portal.controllers.web import Home as home
from odoo.http import request

# class AccorderieMembreHome(home):
#     @http.route()
#     def index(self, *args, **kw):
#         if request.session.uid and not request.env["res.users"].sudo().browse(
#             request.session.uid
#         ).has_group("base.group_user"):
#             return http.local_redirect(
#                 "/explorer", query=request.params, keep_hash=True
#             )
#         return super(AccorderieMembreHome, self).index(*args, **kw)
#
#     def _login_redirect(self, uid, redirect=None):
#         if not redirect and not request.env["res.users"].sudo().browse(
#             uid
#         ).has_group("base.group_user"):
#             return http.local_redirect(
#                 "/explorer", query=request.params, keep_hash=True
#             )
#         return super(AccorderieMembreHome, self)._login_redirect(
#             uid, redirect=redirect
#         )
