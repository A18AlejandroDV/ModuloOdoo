# Inmobiliaria
    Gestion de Pisos,Alquiler y Clientes de una inmobiliaria.

# Modelos
    Como modelos tendremos un único archivo .py en el que crearemos las 3 clases principales: Pisos, Alquiler y Clientes.

    La clase Pisos constará de fields data, además de un campo de selección de estado y un campo relacional Many2one

    La clase Alquiler constará de fields data, cabe destacar que tenemos dos campos de fecha, el de fecha de inicio, que tendrá como valor por defecto la fecha actual, y la fecha de fin, un campo calculado que devolverá la fecha dentro de 1 año.
    (Nota: para evitar la introducción de alquileres errones se ha incluído una restricción por el que la fecha de inicio del alquiler no pueda ser mayor que la fecha de fin de alquiler).

    De clase Clientes destacamos que hereda del la clase res.partner, para asi posibilitar introducir un cliente que ya ha sido almacenado en otro módulo.


# Vistas

    Este módulo consta de 3 vistas de nombre igual a las clases del modelo anteriormente especificado.
    Estas tendrán la misma estructura, es decir, constan de un botón de acción en la barra principal del modulo, además todas constan de un vista de formulario y una vista de lista
