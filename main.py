import sqlite3
from bottle import route, get, post, run, template, request, redirect


@get('/')
def get_index_tpl():
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("SELECT * FROM todo")
    result = c.fetchall()
    c.close()
    output = template('index', rows=result)
    return output


@route('/todo')
def todo_list():
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("SELECT * FROM todo")
    result = c.fetchall()
    c.close()
    output = template('make_table', rows=result)
    return output


@route('/new')
def new_todo_form():
    return template('new_task')


@route('/new', method='POST')
def new_todo_save():
    if request.POST.save:  # the user clicked the `save` button
        new = request.POST.task.strip()    # get the task from the form
        conn = sqlite3.connect('todo.db')
        c = conn.cursor()

        c.execute("INSERT INTO todo (task,status) VALUES (?,?)", (new,1))
        new_id = c.lastrowid

        conn.commit()
        c.close()
        # se muestra el resultado de la operación
    return redirect('/')


@get('/edit/<no:int>')
def edit_todo_form(no):
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("SELECT task FROM todo WHERE id = ?", str(no))
    cur_data = c.fetchone()
    return template('edit_task', old=cur_data, no=no)


@post('/edit/<no:int>')
def edit_todo(no):
    if request.POST.save:
        edit = request.POST.task.strip()
        status = request.POST.status.strip()

        if status == 'pendiente':
            status = 1
        else:
            status = 0

        conn = sqlite3.connect('todo.db')
        c = conn.cursor()
        c.execute("UPDATE todo SET task = ?, status = ? WHERE id LIKE ?", (edit, status, no))
        conn.commit()

        return redirect('/edit/<no:int>')


@get('/delete/<no:int>')
def delete_todo_form(no):
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("SELECT task FROM todo WHERE id LIKE ?", (str(no),))
    cur_data = c.fetchone()

    return template('delete_task', old=cur_data, no=no)


@post('/delete/<no:int>')
def delete_todo(no):
    if request.POST.delete:
        conn = sqlite3.connect('todo.db')
        c = conn.cursor()
        c.execute("DELETE FROM todo WHERE id LIKE ?", str(no))
        conn.commit()
        c.close()

    return redirect('/todo')


if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True, reloader=True)
