from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.utils.text import slugify
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView

from catalog.forms import ProductForm, BlogPostForm
from catalog.models import Product, BlogPost


def home_controller(request):
    latest_blog_posts = BlogPost.objects.order_by('-created_at')[:3]
    return render(request, 'catalog/home.html', {'blog_posts': latest_blog_posts})


def contact_controller(request):
    if request.method == 'POST':
        firstname = request.POST.get('first_name')
        lastname = request.POST.get('last_name')
        email = request.POST.get('email')
        print(f"{firstname} {lastname} {email}")

        return render(request, 'catalog/success.html')

    return render(request, 'catalog/contacts.html')


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/card_product.html'


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
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
        form.instance.slug = slugify(form.instance.title)
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

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.views += 1
        self.object.save()
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)
