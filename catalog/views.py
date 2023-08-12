from django.core.mail import send_mail

from django.shortcuts import render
from django.urls import reverse_lazy, reverse

from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView

from catalog.forms import ProductForm, BlogPostForm, VersionForm
from catalog.models import Product, BlogPost, Version
from django.contrib.auth.decorators import login_required

def home_controller(request):
    latest_blog_posts = BlogPost.objects.order_by('-created_at')[:3]
    return render(request, 'catalog/home.html', {'blog_posts': latest_blog_posts})


def contact_controller(request):
    if request.method == 'POST':
        firstname = request.POST.get('first_name')
        lastname = request.POST.get('last_name')
        email = request.POST.get('email')
        print(f"{firstname} {lastname} {email}")

        return render(request, 'catalog/sucsess.html')

    return render(request, 'catalog/contacts.html')


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/card_product.html'
    context_object_name = 'object_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product_id'] = self.kwargs.get('product_id', None)
        return context


class VersionCreateView(CreateView):
    model = Version
    form_class = VersionForm
    template_name = 'catalog/version_form.html'
    success_url = reverse_lazy('catalog')

    def form_valid(self, form):
        form.instance.product = Product.objects.get(pk=self.kwargs['product_id'])
        form.instance.is_current_version = True

        active_version = form.instance.product.versions.filter(is_current_version=True).first()
        if active_version:
            active_version.is_current_version = False
            active_version.save()

        return super().form_valid(form)


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog')
    
    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()
        
        return super().form_valid(form)
        
    def test_func(self):
        return self.request.user.is_authenticated

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_update.html'
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('catalog')


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'catalog/product_delete.html'
    success_url = reverse_lazy('catalog')


class BlogPostListView(ListView):
    model = BlogPost
    template_name = 'catalog/blog_post_list.html'
    context_object_name = 'blog_posts'

    def get_queryset(self):
        return BlogPost.objects.filter(is_published=True)


class BlogPostCreateView(CreateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = 'catalog/blog_post_create.html'
    success_url = reverse_lazy('blog_post_list')

    def form_valid(self, form):
        form.instance.slug = form.instance.title
        return super().form_valid(form)


class BlogPostUpdateView(UpdateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = 'catalog/blog_post_update.html'
    context_object_name = 'blog_post'

    def get_success_url(self):
        return reverse('blog_post_detail', kwargs={'slug': self.object.slug})


class BlogPostDeleteView(DeleteView):
    model = BlogPost
    template_name = 'catalog/blog_post_delete.html'
    success_url = reverse_lazy('blog_post_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blog_post'] = self.object
        return context


class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = 'catalog/blog_post_detail.html'
    context_object_name = 'blog_post'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        obj.views += 1
        obj.save()

        if obj.views == 100:
            subject = 'Поздравляем! Ваша статья набрала 100 просмотров'
            message = f'Ваша статья "{obj.title}" набрала 100 просмотров. Продолжайте в том же духе!'
            from_email = ''
            to_email = ['mininevgen2906@yandex.ru']
            send_mail(subject, message, from_email, to_email)

        return obj
