SECRET_KEY = 'dev'
DEBUG = True
ALLOWED_HOSTS = []
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
INSTALLED_APPS = ['resume_app', 'django.contrib.admin', 'django.contrib.auth',
'django.contrib.contenttypes', 'django.contrib.sessions', 'django.contrib.messages',
'django.contrib.staticfiles']
MIDDLEWARE = ['django.middleware.security.SecurityMiddleware', 'django.contrib.sessions.middleware.SessionMiddleware',
'django.middleware.common.CommonMiddleware', 'django.middleware.csrf.CsrfViewMiddleware',
'django.contrib.auth.middleware.AuthenticationMiddleware', 'django.contrib.messages.middleware.MessageMiddleware']
ROOT_URLCONF = 'resume_analyzer.urls'
TEMPLATES = [{'BACKEND': 'django.template.backends.django.DjangoTemplates',
'DIRS': ['resume_app/templates'], 'APP_DIRS': True,
'OPTIONS': {'context_processors': ['django.template.context_processors.debug',
'django.template.context_processors.request', 'django.contrib.auth.context_processors.auth',
'django.contrib.messages.context_processors.messages']}}]
WSGI_APPLICATION = 'resume_analyzer.wsgi.application'
DATABASES = {'default': {'ENGINE': 'django.db.backends.sqlite3', 'NAME': 'db.sqlite3'}}
STATIC_URL = '/static/'
STATICFILES_DIRS = ['resume_app/static']
