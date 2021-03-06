"""ProsenjitKumar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from base.sitemaps import (
    BlogPostSitemap,
    PortfolioSitemap,
    QuestionSiteMap,
    ContactSitemap,
)
from django.contrib.sitemaps.views import sitemap

sitemaps = {
    'blog_posts': BlogPostSitemap,
    'question_post': QuestionSiteMap,
    'portfolio_static': PortfolioSitemap,
    'contact_static': ContactSitemap,
}

urlpatterns = [
    path('prosenjit-admin/', admin.site.urls),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),
    path('', include('portfolio.urls')),
    path('', include('blog.urls', namespace='slug')),
    path('accounts/', include('accounts.urls')),
    path('', include('subscription_join.urls')),
    path('review/', include('reviews.urls')),
    path('e-commerce/', include('e_commerce.cart.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
