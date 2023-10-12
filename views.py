from kernel.http import Response
from link_manager.models import Link, LinkOpened
from link_manager.libs import setUrlOpened
from profiles.decorators import load_profile

@load_profile
def mark_link_opened(request):
    """
        @description: Ont s'ent va marquer un link comme ouvert 
    """
    res = Response()
    url = request.POST.get('url', None)
    if url is None:
        return res.error('request.post.URL is required')
    
    
    setUrlOpened(url, request.profile)
    return res.success()

