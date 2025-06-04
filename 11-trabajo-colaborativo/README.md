# 11 – Trabajo colaborativo en Git y GitHub

## Introducción
El trabajo en equipo requiere coordinar los cambios de varias personas en un mismo repositorio. Git y GitHub ofrecen herramientas para organizar este proceso de forma segura y ordenada.

## Flujo de trabajo recomendado
1. **Clonar o hacer *fork* del repositorio.** Si no tienes permisos de escritura, realiza un *fork* y clona tu copia localmente.
2. **Crear una rama nueva para cada aporte.** Utiliza `git checkout -b nombre-de-tu-rama` para mantener el código principal libre de cambios inestables.
3. **Realizar los cambios y confirmar con `git commit`.** Procura que cada commit sea claro y enfocado en una tarea específica.
4. **Sincronizar con la rama principal antes de subir.** Ejecuta `git pull origin main` (o la rama correspondiente) para incorporar los cambios de tus compañeros y resolver posibles conflictos.
5. **Subir la rama al repositorio remoto.** Usa `git push origin nombre-de-tu-rama`.
6. **Abrir un Pull Request en GitHub.** Describe brevemente qué cambios realizaste para que el resto del equipo pueda revisarlos.
7. **Revisar y aprobar cambios.** Utiliza los comentarios y revisiones de GitHub para discutir el código antes de fusionarlo.
8. **Fusionar (merge) la rama cuando esté lista.** Generalmente se realiza desde la interfaz de GitHub.

## Consejos para colaborar con éxito
- Mantén tus ramas pequeñas y con un único objetivo.
- Escribe mensajes de commit descriptivos y en tiempo presente.
- Revisa con regularidad las ramas de tus compañeros para evitar duplicar trabajo.
- Si encuentras conflictos de fusión, resuélvelos localmente y vuelve a subir tu rama.

## Comandos útiles
| Comando                     | Descripción                                   |
|-----------------------------|-----------------------------------------------|
| `git checkout -b rama`      | Crear y cambiar a una nueva rama.             |
| `git pull origin main`      | Trae y fusiona cambios de la rama principal.  |
| `git push origin rama`      | Sube tu rama al repositorio remoto.           |
| `git fetch`                 | Obtiene la información del remoto.            |
| `git merge rama`            | Fusiona otra rama en la actual.               |

## Ejemplo rápido
```bash
# Clonar y crear una rama
git clone <URL-del-repositorio>
cd nombre-del-repositorio
git checkout -b feature-saludo

# Hacer cambios y subirlos
# (edita archivos aquí)

git add archivo.py
git commit -m "Agregar mensaje de saludo"

git pull origin main
# Resolver conflictos si los hubiera

git push origin feature-saludo
```
Luego abre un Pull Request desde GitHub para que tu equipo revise los cambios.

## Ejercicios

Estos ejercicios te ayudarán a practicar el flujo de trabajo colaborativo con
tu equipo. Trabajen en parejas o grupos pequeños y sigan cada paso con un
repositorio de prueba.

1. **Creación de ramas y Pull Requests**
   - Cada integrante debe crear una rama con su nombre.
   - Realicen un cambio simple en un archivo (por ejemplo, añadan su nombre a
     un archivo `colaboradores.md`).
   - Abran un Pull Request describiendo el cambio.

2. **Revisiones cruzadas**
   - Asignen a otro compañero la revisión de su Pull Request.
   - Dejen comentarios o sugerencias antes de aprobar los cambios.

3. **Resolución de conflictos**
   - Coordinen para que dos ramas modifiquen la misma línea de un archivo.
   - Intenten fusionar ambas ramas en `main` y resuelvan el conflicto de forma
     manual.

4. **Documentación del proceso**
   - Creen un documento `acuerdos.md` donde registren las reglas de su flujo de
     trabajo (formato de ramas, mensajes de commit, etc.).
   - Súbanlo mediante un Pull Request y consúltenlo cuando surjan dudas.

## Conclusión
Trabajar de forma colaborativa requiere disciplina y comunicación. Utiliza las ramas y los Pull Requests para mantener un historial claro de las contribuciones de cada miembro del equipo.
