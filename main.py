import sqlite3
from bottle import route, get, run, template, request, redirect

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
def new_item_form():
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
        return redirect('/todo')


@get('/edit/<no:int>')
def edit_item_form(no):
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("SELECT task FROM todo WHERE id = ?", (no,))
    cur_data = c.fetchone()
    return template('edit_task', old=cur_data, no=no)


if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True, reloader=True)
