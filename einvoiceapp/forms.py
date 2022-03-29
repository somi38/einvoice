from django import forms


class EinvoiceForm(forms.Form):
    sellerName = forms.CharField(label="Seller Name", max_length=50)
    taxNumber = forms.IntegerField(label="Tax Number")
    timeStamp = forms.DateTimeField(label="Date Time")
    totalAmount = forms.FloatField(label="Total Amount")
    taxAmount = forms.FloatField(label="Tax Amount")

