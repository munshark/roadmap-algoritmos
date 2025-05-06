# 05 – Introducción a Git y GitHub

## ¿Qué es Git?
Git es un sistema de control de versiones distribuido que permite a los desarrolladores rastrear cambios en el código, colaborar en proyectos y mantener un historial de modificaciones.

## ¿Qué es GitHub?
GitHub es una plataforma basada en la nube que permite alojar repositorios Git, facilitando la colaboración y el trabajo en equipo en proyectos de software.

## ¿Qué es un repositorio?
Un repositorio es un espacio donde se almacena el código de un proyecto junto con su historial de cambios. Puede estar alojado localmente o en plataformas como GitHub.

## ¿Qué es GitHub Classroom y cómo lo están utilizando?
GitHub Classroom es una herramienta que permite a los docentes gestionar tareas y proyectos de programación. En este curso, se utiliza para asignar repositorios individuales a los estudiantes, facilitando el seguimiento de su progreso.

---

## Flujo básico para los estudiantes

1. **Aceptar el link de GitHub Classroom.**  
    Esto creará un repositorio personal para la tarea.

2. **Clonar el repositorio con `git clone`.**  
    ```bash
    git clone <URL-del-repositorio> # Puedes añadir un `.` al final para clonar solo el contenido sin crear una carpeta nueva.
    ```

3. **Entrar a la carpeta del repositorio.**  
    ```bash
    cd <nombre-del-repositorio> # Asegúrate de estar en la carpeta correcta antes de continuar.
    ```

4. **Configurar usuario y correo de Git.**  
    
    - Configura tu nombre y correo electrónico de Git (si no lo has hecho antes).  
    ```bash
    git config --global user.name "Tu Nombre"
    git config --global user.email "tu.email@ejemplo.com"
    ```
    - Configura tu nombre y correo de forma local si estas en un entorno compartido.  
    ```bash
    git config --local user.name "Tu Nombre"
    git config --local user.email "tu.email@ejemplo.com"
    ```
    
5. **Realizar cambios en los archivos.**  
    Edita los archivos según las instrucciones de la tarea.

6. **Ver estado, agregar, hacer commit y subir los cambios.**  
   
    - Con `Git Bash` y otros entornos de terminal.
    ```bash
    git status
    git add <archivo-o-carpeta> # o usa '.' para agregar todo el contenido.
    git commit -m "Descripción de los cambios"
    git push origin main
    ```

    - Con `Visual Studio Code (Opción Gráfica)`:
        - Abre la extensión de Git en la barra lateral izquierda.
        - Selecciona los archivos que deseas agregar y haz clic en el icono de `+` para agregarlos al área de preparación (staging).
        - Escribe un mensaje descriptivo en el campo de commit y haz clic en el botón de commit para guardar los cambios.
        - Haz clic en el botón de sincronización (o push) para subir los cambios al repositorio remoto.


---

## Tabla de comandos esenciales

| Comando         | Descripción                                      |
|------------------|--------------------------------------------------|
| `git clone`      | Clona un repositorio remoto a tu máquina local. |
| `git status`     | Muestra el estado de los archivos en el repositorio. |
| `git add`        | Agrega archivos al área de preparación (staging). |
| `git commit`     | Guarda los cambios en el historial del repositorio. |
| `git push`       | Sube los cambios al repositorio remoto.         |

---

## Recomendación
**Recuerda cerrar sesión en el navegador del laboratorio al terminar.** Esto evitará que otros accedan a tu cuenta de GitHub.

---

## Nota sobre GitHub Codespaces
Si el docente lo habilita, puedes usar **GitHub Codespaces** para trabajar en tus tareas directamente desde el navegador, sin necesidad de instalar software adicional.
