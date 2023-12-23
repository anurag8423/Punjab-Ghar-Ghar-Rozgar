# Punjab-Ghar-Ghar-Rozgar
Our live Django project for Punjab's Ministry of Employment and Innovation includes a user-friendly chatbot, translation into 133 languages, and a resume generator. The platform ensures security with automatic face verification login. It aligns with the Ministry's goals, providing an accessible, secure, and innovative solution.

Certainly! Below is a step-by-step execution process for your Django-based project using a GitHub repository with a `requirements.txt` file:

1. ## Clone the Repository:
   ### git clone https://github.com/anurag8423/Punjab-Ghar-Ghar-Rozgar.git
   ### cd <repository_directory>

2. ## Create a Virtual Environment:
   ### python3 -m venv virtual

3. ## Activate the Virtual Environment:
   - On Windows:
     ### virtual\Scripts\activate
     
   - On macOS/Linux:
     ### source virtual/bin/activate

4. ## Install Dependencies:
   ### pip install -r requirements.txt

5. ## Apply Database Migrations:
   ### python manage.py migrate


6. ## Create Superuser (if needed):
   ### python manage.py createsuperuser

7. ## Run the Development Server:
   ### python manage.py runserver

8. ## Access the Application:
   Open a web browser and go to `http://127.0.0.1:8000/` to view the application.

9. ## Access the Admin Panel:
   If you created a superuser, you can access the admin panel at `http://127.0.0.1:8000/admin/` and log in using the superuser credentials.

10. ## Deactivate the Virtual Environment:
    When you're done working on the project, deactivate the virtual environment.
    ### deactivate
