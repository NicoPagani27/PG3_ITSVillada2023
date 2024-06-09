Descripcion de la API: JSONPlaceholder es una API gratis que nos da datos ficticios en formato JSON para hacer pruebas y desarrollar aplicaciones. Este mismo tiene endpoints que devuelven datos simulados de usuarios, publicaciones, comentarios, álbumes de fotos, entre otros, permitiendo a las personas realizar solicitudes HTTP y tener respuestas JSON  para simular la interacción con una API real. Es útil para probar aplicaciones, prototipos o realizar pruebas de integración sin necesidad de crear una API propia o utilizar datos sensibles.

1. La api que seleccione es: https://jsonplaceholder.typicode.com

2. No encontre ninguna api que me permitiera hacer GET, PUT y POST al mismo tiempo. Solo econtre esta pero no tiene autenticacion

3. 
a. consulta GET genérica para obtener datos de la API: Listar todos los post que hay en la api
GET https://jsonplaceholder.typicode.com/posts/ (Ver resultado en: Imagen3a.png)

b1. consulta POST: Quiero agregar un posteo nuevo
POST https://jsonplaceholder.typicode.com/posts 
Body en JSON
{
  "title": "Como hacer un pancho",
  "body": "Solo necesitas 3 ingredientes: una salchicha un pan y un rico aderezo ",
  "userId": 1
}
(Ver resultado en: Imagen3b1.png)

b2. consulta PUT: Modifico el Titulo del posteo 1
PUT https://jsonplaceholder.typicode.com/posts/1 
Body en JSON
{
  "title": "Como usar APIs"
}
(Ver resultado en: Imagen3b2.png)

c. Consulta GET de búsqueda utilizando parámetros de URL: Consultar todos los posteos que sean del usuario 2
GET https://jsonplaceholder.typicode.com/posts?userId=2
(Ver resultado en: Imagen3c.png)

d. Consulta de búsqueda utilizando al menos dos claves: Consultar dos parametros, el user y el title
GET https://jsonplaceholder.typicode.com/posts?userId=2&title=et ea vero quia laudantium autem
(Ver resultado en: Imagen3d.png)

e. Consulta de búsqueda lógica: No encontre ninguna forma de hacer consulta logica con esa api

4. Pruebas con ThunderClient
4.1 Prueba GET 
En esta prueba ejecuto 2 tests: igualo el JSON y compruebo con lo tipeado y pruebo el Contenido del body y señalo que solo funcione la prueba hasta el largo de 1000 bytes. (Ver resultado en Imagen4.1.png)
4.2 Prueba POST
En esta prueba ejecuto 3 tests: pruebo que la respuesta sea correcta(Codigo201), pruebo que el body de la respuesta sea correcta con un JSON de ejemplo y finalmente pruebo que el tiemp de respuesta sea menor a 5 segundos (5000ms). (Ver resultado en Imagen4.2.png)
4.3 Prueba PUT
En esta prueba ejecuto 4 tests: Pruebo que el tiempo de respuesta sea menos de 10 segundos(10000ms), y que el codigo de respuesta sea OK(200), y que no sea ni 403 ni 404 (Codigos de error). (Ver resultado en Imagen4.3.png)

5. Cree un programa python utilizando la libreria requests para obtener el json desde la API con el listado de posteos y luego utilice la libreria tabulate para convertir el json en una tabla para poder convertir por consola y finalmente utilice la libreria fpdf para convertir esa tabla en un PDF. (Ver codigo del programa en ProyectoPython.py y ver ejemplo de resultado en table.pdf)
