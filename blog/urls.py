from blog.views import post_model_list_view, post_model_detail_view, post_model_create_view, post_model_update_view, \
    post_model_delete_view
from django.urls import path

app_name = "blog"

urlpatterns = [
    path("", post_model_list_view, name="list"),
    path("create/", post_model_create_view, name="create"),
    path("<int:id>/", post_model_detail_view, name="detail"),
    path("<int:id>/edit/", post_model_update_view, name="update"),
    path("<int:id>/delete/", post_model_delete_view, name="delete"),
]
