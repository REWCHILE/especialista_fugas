# -*- coding: utf-8 -*-
"""
Generator Script: Especialista en Fugas
High Engineering Static Site Generator
Generates all 24 indexed + strategic competitor attack pages with:
- Schema.org PlumbingService & FAQPage JSON-LD (10-15 FAQs each)
- Direct WhatsApp lead routing (+56 9 4987 7316)
- Sticky header, responsive drawer, mobile quick-action bar
- 100% SEO optimized for Chile & Core Web Vitals
"""

import os
import json

PAGES_DATA = [
    # 1. Competitor Attack: AS Gasfiter (Prodoral R6-1)
    {
        "slug": "sellado-de-fugas-de-gas-con-prodoral",
        "title": "▷ Sellar Fugas de Gas 【 Prodoral R6-1 Sin Romper • Especialistas SEC Chile 】✔️",
        "meta_desc": "Sellado de fugas de gas con polímero alemán Prodoral R6-1 en Santiago. Sin demoler muros ni baldosas. Garantía por escrito y Sello Verde SEC. Tel/WA: +56 9 4987 7316.",
        "h1": "Sellado de Fugas de Gas con <span class='highlight-red'>Prodoral R6-1</span> Sin Romper Muros",
        "hero_badge": "🛡️ TECNOLOGÍA ALEMANA ORIGINAL • TÉCNICOS AUTORIZADOS SEC",
        "intro": "Recupere la hermeticidad de su red de gas de forma limpia, segura y definitiva. Prodoral R6-1 es el sellante polimérico líder en Europa y Chile que repara microfugas internas circulando por la cañería sin necesidad de picar muros, radieres ni romper cerámicas.",
        "breadcrumb_name": "Sellado con Prodoral R6-1",
        "service_focus": "Sellado no destructivo de microfugas de gas en cañerías empotradas y subterráneas.",
        "specific_content": """
        <h2>¿Cómo Funciona el Sellado Interno de Cañerías con Prodoral R6-1?</h2>
        <p>Prodoral R6-1 es una emulsión polimérica viscosa de formulación alemana diseñada específicamente para sellar herméticamente microfugas en uniones roscadas y porosidades de cañerías de gas. A diferencia de las costosas demoliciones convencionales, el producto se introduce directamente al interior de la red presurizada con un equipo técnico de inyección.</p>
        <p>El compuesto recorre cada codo, tee y tramo de la tubería, reaccionando ante las fugas de presión microscópicas para polimerizarse y formar una película elástica permanente que resiste vibraciones térmicas y mecánicas por décadas.</p>
        <div class="cards-grid" style="margin: 30px 0;">
          <div class="service-card">
            <h3 class="service-card-title">Cero Roturas ni Escombros</h3>
            <p class="service-card-text">No rompemos paredes empotradas, porcelanatos, baldosas ni pisos flotantes. Su vivienda o negocio permanece intacto.</p>
          </div>
          <div class="service-card">
            <h3 class="service-card-title">Repara Más de 20 Microfugas</h3>
            <p class="service-card-text">La fórmula sella la fuga principal y cualquier otra microfisura incipiente en toda la red, actuando de forma preventiva.</p>
          </div>
          <div class="service-card">
            <h3 class="service-card-title">Aprobación Sello Verde SEC</h3>
            <p class="service-card-text">Efectuamos la prueba de presión manométrica reglamentaria y entregamos el informe para que la compañía reponga el gas de inmediato.</p>
          </div>
        </div>
        """,
        "faqs": [
          ("¿Qué es Prodoral R6-1 y para qué sirve?", "Prodoral R6-1 es un sellante polimérico alemán de alta densidad diseñado para sellar microfugas en cañerías de gas empotradas o subterráneas sin romper paredes ni pisos."),
          ("¿El sellado con Prodoral daña o achica el diámetro de la cañería?", "No. El sellante solo forma una película microscópica elástica de micrones de grosor y el excedente se drena al 100% con aire comprimido, manteniendo intacto el caudal de gas."),
          ("¿Cuánto demora el servicio en una casa o departamento?", "El proceso completo dura entre 4 y 6 horas. En el mismo día su instalación queda presurizada, hermética y lista para el uso."),
          ("¿Es compatible con gas natural y gas licuado (GLP)?", "Sí, Prodoral R6-1 es totalmente inerte y compatible tanto con Gas Natural distribuido por cañería como con Gas Licuado de Petróleo (GLP)."),
          ("¿Qué tipos de cañería se pueden sellar con Prodoral?", "Se aplica con total efectividad en cañerías de cobre, acero negro, acero galvanizado y uniones roscadas o soldadas."),
          ("¿Cuánto dura la reparación realizada con Prodoral?", "Tiene una durabilidad comprobada superior a 25 años, resistiendo dilataciones térmicas y las presiones normales de servicio."),
          ("¿La SEC autoriza la prueba de hermeticidad tras sellar con Prodoral?", "Sí. La normativa SEC exige que la instalación mantenga la presión manométrica sin caídas durante la prueba reglamentaria, estándar que Prodoral cumple con creces."),
          ("¿Qué ahorro representa respecto a cambiar cañerías tradicionales?", "Permite ahorrar entre un 40% y 60% del costo total, al evitar gastos de albañilería, rotura de radier, reposición de baldosas y pintura."),
          ("¿Qué ocurre si la compañía de gas cortó o selló mi medidor?", "Realizamos el sellado y emitimos el informe técnico de hermeticidad con instalador SEC para que Metrogas o la distribuidora reactive el servicio sin trabas."),
          ("¿Tienen cobertura de emergencia los fines de semana?", "Sí, atendemos emergencias los 7 días de la semana las 24 horas en todas las comunas de Santiago y alrededores.")
        ]
    },

    # 2. Competitor Strategic: Gas Trazador
    {
        "slug": "deteccion-de-fugas-con-gas-trazador",
        "title": "▷ Detección de Fugas con Gas Trazador 【 Precisión Milimétrica Sin Romper 】✔️",
        "meta_desc": "Localización exacta de fugas subterráneas de gas y agua con Gas Trazador (Hidrógeno/Nitrógeno) en Santiago y RM. Cero excavación destructiva. Tel: +56 9 4987 7316.",
        "h1": "Detección de Fugas con <span class='highlight-red'>Gas Trazador</span> Precisión Milimétrica",
        "hero_badge": "🔬 MÉTODO FORMIGAS NO INVASIVO • GASES INERTES SEGUROS",
        "intro": "Localizamos el punto exacto de filtraciones indetectables en cañerías subterráneas, losas y muros sin realizar excavaciones destructivas. Empleamos mezcla de 95% Nitrógeno y 5% Hidrógeno de máxima sensibilidad.",
        "breadcrumb_name": "Detección con Gas Trazador",
        "service_focus": "Localización milimétrica de fugas complejas en redes enterradas de gas y agua.",
        "specific_content": """
        <h2>Tecnología de Gas Trazador: Máxima Precisión Sin Destruir su Propiedad</h2>
        <p>Cuando una fuga se encuentra bajo un radier de concreto, piso de mármol o a varios metros de profundidad en un jardín, los métodos tradicionales obligan a romper a ciegas hasta dar con la tubería rota. La prueba con <strong>Gas Trazador (Formigas)</strong> soluciona este problema con tecnología de nivel industrial.</p>
        <p>Inyectamos una mezcla gaseosa compuesta por un 95% de Nitrógeno y un 5% de Hidrógeno. Al ser la molécula de hidrógeno la más diminuta de la naturaleza, escapa verticalmente por cualquier microfisura y aflora a la superficie, donde es captada por nuestros sensores electroquímicos de alta precisión con alerta sonora y digital.</p>
        """,
        "faqs": [
          ("¿Qué es el gas trazador y por qué es tan efectivo?", "Es una mezcla no inflamable ni tóxica de nitrógeno e hidrógeno. Su bajísima densidad le permite atravesar tierra, radier y cerámicas hasta el sensor receptor."),
          ("¿El gas trazador es peligroso o inflamable?", "No. Al contener solo un 5% de hidrógeno y 95% de nitrógeno inerte, es completamente seguro, incombustible y no tóxico."),
          ("¿Sirve tanto para fugas de gas como de agua?", "Sí. Es el estándar de oro para localizar tanto fugas de gas como filtraciones complejas en tuberías de agua potable y matrices enterradas."),
          ("¿A qué profundidad puede detectar una fuga?", "Nuestros sensores profesionales de fabricación alemana detectan emanaciones a más de 3 metros de profundidad en suelos compactados."),
          ("¿Es necesario romper el piso para aplicar el gas trazador?", "No. Solo se acopla el equipo a una llave o punto de conexión existente en la red sin alterar la estructura de la vivienda."),
          ("¿Cuánto tarda una inspección con gas trazador?", "En promedio toma entre 2 y 4 horas dependiendo de la extensión del terreno o inmueble."),
          ("¿Qué tipo de informe entregan al finalizar?", "Entregamos un informe técnico detallado señalando la ubicación exacta en plano o sobre el terreno para proceder con la reparación puntual."),
          ("¿Se puede aplicar en departamentos y edificios?", "Sí, es especialmente útil en edificios para determinar en qué piso o shaft vertical se ubica la microfuga."),
          ("¿Qué certificaciones tienen los operadores del equipo?", "Nuestros técnicos cuentan con certificación oficial SEC y entrenamiento en detección acústica y gases trazadores."),
          ("¿Cómo contacto para una prueba urgente?", "Puede llamarnos al +56 9 4987 7316 o presionar el botón de WhatsApp para coordinar el arribo del equipo técnico.")
        ]
    },

    # 3. Competitor Attack: Cerofugas (Fugas de Agua)
    {
        "slug": "deteccion-de-fugas-de-agua",
        "title": "▷ Detección de Fugas de Agua 【 Geófono & Ultrasonido Sin Romper • Chile 】✔️",
        "meta_desc": "Detectamos filtraciones y fugas de agua ocultas bajo radier y jardines con geófono acústico y ultrasonido en Santiago. Ahorre en su cuenta. WhatsApp: +56 9 4987 7316.",
        "h1": "Detección de <span class='highlight-red'>Fugas de Agua</span> Ocultas con Geófono y Ultrasonido",
        "hero_badge": "💧 DIAGNÓSTICO ACÚSTICO DIGITAL • REDUZCA SU CUENTA DE AGUA",
        "intro": "¿Su cuenta de agua se disparó o el medidor sigue girando con todas las llaves cerradas? Ubicamos la fuga subterránea o bajo radier con geófonos digitales de alta ganancia y cámaras térmicas sin picar su casa.",
        "breadcrumb_name": "Detección de Fugas de Agua",
        "service_focus": "Localización y reparación de filtraciones de agua potable fría y caliente.",
        "specific_content": """
        <h2>Detenga las Filtraciones Ocultas y los Cobros Excesivos en su Cuenta de Agua</h2>
        <p>Una fuga silenciosa en una cañería de agua puede desperdiciar miles de litros al mes, saturar el terreno provocando socavones bajo el radier y dañar cimientos estructurales. En <strong>Especialista en Fugas</strong> utilizamos tecnología no invasiva de amplificación sonora y termografía infrarroja para encontrar la falla con exactitud milimétrica.</p>
        <p>Atendemos viviendas unifamiliares, comunidades de edificios, colegios, industrias y recintos comerciales con cuadrillas listas para intervenir en el acto.</p>
        """,
        "faqs": [
          ("¿Cómo sé si tengo una fuga oculta de agua en casa?", "Cierre todas las llaves de artefactos y verifique si la aguja o estrella del medidor de agua sigue girando. Si gira, hay una fuga en la red interna."),
          ("¿Qué es un geófono para fugas de agua?", "Es un equipo electroacústico que capta y amplifica las vibraciones sonoras que produce el agua a presión al salir por una fisura en la cañería."),
          ("¿Pueden detectar fugas de agua caliente?", "Sí, combinamos el geófono con cámaras termográficas de alta sensibilidad que visualizan el gradiente térmico de la cañería a través del piso o muro."),
          ("¿Rompen todo el piso para encontrar la fuga?", "No. Gracias a nuestros instrumentos ubicamos el punto exacto, por lo que si se requiere reparar solo se interviene una baldosa puntual."),
          ("¿Reparan la fuga una vez detectada?", "Sí, contamos con técnicos para efectuar el destape puntual y la reparación definitiva en cobre, PPR, PEX o PVC hidráulico."),
          ("¿Entregan informe para rebaja de cuenta en Aguas Andinas?", "Sí, emitimos informe técnico de reparación de fuga oculta para solicitar la reliquidación por cobro de sobreconsumo o alcantarillado."),
          ("¿Cuánto cuesta una detección de fuga de agua?", "El valor se cotiza según el metraje del inmueble. El costo se recupera rápidamente al detener el desperdicio continuo de agua."),
          ("¿Detectan fugas bajo radier de hormigón?", "Sí, nuestros geófonos digitales filtran el ruido ambiental y detectan fugas bajo losas de hasta 30 cm de espesor."),
          ("¿Qué garantía ofrecen en la reparación?", "Ofrecemos garantía por escrito en todas las soldaduras y uniones mecánicas ejecutadas por nuestro equipo."),
          ("¿Atienden emergencias de inundación o filtración?", "Sí, disponemos de servicio 24/7 en toda la Región Metropolitana con respuesta express al WhatsApp.")
        ]
    },

    # 4. Competitor Strategic: Piscinas
    {
        "slug": "deteccion-de-fugas-de-piscinas",
        "title": "▷ Detección de Fugas en Piscinas 【 Pruebas Hidrostáticas Sin Vaciar • Chile 】✔️",
        "meta_desc": "Especialistas en detección y reparación de fugas en piscinas de hormigón, fibra y liner. Skimmers, retornos y fondo. Atención RM y V Región. WhatsApp: +56 9 4987 7316.",
        "h1": "Detección de Fugas y <span class='highlight-red'>Filtraciones en Piscinas</span> Sin Vaciar el Agua",
        "hero_badge": "🏊 DIAGNÓSTICO INTEGRAL DE PISCINAS • HORMIGÓN, FIBRA Y LINER",
        "intro": "Si su piscina pierde más agua de lo habitual por evaporación, sufre una filtración en el vaso o en las cañerías subterráneas. Identificamos el origen del problema mediante presurización de circuitos y sensores hidrostáticos.",
        "breadcrumb_name": "Fugas en Piscinas",
        "service_focus": "Inspección de tuberías de skimmer, retornos, toma de fondo y vaso estructural.",
        "specific_content": """
        <h2>¿Por Qué Su Piscina Pierde Nivel de Agua?</h2>
        <p>Una pérdida diaria de más de 0.5 cm suele indicar una fuga activa. Las filtraciones pueden originarse en fisuras del hormigón, focos subacuáticos mal sellados o colapso de cañerías de PVC enterradas entre la piscina y la sala de bombas.</p>
        <p>En <strong>Especialista en Fugas</strong> realizamos pruebas hidrostáticas individualizadas para cada circuito (retornos, skimmers, barredera y dreno de fondo) localizando la avería sin tener que vaciar innecesariamente los miles de litros de agua de su piscina.</p>
        """,
        "faqs": [
          ("¿Cómo saber si la pérdida de agua es evaporación o fuga?", "Realice la prueba del balde: coloque un balde con agua al mismo nivel en el borde de la piscina. Si la piscina baja más rápido que el balde, hay fuga."),
          ("¿Es necesario vaciar la piscina para la detección?", "En la gran mayoría de los casos no es necesario vaciar el agua, realizamos las pruebas con instrumental estanco y tintes de flujo."),
          ("¿Qué circuitos de la piscina revisan?", "Presurizamos de manera independiente las líneas de skimmers, retornos, toma de limpiafondos y dreno de fondo."),
          ("¿Qué tipo de piscinas pueden revisar?", "Inspeccionamos piscinas de hormigón pintado o con mosaico vítreo, piscinas de fibra de vidrio y piscinas con liner de PVC."),
          ("¿Pueden detectar fugas en las cañerías bajo el pasto o terraza?", "Sí, aplicamos geófono acústico y gas trazador en los ductos subterráneos que van hacia la sala de máquinas."),
          ("¿También reparan las fisuras en el vaso de la piscina?", "Sí, contamos con selladores epóxicos y poliuretánicos de fraguado subacuático de alta resistencia química al cloro."),
          ("¿Qué pasa si la fuga está en un foco subacuático?", "Revisamos pasamuros, nichos de focos y prensaestopas, sellando cualquier vía de escape de agua."),
          ("¿Tienen cobertura en Chicureo, Pirque, Paine y litoral central?", "Sí, cubrimos todas las comunas con piscinas de la Región Metropolitana y la V Región."),
          ("¿Cuánto tiempo toma la inspección completa?", "El diagnóstico completo suele tomar entre 3 y 5 horas."),
          ("¿Cómo solicito una cotización?", "Escríbanos directamente a nuestro WhatsApp oficial (+56 9 4987 7316) indicando las medidas aproximadas de su piscina.")
        ]
    },

    # 5. Core: Sello Verde SEC
    {
        "slug": "certificacion-sec-sello-verde",
        "title": "▷ Certificación SEC Sello Verde 【 Inspección & Regularización de Gas Chile 】✔️",
        "meta_desc": "Obtenga su Sello Verde SEC. Eliminamos Sellos Rojos y Amarillos en casas, departamentos y edificios. Gásfiter instaladores autorizados SEC. Tel: +56 9 4987 7316.",
        "h1": "Certificación <span class='highlight-red'>Sello Verde SEC</span> y Regularización de Gas",
        "hero_badge": "📜 GÁSFITER AUTORIZADOS SEC CLASE 1, 2 Y 3 • CHILE",
        "intro": "¿Recibió un Sello Rojo o Amarillo en la inspección periódica de gas? Normalizamos su instalación según la normativa del Decreto Supremo Nº 66 para obtener su Sello Verde SEC oficial y garantizar la continuidad del suministro.",
        "breadcrumb_name": "Sello Verde SEC",
        "service_focus": "Regularización de anomalías, proyectos de gas y obtención del Sello Verde.",
        "specific_content": """
        <h2>Eliminamos Sellos Rojos y Amarillos con Respaldo Técnico SEC</h2>
        <p>El Sello Verde es el distintivo oficial que certifica que una instalación de gas es segura y cumple con los estándares exigidos por la SEC en Chile. Un Sello Rojo implica riesgo inminente y puede provocar el corte inmediato del medidor por parte de Metrogas o la distribuidora de gas.</p>
        <p>Nuestro equipo de instaladores certificados SEC realiza la corrección integral de todas las anomalías: eliminación de fugas con Prodoral R6-1, adaptación de ventilaciones superiores e inferiores, conductos de evacuación de calefont y calderas, y reemplazo de llaves de paso no normadas.</p>
        """,
        "faqs": [
          ("¿Qué significa tener Sello Rojo en el medidor de gas?", "Significa que la instalación presenta defectos críticos (fugas de gas, mala evacuación de gases quemados o falta de ventilación) y la distribuidora puede suspender el servicio."),
          ("¿Qué diferencia hay entre Sello Amarillo y Sello Rojo?", "El Sello Amarillo indica defectos menores con plazo para corregir, mientras que el Sello Rojo prohíbe el suministro por riesgo de intoxicación o explosión."),
          ("¿Cómo se pasa de Sello Rojo a Sello Verde?", "Se contrata a un instalador certificado SEC que repara las anomalías, emite el certificado de conformidad y solicita la reinspección ante la entidad certificadora."),
          ("¿Cuánto tiempo demora la regularización?", "Las correcciones técnicas y pruebas de hermeticidad las resolvemos en 24 a 48 horas."),
          ("¿Es obligatorio tener Sello Verde para vender o arrendar una propiedad?", "Sí, en la mayoría de los trámites notariales, ventas hipotecarias y reglamentos de copropiedad se exige el Sello Verde vigente."),
          ("¿Cada cuántos años se renueva la certificación del gas?", "En edificios y condominios residenciales se debe renovar obligatoriamente cada 2 años según la normativa de la SEC."),
          ("¿Qué artefactos revisan en la certificación?", "Calefones, calderas, cocinas, encimeras, estufas fijas y la red completa de cañerías."),
          ("¿Ustedes tramitan directamente con Metrogas o Lipigas?", "Sí, emitimos los documentos técnicos formales necesarios para solicitar el retiro de sellos y reposición del medidor."),
          ("¿Puedo verificar la licencia del técnico en la SEC?", "Sí, todos nuestros técnicos cuentan con credencial con código QR y registro público verificable en sec.cl."),
          ("¿Cómo agendar una visita de inspección SEC?", "Contáctenos vía WhatsApp al +56 9 4987 7316 para coordinar la visita de un instalador acreditado.")
        ]
    },

    # 6. Core: Emergencias 24/7
    {
        "slug": "emergencias-24-7",
        "title": "🚨 Emergencias Fugas de Gas 24/7 【 Gásfiter SEC Atención Inmediata Chile 】✔️",
        "meta_desc": "Atención de urgencia 24 horas por fuga de gas, olor a gas y corte de medidor en Santiago y comunas. Técnicos certificados SEC de turno inmediato. Llamar: +56 9 4987 7316.",
        "h1": "Atención de <span class='highlight-red'>Emergencias por Fugas de Gas</span> 24 Horas",
        "hero_badge": "🚨 CUADRILLAS TÉCNICAS DISPONIBLES AHORA • TURNO 24/7",
        "intro": "Respuesta inmediata ante olor a gas, medidores cortados por la compañía o alarmas activadas. Técnicos autorizados SEC listos para desplazarse a su hogar o empresa en cualquier momento del día o la noche.",
        "breadcrumb_name": "Emergencias 24/7",
        "service_focus": "Corte de suministro, presurización urgente y diagnóstico express en toda la RM.",
        "specific_content": """
        <h2>Respuesta Inmediata Ante Emergencias de Gas: Su Seguridad es Primero</h2>
        <p>Una fuga de gas no puede esperar al día siguiente. El gas licuado (más pesado que el aire) se acumula en el suelo y el gas natural en techos, creando atmósferas explosivas con una simple chispa de un interruptor eléctrico.</p>
        <p>Nuestras unidades móviles de emergencia cuentan con detectores de gas por ionización, manómetros digitales certificados y herramientas de sellado rápido para neutralizar el peligro en el menor tiempo posible.</p>
        """,
        "faqs": [
          ("¿Qué debo hacer si siento fuerte olor a gas ahora mismo?", "1. Cierre la llave general de gas. 2. Ventile abriendo puertas y ventanas. 3. No encienda luces ni fósforos. 4. Evacúe y llámenos al +56 9 4987 7316."),
          ("¿Cuánto tardan en llegar ante una emergencia en Santiago?", "Dependiendo de la comuna y el tráfico, nuestras cuadrillas móviles llegan habitualmente en un plazo de 30 a 60 minutos."),
          ("¿Atienden de noche y en días festivos?", "Sí, mantenemos personal técnico de guardia las 24 horas del día, los 365 días del año sin interrupciones."),
          ("¿Qué costo tiene la visita de emergencia?", "El técnico le informará el costo de la visita diagnóstica antes de concurrir y cotizará la solución inmediata en el lugar."),
          ("¿Pueden reponer el servicio si Metrogas retiró el medidor?", "Efectuamos la reparación, certificamos la hermeticidad y tramitamos la solicitud de reposición de medidor ante Metrogas o Gasco."),
          ("¿Llevan repuestos y materiales en el vehículo?", "Sí, nuestras camionetas están equipadas como talleres móviles con fittings, sellante Prodoral, cañerías y detectores de fuga."),
          ("¿Trabajan con gas licuado en cilindro o tanque a granel?", "Sí, atendemos instalaciones con cilindros de 45 kg, estanques a granel de Lipigas/Abastible y redes urbanas de gas natural."),
          ("¿Cómo se paga el servicio de emergencia?", "Aceptamos transferencias electrónicas bancarias, tarjetas de débito/crédito y efectivo."),
          ("¿Emiten boleta o factura de la empresa?", "Sí, emitimos boletas y facturas electrónicas válidas con todos los datos legales."),
          ("¿Cuál es el teléfono directo de emergencias?", "Llámenos de inmediato al +56 9 4987 7316 o abra nuestro chat directo de WhatsApp.")
        ]
    },

    # 7. Indexed Core: fuga-de-gas
    {
        "slug": "fuga-de-gas",
        "title": "▷ Fuga de Gas 【 Detección & Sellado No Invasivo • Gasfiter SEC Chile 】✔️",
        "meta_desc": "Solución técnica integral a fugas de gas licuado y natural. Detección electrónica y sellado con Prodoral R6-1 en Santiago y RM. Atención 24/7 al WhatsApp: +56 9 4987 7316.",
        "h1": "Solución Definitiva a <span class='highlight-red'>Fugas de Gas</span> en Santiago y Regiones",
        "hero_badge": "🔥 ESPECIALISTAS CERTIFICADOS EN REDES DE GAS CHILE",
        "intro": "Detección milimétrica y reparación no invasiva de fugas de gas en cañerías empotradas y subterráneas. Cumplimiento estricto del Decreto Supremo Nº 66 con instaladores acreditados SEC.",
        "breadcrumb_name": "Fuga de Gas",
        "service_focus": "Detección, diagnóstico manométrico y sellado interno de redes de gas.",
        "specific_content": "<h2>Servicio Especializado en Fugas de Gas Domiciliarias e Industriales</h2><p>Las redes de gas sufren desgaste natural en uniones roscadas, corrosión galvánica y microfisuras por movimientos sísmicos propios de Chile. Diagnosticamos con instrumental certificado y reparamos en tiempo récord con tecnología Prodoral R6-1.</p>",
        "faqs": [
          ("¿Cómo se detecta una fuga de gas en cañerías empotradas?", "Mediante pruebas manométricas de hermeticidad y equipos de detección electrónica y gas trazador sin romper muros."),
          ("¿Qué tipo de gas reparan?", "Reparamos redes de gas natural por cañería y gas licuado de petróleo (GLP) a granel o cilindros."),
          ("¿Por qué es mejor reparar con Prodoral que cambiar cañerías?", "Porque evita demoler pisos y cerámicas, ahorra semanas de obra y reduce el costo total a la mitad."),
          ("¿El técnico entrega certificado SEC al terminar?", "Sí, entregamos el informe técnico con el código de instalador autorizado SEC."),
          ("¿Tienen cobertura en toda la Región Metropolitana?", "Sí, cubrimos todas las comunas de Santiago y zonas aledañas.")
        ]
    },

    # 8. Indexed: fuga-de-gas-deteccion
    {
        "slug": "fuga-de-gas-deteccion",
        "title": "▷ Detección de Fugas de Gas 【 Diagnóstico Electrónico de Hermeticidad SEC 】✔️",
        "meta_desc": "Diagnóstico y detección electrónica de fugas de gas en cañerías empotradas y subterráneas. Equipos manométricos de alta precisión en RM. Tel: +56 9 4987 7316.",
        "h1": "Detección de <span class='highlight-red'>Fugas de Gas</span> con Diagnóstico Electrónico",
        "hero_badge": "🔍 DIAGNÓSTICO MANOMÉTRICO DIGITAL CERTIFICADO",
        "intro": "Inspeccionamos su red de gas con manómetros digitales de alta sensibilidad y detectores olfativos electrónicos capaces de registrar concentraciones mínimas de gas antes de que representen un peligro.",
        "breadcrumb_name": "Detección de Fugas de Gas",
        "service_focus": "Localización precisa de pérdidas de gas con instrumental certificado.",
        "specific_content": "<h2>Equipamiento Tecnológico de Detección de Fugas</h2><p>No pierda tiempo ni dinero adivinando dónde está la fuga. Nuestro equipamiento de diagnóstico evalúa la caída de presión en milibares conforme a la norma SEC, indicando con precisión la gravedad de la fuga y la solución más conveniente.</p>",
        "faqs": [
          ("¿Cómo funciona un detector electrónico de gas?", "Utiliza un sensor semiconductor que reacciona a los hidrocarburos (metano y propano) emitiendo una alarma acústica y visual con el nivel de concentración PPM."),
          ("¿Qué es la prueba de hermeticidad?", "Es una prueba de presión controlada que se realiza con aire inerte en la cañería para comprobar que no existan pérdidas."),
          ("¿Cuánto demora una detección?", "Aproximadamente entre 1 y 2 horas."),
          ("¿Se puede detectar una fuga detrás de un mueble de cocina?", "Sí, nuestros sensores cuentan con sondas flexibles que alcanzan rincones difíciles sin desmontar el mobiliario.")
        ]
    },

    # 9. Indexed: aplicacion-de-prodoral-para-fuga-de-gas
    {
        "slug": "aplicacion-de-prodoral-para-fuga-de-gas",
        "title": "▷ Aplicación de Prodoral para Fuga de Gas 【 Servicio Técnico Certificado 】✔️",
        "meta_desc": "Procedimiento profesional de inyección y aplicación de sellante alemán Prodoral R6-1 para redes de gas en Chile. 100% garantizado. WhatsApp: +56 9 4987 7316.",
        "h1": "Aplicación Profesional de <span class='highlight-red'>Prodoral R6-1</span> para Fugas de Gas",
        "hero_badge": "🇩🇪 PROTOCOLO TÉCNICO OFICIAL DE APLICACIÓN",
        "intro": "La correcta aplicación de Prodoral R6-1 exige un protocolo técnico riguroso de limpieza previa, bombeo presurizado y secado por aire filtrado. Confíe en técnicos capacitados con amplia experiencia en Chile.",
        "breadcrumb_name": "Aplicación de Prodoral",
        "service_focus": "Inyección controlada de sellante polimérico en ductos de gas.",
        "specific_content": "<h2>El Estándar Técnico de Inyección Prodoral R6-1</h2><p>Aplicar Prodoral requiere equipos especiales de bombeo de diafragma y reguladores de presión. Nuestro procedimiento garantiza que el polímero penetre en todas las uniones de la red sin generar sedimentos ni obstrucciones en artefactos de consumo.</p>",
        "faqs": [
          ("¿Por qué debe aplicarlo un técnico especializado?", "Porque requiere calibración exacta de la presión de inyección y extracción completa del remanente mediante raspadores o soplado de aire."),
          ("¿Se limpian las cañerías antes de inyectar?", "Sí, se efectúa un barrido previo con aire para eliminar cualquier residuo de polvo o grasa."),
          ("¿Qué garantía tiene la aplicación?", "Garantía total por escrito de estanqueidad y hermeticidad de la red.")
        ]
    },

    # 10. Indexed: gasfiter-sec-especialista-en-fuga-de-gas
    {
        "slug": "gasfiter-sec-especialista-en-fuga-de-gas",
        "title": "▷ Gásfiter SEC Especialista en Fugas de Gas 【 Instalador Certificado Chile 】✔️",
        "meta_desc": "Contrate un gásfiter certificado por la SEC para reparar su fuga de gas con total seguridad y respaldo legal. Atención 24 horas en Santiago. Tel: +56 9 4987 7316.",
        "h1": "Gásfiter SEC <span class='highlight-red'>Especialista en Fugas de Gas</span> Autorizado",
        "hero_badge": "👨‍🔧 INSTALADORES AUTORIZADOS POR LA SUPERINTENDENCIA SEC",
        "intro": "Un problema de gas en su hogar solo debe ser intervenido por profesionales con licencia vigente de la SEC. Evite riesgos graves y asegure la aprobación de su Sello Verde.",
        "breadcrumb_name": "Gásfiter SEC Especialista",
        "service_focus": "Instaladores autorizados SEC con carnet escaneable por QR.",
        "specific_content": "<h2>Seguridad y Respaldo Legal con Instaladores SEC</h2><p>La manipulación de gas licuado o natural sin certificación es una infracción a la ley chilena que anula coberturas de seguro contra incendios. Nuestros técnicos cuentan con credencial oficial y amplia trayectoria en el rubro.</p>",
        "faqs": [
          ("¿Qué clases de instalador SEC existen?", "Clase 1 (sin límite de potencia), Clase 2 (hasta 60 kW) y Clase 3 (redes residenciales). Nuestros técnicos cubren todas las categorías."),
          ("¿Puedo exigir ver la credencial del gásfiter?", "Absolutamente. Nuestros técnicos portan su credencial física con código QR verificable ante la SEC.")
        ]
    },

    # 11. Indexed: fuga-de-gas-gasfiter-certificado-en-fugas-de-gas
    {
        "slug": "fuga-de-gas-gasfiter-certificado-en-fugas-de-gas",
        "title": "▷ Gásfiter Certificado en Fugas de Gas 【 Atención Rápida a Domicilio 】✔️",
        "meta_desc": "Técnicos certificados en cañerías de cobre, PEX, acero y HDPE. Detección y sellado de fugas en toda la Región Metropolitana. WhatsApp: +56 9 4987 7316.",
        "h1": "Gásfiter Certificado en <span class='highlight-red'>Reparación de Fugas de Gas</span>",
        "hero_badge": "🛡️ VISITAS A DOMICILIO EN TODA LA REGIÓN METROPOLITANA",
        "intro": "Asistencia técnica inmediata para residencias particulares, comunidades de departamentos y empresas. Reparamos cañerías, llaves de paso y conexiones de gas con certificación oficial.",
        "breadcrumb_name": "Gásfiter Certificado en Fugas",
        "service_focus": "Atención profesional y segura a domicilio en toda la Región Metropolitana.",
        "specific_content": "<h2>Atención Personalizada y Rápida en su Domicilio</h2><p>Contamos con unidades móviles distribuidas estratégicamente por Santiago para llegar a su domicilio en el menor tiempo posible y solucionar cualquier problema de gas de forma definitiva.</p>",
        "faqs": [
          ("¿Qué tipo de cañerías pueden reparar?", "Trabajamos con cañerías de cobre (tipo L y K), acero, polietileno HDPE y sistemas multicapa PEX-Al-PEX."),
          ("¿Emiten comprobante oficial de la intervención?", "Sí, entregamos informe técnico formal de la reparación realizada.")
        ]
    },

    # 12. Indexed: fuga-de-gas-reparamos-fugas-de-gas-sin-romper
    {
        "slug": "fuga-de-gas-reparamos-fugas-de-gas-sin-romper",
        "title": "▷ Reparamos Fugas de Gas Sin Romper 【 Tecnología Prodoral R6-1 】✔️",
        "meta_desc": "Olvídese de picar paredes y pisos. Reparamos microfugas internas de gas en 1 solo día con tecnología alemana de polímero líquido. Tel: +56 9 4987 7316.",
        "h1": "Reparamos Fugas de Gas <span class='highlight-red'>Sin Romper Pisos ni Muros</span>",
        "hero_badge": "🔨 CERO DEMOLICIÓN • CERO ESCOMBROS • CERO POLVO",
        "intro": "No destruya sus cerámicas, parquets ni paredes recién pintadas. Nuestra tecnología de sellado polimérico resuelve la fuga desde el interior de la cañería en pocas horas.",
        "breadcrumb_name": "Reparamos Sin Romper",
        "service_focus": "Reparación limpia y no invasiva de redes de gas empotradas.",
        "specific_content": "<h2>La Alternativa Moderna a la Demolición Tradicional</h2><p>Picar muros para buscar una fuga de gas genera semanas de polvo, suciedad y costos elevados de reposición de cerámicas descontinuadas. Con Prodoral R6-1 su propiedad se mantiene 100% impecable y la red queda sellada con garantía.</p>",
        "faqs": [
          ("¿Es seguro el sellado sin romper?", "Es 100% seguro y cuenta con certificaciones internacionales DVGW de Alemania y validación técnica en Chile."),
          ("¿Cuánto tiempo demora?", "Entre 4 y 6 horas en promedio, listo en el mismo día.")
        ]
    },

    # 13. Indexed: fuga-de-gas-servicio-de-experto-en-fugas-de-gas
    {
        "slug": "fuga-de-gas-servicio-de-experto-en-fugas-de-gas",
        "title": "▷ Servicio de Experto en Fugas de Gas 【 Asistencia Profesional 24/7 】✔️",
        "meta_desc": "Ingeniería y gasfitería especializada en redes de gas natural y gas licuado para casas, edificios y empresas en Chile. WhatsApp directo: +56 9 4987 7316.",
        "h1": "Servicio de <span class='highlight-red'>Experto en Fugas de Gas</span> y Redes Térmicas",
        "hero_badge": "⚙️ ALTA INGENIERÍA EN GASFITERÍA Y SEGURIDAD",
        "intro": "Brindamos consultoría técnica, diagnóstico de hermeticidad y ejecución de obras de reparación de gas para administradores de edificios, industrias y propietarios exigentes.",
        "breadcrumb_name": "Experto en Fugas de Gas",
        "service_focus": "Servicio técnico integral de gas para residencias y comunidades.",
        "specific_content": "<h2>Ingeniería y Seguridad al Servicio de su Comunidad</h2><p>Atendemos comunidades de edificios y condominios que requieren regularizar matrices centrales de gas, salas de calderas y montantes verticales para la certificación del sello verde del edificio.</p>",
        "faqs": [
          ("¿Atienden matrices centrales de edificios?", "Sí, realizamos pruebas de hermeticidad por tramos verticales y horizontales en edificios de departamentos."),
          ("¿Pueden emitir presupuestos para comités de administración?", "Sí, emitimos propuestas formales detalladas para comités de administración y administradores.")
        ]
    },

    # 14. Indexed Commune: Peñalolén
    {
        "slug": "fuga-de-gas-penalolen",
        "title": "▷ Fuga de Gas en Peñalolén 【 Gásfiter SEC Sellado Prodoral 】✔️",
        "meta_desc": "Atención urgente de fugas de gas en Peñalolén (Las Pircas, Consistorial, Tobalaba, Quilín). Gásfiter certificado SEC. Sellado sin romper. Tel: +56 9 4987 7316.",
        "h1": "Detección y Reparación de <span class='highlight-red'>Fugas de Gas en Peñalolén</span>",
        "hero_badge": "📍 COBERTURA RÁPIDA EN PEÑALOLÉN Y COMUNAS DEL ORIENTE",
        "intro": "Cuadrilla móvil permanente en la comuna de Peñalolén para atender emergencias por olor a gas, cortes de suministro y sellado de microfugas sin romper con Prodoral R6-1.",
        "breadcrumb_name": "Peñalolén",
        "service_focus": "Servicio técnico SEC a domicilio en Peñalolén y sectores aledaños.",
        "specific_content": "<h2>Atención Rápida en Todos los Sectores de Peñalolén</h2><p>Cubrimos Las Pircas, Avenida Consistorial, Antupirén, Avenida Tobalaba, El Remanso, Quilín y Peñalolén Alto con instrumental de detección de gas de última generación y sellado no invasivo.</p>",
        "faqs": [
          ("¿Cuánto tardan en llegar a Peñalolén?", "Nuestra unidad del sector oriente suele llegar en un tiempo estimado de 25 a 45 minutos."),
          ("¿Trabajan con gas natural Metrogas en Peñalolén?", "Sí, reparamos redes de gas natural y dejamos la instalación apta para la reposición del medidor.")
        ]
    },

    # 15. Indexed Commune: Pirque
    {
        "slug": "fuga-de-gas-pirque",
        "title": "▷ Fuga de Gas en Pirque 【 Gásfiter Certificado SEC a Domicilio 】✔️",
        "meta_desc": "Detección y sellado de fugas de gas en Pirque (El Principal, Casas Viejas, Santa Rita). Especialistas SEC en gas licuado y estanques. WhatsApp: +56 9 4987 7316.",
        "h1": "Reparación de <span class='highlight-red'>Fugas de Gas en Pirque</span> y Alrededores",
        "hero_badge": "📍 ATENCIÓN ESPECIALIZADA EN PARCELAS Y VIVIENDAS DE PIRQUE",
        "intro": "Expertos en redes de gas licuado a granel (estanques de gas) y cañerías subterráneas en parcelas y condominios de Pirque. Detección con gas trazador y sellado sin romper.",
        "breadcrumb_name": "Pirque",
        "service_focus": "Redes de gas en parcelas, estanques y viviendas en Pirque.",
        "specific_content": "<h2>Solución a Fugas Subterráneas en Parcelas de Pirque</h2><p>En las parcelas de Pirque las cañerías suelen recorrer largas distancias bajo tierra desde el estanque de gas hasta la casa. Localizamos microfugas enterradas con Gas Trazador sin abrir zanjas innecesarias.</p>",
        "faqs": [
          ("¿Atienden parcelas de agrado en Pirque?", "Sí, contamos con equipamiento para inspeccionar líneas extensas de gas subterráneo."),
          ("¿Reparan tanques a granel Lipigas, Gasco o Abastible?", "Efectuamos el diagnóstico y reparación de toda la red desde la salida del regulador del estanque.")
        ]
    },

    # 16. Indexed Commune: Papudo
    {
        "slug": "fuga-de-gas-papudo",
        "title": "▷ Fuga de Gas en Papudo 【 Gásfiter SEC Litoral Norte V Región 】✔️",
        "meta_desc": "Servicio técnico de fugas de gas y agua en Papudo, Punta Puyai y Zapallar. Gásfiter autorizado SEC. Sellado Prodoral sin romper. Llamar: +56 9 4987 7316.",
        "h1": "Especialista en <span class='highlight-red'>Fugas de Gas en Papudo</span> y V Región",
        "hero_badge": "🌊 COBERTURA EN PAPUDO, PUNTA PUYAI Y ZAPALLAR",
        "intro": "Atendemos condominios costeros, casas de verano y departamentos en Papudo y Punta Puyai con servicio de detección y sellado no destructivo de fugas de gas y piscinas.",
        "breadcrumb_name": "Papudo",
        "service_focus": "Servicio de gas y piscinas en condominios y casas de Papudo.",
        "specific_content": "<h2>Servicio Técnico para Casas de Veraneo en Papudo</h2><p>El aire marino y la humedad costera aceleran la corrosión en fittings y uniones de gas en la costa. Dejamos su propiedad de vacaciones segura y certificada con Sello Verde.</p>",
        "faqs": [
          ("¿Atienden departamentos en Punta Puyai?", "Sí, atendemos condominios frente al mar en Papudo y Punta Puyai."),
          ("¿Revisan filtraciones de piscinas en Papudo?", "Sí, realizamos pruebas de presión estanca en piscinas de casas y condominios.")
        ]
    },

    # 17. Indexed Commune: Rancagua
    {
        "slug": "fuga-de-gas-rancagua",
        "title": "▷ Fuga de Gas en Rancagua 【 Gásfiter SEC Machalí & VI Región 】✔️",
        "meta_desc": "Detección y sellado de fugas de gas en Rancagua y Machalí. Técnicos acreditados SEC. Tecnología Prodoral R6-1 sin picar pisos. Tel: +56 9 4987 7316.",
        "h1": "Detección y Reparación de <span class='highlight-red'>Fugas de Gas en Rancagua</span>",
        "hero_badge": "📍 COBERTURA EN RANCAGUA, MACHALÍ Y VI REGIÓN",
        "intro": "Instaladores autorizados SEC para la ciudad de Rancagua y Machalí. Solución limpia a filtraciones de gas en cañerías empotradas y redes de agua potable.",
        "breadcrumb_name": "Rancagua",
        "service_focus": "Atención técnica SEC en Rancagua, Machalí y alrededores.",
        "specific_content": "<h2>Servicio Certificado para la Región de O'Higgins</h2><p>Ofrecemos servicio a condominios de Carretera del Cobre, Machalí, centro de Rancagua y zonas residenciales con certificación SEC y tecnología alemana Prodoral R6-1.</p>",
        "faqs": [
          ("¿Tienen cobertura en Machalí?", "Sí, atendemos frecuentemente condominios en Machalí y Rancagua oriente."),
          ("¿Trabajan con empresas e industrias en Rancagua?", "Sí, prestamos servicio a comercios, restaurantes e industrias de la zona.")
        ]
    },

    # 18. Indexed Commune: Paine
    {
        "slug": "fuga-de-gas-paine",
        "title": "▷ Fuga de Gas en Paine 【 Gásfiter SEC Buin & Parcelas 】✔️",
        "meta_desc": "Detección y reparación de fugas de gas en Paine, Champa, Huelquén y Buin. Gásfiter autorizado SEC. Sellado sin romper muros. WhatsApp: +56 9 4987 7316.",
        "h1": "Reparación de <span class='highlight-red'>Fugas de Gas en Paine</span> y Buin",
        "hero_badge": "📍 COBERTURA EN PAINE, BUIN, CHAMPA Y HUELQUÉN",
        "intro": "Especialistas en redes de gas para parcelas, condominios y viviendas en Paine y Buin. Sellado con Prodoral R6-1 y detección subterránea con gas trazador.",
        "breadcrumb_name": "Paine",
        "service_focus": "Servicio técnico integral de gas en la zona sur de Santiago.",
        "specific_content": "<h2>Servicio para Parcelas y Viviendas en Paine</h2><p>Inspeccionamos redes de gas GLP en cilindro o granel, cañerías bajo radier y redes de riego en parcelaciones de Paine y Buin.</p>",
        "faqs": [
          ("¿Atienden sectores rurales de Paine?", "Sí, cubrimos Champa, Rangue, Huelquén, Viluco y alrededores de Paine."),
          ("¿Qué tipo de cañería instalan o reparan?", "Reparamos cañerías de cobre, PEX y HDPE con soldadura certificada.")
        ]
    },

    # 19. Indexed Commune: Chicureo
    {
        "slug": "fuga-de-gas-la-chicureo",
        "title": "▷ Fuga de Gas en Chicureo 【 Gásfiter SEC Colina & Piedra Roja 】✔️",
        "meta_desc": "Especialistas en fugas de gas en Chicureo (Piedra Roja, Chamisero, Las Brisas, Santa Elena). Sellado Prodoral R6-1 sin romper. WhatsApp: +56 9 4987 7316.",
        "h1": "Detección y Sellado de <span class='highlight-red'>Fugas de Gas en Chicureo</span>",
        "hero_badge": "📍 ATENCIÓN EXPRESS EN CHICUREO, CHAMISERO Y PIEDRA ROJA",
        "intro": "Atención prioritaria para condominios de Chicureo y Colina. Sellado de microfugas de gas sin romper baldosas ni muros finos con polímero alemán Prodoral R6-1.",
        "breadcrumb_name": "Chicureo / Colina",
        "service_focus": "Condominios residenciales de alto estándar en Chicureo.",
        "specific_content": "<h2>Protegemos la Estética y los Acabados de su Hogar en Chicureo</h2><p>En condominios como Piedra Roja, Chamisero, Las Brisas de Chicureo y Santa Elena, romper pisos de porcelanato importado o radieres significa un costo enorme. Con Prodoral R6-1 la fuga se sella desde adentro en un solo día sin tocar sus terminaciones.</p>",
        "faqs": [
          ("¿Tienen técnicos disponibles para Chicureo?", "Sí, mantenemos unidades operativas que cubren la zona norte y nororiente de Santiago."),
          ("¿Atienden filtraciones en piscinas de condominios en Chicureo?", "Sí, disponemos de equipos para detección estanca en piscinas de fibra y hormigón.")
        ]
    },

    # 20. Indexed Commune: Quinta Normal
    {
        "slug": "fuga-de-gas-quinta-normal",
        "title": "▷ Fuga de Gas en Quinta Normal 【 Gásfiter Certificado SEC 24/7 】✔️",
        "meta_desc": "Reparación de fugas de gas en Quinta Normal (Carrascal, Matucana, Mapocho). Gásfiter autorizado SEC. Sello Verde y sellado sin romper. Tel: +56 9 4987 7316.",
        "h1": "Reparación de <span class='highlight-red'>Fugas de Gas en Quinta Normal</span>",
        "hero_badge": "📍 COBERTURA INMEDIATA EN QUINTA NORMAL Y SANTIAGO PONIENTE",
        "intro": "Servicio de gasfitería certificada SEC en Quinta Normal para casas antiguas, edificios y locales comerciales. Solución limpia de fugas sin picar pisos.",
        "breadcrumb_name": "Quinta Normal",
        "service_focus": "Detección y sellado SEC a domicilio en Quinta Normal.",
        "specific_content": "<h2>Servicio Especializado para Viviendas de Quinta Normal</h2><p>Las redes de gas antiguas de cañería de fierro galvanizado o cobre envejecido en Quinta Normal pueden presentar porosidades. El sellado Prodoral R6-1 renueva la hermeticidad de toda la matriz sin demolición.</p>",
        "faqs": [
          ("¿Atienden casas antiguas en Quinta Normal?", "Sí, contamos con amplia experiencia en normalización de redes de gas antiguas."),
          ("¿Cuánto demora la atención en Quinta Normal?", "Llegamos habitualmente en 30 a 45 minutos ante emergencias.")
        ]
    },

    # 21. Indexed Commune: Puente Alto
    {
        "slug": "fuga-de-gas-puente-alto",
        "title": "▷ Fuga de Gas en Puente Alto 【 Gásfiter SEC Ciudad del Este & Las Vizcachas 】✔️",
        "meta_desc": "Urgencias por fuga de gas en Puente Alto (Ciudad del Este, Las Vizcachas, Vicuña Mackenna). Instalador autorizado SEC. WhatsApp: +56 9 4987 7316.",
        "h1": "Detección y Reparación de <span class='highlight-red'>Fugas de Gas en Puente Alto</span>",
        "hero_badge": "📍 ATENCIÓN RÁPIDA EN PUENTE ALTO Y CORDILLERA",
        "intro": "Cuadrillas técnicas para casas y condominios en Puente Alto. Sellado no invasivo con Prodoral R6-1, detección de gas trazador y certificación Sello Verde SEC.",
        "breadcrumb_name": "Puente Alto",
        "service_focus": "Servicio de gasfitería autorizada SEC en la comuna de Puente Alto.",
        "specific_content": "<h2>Cobertura Total en Puente Alto</h2><p>Atendemos sectores como Ciudad del Este, Las Vizcachas, Los Toros, San Carlos, La Florida sur y todo el eje de Vicuña Mackenna con atención 24 horas.</p>",
        "faqs": [
          ("¿Qué hago si Metrogas me cortó el gas en Puente Alto?", "Llámenos al +56 9 4987 7316. Realizamos la prueba, sellamos la red y entregamos el informe para la reconexión."),
          ("¿Tienen atención los fines de semana en Puente Alto?", "Sí, atendemos emergencias de lunes a domingo las 24 horas.")
        ]
    },

    # 22. Indexed Commune: María Pinto
    {
        "slug": "fuga-de-gas-maria-pinto",
        "title": "▷ Fuga de Gas en María Pinto 【 Gásfiter SEC Curacaví & Melipilla 】✔️",
        "meta_desc": "Atención técnica de fugas de gas y agua en María Pinto, Curacaví y zona rural poniente. Gásfiter autorizado SEC. WhatsApp: +56 9 4987 7316.",
        "h1": "Servicio de <span class='highlight-red'>Fugas de Gas en María Pinto</span>",
        "hero_badge": "📍 COBERTURA EN MARÍA PINTO, CURACAVÍ Y MELIPILLA",
        "intro": "Especialistas en redes de gas licuado en parcelas y sectores rurales de María Pinto. Diagnóstico de hermeticidad manométrica y sellado no destructivo.",
        "breadcrumb_name": "María Pinto",
        "service_focus": "Redes de gas en parcelas y sectores rurales de María Pinto.",
        "specific_content": "<h2>Atención de Parcelas en María Pinto</h2><p>Revisamos estanques de gas, calefones solares y cañerías subterráneas en parcelaciones de agrado de María Pinto y alrededores con instrumental móvil de precisión.</p>",
        "faqs": [
          ("¿Llegan a parcelas apartadas en María Pinto?", "Sí, coordinamos visitas técnicas a parcelas de agrado y fundos en la comuna."),
          ("¿Qué hago si hay olor a gas en el estanque?", "Cierre la válvula de servicio del tanque y contáctenos para una revisión inmediata.")
        ]
    },

    # 23. Indexed Commune: San Bernardo
    {
        "slug": "fuga-de-gas-san-bernardo",
        "title": "▷ Fuga de Gas en San Bernardo 【 Gásfiter SEC Nos & Calera de Tango 】✔️",
        "meta_desc": "Detección y sellado de fugas de gas en San Bernardo (Nos, Lo Herrera, Portada Sur). Gásfiter certificado SEC. Atención 24/7. Tel: +56 9 4987 7316.",
        "h1": "Reparación de <span class='highlight-red'>Fugas de Gas en San Bernardo</span>",
        "hero_badge": "📍 COBERTURA EN SAN BERNARDO, NOS Y CALERA DE TANGO",
        "intro": "Servicio de gasfitería certificada SEC en San Bernardo para casas particulares, condominios en Nos y empresas del sector sur de Santiago. Sellado sin romper.",
        "breadcrumb_name": "San Bernardo",
        "service_focus": "Servicio SEC en San Bernardo y sectores aledaños.",
        "specific_content": "<h2>Atención Rápida en Todo San Bernardo</h2><p>Cubrimos Nos, Los Morros, Avenida Portales, Ochagavía, Lo Herrera y Calera de Tango con cuadrillas móviles disponibles 24/7.</p>",
        "faqs": [
          ("¿Atienden emergencias nocturnas en San Bernardo?", "Sí, disponemos de turno de emergencia permanente."),
          ("¿Reparan fugas en cocinas y calefones?", "Sí, realizamos reparación de cañerías de alimentación y artefactos.")
        ]
    },

    # 24. Indexed Commune: San Joaquín
    {
        "slug": "fuga-de-gas-san-joaquin",
        "title": "▷ Fuga de Gas en San Joaquín 【 Gásfiter Autorizado SEC 24 Horas 】✔️",
        "meta_desc": "Solución a fugas de gas en San Joaquín (Carlos Valdovinos, Las Industrias, Santa Rosa). Gásfiter SEC. Sellado Prodoral sin romper. WhatsApp: +56 9 4987 7316.",
        "h1": "Detección y Reparación de <span class='highlight-red'>Fugas de Gas en San Joaquín</span>",
        "hero_badge": "📍 COBERTURA INMEDIATA EN SAN JOAQUÍN Y SANTIAGO SUR",
        "intro": "Técnicos autorizados SEC para viviendas, edificios residenciales e industrias en la comuna de San Joaquín. Detección electrónica y sellado no invasivo.",
        "breadcrumb_name": "San Joaquín",
        "service_focus": "Servicio técnico a domicilio en la comuna de San Joaquín.",
        "specific_content": "<h2>Servicio Residencial e Industrial en San Joaquín</h2><p>Atendemos emergencias de gas en los sectores residenciales y el cordón industrial de San Joaquín con estricto apego a las normas de seguridad de la SEC.</p>",
        "faqs": [
          ("¿Trabajan con redes comerciales en San Joaquín?", "Sí, realizamos pruebas de hermeticidad y sellado en locales gastronómicos e industrias."),
          ("¿Cuánto tardan en acudir a una emergencia en San Joaquín?", "Llegamos en aproximadamente 30 minutos.")
        ]
    },

    # 25. New Commune: Las Condes
    {
        "slug": "fuga-de-gas-las-condes",
        "title": "▷ Fuga de Gas en Las Condes 【 Gásfiter SEC San Damián & El Golf 】✔️",
        "meta_desc": "Detección y sellado de fugas de gas en Las Condes (El Golf, San Damián, Los Dominicos). Gásfiter autorizado SEC. Sin picar muros ni baldosas. Tel: +56 9 4987 7316.",
        "h1": "Detección y Sellado de <span class='highlight-red'>Fugas de Gas en Las Condes</span>",
        "hero_badge": "📍 ATENCIÓN EXPRESS EN LAS CONDES • TÉCNICOS AUTORIZADOS SEC",
        "intro": "Servicio de urgencia para casas y departamentos en Las Condes. Solución definitiva a fugas de gas sin picar muros ni baldosas mediante tecnología alemana Prodoral R6-1 y detección con gas trazador.",
        "breadcrumb_name": "Las Condes",
        "service_focus": "Servicio técnico SEC de alta precisión en viviendas y edificios de Las Condes.",
        "specific_content": "<h2>Servicio Técnico de Alta Precisión para Las Condes</h2><p>En Las Condes, demoler muros o levantar pisos de madera noble, porcelanatos o mármol para buscar una fuga de gas genera daños patrimoniales cuantiosos. En <strong>Especialista en Fugas</strong> utilizamos tecnología de localización acústica con geófonos, gas trazador (Formigas) y sellado polimérico alemán <strong>Prodoral R6-1</strong>.</p><p>Cubrimos con rapidez El Golf, San Damián, San Carlos de Apoquindo, Los Dominicos, Manquehue, Estoril y Avenida Las Condes, restableciendo la hermeticidad de la red en el mismo día con certificación reglamentaria SEC.</p>",
        "faqs": [
          ("¿Cuánto tardan en llegar a una emergencia en Las Condes?", "Nuestra cuadrilla asignada a la zona oriente arriba habitualmente en un lapso de 25 a 40 minutos."),
          ("¿Qué ocurre si Metrogas retiró el medidor en mi departamento de Las Condes?", "Efectuamos el sellado sin demoler, realizamos la prueba manométrica oficial y extendemos el certificado técnico SEC para que Metrogas reactive el suministro con urgencia."),
          ("¿El sellado Prodoral daña las terminaciones de mi vivienda?", "No. El producto se inyecta directamente por las cañerías existentes sin picar paredes ni romper pisos.")
        ]
    },

    # 26. New Commune: Providencia
    {
        "slug": "fuga-de-gas-providencia",
        "title": "▷ Fuga de Gas en Providencia 【 Gásfiter SEC Los Leones & Pedro de Valdivia 】✔️",
        "meta_desc": "Reparación y detección de fugas de gas en Providencia (Los Leones, Pedro de Valdivia, Pocuro). Gásfiter SEC. Sellado Prodoral sin romper. Tel: +56 9 4987 7316.",
        "h1": "Detección y Reparación de <span class='highlight-red'>Fugas de Gas en Providencia</span>",
        "hero_badge": "📍 COBERTURA INMEDIATA EN PROVIDENCIA • INSTALADORES SEC",
        "intro": "Atención especializada para edificios residenciales, departamentos y casas en Providencia. Sellado de microfugas de gas sin romper muros ni shafts comunitarios con polímero alemán Prodoral R6-1.",
        "breadcrumb_name": "Providencia",
        "service_focus": "Detección y sellado de fugas en edificios y casas de Providencia.",
        "specific_content": "<h2>Expertos en Edificios Residenciales y Casas Patrimoniales de Providencia</h2><p>Providencia concentra una gran cantidad de edificios residenciales de media y gran altura, además de construcciones patrimoniales y locales gastronómicos en barrios como Manuel Montt, Bellavista y Barrio Italia. Una microfuga en shafts o ductos comunes puede provocar el corte inmediato de todo el suministro.</p><p>Aplicamos sellado interno con Prodoral R6-1, evitando picar losas comunitarias o muros estructurales, y gestionamos la regularización ante Metrogas con instaladores autorizados SEC de clase superior.</p>",
        "faqs": [
          ("¿Atienden edificios comunitarios y shafts de gas en Providencia?", "Sí, trabajamos habitualmente con comités de administración y administradores de edificios en Providencia, emitiendo cotizaciones y facturas formales."),
          ("¿Cuánto tiempo toma normalizar una fuga de gas en un departamento?", "El diagnóstico y sellado polimérico se completa en una sola jornada de 4 a 6 horas."),
          ("¿Cuentan con atención de emergencias los fines de semana en Providencia?", "Sí, nuestro servicio de guardia técnica funciona las 24 horas del día, los 7 días de la semana.")
        ]
    },

    # 27. New Commune: Vitacura
    {
        "slug": "fuga-de-gas-vitacura",
        "title": "▷ Fuga de Gas en Vitacura 【 Gásfiter SEC Lo Curro & Jardín del Este 】✔️",
        "meta_desc": "Sellado no destructivo y detección de fugas de gas en Vitacura (Lo Curro, Santa María de Manquehue, Tabancura). Instalador SEC. Tel: +56 9 4987 7316.",
        "h1": "Detección y Sellado de <span class='highlight-red'>Fugas de Gas en Vitacura</span>",
        "hero_badge": "📍 SERVICIO TÉCNICO PREMIUM EN VITACURA • AUTORIZADO SEC",
        "intro": "Servicio de alta exigencia para residencias y departamentos en Vitacura. Reparamos microfugas sin dañar acabados de lujo, baldosas ni pisos flotantes mediante tecnología Prodoral R6-1.",
        "breadcrumb_name": "Vitacura",
        "service_focus": "Servicio técnico SEC de alta gama en la comuna de Vitacura.",
        "specific_content": "<h2>Cero Roturas de Acabados Exclusivos en Vitacura</h2><p>En residencias de Lo Curro, Santa María de Manquehue, Jardín del Este y Tabancura, las redes de gas suelen recorrer losas radiantes, tabiquerías finas y terrazas con pavimentos importados. Romper a ciegas para encontrar una fisura es una alternativa costosa y desproporcionada.</p><p>En <strong>Especialista en Fugas</strong> garantizamos la recuperación de la hermeticidad total inyectando Prodoral R6-1 por el interior de la tubería. Además, disponemos de gas trazador no inflamable para localizar filtraciones complejas en jardines y matrices enterradas.</p>",
        "faqs": [
          ("¿Pueden intervenir cañerías bajo losas o pisos de mármol en Vitacura sin picar?", "Efectivamente. Con Prodoral R6-1 la reparación se hace 100% por el interior de la cañería sin tocar revestimientos ni pisos."),
          ("¿Cuánto tardan en acudir a una emergencia en Vitacura?", "El equipo técnico para Vitacura tiene un tiempo de arribo preferente de 25 a 35 minutos."),
          ("¿Emiten certificados oficiales para Metrogas en Vitacura?", "Sí, realizamos la prueba manométrica oficial y emitimos el formulario SEC correspondiente para la reapertura del medidor.")
        ]
    },

    # 28. New Commune: Lo Barnechea
    {
        "slug": "fuga-de-gas-lo-barnechea",
        "title": "▷ Fuga de Gas en Lo Barnechea 【 Gásfiter SEC La Dehesa & Trapenses 】✔️",
        "meta_desc": "Servicio de urgencia por fuga de gas en Lo Barnechea (La Dehesa, Los Trapenses, El Arrayán). Gásfiter autorizado SEC. Prodoral R6-1 sin romper. Tel: +56 9 4987 7316.",
        "h1": "Detección y Sellado de <span class='highlight-red'>Fugas de Gas en Lo Barnechea</span>",
        "hero_badge": "📍 COBERTURA EN LA DEHESA, LOS TRAPENSES Y EL ARRAYÁN",
        "intro": "Atención especializada para residencias de alto metraje y parcelas en Lo Barnechea. Localización milimétrica con gas trazador y sellado hermético definitivo sin obras civiles.",
        "breadcrumb_name": "Lo Barnechea",
        "service_focus": "Servicio técnico SEC especializado en residencias y parcelas de Lo Barnechea.",
        "specific_content": "<h2>Soluciones Avanzadas para Grandes Residencias y Parcelas de Lo Barnechea</h2><p>En sectores como La Dehesa, Los Trapenses, Valle Escondido y El Arrayán, las instalaciones de gas comprenden extensas redes bajo radier, cañerías empotradas y tanques de gas a granel o conexiones directas a Gas Natural. Una caída de presión en estos circuitos requiere instrumental diagnóstico de alta gama.</p><p>Nuestros técnicos autorizados SEC emplean geófonos digitales, detectores de hidrógenos Formigas y el método de sellado polimérico alemán para subsanar microfugas sin alterar jardines ni estructuras.</p>",
        "faqs": [
          ("¿Atienden parcelas y condominios en El Arrayán y Los Trapenses?", "Sí, cubrimos toda la comuna de Lo Barnechea con vehículos equipados con instrumental móvil avanzado."),
          ("¿Detectan fugas en estanques de gas licuado a granel?", "Sí, revisamos la matriz completa desde la llave de salida del tanque hasta cada artefacto receptor."),
          ("¿Qué garantía entregan por el sellado de cañerías?", "Otorgamos garantía escrita y certificamos la hermeticidad con manómetros calibrados ante la SEC.")
        ]
    },

    # 29. New Commune: Ñuñoa
    {
        "slug": "fuga-de-gas-nunoa",
        "title": "▷ Fuga de Gas en Ñuñoa 【 Gásfiter SEC Plaza Ñuñoa & Irarrázaval 】✔️",
        "meta_desc": "Reparación y detección de fugas de gas en Ñuñoa (Plaza Ñuñoa, Irarrázaval, Simón Bolívar). Gásfiter SEC. Sello Verde y sellado sin picar. Tel: +56 9 4987 7316.",
        "h1": "Detección y Reparación de <span class='highlight-red'>Fugas de Gas en Ñuñoa</span>",
        "hero_badge": "📍 ATENCIÓN RÁPIDA EN ÑUÑOA • INSTALADOR AUTORIZADO SEC",
        "intro": "Servicio técnico express para viviendas y torres de departamentos en Ñuñoa. Regularización urgente de Sello Rojo, pruebas manométricas y sellado sin romper con Prodoral R6-1.",
        "breadcrumb_name": "Ñuñoa",
        "service_focus": "Normalización y sellado SEC a domicilio en la comuna de Ñuñoa.",
        "specific_content": "<h2>Diagnóstico y Reparación Limpia de Fugas en Casas y Edificios de Ñuñoa</h2><p>Ñuñoa combina barrios residenciales clásicos con un gran auge de torres de departamentos a lo largo de Irarrázaval, Grecia y Avenida José Pedro Alessandri. Las inspecciones periódicas de Sello Verde frecuentemente arrojan rechazos por caídas de presión en cañerías embutidas.</p><p>Con nuestro sistema de inyección Prodoral R6-1, eliminamos las pérdidas microscópicas de gas en un solo día sin generar ruidos molestos, escombros ni polvo, garantizando la aprobación inmediata ante la SEC.</p>",
        "faqs": [
          ("¿Qué solución ofrecen si mi departamento en Ñuñoa quedó con Sello Rojo?", "Realizamos la detección exacta de la fuga, la sellamos con Prodoral R6-1 y gestionamos la nueva inspección para obtener el Sello Verde."),
          ("¿Cuánto tardan en atender un aviso en Ñuñoa?", "Estamos a 20-30 minutos de distancia en todo el radio urbano de Ñuñoa."),
          ("¿Reparan fugas en calefones e instalaciones de cocina?", "Sí, reparamos uniones, llaves de paso y cañerías de cobre o fierro con certificación oficial.")
        ]
    },

    # 30. New Commune: La Reina
    {
        "slug": "fuga-de-gas-la-reina",
        "title": "▷ Fuga de Gas en La Reina 【 Gásfiter SEC La Reina Alta & Príncipe de Gales 】✔️",
        "meta_desc": "Detección y sellado de fugas de gas en La Reina (Príncipe de Gales, La Reina Alta, Larraín). Gásfiter autorizado SEC. Sin romper pisos. Tel: +56 9 4987 7316.",
        "h1": "Reparación y Sellado de <span class='highlight-red'>Fugas de Gas en La Reina</span>",
        "hero_badge": "📍 COBERTURA TÉCNICA EN LA REINA Y PRECORDILLERA",
        "intro": "Instaladores autorizados SEC para casas y condominios familiares en La Reina. Localización de fugas bajo radier y sellado polimérico garantizado sin obras de demolición.",
        "breadcrumb_name": "La Reina",
        "service_focus": "Servicio técnico SEC integral en la comuna de La Reina.",
        "specific_content": "<h2>Servicio Especializado para Viviendas Familiares en La Reina</h2><p>En La Reina, las viviendas suelen contar con amplios terrenos, redes de agua y gas que pasan bajo radieres de terrazas y calefacciones centrales con calderas. Una pérdida de presión puede pasar desapercibida hasta que el olor se vuelve persistente o la cuenta mensual de Metrogas se dispara.</p><p>Intervenimos con equipos de gas trazador de extrema sensibilidad y aplicamos sellado interno Prodoral R6-1 para proteger la integridad de su casa y evitar costosas obras de albañilería.</p>",
        "faqs": [
          ("¿Atienden emergencias en La Reina Alta y precordillera?", "Sí, atendemos condominios y casas en toda la comuna de La Reina de lunes a domingo."),
          ("¿Cómo sé si la cañería de gas bajo mi radier tiene una fisura?", "Realizamos una prueba manométrica de presión estanca que evidencia cualquier descenso por mínimo que sea."),
          ("¿Entregan informe técnico válido para la distribuidora de gas?", "Sí, emitimos informe formal firmado por instalador autorizado SEC.")
        ]
    },

    # 31. New Commune: Maipú
    {
        "slug": "fuga-de-gas-maipu",
        "title": "▷ Fuga de Gas en Maipú 【 Gásfiter Autorizado SEC Ciudad Satélite & Pajaritos 】✔️",
        "meta_desc": "Detección y sellado de fugas de gas en Maipú (Ciudad Satélite, El Abrazo, Pajaritos). Gásfiter certificado SEC. Atención urgente 24/7. Tel: +56 9 4987 7316.",
        "h1": "Detección y Reparación de <span class='highlight-red'>Fugas de Gas en Maipú</span>",
        "hero_badge": "📍 URGENCIAS 24/7 EN MAIPÚ Y SANTIAGO PONIENTE",
        "intro": "Cuadrilla móvil permanente para atención inmediata en Maipú. Diagnóstico de hermeticidad con equipos electrónicos y sellado sin romper con Prodoral R6-1.",
        "breadcrumb_name": "Maipú",
        "service_focus": "Servicio de gasfitería certificada SEC en la comuna de Maipú.",
        "specific_content": "<h2>Atención Rápida en Condominios y Villas de Maipú</h2><p>Maipú es una de las comunas más populosas de la Región Metropolitana, con miles de casas y departamentos en sectores como Pajaritos, Ciudad Satélite, El Abrazo y La Farfana. Frecuentemente, el olor a gas en patios de servicio o cocinas alarma a las familias.</p><p>Disponemos de unidades móviles equipadas con detectores electroquímicos para encontrar la fuga al instante, sellar sin romper con tecnología Prodoral R6-1 y dejar su hogar 100% seguro con Sello Verde.</p>",
        "faqs": [
          ("¿Cuánto demora una cuadrilla en llegar a Ciudad Satélite o El Abrazo?", "Contamos con móviles en el sector poniente con tiempo de llegada aproximado de 30 a 45 minutos."),
          ("¿Qué hago si siento fuerte olor a gas en mi cocina o calefón en Maipú?", "Ventile inmediatamente el área, cierre la llave de paso general y llámenos al +56 9 4987 7316."),
          ("¿Atienden redes de gas licuado de cilindro y gas natural Metrogas?", "Sí, trabajamos con ambas matrices bajo estrictos protocolos SEC.")
        ]
    },

    # 32. New Commune: La Florida
    {
        "slug": "fuga-de-gas-la-florida",
        "title": "▷ Fuga de Gas en La Florida 【 Gásfiter SEC Jardín Alto & Rojas Magallanes 】✔️",
        "meta_desc": "Reparación urgente de fugas de gas en La Florida (Jardín Alto, Walker Martínez, Vicuña Mackenna). Instaladores autorizados SEC 24/7. Tel: +56 9 4987 7316.",
        "h1": "Detección y Sellado de <span class='highlight-red'>Fugas de Gas en La Florida</span>",
        "hero_badge": "📍 ATENCIÓN DE EMERGENCIAS EN LA FLORIDA Y CORDILLERA SUR",
        "intro": "Servicio de urgencia para casas y edificios en La Florida. Detección electrónica de fugas y sellado definitivo con garantía por escrito de instaladores SEC.",
        "breadcrumb_name": "La Florida",
        "service_focus": "Detección y sellado no invasivo SEC en la comuna de La Florida.",
        "specific_content": "<h2>Cobertura Completa en Casas y Edificios de La Florida</h2><p>Desde Jardín Alto y Rojas Magallanes hasta el corredor de Vicuña Mackenna y Walker Martínez, La Florida cuenta con una variada tipología habitacional. Las fallas en cañerías empotradas por movimientos telúricos o fatiga de material son comunes en la comuna.</p><p>Brindamos solución express mediante sellado polimérico alemán sin demoler muros ni baldosas, realizando pruebas de hermeticidad de rigor para devolver la tranquilidad y el gas a su hogar.</p>",
        "faqs": [
          ("¿Tienen técnicos disponibles los fines de semana en La Florida?", "Sí, atendemos urgencias las 24 horas del día de lunes a domingo."),
          ("¿Qué certificación tienen los técnicos que visitan La Florida?", "Todos son técnicos autorizados SEC con credencial física y verificación QR en línea."),
          ("¿Pueden detectar fugas de agua oculta además de gas en La Florida?", "Sí, contamos con geófonos digitales para filtraciones en redes de agua potable.")
        ]
    },

    # 33. New Commune: Santiago Centro
    {
        "slug": "fuga-de-gas-santiago-centro",
        "title": "▷ Fuga de Gas en Santiago Centro 【 Gásfiter SEC Edificios & Departamentos 】✔️",
        "meta_desc": "Especialistas en fugas de gas en Santiago Centro (Santa Isabel, Lastarria, Barrio Brasil). Regularización Metrogas y Sello Verde SEC. Tel: +56 9 4987 7316.",
        "h1": "Reparación de <span class='highlight-red'>Fugas de Gas en Santiago Centro</span>",
        "hero_badge": "📍 ESPECIALISTAS EN DEPARTAMENTOS Y EDIFICIOS DE SANTIAGO",
        "intro": "Atención prioritaria para departamentos y comunidades en Santiago Centro. Solución a cortes de medidor de Metrogas mediante sellado Prodoral R6-1 sin demoler paredes.",
        "breadcrumb_name": "Santiago Centro",
        "service_focus": "Normalización urgente de gas en edificios de Santiago Centro.",
        "specific_content": "<h2>Expertos en Normalización de Fugas en Edificios de Santiago Centro</h2><p>En Santiago Centro, la gran densidad de departamentos y comunidades residenciales hace que cualquier microfuga represente un riesgo mayúsculo. Metrogas aplica suspensiones preventivas retirando medidores al detectar pérdidas de presión en matrices o shafts.</p><p>Nuestro equipo especializado sella redes internas con polímero Prodoral R6-1 sin causar destrozos en cerámicas de cocina o baños, emitiendo el certificado manométrico SEC reglamentario para que la compañía reasigne el medidor sin demoras.</p>",
        "faqs": [
          ("¿Cuánto demora Metrogas en reponer el servicio tras su intervención?", "Una vez ejecutado el sellado y emitida nuestra prueba de hermeticidad SEC, Metrogas programa la reposición en el plazo mínimo normado."),
          ("¿Es posible sellar cañerías en departamentos sin picar porcelanatos?", "Exacto, esa es la ventaja de la tecnología alemana Prodoral R6-1: no se toca ningún muro ni piso."),
          ("¿Atienden locales comerciales y restaurantes en el centro de Santiago?", "Sí, atendemos cocinas comerciales con protocolos de máxima exigencia técnica.")
        ]
    },

    # 34. New Commune: San Miguel
    {
        "slug": "fuga-de-gas-san-miguel",
        "title": "▷ Fuga de Gas en San Miguel 【 Gásfiter SEC El Llano & Gran Avenida 】✔️",
        "meta_desc": "Detección y reparación de fugas de gas en San Miguel (El Llano, Gran Avenida, Salesianos). Instaladores certificados SEC. Sello Verde. Tel: +56 9 4987 7316.",
        "h1": "Detección y Sellado de <span class='highlight-red'>Fugas de Gas en San Miguel</span>",
        "hero_badge": "📍 COBERTURA RÁPIDA EN SAN MIGUEL Y SANTIAGO SUR",
        "intro": "Gásfiter autorizado SEC para viviendas y edificios en San Miguel. Detección no destructiva de fugas de gas y sellado garantizado con informe oficial de hermeticidad.",
        "breadcrumb_name": "San Miguel",
        "service_focus": "Servicio técnico SEC certificado en San Miguel.",
        "specific_content": "<h2>Servicio Técnico Confiable en San Miguel</h2><p>San Miguel ha experimentado un fuerte crecimiento vertical en Gran Avenida, combinado con el tradicional barrio residencial de El Llano Subercaseaux. Las redes de gas en departamentos nuevos y casas clásicas requieren una revisión exhaustiva ante bajas de presión o malos olores.</p><p>Aplicamos instrumental de última generación para ubicar pérdidas milimétricas y procedemos al sellado limpio sin roturas con Prodoral R6-1, respaldado por instaladores acreditados SEC.</p>",
        "faqs": [
          ("¿Cuánto demoran en llegar a una emergencia en San Miguel?", "Nuestra base suroriental nos permite arribar en aproximadamente 25 a 35 minutos."),
          ("¿Entregan informe para regularización de Sello Rojo en San Miguel?", "Sí, dejamos la red en norma y emitimos el documento técnico para la obtención del Sello Verde."),
          ("¿Reparan cañerías en edificios antiguos de El Llano?", "Sí, reparamos redes de cobre y cañerías galvanizadas con total garantía.")
        ]
    },

    # 35. New Commune: Macul
    {
        "slug": "fuga-de-gas-macul",
        "title": "▷ Fuga de Gas en Macul 【 Gásfiter Certificado SEC Quilín & Macul Alto 】✔️",
        "meta_desc": "Detección de fugas de gas y sellado sin romper en Macul (Quilín, Macul Alto, Ramón Cruz). Gásfiter autorizado SEC 24/7. Tel: +56 9 4987 7316.",
        "h1": "Detección y Reparación de <span class='highlight-red'>Fugas de Gas en Macul</span>",
        "hero_badge": "📍 ATENCIÓN EXPRESS EN MACUL Y COMUNAS ALEDAÑAS",
        "intro": "Atención especializada para hogares y condominios en Macul. Localización precisa de pérdidas de gas con detectores digitales y sellado sin picar pisos.",
        "breadcrumb_name": "Macul",
        "service_focus": "Detección y reparación de fugas en la comuna de Macul.",
        "specific_content": "<h2>Soluciones Integrales para Hogares e Industrias en Macul</h2><p>En Macul atendemos desde las zonas residenciales de Macul Alto y Quilín hasta los condominios consolidados cercanos a Marathon y Escuela Agrícola. Las cañerías empotradas en losas pueden sufrir fisuras en uniones que el ojo humano no puede ver.</p><p>Con nuestro equipamiento manométrico y detectores de gas de alta precisión, localizamos y sellamos la fuga sin necesidad de romper muros ni cerámicas, otorgando garantía técnica por escrito.</p>",
        "faqs": [
          ("¿Tienen cobertura de emergencia en Macul?", "Sí, atendemos llamados de urgencia los 7 días de la semana las 24 horas."),
          ("¿Qué métodos usan para detectar fugas ocultas?", "Utilizamos manometría digital de alta precisión, detectores de gas con sniffer y gas trazador inerte."),
          ("¿Pueden verificar la instalación completa de mi vivienda en Macul?", "Sí, realizamos una inspección integral de hermeticidad y artefactos (calefón, cocina y estufas).")
        ]
    },

    # 36. New Commune: Pudahuel
    {
        "slug": "fuga-de-gas-pudahuel",
        "title": "▷ Fuga de Gas en Pudahuel 【 Gásfiter SEC Ciudad de Los Valles & Enea 】✔️",
        "meta_desc": "Urgencias por fuga de gas en Pudahuel (Ciudad de Los Valles, Pudahuel Sur, Enea, Lo Aguirre). Instalador SEC. Sellado sin romper. Tel: +56 9 4987 7316.",
        "h1": "Detección y Sellado de <span class='highlight-red'>Fugas de Gas en Pudahuel</span>",
        "hero_badge": "📍 COBERTURA EN CIUDAD DE LOS VALLES, ENEA Y PUDAHUEL",
        "intro": "Servicio técnico SEC para condominios residenciales y empresas en Pudahuel. Expertos en detección con gas trazador y sellado de microfugas sin roturas.",
        "breadcrumb_name": "Pudahuel",
        "service_focus": "Servicio de gasfitería autorizada SEC en Pudahuel.",
        "specific_content": "<h2>Servicio Certificado para Condominios y Empresas en Pudahuel</h2><p>Cubrimos los extensos condominios de Ciudad de Los Valles y Lo Aguirre, las residencias de Pudahuel Sur y los centros logísticos del parque industrial Enea. En condominios suburbanos las redes suelen ser largas y transitar bajo jardines o radieres de estacionamiento.</p><p>Ubicamos filtraciones subterráneas con gas trazador y aplicamos sellado interno Prodoral R6-1 sin demoliciones, asegurando el cumplimiento estricto de la normativa SEC.</p>",
        "faqs": [
          ("¿Llegan a Ciudad de Los Valles y Lo Aguirre?", "Sí, nuestras unidades transitan por la Ruta 68 con respuesta ágil para estos condominios."),
          ("¿Reparan fugas en empresas y bodegas de Enea?", "Sí, prestamos servicio a recintos industriales con entrega de informes técnicos y facturación."),
          ("¿Qué garantía entregan en la reparación?", "Ofrecemos garantía por escrito y certificación manométrica de hermeticidad al 100%.")
        ]
    },

    # 37. New Commune: Lampa
    {
        "slug": "fuga-de-gas-lampa",
        "title": "▷ Fuga de Gas en Lampa 【 Gásfiter SEC Valle Grande, Batuco & Chicauma 】✔️",
        "meta_desc": "Detección y reparación de fugas de gas en Lampa (Valle Grande, Batuco, Chicauma, Larapinto). Gásfiter autorizado SEC. WhatsApp: +56 9 4987 7316.",
        "h1": "Reparación y Sellado de <span class='highlight-red'>Fugas de Gas en Lampa</span>",
        "hero_badge": "📍 ATENCIÓN EN VALLE GRANDE, BATUCO, CHICAUMA Y PARCELAS",
        "intro": "Instaladores autorizados SEC en Lampa, Valle Grande y Batuco. Detección en redes subterráneas, estanques de gas a granel y sellado no invasivo con Prodoral R6-1.",
        "breadcrumb_name": "Lampa",
        "service_focus": "Servicio técnico SEC en condominios y parcelas de Lampa.",
        "specific_content": "<h2>Especialistas en Parcelas y Nuevos Condominios de Lampa</h2><p>En Lampa convergen condominios de reciente desarrollo como Valle Grande y Chicauma, junto con amplias parcelaciones en Batuco y Larapinto. Las redes de gas en estas zonas a menudo dependen de estanques de gas licuado (GLP) a granel o redes subterráneas extensas que sufren por asentamiento de terreno.</p><p>Realizamos localización no destructiva con gas trazador y sellado polimérico alemán Prodoral R6-1 para rehabilitar la red sin necesidad de excavar jardines ni romper pavimentos.</p>",
        "faqs": [
          ("¿Atienden condominios en Valle Grande y Chicauma?", "Sí, mantenemos constante cobertura en Valle Grande y todos los desarrollos inmobiliarios de Lampa."),
          ("¿Reparan redes asociadas a estanques de gas en Batuco?", "Sí, revisamos la matriz desde la salida del tanque hasta el interior de la vivienda."),
          ("¿Cómo solicitar una visita urgente en Lampa?", "Contáctenos vía WhatsApp o llamada telefónica al +56 9 4987 7316 para despacho inmediato.")
        ]
    }
]

