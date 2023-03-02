from django.urls import path
from .views import news_list, news_detail, contact_us, error_404, about_us, homepage, \
    LocalNewsView, SportNewsView, TechnologyNewsView, BusinessNewsView


urlpatterns = [
    path('', homepage, name="home_page"),
    path('news/', news_list, name="all_news"),
    path('news/<slug:news>/', news_detail, name="news_detail"),
    path('local-news/', LocalNewsView.as_view(), name="local_news"),
    path('sport-news/', SportNewsView.as_view(), name="sport_news"),
    path('technology-news/', TechnologyNewsView.as_view(), name="technology_news"),
    path('business-news/', BusinessNewsView.as_view(), name="business_news"),

    # Additional links
    path('contact-us/', contact_us, name="contact_page"),
    path('about-us/', about_us, name="about_page"),
    path('error-page', error_404, name="error_page"),
]