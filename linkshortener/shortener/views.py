from django.shortcuts import render
from django.views import View
from .models import Link
from .forms import LinkForm
from django.http import HttpResponse


# Create your views here.


class CreateorUpdateLinkView(View):
    def get(self, request):
        form = LinkForm()
        template_name = 'shortener/short_link.html'
        return render(request, template_name, {'form': form})

    def post(self, request):
        form = LinkForm(request.POST)

        if form.is_valid():
            original_url = form.cleaned_data['url']
            shortened = form.cleaned_data['shortened_url']

            link_obj = Link.objects.filter(url=original_url).first()

            if link_obj:
                if not shortened:
                    shortened = link_obj.create_short_url()
                base_url = ''.join(original_url.split('/', 3)[1:3])
                base_url = 'https://' + base_url
                link_obj.shortened_url = base_url + '/' + shortened
                link_obj.save()

            else:
                if not shortened:
                    shortened = Link().create_short_url()
                base_url = ''.join(original_url.split('/', 3)[1:3])
                base_url = 'https://' + base_url
                link_obj = Link.objects.create(url=original_url, shortened_url=base_url + '/' + shortened)
            

            return HttpResponse(f"short link: {link_obj.shortened_url}")
        return render(request, 'shortener/short_link.html', {'form': form})