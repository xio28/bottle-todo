<!DOCTYPE html>
<html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Mostrar tabla</title>
        <!-- <link rel="stylesheet" href="styles.css"> -->
    </head>
    <body>
        %#template to generate a HTML table from a list of tuples (or list of lists, or tuple of tuples or ...)
        <p>Las tareas pendientes son las siguientes:</p>
        <table border="1" style="border-collapse: collapse;">
            <tr>
                <th>Id</th>
                <th>Tarea</th>
                <th>Estado</th>
            </tr>
            %for row in rows:
                <tr>
                %for i in range(len(row)):
                    %if i == 2:
                        %if row[i] == 0:
                            <td style="padding: 1em;">Cerrada</td>
                        %else:
                            <td style="padding: 1em;">Abierta</td>
                        %end
                    %else:
                    <td style="padding: 1em;">{{row[i]}}</td>
                    %end
                %end
                </tr>
            %end
        </table>
    </body>
</html>
