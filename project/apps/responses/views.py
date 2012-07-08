from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from annoying.decorators import *
from responses.forms import ResponseForm
from responses.models import EnoughResponse

@render_to("responses/entry.html")
def entry(request):
    if request.method == "POST":
        form = ResponseForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("saved"))
    else:
        form = ResponseForm
    return locals()

@render_to("responses/saved.html")
def saved(request):
    return locals()

@render_to("responses/begin.html")
def begin(request):
    enough_responses = EnoughResponse.objects.count() > 5
    print enough_responses
    return locals()


@render_to("responses/display_all.html")
def display_all(request):
    all_responses = EnoughResponse.objects.all().order_by("?")
    return locals()


@render_to("responses/display_one.html")
def display_one(request):
    if "last" in request.GET:
        last = request.GET["last"]
        responses = EnoughResponse.objects.filter(order__gt=int(last))
        if responses.count() == 0:
            one_response = EnoughResponse.objects.all()[0]
        else:
            one_response = responses[0]
    else:
        one_response = EnoughResponse.objects.all()[0]

    return locals()