BASE_TRUST_FAQS = [
    ("¿Cómo certifican que no quede ninguna fuga tras el trabajo?", "Realizamos una prueba manométrica de hermeticidad con manómetros digitales certificados según la norma SEC. Si la columna de presión permanece estable sin caídas durante el tiempo normado, se certifica estanqueidad del 100%."),
    ("¿El instalador que asiste a mi domicilio cuenta con acreditación SEC vigente?", "Sí. Todos nuestros técnicos son instaladores autorizados por la Superintendencia de Electricidad y Combustibles (SEC) y portan credencial física con código QR verificable en sec.cl."),
    ("¿Qué ocurre si la compañía de gas ya retiró o precintó mi medidor?", "Efectuamos el diagnóstico, reparamos o sellamos la red con Prodoral R6-1 y emitimos el informe técnico formal con código SEC para que Metrogas, Lipigas, Gasco o Abastible retire el sello y reponga el suministro."),
    ("¿Se puede reparar una microfuga de gas sin picar muros ni cerámicas?", "Sí, mediante el método de inyección interna Prodoral R6-1. El polímero alemán sella las fisuras recorriendo el ducto por dentro sin demoler paredes ni pisos."),
    ("¿Qué garantía técnica ofrecen en sus reparaciones?", "Entregamos garantía técnica por escrito en todos nuestros servicios de sellado y reparación de fugas, respaldada por instaladores autorizados."),
    ("¿Atienden emergencias fines de semana, feriados y en horario nocturno?", "Sí, disponemos de servicio técnico de emergencia operativo las 24 horas del día, los 7 días de la semana en toda la Región Metropolitana."),
    ("¿Cuáles son los medios de pago disponibles?", "Aceptamos transferencias electrónicas bancarias, tarjetas de débito/crédito y efectivo, emitiendo boleta o factura formal."),
    ("¿Cuál es el canal más rápido para coordinar una visita técnica?", "Nuestro canal prioritario es WhatsApp (+56 9 4987 7316) o llamada telefónica directa, donde un técnico le orientará de inmediato.")
]

