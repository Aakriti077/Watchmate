from django.urls import path
from rest_framework import routers

from watchlist_app.api.v1 import views
from watchlist_app.api.v1.views import ReviewModelViewSet, StreamPlatformModelViewSet, ReviewModelViewSet
from watchlist_app.models import StreamPlatform

# review_list = ReviewListViewSet.as_view({'get':'list'})
# review_detail = ReviewModelViewSet.as_view({'get':'retrieve'})

router = routers.DefaultRouter()
router.register("review",ReviewModelViewSet, basename="reviews")
router.register("stream",StreamPlatformModelViewSet,basename='stream')

urlpatterns = []

urlpatterns = [
    path("list/", views.MovieListAV.as_view(), name="movie_list"),
    path("list/<int:pk>/", views.MovieDetailAV.as_view(), name="movie_detail"),

    # path("stream/", views.StreamPlatformAV.as_view(), name="stream_list"),

    # path("review/", views.ReviewListAV.as_view(), name="review_list"),
    # path("review/<int:pk>/", views.ReviewDetailAV.as_view(), name="review_detail"),

    # path("review/",review_list,name="review_list"),
    # path("review/<int:pk>/",review_detail,name="review_detail"),

] + router.urls
