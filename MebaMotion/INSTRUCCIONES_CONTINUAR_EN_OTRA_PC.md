# Instrucciones para continuar el proyecto Mebaten en otra PC

Este documento sirve para retomar el mismo proyecto en otra computadora con Codex.

## Carpeta principal del proyecto

La versión actual que debes conservar y mover es:

```text
C:\Users\Mebaten\Documents\Codex\2026-07-06\new-chat-2\outputs\mebaten-premium
```

Dentro de esa carpeta están:

```text
index.html
MANUAL_INSTRUCCIONES.md
assets\
```

El archivo principal de la página es:

```text
index.html
```

## Qué copiar a la otra computadora

Copia completa la carpeta:

```text
mebaten-premium
```

No copies solo el `index.html`, porque la página depende de imágenes, logos, carruseles, favicon y assets dentro de `assets\`.

Puedes copiarla con USB, OneDrive, Google Drive, Dropbox, WeTransfer o un ZIP.

## Recomendación para moverla

1. Comprime la carpeta `mebaten-premium` en ZIP.
2. Pasa el ZIP a la otra computadora.
3. Descomprímelo en una carpeta fácil de encontrar, por ejemplo:

```text
C:\Users\TU_USUARIO\Documents\Mebaten\mebaten-premium
```

4. En la otra PC, abre Codex.
5. Dile a Codex que trabaje sobre esa carpeta.

## Mensaje recomendado para pegar en Codex en la otra PC

Copia y pega este mensaje en la nueva conversación de Codex:

```text
Quiero continuar trabajando una página web de Mebaten.

La carpeta del proyecto es:
[PEGA_AQUI_LA_RUTA_DE_LA_CARPETA]\mebaten-premium

El archivo principal es index.html.

Restricciones importantes:
- El sitio debe seguir siendo de una sola página.
- Debe conservar la navegación por anclas.
- Debe conservar la barra superior de progreso .progress.
- Debe conservar el header fijo con sección activa.
- No dividir en páginas separadas.

Contexto del proyecto:
- Es una página web premium para Mebaten, empresa de transformadores, tableros eléctricos, bancos de capacitores y subestaciones compactas.
- La versión actual está en index.html.
- Los assets están dentro de assets.
- El carrusel de subestaciones compactas usa assets/carousel/subestaciones-compactas.
- El botón de WhatsApp flotante debe mantenerse.
- El formulario está preparado con validación visual y respaldo mailto.
- El diseño actual usa una estética industrial B2B, con azul/navy y acento ámbar.

Antes de modificar, revisa index.html y MANUAL_INSTRUCCIONES.md.
Después aplica los cambios directamente sobre index.html y valida que no haya imágenes rotas.
```

## Archivos importantes actuales

```text
index.html
MANUAL_INSTRUCCIONES.md
assets\mebaten-logo.png
assets\mebaten-logo-full.png
assets\product-substation-compacta.jpeg
assets\product-control-panels.jpg
assets\carousel\subestaciones-compactas\
assets\carousel\transformadores\
assets\carousel\logistica\
assets\carousel\instalacion\
assets\carousel\capacitores\
```

## Últimos cambios realizados

- Se corrigió el logo del footer para que no se viera estirado.
- Se cambió la imagen de tableros eléctricos por `assets/product-control-panels.jpg`.
- Se cambió la imagen del producto de subestaciones compactas por `assets/product-substation-compacta.jpeg`.
- Se creó un carrusel específico para subestaciones compactas:

```text
assets\carousel\subestaciones-compactas\
```

- Se eliminó la sección "Clientes y proyectos".
- En "Proyectos reales" quedaron 5 tarjetas.
- Se eliminó "Pedestal" de Proyectos reales.
- Se sustituyó el fondo inicial pixelado por una imagen de logística más nítida.

## Cómo revisar la página en la otra PC

Como es una página estática, puedes abrir:

```text
index.html
```

directamente con doble clic en el navegador.

Si alguna función visual no carga por políticas del navegador, puedes pedirle a Codex que inicie un servidor local para probarla.

## Qué debe validar Codex después de cada cambio

Pídele que revise:

- Que exista un solo `<h1>`.
- Que no haya rutas de imágenes rotas.
- Que las imágenes tengan `width` y `height`.
- Que las imágenes fuera del primer pantallazo mantengan `loading="lazy"`.
- Que la barra `.progress` siga existiendo.
- Que el sitio siga siendo single-page.
- Que el menú siga navegando por anclas.

## Pendientes sugeridos

- Comprimir el logo grande `assets/mebaten-logo-full.png`.
- Convertir carruseles a WebP si se quiere mejorar rendimiento.
- Completar datos técnicos reales de productos.
- Completar normas exactas por producto.
- Configurar Formspree, Web3Forms o Getform para recibir leads sin depender de mailto.
- Revisar el diseño final en móvil y escritorio antes de publicar.

