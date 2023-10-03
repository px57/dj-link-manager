from kernel.http import Response
from link_manager.models import Link, LinkOpened
from profiles.decorators import load_profile

@load_profile
def mark_link_opened(request):
    """
        @description: Ont s'ent va marquer un link comme ouvert 
    """
    res = Response()
    url = request.GET.get('url', None)
    if url is None:
        return res.error('request.post.URL is required')
    
    link = Link.objects.filter(full_url=url).first()
    # if link is None:
    #     link =
    
    # link_opened = LinkOpened.objects.filter(

    return res.success()