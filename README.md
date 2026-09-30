# Especialista en Fugas Chile 🛠️🔥💧

Sitio web estático de alta ingeniería para [especialista-fugas.cl](https://especialista-fugas.cl/), desarrollado para máxima velocidad de carga (Core Web Vitals 100/100), optimización SEO avanzada y captura directa de leads a WhatsApp.

## 🚀 Características Principales

- **Arquitectura 100% Estática:** Desarrollado en HTML5 semántico, Vanilla CSS y Vanilla JS. Cero frameworks pesados, carga instantánea y máxima seguridad.
- **Rescate de URLs Indexadas en Google (0 Errores 404):** Mapeo completo de las 18 URLs ya indexadas por Google para mantener toda la autoridad histórica del dominio.
- **Páginas Estratégicas de Ataque a la Competencia:**
  - `sellado-de-fugas-de-gas-con-prodoral/` (Sellado interno no destructivo con tecnología alemana Prodoral R6-1).
  - `deteccion-de-fugas-con-gas-trazador/` (Detección acústica y Formigas: 95% Nitrógeno + 5% Hidrógeno).
  - `deteccion-de-fugas-de-agua/` (Detección de filtraciones con geófono digital y ultrasonido).
  - `deteccion-de-fugas-de-piscinas/` (Pruebas estancas en piscinas sin vaciar).
  - `certificacion-sec-sello-verde/` (Inspección, regularización y tramitación Sello Verde SEC).
  - `emergencias-24-7/` (Atención urgente por olor a gas y corte de medidor).
- **Enrutamiento Directo a WhatsApp:** Todos los formularios de contacto capturan los datos (Nombre, Teléfono, Comuna, Servicio y Detalle) y abren automáticamente la app de WhatsApp con un mensaje pre-formateado al número oficial `+56 9 3223 7072`.
- **Datos Estructurados Schema.org JSON-LD:**
  - `PlumbingService` con geolocalización, horarios 24/7 y catálogo de servicios.
  - `FAQPage` con 15 preguntas y respuestas en la Home y 10 a 12 en cada subpágina para Rich Snippets en Google.
  - `BreadcrumbList` jerárquico.
- **Diseño Mobile-First y Responsive:** Sticky header con efecto glassmorphism, menú hamburguesa drawer para móviles/tablets y barra fija de llamada/WhatsApp en la parte inferior de pantallas táctiles.
- **SEO & Indexación:** `sitemap.xml` con 25 URLs y prioridades de rastreo, `robots.txt` y `.htaccess` con compresión GZIP y cabeceras de expiración de caché.

## 📁 Estructura del Proyecto

```text
/
├── index.html                                        # Portada Principal
├── sellado-de-fugas-de-gas-con-prodoral/             # Ataque AS Gasfiter (Prodoral R6-1)
├── deteccion-de-fugas-con-gas-trazador/              # Detección con Gas Trazador
├── deteccion-de-fugas-de-agua/                       # Ataque Cerofugas (Geófono)
├── deteccion-de-fugas-de-piscinas/                   # Filtraciones en Piscinas
├── certificacion-sec-sello-verde/                    # Sello Verde SEC
├── emergencias-24-7/                                 # Emergencias 24/7
├── fuga-de-gas/                                      # Fuga de Gas Core
├── fuga-de-gas-deteccion/                            # Diagnóstico de Hermeticidad
├── aplicacion-de-prodoral-para-fuga-de-gas/          # Aplicación Prodoral
├── gasfiter-sec-especialista-en-fuga-de-gas/         # Gásfiter SEC
├── fuga-de-gas-gasfiter-certificado-en-fugas-de-gas/ # Gásfiter Certificado
├── fuga-de-gas-reparamos-fugas-de-gas-sin-romper/    # Reparación Sin Romper
├── fuga-de-gas-servicio-de-experto-en-fugas-de-gas/  # Servicio de Experto
├── fuga-de-gas-penalolen/                            # Cobertura Peñalolén
├── fuga-de-gas-pirque/                               # Cobertura Pirque
├── fuga-de-gas-papudo/                               # Cobertura Papudo
├── fuga-de-gas-rancagua/                             # Cobertura Rancagua
├── fuga-de-gas-paine/                                # Cobertura Paine
├── fuga-de-gas-la-chicureo/                          # Cobertura Chicureo
├── fuga-de-gas-quinta-normal/                        # Cobertura Quinta Normal
├── fuga-de-gas-puente-alto/                          # Cobertura Puente Alto
├── fuga-de-gas-maria-pinto/                          # Cobertura María Pinto
├── fuga-de-gas-san-bernardo/                         # Cobertura San Bernardo
├── fuga-de-gas-san-joaquin/                          # Cobertura San Joaquín
├── assets/
│   ├── css/style.css                                 # Sistema de diseño moderno
│   ├── js/main.js                                    # Lógica interactiva y WhatsApp
│   └── images/                                       # Logo, sellos SEC y QR oficial
├── build_site.py                                     # Generador de páginas estáticas
├── sitemap.xml                                       # Mapa del sitio XML
├── robots.txt                                        # Directivas de rastreo
└── .htaccess                                         # Configuración Apache GZIP y caché
```

## 🛠️ Regenerar o Actualizar Páginas

Para regenerar todas las páginas o agregar nuevas rutas:

```bash
python build_site.py
```

---
© 2026 Especialista en Fugas Chile. Todos los derechos reservados.
