# Django settings for Biblioteca project.

# Generated by 'django-admin startproject' using Django 4.0.7.

# For more information on this file, see
# https://docs.djangoproject.com/en/4.0/topics/settings/

# For the full list of settings and their values, see
# https://docs.djangoproject.com/en/4.0/ref/settings/


import os
from pathlib import Path
from django.contrib.messages import constants as message_constants
import dj_database_url
from dotenv import load_dotenv

# Cargar variables de entorno desde un archivo .env si existe (para desarrollo local)
# Asegúrate de que .env esté en tu .gitignore para no subirlo a producción.
load_dotenv()


MESSAGE_TAGS = {
    message_constants.ERROR: 'error',
}

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# Usa la variable de entorno 'SECRET_KEY' en producción.
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-s=ijw7-8rm4r70q+6$n_3874g645ck$9$)3ogjj6w21#9ew5wu')

# SECURITY WARNING: don't run with debug turned on in production!
# Asegúrate de que en Render la variable DEBUG esté como 'False' (cadena de texto)
DEBUG = (os.environ.get('DEBUG', 'False').lower() == 'true')

# ALLOWED_HOSTS para tu despliegue en Render y desarrollo local
ALLOWED_HOSTS = []
RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)
ALLOWED_HOSTS += ['localhost', '127.0.0.1']


# Application definition
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'login'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Aplicaciones.Cursos',
    'storages', # Necesario para django-storages y AWS S3 para los archivos media y estáticos
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # Whitenoise se debe usar SOLO si no estás sirviendo estáticos desde S3 en producción.
    # Si DEBUG es True y quieres servir estáticos localmente sin S3, puedes descomentarlo.
    # Para producción con S3, DEBE estar comentado o excluido.
    # 'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Biblioteca.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Biblioteca.wsgi.application'


# **** INICIO: CONFIGURACIÓN DE AWS S3 PARA ARCHIVOS MEDIA Y ESTÁTICOS ****
# Estas variables se leerán de las que configuraste en Render o de .env localmente
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
AWS_S3_REGION_NAME = os.environ.get('AWS_S3_REGION_NAME', 'us-east-2') # Tu región confirmada

# Inicializar STORAGE_TYPE como "local" por defecto
STORAGE_TYPE = "local"

# Cargar variables de entorno de depuración para ver si se usan
# Estas líneas de "print" te ayudarán a ver si las variables de entorno se están cargando
# correctamente. ¡Elimínalas una vez que todo funcione!
print(f"DEBUG: AWS_ACCESS_KEY_ID cargado: {bool(AWS_ACCESS_KEY_ID)}")
print(f"DEBUG: AWS_SECRET_ACCESS_KEY cargado: {bool(AWS_SECRET_ACCESS_KEY)}")
print(f"DEBUG: AWS_STORAGE_BUCKET_NAME cargado: {AWS_STORAGE_BUCKET_NAME}")
print(f"DEBUG: AWS_S3_REGION_NAME cargado: {AWS_S3_REGION_NAME}")
print(f"DEBUG: DEBUG es: {DEBUG}")

# Condición principal para usar S3:
# Solo usaremos S3 si NO estamos en DEBUG (es decir, en producción)
# Y si todas las variables de entorno de AWS están presentes.
if not DEBUG and AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY and AWS_STORAGE_BUCKET_NAME and AWS_S3_REGION_NAME:
    STORAGE_TYPE = "s3"
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.{AWS_S3_REGION_NAME}.amazonaws.com'
    print(f"DEBUG: Se usará AWS S3 para almacenamiento. Dominio: {AWS_S3_CUSTOM_DOMAIN}")

    AWS_S3_FILE_OVERWRITE = False # No permitir sobrescribir archivos con el mismo nombre por defecto
    AWS_DEFAULT_ACL = 'public-read' # ¡CRUCIAL! Hace que los archivos subidos sean públicamente legibles
    AWS_QUERYSTRING_AUTH = False # No genera URLs con firma si los archivos son públicos (ideal para archivos públicos)
    AWS_S3_VERIFY = True # Verificar certificados SSL para mayor seguridad

    # Configuración de almacenamiento para S3
    # Este es el almacenamiento por defecto para Model.FileField y Model.ImageField
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    # Esta es la URL base para tus archivos media en S3
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/media/'
    # No es necesario definir MEDIA_ROOT cuando usas S3 como almacenamiento por defecto
    MEDIA_ROOT = ''

    # Configuración para archivos estáticos para que también usen S3
    STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    # La URL base para tus archivos estáticos ahora será en S3, dentro de la carpeta 'static/'
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/static/'

    # Define dónde se guardarán los archivos estáticos recolectados temporalmente antes de subirlos a S3.
    STATIC_ROOT = BASE_DIR / 'staticfiles_collected' # Nombre más descriptivo

else:
    # Si DEBUG es True, o faltan credenciales AWS, o STORAGE_TYPE no es "s3", usamos almacenamiento local.
    STORAGE_TYPE = "local"
    print(f"DEBUG: Se usará almacenamiento LOCAL. DEBUG: {DEBUG}, Credenciales AWS_ACCESS_KEY_ID presentes: {bool(AWS_ACCESS_KEY_ID)}")

    DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'
    STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

    STATIC_URL = '/static/'
    MEDIA_URL = '/media/'

    STATIC_ROOT = BASE_DIR / 'staticfiles_local' # Un directorio diferente para evitar conflictos si pruebas S3
    MEDIA_ROOT = BASE_DIR / 'media_local' # Define un MEDIA_ROOT local si no se usa S3


# STATICFILES_DIRS es donde Django busca los archivos estáticos antes de collectstatic
# Esto se aplica tanto si usas S3 como si no.
STATICFILES_DIRS = [
    BASE_DIR / 'Biblioteca' / 'static', # Esta es la ruta correcta según tu repositorio en GitHub
    # Puedes añadir más directorios si tienes archivos estáticos en otras apps.
]

# FIN: CONFIGURACIÓN DE AWS S3 PARA MEDIA Y ESTÁTICOS


DATABASES = {
    'default': dj_database_url.config(
        default=os.getenv('DATABASE_URL', f'sqlite:///{BASE_DIR}/BDD.Biblioteca.db'),
        conn_max_age=600,
        conn_health_checks=True,
    )
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'es-ec'

TIME_ZONE = 'America/Guayaquil'

USE_I18N = True

USE_TZ = True

# Agregar configuración de mensajes
MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'


# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'