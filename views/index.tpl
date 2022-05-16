<!DOCTYPE html>
<html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
    </head>
    <body>
        <p>Añadir nueva tarea:</p>
        <form action="/new" method="POST">
            <input type="text" name="task" size="100" maxlength="100" />
            <input type="submit" name="save" value="Guardar" />
        </form>
        <p>Las tareas pendientes son las siguientes:</p>
        <table border="1" style="border-collapse: collapse;">
            <tr>
                <th>Id</th>
                <th>Tarea</th>
                <th>Estado</th>
                <th colspan="2">Acciones</th>
            </tr>
            %for row in rows:
            %print(row[0])
                <tr>
                    %for i in range(len(row)):
                        %if i == 2:
                            %if row[i] == 0:
                                <td style="padding: 1em;">Finalizada</td>
                            %else:
                                <td style="padding: 1em;">Pendiente</td>
                            %end
                        %else:
                        <td style="padding: 1em;">{{row[i]}}</td>
                        %end
                    %end
                    <form action="/edit/{{row[0]}}" method="POST">
                        <td style="padding: .5em;"><input type="submit" name="edit" value="Editar"/></td>
                    </form>
                    <form action="/delete/{{row[0]}}" method="POST">
                        <td style="padding: .5em;"><input type="submit" name="delete" value="Borrar"/></td>
                    </form>
                </tr>
            %end
        </table>
    </body>
</html>
