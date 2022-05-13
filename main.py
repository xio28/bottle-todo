import sqlite3
from bottle import route, run, template, static_file

@route('/todo')
def todo_list():
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("SELECT * FROM todo")
    result = c.fetchall()
    c.close()
    output = template('make_table', rows=result)
    return output

if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True, reloader=True)