def build_faq_html(faqs):
    html = '<div class="faq-container">\n'
    for i, (q, a) in enumerate(faqs, 1):
        active_cls = " active" if i == 1 else ""
        expanded = "true" if i == 1 else "false"
        html += f"""
        <div class="faq-item{active_cls}">
          <button class="faq-question" aria-expanded="{expanded}">
            <span>{i}. {q}</span>
            <span class="faq-icon">+</span>
          </button>
          <div class="faq-answer">
            <p>{a}</p>
          </div>
        </div>
        """
    html += '</div>\n'
    return html

def build_faq_jsonld(faqs):
    entities = []
    for q, a in faqs:
        entities.append({
            "@type": "Question",
            "name": q,
            "acceptedAnswer": {
                "@type": "Answer",
                "text": a
            }
        })
    return json.dumps({
        "@type": "FAQPage",
        "mainEntity": entities
    }, ensure_ascii=False, indent=6)

def generate_page_html(page):
    canonical_url = f"https://especialista-fugas.cl/{page['slug']}/"
    page_faqs = list(page['faqs'])
    
    # Ensure every page has at least 10 to 12 rich FAQs
    existing_questions = set(q for q, _ in page_faqs)
    for bq, ba in BASE_TRUST_FAQS:
        if len(page_faqs) >= 11:
            break
        if bq not in existing_questions:
            page_faqs.append((bq, ba))
            existing_questions.add(bq)
            
    faq_html = build_faq_html(page_faqs)
    faq_jsonld = build_faq_jsonld(page_faqs)
    
    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{page['title']}</title>
  <meta name="description" content="{page['meta_desc']}">
  <link rel="canonical" href="{canonical_url}">
  <meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1">
  
  <!-- Open Graph -->
  <meta property="og:locale" content="es_CL">
  <meta property="og:type" content="article">
  <meta property="og:title" content="{page['title']}">
  <meta property="og:description" content="{page['meta_desc']}">
  <meta property="og:url" content="{canonical_url}">
  <meta property="og:site_name" content="Especialista en Fugas Chile">
  <meta property="og:image" content="https://especialista-fugas.cl/assets/images/logotipo.jpg">
  
  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{page['title']}">
  <meta name="twitter:description" content="{page['meta_desc']}">
  <meta name="twitter:image" content="https://especialista-fugas.cl/assets/images/logotipo.jpg">

  <!-- Favicon -->
  <link rel="icon" type="image/jpeg" href="../assets/images/logotipo.jpg">
  
  <!-- Stylesheet -->
  <link rel="stylesheet" href="../assets/css/style.css?v=3.0">

  <!-- Schema.org JSON-LD -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@graph": [
      {{
        "@type": "PlumbingService",
        "@id": "{canonical_url}#service",
        "name": "Especialista en Fugas - {page['breadcrumb_name']}",
        "image": "https://especialista-fugas.cl/assets/images/logotipo.jpg",
        "logo": "https://especialista-fugas.cl/assets/images/logotipo.jpg",
        "url": "{canonical_url}",
        "telephone": "+56949877316",
        "priceRange": "$$",
        "address": {{
          "@type": "PostalAddress",
          "streetAddress": "Santiago Central",
          "addressLocality": "Santiago",
          "addressRegion": "Región Metropolitana",
          "postalCode": "8320000",
          "addressCountry": "CL"
        }},
        "openingHoursSpecification": {{
          "@type": "OpeningHoursSpecification",
          "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
          "opens": "00:00",
          "closes": "23:59"
        }}
      }},
      {faq_jsonld},
      {{
        "@type": "BreadcrumbList",
        "itemListElement": [
          {{
            "@type": "ListItem",
            "position": 1,
            "name": "Inicio",
            "item": "https://especialista-fugas.cl/"
          }},
          {{
            "@type": "ListItem",
            "position": 2,
            "name": "{page['breadcrumb_name']}",
            "item": "{canonical_url}"
          }}
        ]
      }}
    ]
  }}
  </script>
