# employee-management3
# Система управления персоналом ILINE GROUP

## Описание
Веб-приложение для управления сотрудниками компании с возможностью:
- Просмотра списка сотрудников
- Поиска по ФИО
- Изменения руководителя

## Технологии
Flask==2.3.2
Flask-SQLAlchemy==3.0.3
Flask-Migrate==4.0.4
psycopg2-binary==2.9.6
python-dotenv==1.0.0


## Установка
1. Клонировать репозиторий:
```bash
git clone https://github.com/ваш-логин/employee-management-system.git
```

2. Установить зависимости:
```bash
pip install -r requirements.txt
```

3. Настроить базу данных в `.env`:
```ini
DATABASE_URI = 'postgresql://postgres:user:password@localhost:employee_db'
SECRET_KEY=your-secret-key
```

4. Запустить приложение:
```bash
flask run
```
