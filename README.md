# Real-Time System Health Monitor & Notifier

A robust Django-based web application designed to monitor real-time system resource metrics (CPU, RAM, Disk usage), log system performance history into a database, and send instant notification alerts via Slack Webhooks during high load conditions.

## 🚀 Features
- **Real-Time Resource Monitoring:** Fetches live CPU, RAM, and Disk metrics using `psutil`.
- **Database Logging:** Automatically records health status in an SQLite database using Django ORM (`SystemHealthLog`).
- **Interactive Dashboard:** Auto-refreshing frontend dashboard built with HTML, Bootstrap, and JavaScript AJAX/Fetch API.
- **Admin Panel Integration:** Fully customized Django Admin interface to review performance log history.
- **Alert Notifications:** Integrated with Slack Webhooks to trigger instant alerts when system metrics cross threshold limits.

## 🛠️ Tech Stack
- **Backend:** Python, Django
- **Database:** SQLite
- **Frontend:** HTML5, CSS3, Bootstrap 5, JavaScript (Fetch API)
- **Libraries & APIs:** `psutil`, Slack Webhook API

## ⚙️ How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/holkargopal160-cmyk/Automsted-Sysytem-Health-Slack-Notifier-Project.git](https://github.com/holkargopal160-cmyk/Automsted-Sysytem-Health-Slack-Notifier-Project.git)
   cd Automsted-Sysytem-Health-Slack-Notifier-Project

   ## set up virtual enviroment.
   python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

## install dependancies
pip install django psutil requests

##apply database migrations.
## python manage.py makemigrations
python manage.py migrate

## create a superuser (for admin access)
python manage.py createsuperuser

## run the server
python manage.py runserver

## open http://127.0.0.1:8000/in browser


   
