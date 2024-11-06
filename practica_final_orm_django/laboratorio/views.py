from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Laboratorio

def inicio(request):
    return render(request, 'laboratorio/base.html')

class LaboratorioListView(ListView):
    model = Laboratorio
    template_name = 'laboratorio/laboratorio_list.html'
    context_object_name = 'laboratorios'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['visit_count'] = self.request.session.get('visit_count', 0)
        self.request.session['visit_count'] = context['visit_count'] + 1
        return context

class LaboratorioCreateView(CreateView):
    model = Laboratorio
    template_name = 'laboratorio/laboratorio_form.html'
    fields = ['nombre', 'ciudad', 'pais']
    success_url = reverse_lazy('laboratorio_list')

class LaboratorioUpdateView(UpdateView):
    model = Laboratorio
    template_name = 'laboratorio/laboratorio_form.html'
    fields = ['nombre', 'ciudad', 'pais']
    success_url = reverse_lazy('laboratorio_list')

class LaboratorioDeleteView(DeleteView):
    model = Laboratorio
    template_name = 'laboratorio/laboratorio_confirm_delete.html'
    success_url = reverse_lazy('laboratorio_list')