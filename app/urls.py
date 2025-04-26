from django.urls import path

from app.views import blog_list, blog_detail, create_blog, update_blog, delete_blog, dashboard

urlpatterns = [
    path("", blog_list, name="blog_list"),
    path("<int:post_id>/", blog_detail, name="blog_detail"),
    path("create/", create_blog, name="create_blog"),
    path("update/<int:post_id>/", update_blog, name="update_blog"),
    path("delete/<int:post_id>/", delete_blog, name="delete_blog"),
    path("account/dashboard/", dashboard, name="dashboard"),
]
