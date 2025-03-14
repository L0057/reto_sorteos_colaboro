"""
###
Esta propuesta fue realizada por el quipo número 2.


Recordar que el hecho de mostrarse como una página web fue idea del equipo de trabajo número 2 para poder realizar una demostración visual sobre las funcionalidades de la propuesta a los socios formadores el día de la presentación, pero que no está pensada para ser una página web, sino para que dichas funcionalidades sean integradas dentro de la app "Colaboro +".

###
"""

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


## Requisitos
- Python 3.8 o superior
- Las siguientes librerías de Python:
  - `tkinter` (incluido por defecto en Python)
  - `sqlite3` (incluido por defecto en Python)

## Organización de los archivos
/Proyecto_equipo_2
│
├── app.py
├── submissions.db         # Se crea automáticamente (datos)
├── /templates
│   ├── layout.html
│   ├── choose_role.html
│   ├── buyer.html
│   ├── buyer_result.html
│   ├── login.html
│   ├── collaborator_form.html
│   ├── submission_success.html
│   └── dashboard.html     # Nueva plantilla para la tabla de registros
└── /static
    └── /qr_codes          # Carpeta para guardar los QR generados


## Instrucciones de Ejecución
1. Asegúrate de tener Python instalado en tu sistema.
2. Guarda el archivo del programa en una carpeta de tu elección.
3. Abre una terminal o línea de comandos en la ubicación donde guardaste el archivo.
4. Ejecuta el siguiente comando:
   ```
   python app.py
   ```

- La interfaz gráfica te permitirá realizar todas las acciones necesarias.
- Sigue las indicaciones en pantalla para interactuar con la base de datos.

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Instrucciones de Uso

## Acceso a la Página
Para acceder a la página web, sigue estos pasos:
1. Ejecuta el programa siguiendo las instrucciones anteriores.
2. En la terminal, se mostrará un enlace con el formato:
   ```
   http://127.0.0.1:5000
   ```
3. Copia y pega este enlace en tu navegador para acceder a la página web.

## Funcionalidad de Cada Pestaña

### 1. Página Principal (Inicio)
- Al entrar, se pregunta qué acción el colaborador quiere realizar en ese momento:
  - **Me gustaría ver los datos guardados**: Puede escanear su código QR para ver sus datos, o puede copiar y pegar la llave (número de serie) que contiene los datos cifrados.
  - **Me gustaría ingresar nuevos datos**: Debe iniciar sesión para acceder a las funciones adicionales y poder registrar los datos de un nuevo comprador.

### 2. Llenado de Datos
- Los colaboradores pueden ingresar la información de un comprador:
  - Nombre
  - Correo electrónico
  - Número de teléfono
  - Estado de procedencia
- Al guardar, se genera un código QR único para el comprador y se muestra la llave cifrada en texto.

### 3. Base de Datos
- Muestra una tabla con todos los datos ingresados previamente.
- Permite revisar la información almacenada de cada comprador.
- Puede filtrar los datos por nombre, correo o estado de procedencia.

### 4. Escaneo de QR
- Los compradores pueden escanear su código QR.
- Al escanearlo, se mostrará su información en una ventana emergente con los datos en formato de viñetas.

### 5. Generación de Nuevo QR
- Cada vez que un colaborador ingresa nuevos datos, se genera un código QR único.
- Este QR es el que el comprador podrá escanear posteriormente para ver su información.

## Inicio de Sesión (Log In)

### Credenciales de Acceso para los Colaboradores
- **Correo 1:** `colaborador@example.com`
- **Contraseña 1:** `password1`

- **Correo 2:** `otrocolaborador@example.com`
- **Contraseña 2:** `password2`


### Cómo Modificar o Agregar Nuevas Credenciales
1. Abre el archivo `app.py`.
2. Busca la sección donde se definen los colaboradores en el archivo. Debería verse algo como esto:
   ```
   collaborators = {
    'colaborador@example.com': 'password1',
    'otrocolaborador@example.com': 'password2'
   }
   ```
3. Para agregar un nuevo usuario, simplemente añade una nueva línea dentro del diccionario:
   ```
   collaborators = {
    'colaborador@example.com': 'password1',
    'otrocolaborador@example.com': 'password2',
    ...,
    'nuevo_usuario@email.com': 'nueva_contraseña'
   }
   ```
4. Guarda los cambios, reinicia el programa Y vuelve a seguir todos los pasos anteriores.




