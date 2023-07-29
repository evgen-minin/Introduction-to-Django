from django.urls import path

from catalog.views import home_controller, contact_controller, ProductListView, ProductCreateView, BlogPostListView, \
    BlogPostCreateView, BlogPostUpdateView, BlogPostDeleteView, BlogPostDetailView

urlpatterns = [
    path('', home_controller, name='home'),
    path('contacts/', contact_controller, name='contacts'),
    path('catalog/', ProductListView.as_view(), name='catalog'),
    path('create/', ProductCreateView.as_view(), name='create_product'),
    path('blog/create/', BlogPostCreateView.as_view(), name='blog_post_create'),
    path('blog/update/<slug:slug>/', BlogPostUpdateView.as_view(), name='blog_post_update'),
    path('blog/delete/<slug:slug>/', BlogPostDeleteView.as_view(), name='blog_post_delete'),
    path('blog/<slug:slug>/', BlogPostDetailView.as_view(), name='blog_post_detail'),
    path('blog/', BlogPostListView.as_view(), name='blog_post_list'),
]
