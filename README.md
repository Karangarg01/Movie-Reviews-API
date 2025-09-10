# 🎬 Movies Review API  
A simple RESTful API built with **Django REST Framework (DRF)** that allows users to manage movies and reviews. Users can add movies, write reviews, check ratings, and fetch details — all through clean API endpoints.  

---

## 🚀 Features  
- Add new movies with title, genre, and release year.  
- Add reviews with reviewer name, rating, and comment.  
- Fetch all movies or a specific movie by ID.  
- Fetch reviews for a specific movie.  
- Prevent duplicate movies from being added.  
- Admin panel to manage movies and reviews.  

---

## 🛠️ Tech Stack  
- **Backend:** Django, Django REST Framework  
- **Database:** SQLite (default, can be changed)  
- **Tools:** Python, Git, GitHub  

---

## 📂 Project Structure  
``` bash
movies-review-api/
│── manage.py
│── requirements.txt
│── README.md
│── .gitignore
│
├── movies_review_api/ # Main project folder
│ ├── settings.py
│ ├── urls.py
│ └── ...
│
└── reviews/ # App folder
├── models.py
├── serializers.py
├── views.py
├── urls.py
├── admin.py
└── migrations/
```
---

## ⚙️ Installation  

1. **Clone the repository**  
```bash
git clone https://github.com/your-username/movies-review-api.git
cd movies-review-api
```
---

2. **Create and activate virtual environment**
``` bash
python -m venv venv
venv\Scripts\activate   # On Windows
source venv/bin/activate   # On Mac/Linux
```
---

3. Install dependencies
```bash
pip install -r requirements.txt
```
---

4. Apply migrations
``` bash
python manage.py migrate
```
---

5. Run the server
``` bash
python manage.py runserver
```
---

## 🔗 API Endpoints
**🎥 Movies**

- `GET /api/movies/`→ Get all movies
- `GET /api/movies/<id>/` → Get a specific movie
- `POST /api/movies/` → Add a new movie

**📝 Reviews**

- `GET /api/movies/<id>/reviews/` → Get reviews for a movie
- `POST /api/movies/<id>/reviews/` → Add a review for a movie
---

## 🔑 Admin Panel

1. **Create superuser:**
``` bash
python manage.py createsuperuser
```

2. Log in at → http://127.0.0.1:8000/admin/
