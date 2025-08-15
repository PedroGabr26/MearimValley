from django.contrib import admin


admin.site.site_header = "Painel Administrativo Mearim Valley"
admin.site.site_title = "Mearim Admin"

class GlobalAdmin(admin.AdminSite):
    class Media:
        css = {
            'all' : ('/static/css/admin_custom.css',)
        }