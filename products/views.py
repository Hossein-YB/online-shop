from django.shortcuts import render
from django.views import generic
from .models import Products, Comments
from .forms import CommentForm
from django.shortcuts import get_object_or_404, reverse
from django.utils.translation import gettext as _
from django.contrib import messages


class ProductListView(generic.ListView):
    # model = Products
    queryset = Products.objects.filter(active=True)
    template_name = 'products/product_list.html'
    context_object_name = 'products'
    paginate_by = 8


class ProductDetailView(generic.DetailView):
    model = Products
    template_name = 'products/product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        return context


class CommentCreateView(generic.CreateView):
    model = Comments
    form_class = CommentForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        if self.request.user.is_authenticated:
            obj.user = self.request.user
            product_id = int(self.kwargs['product_id'])
            product = get_object_or_404(Products, id=product_id)
            obj.product = product
            messages.success(self.request, _('Your comment was successfully registered'))
            return super().form_valid(form)
        else:
            return reverse('account_login')

