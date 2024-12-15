
# Flask Data Management App

This is a simple Flask application built for managing data through a web interface.

## Features:
- User login system
- Protected pages
- Data visualization

## Setup Instructions:
1. Clone this repository.
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run the app locally:
   ```
   python eksamen_3.py
   ```

## Deployment Instructions:
1. Connect this repository to [Render](https://render.com).
2. Use these deployment settings:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn eksamen_3:app`
