## Descripción

La aplicación consiste en un pequeño servidor que expone dos endpoints utilizando métodos HTTP.

## Endpoints

### GET /info
Devuelve información general sobre la aplicación.

### POST /mensaje
Recibe un mensaje en formato JSON y devuelve una respuesta personalizada.

Ejemplo de JSON enviado:

{
 "mensaje": "Hola servidor"
}

## Arquitectura

El sistema sigue una arquitectura Cliente/Servidor:

Cliente (Navegador o Postman) → Servidor Flask → Base de datos

El cliente envía solicitudes HTTP al servidor, el servidor procesa la información y devuelve una respuesta en formato JSON.

## Archivos del proyecto

- app.py → servidor Flask con los endpoints
- diagrama.png → diagrama de arquitectura del sistema
