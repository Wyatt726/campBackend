SECRET_KEY = 'django-insecure-7kepo2v&m^%ubza=*wl(i%&cbcd=qu7o$zownq^chw+1q37^ma'

DATABASES = {
    'default':{
        'ENGINE': 'mysql.connector.django',
        'NAME': 'CampTrail',
        'USER': 'root',
        'PASSWORD': 'Number11',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS':{
            'autocommit': True
        }
    }
}