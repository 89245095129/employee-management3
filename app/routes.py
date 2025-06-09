from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models import Employee, Position
from app import db

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    sort = request.args.get('sort', 'id')
    order = request.args.get('order', 'asc')
    search_query = request.args.get('q', '')
    
    query = Employee.query
    
    if search_query:
        query = query.filter(
            (Employee.first_name.ilike(f'%{search_query}%')) | 
            (Employee.last_name.ilike(f'%{search_query}%'))
        )
    
    if order == 'asc':
        query = query.order_by(getattr(Employee, sort).asc())
    else:
        query = query.order_by(getattr(Employee, sort).desc())
    
    employees = query.all()
    return render_template('employees.html', employees=employees)

@bp.route('/update_manager/<int:employee_id>', methods=['POST'])
def update_manager(employee_id):
    employee = Employee.query.get_or_404(employee_id)
    new_manager_id = request.form.get('manager_id')
    
    if new_manager_id:
        if int(new_manager_id) == employee.id:
            flash('Сотрудник не может быть своим руководителем', 'danger')
        else:
            employee.manager_id = new_manager_id
            db.session.commit()
            flash('Руководитель успешно обновлен', 'success')
    
    return redirect(url_for('main.index'))

