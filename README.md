# 🇨🇳 ICTS Consulting — Chinese Language Learning Platform

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)

> A professional full-stack web platform for learning the Chinese language — featuring structured courses, testimonials, and an intuitive user experience.

---

##  Live Features

-  **Home** — Hero section with highlights
-  **Courses** — Browse available Chinese language courses
-  **About** — Institution background and mission
-  **Testimonials** — Student reviews and feedback
-  **Contact** — Get in touch form

---

##  Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python, Django |
| Frontend | HTML5, CSS3, JavaScript |
| Styling | Bootstrap |
| Database | SQLite3 |
| Media | Django Media Files |

---

##  Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/Shanum-959/ICTS-Consulting.git
cd ICTS-Consulting
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Apply Migrations
```bash
python manage.py migrate
```

### 4. Run Development Server
```bash
python manage.py runserver
```

### 5. Open in Browser
 http://127.0.0.1:8000/

 ---

## 📁 Project Structure

```
chinese_website/
│
├── manage.py
├── requirements.txt
├── .gitignore
│
├── chinese_website/          # Project configuration
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── main/                     # Main application
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   │
│   ├── migrations/
│   │   └── 0001_initial.py
│   │
│   ├── static/main/
│   │   ├── css/
│   │   │   ├── style.css
│   │   │   ├── home.css
│   │   │   ├── about.css
│   │   │   ├── courses.css
│   │   │   ├── contact.css
│   │   │   ├── footer.css
│   │   │   └── bootstrap.min.css
│   │   │
│   │   └── images/
│   │       ├── logo1.jpeg
│   │       ├── logo2.jpeg
│   │       ├── h1.jpg
│   │       └── hero.jpg
│   │
│   └── templates/main/
│       ├── base.html
│       ├── home.html
│       ├── about.html
│       ├── courses.html
│       ├── course_detail.html
│       └── contact.html
│
└── media/                    # Uploaded content (via Django Admin)
    ├── about/
    ├── courses/
    ├── features/
    ├── testimonials/
    └── videos/
```

##  Developer

<table>
  <tr>
    <td align="center">
      <b>Shanum</b><br/>
      <a href="https://github.com/Shanum-959">GitHub Profile</a>
    </td>
  </tr>
</table>

---

##  License

This project is for educational purposes under **ICTS Consulting**.

---

<p align="center"> Shanum — ICTS Consulting</p>
