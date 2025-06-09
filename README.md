# employee-management3
# Система управления персоналом ILINE GROUP

## Описание
Веб-приложение для управления сотрудниками компании с возможностью:
- Просмотра списка сотрудников
- Поиска по ФИО
- Изменения руководителя

## Технологии
- Python 3.10+
- Flask 2.3
- MySQL/MariaDB
- SQLAlchemy

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
DATABASE_URL=mysql+pymysql://user:password@localhost/employee_db
SECRET_KEY=your-secret-key
```

4. Запустить приложение:
```bash
flask run
```
