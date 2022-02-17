# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-zi$rk!2=#dm0%@y^&0*=u8iad4=0!f_^lra8s45p0l=go528d6'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'heroes_villains_database',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'Daughtry'
    }
}