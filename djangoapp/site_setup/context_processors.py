from  site_setup.models import SiteSetup


def site_setup(request):

    site_setup = SiteSetup.objects.order_by('-id')[0]
    return {
        
        'site_setup': {
            'title': site_setup,
            'description': site_setup.description,
        }
    }  #