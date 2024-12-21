from  site_setup.models import SiteSetup


def site_setup(request):

    
    try:
        setup = SiteSetup.objects.order_by('-id')[0]
    except IndexError:
        setup = None
    return {
        'site_setup': setup,
    }  #
