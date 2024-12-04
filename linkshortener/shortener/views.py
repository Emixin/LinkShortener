from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Link
from .forms import LinkForm
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings




class CreateorUpdateLinkView(View):
    def get(self, request):
        form = LinkForm()
        template_name = 'shortener/short_link.html'
        return render(request, template_name, {'form': form})

    def post(self, request):
        form = LinkForm(request.POST)

        if form.is_valid():
            original_url = form.cleaned_data['url']

            link_obj = Link(url=original_url)
            link_obj.set_short_url()
            link_obj.save()

            return HttpResponse(f"<p>{settings.HOST}/s/{link_obj.shortened_url}</p>")
        return render(request, 'shortener/short_link.html', {'form': form})


class ShortLinkView(View):
    def get(self, request, code):
        link = get_object_or_404(Link, shortened_url=code)
        if link.is_expired():
            return HttpResponse(status=404)
        link.increase_views()
        return HttpResponseRedirect(link.url)
    

class ViewsDetail(View):
    def get(self, request, code):
        link = get_object_or_404(Link, shortened_url=code)
        return HttpResponse(f"<p>views: {link.views}</p>")