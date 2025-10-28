# ▷ вивести інформацію про всі навчальні групи,
 # ▷ вивести інформацію про конкретного викладача,
 # ▷ вивести назви груп, що належать до конкретного факультету,
 # ▷ вивести назви предметів, які викладає конкретний викладач


from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text

import json




with open('credentials.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    login = data['login']
    password = data['password']

DATABASE_URL = f'postgresql+psycopg2://{login}:{password}@localhost/academy'


engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()
metadata = MetaData()
metadata.reflect(bind=engine)


# ▷ 1. Вивести інформацію про всі навчальні групи
query_all_groups = text("""
    SELECT g.id, g.name, g.year, d.name AS department_name
    FROM groups g
    JOIN departments d ON g.departmentid = d.id
    ORDER BY g.id;
""")

# ▷ 2. Вивести інформацію про конкретного викладача
query_teacher_info = text("""
    SELECT id, name, surname, salary
    FROM teachers
    WHERE id = :teacher_id;
""")

# ▷ 3. Вивести назви груп, що належать до конкретного факультету
query_groups_by_faculty = text("""
    SELECT g.name AS group_name
    FROM groups g
    JOIN departments d ON g.departmentid = d.id
    JOIN faculties f ON d.facultyid = f.id
    WHERE f.id = :faculty_id;
""")

# ▷ 4. Вивести назви предметів, які викладає конкретний викладач
query_subjects_by_teacher = text("""
    SELECT DISTINCT s.name AS subject_name
    FROM subjects s
    JOIN lectures l ON s.id = l.subjectid
    JOIN teachers t ON l.teacherid = t.id
    WHERE t.id = :teacher_id;
""")

# === 4.  ВИКОНАННЯ ЗАПИТІВ ===

print("\n=== 1. Усі навчальні групи ===")
groups = session.execute(query_all_groups).fetchall()
for g in groups:
    print(f"ID: {g.id}, Назва: {g.name}, Рік: {g.year}, Кафедра: {g.department_name}")

print("\n=== 2. Інформація про викладача (ID = 1) ===")
teacher = session.execute(query_teacher_info, {'teacher_id': 1}).fetchone()
if teacher:
    print(f"ID: {teacher.id}, Ім'я: {teacher.name}, Прізвище: {teacher.surname}, Зарплата: {teacher.salary}")
else:
    print("Викладача з таким ID не знайдено.")

print("\n=== 3. Групи певного факультету (ID факультету = 1) ===")
faculty_groups = session.execute(query_groups_by_faculty, {'faculty_id': 1}).fetchall()
for g in faculty_groups:
    print(f"- {g.group_name}")

print("\n=== 4. Предмети, які викладає певний викладач (ID = 1) ===")
teacher_subjects = session.execute(query_subjects_by_teacher, {'teacher_id': 1}).fetchall()
for s in teacher_subjects:
    print(f"- {s.subject_name}")
