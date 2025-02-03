
## **Multilingual FAQ API**
### **Overview**
This project is a backend application built with Django to manage multilingual Frequently Asked Questions (FAQs). It provides a REST API to fetch, create, and manage FAQs in multiple languages. It also integrates a WYSIWYG editor for rich-text answers, utilizes Redis for caching, and supports Google Translate API for automatic translations.

### **Features**
- Multilingual FAQ storage with dynamic language selection.
- Rich text editor (WYSIWYG) for formatting answers.
- REST API with query parameter support for language selection.
- Caching with Redis for better performance.
- Automatic translation using Google Translate API.
- Admin panel to manage FAQs effortlessly.
- Unit tests to ensure API reliability and model correctness.
- Docker support for easy deployment.

### **Tech Stack**
- **Backend:** Django, Django REST Framework
- **Database:** PostgreSQL
- **Caching:** Redis
- **WYSIWYG Editor:** django-ckeditor
- **Translation:** googletrans (Google Translate API)
- **Testing:** pytest
- **Containerization:** Docker, Docker Compose

### **Installation**

#### **Prerequisites**
- Python 3.9+
- PostgreSQL
- Redis
- Docker (optional)

#### **Steps to Set Up the Project:**

1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/multilingual-faq-api
   cd multilingual-faq-api/faq_project
   ```

2. **Create a virtual environment and activate it:**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Configure environment variables:**
   - Create a `.env` file in the project root and add the following:
     ```env
     SECRET_KEY=your_secret_key
     DEBUG=True
     DATABASE_URL=postgres://user:password@localhost:5432/dbname
     REDIS_URL=redis://localhost:6379/0
     GOOGLE_TRANSLATE_API_KEY=your_api_key
     ```

5. **Apply database migrations:**
   ```sh
   python manage.py migrate
   ```

6. **Create a superuser for the admin panel:**
   ```sh
   python manage.py createsuperuser
   ```

7. **Run the development server:**
   ```sh
   python manage.py runserver
   ```

#### **API Endpoints**
- **Fetch all FAQs (default language: English)**  
  `GET /api/faqs/`
  
- **Fetch FAQs in Hindi**  
  `GET /api/faqs/?lang=hi`
  
- **Fetch FAQs in Bengali**  
  `GET /api/faqs/?lang=bn`

- **Create a new FAQ (Admin required)**  
  `POST /api/faqs/`  
  **Content-Type:** application/json  
  Example body:
  ```json
  {
    "question": "What is Django?",
    "answer": "Django is a high-level Python Web framework."
  }
  ```

#### **Admin Panel**
Access the admin panel at:
- **http://localhost:8000/admin/**
- Login using the superuser credentials created earlier.

#### **Running Tests**
To run the tests, use pytest:
```sh
pytest
```

#### **Docker Setup (Optional)**
To set up the application using Docker, follow these steps:

1. **Build and start the containers:**
   ```sh
   docker-compose up --build
   ```

2. **Access the application at:**  
   - `http://localhost:8000`

#### **Git Best Practices**
- **Follow conventional commits:**
  - `feat: Add multilingual FAQ model`
  - `fix: Improve translation caching`
  - `docs: Update README with API examples`

- **Use meaningful commit messages.**
- **Push changes to a feature branch and merge via pull requests.**

#### **Deployment (Optional)**
You can deploy the application to **Heroku** or **AWS** using Docker and environment variables for configuration.

#### **Contribution Guidelines**
1. Fork the repository.
2. Create a feature branch:
   ```sh
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```sh
   git commit -m "feat: Add new feature"
   ```
4. Push to your feature branch:
   ```sh
   git push origin feature-name
   ```
5. Open a Pull Request.


---

#### **Contact**
For any queries or issues, open an issue in the repository or contact the maintainer directly.

---

This structure will provide a clean, organized way for users to set up, contribute to, and deploy your multilingual FAQ API project!
