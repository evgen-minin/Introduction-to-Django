from django.urls import path

from catalog.views import home_controller, contact_controller, ProductListView, ProductCreateView, BlogPostListView, \
    BlogPostCreateView, BlogPostUpdateView, BlogPostDeleteView, BlogPostDetailView, ProductDeleteView, \
    ProductUpdateView, VersionCreateView

urlpatterns = [
    path('', home_controller, name='home'),
    path('catalog/', ProductListView.as_view(), name='catalog'),
    path('create/', ProductCreateView.as_view(), name='create_product'),
    path('create_version/<int:product_id>/', VersionCreateView.as_view(), name='create_version'),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
    path('blog/create/', BlogPostCreateView.as_view(), name='blog_post_create'),
    path('blog/update/<slug:slug>/', BlogPostUpdateView.as_view(), name='blog_post_update'),
    path('blog/delete/<slug:slug>/', BlogPostDeleteView.as_view(), name='blog_post_delete'),
    path('blog/<slug:slug>/', BlogPostDetailView.as_view(), name='blog_post_detail'),
    path('blog/', BlogPostListView.as_view(), name='blog_post_list'),
]
