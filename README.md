# Mi Portfolio (Django)

Este proyecto convierte el portfolio estático en un sitio **Django** y agrega un **blog** con comentarios.

## Requisitos
- Python 3.10+
- pip
- (opcional) virtualenv

## Puesta en marcha

```bash
python -m venv .venv && source .venv/bin/activate  # En Windows: .venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser   # crea el admin
python manage.py runserver
```

- Home: http://127.0.0.1:8000/
- Blog: http://127.0.0.1:8000/blog/
- Admin: http://127.0.0.1:8000/admin/

### Crear posts
Ingresá al **admin** con el superusuario y creá entradas en **Posts** (pueden incluir imagen).

### Comentarios y moderación
Cualquiera puede comentar en el detalle del post. Solo el usuario staff puede eliminar comentarios
(desde el admin o con el botón *Eliminar* que aparece si estás logueado como staff).

### Estructura
- `core/` homepage con el portfolio (usa tus imágenes y estilos).
- `blog/` app del blog (models, views, urls, templates).
- `templates/` (`base.html`, `core/index.html`, `blog/*.html`)
- `static/` (`css/styles.css`, `img/*`)

### Notas
- Las rutas estáticas usan `{% load static %}`.
- Para imágenes en posts se usa `Pillow` y `MEDIA_URL`/`MEDIA_ROOT`.
