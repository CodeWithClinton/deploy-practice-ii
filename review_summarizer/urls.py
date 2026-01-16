"""
URL configuration for review_summarizer project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('review_app.urls')),   
]





# [Unit]
# Description=gunicorn daemon
# Requires=gunicorn.socket
# After=network.target

# [Service]
# User=chibunna
# Group=www-data
# WorkingDirectory=/home/chibunna/deploy-pratice-i
# ExecStart=/home/chibunna/deploy-pratice-i/venv/bin/gunicorn \
#           --access-logfile - \
#           --workers 3 \
#           --bind unix:/run/gunicorn.sock \
#           review_summarizer.wsgi:application

# [Install]
# WantedBy=multi-user.target



# server {
#     listen 80;
#     server_name 138.68.158.95;

#     location = /favicon.ico { access_log off; log_not_found off; }
#     location /staticfiles/ {
#         root /home/chibunna/deploy-practice-i;
#     }

#     location / {
#         include proxy_params;
#         proxy_pass http://unix:/run/gunicorn.sock;
#     }
# }