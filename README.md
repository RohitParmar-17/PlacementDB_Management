# Placement System Database

## Introduction
The Placement System Database is a database management system designed to streamline the process of managing placement-related information for educational institutions, companies, and students. It facilitates the storage, retrieval, and manipulation of data related to job placements, internships, and recruitment activities.

## Screenshots
Here are some screenshots of the TextUtils React application:

<img src="https://github.com/RohitParmar-17/Text-Utils-React/blob/master/screenshots/textutil1.png" alt="Home Page" width="100%">

<img src="https://github.com/RohitParmar-17/Text-Utils-React/blob/master/screenshots/textutil2.png" alt="Dark Mode" width="100%">

## Features
- **Student Management**: Store and manage student details, resumes, and placement status.
- **Company Management**: Maintain records of recruiting companies, job openings, and requirements.
- **Placement Records**: Track job offers, interview schedules, and hiring statistics.
- **Internship Tracking**: Record internship opportunities and student applications.
- **Admin Dashboard**: Secure and intuitive interface for administrators to manage the system.

## Tech Stack
- **Backend**: Python (Flask/Django)
- **Database**: MySQL
- **Frontend**: HTML, CSS, JavaScript (Optional, if a web interface is included)

## Installation
### Prerequisites
Ensure you have the following installed on your system:
- Python (v3.x)
- MySQL Server
- Required Python libraries (Flask/Django, MySQL Connector, Pandas, etc.)

### Steps to Setup Locally
1. **Clone the Repository**
   ```sh
   git clone https://github.com/RohitParmar-17/PlacementDB_Management.git
   cd PlacementDB_Management
   ```

2. **Create Virtual Environment (Optional but Recommended)**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**
   ```sh
   pip install -r requirements.txt
   ```

4. **Set Up MySQL Database**
   - Create a new database in MySQL:
     ```sql
     CREATE DATABASE db_proj1;
     ```
   - Configure database credentials in `config.py` or `.env` file.

5. **Run Database Migrations (If using Django)**
   ```sh
   python manage.py migrate
   ```

6. **Start the Application**
   - If using Flask:
     ```sh
     python login.py
     ```
   - If using Django:
     ```sh
     python manage.py runserver
     ```

   The application will be available at `http://localhost:5000/` (Flask) or `http://127.0.0.1:8000/` (Django).

## Deployment
To deploy the project:
1. **Set Up a Production Database** (MySQL Server on cloud/local server).
2. **Use a Production Server** (Gunicorn, Apache, Nginx with WSGI for Flask/Django).
3. **Deploy on Cloud Platforms** like AWS, Heroku, DigitalOcean, or shared hosting.

## Contributing
If you’d like to contribute:
- Fork the repository
- Create a new branch (`git checkout -b feature-branch`)
- Make your changes and commit (`git commit -m "Added new feature"`)
- Push to the branch (`git push origin feature-branch`)
- Open a pull request

## Contact
For any issues or suggestions, feel free to reach out:
- **Email**: rohitghost5050@gmail.com

