from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView

from item.form import CategoryForm
from item.models import Category


class HelloView(TemplateView):
    """
    A view that renders the home page.

    Attributes:
    template_name (str): The name of the HTML template to use.

    Methods:
    get_context_data(**kwargs): Adds the 'title' key to the context dictionary.
    """
    template_name = 'item/home.html'

    def get_context_data(self, **kwargs):
        """
        Adds the 'title' key to the context dictionary.

        Parameters:
        **kwargs: Arbitrary keyword arguments.

        Returns:
        dict: The updated context dictionary.
        """
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home Page'
        return context


class ItemListView(ListView):
    model = Category
    template_name = 'item/item_list.html'
    context_object_name = 'items'


class ItemDetailView(DetailView):
    model = Category
    template_name = 'item/item_detail.html'
    context_object_name = 'item'


class ItemCreateView(CreateView):
    # model name , form name, template name
    model = Category
    form_class = CategoryForm
    template_name = "item/item_create.html"
    success_url = reverse_lazy('item')