</head>
<body>

  <!-- Top Emergency Announcement Bar -->
  <aside class="top-bar" aria-label="Alerta de Emergencia 24/7">
    <div class="container top-bar-inner">
      <div class="emergency-pulse">
        <span class="pulse-dot"></span>
        <span class="top-bar-text-desktop"><strong>EMERGENCIAS 24/7:</strong> Técnicos Autorizados SEC de Guardia Inmediata</span>
        <a href="tel:+56949877316" class="top-bar-text-mobile">🚨 Emergencias 24/7 SEC • <strong>📞 +56 9 4987 7316</strong></a>
      </div>
      <div class="top-bar-contact">
        <span>Llamada Urgente: <a class="top-bar-link" href="tel:+56949877316"><strong>+56 9 4987 7316</strong></a></span>
        <span>•</span>
        <a class="top-bar-link" href="https://wa.me/56949877316?text=Hola,%20solicito%20atenci%C3%B3n%20urgente%20para%20{page['breadcrumb_name']}" target="_blank" rel="noopener">WhatsApp Inmediato 💬</a>
      </div>
    </div>
  </aside>

  <!-- Sticky Main Header -->
  <header class="main-header" id="header">
    <div class="container header-container">
      <!-- Brand Logo & Name -->
      <a href="../" class="brand-wrapper" aria-label="Ir al inicio de Especialista en Fugas">
        <img src="../assets/images/logotipo.jpg" alt="Logo Especialista en Fugas" class="brand-logo" width="44" height="44">
        <div class="brand-text">
          <span class="brand-name">ESPECIALISTA <span>FUGAS</span></span>
          <span class="brand-tagline">Gasfiter SEC Certificado</span>
        </div>
      </a>

      <!-- Desktop Navigation -->
      <nav class="nav-desktop" aria-label="Navegación Principal">
        <a href="../" class="nav-link">Inicio</a>
        
        <div class="nav-item-dropdown">
          <a href="../fuga-de-gas/" class="nav-link">Fugas de Gas ▾</a>
          <div class="dropdown-menu">
            <a href="../sellado-de-fugas-de-gas-con-prodoral/" class="dropdown-item">Sellado con Prodoral R6-1 (Sin Romper)</a>
            <a href="../deteccion-de-fugas-con-gas-trazador/" class="dropdown-item">Detección con Gas Trazador</a>
            <a href="../fuga-de-gas-deteccion/" class="dropdown-item">Detección Electrónica</a>
            <a href="../gasfiter-sec-especialista-en-fuga-de-gas/" class="dropdown-item">Gásfiter Certificado SEC</a>
            <a href="../certificacion-sec-sello-verde/" class="dropdown-item">Certificación Sello Verde SEC</a>
          </div>
        </div>

        <div class="nav-item-dropdown">
          <a href="../deteccion-de-fugas-de-agua/" class="nav-link">Fugas de Agua ▾</a>
          <div class="dropdown-menu">
            <a href="../deteccion-de-fugas-de-agua/" class="dropdown-item">Detección de Fugas de Agua (Geófono)</a>
            <a href="../deteccion-de-fugas-de-piscinas/" class="dropdown-item">Fugas en Piscinas</a>
            <a href="../fuga-de-gas-reparamos-fugas-de-gas-sin-romper/" class="dropdown-item">Reparación No Invasiva</a>
          </div>
        </div>

        <div class="nav-item-dropdown">
          <a href="../#cobertura" class="nav-link">Comunas ▾</a>
          <div class="dropdown-menu dropdown-menu-comunas">
            <a href="../fuga-de-gas-las-condes/" class="dropdown-item">Las Condes</a>
            <a href="../fuga-de-gas-providencia/" class="dropdown-item">Providencia</a>
            <a href="../fuga-de-gas-vitacura/" class="dropdown-item">Vitacura</a>
            <a href="../fuga-de-gas-lo-barnechea/" class="dropdown-item">Lo Barnechea</a>
            <a href="../fuga-de-gas-nunoa/" class="dropdown-item">Ñuñoa</a>
            <a href="../fuga-de-gas-la-reina/" class="dropdown-item">La Reina</a>
            <a href="../fuga-de-gas-la-chicureo/" class="dropdown-item">Chicureo / Colina</a>
            <a href="../fuga-de-gas-penalolen/" class="dropdown-item">Peñalolén</a>
            <a href="../fuga-de-gas-santiago-centro/" class="dropdown-item">Santiago Centro</a>
            <a href="../fuga-de-gas-san-miguel/" class="dropdown-item">San Miguel</a>
            <a href="../fuga-de-gas-maipu/" class="dropdown-item">Maipú</a>
            <a href="../fuga-de-gas-la-florida/" class="dropdown-item">La Florida</a>
            <a href="../fuga-de-gas-macul/" class="dropdown-item">Macul</a>
            <a href="../fuga-de-gas-puente-alto/" class="dropdown-item">Puente Alto</a>
            <a href="../fuga-de-gas-san-bernardo/" class="dropdown-item">San Bernardo</a>
            <a href="../fuga-de-gas-quinta-normal/" class="dropdown-item">Quinta Normal</a>
            <a href="../fuga-de-gas-san-joaquin/" class="dropdown-item">San Joaquín</a>
            <a href="../fuga-de-gas-pudahuel/" class="dropdown-item">Pudahuel</a>
            <a href="../fuga-de-gas-lampa/" class="dropdown-item">Lampa</a>
            <a href="../fuga-de-gas-pirque/" class="dropdown-item">Pirque</a>
            <a href="../fuga-de-gas-paine/" class="dropdown-item">Paine</a>
            <a href="../fuga-de-gas-maria-pinto/" class="dropdown-item">María Pinto</a>
            <a href="../fuga-de-gas-rancagua/" class="dropdown-item">Rancagua</a>
            <a href="../fuga-de-gas-papudo/" class="dropdown-item">Papudo</a>
          </div>
        </div>

        <a href="#faqs" class="nav-link">Preguntas Frecuentes</a>
      </nav>

      <!-- Action Buttons -->
      <div class="header-ctas">
        <a href="tel:+56949877316" class="btn-header-call" aria-label="Llamar al gasfiter">
          📞 949 877 316
        </a>
        <a href="https://wa.me/56949877316?text=Hola,%20solicito%20atenci%C3%B3n%20para%20{page['breadcrumb_name']}" class="btn-header-wa" target="_blank" rel="noopener" aria-label="Abrir WhatsApp">
          <svg class="icon-wa" width="16" height="16" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
            <path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.893 11.892-1.99-.001-3.951-.5-5.688-1.448l-6.305 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-.999 3.648 3.742-.981zm11.387-5.464c-.074-.124-.272-.198-.57-.347-.297-.149-1.758-.868-2.031-.967-.272-.099-.47-.149-.669.149-.198.297-.768.967-.941 1.165-.173.198-.347.223-.644.074-.297-.149-1.255-.462-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.297-.347.446-.521.151-.172.2-.296.3-.495.099-.198.05-.372-.025-.521-.075-.148-.669-1.611-.916-2.206-.242-.579-.487-.501-.669-.51l-.57-.01c-.198 0-.52.074-.792.372s-1.04 1.016-1.04 2.479 1.065 2.876 1.213 3.074c.149.198 2.095 3.2 5.076 4.487.709.306 1.263.489 1.694.626.712.226 1.36.194 1.872.118.571-.085 1.758-.719 2.006-1.413.248-.695.248-1.29.173-1.414z"/>
          </svg>
          <span class="btn-wa-text">WhatsApp</span>
        </a>
        <button class="menu-toggle" aria-label="Abrir Menú de Navegación">
          <span></span>
          <span></span>
          <span></span>
        </button>
      </div>
    </div>
  </header>

  <!-- Mobile Drawer Backdrop & Menu -->
  <div class="mobile-nav-backdrop"></div>
  <aside class="mobile-drawer" aria-label="Menú Móvil">
    <div>
      <div class="mobile-drawer-header">
        <div class="brand-wrapper">
          <img src="../assets/images/logotipo.jpg" alt="Logo Especialista en Fugas" class="brand-logo" width="40" height="40">
          <div class="brand-text">
            <span class="brand-name">ESPECIALISTA <span>FUGAS</span></span>
            <span class="brand-tagline">Gasfiter Certificado SEC</span>
          </div>
        </div>
        <button class="mobile-drawer-close" aria-label="Cerrar Menú">✕</button>
      </div>

      <nav class="mobile-menu-list">
        <div class="mobile-menu-item">
          <a href="../" class="mobile-menu-link">🏠 Inicio</a>
        </div>
        <div class="mobile-menu-item">
          <span class="mobile-menu-link">🔥 Fugas de Gas</span>
          <div class="mobile-submenu">
            <a href="../sellado-de-fugas-de-gas-con-prodoral/" class="mobile-sub-link">➡️ Sellado con Prodoral (Sin Romper)</a>
            <a href="../deteccion-de-fugas-con-gas-trazador/" class="mobile-sub-link">➡️ Detección con Gas Trazador</a>
            <a href="../fuga-de-gas-deteccion/" class="mobile-sub-link">➡️ Detección Electrónica</a>
            <a href="../gasfiter-sec-especialista-en-fuga-de-gas/" class="mobile-sub-link">➡️ Gásfiter SEC Certificado</a>
            <a href="../certificacion-sec-sello-verde/" class="mobile-sub-link">➡️ Regularización Sello Verde SEC</a>
          </div>
        </div>
        <div class="mobile-menu-item">
          <span class="mobile-menu-link">💧 Fugas de Agua</span>
          <div class="mobile-submenu">
            <a href="../deteccion-de-fugas-de-agua/" class="mobile-sub-link">➡️ Detección con Geófono y Ultrasonido</a>
            <a href="../deteccion-de-fugas-de-piscinas/" class="mobile-sub-link">➡️ Fugas en Piscinas</a>
            <a href="../fuga-de-gas-reparamos-fugas-de-gas-sin-romper/" class="mobile-sub-link">➡️ Reparación Sin Romper</a>
          </div>
        </div>
        <div class="mobile-menu-item">
          <span class="mobile-menu-link">📍 Comunas Cobertura</span>
          <div class="mobile-submenu mobile-submenu-comunas">
            <a href="../fuga-de-gas-las-condes/" class="mobile-sub-link">Las Condes</a>
            <a href="../fuga-de-gas-providencia/" class="mobile-sub-link">Providencia</a>
            <a href="../fuga-de-gas-vitacura/" class="mobile-sub-link">Vitacura</a>
            <a href="../fuga-de-gas-lo-barnechea/" class="mobile-sub-link">Lo Barnechea</a>
            <a href="../fuga-de-gas-nunoa/" class="mobile-sub-link">Ñuñoa</a>
            <a href="../fuga-de-gas-la-reina/" class="mobile-sub-link">La Reina</a>
            <a href="../fuga-de-gas-la-chicureo/" class="mobile-sub-link">Chicureo / Colina</a>
            <a href="../fuga-de-gas-penalolen/" class="mobile-sub-link">Peñalolén</a>
            <a href="../fuga-de-gas-santiago-centro/" class="mobile-sub-link">Santiago Centro</a>
            <a href="../fuga-de-gas-san-miguel/" class="mobile-sub-link">San Miguel</a>
            <a href="../fuga-de-gas-maipu/" class="mobile-sub-link">Maipú</a>
            <a href="../fuga-de-gas-la-florida/" class="mobile-sub-link">La Florida</a>
            <a href="../fuga-de-gas-macul/" class="mobile-sub-link">Macul</a>
            <a href="../fuga-de-gas-puente-alto/" class="mobile-sub-link">Puente Alto</a>
            <a href="../fuga-de-gas-san-bernardo/" class="mobile-sub-link">San Bernardo</a>
            <a href="../fuga-de-gas-quinta-normal/" class="mobile-sub-link">Quinta Normal</a>
            <a href="../fuga-de-gas-san-joaquin/" class="mobile-sub-link">San Joaquín</a>
            <a href="../fuga-de-gas-pudahuel/" class="mobile-sub-link">Pudahuel</a>
            <a href="../fuga-de-gas-lampa/" class="mobile-sub-link">Lampa</a>
            <a href="../fuga-de-gas-pirque/" class="mobile-sub-link">Pirque</a>
            <a href="../fuga-de-gas-paine/" class="mobile-sub-link">Paine</a>
            <a href="../fuga-de-gas-maria-pinto/" class="mobile-sub-link">María Pinto</a>
            <a href="../fuga-de-gas-rancagua/" class="mobile-sub-link">Rancagua</a>
            <a href="../fuga-de-gas-papudo/" class="mobile-sub-link">Papudo</a>
          </div>
        </div>
        <div class="mobile-menu-item">
          <a href="#faqs" class="mobile-menu-link">❓ Preguntas Frecuentes</a>
        </div>
      </nav>
    </div>

    <div class="mobile-drawer-footer">
      <a href="tel:+56949877316" class="btn-sticky-call" style="width: 100%;">📞 Llamar: 949 877 316</a>
      <a href="https://wa.me/56949877316?text=Hola,%20solicito%20atenci%C3%B3n%20urgente%20para%20{page['breadcrumb_name']}" class="btn-sticky-wa" target="_blank" rel="noopener" style="width: 100%;">💬 WhatsApp 24/7</a>
    </div>
  </aside>

  <!-- Breadcrumbs -->
  <nav class="breadcrumbs" aria-label="Migas de pan">
    <div class="container">
      <ol>
        <li><a href="../">Inicio</a></li>
        <li class="current">{page['breadcrumb_name']}</li>
      </ol>
    </div>
  </nav>

  <!-- Hero Section -->
  <main>
    <section class="hero" style="padding-top: 36px;">
      <div class="container hero-grid">
        <div class="hero-content">
          <div class="hero-badge">
            <span>{page['hero_badge']}</span>
          </div>

          <h1 class="hero-title">
            {page['h1']}
          </h1>

          <p class="hero-subtitle">
            {page['intro']}
          </p>

          <div class="hero-checklist">
            <div class="checklist-item">
              <span class="check-icon">✓</span>
              <span><strong>Técnicos Certificados SEC:</strong> Con credencial física y QR oficial.</span>
            </div>
            <div class="checklist-item">
              <span class="check-icon">✓</span>
              <span><strong>Cero Daños Estructurales:</strong> Diagnóstico no invasivo sin romper muros.</span>
            </div>
            <div class="checklist-item">
              <span class="check-icon">✓</span>
              <span><strong>Garantía Escrita:</strong> Pruebas manométricas de hermeticidad certificadas.</span>
            </div>
          </div>

          <div class="hero-actions">
            <a href="tel:+56949877316" class="btn-hero-emergency">
              🚨 Llamar a Emergencias: 949 877 316
            </a>
            <a href="https://wa.me/56949877316?text=Hola%20Especialista%20en%20Fugas,%20necesito%20asistencia%20inmediata%20para%20{page['breadcrumb_name']}" class="btn-hero-wa" target="_blank" rel="noopener">
              💬 Enviar WhatsApp Directo
            </a>
          </div>
        </div>

        <!-- Quick Lead Capture Form (Redirects to WhatsApp) -->
        <div class="hero-card">
          <div class="hero-card-header">
            <h2 class="hero-card-title">Atención Inmediata al WhatsApp</h2>
            <p class="hero-card-subtitle">Solicite diagnóstico rápido para {page['breadcrumb_name']}</p>
          </div>

          <form class="lead-form" data-whatsapp-lead>
            <div class="form-group">
              <label class="form-label" for="nombre">Nombre y Apellido *</label>
              <input type="text" id="nombre" name="nombre" class="form-input" placeholder="Ej: Marcela González" required>
            </div>

            <div class="form-group">
              <label class="form-label" for="telefono">Teléfono / WhatsApp *</label>
              <input type="tel" id="telefono" name="telefono" class="form-input" placeholder="+56 9 8765 4321" required>
            </div>

            <div class="form-group">
              <label class="form-label" for="comuna">Comuna / Dirección *</label>
              <input type="text" id="comuna" name="comuna" class="form-input" placeholder="Ej: {page['breadcrumb_name']} / RM" required>
            </div>

            <div class="form-group">
              <label class="form-label" for="servicio">Servicio Solicitado</label>
              <input type="text" id="servicio" name="servicio" class="form-input" value="{page['breadcrumb_name']}" readonly>
            </div>

            <div class="form-group">
              <label class="form-label" for="mensaje">Detalle de la Fuga / Consulta</label>
              <textarea id="mensaje" name="mensaje" class="form-textarea" placeholder="¿Siente olor a gas, le cortaron el medidor o pierde agua?"></textarea>
            </div>

            <button type="submit" class="btn-form-submit">
              💬 Enviar Consulta Directa a WhatsApp
            </button>
            <p class="form-note">🔒 Respuesta técnica prioritaria 24/7. Instalador autorizado SEC.</p>
          </form>
        </div>
      </div>
    </section>

    <!-- Trust Signals Bar -->
    <section class="trust-bar" aria-label="Acreditaciones">
      <div class="container trust-bar-grid">
        <div class="trust-item">
          <img src="../assets/images/IMG-20240613-WA0008.jpg" alt="Sello Gásfiter Certificado Central" width="44" height="44">
          <div>
            <div class="trust-title">Gásfiter Certificado</div>
            <div class="trust-desc">Instaladores SEC Autorizados</div>
          </div>
        </div>

        <div class="trust-item">
          <img src="../assets/images/sec-qr.png" alt="Código QR SEC Verificable" width="44" height="44">
          <div>
            <div class="trust-title">Verificación SEC QR</div>
            <div class="trust-desc">Credencial oficial escaneable</div>
          </div>
        </div>

        <div class="trust-item">
          <div class="trust-icon-box">🇩🇪</div>
          <div>
            <div class="trust-title">Prodoral R6-1 Original</div>
            <div class="trust-desc">Polímero alemán sin picar muros</div>
          </div>
        </div>

        <div class="trust-item">
          <div class="trust-icon-box">⭐</div>
          <div>
            <div class="trust-title">Garantía Escrita</div>
            <div class="trust-desc">Prueba manométrica certificada</div>
          </div>
        </div>
      </div>
    </section>

    <!-- Page Specific Details Section -->
    <section class="section section-alt">
      <div class="container">
        <div style="max-width: 900px; margin: 0 auto; font-size: 1.05rem; line-height: 1.7; color: var(--text-muted);">
          {page['specific_content']}
        </div>
      </div>
    </section>

    <!-- SEC Authority & Trust Card -->
    <section class="section">
      <div class="container">
        <div class="authority-card">
          <div class="authority-content">
            <span class="section-badge" style="background: rgba(255,255,255,0.15); color: #FFD166;">Marco Legal y Seguridad</span>
            <h2 class="authority-title">Acreditación Oficial SEC en Todo Chile</h2>
            <p class="authority-text">
              Toda intervención en redes de gas debe ser efectuada bajo la normativa del <strong>Decreto Supremo Nº 66</strong> por técnicos certificados por la <strong>Superintendencia de Electricidad y Combustibles (SEC)</strong>.
            </p>
            <p class="authority-text">
              Nuestras cuadrillas cuentan con acreditación oficial vigente para asegurar la validez legal ante las compañías distribuidoras (Metrogas, Lipigas, Abastible, Gasco) y compañías de seguros.
            </p>
            <div style="margin-top: 10px;">
              <a href="https://wa.me/56949877316?text=Hola,%20deseo%20validar%20mi%20instalaci%C3%B3n%20para%20{page['breadcrumb_name']}" class="btn-hero-emergency" target="_blank" rel="noopener">
                💬 Solicitar Visita de Técnico Autorizado SEC
              </a>
            </div>
          </div>

          <div class="authority-badges">
            <div class="qr-box">
              <img src="../assets/images/sec-qr.png" alt="Código QR Credencial SEC" width="146" height="146">
              <div class="qr-label">Escanee para verificar acreditación SEC</div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Specific FAQ Accordion Section -->
    <section class="section section-alt" id="faqs">
      <div class="container">
        <div class="section-header">
          <span class="section-badge">Preguntas Frecuentes</span>
          <h2 class="section-title">Dudas Comunes sobre {page['breadcrumb_name']}</h2>
          <p class="section-subtitle">
            Información técnica transparente para resolver sus inquietudes con total claridad.
          </p>
        </div>

        {faq_html}
      </div>
    </section>

    <!-- Final Call to Action Banner -->
    <section class="section" style="background: linear-gradient(135deg, #990000 0%, #D90429 100%); color: #FFFFFF; text-align: center;">
      <div class="container" style="max-width: 800px;">
        <h2 style="font-size: 2.2rem; font-weight: 900; margin-bottom: 16px; line-height: 1.2;">
          ¿Necesita Asistencia Técnica Inmediata?
        </h2>
        <p style="font-size: 1.15rem; margin-bottom: 30px; color: #FFE5E5;">
          No deje que una fuga de gas o agua comprometa su seguridad ni su patrimonio. Contáctenos ahora mismo al WhatsApp oficial.
        </p>
        <div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 16px;">
          <a href="tel:+56949877316" class="btn-hero-emergency" style="background: #FFFFFF; color: #D90429; box-shadow: 0 4px 15px rgba(0,0,0,0.2);">
            📞 Llamar Ahora: +56 9 4987 7316
          </a>
          <a href="https://wa.me/56949877316?text=Hola,%20solicito%20atenci%C3%B3n%20urgente%20para%20{page['breadcrumb_name']}" class="btn-hero-wa" target="_blank" rel="noopener">
            💬 WhatsApp 24/7 Urgente
          </a>
        </div>
      </div>
    </section>
  </main>

  <!-- Main Footer -->
  <footer class="main-footer">
    <div class="container">
      <div class="footer-grid">
        <!-- Col 1: Brand Info -->
        <div class="footer-brand">
          <div class="brand-wrapper">
            <img src="../assets/images/logotipo.jpg" alt="Logo Especialista en Fugas" class="brand-logo" width="48" height="48">
            <span class="footer-brand-title">ESPECIALISTA <span>FUGAS</span></span>
          </div>
          <p>
            Especialistas autorizados SEC en detección acústica de fugas y sellado no destructivo con tecnología alemana Prodoral R6-1. Cobertura integral en la Región Metropolitana y zonas aledañas.
          </p>
          <div style="display: flex; gap: 12px; align-items: center; margin-top: 8px;">
            <img src="../assets/images/IMG-20240613-WA0008.jpg" alt="Gásfiter Certificado Central" width="46" height="46">
            <img src="../assets/images/sec-qr.png" alt="Acreditación SEC QR" width="46" height="46">
          </div>
        </div>

        <!-- Col 2: Servicios de Gas -->
        <div>
          <div class="footer-column-title">Fugas de Gas</div>
          <ul class="footer-links">
            <li><a href="../sellado-de-fugas-de-gas-con-prodoral/" class="footer-link">Sellado con Prodoral R6-1</a></li>
            <li><a href="../deteccion-de-fugas-con-gas-trazador/" class="footer-link">Detección con Gas Trazador</a></li>
            <li><a href="../fuga-de-gas-deteccion/" class="footer-link">Diagnóstico de Hermeticidad</a></li>
            <li><a href="../gasfiter-sec-especialista-en-fuga-de-gas/" class="footer-link">Gásfiter Autorizado SEC</a></li>
            <li><a href="../certificacion-sec-sello-verde/" class="footer-link">Certificación Sello Verde</a></li>
            <li><a href="../fuga-de-gas-reparamos-fugas-de-gas-sin-romper/" class="footer-link">Reparación Sin Romper</a></li>
          </ul>
        </div>

        <!-- Col 3: Servicios de Agua -->
        <div>
          <div class="footer-column-title">Fugas de Agua</div>
          <ul class="footer-links">
            <li><a href="../deteccion-de-fugas-de-agua/" class="footer-link">Detección de Fugas de Agua</a></li>
            <li><a href="../deteccion-de-fugas-de-piscinas/" class="footer-link">Filtraciones en Piscinas</a></li>
            <li><a href="../deteccion-de-fugas-de-agua/" class="footer-link">Geófono y Ultrasonido</a></li>
            <li><a href="../emergencias-24-7/" class="footer-link">Servicio de Emergencia 24/7</a></li>
          </ul>
        </div>

        <!-- Col 4: Contacto Oficial -->
        <div>
          <div class="footer-column-title">Atención 24/7</div>
          <ul class="footer-links">
            <li><strong>Central Telefónica:</strong></li>
            <li><a href="tel:+56949877316" class="footer-link" style="color: #FFFFFF; font-weight: 700;">📞 (+56) 9 4987 7316</a></li>
            <li style="margin-top: 8px;"><strong>WhatsApp Técnico:</strong></li>
            <li><a href="https://wa.me/56949877316?text=Hola,%20solicito%20atenci%C3%B3n%20para%20{page['breadcrumb_name']}" class="footer-link" style="color: #25D366; font-weight: 700;" target="_blank" rel="noopener">💬 Chatear por WhatsApp</a></li>
            <li style="margin-top: 8px;"><strong>Cobertura:</strong></li>
            <li>Región Metropolitana, V y VI Región</li>
            <li>Lunes a Domingo las 24 horas</li>
          </ul>
        </div>
      </div>

      <div class="footer-bottom">
        <div>
          © 2026 Especialista en Fugas Chile • Todos los derechos reservados.
        </div>
        <div>
          Instalador Autorizado SEC • Tecnología Prodoral R6-1
        </div>
      </div>
    </div>
  </footer>

  <!-- Sticky Bottom Quick Action Bar for Mobile -->
  <aside class="mobile-sticky-bar" aria-label="Contacto Rápido Móvil">
    <a href="tel:+56949877316" class="btn-sticky-call">
      📞 Llamar 24/7
    </a>
    <a href="https://wa.me/56949877316?text=Hola%20Especialista%20en%20Fugas,%20tengo%20una%20emergencia%20para%20{page['breadcrumb_name']}" class="btn-sticky-wa" target="_blank" rel="noopener">
      💬 WhatsApp Urgente
    </a>
  </aside>

  <!-- Main JavaScript File -->
  <script src="../assets/js/main.js?v=3.0"></script>
