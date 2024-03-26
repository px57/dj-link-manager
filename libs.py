
from django.db.models import Q
from link_manager.models import LinkOpened, Link

def findUrl(url):
    """
        @description: 
        @param url: string -> url to find
        @param dbProfile: Profile -> user profile 
    """
    return Link.objects.filter(full_url=url).first()

def get_or_create_url(url):
    """
        @description: 
        @param url: string -> url to find
        @param dbProfile: Profile -> user profile
    """
    dbLink = findUrl(url)
    if dbLink is None:
        dbLink = Link()
        dbLink.full_url = url
        dbLink.decompose_full_url()
        dbLink.save()
    return dbLink

def setUrlOpened(url, dbProfile=None):
    """
        @description: Send one url and save. 
    """
    dbLink = get_or_create_url(url)
    dbLinkOpened = LinkOpened()
    dbLinkOpened.link = dbLink
    dbLinkOpened.profile = dbProfile
    dbLinkOpened.save()
    return dbLinkOpened

def getUrlListOpened(url_list, dbProfile=None):
    """
        @description: Get list of urls and return list of urls opened.
    """
    query = Q()
    for url in url_list:
        query |= Q(link__full_url=url)

    if dbProfile is not None:
        query &= Q(profile=dbProfile)
    dbLinkOpened = LinkOpened.objects.filter(query)
    return dbLinkOpened
