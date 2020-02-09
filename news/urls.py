
from django.urls import path
from .views import ListSwedishwordsView, all_word_api, top_ten, all_word_count


urlpatterns = [
    path('swedishwords/', ListSwedishwordsView.as_view(), name="swedishwords-all"),
    path('topten/', top_ten),
    path('allwordcount/', all_word_count),

]


