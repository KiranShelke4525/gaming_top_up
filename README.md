# Gaming Top-Up Management System (Django Project)

This project is a Django-based backend system that simulates a gaming top-up platform. It includes admin panel management, a REST API, an HTML form for top-up orders, and a staff-only analytics dashboard.

---

## 🛠️ Step-by-Step Instructions to Run the Project

### 1. Clone the Project

```bash
git clone https://github.com/your-username/gaming-topup-project.git
cd gaming-topup-project

2. set up virtual env
python -m venv env
env\Scripts\activate

3. Install All Dependencies
pip install -r requirements.txt

 

## Database conection 

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'Pubg_game',
        'USER': 'root',         
        'PASSWORD': 'Kiran@4525', 
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

### this is my local machine DB PLEASE DO SETTING OF YOUR DB ###


4. Apply Migrations
python manage.py makemigrations
python manage.py migrate 

5. Create Superuser for Admin Login 
python manage.py createsuperuser
1 And add game and Top up products from admin side 

How to Add Game & Product in Django Admin
Step-by-Step:
Go to: http://127.0.0.1:8000/admin/

Log in using the superuser you just created

Click on "Games" → "Add"

Name: PUBG Mobile

Game ID: pubg123

Is active: 

Click Save

Then click on "TopUp Products" → "Add"

Game: Select PUBG Mobile

Name: UC Pack 500

Price: 399

In-game currency: 500 UC

Click Save




