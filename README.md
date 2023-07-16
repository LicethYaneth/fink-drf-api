
# Prueba Tecnica  - Django Rest Framework



## API en Producción

La URL de la API en producción se encuentra en el siguiente enlace: https://fink-drf-api.onrender.com/api/. 
Para las solicitudes de autenticación: https://fink-drf-api.onrender.com/api/auth/
Esta URL es la dirección principal a la cual los usuarios pueden acceder para interactuar con la API y utilizar sus servicios. Asegúrate de utilizar esta URL para todas las solicitudes y pruebas de integración con la API en producción.


## Ejecución Localmente

Clone el proyecto

```bash
  git clone https://link-to-project
```

Ir al directorio del proyecto

```bash
  cd my-project
```
Generar entorno virtual de Python

```bash
  virtualenv venv
```

Activar entorno virtual

```bash
  source venv/bin/activate
```

Instalar las dependencias

```bash
  pip install -r requirements.txt
```

Start the server

```bash
  python manage.py runserver
```


## API 
### Endpoint 1
Se creo un endpoint para ordenar una matriz de números recibida de tal forma que los números ordenados queden al final de la lista
```http
POST /api/sorted-numbers/
```
##### Request
```json

{
    "sin_clasificar": [3,5,5,6,8,3,4,4,7,7,1,1,2]
}
```
##### Response
```json
{
    "sin clasificar": [3,5,5,6,8,3,4,4,7,7,1,1,2],
    "clasificado": [1,2,3,4,5,6,7,8,1,3,4,5,7]
}
```
### Endpoint 2
Se creo un endpoint para procesar los datos registrados en cuanto a ventas y gastos de cada mes y obtener el balance mensual. Una vez procesada la información los registros son almacenados en la base de datos asociado al usuario del vendedor que se encuentra logueado y a la sucursal a la que esta pertenece.

#### Post calculate monthly balance

```http
  POST /api/balance-montly/
```
##### Request

```json

{
    "Mes":["Enero", "Febrero", "Marzo", "Abril"],
    "Ventas":[30500, 35600, 28300, 33900],
    "Gastos":[22000, 23400, 18100, 20700]
}
```
##### Response
```json
{
    "anual_balance": [
        {
            "mes": "Enero",
            "Ventas": 30500,
            "Gastos": 22000,
            "Balance": 8500
        },
        {
            "mes": "Febrero",
            "Ventas": 35600,
            "Gastos": 23400,
            "Balance": 12200
        },
        {
            "mes": "Marzo",
            "Ventas": 28300,
            "Gastos": 18100,
            "Balance": 10200
        },
        {
            "mes": "Abril",
            "Ventas": 33900,
            "Gastos": 20700,
            "Balance": 13200
        }
    ]
}
```

### Endpoint 3

Se ha implementado un esquema de base de datos para el endpoint 3, utilizando la información del endpoint 2. Este esquema permite almacenar el balance mensual de cada sucursal. Cada vendedor de la sucursal está asociado a un usuario del sistema y es responsable de ingresar la información del balance correspondiente

![modelo_datos](https://github.com/LicethYaneth/fink-drf-api/assets/25712062/851672e8-0bbf-4be1-b4f7-a40ed62a772b)



#### Get Branche stores

```http
  GET /api/branch_stores
```


#### Get Branche store

```http
  GET /api/branch_stores/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of branch store to fetch |

#### Save Branch Store

```http
  POST /api/branch_stores
```


##### Request:
```json
{
  "name": "",
  "address": "",
}

```

#### Update Branch Store

```http
  PUT /api/branch_stores/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of branch store to update |

##### Request:
```json
{
  "name": "",
  "address": "",
}
```

#### Delete Branches

```http
  DELETE /api/branch_stores/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of branch store to delete |

#### Get Sellers

```http
  GET /api/sellers
```


#### Get Seller

```http
  GET /api/sellers/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of seller to fetch |

#### Save Seller

```http
  POST /api/sellers
```


##### Request:
```json
{
  "user": 1,
  "address": "",
  "birthdate": null,
  "is_active": false
}

```

#### Update Seller

```http
  PUT /api/sellers/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of seller to update |

##### Request:
```json
{
  "user": 1,
  "address": "",
  "birthdate": null,
  "is_active": false
}
```

#### Delete Seller

```http
  DELETE /api/branch_stores/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of seller to delete |

#### Get Users

```http
  GET /api/users
```


#### Get User

```http
  GET /api/users/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of user to fetch |

#### Save User

```http
  POST /api/users
```


##### Request:
```json
{
    "password": "",
    "last_login": null,
    "is_superuser": false,
    "username": "",
    "first_name": "",
    "last_name": "",
    "email": "",
    "is_staff": false,
    "is_active": false,
    "date_joined": null,
}

```

#### Update User

```http
  PUT /api/users/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of user to update |

##### Request:
```json
{
    "password": "",
    "last_login": null,
    "is_superuser": false,
    "username": "",
    "first_name": "",
    "last_name": "",
    "email": "",
    "is_staff": false,
    "is_active": false,
    "date_joined": null,
}
```

#### Delete User

```http
  DELETE /api/branch_stores/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of user to delete |

### Endpoint 4

Se ha creado un endpoint para el inicio de sesión y la simulación de autenticación. Este endpoint recibe en la solicitud el nombre de usuario y la contraseña, y devuelve un valor en formato base64. Dicho valor se utiliza para configurar la cabecera de Autorización y permitir el acceso a otros endpoints para su consumo posterior.

#### Login User

```http
  POST /api/auth/login
```


##### Request:
```json
{
  "username": "",
  "password": "",
}

```

##### Response:
```json
{
  "message": "",
  "access_token": "",
}

```
