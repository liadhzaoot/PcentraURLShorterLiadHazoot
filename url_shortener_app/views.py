import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, Http404, HttpResponseRedirect

from .models import UrlShortener

@csrf_exempt
def home_view(request):
    if request.method == 'GET':
        return HttpResponse("test")
    if request.method == 'POST':
        my_json = request.body.decode('utf8').replace("'", '"')
        data = json.loads(my_json)

        shortened_object = UrlShortener.objects.create(long_url=data["url"])  # generate new short_url
        short_url = request.build_absolute_uri('/s/') + shortened_object.short_url
        if shortened_object:
            return HttpResponse(short_url, status=201)  # status 201 craeted
    return Http404({"error": "not created"})  # status 404 not found


def redirect_url_view(request, shortened_part):

    try:
        shortener = UrlShortener.objects.get(short_url=shortened_part)
        shortener.click_count += 1
        shortener.save()
        return HttpResponseRedirect(shortener.long_url)

    except:
        raise Http404('Sorry this link is broken...')