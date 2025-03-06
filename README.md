# Event-Management

# Download Source Code
# 1. Create a Virtual Environment(if not created ,so we alread created)
       # python -m venv venv

# 2. activate a Virtual Environment 
      # >.\venv\Scripts\activate  (in cmd)

# 3. Install all Packages using requirements.txt file
      # pip install -r requirements.txt

# 4. Run the Makemigrations and Migrate commond.
      # python manage.py makemigrations
      # python manage.py migrate
      
# 5. Create a Superuser.
      # python manage.py createsuperuser

# 6. Run the server with localhost.
      # # python manage.py runserver

# 7. Endpoints.

    # your API is available at:

    // GET /api/organizer_details/ – List organizer

    // GET /api/events/ – List events
    // POST /api/events/ – Create an event
    // GET /api/events/{id}/ – Retrieve an event
    // PUT /api/events/{id}/ – Update an event

    // GET /api/venues/ – List venues
    // POST /api/venues/ – Create an venues
    // GET /api/venues/{id}/ – Retrieve an venues
    // PUT /api/venues/{id}/ – Update an venues     participants/


    // GET /api/participants/ – List participants
    // POST /api/participants/ – Create an participants
    // GET /api/participants/{id}/ – Retrieve an participants
    // PUT /api/participants/{id}/ – Update an participants

    
