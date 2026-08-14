# Manual de instrucciones - MebaMotion

## Ubicación del proyecto

La versión actual del sitio está en:

`D:\Alex\MebaMotion`

Archivos principales:

- `index.html`: contiene todo el HTML, CSS y JavaScript del sitio.
- `assets/`: contiene logos, imágenes principales, catálogos PDF y fotos de proyectos.
- `assets/carousel/`: contiene las fotos organizadas por categoría para la sección de proyectos reales.
- `assets/catalogos/`: contiene los catálogos PDF descargables.
- `assets/sin-uso/`: contiene archivos archivados que ya no se muestran en el sitio.

## Estructura del sitio

El sitio es una sola página con navegación por anclas:

- Inicio
- Empresa
- Soluciones
- Productos
- Proyectos
- Calidad
- FAQ
- Contacto

La barra superior permanece fija y el JavaScript marca dinámicamente la sección activa mientras el usuario navega.

## Identidad y mensaje principal

El mensaje central del sitio es:

`Distribuyendo Energía a tu Vida`

Este mensaje se usa en el hero, el `<title>`, `og:title` y `twitter:title`.

## Imágenes principales

La imagen del hero visible al cargar el sitio usa:

`assets/hero-mebaten-transformador-real-bright.webp`

La versión PNG original quedó archivada en:

`assets/sin-uso/hero-mebaten-transformador-real-bright.png`

Para cambiar la imagen del hero, actualiza el `src` dentro de `.hero-bg img` y conserva `width`, `height`, `fetchpriority="high"` y `decoding="async"`.

## Productos interactivos

La sección de productos mantiene cuatro categorías principales:

- Transformadores
- Tableros eléctricos
- Bancos de capacitores
- Subestaciones compactas

Transformadores tiene subcategorías desplegadas dentro del menú izquierdo:

- Pedestal
- Sumergible
- Poste
- Estación
- Subestación con gargantas
- Seco VPI
- Seco encapsulado

Cada subcategoría cambia imagen, nombre, descripción, datos técnicos y puntos destacados desde el objeto JavaScript `transformerProducts`.

## Proyectos reales

Cada tarjeta de proyectos usa `data-carousel` con rutas separadas por `|`.

Ejemplo:

```html
data-carousel="assets/carousel/logistica/logistica-01.jpeg|assets/carousel/logistica/logistica-03.jpeg"
```

Para agregar fotos:

1. Copia la imagen a la carpeta correspondiente dentro de `assets/carousel/`.
2. Agrega la ruta en `data-carousel`.
3. Separa cada imagen con `|`.

## Formulario de cotización

El formulario funciona como captador de prospectos y solicitudes de cotización, no como cotizador técnico automático.

Campos actuales:

- Nombre
- Empresa
- Teléfono
- Correo
- Ciudad / Estado
- Equipo a cotizar
- Mensaje libre sobre lo que necesita
- Archivo adjunto opcional en PDF, JPG o PNG

En esta versión estática, al enviar el formulario se abre un correo prellenado dirigido a:

`ventas@mebaten.com`

Si se configura un servicio externo en `data-endpoint`, el formulario envía `FormData` y puede incluir archivo adjunto.

## Cómo activar Formspree o un servicio similar

En `index.html`, busca:

```html
data-endpoint=""
```

Coloca ahí la URL real del servicio de formularios, por ejemplo la URL de Formspree, Web3Forms o Getform.

Mientras no se cambie ese valor, el sitio usará el correo prellenado como respaldo.

## WhatsApp

El botón flotante de WhatsApp, la barra móvil y los enlaces de contacto apuntan al número vigente:

`228 203 8038`

El enlace está configurado con:

`https://wa.me/522282038038`

## Assets archivados

Se descartó la franja de normas/certificaciones y los logos de clientes. Sus placeholders se archivaron en:

- `assets/sin-uso/certifications/`
- `assets/sin-uso/clients/`

También se archivaron imágenes no referenciadas por el sitio, como `product-control-panels.png`, `mebaten-logo-header.png`, `product-panels.jpg`, `stock-pedestal.jpg`, `delivery.jpg`, `hero-project.jpg` y las imágenes `trust-*.jpeg`.

`quality-floor.jpg` se conserva porque sí está referenciada en el CSS de la sección de contacto.

## Cómo editar textos

Abre `index.html` y busca el texto visible dentro de etiquetas como:

- `<h1>`
- `<h2>`
- `<h3>`
- `<p>`
- `<summary>`
- `<button>`
- `<option>`

El archivo usa UTF-8 con acentos directos. Para mantenerlo editable, escribe acentos como `México`, `eléctrico`, `cotización` y evita volver a entidades HTML como `&eacute;`.

## Cómo cambiar colores

Los colores principales están en `:root`, al inicio del CSS.

Ejemplo:

```css
--navy: #082b55;
--blue: #0a4f90;
--accent: #f1b434;
```

Antes de eliminar una variable, busca `var(--nombre)` en todo `index.html` para confirmar que no se usa.

## Validaciones recomendadas

Antes de publicar o entregar cambios, revisa:

- El botón de WhatsApp abre el chat del número correcto.
- El título de pestaña usa `Mebaten | Distribuyendo Energía a tu Vida`.
- Las cuatro pestañas de productos funcionan.
- Las subcategorías de Transformadores cambian el contenido correcto.
- Los carruseles de Proyectos abren el modal y navegan imágenes.
- El FAQ abre y cierra correctamente.
- El formulario valida campos obligatorios, archivo opcional y abre el correo de respaldo si no hay endpoint.
- En móvil no hay scroll horizontal y la barra inferior no tapa contenido importante.