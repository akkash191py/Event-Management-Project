# Event-Management

# Download Source Code
# 1. Create a Virtual Environment(if not created ,so we alread created)
       # python -m venv venv

# 2. activate a Virtual Environment 
      # >.\venv\Scripts\activate  (in cmd)

# 3. Install all Packages using requirements.txt file
      # pip install -r requirements.txt
      
# 4. Setup the Database (MySQL) at settings.py.

              DATABASES = {
                  'default': {
                      'ENGINE': 'django.db.backends.mysql',
                      'NAME': 'eventmangdb',
                      'USER': 'root',
                      'PASSWORD': '',
                      'HOST': 'localhost',
                      'PORT': '3306',
                  }
              }

# 5. Setup the Email at settings.py for send a Email.

              EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
              EMAIL_HOST = 'smtp.gmail.com'
              EMAIL_PORT = 587
              EMAIL_HOST_USER = 'example@gmail.com'
              EMAIL_HOST_PASSWORD = 'xbpyehcambtqlauv'
              EMAIL_USE_TLS = True


# 6. Setup the SIMPLE_JWT and django-filters at settings.py.

              # Setup the SIMPLE_JWT for Token Authentication
              
              SIMPLE_JWT = {
              'ACCESS_TOKEN_LIFETIME': timedelta(days=180),
              'REFRESH_TOKEN_LIFETIME': timedelta(days=180),

              'AUTH_HEADER_TYPES': ('Bearer',),
              'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
              'USER_ID_FIELD': 'id',
              'USER_ID_CLAIM': 'user_id',
              'USER_AUTHENTICATION_RULE': 'rest_framework_simplejwt.authentication.default_user_authentication_rule',
              
              'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
              'TOKEN_TYPE_CLAIM': 'token_type',
              'TOKEN_USER_CLASS': 'rest_framework_simplejwt.models.TokenUser',
              
              'JTI_CLAIM': 'jti',

              }

       # Setup the django-filters for Filter data.

              REST_FRAMEWORK = {
                     'DEFAULT_AUTHENTICATION_CLASSES': [
                            'rest_framework_simplejwt.authentication.JWTAuthentication',
                            ],
                     'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
       }
       
# 7. Run the Makemigrations and Migrate commond.
      # python manage.py makemigrations
      # python manage.py migrate
      
# 5. Create a Superuser.
      # python manage.py createsuperuser

      # Create Super User with email and passord
      ex . email : example@gmail.com
           password: example@1245

# 6. Run the server with localhost.
      # # python manage.py runserver

# 7. Endpoints.

    # your API is available at:



    1. // POST http://127.0.0.1:8000/api/register/         ----  Register Form

           {
              "email" : "examle@gmail.com",              # email is Required for send a passord to email
              "mobile" : "+919422060358",
              "first_name" : "First",
              "last_name" : "Last",
              "role" : "admin",      # Role:  admin, user -----Options
              "gender" : "Female"    # Gender: Male, Female, Transgender     ---------Options
         }
       # Note : if user role is Admin the Automatically save data as Organizer and if role is user then save as Participants

   2.  // POST   http://127.0.0.1:8000/api/login/      # Login for Access Key and Refresh Key

              {
                  "email": "example@gmail.com",
                  "password" : "example@3952"
              }

              
  3.  // POST http://127.0.0.1:8000/api/user/change-password/     ----- For Change the Password with Access Key

            [Postman]
            Headers: Key : Authorization
                     Value: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzU3MjM3Nzk2LCJpYXQiOj

             {
               "old_password": "AkashR@8335",
               "new_password": "Akash@9099"
            }

 4.  // POST http://127.0.0.1:8000/api/user/forgot-password/       ---- User Fogot Password using email field and Password send to user email

           {
              "email": "akashpanchal07@gmail.com"
          }
          
5 . // GET http://127.0.0.1:8000/api/organizer_details/ – List organizer
       
6. // GET http://127.0.0.1:8000/api/events/ – List events
     
        [Postman]
        Headers: Key : Authorization
                 Value: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzU3MjM3Nzk2LCJpYXQiOj
     
7.   // GET http://127.0.0.1:8000/api/events/?name=name         – # Fiter data from event list passing query parameters in the URL
     
8.  // POST http://127.0.0.1:8000/api/events/ – Create an event

     [Postman]
     Headers: Key : Authorization
              Value: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzU3MjM3Nzk2LCJpYXQiOj
                     
9.  // GET http://127.0.0.1:8000/api/events/{id}/ – Retrieve an event

           [Postman]
            Headers: Key : Authorization
              Value: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzU3MjM3Nzk2LCJpYXQiOj
              
10.  // PUT http://127.0.0.1:8000/api/events/{id}/ – Update an event

           [Postman]
           Headers: Key : Authorization
                    Value: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzU3MjM3Nzk2LCJpYXQiOj

11.  // GET http://127.0.0.1:8000/api/venues/ – List venues

      
12.  // POST http://127.0.0.1:8000/api/venues/ – Create an venues

13.  // GET http://127.0.0.1:8000/api/venues/{id}/ – Retrieve an venues
     
14.  // PUT /api/venues/{id}/ – Update an venues     
      
       
15.  // GET http://127.0.0.1:8000/api/participants/ – List participants

           [Postman]
           Headers: Key : Authorization
                    Value: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzU3MjM3Nzk2LCJpYXQiOj
        
    
16.  // GET http://127.0.0.1:8000/api/participants/?email=email&first_name=first_name&last_name=last_name       # Fiter data from list passing query parameters in the URL
           
17.  // GET http://127.0.0.1:8000/api/participants/{id}/ – Retrieve an participants

          [Postman]
          Headers: Key : Authorization
                   Value: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzU3MjM3Nzk2LCJpYXQiOj
                
 18.  // PUThttp://127.0.0.1:8000 /api/participants/{id}/ – Update an participants
       
          [Postman]
          Headers: Key : Authorization
                   Value: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzU3MjM3Nzk2LCJpYXQiOj
    

    
