<!DOCTYPE html>
<html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Mostrar tabla</title>
    </head>
    <body>
        %#template to generate a HTML table from a list of tuples (or list of lists, or tuple of tuples or ...)
        <p>Las tareas pendientes son las siguientes:</p>
        <table border="1" style="border-collapse: collapse">
            %for row in rows:
            <tr>
            %for col in row:
                <td style="padding: 1em;">{{col}}</td>
            %end
            </tr>
            %end
        </table>
    </body>
</html>
