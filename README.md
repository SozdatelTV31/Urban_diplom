# Urban_diplom.
---
Проект заключается в создании веб-приложения на основе фреймворка Django, которое позволит пользователям использовать предварительно обученную модель для обнаружения и классификации объектов на фотографиях. Для этого потребуется наличие механизмов регистрации и авторизации пользователей, чтобы каждый пользователь мог создать учетную запись и просматривать только свои загруженные изображения. Для создания интерфейса будет использоваться Bootstrap. В качестве модели для обнаружения объектов предлагается использовать MobileNet SSD.  
Для входа домой ссылка:ip/main/  
Файловая структура проекта:  
│  db.new   
│  manage.py  
│  
├─── web_site  
│  │  asgi.py  
│  │  settings.py  
│  │  urls.py  
│  │  wsgi.py  
│  │  __init__.py  
│  │  
│  
├───media  
│  ├───images  
│  │  
│  └───processed_images  
│  
└───object_detection  
   │  admin.py  
   │  apps.py  
   │  forms.py  
   │  mobilenet_iter_73000.caffemodel  
   │  mobilenet_ssd_deploy.prototxt  
   │  models.py  
   │  tests.py  
   │  urls.py  
   │  utils.py  
   │  views.py  
   │  __init__.py  
   │  
   ├───migrations  
   │  │  0001_initial.py  
   │  │    0002_imagefeed_processed_image.py  
   │  │  __init__.py  
   │  
   ├───templates  
   │  └───object_detection  
   │          add_image_feed.html  
   │          base_generic.html  
   │          dashboard.html  
   │          home.html  
   │          login.html  
   │          register.html  
  
