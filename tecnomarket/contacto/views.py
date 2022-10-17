from django.shortcuts import render, redirect
from .forms import ContactoForm
from django.views.generic import TemplateView


# Create your views here.
class Contacto(TemplateView):
	template_name = "contacto.html"
	form_class = ContactoForm

	def get(self, request, *args, **kwargs):
		form = self.form_class
		return render(request, self.template_name, {'form': form})

	def post(self, request, *args, **kwargs):
		form = self. form_class(request.POST)
		if form.is_valid():
			form.save()
		return redirect("/")