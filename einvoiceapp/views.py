from io import BytesIO
import qrcode
import qrcode.image.svg
from django.db.models.functions import Now
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
from django.utils import timezone
from .forms import EinvoiceForm
from .fatoora import Fatoora


# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class QRCodeFormView(FormView):
    template_name = 'index.html'
    initial = {'key': 'value'}
    form_class = EinvoiceForm

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            fatoora_obj = Fatoora(
                seller_name=form.cleaned_data['sellerName'],
                tax_number=form.cleaned_data['taxNumber'],
                # invoice_date=timezone.now(),
                invoice_date=form.cleaned_data['timeStamp'],
                total_amount=form.cleaned_data['totalAmount'],
                tax_amount=form.cleaned_data['taxAmount'])

            qr = fatoora_obj.qrcode_svg(fatoora_obj.base64)

            return render(request, 'success.html', {'fatoora_obj': fatoora_obj, 'qr': qr})

        return render(request, self.template_name, {'form': form})

        # print(fatoora_obj.base64)
        # fatoora_obj.qrcode("qr_code.png")


class SuccessView(TemplateView):
    template_name = 'success.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
