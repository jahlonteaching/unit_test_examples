# Ejemplos de pruebas unitarias

## 1. Factorial
Supón que tienes una función `factorial(n)` que calcula el factorial de un
número entero `n`.

## 2. String invertido
Supongamos que tenemos una función llamada reverse_string que toma una cadena de 
caracteres como entrada y devuelve la cadena invertida. Por ejemplo, si se ingresa 
la cadena "Hola Mundo", la función debe devolver "odnuM aloH".

## 3. Elementos comunes
Supongamos que tenemos una función llamada find_common_elements que toma dos listas
como entrada y devuelve una lista que contiene los elementos comunes entre las dos
listas. Por ejemplo, si se ingresa la lista [1, 2, 3, 4, 5] y la lista [3, 4, 5, 6, 7],
la función debe devolver la lista [3, 4, 5].

## 4. Calculadora
Tienes una clase `Calculator` que tiene cuatro métodos: `add(a, b)`, `subtract(a, b)`,
`multiply(a, b)` y `divide(a, b)`

## 5. Aplicación de banco
Supón que tienes una aplicación simple de un banco que tiene tres clases: 
`Account`, `Transaction` y `Bank`. 

`Account` representa una cuenta de banco con un balance y un número de cuenta.
`Transaction` representa una transacción entre dos cuentas, y `Bank` representa un
banco con una lista de cuentas y la capacidad de realizar transacciones entre cuentas.

## 6. Aplicación de ecommerce
Supongamos que tenemos un sitio web de comercio electrónico que tiene un diseño de clases que 
representa productos, clientes, pedidos y pagos. La implementación de esta diseño incluye cuatro 
clases principales: `Product`, `Customer`, `Order` y `Payment`.

La clase `Product` representa un producto en el sitio web y tiene atributos como el nombre
del producto, el precio y el stock disponible. También tiene un método `purchase` que permite
a los clientes comprar el producto y reduce el stock disponible en consecuencia.

La clase `Customer` representa a un cliente en el sitio web y tiene atributos como el nombre 
del cliente, la dirección de correo electrónico y un carrito de compras que contiene una lista 
de productos y cantidades que el cliente ha agregado al carrito. La clase también tiene métodos 
para agregar y eliminar productos del carrito y para procesar una compra, que crea un nuevo 
objeto `Order` y vacía el carrito de compras.

La clase `Order` representa un pedido de un cliente y contiene información sobre los productos 
que se compraron, las cantidades y el costo total. La clase también verifica si hay suficiente 
stock disponible para cada producto antes de crear el pedido.

Finalmente, la clase `Payment` representa un pago por un pedido y tiene atributos como el objeto 
`Order` al que se refiere el pago y la cantidad pagada. La clase también tiene un método 
`process` que verifica si la cantidad pagada es igual al costo total del pedido y, si es así, 
completa el pago.