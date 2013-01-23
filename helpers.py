from models import Update
from blog.models import Post
from operator import itemgetter
import simplejson as json

def collect_updates(page=1, req_project=False):
    """
    Returns a JSON array of recent entries.
    This is hackier than I would like it to be, but it still seems better to
    isolate this code where it's easier to access than cramming it all into
    views.py or somesuch.
    """
    items = []

    if(req_project):
        if(req_project == "all"):
            for w in Update.objects.all():
                items.append(w.get_frontpage_json())
        else:
            for z in Update.objects.filter(project__slug=req_project):
                items.append(z.get_frontpage_json())

    else:
        # Home page shows blog posts, too.
        for x in Update.objects.all():
            items.append(x.get_frontpage_json())

        for y in Post.objects.all():
            items.append(y.get_frontpage_json())

    # Need to sort by date here
    items = sorted(items, key=itemgetter('created'), reverse=True)

    # Handle pagination, if crudely...
    if page == "all":
        return json.dumps(items)

    page_end = int(page) * 10
    if page_end - len(items) > 10: return 0
    if page_end > len(items): page_end = len(items)
    if page_end % 10: page_start = page_end - (page_end % 10)
    else: page_start = page_end - 10
    
    # Return requested pages as JSONified string
    return json.dumps(items[page_start:page_end])