</body>
</html>
"""
    return html

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    print(f"Generating pages in {base_dir}...")
    
    count = 0
    for page in PAGES_DATA:
        folder = os.path.join(base_dir, page["slug"])
        os.makedirs(folder, exist_ok=True)
        file_path = os.path.join(folder, "index.html")
        content = generate_page_html(page)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        count += 1
        print(f"[{count}/{len(PAGES_DATA)}] Generated: {page['slug']}/index.html")

    # Generate sitemap.xml
    sitemap_path = os.path.join(base_dir, "sitemap.xml")
    sitemap_entries = [
        """  <url>
    <loc>https://especialista-fugas.cl/</loc>
    <lastmod>2026-09-30</lastmod>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
  </url>"""
    ]
    for page in PAGES_DATA:
        priority = "0.9" if "sellado" in page["slug"] or "deteccion" in page["slug"] or "fuga-de-gas" in page["slug"] else "0.8"
        sitemap_entries.append(f"""  <url>
    <loc>https://especialista-fugas.cl/{page['slug']}/</loc>
    <lastmod>2026-09-30</lastmod>
    <changefreq>monthly</changefreq>
    <priority>{priority}</priority>
  </url>""")

    sitemap_xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{chr(10).join(sitemap_entries)}
</urlset>"""

    with open(sitemap_path, "w", encoding="utf-8") as f:
        f.write(sitemap_xml)
    print("Generated sitemap.xml")

    # Generate robots.txt
    robots_path = os.path.join(base_dir, "robots.txt")
    robots_txt = """User-agent: *
Allow: /

Sitemap: https://especialista-fugas.cl/sitemap.xml
"""
    with open(robots_path, "w", encoding="utf-8") as f:
        f.write(robots_txt)
    print("Generated robots.txt")
    print("SUCCESS: All static pages, schemas, sitemap, and robots generated!")

if __name__ == "__main__":
    main()
