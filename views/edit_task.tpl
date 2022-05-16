<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Editar Tarea</title>
    </head>
    <body>
        <p>Editar la tarea número = {{no}}</p>
        <form action="/edit/{{no}}" method="POST">
            <input type="text" name="task" value="{{old[0]}}" size="75" maxlength="100">
            <select name="status">
                <option>pendiente</option>
                <option>cerrada</option>
            </select>
            <br>
            <input type="submit" name="save" value="save">
        </form>   
    </body>
</html>
