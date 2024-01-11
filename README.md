# Punjab-Ghar-Ghar-Rozgar
Our live Django project for Punjab's Ministry of Employment and Innovation includes a user-friendly chatbot, translation into 133 languages, and a resume generator. The platform ensures security with automatic face verification login. It aligns with the Ministry's goals, providing an accessible, secure, and innovative solution.

Certainly! Below is a step-by-step execution process for your Django-based project using a GitHub repository with a `requirements.txt` file:

1. ## Clone the Repository:
   ### git clone https://github.com/anurag8423/Punjab-Ghar-Ghar-Rozgar.git
   ### cd <repository_directory>

2. ## Create a Virtual Environment:
   ```bash
   python3 -m venv virtual

4. ## Activate the Virtual Environment:
   - On Windows:
     ```bash
     virtual\Scripts\activate
     
   - On macOS/Linux:
     ```bash
     virtual/bin/activate

5. ## Install Dependencies:
   ```bash
   pip install -r requirements.txt

7. ## Apply Database Migrations:
   ```bash
   python manage.py migrate

9. ## Create Superuser (if needed):
   ```bash
   python manage.py createsuperuser

11. ## Run the Development Server:
    ```bash
    python manage.py runserver

12. ## Access the Application:
    Open a web browser and go to `http://127.0.0.1:8000/` to view the application.

13. ## Access the Admin Panel:
    If you created a superuser, you can access the admin panel at `http://127.0.0.1:8000/admin/` and log in using the superuser credentials.

14. ## Deactivate the Virtual Environment:
    When you're done working on the project, deactivate the virtual environment.
    ```bash
    deactivate
