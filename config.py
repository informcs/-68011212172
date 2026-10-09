import os

# ==========================================================
# การตั้งค่าเชื่อมต่อฐานข้อมูล (Database Configuration)
# ตามข้อกำหนดการเดโมรอบที่ 1: "website ต้อง connect local database"
# ==========================================================

# สลับโหมดการเชื่อมต่อ: True = Localhost (ตามเกณฑ์เดโม), False = Server มหาวิทยาลัย
USE_LOCAL_DB = True

if USE_LOCAL_DB:
    # 1. เชื่อมต่อ Local Database (XAMPP / MAMP / MySQL Native บนเครื่อง)
    DB_HOST = os.environ.get("DB_HOST", "127.0.0.1")
    DB_PORT = int(os.environ.get("DB_PORT", 3306))
    DB_USER = os.environ.get("DB_USER", "root")
    DB_PASSWORD = os.environ.get("DB_PASSWORD", "67676767")  # ค่าเริ่มต้น XAMPP รหัสผ่าน root คือค่าว่าง ""
    DB_NAME = os.environ.get("DB_NAME", "online_course_db")
else:
    # 2. เชื่อมต่อ Server ของมหาวิทยาลัย
    DB_HOST = os.environ.get("DB_HOST", "202.28.34.202")
    DB_PORT = int(os.environ.get("DB_PORT", 3306))
    DB_USER = os.environ.get("DB_USER", "s68011212172")
    DB_PASSWORD = os.environ.get("DB_PASSWORD", "s68011212172pwd")
    DB_NAME = os.environ.get("DB_NAME", "prymania_s68011212172")

# Secret key สำหรับ Flask Session / Flash messages
SECRET_KEY = os.environ.get("SECRET_KEY", "online-course-secret-key-2026")
