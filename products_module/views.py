from django.contrib import messages
from django.db.models import F
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView

from .forms import PhoneModelform, BrandModelform
from .models import Phone, Brand


def home_view(request):
    return render(request, 'products_module/home_page.html')


class FormsView(TemplateView):
    template_name = 'products_module/forms_page.html'


class PhoneFormView(FormView):
    form_class = PhoneModelform
    template_name = 'products_module/phone_form_page.html'
    success_url = reverse_lazy('phone_form_page')

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'محصول مورد نظر با موفقیت ذخیره شد!')
        return super(PhoneFormView, self).form_valid(form)


class BrandFormView(FormView):
    form_class = BrandModelform
    template_name = 'products_module/brand_form_page.html'
    success_url = reverse_lazy('brand_form_page')

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'برند مورد نظر با موفقیت ذخیره شد!')
        return super(BrandFormView, self).form_valid(form)


def reports_view(request):
    data = None
    query = request.GET.get('query')
    if not query:
        return render(request, 'products_module/reports_page.html')
    elif int(query) == 1:
        data = list(Brand.objects.filter(brand_nationality='Korea').values())
    elif int(query) == 2:
        brand = request.GET.get('brand')
        data = list(Phone.objects.filter(brand__brand_name__iexact=brand).values())
    elif int(query) == 3:
        data = list(Phone.objects.filter(brand__brand_nationality=F('manufacturing_country')).values())
    else:
        return JsonResponse({'message': 'Invalid query parameter.'}, status=400)
    return JsonResponse(data, safe=False)
