# <center>🌐 Bienvenido a Ciencia de Datos</center>

## 📚 Índice temático del curso OCI Data Science 

### 1. **Bienvenida e Introducción General**
- Qué es Data Science y por qué es relevante hoy
- Objetivo del curso y habilidades requeridas
- Casos de uso: Employee Attrition
- Estructura del curso por módulos
- Consejos de estudio y comunidad de aprendizaje

### 2. **Historia y Evolución de Data Science**
- Filosofía: Navaja de Ockham
- Primeros enfoques científicos (Mayer, Tukey, Samuel)
- Hitos tecnológicos (Deep Blue, AutoML)
- Nacimiento del término “Data Science”
- Aplicaciones modernas: Great Resignation y predicción de abandono

### 3. **Servicios de Oracle para Data Science y AI**
- Diferencias entre ML Services y AI Services
- OCI Data Labeling y Catálogo de Modelos
- Arquitectura: datos, aplicaciones, servicios
- Principios guía: aceleración individual, colaboración y escalabilidad empresarial

### 4. **Terminología y Componentes Clave de OCI Data Science**
- Projects, Notebook Sessions, Conda
- ADS SDK: funcionalidades y flujo completo
- Model Catalog, Model Deployment, Data Science Jobs
- Interfaces disponibles: consola, SDK, CLI, API REST

### 5. **Visualización, Ingeniería de Features y Entrenamiento**
- Acceso a datos: local, object storage, bases Oracle y terceros
- Exploración de datos: Feature Types, heatmaps, estadísticas
- Feature Engineering: codificación, imputación, recomendaciones
- Entrenamiento de modelos: AutoML, ADSTuner
- Evaluación de modelos y explicación (interpretabilidad local/global)

### 6. **Políticas, Tenencia y Configuración IAM**
- Compartments, grupos de usuarios, grupos dinámicos
- Sintaxis de políticas: verbs, resource types
- Políticas requeridas y útiles para logging, métricas, red y servicios relacionados
- Ejemplo de configuración manual y con OCI Resource Manager
- Acceso y estructura del Terraform Script

### 7. **Networking para Data Science**
- Componentes de red: VCN, Subnets, VNICs, DRG, NAT, Service Gateway
- Patrones: red por defecto vs red personalizada
- Uso del VCN Wizard
- Requisitos para conectar workloads a activos externos

### 8. **Autenticación en APIs de OCI**
- Interfaces disponibles: ADS SDK, Python SDK, CLI
- Diferencias entre autenticación y autorización
- Resource Principals: seguridad, rotación de certificados
- Archivos de configuración y claves API (.pem)
- Notebooks de ejemplo para crear credenciales</br></br>

************************************************************************************************************
</br>
</br>



### -- Visión General del Curso

Bienvenidos todos al curso de Ciencia de Datos de Oracle Cloud Infrastructure. La ciencia de datos es el arte y la ciencia de extraer conocimientos valiosos de los datos para resolver problemas del mundo real y de negocios.

Y este es el momento perfecto para mejorar o reentrenar a tu fuerza laboral para satisfacer esta enorme demanda de profesionales en ciencia de datos. Estamos emocionados de tenerte aquí y hemos preparado una gran cantidad de información valiosa para ti. Para simplificar, usaré OCI para referirme a Oracle Cloud Infrastructure, que es nuestra poderosa plataforma.

En las siguientes diapositivas, te guiaré a través del público objetivo, los requisitos previos, los objetivos y la estructura del curso. Pero antes de eso, echemos un vistazo a las personas que contribuyeron a este curso.

Además de mí, escucharás a varios expertos y especialistas a lo largo de este curso, incluyendo Wes Prichard, John Peach, John Stanesby, JR Gauthier, Lyudmil Pelov, Praveen Patil y Hemant Gahankari. Aunque tal vez no escuches sus voces, hay docenas de personas que ayudaron a desarrollar este curso. Están listadas aquí alfabéticamente por equipo.

Este curso fue diseñado con una audiencia específica en mente. Está destinado principalmente a científicos de datos, pero también es apropiado para roles relacionados como ingenieros de aprendizaje automático (ML engineers) e ingenieros de inteligencia artificial (AI engineers).

Nuestro objetivo es ayudarte a dominar el uso de OCI Data Science y servicios en la nube relacionados para construir soluciones de ciencia de datos. Para eso, deberías tener habilidades en Python para aprendizaje automático. Deberías tener conocimientos generales de bibliotecas de ciencia de datos y aprendizaje automático de código abierto, y saber cómo aplicarlas.

Eso significa que probablemente tienes un año o más de experiencia en uno de los roles mencionados en la diapositiva anterior. Y será útil si ya tienes algo de experiencia práctica con OCI.

Dado que este curso trata sobre ayudarte a prepararte para el examen de certificación, es útil saber desde el principio lo que el examen va a validar. Evaluará tu capacidad para identificar servicios de OCI utilizados para implementar una solución de aprendizaje automático para un caso de uso empresarial. Verificará si puedes incorporar buenas prácticas de aprendizaje automático en la nube.

Se centrará fuertemente en el uso de OCI Data Science para construir, entrenar, desplegar y gestionar modelos de ML. También incluirá el uso de otros servicios de datos e inteligencia artificial de OCI para crear soluciones de aprendizaje automático.

Este curso está dividido en cinco módulos principales. Tomemos un momento para repasarlos. Una introducción a la ciencia de datos presentará OCI Data Science, y cómo configurar una tenencia de OCI (OCI tenancy) para usar OCI Data Science. La configuración del entorno se centrará en la preparación del entorno de OCI Data Science.

El módulo del ciclo de vida de aprendizaje automático te guiará por las capacidades de OCI Data Science que apoyan todos los pasos del ciclo de vida de ML. Las prácticas de MLOps se enfocan en características que soportan MLOps como escalado, monitoreo.

Y finalmente, Servicios Relacionados de OCI cubre otros servicios en la nube útiles al construir soluciones de ciencia de datos. Cada uno de estos módulos contiene múltiples lecciones presentadas por diferentes especialistas. Recomendamos avanzar en los módulos en orden, porque los módulos posteriores se basan en los anteriores.

Muchas de las lecciones incluirán una demostración grabada para ilustrar los conceptos y prácticas importantes presentadas en la lección. El curso también incluye un laboratorio de extremo a extremo que los estudiantes pueden usar para obtener experiencia práctica y reforzar conceptos de todos los módulos.

Este laboratorio utiliza un caso de uso sobre la deserción de empleados (employee attrition). Y muchas de las demostraciones usarán ese mismo caso. El caso predice la probabilidad de que un empleado deje la organización según múltiples características.

Para completar el laboratorio, necesitarás acceso a una cuenta de Oracle Cloud. Si aún no tienes una, puedes registrarte para una prueba gratuita en signup.cloud.oracle.com. También puedes usar GitHub para acceder al repositorio de ejemplos de OCI Data Science y AI (OCI Data Science AI samples repo). Y vamos a presentarte la terminología de los productos de ciencia de datos en el primer módulo.

En cualquier momento, si tienes una pregunta específica sobre el material del curso o necesitas ayuda adicional, completa nuestro formulario “Ask Your Instructor”. Nuestros instructores expertos se comunicarán contigo lo antes posible con soporte personalizado.

También queremos que saques el máximo provecho de tu experiencia de aprendizaje. Por eso hemos creado este espacio comunitario donde puedes conectar con otros estudiantes y expertos en la materia. Si tienes alguna otra pregunta o quieres iniciar una discusión sobre un tema en particular, este es el lugar. Así que no seas tímido. Únete hoy a la comunidad de Oracle University (OU Community) y empieza a colaborar con tus compañeros de estudio. Estamos ansiosos por ver lo que aportarás.

Me gustaría reconocer que este es un curso extenso. También me gustaría ofrecer algunos consejos para mejorar la retención y darte la mejor oportunidad de aprobar el examen. Sugerimos que tomes notas sobre los temas según tu conocimiento previo. Y recuerda que puedes seguir usando la transcripción de preparación.

Programa descansos cada hora y muévete. No permanezcas estático frente a la computadora por mucho tiempo. Regístrate para una cuenta gratuita en la nube. Familiarízate con la plataforma OCI y completa todos los ejercicios de verificación de habilidades en el curso. También completa la preparación para el examen y toma el examen de práctica antes de presentar el examen de certificación.

Aquí en OCI estamos continuamente creando y entregando formación, integrando comentarios y monitoreando los análisis de uso. Si algo está roto o no está resonando con nuestros usuarios, queremos saberlo—y ahí es donde entran tus valoraciones.

Siéntete libre de calificar este curso y dejar comentarios específicos sobre lo que fue útil y lo que no. Estamos ajustando constantemente nuestro enfoque para ayudar a nuestra audiencia a lograr sus metas. Así que unamos fuerzas y trabajemos juntos para tu aprendizaje y certificación.</br></br>

---

### -- Consejos de Expertos: Introducción

Primero que nada, gracias por elegir tomar el curso profesional de OCI Data Science y obtener la certificación. Mi nombre es Hemant Gahankari. Soy líder principal de formación en Oracle University.

Como científico de datos o ingeniero de aprendizaje automático, nuestro trabajo diario consiste en obtener datos, preparar datos, construir y entrenar modelos, evaluar modelos, desplegar y escalar modelos, y también automatizar pipelines (flujos de trabajo) de aprendizaje automático. Con el servicio OCI Data Science y los servicios de IA, podemos realizar todas estas tareas de manera eficiente.

A través de una serie de videos con consejos de expertos, te mostraremos cómo usar algunas de las características poderosas —y al mismo tiempo fáciles de usar— del servicio de ciencia de datos y servicios de IA de OCI. Esperamos que estos videos te resulten útiles. Gracias por escuchar.</br></br>

---
### -- Introducción y Configuración

#### -- Ciencia de Datos: Introducción

Este es el módulo 1, que cubre introducción y configuración. Esta primera lección es la introducción al servicio de Ciencia de Datos en la Nube de Oracle Cloud Infrastructure. Soy Wes Pritchard, gerente principal de producto para Ciencia de Datos y Servicios de IA.

---

## 📜 Antes de entrar en ciencia de datos y Oracle

Echemos una mirada divertida a la historia y cómo llegamos aquí. En los años 1300, William Ockham, un filósofo y fraile, creía que los científicos deberían preferir teorías más simples por sobre las más complejas. El principio que lleva su nombre, conocido como la navaja de Ockham (*Ockham’s razor*), puede aplicarse al aprendizaje automático buscando la solución más simple.

A mediados de 1700, el astrónomo Tobias Mayer hizo un argumento cuantitativo de que más datos son mejores. Estudiaba los movimientos de la luna y recolectó 9 veces más puntos de datos de los necesarios, afirmando que esto hacía sus observaciones más precisas. Por esto, a menudo se le considera el primer verdadero científico de datos.

En 1952, Arthur Samuel, pionero de IBM en computación, juegos e inteligencia artificial, acuñó el término *machine learning* (aprendizaje automático). Diseñó un juego para jugar damas y descubrió que cuanto más jugaba la computadora, más aprendía estrategias ganadoras mediante la experiencia.

En 1962, el matemático John W. Tukey predijo el efecto de la computación electrónica moderna en el análisis de datos como una ciencia empírica. Sin embargo, sus predicciones ocurrieron décadas antes de la explosión del *big data* y de la capacidad para realizar análisis complejos y a gran escala.

En 1997, una supercomputadora de IBM llamada Deep Blue derrotó al gran maestro de ajedrez Garry Kasparov en solo 19 movimientos. Kasparov se rindió tras este partido. La supercomputadora, altamente avanzada, podía calcular entre 100 mil millones y 200 mil millones de posiciones en los tres minutos tradicionalmente asignados a cada jugador por jugada en ajedrez estándar.

En 2008, el Dr. DJ Patil de LinkedIn y Jeff Hammerbacher de Facebook acuñaron el término *data science* (ciencia de datos) para describir un campo de estudio emergente que se enfocaba en extraer el valor oculto de los datos recolectados en los sectores comerciales y minoristas.

Dado ese contexto histórico, veamos cómo se aplica hoy la ciencia de datos. En 2021, en medio de la pandemia global por COVID-19, el profesor y psicólogo Anthony Klotz acuñó el término *la Gran Renuncia* (*the Great Resignation*) para describir una nueva tendencia de insatisfacción y rotación en el empleo. Muchas empresas quieren rastrear, analizar y predecir los patrones de retención de sus empleados.

En este curso, usaremos la deserción de empleados (*employee attrition*) como un caso de uso para conectar nuestras actividades de aprendizaje automático con un problema empresarial del mundo real. Mejor aún, te ayudaremos a construir un modelo predictivo de ML (*Machine Learning*) por ti mismo en el laboratorio independiente para estudiantes que acompaña este curso.</br></br>

---

## 🔍 Enfoque de Oracle hacia ciencia de datos e IA

Todo gira en torno a los datos. Durante muchos años, los datos disponibles para las organizaciones eran los datos estructurados de sus aplicaciones empresariales. Y estos siguen siendo datos de negocios muy importantes, pero ciertamente no son los únicos. Las organizaciones tienen muchos tipos de datos únicos y a menudo no estructurados, provenientes de muchas fuentes diferentes: sensores de equipos, aplicaciones móviles, redes sociales, interacciones con clientes vía voz y texto, videos, imágenes, documentos, y muchos más.

Las organizaciones quieren usar **todos los datos** para producir nuevos conocimientos y nuevos productos de datos. Quieren mejorar sus operaciones creando mejores experiencias para clientes, anticipando demanda de servicios y evitando fallas de equipos que se podrían haber prevenido. La siguiente generación de problemas empresariales o escenarios exige poder usar todos los datos. Y necesitamos las capacidades que brindan la ciencia de datos, el aprendizaje automático y la inteligencia artificial para comprender y utilizar esos datos.

Oracle AI es el portafolio de servicios en la nube para ayudar a las organizaciones a aprovechar todos los datos en esta nueva generación de escenarios. Por lo tanto, la **base de todo esto son los datos**. Es como una barra en la parte inferior. Obviamente, la IA y el aprendizaje automático trabajan sobre datos y requieren datos.

Ahora, la capa superior de este diagrama son las aplicaciones, y esto se refiere de forma amplia a todas las maneras en que se consume la IA. Puede ser una aplicación, un proceso de negocio o un sistema analítico.

Entre la capa de aplicaciones y la de datos, hay dos grupos: los servicios de IA (*AI services*) en la parte superior y los servicios de aprendizaje automático (*ML services*) en la parte inferior. La diferencia entre los dos grupos es que los servicios de ML son utilizados principalmente por los científicos de datos para construir, entrenar, desplegar y administrar modelos de ML. Los científicos de datos pueden trabajar con frameworks de código abierto conocidos y con OCI Data Science. Por cierto, ese es el servicio en la nube que es el enfoque de este curso.

Los científicos de datos y especialistas en bases de datos pueden aprovechar algoritmos de ML incorporados en la base de datos de Oracle. Y un servicio importante que respalda tanto a los servicios de ML como de IA es **OCI Data Labeling** (etiquetado de datos), ya que al construir modelos de ML que trabajan con imágenes, texto o voz, se necesita **datos etiquetados** para entrenar los modelos.

Los servicios de IA contienen modelos de ML preconstruidos para usos específicos. Algunos están preentrenados y otros son entrenados por el cliente con sus propios datos. Todos se utilizan simplemente llamando a la API del servicio, enviando los datos a procesar, y el servicio devuelve un resultado. No hay infraestructura que administrar. Y aunque este curso se centrará principalmente en OCI Data Science, también incluimos algunas lecciones sobre servicios de IA y etiquetado de datos. Hay otro curso aparte que cubre ML y base de datos Oracle.

Ahora bien, esos servicios de IA y ML que acabo de mostrarte no funcionan de manera aislada. Están respaldados por muchos otros servicios disponibles en nuestra infraestructura en la nube, incluyendo análisis de negocios, análisis de grafos y muchas formas de integración y gestión de datos, todo funcionando sobre la infraestructura básica de la nube. Estos servicios pueden combinarse en varias arquitecturas para respaldar diferentes escenarios.</br></br>

---

## 🔧 OCI Data Science: visión general

Ya definimos Oracle AI y los servicios que lo componen. Ahora, veamos más de cerca Oracle Cloud Infrastructure Data Science (abreviado como OCI Data Science). Es el servicio en la nube enfocado en asistir al científico de datos durante todo el ciclo de vida de aprendizaje automático, con soporte para Python y software de código abierto. Como verás en los íconos del gráfico, el servicio tiene muchas características que cubriremos a lo largo del curso.

Ahora, repasemos los tres principios fundamentales que guían el producto:

1. **Acelerar el trabajo del científico de datos individual**. Quienes salen hoy de las universidades han sido formados usando herramientas de código abierto, y eso es lo que les resulta más cómodo. Pero usar estas herramientas en una laptop significa gestionar muchas bibliotecas de diferentes fuentes, y estar limitado por la potencia de cómputo de la máquina.

   OCI Data Science proporciona bibliotecas de código abierto junto con acceso fácil a diferentes niveles de potencia de cómputo sin necesidad de gestionar ninguna infraestructura. También incluye una biblioteca propia de Oracle para facilitar varios aspectos del trabajo del científico de datos.

2. **Colaboración**. Va más allá de la productividad individual, permitiendo que los equipos de ciencia de datos trabajen juntos. Esto se logra mediante el **compartir recursos**, lo que reduce el trabajo duplicado y apoya la **reproducibilidad y auditabilidad** de los modelos, para facilitar la colaboración y la gestión de riesgos.

3. **Calidad empresarial (*Enterprise-grade*)**.El tercer principio trata sobre ser de calidad empresarial. Eso significa que está integrado con todos los protocolos de seguridad y acceso de OCI. La infraestructura subyacente está completamente gestionada. El cliente no tiene que pensar en aprovisionar cómputo ni almacenamiento, ya que el servicio se encarga de todo el mantenimiento, actualizaciones y parches, para que los usuarios puedan enfocarse en resolver problemas empresariales con ciencia de datos.</br></br>

---

## ⚙️ Detalles específicos de OCI Data Science

Primero que nada, es un servicio en la nube para construir, entrenar, desplegar y gestionar modelos de aprendizaje automático de manera rápida. Sirve a científicos de datos y equipos de ciencia de datos a lo largo del ciclo completo de vida del aprendizaje automático, con soporte para Python y herramientas de código abierto. Los usuarios trabajan en una interfaz familiar de JupyterLab, donde escriben código Python. Y los modelos se preservan en el catálogo de modelos (*Model Catalog*) y se despliegan para gestionar la infraestructura.</br></br>

---

## 🧠 Terminología importante del producto

Vamos a cubrir algunos términos clave que se usarán a lo largo del curso. Tómate un tiempo para asimilarlos:

- **Projects (Proyectos)**: Son contenedores que permiten a los equipos de ciencia de datos organizar su trabajo. Representan espacios de colaboración para organizar y documentar recursos como sesiones de notebook y modelos. Una tenencia (*tenancy*) puede tener tantos proyectos como se necesite, sin límites.

- **Notebook Sessions (Sesiones de Notebook)**: Es donde trabajan los científicos de datos. Proveen un entorno de JupyterLab con bibliotecas de código abierto preinstaladas y la posibilidad de agregar más. Son entornos interactivos para codificar, construir y entrenar modelos. Estas sesiones corren sobre infraestructura gestionada, y el usuario puede seleccionar CPU o GPU, el tipo de cómputo (*compute shape*) y la cantidad de almacenamiento sin necesidad de aprovisionar manualmente.

- **Conda**: Sistema de gestión de entornos y paquetes de código abierto, creado para programas en Python. Se utiliza en el servicio de ciencia de datos para instalar, ejecutar y actualizar paquetes con sus dependencias rápidamente. Conda permite crear, guardar, cargar y alternar entre entornos de forma sencilla dentro del notebook.

- **ADS SDK (Accelerated Data Science Software Development Kit)**: Es una biblioteca en Python incluida en OCI Data Science. Tiene muchas funciones y objetos que automatizan o simplifican pasos del flujo de trabajo en ciencia de datos: conexión a datos, exploración, visualización, entrenamiento con AutoML, evaluación y explicación de modelos. Además, ofrece una interfaz sencilla para acceder al catálogo de modelos y otros servicios de OCI, incluyendo almacenamiento de objetos (*Object Storage*).

---

## 🔍 Modelos, Catálogo y Despliegue

- **Modelos**: Definen una representación matemática de tus datos y negocio. Se crean en sesiones de notebook dentro de proyectos.

- **Model Catalog (Catálogo de Modelos)**: Lugar donde se almacenan, rastrean, comparten y gestionan los modelos. Es un repositorio centralizado y gestionado de artefactos de modelos. Incluye metadatos sobre el origen del modelo, información relacionada con Git, y el script o notebook usado para subirlo al catálogo. Los modelos almacenados pueden compartirse entre miembros del equipo y volverse a cargar en una sesión de notebook.

- **Model Deployments (Despliegue de Modelos)**: Permite desplegar modelos desde el catálogo como endpoints HTTP sobre infraestructura gestionada. Este tipo de despliegue como aplicaciones web que sirven predicciones en tiempo real es la forma más común de operacionalizar modelos. Los endpoints HTTP son flexibles y pueden procesar solicitudes de predicción.

---

## 🚀 Tareas, Accesos y Regiones

- **Data Science Jobs (Tareas de Ciencia de Datos)**: Permiten definir y ejecutar tareas repetibles de aprendizaje automático en infraestructura gestionada.

- **OCI Console**: Método más común de acceso. Proporciona una interfaz basada en navegador, fácil de usar, que da acceso a las sesiones de notebook y todas las características del servicio. Esta será la interfaz usada durante el curso.

- **REST API**: Proporciona acceso programático a las funcionalidades del servicio. Hay documentación con referencia de la API.

- **SDKs (Kits de desarrollo)**: OCI ofrece SDKs para varios lenguajes de programación (Java, Python, TypeScript, JavaScript, .NET, Go, Ruby). Estos permiten escribir código para gestionar recursos del servicio. Se mostrarán ejemplos del uso del SDK de Python para desplegar modelos y crear tareas.

- **CLI (Command Line Interface)**: Ofrece acceso rápido y funcionalidad completa sin necesidad de scripting.

- **Regions (Regiones)**: OCI Data Science como servicio en la nube está disponible a través de regiones, que son centros de datos distribuidos globalmente, ofreciendo entornos seguros y de alto rendimiento local. Esto lo hace accesible en todo el mundo para sectores comerciales, gubernamentales y dedicados. Oracle agrega nuevas regiones frecuentemente, más información en [oracle.com/cloud](https://oracle.com/cloud).

---

## 📚 ADS SDK Overview

Hola, bienvenido a este módulo sobre el SDK de Accelerated Data Science. Soy John Peach, científico de datos en el equipo de OCI Data Science Service.

En este módulo obtendrás una comprensión general del ADS SDK, sus metas y capacidades. ADS SDK fue diseñado por y para científicos de datos. Cubre todo el ciclo de vida del aprendizaje automático, con el objetivo de integrar los servicios de OCI en flujos de trabajo típicos de ciencia de datos.

Por ejemplo, se integra con Autonomous Database y el servicio de Big Data mediante clases como *SecretKeeper*, que facilitan el almacenamiento seguro de credenciales y el acceso a esos servicios.

También busca mejorar tareas comunes como análisis exploratorio con *Feature Types* (tipos de características), y optimización de hiperparámetros mediante *ADSTuner*. Además, ADS ofrece AutoML y funcionalidades de *explainability* (explicabilidad de modelos).

Hay dos versiones de ADS:

- Una pública disponible en GitHub o instalable desde PyPI.
- Otra especial que viene incluida en ciertos packs dentro del servicio de Oracle Cloud, que contiene las funcionalidades de AutoML y explicabilidad.

Se puede acceder al SDK de varias formas. Está instalado en los entornos *Conda* dentro del servicio de Data Science, listo para usarse. También puede instalarse desde PyPI o GitHub mediante el comando `pip install`.

---

## 🌟 Funciones clave de ADS

- **Conexión a fuentes de datos**: ADS provee conectores a muchas ubicaciones populares de datos.

- **Visualización de datos**: ADS tiene gráficos inteligentes (*smart plotting*) con ajustes predeterminados según el tipo de datos. También permite visualizar según tipos de característica, correlaciones y relaciones entre variables.

- **Ingeniería de características (Feature Type Engineering)**: ADS analiza los datos y da recomendaciones para transformar características y mejorar modelos.

- **Entrenamiento de modelos**: ADS permite entrenar modelos con AutoML de Oracle Labs o afinar hiperparámetros con ADSTuner. Tiene clases que empaquetan rápidamente modelos para su despliegue.

- **Evaluación de modelos**: ADS incluye clases para evaluar desempeño de modelos con pocas líneas de código.

- **Interpretabilidad de modelos**: Entender y explicar lo que el modelo está aprendiendo es esencial para confiar en él y comunicarlo a otros.

- **Despliegue de modelos**: ADS lo facilita con clases para los tipos de modelos más comunes, y también para modelos genéricos. Con unas pocas líneas de código, el modelo puede ponerse en producción.

---

## 🔗 Conexión a fuentes de datos

Los datos están almacenados en muchos lugares, y necesitas poder acceder a ellos. A menudo, los datos son demasiado grandes para caber en tu sesión de notebook. Puedes usar ADS para limitar la transferencia de datos por la red.

**Almacenamiento local** es una ubicación común para guardar tus datos. Este es el almacenamiento en bloques dentro de la sesión de notebook. ADS proporciona acceso fácil a eso.

Para conjuntos de datos más grandes o para compartir conjuntos de datos, se utiliza comúnmente el **almacenamiento de objetos** (*Object Storage*). ADS utiliza el protocolo **APE Spec** para permitirte usar *pandas* y acceder al almacenamiento de objetos como si estuviera en tu disco local. Esto se realiza mediante el protocolo de OCI y *pandas* cuando el archivo está en almacenamiento de objetos.

Gran parte de nuestros datos están en **bases de datos Oracle**. ADS proporciona una conexión fácil a estas bases de datos. Herramientas como **Oracle DB Secret Keeper** permiten almacenar credenciales de inicio de sesión en el archivo **DTP Wallet** dentro de un **OCI Vault**, de modo que no tengas que exponer esa información en tu notebook.

**ADB Secret Keeper** funciona con Autonomous Database. ADS proporciona integración con proveedores de nube de terceros. Con ADS instalado, *pandas* puede conectarse a proveedores como S3, Google Cloud Storage, Azure Data Lake Storage, Azure Blob Service, Dropbox y muchos más.

Para datos no relacionales, ADS proporciona acceso mediante la clase **Data Set Factory** para hacer conexiones simples con bases de datos NoSQL, ejecutar consultas y devolver resultados.

**OCI Big Data Service** es un servicio basado en Hadoop que utiliza **HDFS** como sistema de archivos.

ADS permite conectarse fácilmente a BDS sin necesidad de copiar los datos al almacenamiento local. También proporciona acceso a la web usando HTTP y HTTPS para leer archivos directamente hacia un dataframe.

---

## 📊 Visualización de Datos

El análisis exploratorio de datos es crítico para entender tus datos. Puede llevar tiempo crear y desechar clases, solo para tener que crearlas nuevamente la próxima vez que uses datos similares.

Las clases **Feature Type** proporcionan los mismos valores predeterminados para visualizar tus datos. También es muy fácil crear tipos de características personalizados para visualizar según tus preferencias. Luego, puedes reutilizar estas visualizaciones en diferentes proyectos o en toda la organización.

Además, el sistema de tipos de características proporciona **estadísticas resumidas**, **visualizaciones resumen** de cada característica y **mapas de calor de correlaciones**.

La **ingeniería de características** puede ser un problema desafiante. Puede mejorar enormemente la calidad de tu modelo tomando características existentes y generando nuevas a partir de ellas—transformando los datos que tienes en otros tipos de relaciones que el modelo pueda aprender.

ADS tiene funcionalidad integrada para apoyar esto. Hay una clase llamada **ADS Data Set** que envuelve un dataframe de *pandas*. Proporciona sugerencias de transformación y puede hacerlo automáticamente. Soporta codificación categórica, valores nulos e imputación. Puede ofrecer recomendaciones sobre qué cambios hacer a tus datos para crear mejores características.

---

## 🧪 Entrenamiento de Modelos

Una vez que tengas tus datos preparados, es hora de crear un modelo. ADS puede automatizar completamente este proceso usando tecnología **Auto Machine Learning**.

Puede probar muchos tipos diferentes de clases de modelo, ajustar hiperparámetros y proporcionar métricas de desempeño para cada modelo.

**ADSTuner** realiza la **optimización de hiperparámetros**. Una vez entrenado el modelo, ADS también puede empaquetar los archivos necesarios para crear un **artifact del modelo**, guardar ese artifact en el catálogo de modelos (*Model Catalog*), y luego puedes enviarlo a producción. Ya no necesitas luchar para poner tu modelo en producción.

---

## 📈 Evaluación de Modelos

Si tienes uno o varios modelos, puede que necesites entender el rendimiento y compararlos. **ADS Evaluator** permite realizar comparaciones entre modelos diferentes. Ofrece herramientas comunes, métricas y gráficos.

Entiende clasificación **binaria**, **multinomial** y **regresión**, y genera métricas y gráficos apropiados para el tipo de problema. Ya no necesitas regenerar constantemente estos gráficos o verificar si estás usando los correctos. ADS lo hace automáticamente por vos.

---

## 🔍 Interpretabilidad del Modelo y Explicabilidad

Puedes desarrollar confianza en tu modelo si puedes explicar lo que ha aprendido y lo que está haciendo. Interpretar el comportamiento del modelo es clave para entender qué hace y qué mejoras pueden aplicarse en versiones futuras.

ADS ofrece herramientas para interpretar modelos que son **agnósticas al tipo de modelo**, es decir, no dependen del tipo de modelo que se haya construido.

Proporciona explicaciones mediante el módulo de ADS que son interpretables, agnósticas y ofrece herramientas para hacer **tests de escenarios hipotéticos** (*what-if*): cambiar valores de entrada y observar cómo responde el modelo.

También ofrece **explicabilidad local**, es decir, permite entender por qué el modelo hizo una determinada predicción sobre una observación específica. Y ofrece **explicabilidad global**, para comprender qué ha aprendido el modelo y cómo se comporta.

Lo hace mediante gráficos como **Partial Dependence Plots** y **ALE Plots** (*Accumulated Local Effects*), para entender el comportamiento general. Usalos para verificar si el modelo está aprendiendo lo que debería y entender las relaciones entre los datos.

---

## 🚀 Despliegue de Modelos

Muchos científicos de datos enfrentan un gran desafío al poner sus modelos en producción. Lo tienen corriendo en su notebook, pero ¿cómo hacerlo escalable y seguro?

ADS proporciona el **ADS Model Framework**, un conjunto de clases que permite desplegar modelos de distintos tipos. Con unos pocos comandos, podés poner un modelo en producción.

ADS soporta colecciones de modelos como **Oracle Labs AutoML**, **PyTorch**, **scikit-learn**, **TensorFlow**, y muchos más.

También tiene la capacidad de soportar **modelos genéricos**. No importa el tipo de modelo que uses, puede ser desplegado con unos pocos comandos.

Una vez que tu modelo está en producción, necesitas entender qué está ocurriendo. Se integra con el servicio de **OCI Logging**, y crea **logs de predicción y acceso**. Esto te permite ver cómo se accede al modelo y cuáles fueron los resultados de predicción.

---

## 🧾 Recapitulación del Módulo

En este módulo aprendiste que los objetivos del SDK son tres:

- Acceder e instalar la biblioteca ADS.
- Conectar a diferentes fuentes de datos y visualizar rápidamente el análisis exploratorio.
- Recibir guía para la ingeniería de características, entrenamiento y optimización de modelos.

También aprendiste cómo evaluar modelos, entender su calidad, interpretarlos, y herramientas para desplegarlos en producción.

Muchas gracias.

---

## 🧩 Conceptos Básicos de Configuración de Tenancy

Hola, soy Jon Stanesby. En esta lección vamos a cubrir los conceptos básicos de configuración de **tenancy** para ciencia de datos.

Aunque es conocimiento común y probablemente solo un repaso para vos, repasemos rápidamente estos conceptos:

- **Compartments (Compartimientos)**: Son contenedores lógicos para organizar recursos de OCI.
- **User Groups (Grupos de Usuarios)**: Simplemente un grupo de usuarios.
- **Dynamic Groups (Grupos Dinámicos)**: Grupos especiales de *principals* de recursos.
- **Policies (Políticas)**: Se usan para otorgar acceso a grupos dentro de compartimientos.

Veamos cómo estos componentes trabajan juntos para habilitar el acceso a los recursos de ciencia de datos:

1. Asignás usuarios a grupos de usuarios apropiados.
2. Creamos grupos dinámicos para recursos de ciencia de datos.
3. Finalmente, se crean políticas que otorgan acceso a esos recursos dentro de un compartimiento.

---

## 🧩 Compartimientos

Empezando entonces con los **compartimientos**, estos te permiten organizar y controlar el acceso a tus recursos en la nube. Un compartimiento es un agrupamiento lógico de recursos que solo pueden ser accedidos por ciertos grupos. Se les ha otorgado permiso por parte de un administrador.

Al configurar tu tenencia (*tenancy*), el primer paso es hacer un plan sobre cómo vas a organizar tus recursos de ciencia de datos de ahora en adelante. Una vez que tengas el plan, puedes comenzar a crear uno o varios compartimientos. Mostraremos esto al final de la lección. Por ahora, veamos el proceso rápido y sencillo de tres pasos para crear un compartimiento:

Desde la consola de Identidad, ve a **Identity** y selecciona **Compartments**. Haz clic en **Create Compartment**, ingresa un nombre y una descripción, y luego haz clic en **Create Compartment**.

---

## 👥 Grupos de usuarios

Pasando ahora a los **grupos de usuarios**, son usuarios individuales que se agrupan en OCI y se les otorga acceso a los recursos de ciencia de datos dentro de los compartimientos.

Los administradores pueden realizar tres pasos simples para crear grupos de usuarios:

1. Crear los usuarios.
2. Crear los grupos.
3. Agregar usuarios a los grupos.

Al configurar grupos, primero decidí cómo accederán los usuarios a los recursos dentro de los compartimientos.

---

## 🔄 Grupos dinámicos

Ahora, sobre un tipo especial de grupo llamado **grupos dinámicos** (*dynamic groups*), contienen recursos que coinciden con reglas que vos definís. Recursos como sesiones de notebook de ciencia de datos, ejecuciones de tareas (*job runs*), y despliegues de modelos pueden incluirse en un grupo dinámico.

Estas reglas permiten que la membresía del grupo cambie dinámicamente a medida que se crean o eliminan recursos que coincidan con esas reglas.

Estos recursos actúan como **principales** (*principal actors*). Pueden hacer llamadas a la API de servicios de acuerdo con las políticas que hayas escrito para el grupo dinámico. Veremos políticas en breve.

Por ejemplo: usando el principal de recurso de una sesión de notebook en ciencia de datos, donde su grupo dinámico tiene una política que habilita el acceso a almacenamiento de objetos, podrías hacer una llamada a la API de Object Storage para leer datos desde un bucket.

Entonces, los recursos coinciden con reglas, y las reglas se aplican a grupos dinámicos. Una vez que le das a tu grupo dinámico un nombre y una descripción, llenás las reglas de coincidencia (*matching rules*), donde el OCID del compartimiento es reemplazado por el identificador del compartimiento que creaste para ciencia de datos.

En este ejemplo, con estas reglas, el grupo dinámico estará compuesto por todos los recursos de esos tres tipos que existan en el compartimiento. Lo que estos recursos pueden hacer, como se mencionó antes, dependerá de las **políticas**.

---

## 🛡️ Políticas

Las **políticas** definen qué principales, como usuarios y recursos, tienen acceso en OCI. El acceso se otorga a nivel de grupo y de compartimiento, lo que significa que podés escribir una política que dé a un grupo un tipo específico de acceso dentro de un compartimiento específico.

Las políticas tienen una sintaxis básica:

> `allow group nombre-del-grupo to do acción on tipo-de-recurso in compartment nombre-del-compartimiento`

Veamos más de cerca cada variable de la sintaxis:

- **Group name**: nombre del grupo de usuarios o grupo dinámico.
- **Verb (Verbo)**: define el nivel de acceso. Veremos los tipos de verbo a continuación.
- **Resource type**: especifica el tipo de recurso o familia de recursos.
- **Compartment name**: nombre del compartimiento.

---

## ✅ Tipos de verbos (acciones permitidas)

Los verbos definen el nivel de acceso permitido al recurso o familia de recursos. De menor a mayor permisividad:

- `inspect`: permite listar recursos sin acceder a metadatos definidos por el usuario.
- `read`: incluye inspect + acceso a metadatos y al recurso mismo.
- `use`: incluye read + posibilidad de trabajar con el recurso (por ejemplo, actualizar). No suele incluir crear o eliminar.
- `manage`: incluye todos los permisos, incluyendo creación y eliminación.

---

## 🧬 Tipos de recursos

El tipo de recurso en la política define para qué recurso estás escribiendo la política. Por ejemplo, “data science” incluye modelos y tareas de ciencia de datos.

Para facilitar la escritura de políticas para recursos relacionados, hay tipos **agregados** que abarcan familias. El tipo agregado para ciencia de datos es `data-science-family`.

🔸 Importante: estos son ejemplos **críticos** de políticas requeridas, no simplemente ilustraciones.

1. Política para permitir que científicos de datos gestionen todos los recursos de ciencia de datos en un compartimiento específico:

```plaintext
allow group tu-grupo-de-usuarios to manage data-science-family in tu-compartimiento
```

2. Política para permitir que recursos de ciencia de datos (como notebook sessions), dentro de un grupo dinámico que hayas creado, gestionen todos los recursos de ciencia de datos:

```plaintext
allow dynamic-group tu-grupo-dinamico to manage data-science-family in tu-compartimiento
```

---

## 📊 Políticas para métricas y logs

Las siguientes políticas permiten acceso a métricas y registros (*logging*):

- Permitir que el grupo de usuarios lea métricas:

```plaintext
allow group tu-grupo to read metrics in compartment tu-compartimiento
```

- Permitir que el grupo dinámico use contenido de logs:

```plaintext
allow dynamic-group tu-grupo to use log-content in compartment tu-compartimiento
```

- Permitir que el grupo de usuarios gestione grupos de logs:

```plaintext
allow group tu-grupo to manage log-groups in compartment tu-compartimiento
```

- Permitir que el grupo de usuarios use contenido de logs:

```plaintext
allow group tu-grupo to use log-content in compartment tu-compartimiento
```

---

## 🌐 Políticas para red personalizada

Si planeás usar networking personalizado (tema del próximo módulo), necesitarás estas políticas:

- Para el servicio de data science:

```plaintext
allow service data-science to use virtual-network-family in compartment tu-compartimiento
```

- Para el grupo de usuarios:

```plaintext
allow group tu-grupo to use virtual-network-family in compartment tu-compartimiento
```

- Para el grupo dinámico:

```plaintext
allow dynamic-group tu-grupo to use virtual-network-family in compartment tu-compartimiento
```

---

## 🛠️ Creación de recursos en la consola de Identidad

- **Crear un compartimiento**: ir a Compartments → Create Compartment → agregar nombre, descripción y etiquetas (opcional). Esperar unos momentos hasta su creación. Anotar el OCID para uso posterior.

- **Crear un usuario**: ir a Users → Create User → añadir nombre de usuario, descripción y correo electrónico. Repetir para cada usuario que desees agregar.

- **Crear un grupo de usuarios**: ir a Groups → Create Group → añadir nombre y descripción → Create. Luego, hacer clic en Add User to Group, seleccionar el usuario y confirmar.

- **Crear grupo dinámico**: ir a Dynamic Groups → Create Dynamic Group → añadir nombre y descripción. Luego ingresar las reglas de coincidencia:

   1. Para sesiones de notebook.
   2. Para despliegues de modelos.
   3. Para ejecuciones de tareas.

   Sustituir el ID del compartimiento por el que creaste antes. Hacer clic en Create para finalizar.

---

## 🔐 Paso final: crear políticas para habilitar acceso

Ahora, para el paso final, necesitamos permitir que nuestros recursos y usuarios accedan a ciencia de datos en nuestro compartimiento. Para esto vamos a crear una **política**.

En esta política, voy a cubrir las políticas requeridas para ciencia de datos. Le doy un nombre y descripción relevante. En el **Policy Builder**, cambio al editor manual para poder pegar mis declaraciones de política. Una vez agregadas, hago clic en **Create** para crear la política.

Había algunas políticas adicionales requeridas, específicamente para que usuarios y grupos dinámicos accedan a métricas. Así que edito esta política y agrego las siguientes declaraciones:

- Que mi grupo de usuarios pueda leer métricas en el compartimiento.
- Que mi grupo dinámico acceda a contenido de logs.
- Que mi grupo de usuarios acceda a grupos de logs.
- Finalmente, que mi grupo de usuarios acceda a contenido de logs.

Una vez agregadas estas declaraciones, guardo mis cambios.

Ya que cubrimos las políticas requeridas, mostramos algunas políticas **útiles** que también conviene crear, especialmente cuando queremos que los recursos o usuarios de un servicio de ciencia de datos accedan a otros servicios de OCI.

En este caso, estoy agregando **políticas útiles** para ciencia de datos. Nuevamente, les doy un nombre y una descripción, y cambio al editor manual para agregarlas. Estas políticas son específicas para **Object Storage**, así que quiero permitir que **mi grupo dinámico y mi grupo de usuarios** gestionen la familia de objetos (*object-family*) en mi compartimiento. Puedo repetir este proceso para todas las políticas que quiera agregar.

---

## 🧭 Resumen de conceptos de configuración de tenencia

- Compartimientos
- Grupos de usuarios
- Grupos dinámicos
- Políticas

Repasamos reglas de coincidencia para agrupar recursos en grupos dinámicos, la sintaxis de las políticas y sus variantes. Discutimos las políticas requeridas para ciencia de datos, las relacionadas, y algunas opcionales que pueden resultar útiles.

Gracias.

---

## ⚙️ Configurar la tenencia con OCI Resource Manager

Hola, soy John Stanesby. En esta lección vamos a mostrar cómo configurar una tenencia con **OCI Resource Manager**.

En vez de configurar tu tenencia manualmente, podés usar la **plantilla del servicio de ciencia de datos** que viene preconfigurada en Oracle Resource Manager. Esta plantilla crea automáticamente los grupos de usuarios, grupos dinámicos y políticas requeridas para un caso básico.

La plantilla crea:

- Un grupo de usuarios (nombre definido por vos).
- Un grupo dinámico (nombre definido por vos).
- Reglas de coincidencia para: `datasciencenotebooksession`, `datasciencemodeldeployment`, `datasciencejobrun`.

También crea una política con las siguientes declaraciones:

- Permitir que el grupo de usuarios gestione `data-science-family` en el compartimiento.
- Permitir que el grupo dinámico gestione `data-science-family` de recursos en el compartimiento.
- Permitir que el grupo de usuarios lea métricas en el compartimiento.
- Permitir que el grupo dinámico use contenido de logs en el compartimiento.

Haremos una demo al final de la lección.

---

## 🔁 Proceso general para usar el ORM Stack

1. Crear el **Stack**.
2. Seleccionar tu plantilla.
3. Seleccionar el compartimiento.
4. Ejecutar el stack.
5. Agregar usuarios al grupo creado.

Recordá: las plantillas solo están disponibles en la consola. Y podés editar tu stack en cualquier momento.

---

## 🧱 Opciones alternativas

Además de usar la plantilla de muestra, también podés usar tu propio **script Terraform**, ubicado en este repo público de GitHub.

Ahora voy a mostrar la configuración de una tenencia con OCI Resource Manager:

- Navegar a Resource Manager → Stacks → Create Stack.
- Seleccionar **Template** como origen.
- Ir a **Service** y elegir **Data Science** → Select Template.
- Elegir el compartimiento deseado → Next.
- Completar variables adicionales si querés → Next.
- Ejecutar `apply` sobre el stack → Click Create.
- Esperar que corra el job.
- Una vez creado, solo necesitás agregar tus usuarios al grupo generado.

También podés acceder al script Terraform en el repo público de GitHub.

---

## 📡 Networking para Ciencia de Datos

Hola, soy Jon Stanesby. En esta lección veremos **networking en ciencia de datos**. Vamos a presentar algunos componentes útiles de red en la nube, con una introducción de alto nivel para entender cómo se relacionan con ciencia de datos. Este curso no entra en profundidad sobre networking.

### 🔧 Componentes clave:

- **VCN (Virtual Cloud Network)**  
- **Subnets**
- **VNICs (Virtual Network Interface Cards)**
- **DRG (Dynamic Routing Gateway)**
- **NAT Gateway (Network Address Translation)**
- **Service Gateway**

---

## 🔌 Cómo trabajan juntos

- El **VCN** es una red privada virtual que configurás en los data centers de Oracle.
- Las **subnets** son subdivisiones dentro de un VCN. Contienen **VNICs**, que se adjuntan a instancias.
- Todas las VNICs en una subnet comparten las mismas políticas de red: tabla de rutas, listas de seguridad y opciones DHCP.

---

### 🚪 Enrutadores virtuales opcionales

1. **DRG**: Provee ruta de tráfico privado entre el VCN y tu red on-premise.  
   Se puede usar para establecer conexión mediante VPN sitio a sitio o **FastConnect**.

   También conecta tu VCN con otro VCN en otra región.

   Da acceso a internet para recursos sin IP pública, sin exponerlos a conexiones entrantes.

2. **Service Gateway**: Permite tráfico privado entre tu VCN y servicios de Oracle.  
   Ejemplo: sistemas de bases de datos en subnet privada pueden respaldar datos en Object Storage sin IP pública ni acceso a internet.

---

## 🖥️ Workloads en ciencia de datos

Podés crear varios tipos de recursos que ejecutan código para distintos usos:

- **Notebook sessions**
- **Jobs y job runs**
- **Model deployments**

En esta lección los llamaremos **workloads**.

Muchas veces vas a querer acceder a recursos externos desde tu workload: archivos de código, datos, bibliotecas, secretos y logs.

También podrías querer ejecutar otros workloads en Data Science o en otra plataforma como Data Flow.

Estos recursos externos pueden estar en internet público o en una red privada.

---

## 🌐 Patrones de Networking

Para acceder a estos recursos, necesitás conectividad entre tu workload y la ubicación de red donde estén.

Hay **dos patrones de red** que podés usar:

1. **Default networking**:  
   El workload se conecta mediante una VNIC secundaria a una subnet gestionada por el servicio.

   Esta subnet permite salida a internet por un **NAT Gateway** y acceso a servicios de OCI vía **Service Gateway**.

   Si solo necesitás acceso a internet y/o servicios OCI, esta es la forma más rápida y sencilla de comenzar, ya que no requiere crear recursos de red propios ni escribir políticas de permisos.

---

## 🌐 Configuración personalizada de red

Cuando seleccionás **custom networking** (red personalizada) al crear un recurso de ciencia de datos, vas a especificar una **subnet preexistente** que pertenezca a tu tenencia y que querés usar para los workloads (cargas de trabajo) de ciencia de datos. Cuando se crea el workload, el servicio de ciencia de datos se conectará a tu subnet seleccionada mediante una conexión secundaria con VNIC (interfaz de red virtual).

Esta configuración de “trae tu propia red” (*bring-your-own-network*) mediante red personalizada te permitirá acceder a los recursos y activos definidos por tu subnet.

Si necesitás acceso a activos externos dentro de una **red privada**, como archivos de código en un servidor empresarial de Git o datos en una base de datos on-prem, vas a necesitar usar **custom networking** para asegurar la conectividad de tus workloads. Por favor, trabajá con el administrador de red de tu tenencia para configurar tu subnet VCN para ciencia de datos.

Como se discutió en la lección sobre configuración de tenencia, necesitarás **políticas adicionales** para usar red personalizada en ciencia de datos.

---

## 🧰 Asistente de configuración rápida de red (VCN Wizard)

Voy a mostrarte una forma rápida de configurar red para ciencia de datos. Para hacerlo, vamos a usar el **VCN Wizard**.

- Navegá a **Networking > Virtual Cloud Networks**.
- Hacé clic en **Start VCN wizard**, y luego elegí **Create VCN with Internet Connectivity**.
- Al iniciar el asistente, solo necesitás darle un **nombre** a tu VCN.

Al desplazarte hacia abajo, verás varias opciones que suelen usar los usuarios avanzados. Si querés continuar con la red por defecto, simplemente hacé clic en **Next** y luego en **Create**.

Esperá un momento mientras se crean varios recursos dentro de tu compartimiento. Una vez finalizado, hacé clic en **View Virtual Cloud Network**.

Ahora podemos ver que nuestra red ha sido creada. Si vuelvo a la pantalla de **Virtual Cloud Network**, puedo ver que mi ejemplo *DS VCN* ya fue creado.

📝 *Nota: no necesitás realizar este paso si configuraste tu tenencia usando OCI Resource Manager, ya que el VCN se crea automáticamente.*

---

## 🧵 Conectividad: red por defecto vs red personalizada

En esta lección vimos:

- Componentes y definiciones de red en la nube.
- Cómo se combinan esos componentes.
- Las dos opciones de conectividad: **default networking** o **custom networking**.

---

## 🔑 Autenticación en APIs de OCI

Hola, soy Jon Stanesby. En esta lección veremos cómo autenticarse en las **APIs de OCI**.

Los recursos de ciencia de datos (como notebook sessions, jobs y model deployments) te permiten ejecutar código personalizado.

Como parte de tu código, podrías querer interactuar con otros servicios de OCI mediante las APIs REST. Esto permitiría, por ejemplo, leer o escribir datos en Object Storage desde un job, o crear/ejecutar aplicaciones de Data Flow desde una notebook session.

Para interactuar con las APIs de OCI, necesitás operar como un **usuario autenticado**.

En ciencia de datos, los métodos más comunes para interactuar con las APIs de OCI son:

- **ADS SDK**
- **OCI Python SDK**
- **OCI Command Line Interface (CLI)**

Esta lección explica las opciones de autenticación para cada uno de estos interfaces.

📌 *Importante: esta lección solo trata sobre autenticación (verificación de identidad reconocida por OCI), no sobre autorización (nivel de acceso), ya cubierto en la lección 2 del módulo de configuración de tenencia.*

---

## 👥 Principios de recurso (Resource Principals)

Un **resource principal** es una funcionalidad de IAM (Identity and Access Management) que permite que los recursos sean actores principales autorizados para realizar acciones sobre otros servicios.

Cada recurso tiene su propia identidad, y se autentica usando certificados que se le asignan automáticamente. Estos certificados son creados, asignados y rotados sin que vos tengas que guardar credenciales en tu sesión de notebook o job.

El servicio de ciencia de datos permite autenticarse usando el **resource principal** de la notebook session o de la ejecución del job para acceder a otros recursos de OCI. Este método es más seguro que usar configuración de OCI y claves API.

Además, es más práctico para jobs que no tienen una interfaz interactiva como la notebook para crear y mover archivos de configuración.

🔐 *Si no usás explícitamente resource principals al invocar un SDK o CLI, se usará el enfoque tradicional de archivo de configuración + clave API.*

---

## ⏳ Token de resource principal

- Se **almacena en caché por 15 minutos**.
- Si cambiás la política o el grupo dinámico, deberás **esperar 15 minutos** para que el cambio tenga efecto.
- El código para establecer resource principal como mecanismo de autenticación varía levemente según el interfaz usado.

📌 Puede ser útil **pausar la lección y anotar los ejemplos de código**.

---

## 👤 Autenticarse como usuario IAM personal

Podés operar como tu propio usuario IAM creando:

- Un **archivo de configuración de OCI**.
- Una **clave API (.pem)**

Este es el método por defecto con ADS, OCI SDK de Python o CLI.

Para autenticarte con este enfoque, debés:

1. Subir tu archivo de configuración de OCI a la carpeta `oci/` dentro de la notebook session.
2. Subir o crear los archivos `.pem` necesarios para el perfil definido.

📓 *En vez de subir archivos existentes, podés usar el notebook `api_key` para generarlos.*

- Para lanzarlo, hacé clic en **Notebook Examples** desde la pestaña de **JupyterLab Launcher**.

---

## 🧾 Recapitulación

En esta lección cubrimos:

- La importancia de la autenticación en ciencia de datos.
- La necesidad de autenticar diferentes interfaces.
- Definición de resource principals.
- Cómo se combinan con el servicio de ciencia de datos.
- Cómo trabajar con resource principals en distintos entornos.
- Uso de archivos de configuración de OCI.

</br>
</br>
</br>




---
<h1>## 🧠 Unidad 3: Diseño y configuración del espacio de trabajo</h1>

### 🎓 Módulo 2: Workspace Design and Setup  
Instructor: *John Stanseby*
---

<h2>Projects</h2>
## 📌 Tema central: El proyecto como componente principal

Un **proyecto de ciencia de datos** en OCI es un espacio colaborativo donde los equipos organizan su trabajo en torno a un caso de uso o pregunta de negocio.  
Todos los recursos de ciencia de datos (como notebooks y modelos) se crean **dentro de un proyecto**.

---

## 🛠️ Creación de proyectos

### 1. Desde la **Consola de OCI**

Pasos:
- Iniciar sesión con políticas adecuadas
- Ir a **Analytics & AI → Machine Learning → Data Science**
- Clic en **Create Project**
- Seleccionar el **compartimento**

Opciones recomendadas:
- **Nombre único** (si no se define, se genera automáticamente con timestamp)
- **Descripción** (útil para otros usuarios)
- **Tags decorativos**: seleccionar namespace, clave y valor  
  → Para más de un tag: clic en *Add Additional Tags*

Al finalizar:
- Clic en **View Detail page** y luego en **Create**
- Se habilita la creación de notebooks y modelos asociados al proyecto

---

### 2. Desde el **SDK de ADS (Python)**

Usar el objeto `ProjectCatalog` y el método `create_project`, especificando el `compartment_id`.  
Ejemplo: usar la variable de entorno del notebook para crear el proyecto en el mismo compartimento.

---

## 🧾 Gestión de proyectos

### 🔍 Visualización
- Ir a la **Project List page**
- Clic en un proyecto para ver detalles:  
  - Nombre, descripción  
  - OCID  
  - Fecha y autor de creación  
  - Tags

### ✏️ Edición
- Solo se pueden editar:  
  - Nombre  
  - Descripción  
  - Tags (desde el menú de detalles)

### 🗑️ Eliminación
- Requisito: el proyecto debe estar **vacío**
- Eliminar notebooks, modelos y recursos asociados primero
- Confirmar escribiendo el **nombre exacto** del proyecto
- Estado pasa a **"deleting"**, luego a **"deleted"**
- Se puede filtrar por estado (ej. ocultar los eliminados)

---

## 🧩 Consideraciones clave

| Elemento | Recomendación |
|---------|----------------|
| Nombre | Único, descriptivo |
| Descripción | Breve, clara, útil para terceros |
| Tags | Decorativos, funcionales, agrupables |
| Compartimento | Bien definido, con políticas IAM adecuadas |
| Eliminación | Solo si está vacío, con confirmación exacta |

---

<h2>Notebook Sessions en OCI</h2>

### 🧠 ¿Qué son?
- Interfaces JupyterLab gestionadas por OCI para construir y entrenar modelos ML.
- Infraestructura totalmente administrada: no requiere interacción directa con APIs de cómputo o almacenamiento.

### ⚙️ Características clave
- Soporte para CPU y GPU (AMD, Intel, Nvidia).
- Almacenamiento persistente para datos, notebooks y entornos.
- Actualizaciones y parches automáticos.
- Escalables: podés cambiar forma de cómputo y tamaño de almacenamiento.

### 🛠️ Creación desde la consola
1. Crear un proyecto.
2. Ir a la página de detalles del proyecto → *Create notebook session*.
3. Seleccionar compartimento (`HotelConciliacionML`, por ejemplo).
4. Elegir forma de cómputo (ej. Standard 2.2).
5. Definir tamaño de almacenamiento (mínimo 50 GB).
6. Configurar red (default o custom con VCN y subnet).
7. Agregar tags decorativos.
8. Click en *Create* → tarda unos minutos en activarse.

### 📋 Gestión de sesiones
- **Visualización**: desde la lista de sesiones o detalles del proyecto.
- **Edición**: solo el nombre es editable cuando está activa.
- **Eliminación**: requiere confirmar el nombre; se destruye instancia y volumen.
- **Activación/Desactivación**:
  - Activar: permite escalar recursos.
  - Desactivar: apaga instancia pero conserva el volumen (excepto boot volume).
  - Reactivar: se crea nueva instancia y se adjunta el volumen anterior.

### 📊 Métricas disponibles
- Uso de CPU y memoria.
- Tráfico de red (bytes in/out).

---
<h2>JupyterLab</h2>

## 🧪 Unidad: Cómo trabajar con JupyterLab en OCI

### 🧠 ¿Qué es JupyterLab?
- Interfaz web de próxima generación para notebooks.
- Utilizada en las *notebook sessions* de OCI por su familiaridad con data scientists.
- Permite integrar notebooks, editores de texto, terminales y componentes personalizados.

---

## 📦 Funcionalidades principales

### 🔹 Soporte de formatos
- Compatible con: `.ipynb`, `.txt`, `.csv`, `.json`, `.md`, `.pdf`, imágenes, y visualizaciones Vega/Vega Lite.

### 🔹 Diferencias con JupyterLab open source
Aunque la estructura es similar, en OCI se agregan:
- **Launcher personalizado** con acceso directo a notebooks, terminales, editores y ejemplos.
- **Environment Explorer**: GUI para gestionar entornos Conda.
- **Extensión GitHub**: para control de versiones dentro del notebook.

---

## 🧭 Componentes de la interfaz

### 🔝 Barra superior (Chrome bar)
- Logo de Oracle: vuelve a la consola principal.
- Nombre de la sesión: lleva al detalle del notebook.
- Tiempo restante: por defecto 1 hora de inactividad → se puede extender hasta 24 horas.
- Icono de ayuda: acceso a documentación.
- Cierre de sesión.

### 📁 Barra lateral izquierda
- **Explorador de archivos**: navegar, abrir, crear y borrar carpetas.
- **Terminal y kernels activos**: detener procesos.
- **Extensión Git**: gestión de versiones (cubierta en otra lección).
- **Comandos**: acceso a todos los comandos de JupyterLab.
- **Inspector de propiedades**: activo en notebooks.
- **Lista de pestañas abiertas**
- **Tabla de contenidos**: generada desde Markdown.
- **Gestor de extensiones instaladas**

👉 Para ocultar la barra lateral: hacer doble clic en cualquier ícono.

---

## 🧩 Área de trabajo principal
- Paneles de pestañas redimensionables.
- Actividad actual marcada con borde azul.
- **Code Consoles**: espacio temporal para ejecutar código interactivo.
- **Kernel-backed documents**: permiten ejecutar código desde cualquier archivo de texto.
- **Vista múltiple**: edición en vivo desde distintos editores o visores.
- **Gestión de kernels**: desde el menú *Kernel*, se accede a acciones como reiniciar, detener o cambiar kernel.


---

## 🧪 Unidad: Cómo trabajar con JupyterLab – Parte 2

### 🎯 Objetivo
Explorar el uso del **Launcher**, la creación de notebooks, el manejo de celdas, kernels, extensiones y herramientas visuales dentro de JupyterLab en OCI.

---

## 🚀 El Launcher

- Acceso rápido a:
  - Notebooks
  - Consolas
  - Editor de texto
  - Terminales
  - **Environment Explorer**
  - **Notebook Examples**

- Parte superior: enlaces útiles para empezar, documentación y ejemplos.
- Lado izquierdo: extensiones destacadas:
  - **Environment Explorer**: descubre y gestiona entornos Conda.
  - **Notebook Examples**: accede a tutoriales y casos de uso.

- Lado derecho: crear archivos nuevos (notebooks, Markdown, texto) o sesiones (terminal, consola).

---

## 📓 Creación y uso de notebooks

### 🔹 Crear notebook con kernel Python3
- Clic en el kernel → *Create Notebook*
- Se genera un archivo con tips útiles:
  - Verificación de conectividad
  - Imports típicos de ADS
  - Variables de entorno

### 🔹 Acciones básicas
- **Renombrar**: clic derecho → *Rename*
- **Ejecutar código**:
  - Clic en triángulo
  - Menú *Run → Selected Cell*
  - Atajo: `Shift + Enter`
- **Indicadores**:
  - ⭐ Estrella: celda en ejecución
  - Número: orden de ejecución

### 🔹 Tipos de celda
- Cambiar entre `Code`, `Markdown`, etc.
- Ejemplo Markdown:  
  ```markdown
  # Título
  ```

- Reordenar celdas: arrastrar desde el borde izquierdo

---

## ✏️ Menú Edit

- **Merge cells**: combinar celdas seleccionadas
- **Split cells**: dividir celdas
- **Cambiar kernel**: clic en nombre del kernel → seleccionar otro

---

## 📊 Ejemplo avanzado: notebook de clasificación binaria

- Desde el launcher → *Notebook Examples* → *Binary Classification Attrition* → *Load Example*
- Ejecutar todas las celdas
- Para detener: *Kernel → Interrupt Kernel*

---

## 🔍 Herramientas visuales

### 🔹 Variable Inspector
- Ver variables activas
- Posicionar junto al notebook: arrastrar pestaña hasta que se marque en azul

### 🔹 Menú View
- Mostrar números de línea
- Colapsar/expandir celdas y salidas

---

## 🧰 Explorador de archivos

- Crear archivos: clic derecho
- Subir archivos: arrastrar y soltar
- Visualización depende del tipo:
  - `.csv`: muestra columnas y filas

---

## 🖥️ Terminal

- Comandos Linux estándar (`ls`, etc.)
- Herramientas disponibles:
  - `ODSC conda CLI`
  - `Git CLI`
  - `OCI CLI`

---

## 📚 Menú Help

- Acceso a:
  - Documentación
  - FAQs
  - Material de referencia

---

## 🧩 Aplicación en tus flujos

Podés usar JupyterLab para:
- Documentar pruebas con Markdown y tabla de contenidos
- Versionar código con Git desde la sesión
- Ejecutar modelos y visualizar métricas
- Usar terminal para automatizaciones con OCI CLI
- Explorar entornos Conda para pruebas familiares

---
</br>
</br>

# <h1>Conda Environments en OCI Data Science</h1>

---

## 🧪 ¿Qué es un Conda Environment?

Un **Conda Environment** es un contenedor de software que incluye:

- Intérprete (ej. Python)
- Módulos y librerías específicas (ej. `scikit-learn`, `pandas`, `tensorflow`)
- Configuraciones personalizadas

Permite trabajar de forma **aislada, reproducible y compartible**.

---

## 🎯 Beneficios clave

- **Instalación selectiva**: solo los paquetes que necesitás
- **Aislamiento**: distintos entornos para distintos modelos (ej. visión vs regresión)
- **Cambio rápido**: podés alternar entre entornos sin conflictos
- **Compartibilidad**: se pueden compartir entre notebook sessions o con tu equipo
- **Reproducibilidad**: podés volver a la versión exacta de librerías usadas en un modelo

---

## 🧭 Tipos de Conda Environments en OCI

| Tipo                        | ¿Quién lo gestiona? | ¿Dónde se usa?                          |
|-----------------------------|---------------------|------------------------------------------|
| **Data Science Conda**      | Oracle               | Preinstalados, listos para usar          |
| **Published Conda**         | Vos (el usuario)     | Guardados en Object Storage, compartibles |
| **Installed Conda**         | Notebook session     | Activos en tu sesión, persistentes en block volume |

---

## 🖥️ Environment Explorer

Una interfaz gráfica dentro de JupyterLab que te permite:

- Ver entornos en **vista de tarjetas** o **lista**
- Buscar por palabra clave
- Filtrar por GPU, estado (activo/deprecado), tipo
- Instalar, clonar o eliminar entornos
- Ver detalles técnicos y librerías incluidas

---

</br>
</br>

<h1> Conda </h1>
---
# 🧠 Teoría de los Entornos Conda en OCI Data Science

## 1. ¿Qué es un entorno Conda en OCI?

Un entorno Conda en el servicio de Data Science de Oracle Cloud Infrastructure (OCI) es un paquete preconfigurado de herramientas, librerías y configuraciones que permite desarrollar, entrenar y desplegar modelos de machine learning de forma eficiente. Estos entornos están basados en software open source y pueden personalizarse según las necesidades del proyecto.

### ✅ Ventajas:
- Ahorra tiempo en la configuración inicial.
- Incluye librerías optimizadas para tareas específicas.
- Compatible con JupyterLab y el ecosistema de OCI.
- Permite trabajar con CPU o GPU según el entorno elegido.

---

## 2. Acceso y uso

Los entornos Conda se acceden desde la pestaña **Launcher** de JupyterLab, mediante el botón **Environment Explorer**. Todos los entornos incluyen:

- **OCI Python SDK**: para interactuar con servicios de OCI.
- **ADS SDK (oracle-ads)**: para flujos de machine learning, AutoML, ingestión de datos y explicabilidad de modelos.

---

## 3. Tipos de entornos Conda

### 🔧 Según aplicación:
- **ONNX**: para portabilidad de modelos entre frameworks.
- **PyPGX**: para grafos y análisis de redes.
- **PySpark**: para procesamiento distribuido con Apache Spark.

### 🎯 Según caso de uso:
- **Computer Vision**: procesamiento de imágenes y video.
- **Data Exploration & Manipulation**: análisis exploratorio y visualización.
- **Financial Services**: flujos específicos para servicios financieros.
- **Natural Language Processing (NLP)**: procesamiento de texto y lenguaje.

---

## 4. Familias de entornos Conda

Los entornos se agrupan por:

- **Versión de Python** (ej. 3.6, 3.7).
- **Arquitectura** (CPU o GPU).
- **Versión del entorno** (v1, v2, etc.).

Ejemplo:  
`Natural Language Processing for CPU - Python 3.7 - v2`  
→ Misma arquitectura y versión de Python que v1, pero con librerías actualizadas.

---

## 5. Convención de nombres

### 🧩 Basados en aplicación:
`TensorFlow 2.7 for CPU - Python 3.7 - v1`

### 🧪 Basados en tarea:
`Data Exploration and Manipulation for CPU - Python 3.7`

---

## 6. Entornos populares y sus librerías clave

### 📷 Computer Vision
- Tareas: detección de objetos, reconocimiento facial, seguimiento ocular.
- Librerías: `scikit-image`, `Pillow`, `PyTorch`, `OpenCV`.

### 📊 Data Exploration & Manipulation
- Tareas: ingestión, visualización, análisis exploratorio.
- Librerías: `ADS`, `Kafka`, `pandas`, `pandaparallel`, `matplotlib`, `seaborn`, `plotly`, `bokeh`.

### 🤖 General Machine Learning
- Tareas: ML supervisado, AutoML, explicabilidad.
- Librerías: `xgboost`, `lightgbm`, `keras`, `TensorFlow`, `Oracle AutoML`, `Oracle MLX`.

### 📝 Natural Language Processing
- Tareas: extracción de texto, frases clave, POS tagging.
- Librerías: `nltk`, `keybert`, `pytorch-lightning`, `simpletransformers`.

### 🔄 ONNX
- Tareas: conversión y ejecución de modelos en formato portable.
- Librerías: `ONNX`, `ONNX Runtime`.

### 🗃️ Oracle Database
- Tareas: ETL, transformaciones, consultas SQL.
- Librerías: `ipython-sql`, `SQLAlchemy`, `ADS Connector`.

### ⚡ PyTorch
- Tareas: redes neuronales, aceleración en CPU.
- Librerías: `PyTorch`, `daal4py`, `oneAPI DAL`.

### 🔥 PySpark
- Tareas: procesamiento distribuido, MLlib.
- Librerías: `PySpark`, `MLlib`, `sparksql-magic`.

### 🧬 TensorFlow
- Tareas: entrenamiento y despliegue de modelos de deep learning.
- Librerías: `TensorFlow`, `TensorBoard`, `ADS`.

---

## 7. Conclusión

Los entornos Conda en OCI Data Science son una solución modular, escalable y decorativa para acelerar proyectos de ciencia de datos. Permiten trabajar con herramientas de última generación sin preocuparse por la instalación manual, y están diseñados para adaptarse a distintos casos de uso, arquitecturas y versiones de Python.

---

## 🧠 Librerías mencionadas en entornos Conda de OCI Data Science

| 📚 Librería              | 🧩 Característica principal                                                                 | 🗂️ Categoría del entorno Conda                     |
|--------------------------|---------------------------------------------------------------------------------------------|----------------------------------------------------|
| **oracle-ads (ADS SDK)** | SDK para ML en OCI: ingestión, AutoML, explicabilidad, despliegue.                         | Todos los entornos                                 |
| **OCI Python SDK**       | Acceso a servicios de OCI desde Python.                                                    | Todos los entornos                                 |
| **scikit-image**         | Procesamiento de imágenes.                                                                 | Computer Vision                                    |
| **Pillow**               | Manipulación de imágenes.                                                                  | Computer Vision                                    |
| **PyTorch**              | Deep Learning con soporte GPU.                                                             | Computer Vision, NLP, General ML                   |
| **OpenCV**               | Algoritmos de visión por computadora.                                                      | Computer Vision                                    |
| **Kafka (Python)**       | Consumo de streams de datos.                                                               | Data Exploration & Manipulation                    |
| **pandas**               | Manipulación de datos tabulares.                                                           | Data Exploration & Manipulation, General ML        |
| **pandaparallel**        | Paralelización de pandas.                                                                  | Data Exploration & Manipulation                    |
| **task**                 | (No especificado, posiblemente auxiliar).                                                  | Data Exploration & Manipulation                    |
| **Matplotlib**           | Visualización 2D.                                                                          | Data Exploration & Manipulation                    |
| **Seaborn**              | Visualización estadística.                                                                 | Data Exploration & Manipulation                    |
| **Plotly**               | Gráficos interactivos.                                                                     | Data Exploration & Manipulation                    |
| **Bokeh**                | Visualización web interactiva.                                                             | Data Exploration & Manipulation                    |
| **xgboost**              | Algoritmo de boosting eficiente.                                                           | General Machine Learning                           |
| **lightgbm**             | Boosting rápido y ligero.                                                                  | General Machine Learning                           |
| **Keras con TensorFlow** | API de alto nivel para redes neuronales.                                                   | General Machine Learning                           |
| **Oracle MLX**           | Explicabilidad de modelos.                                                                 | General Machine Learning                           |
| **nltk**                 | Procesamiento de texto.                                                                    | Natural Language Processing                        |
| **keybert**              | Extracción de frases clave con BERT.                                                       | Natural Language Processing                        |
| **pytorch-lightning**    | Abstracción de PyTorch para NLP.                                                           | Natural Language Processing                        |
| **simpletransformers**   | Framework NLP con transformers.                                                            | Natural Language Processing                        |
| **ONNX**                 | Formato portable de modelos ML.                                                            | ONNX (Interoperabilidad y despliegue)              |
| **ONNX Runtime**         | Ejecución de modelos ONNX.                                                                 | ONNX (Interoperabilidad y despliegue)              |
| **ipython-sql**          | Comandos SQL en notebooks.                                                                 | Oracle Database                                    |
| **SQLAlchemy**           | ORM para bases de datos.                                                                   | Oracle Database                                    |
| **daal4py**              | Aceleración de scikit-learn en CPUs Intel.                                                 | PyTorch (optimizado para CPU)                      |
| **oneAPI DAL**           | Librería de Intel para análisis de datos.                                                  | PyTorch (optimizado para CPU)                      |
| **PySpark**              | API Python para Apache Spark.                                                              | PySpark (procesamiento distribuido)                |
| **MLlib**                | ML en Spark.                                                                               | PySpark                                            |
| **sparksql-magic**       | Comandos Spark SQL en notebooks.                                                           | PySpark                                            |
| **TensorFlow**           | Framework de ML y Deep Learning.                                                           | TensorFlow                                         |
| **TensorBoard**          | Visualización de métricas de entrenamiento.                                                | TensorFlow                                         |



</br>
</br>
---

# 🧠 Gestión de entornos Conda con la herramienta de línea de comandos `odsc`

## 1. Introducción
En este módulo aprenderás a **gestionar entornos Conda** utilizando la herramienta de línea de comandos `odsc` incluida en el servicio **Oracle Cloud Infrastructure (OCI) Data Science**.

Antes de entrar en detalle, recordemos qué es un entorno Conda:  
Un **entorno Conda** es una colección de software empaquetada que incluye intérprete, librerías y configuraciones necesarias para ejecutar proyectos de ciencia de datos.  
En OCI existen:
- **Conda packs gestionados** por el equipo de Data Science Service.
- **Conda packs publicados por el usuario**, que podés crear y compartir.

Aunque gran parte de la gestión se puede hacer con la interfaz gráfica **Environment Explorer**, la CLI `odsc` ofrece **mayor control y flexibilidad**.

---

## 2. Funcionalidades principales de `odsc conda`

Con la CLI podés:

- **Explorar (browse)**: ver información detallada de entornos Conda en formato YAML (nombre, descripción, librerías clave, *slug*).
- **Buscar (search)**: combinar `odsc conda list` con herramientas como `grep` para filtrar resultados.
- **Instalar (install)**: añadir entornos Conda gestionados o publicados.
- **Clonar (clone)**: copiar un entorno a otra ubicación para modificarlo sin afectar el original.
- **Modificar (modify)**: actualizar o cambiar librerías de un entorno instalado.
- **Publicar (publish)**: guardar entornos personalizados en Object Storage para compartirlos o usarlos en despliegues y *jobs*.
- **Eliminar (delete)**: borrar entornos que ya no necesites.
- **Crear (create)**: generar entornos personalizados a partir de un archivo `environment.yaml`.

---

## 3. Exploración de entornos Conda

Podés hacerlo de dos maneras:
1. **Environment Explorer** (GUI).
2. **Línea de comandos** con:
   ```bash
   odsc conda list
   ```
   - Por defecto, muestra entornos **Data Science** gestionados.
   - Para listar solo los entornos instalados localmente en tu notebook:
     ```bash
     odsc conda list --local
     ```
   - Para listar entornos **publicados**:
     ```bash
     odsc conda list --override
     ```
     *(Requiere tener configurado el bucket de Object Storage y `odsc conda init`)*

---

## 4. Búsqueda avanzada

No existe un comando específico de búsqueda en la CLI, pero podés filtrar resultados combinando `odsc conda list` con utilidades como `grep`, `awk` o `perl`.

Ejemplo para obtener nombres y *slugs*:
```bash
odsc conda list | grep -E "name:|slug:"
```

---

## 5. Instalación de entornos Conda

- **Instalar un entorno gestionado**:
  ```bash
  odsc conda install --slug <nombre-del-slug>
  ```
- **Instalar un entorno publicado**:
  ```bash
  odsc conda install --slug <nombre-del-slug> --override
  ```
  *(El parámetro `--override` indica que se debe instalar desde entornos publicados en Object Storage, no desde los gestionados por OCI)*

---

## 6. Buenas prácticas

- **Clonar antes de modificar**: evita romper un entorno funcional.
- **Publicar entornos estables**: facilita la colaboración y el despliegue.
- **Usar nombres descriptivos en el slug**: mejora la búsqueda y el mantenimiento.
- **Documentar cambios**: registra librerías añadidas o actualizadas.

---

# 🧠 Gestión avanzada de entornos Conda con `odsc` (Parte 2)

## 7. Clonar entornos Conda

La clonación permite **copiar e instalar** un entorno Conda existente, creando una **nueva versión personalizada** sin modificar el original.

**Comando base:**
```bash
odsc conda clone --from <slug_origen> --env <nombre_nuevo_entorno>
```

- **`--from`**: *slug* del entorno Conda instalado que querés clonar.
- **`--env`**: nombre del nuevo entorno.  
  Al asignarlo, OCI genera automáticamente un nuevo *slug*.

💡 **Ventaja**: Ideal para probar cambios importantes sin arriesgar la estabilidad del entorno original.

---

## 8. Modificar un entorno Conda

Cuando querés **instalar nuevas librerías** o **actualizar versiones**, no se usa `odsc`, sino la herramienta estándar `conda`.

**Pasos:**
8.1. Activar el entorno:
   ```bash
   conda activate /home/datascience/conda/<slug_entorno>
   ```
8.2. Realizar cambios. Ejemplo: actualizar ADS a la última versión:
   ```bash
   python3 -m pip install oracle-ads --upgrade
   ```

🔹 Los cambios afectan **solo** al entorno activado.

---

## 9. Publicar un entorno Conda

Publicar un entorno lo **empaqueta y sube a un bucket de Object Storage**, permitiendo:
- Compartirlo con tu equipo.
- Usarlo en *jobs* y despliegues de modelos.
- Garantizar **reproducibilidad**.

**Preparación:**
9.1. Crear un bucket en **Object Storage**.
9.2. Anotar:
   - **Namespace** del bucket.
   - **Nombre** del bucket.
9.3. Inicializar la configuración (solo una vez por sesión):
   ```bash
   odsc conda init --bucket_namespace <namespace> --bucket_name <nombre_bucket>
   ```

**Publicar:**
```bash
odsc conda publish --slug <slug_entorno>
```

---

## 10. Eliminar un entorno Conda

Para liberar espacio:
```bash
odsc conda delete --slug <slug_entorno>
```

---

## 11. Crear un entorno Conda desde cero

Podés crear un entorno nuevo usando un **archivo de manifiesto Conda** (`environment.yaml`).

**Comando:**
```bash
odsc conda create --file <ruta/environment.yaml>
```

- Por defecto, se instalan paquetes base desde `/opt/base-env.yaml` para compatibilidad con JupyterLab.
- Si querés evitarlo:
  ```bash
  odsc conda create --file <ruta/environment.yaml> --empty
  ```
  ⚠️ No recomendado, ya que podría impedir que el entorno aparezca como kernel en JupyterLab.

---

## 12. Resumen de funcionalidades vistas

| Acción        | Comando principal                         | Uso típico |
|---------------|-------------------------------------------|------------|
| **Explorar**  | `odsc conda list`                         | Ver entornos disponibles |
| **Buscar**    | `odsc conda list | grep ...`               | Filtrar por nombre o slug |
| **Instalar**  | `odsc conda install --slug ...`            | Añadir entornos gestionados o publicados |
| **Clonar**    | `odsc conda clone --from ... --env ...`    | Crear copia editable |
| **Modificar** | `conda activate ...` + `pip install ...`   | Actualizar librerías |
| **Publicar**  | `odsc conda publish --slug ...`            | Compartir en Object Storage |
| **Eliminar**  | `odsc conda delete --slug ...`             | Borrar entornos |
| **Crear**     | `odsc conda create --file ...`             | Nuevo entorno desde YAML |

📌 **Resumen**:  
La CLI `odsc` es la herramienta más potente para gestionar entornos Conda en OCI. Te permite no solo instalar y explorar, sino también clonar, modificar, publicar y crear entornos personalizados, asegurando control total sobre tu infraestructura de ciencia de datos.



</br>
</br>

---

# 🧠 Demo: Gestión de entornos Conda con la CLI `odsc`

## 1. Introducción

En esta demostración aprenderás a **gestionar entornos Conda** usando la herramienta de línea de comandos `odsc` en **OCI Data Science**.  
Veremos cómo:

- Explorar (*browse*)
- Buscar (*search*)
- Instalar (*install*)
- Clonar (*clone*)
- Modificar (*modify*)
- Publicar (*publish*)
- Eliminar (*delete*) entornos Conda
- Crear un entorno personalizado desde cero usando un archivo **YAML**

El comando principal que utilizaremos es:

```bash
odsc
```

Al ejecutar `odsc --help`, verás varios subcomandos. En este caso, trabajaremos con el subcomando:

```bash
odsc conda
```

---

## 2. Subcomandos disponibles

Al listar la ayuda de `odsc conda`, encontrarás opciones como:

- `list` → listar entornos
- `initialize` → inicializar configuración
- `show-configuration` → mostrar configuración actual
- `publish` → publicar entornos
- `install` → instalar entornos
- … entre otros

---

## 3. Explorando entornos Conda

### 3.1 Listar entornos gestionados por OCI
```bash
odsc conda list
```
Devuelve un archivo **YAML** con información detallada:
- **name** → nombre del conda-pack
- **slug** → identificador único
- **type** → `dataScience` (gestionado por OCI)

### 3.2 Listar entornos instalados localmente
```bash
odsc conda list --local
```
- Muestra entornos instalados en la sesión de notebook.
- El campo **type** será `local`.

### 3.3 Listar entornos publicados
```bash
odsc conda list --override
```
- Muestra entornos publicados en Object Storage.
- Requiere configuración previa (`odsc conda init`).

---

## 4. Búsqueda de información

El listado en YAML puede ser extenso. Para filtrar, combinamos `odsc conda list` con herramientas como `grep` y expresiones regulares.

Ejemplo: obtener solo nombres y slugs
```bash
odsc conda list | grep -E "name:|slug:"
```

Para buscar entornos relacionados con *Data Exploration*:
```bash
odsc conda list | grep -i "data exploration"
```

---

## 5. Instalación de un entorno Conda

Ejemplo: instalar un entorno de *Data Exploration*:

1. Buscar el slug:
   ```bash
   odsc conda list | grep -i "data exploration"
   ```
2. Instalar:
   ```bash
   odsc conda install --slug <slug_encontrado>
   ```
3. El sistema pedirá la versión a instalar.
4. Descargará y extraerá el entorno.

Verificar instalación:
```bash
odsc conda list --local | grep <slug>
```

---

## 6. Clonación de un entorno Conda

Para modificar un entorno sin afectar el original:

```bash
odsc conda clone --from <slug_origen> --env "Mi Data Exploration"
```

- `--from`: slug del entorno original.
- `--env`: nombre del nuevo entorno (OCI generará un slug automáticamente).
- El sistema pedirá la versión y luego empaquetará e instalará la copia.

---

## 7. Flujo de trabajo típico en esta demo

1. **Listar** entornos gestionados (`odsc conda list`).
2. **Filtrar** por nombre o slug con `grep`.
3. **Instalar** el entorno deseado (`odsc conda install`).
4. **Verificar** instalación (`odsc conda list --local`).
5. **Clonar** para personalizar (`odsc conda clone`).

---
# 🧠 Gestión avanzada de entornos Conda con `odsc` (Parte final del capítulo)

## 8. Verificar el *slug* del entorno clonado

Después de clonar un entorno Conda, es importante identificar su **slug** (identificador único).  
Para hacerlo:

```bash
odsc conda list --local | grep -E "name:|slug:"
```

- `--local` → lista solo los entornos instalados en la sesión de notebook.
- `grep` → filtra para mostrar únicamente los campos `name` y `slug`.

---

## 9. Modificar un entorno Conda

Para modificar un entorno (añadir librerías, cambiar versiones, etc.) **no** se usa `odsc conda`, sino la herramienta estándar `conda`.

**Pasos:**
1. Activar el entorno:
   ```bash
   conda activate /home/datascience/conda/<slug_entorno>
   ```
2. Realizar cambios. Ejemplo: instalar la librería `pendulum`:
   ```bash
   python3 -m pip install pendulum
   ```
3. Desactivar el entorno:
   ```bash
   conda deactivate
   ```

💡 **Nota:** Los cambios afectan únicamente al entorno activado.

---

## 10. Publicar un entorno Conda

Publicar un entorno lo empaqueta y lo sube a un **bucket de Object Storage**, permitiendo:
- Compartirlo con otros usuarios.
- Usarlo en *jobs* y despliegues de modelos.
- Garantizar reproducibilidad.

**Pasos:**
1. Crear un bucket en Object Storage (ej. `published-conda-environments`).
2. Anotar:
   - **Namespace** del bucket.
   - **Nombre** del bucket.
3. Inicializar la configuración (solo una vez por sesión):
   ```bash
   odsc conda init --bucket_namespace <namespace> --bucket_name <nombre_bucket>
   ```
4. Publicar el entorno:
   ```bash
   odsc conda publish --slug <slug_entorno>
   ```

---

## 11. Verificar publicación

Para confirmar que el entorno está publicado:
```bash
odsc conda list --override | grep -E "name:|slug:"
```
- `--override` → lista entornos publicados en Object Storage en lugar de los gestionados por OCI.

En el bucket, la estructura será:
```
Conda Environments/
   CPU/
      My Data Exploration/
         v1/
            <archivos del entorno>
```

---

## 12. Eliminar un entorno Conda

Para liberar espacio en la sesión de notebook:
```bash
odsc conda delete --slug <slug_entorno>
```
El sistema pedirá confirmación antes de eliminarlo.

---

## 13. Crear un entorno Conda desde un archivo YAML

Otra forma de crear un entorno es a partir de un **archivo de manifiesto Conda** (`environment.yaml`).

**Comando:**
```bash
odsc conda create --file <ruta/environment.yaml>
```

- Por defecto, se añaden paquetes base desde `/opt/base-env.yaml` para compatibilidad con JupyterLab.
- Para evitarlo:
  ```bash
  odsc conda create --file <ruta/environment.yaml> --empty
  ```
  ⚠️ No recomendado, ya que podría impedir que el entorno aparezca como kernel en JupyterLab.

---

📌 **Resumen**:  
Esta demo muestra cómo usar `odsc conda` para explorar, buscar, instalar y clonar entornos Conda en OCI Data Science, combinando la potencia de la CLI con utilidades de filtrado como `grep` para trabajar de forma más ágil y precisa.


Resumen de operaciones vistas
| Acción        | Comando principal                         | Uso típico |
|---------------|-------------------------------------------|------------|
| **Listar**    | `odsc conda list`                         | Ver entornos disponibles |
| **Buscar**    | `odsc conda list | grep ...`               | Filtrar por nombre o slug |
| **Instalar**  | `odsc conda install --slug ...`            | Añadir entornos gestionados o publicados |
| **Clonar**    | `odsc conda clone --from ... --env ...`    | Crear copia editable |
| **Modificar** | `conda activate ...` + `pip install ...`   | Actualizar librerías |
| **Publicar**  | `odsc conda publish --slug ...`            | Compartir en Object Storage |
| **Eliminar**  | `odsc conda delete --slug ...`             | Borrar entornos |
| **Crear**     | `odsc conda create --file ...`             | Nuevo entorno desde YAML |



</br>
</br>
---
# 🧠 OCI Vault: Gestión segura de secretos y claves para Data Science

## 1. Introducción

En este módulo aprenderás:

- Por qué es importante usar el servicio **OCI Vault** para compartir y proteger secretos.
- Conceptos clave como:
  - Tipos de claves.
  - Rotación de claves.
  - Almacenamiento seguro de secretos en el Vault (en lugar de en tu código).

---

## 2. ¿Qué es OCI Vault y por qué es importante?

En un flujo de trabajo de ciencia de datos, es habitual interactuar con otros servicios para:

- Conectarse a datos importantes.
- Almacenar y recuperar artefactos.
- Importar y exportar información.

Muchas de estas interacciones requieren **credenciales** (usuarios, contraseñas, tokens, certificados).

**Mejor práctica de seguridad:**  
Nunca almacenar credenciales localmente o en el código, ya que es una de las formas más comunes de filtración.  
En su lugar, se recomienda usar un servicio especializado: **OCI Vault**.

---

## 3. Funcionalidad principal de OCI Vault

- Servicio **gestionado por Oracle** para administrar de forma centralizada:
  - **Claves de cifrado**.
  - **Credenciales** y secretos.
- Soporta tres algoritmos de cifrado:
  - **AES** (Advanced Encryption Standard)
  - **RSA** (Rivest–Shamir–Adleman)
  - **ECDSA** (Elliptic Curve Digital Signature Algorithm)
- Integración con:
  - **OCI SDK**
  - **CLI de OCI**
  - **Clientes API**
  - **ADS SDK** (con múltiples puntos de integración entre Data Science y otros servicios OCI)

Esto facilita almacenar credenciales en el Vault y conectarse a los recursos necesarios sin exponer datos sensibles en código o archivos de configuración.

---

## 4. Elementos principales del servicio

- **Vaults**: contenedores lógicos para almacenar claves y secretos.
- **Keys**: entidades lógicas que representan una o más versiones de material criptográfico.
- **Secrets**: credenciales o datos sensibles cifrados.

El Vault elimina la necesidad de guardar claves y secretos en archivos de configuración o en el código.

---

## 5. Mejores prácticas

Tanto ingenieros DevOps como científicos de datos deberían usar el Vault para **mejorar la postura de seguridad** de sus aplicaciones y servicios.

---

## 6. Tipos de Vault

Al crear un Vault, se puede elegir entre:

### 🔹 Virtual Private Vault
- Partición dedicada en un **HSM** (*Hardware Security Module*).
- Hasta **1.000 versiones de claves**.
- Mejor aislamiento.
- Permite **copias de seguridad** en Object Storage.
- Soporta **recuperación ante desastres** y **replicación entre regiones**.

### 🔹 Vault en partición compartida (opción por defecto)
- Comparte la partición HSM con otros clientes de Oracle.
- Seguridad garantizada, pero sin funciones avanzadas como backup a Object Storage.
- **Menor coste**: se cobra solo por el número de claves, versiones y secretos almacenados.

---

## 7. ¿Qué son las claves (*Keys*)?

- Entidades lógicas que representan una o más versiones de material criptográfico.
- El material criptográfico se genera para un algoritmo específico (AES, RSA o ECDSA).
- Se utilizan para:
  - **Cifrar datos**.
  - **Firmar digitalmente** información.


---

# 🔐 OCI Vault – Tipos de claves, rotación y gestión de secretos

## 8. Técnicas de cifrado y descifrado

Las tecnologías de cifrado utilizan distintos enfoques:

- **AES** → Cifrado simétrico: la misma clave puede cifrar y descifrar los datos.
- **RSA** y **ECDSA** → Cifrado asimétrico: una clave cifra y la otra descifra.

---

## 9. Tipos de claves en OCI Vault

En el servicio Vault existen tres tipos conceptuales de claves:

### 9.1 Master Encryption Key (Clave maestra de cifrado)
- Claves que creás o importás en tu Vault.
- Definís:
  - Algoritmo de cifrado (AES, RSA, ECDSA).
  - Forma de la clave (*key shape*): número de bits (AES/RSA) o ID de curva elíptica (ECDSA).

### 9.2 Data Encryption Key (Clave de cifrado de datos)
- Generadas a partir de una clave maestra.
- Se cifran dinámicamente con la clave maestra (**envelope encryption**).
- Permiten:
  - Usar múltiples claves para distintos datos.
  - Rotar claves sin afectar todo el sistema.
  - Reducir el impacto si una clave se ve comprometida (solo afecta a los datos cifrados con ella).

### 9.3 Wrapping Keys
- Usadas para proteger (envolver) otras claves durante su transporte o almacenamiento.

---

## 10. Uso de claves en servicios OCI

Servicios como **Block Storage** o **File Storage** pueden:
- Usar claves gestionadas por Oracle.
- Usar claves maestras personalizadas desde tu Vault.

Ejemplo: un bucket de Object Storage o un volumen de bloque puede usar una clave de cifrado de datos específica.

---

## 11. Rotación de claves maestras

- Cada clave tiene una **versión** asignada al crearse.
- Al rotar:
  - Se genera automáticamente una nueva versión.
  - O podés importar otra clave.
- **Mejor práctica**: rotar periódicamente para limitar la cantidad de datos cifrados con una misma versión.
- El Vault usa el **OCID** de la versión anterior para descifrar datos cifrados con ella.
  - Versiones antiguas → ya no cifran, pero sí pueden descifrar.

---

## 12. Componentes clave del servicio Vault

1. **Keys** → Claves de cifrado.
2. **HSM** (*Hardware Security Module*) con certificación **FIPS 140-2 Nivel 3**.
3. **Secrets** → Datos sensibles como contraseñas, tokens o credenciales.

---

## 13. Gestión de secretos

- **Qué son**: credenciales necesarias para acceder a servicios OCI o aplicaciones externas.
- **Ventajas de almacenarlos en Vault**:
  - Mayor seguridad que en código o archivos de configuración.
  - Recuperación bajo demanda.
  - Código más robusto: si cambian las credenciales, solo se actualizan en Vault.
- **Funcionamiento**:
  - Guardás localmente el **OCID** del secreto.
  - El código solicita las credenciales al Vault cuando las necesita.
  - Se usan y luego se descartan.
- **Control de acceso**:
  - Más fácil restringir acceso al secreto que al notebook.
- **Creación de secretos**:
  - Desde la **Consola OCI**.
  - Programáticamente con **OCI SDK**, **CLI** o **REST API**.
- **Versionado**:
  - Cada secreto tiene un OCID único que no cambia.
  - Al rotar, se crea una nueva versión con el contenido actualizado.
  - Rotar periódicamente reduce el impacto de una posible exposición.

---

## Resumen del módulo

En este capítulo aprendiste:

OCI Vault es la herramienta centralizada para almacenar y gestionar claves y secretos de forma segura en OCI. Protege credenciales, evita filtraciones y se integra con múltiples servicios y SDKs, ofreciendo opciones de aislamiento y recuperación según las necesidades y presupuesto.

- Qué es el servicio **OCI Vault** y su importancia.
- Tipos de Vault y tipos de claves.
- Concepto de versiones y rotación de claves.
- Gestión segura de secretos y credenciales.
- Por qué **no** almacenar credenciales en código, sino en el Vault.



</br>
</br>

---
# 🔐 Gestión de cifrado y secretos en OCI: Oracle Managed Keys vs Customer Managed Keys

## 1. Introducción

En este módulo aprenderás:

- Las distintas formas de gestionar el cifrado en OCI:
  - **Oracle Managed Keys** (claves gestionadas por Oracle).
  - **Customer Managed Keys** (claves gestionadas por el cliente).
- Cómo usar el **OCI SDK** para almacenar y recuperar secretos desde el Vault.
- Clases especializadas del **ADS SDK** diseñadas para integrarse con el Vault y simplificar el acceso a recursos seguros en flujos de trabajo de ciencia de datos.

---

## 2. Cifrado en OCI

OCI utiliza cifrado en múltiples puntos del servicio.  
Al trabajar con recursos, se te pedirá elegir entre:

- **Oracle Managed Keys** → Claves maestras gestionadas por Oracle en su Vault interno.
- **Customer Managed Keys** → Claves maestras almacenadas en tu propio Vault.

### 2.1 Oracle Managed Keys
- Por defecto, OCI cifra y descifra datos usando claves maestras gestionadas por Oracle.
- Ejemplo: al aprovisionar un **Block Volume**, **Object Storage Bucket** o un **OKE Cluster**, Oracle usa una de sus claves maestras para generar la **Data Encryption Key** que cifrará los datos.

### 2.2 Customer Managed Keys
- La clave maestra está en tu Vault.
- Se usa para generar las **Data Encryption Keys**.
- Aunque no uses el Vault, **todos los datos en reposo (data at rest)** en OCI están cifrados por defecto y no se puede desactivar.
- Obligatorio en ciertos contextos, como **Security Zones**, donde no se permite usar claves gestionadas por Oracle.

💡 **Nota**: *Customer Managed Key* no es lo mismo que *Bring Your Own Key (BYOK)*.  
En este caso, la clave puede haber sido:
- Importada previamente a tu Vault.
- Generada directamente por el servicio Vault.

En ambos casos:
- La clave es tuya.
- Gestionás su rotación.
- Sos responsable de su ciclo de vida.

---

## 3. Recursos que requieren elección de tipo de clave

- Block Volumes y Boot Volumes.
- File Systems.
- Object Storage.
- Kubernetes Secrets (OKE).
- Autonomous Container Databases.
- OCI Streaming Pools.
- Y más.

---

## 4. Configuración de una Customer Managed Key

1. Seleccionar la opción **Customer Managed Key**.
2. Localizar tu Vault.
3. Elegir la clave maestra que deseas usar.
4. Esa clave generará las **Data Encryption Keys** que cifrarán los datos.

---

## 5. Trabajo con secretos en Python

### 5.1 Opciones
- **OCI SDK**:
  - API general para trabajar con el Vault.
  - Muy potente, pero más compleja.
  - No está pensada específicamente para flujos de trabajo de ciencia de datos.
- **ADS SDK**:
  - Clases adaptadas a Data Science.
  - Más simple para casos de uso comunes de científicos de datos.

---

## 6. Ejemplo: creación y almacenamiento de credenciales

**Problema común**: credenciales almacenadas en código o archivos de configuración → inseguro y difícil de mantener.

**Ejemplo motivador**: credenciales para conectarse a una **Autonomous Database** (o cualquier base de datos).

6.1. Crear un diccionario Python con:
   - Nombre de la base de datos.
   - Usuario.
   - Contraseña.
   ```python
   credentials = {
       "dbname": "...",
       "username": "...",
       "password": "..."
   }
   ```

6.2. **Vault y clave ya creados**.

6.3. **Codificación Base64**:
   - No se puede almacenar un objeto binario (diccionario Python) directamente en el Vault.
   - Convertir a JSON y luego codificar en Base64.
   - Usar `Base64SecretContentDetails`.

6.4. **Creación del objeto de detalles del secreto**:
   - Incluir:
     - Compartment OCID.
     - Vault ID.
     - Key ID.
     - Descripción.
     - Nombre del secreto.
     - Contenido codificado en Base64.

---

## 7. Almacenamiento del secreto en el Vault

7.1. Cargar configuración OCI:
   ```python
   config = oci.config.from_file()
   ```
7.2. Crear cliente de Vault:
   ```python
   vault_client = oci.vault.VaultsClient(config)
   ```
7.3. Usar `vaults_client_composite_operations` para:
   - Llamar a `create_secret_and_wait_for_state`.
   - Pasar el objeto de detalles del secreto.
   - Esperar hasta que el estado sea **ACTIVE**.

---

# 🔐 Recuperación de secretos y uso del ADS SDK con OCI Vault

## 8. Recuperar secretos desde el Vault con OCI SDK

Para recuperar secretos almacenados en el Vault usando el **OCI SDK**:

8.1. **Cliente de secretos**:
   - Usar la clase `SecretsClient`.
   - Requiere el objeto de configuración (`config`) que ya cargamos previamente.

8.2. **Método principal**:
   - `get_secret_bundle(secret_ocid)` → devuelve un **response object**.

8.3. **Estructura de acceso**:
   - `response.data` → devuelve un **secret bundle**.
   - `secret_bundle_content` → contiene el objeto con el contenido codificado en Base64.
   - `content` → el valor real del secreto en Base64.

8.4. **Decodificación**:
   - Crear un método auxiliar que:
     - Decodifique Base64.
     - Convierta el JSON resultante en un diccionario Python.

**Flujo resumido**:
```python
# 1. Crear cliente de secretos
secret_client = oci.secrets.SecretsClient(config)

# 2. Obtener el bundle
secret_bundle = secret_client.get_secret_bundle(secret_ocid)

# 3. Extraer y decodificar
decoded_secret = base64_to_dict(secret_bundle.data.secret_bundle_content.content)
```

---

## 9. Uso del ADS SDK para simplificar la gestión de secretos

El **ADS SDK** ofrece clases especializadas para almacenar y recuperar secretos en OCI Vault, pensadas para flujos de trabajo de ciencia de datos:

- **ADBSecretKeeper** → Autonomous Database (incluye opción de almacenar el *wallet file*).
- **BDSSecretKeeper** → OCI Big Data Service (HDFS, Hive, Kerberos).
- **MySQLDBSecretKeeper** → Oracle MySQL Database.
- **AuthTokenSecretKeeper** → Tokens de autenticación (ej. Streaming, GitHub).

---

## 10. Ejemplo: MySQLDBSecretKeeper

### 10.1 Guardar credenciales
```python
from ads.secrets import MySQLDBSecretKeeper

# Crear objeto
keeper = MySQLDBSecretKeeper(
    vault_id="<Vault_OCID>",
    key_id="<Key_OCID>",
    credentials={
        "dbname": "...",
        "host": "...",
        "port": 3306,
        "username": "...",
        "password": "..."
    }
)

# Guardar en el Vault
keeper.save(name="MySQL_Creds", description="Credenciales MySQL de producción")
```

### 10.2 Recuperar credenciales (mejor práctica)
Usar un **context manager** para no dejar las credenciales en memoria más tiempo del necesario:
```python
with MySQLDBSecretKeeper() as keeper:
    creds = keeper.load_secret(secret_ocid="<Secret_OCID>")
    # creds es un diccionario con las credenciales
```

---

## 11. Ventajas del ADS SDK frente al OCI SDK puro

- **Menos código**: guardar → 2 líneas, recuperar → 1 línea.
- **Adaptado a casos de uso de Data Science**.
- **Soporte para múltiples servicios** (ADB, BDS, MySQL, tokens).
- **Manejo simplificado de formatos** (no requiere codificación/decodificación manual en Base64).

---

## 12. Resumen del módulo

En este capítulo aprendiste que:

- Entendiste la diferencia entre claves gestionadas por Oracle y por el cliente.
- Viste cómo elegir y configurar una Customer Managed Key.
- Aprendiste a crear y almacenar credenciales seguras en el Vault usando Python y el OCI SDK.
- Los servicios que usan cifrado pueden tener su clave maestra gestionada por Oracle o por el cliente en su Vault.
- Las credenciales pueden convertirse de diccionario Python → JSON → Base64 y almacenarse en el Vault con el OCI SDK.
- El proceso con OCI SDK implica:
  - Crear `VaultsClient` y `SecretsClient`.
  - Usar `create_secret_and_wait_for_state` para almacenar.
  - Usar `get_secret_bundle` para recuperar.
  - Decodificar Base64 y reconstruir el diccionario.
- El **ADS SDK** simplifica enormemente este flujo con clases como `MySQLDBSecretKeeper`, `ADBSecretKeeper`, `BDSSecretKeeper` y `AuthTokenSecretKeeper`.



</br>
</br>

---

# 📂 Sistemas de Control de Versiones en Ciencia de Datos (Parte 1)

## 1. Introducción

En este módulo veremos:

- Qué es un **sistema de control de versiones** (*Version Control System*, VCS).
- Cómo se utilizan en ciencia de datos.
- Cómo configurar uno y ejecutar comandos básicos.

Los sistemas de control de versiones, también llamados **sistemas de gestión de código fuente** (*Source Code Management Systems*), permiten gestionar distintas versiones de código, documentos, datos, análisis y otros recursos similares.  
Aunque fueron creados para el desarrollo de software tradicional, los científicos de datos los han adoptado para gestionar y versionar sus análisis.

---

## 2. Uso en ciencia de datos

Ejemplo:  
Los usuarios de ciencia de datos utilizan sistemas de control de versiones para **rastrear las distintas versiones de sus notebooks de JupyterLab**. Esto facilita:

- Gestionar cambios.
- Compartir trabajo con otros.
- Mantener un historial de versiones.

Existen múltiples sistemas de repositorios: CVS, Bazaar, Subversion, Perforce, CodeCommit, Mercurial, Helix Core, entre otros.  
Sin embargo, **Git** es el más popular y está integrado en el **OCI Data Science Service**, por lo que este módulo se centrará casi exclusivamente en Git.

---

## 3. Qué entendemos por “código”

En este contexto, “código” se refiere a **cualquier recurso que se rastree en un sistema de control de versiones**:

- Código fuente.
- Documentos.
- Informes.
- Datos recopilados.
- Análisis estadísticos o de machine learning.
- Otros productos de trabajo.

---

## 4. Concepto de repositorio

Un sistema de control de versiones puede gestionar múltiples recursos, cada uno en un **repositorio** independiente.

📦 **Analogía**:  
- El repositorio es como un **archivo o gabinete** que contiene un proyecto o análisis.
- Cada repositorio mantiene un **historial de cambios** del código base.

---

## 5. Funciones clave de un repositorio

- **Almacenamiento central** del código.
- **Versionado**: seguimiento de versiones de desarrollo y de lanzamiento.
- **Colaboración**: integración de cambios de varios usuarios (*merge*).
- **Historial**: archivo de estados previos del código y documentación.
- **Ramas (branches)**: copias independientes del código para trabajar en paralelo.
- **Commits**: puntos de guardado que permiten volver a un estado anterior.

Ejemplo:  
- Creás un modelo de ML que funciona → lo **commiteás**.
- Probás una mejora → falla → revertís al commit anterior.

---

## 6. Tipos de sistemas de control de versiones

### 🔹 Centralizados
- Un servidor central recibe todos los cambios.
- Ventajas: fácil de configurar, control administrativo.
- Ejemplos: Subversion, CVS, Perforce.

### 🔹 Distribuidos
- No dependen de un único servidor.
- Cada desarrollador clona el repositorio completo en su máquina.
- Ventajas:
  - Trabajar sin conexión.
  - Mayor flexibilidad.
  - Creación rápida de ramas.
  - Sin punto único de fallo.
- Ejemplos: Git, Bazaar, Mercurial.

---

## 7. Uso en ciencia de datos

Para un científico de datos, un sistema distribuido como Git permite:

- Crear repositorios locales sin pedir permisos en un servidor central.
- Trabajar y analizar datos localmente.
- Archivar el repositorio al finalizar el proyecto.

**Limitación**:  
En colaboración, cada persona debe configurar su sistema para compartir cambios con cada otro miembro, lo que no escala bien en equipos grandes.

---

# 📂 Sistemas de Control de Versiones en Ciencia de Datos (Parte 2)

## 8. Configuración híbrida en sistemas distribuidos

Para evitar la complejidad de que cada miembro de un equipo se conecte con todos los demás, normalmente se configura **un nodo central** al que todos envían (*push*) sus cambios.  
Cuando alguien quiere las últimas actualizaciones, las descarga (*pull*) desde ese nodo.

En la práctica, los sistemas de control de versiones distribuidos no siempre funcionan de forma totalmente distribuida.  
Muchos equipos optan por un **modelo híbrido**: por ejemplo, usar Git (distribuido) pero con un servidor central para compartir.

---

## 9. Uso de Git en el flujo de trabajo de ciencia de datos

**Git** permite:

- Rastrear cambios en un conjunto de archivos.
- Revertir a versiones anteriores.
- Versionar no solo código, sino también:
  - Notebooks de JupyterLab.
  - Informes.
  - Otros productos de trabajo.

En equipos, un repositorio compartido permite que cada miembro contribuya y fusione (*merge*) sus cambios.  
Esto es clave para proyectos de ciencia de datos y construcción de modelos.

---

## 10. Ventajas de Git como sistema distribuido

- **Velocidad**: la mayoría de operaciones son locales.
- **Trabajo offline**: solo se necesita conexión para *push* o *pull*.
- **Tolerancia a fallos**: incluso con un servidor central, se puede compartir directamente entre compañeros si el servidor cae.

---

## 11. Extensión de Git en OCI Data Science

OCI Data Science integra una **extensión de Git en JupyterLab**:

- Interfaz gráfica amigable.
- Acceso desde el ícono de Git o el menú Git.
- Funciones:
  - Crear o clonar repositorios.
  - *Push* y *pull*.
  - *Stage* de cambios para commit.
  - Comparar versiones.
- Compatible con:
  - GitHub
  - Bitbucket
  - GitLab
  - OCI Code Repository
  - Instalaciones propias de Git

---

## 12. Terminología básica en Git

- **Commit**: instantánea del estado actual del código.
  - Identificado por un **SHA ID** (hash único de 40 caracteres).
  - Puede tener etiquetas (*tags*) legibles.
- **Repositorio (repo)**: directorio que contiene todos los cambios de un proyecto.
  - Local o remoto.
  - Colección de commits.
- **Área de trabajo (working area)**:
  - Archivos de la versión actual en la que trabajás.
  - En notebooks, se almacenan en el **block storage local**.
- **Staging**:
  - Paso previo al commit.
  - Indica a Git qué archivos modificados se incluirán en la nueva versión.

---

## 13. Flujo de trabajo de un commit en Git

1. **Área de trabajo**: crear o modificar archivos.
2. **Staging**: seleccionar qué cambios incluir.
3. **Commit**:
   - Guardar cambios en el repositorio.
   - Añadir un comentario descriptivo.
   - Registrar autor y fecha.
4. **Compartir**:
   - *Push* → enviar cambios a otro repositorio/peer.
   - *Pull* → traer cambios de otro repositorio/peer.

💡 **Buenas prácticas**:
- Hacer commits frecuentes y pequeños.
- No incluir en *staging* archivos irrelevantes o que no deban ser rastreados.

---

## 14. OCI Code Repository

- Servicio similar a GitHub o Bitbucket, pero integrado en OCI.
- Funciona como **peer central**.
- Integrado con el sistema de **Identity and Access Management (IAM)** de OCI.
- Permite:
  - Commits.
  - Actualizaciones.
  - Creación de ramas (*branches*).
  - Control de acceso seguro.

---

# 📂 Sistemas de Control de Versiones en Ciencia de Datos (Parte 3)

## 15. Gestión y visualización de repositorios en OCI

- En la **consola de OCI** podés ver:
  - El **almacenamiento** utilizado por cada repositorio.
  - El **OCID** asignado a cada repo al crearlo.
- Con ese OCID podés:
  - Editar el contenido.
  - Clonar el repo a otro peer.
  - Eliminar repos que ya no necesites.
  - Ver el historial de cambios y commits.
  - Navegar por ramas (*branches*).
  - Consultar el tamaño del repositorio.

---

## 16. Trabajo con repositorios remotos y externos

En **OCI Data Science** podés trabajar con repositorios remotos como:

- GitLab
- Bitbucket
- Tus propios repos Git

También podés **conectar repos externos** (ej. GitHub) al **OCI Code Repository**.  
La conexión incluye:
- Tipo (GitHub, GitLab, etc.).
- Nombre.
- Referencia a un **secreto en OCI Vault** que almacena el *personal access token* de tu cuenta.

💡 **Ventaja**:  
Una vez definida la conexión, los cambios en tu repo de GitHub se **replican automáticamente** en el OCI Code Repository.

---

## 17. Permisos y políticas

Para dar acceso a repos y otros recursos, debés crear **políticas IAM**.  
Con un repositorio OCI o externo, podés:

- Clonarlo vía **HTTPS** o **SSH keys**.
- Crear una copia local.
- Agregar o eliminar archivos.
- Hacer commits.
- Trabajar con ramas y operaciones típicas de GitHub.

---

## 18. Git vs GitHub

- **Git** → Sistema de control de versiones.
- **GitHub** → Servicio en la nube que aloja proyectos Git.

---

## 19. Conexión mediante SSH

- **SSH** permite conectar y autenticarte a servidores remotos sin ingresar usuario/token cada vez.
- Pasos:
  1. Instalar y configurar Git (nombre y email).
  2. Crear cuenta en GitHub (si no la tenés).
  3. Generar un **par de claves SSH** (privada y pública).
  4. Agregar la clave pública a GitHub.
  5. Autenticar tu repo local con GitHub.

---

## 20. Flujo básico de trabajo con Git y GitHub

1. Tener un repo local y uno remoto (GitHub).
2. Si empezás de cero:
   - Crear repo vacío en GitHub.
   - Clonarlo en tu notebook:
     ```bash
     git clone <URL>
     ```
3. Crear/modificar archivos.
4. Hacer commit en el repo local.
5. Hacer push al repo remoto para compartir cambios.

---

## 21. Comandos básicos de Git

| Comando         | Función |
|-----------------|---------|
| `git init`      | Inicializa un nuevo repo o convierte un directorio existente en repo Git. |
| `git clone`     | Crea una copia local de un repo remoto y los vincula. |
| `git add`       | Añade archivos al *staging area* para el próximo commit. |
| `git commit`    | Guarda una instantánea de los archivos en *staging*. |
| `git remote`    | Gestiona conexiones entre repos locales y remotos. |
| `git fetch`     | Descarga commits y datos del repo remoto sin fusionar. |
| `git push`      | Sube commits locales al repo remoto. |
| `git pull`      | Descarga y fusiona cambios del repo remoto al local. |

---

## 22. Resumen del módulo

En este capítulo vimos:

- Qué es un sistema de control de versiones y sus tipos (centralizado y distribuido).
- Definición y usos de un repositorio de código.
- Importancia del control de versiones en ciencia de datos.
- Extensión de Git en JupyterLab.
- Terminología clave: commit, repo, área de trabajo, staging.
- OCI Code Repository y su integración con repos externos como GitHub.
- Pasos para configurar un repo remoto.
- Comandos esenciales de Git.



</br>
</br>
---

# 📂 Demo: Creación y uso de un repositorio Git local y remoto en GitHub

## 1. Objetivo de la demo
El objetivo de esta demostración es:

- Crear un nuevo repositorio Git local.  
- Hacer commits de archivos en el repositorio.  
- Conectar con un repositorio en GitHub.  
- Enviar (*push*) y recibir (*pull*) archivos entre ambos.  

---

## 2. Configuración inicial de Git

1. Abrir una terminal.  
2. Git ya está instalado, solo hay que configurarlo:  
   ```bash
   git config user.name "Tu Nombre"
   git config user.email "tu_email@ejemplo.com"
   ```
   - Esto permite que cada commit registre quién lo realizó.  
3. Verificar configuración:  
   ```bash
   git config --list
   ```

---

## 3. Crear un repositorio local

1. En el explorador de archivos → **Nuevo Folder** → nombrarlo `demo`.  
2. En JupyterLab → ícono de Git → **Initialize Repository**.  
3. Ahora el directorio es un repositorio Git local.  

---

## 4. Autenticación con GitHub mediante SSH

GitHub requiere autenticación para hacer *push*. Esto se hace con un **par de claves SSH**.

1. Generar clave SSH:  
   ```bash
   ssh-keygen -t rsa -C "tu_email@ejemplo.com"
   ```
   - Se crean dos archivos:  
     - **Clave privada** (mantener en secreto).  
     - **Clave pública** (se puede compartir).  

2. Copiar la clave pública al portapapeles.  

3. Iniciar el agente SSH:  
   ```bash
   eval "$(ssh-agent -s)"
   ssh-add -k ~/.ssh/id_rsa
   ```

4. En GitHub → **Settings → SSH and GPG Keys → New SSH Key** → pegar la clave pública.  

---

## 5. Crear un repositorio en GitHub

1. En GitHub → **New Repository** → nombrarlo `demo`.  
2. Copiar la URL SSH (ejemplo: `git@github.com:usuario/demo.git`).  
3. En JupyterLab → Git → **Add Remote Repository** → pegar la URL.  
4. Verificar conexión:  
   ```bash
   git remote -v
   ```

---

## 6. Flujo de trabajo: crear, trackear y commitear archivos

1. Crear un nuevo notebook (`File → New → Notebook`).  
2. Git lo mostrará como **Untracked**.  
3. Hacer clic derecho → **Stage** para rastrearlo.  
4. Hacer commit:  
   - Mensaje: `"Initial Commit"`.  
   - Confirmar.  

---

## 7. Push al repositorio remoto

1. Configurar upstream (solo la primera vez):  
   ```bash
   git push --set-upstream origin master
   ```
2. Luego, simplemente:  
   ```bash
   git push
   ```

3. Verificar en GitHub → el archivo y el mensaje de commit aparecen en el repo remoto.  

---

## 8. Ejemplo de actualización

1. Editar el notebook (ej. agregar cálculos).  
2. Guardar cambios.  
3. En la pestaña Git → archivo aparece como **Changed**.  
4. Hacer **Stage** → **Commit** (ej. mensaje `"some math"`).  
5. Hacer **Push to Remote**.  
6. Verificar en GitHub → cambios reflejados.  

---

## 9. Resumen de la demo

En esta demostración:

- Configuramos Git con nombre y correo.  
- Creamos un repositorio local.  
- Generamos un par de claves SSH y lo vinculamos a GitHub.  
- Creamos un repositorio en GitHub y lo enlazamos con el local.  
- Creamos un notebook, lo rastreamos, lo commiteamos y lo subimos a GitHub.  
- Finalmente, hicimos cambios, los volvimos a commitear y los sincronizamos con el remoto.  

---

📌 **Conclusión**:  
Este flujo demuestra cómo **integrar Git y GitHub en un entorno de ciencia de datos con JupyterLab**, permitiendo versionar notebooks, colaborar y mantener sincronizados los repositorios locales y remotos.

---
# 🔄 Módulo: Machine Learning Lifecycle  
## 📘 Capítulo: ML Lifecycle Overview – Parte 1

### 1. Introducción

Bienvenido al módulo sobre el ciclo de vida del aprendizaje automático (*Machine Learning Lifecycle*).  
Esta primera lección ofrece una **visión general** del ciclo de vida de ML.  
Soy Wes Prichard, gerente principal de producto para Data Science y Servicios de IA en Oracle.

---

### 2. ¿Por qué es importante el ciclo de vida de ML?

Las organizaciones buscan herramientas **versátiles y productivas** para sus científicos de datos, y desean que esas herramientas cubran **todo el ciclo de vida del aprendizaje automático**.  
Cuanto más fácil y eficiente sea este ciclo, más rápido y frecuentemente se podrán obtener resultados valiosos para la organización.

---

### 3. Las 6 etapas del ciclo de vida

Usaremos una versión simplificada del ciclo de vida, compuesta por **6 pasos**:

1. **Acceso a los datos**  
2. **Exploración y preparación de los datos**  
3. **Modelado** (construcción y entrenamiento del modelo)  
4. **Validación del modelo**  
5. **Despliegue del modelo**  
6. **Monitoreo del modelo** (que puede llevar a su actualización o retiro)

🔹 Todo comienza con un **problema de negocio**, que define el objetivo del modelo.

---

### 4. Un proceso iterativo

Construir un modelo de ML es un proceso **iterativo**.  
Los pasos se repiten y ajustan hasta que el rendimiento del modelo sea satisfactorio.

💡 Existen representaciones más complejas del ciclo de vida, como **CRISP-DM** (*Cross Industry Standard Process for Data Mining*), que podés explorar por tu cuenta.  
Para este curso, usaremos el ciclo simplificado como marco para abordar las tareas clave del científico de datos.

---

### 5. Acceso y adquisición de datos

Todo modelo de ML comienza con **datos**.  
En OCI Data Science, es útil almacenar los datos en la sesión de notebook para acceder rápidamente.

- El primer paso es **acceder y recopilar los datos** en el notebook.
- Conocer el **ecosistema de datos** de la organización ayuda a identificar fuentes potenciales.

#### Fuentes de datos comunes:
- **Sistemas de gestión de datos empresariales** (bases de datos, data lakes).
- **Pipelines de ingestión** desarrollados por ingenieros de datos y ML.
- **Datos no estructurados**: logs, texto, imágenes, videos.
- **Catálogo de datos**: útil para localizar conjuntos existentes.
- **Fuentes externas**:
  - Datos públicos (gobiernos, open data).
  - Scraping web.
  - Proveedores de datos.
  - Encuestas, sensores, cámaras, clickstream.

---

### 6. Exploración y preparación de datos

Una vez obtenidos los datos, el científico de datos debe:

- **Explorar** y **visualizar** los datos.
- **Transformarlos** y repetir el proceso si es necesario.
- **Prepararlos**: limpieza y procesamiento antes del análisis.

#### Tareas típicas:
- Identificar y corregir datos corruptos, duplicados o incompletos.
- Determinar si los datos están **etiquetados** (ej. imágenes con bounding boxes).
- Si no lo están, usar servicios como **OCI Data Labeling Cloud Service**.

---

### 7. Análisis exploratorio y estadístico

Después de la limpieza, se analizan las **features** (variables):

- Identificar relaciones entre variables.
- Decidir transformaciones adicionales.
- Usar herramientas de análisis estadístico y visualización.

#### Preguntas clave:
- ¿Qué tipo de features hay?
- ¿Cuál es la distribución de valores?
- ¿Hay valores nulos o inválidos?
- ¿Existen outliers?
- ¿Hay sesgos o correlaciones?
- ¿Es necesario normalizar o transformar (ej. log)?
- ¿Cómo manejar categorías con cola larga?

---

### 8. Ingeniería de features

Durante la exploración, se pueden crear nuevas features que representen mejor los datos.

Ejemplo:  
En un dataset de tráfico con conteo por hora, podés crear una feature que agrupe las horas en franjas como:

- Madrugada  
- Mañana  
- Tarde  
- Noche  

Para features categóricas, suele ser necesario convertirlas en binarias (una por categoría).

---

### 9. Modelado (inicio)

La etapa de modelado consiste en:

- Elegir el algoritmo de ML adecuado.
- Seleccionar las features que alimentarán el modelo.

🔹 En el primer paso, el científico de datos debe decidir **qué tipo de modelo** es apropiado para resolver el problema planteado.

---

### 10. Tipos de aprendizaje automático

Existen dos tipos principales:

- **Aprendizaje supervisado**:  
  - El modelo aprende a partir de datos de entrada asociados a una **salida o etiqueta**.  
  - Ejemplos: clasificación, regresión.

- **Aprendizaje no supervisado**:  
  - El modelo trabaja con datos **sin etiquetas**.  
  - Ejemplo: segmentación de clientes → el modelo asigna los segmentos automáticamente.

---

### 11. Selección de algoritmos y entrenamiento

- Se utilizan diferentes clases de modelos para problemas supervisados y no supervisados.
- Los científicos de datos suelen probar **múltiples algoritmos** y generar **varios candidatos de modelos**.
- No se sabe de antemano cuál funcionará mejor → se experimenta.

Durante el entrenamiento:

- Se prueban distintos **subconjuntos de features** como entrada.
- Reducir el número de variables:
  - Disminuye el costo computacional.
  - Mejora la generalización.
  - Puede mejorar el rendimiento.

---

### 12. División del conjunto de datos

- **Training set** → para entrenar el modelo.  
- **Testing set** → para evaluar el rendimiento en datos no vistos.

---

### 13. Evaluación del modelo

Una vez entrenado, se debe evaluar su **idoneidad**.

- Hay herramientas open-source para calcular y visualizar métricas.
- Elegir las métricas adecuadas depende del **problema de negocio**.

#### Ejemplos:

- **Clasificación**:
  - Métrica común: **accuracy**.
  - Pero en casos como detección de enfermedades raras, es mejor usar:
    - **Precisión** y **recall**.
    - **Matriz de confusión**: TP, TN, FP, FN.

- **Regresión**:
  - **RMSE** (error cuadrático medio).
  - **MAE** (error absoluto medio).
  - **R²** (coeficiente de determinación).

- **No supervisado**:
  - Se busca que los **clusters** tengan alta cohesión interna.

---

### 14. Guardado de modelos

- Los modelos se guardan en formatos como:
  - **Pickle**
  - **ONNX**
  - **PMML**
- OCI Data Science ofrece un **catálogo de modelos** para preservarlos.

Según el objetivo, el trabajo puede ser:

- Prueba de concepto.
- Experimentación.
- Despliegue en producción.

---

### 15. Despliegue del modelo

Proceso de poner el modelo en uso.  
También se debe desplegar el **pipeline de transformación de datos**.

- Los científicos de datos colaboran con **ingenieros MLOps**.
- El despliegue puede ser:
  - **Batch**: inferencias programadas (ej. cada hora/día).
  - **Tiempo real**: activadas por eventos (ej. detección de fraude en pagos).

#### Consideraciones:
- ¿Qué tan rápido se necesita la respuesta? ¿Milisegundos o segundos?
- ¿Cuántas solicitudes se esperan?
- ¿Qué tamaño tienen los datos?

---

### 16. Monitoreo del modelo

Paso desafiante pero esencial para mantener la **eficacia** del modelo.

Dos componentes:

1. **Monitoreo estadístico (drift)**:
   - Las métricas pueden degradarse con el tiempo.
   - Ejemplo: valores fuera del rango del entrenamiento, cambios en la distribución.

2. **Monitoreo operacional (ops)**:
   - Latencia de respuesta.
   - Uso de memoria y CPU.
   - Rendimiento y confiabilidad del sistema.
   - Logs y métricas para diagnóstico.

---

### 17. Iteración continua

El aprendizaje automático es un proceso **altamente iterativo**.  
Los pasos se repiten múltiples veces hasta alcanzar el objetivo de negocio.

---

### 18. Próximas lecciones

En las siguientes lecciones, veremos cómo **OCI Data Science** ayuda a los científicos de datos a ejecutar cada etapa del ciclo de vida de ML.

---
# 📥 Lección: Access Data – 🔍 Acceso a datos en OCI Data Science

## 1. Introducción

Hola y bienvenido a la siguiente lección del curso de Oracle Cloud Infrastructure Data Science.  
Soy Himanshu Raj, científico de datos y líder senior de entrenamiento en AI/ML en Oracle.

En esta lección aprenderemos sobre el **primer paso del ciclo de vida del aprendizaje automático**:  
👉 **Acceder a los datos**.

También veremos:

- Por qué necesitamos datos.
- Cómo se recopilan.
- Cuáles son las fuentes clave para acceder a datos en OCI Data Science.

---

### 2. ¿Por qué necesitamos datos?

Toda aplicación o servicio, digital o no, **genera información**.  
Esta información puede clasificarse según su tamaño o fuente:

- **Datos por lotes (batch)**: generados con el tiempo por cargas diarias (ej. backups, migraciones).
- **Datos de servicios de streaming**: mensajes o logs de eventos de usuario e IoT.
- **Datos de aplicaciones**: generados por llamadas a APIs, eventos de aplicaciones, archivos de log, etc.

🔁 Estos datos deben ser **traídos a OCI** para su preprocesamiento y entrenamiento de modelos.  
Podés acceder a ellos desde la **interfaz gráfica** o desde la **línea de comandos** usando librerías específicas.

---

### 3. ¿Qué rol cumple el dato en ciencia de datos?

La ciencia de datos es una disciplina multidisciplinaria que necesita datos para:

- Formular hipótesis y extraer conclusiones.
- Realizar investigaciones basadas en datos.
- Resolver problemas concretos.

💡 Preguntas clave:
- ¿Qué tipo de datos necesito para resolver este problema?
- ¿Con los datos que ya tengo, puedo resolver problemas existentes?

---

### 4. Fuentes clave de datos en OCI Data Science

Estas son algunas de las fuentes más comunes (aunque no las únicas):

- **OCI Object Storage**
- **Almacenamiento local**
- **Oracle Autonomous Databases**
- **MySQL**
- **Amazon S3**
- **Endpoints HTTPS**
- **DatasetBrowser**
- **PyArrow**

---

### 5. Acceso a Oracle Object Storage

Para cargar un `DataFrame` desde Object Storage:

- Usá el ejemplo proporcionado, reemplazando el nombre del bucket y archivo.
- Podés autenticarte usando:
  - **API Key**
  - **Resource Principal** (usualmente en funciones serverless)

🔐 El módulo `set_auth` permite habilitar o deshabilitar la identidad del principal o del par de claves en una sesión abierta.

📚 Para más detalles, consultá la documentación de la clase ADS.

---

### 6. Acceso a almacenamiento local

Podés acceder a archivos locales usando funciones como:

```python
pandas.read_csv("ruta/al/archivo.csv")
```

---

### 7. Acceso a Oracle Autonomous Databases

OCI Data Science soporta ambos servicios de Autonomous Database.

- Usá `ads.read_sql`, que es **15 veces más rápido** que `pandas.read_sql`.
- Esto se debe a que **evita el ORM** y está optimizado para bases de datos Oracle.

#### Si usás un wallet file:
- Definí los parámetros de conexión y la ubicación del wallet.
- Luego ejecutá la consulta con `ads.read_sql`.

#### Si no usás wallet:
- Definí `hostname` y `port` en el diccionario `connection_parameters`.
- ⚠️ Esta opción está disponible solo en **ADS versión 2.5.6 o superior**.

🔐 Se recomienda usar **bind variables** para evitar ataques de inyección SQL.

📉 El rendimiento puede verse afectado por factores como la red, latencia, etc.

---
# 📥 Lección: Access Data – Parte 2  
## 🔍 Acceso a datos en OCI Data Science (continuación)

### 8. Optimización del acceso a bases de datos

El **tiempo de respuesta** de una base de datos puede mejorar significativamente mediante:

- Uso de **índices**.
- Escritura de **consultas SQL eficientes**.

🔹 Aunque la red de OCI es muy rápida, factores como VPNs o topologías complejas pueden afectar el rendimiento.  
Es importante considerar el **tiempo necesario para acceder a los datos**.

---

### 9. Acceso a MySQL

Podés seguir los mismos pasos que con Oracle Autonomous Database, pero:

- Debés definir el motor como `"MySQL"`.
- Esta funcionalidad está disponible a partir de **ADS versión 2.5.6**.

Para guardar un `DataFrame` en MySQL:

```python
ads.to_sql(df, engine="MySQL", ...)
```

---

### 10. Acceso a Amazon S3

- Archivos públicos o privados de **Amazon S3** pueden ser accedidos vía `pandas`.
- Para archivos privados, debés pasar las **credenciales correctas** usando el diccionario `storage_options` de ADS.

---

### 11. Acceso vía HTTP/HTTPS

También podés acceder a datos desde **URLs** usando `pandas`:

```python
pd.read_csv("https://ejemplo.com/datos.csv")
```

---

### 12. Uso de DatasetBrowser

ADS incluye el método `DatasetBrowser` para acceder fácilmente a conjuntos de datos bien definidos desde bibliotecas de referencia como:

- **Seaborn**
- **Scikit-learn**
- **GitHub**

Podés listar los datasets disponibles con:

```python
DatasetBrowser.list()
```

Y abrir uno específico con:

```python
DatasetBrowser.open("nombre_dataset")
```

---

### 13. Acceso a datos con PyArrow y OCI FS

ADS también permite editar y procesar datos grandes usando **PyArrow** a través de **OCI File Systems (OCI FS)**.

- OCI FS es un sistema de archivos Pythonic que:
  - Contiene información de conexión.
  - Permite operaciones típicas de sistema de archivos.

---

### 14. Detección de tipos semánticos de datos

ADS detecta automáticamente los **tipos semánticos** al abrir un dataset:

- **Categóricos**: ej. color de ojos, talla de camisa.
- **Ordinales**: ej. nivel educativo (primaria, secundaria, universidad).
- **Continuos**: ej. altura, versiones de software.
- **Fechas y horas**: formato datetime.

Podés inspeccionar los tipos con:

```python
df.feature_types
df.show_in_notebook()
```

---

### 15. Fuentes y formatos soportados por ADS

ADS soporta múltiples fuentes y formatos de datos en OCI Data Science.  
📚 Están listados en la [documentación oficial](https://docs.oracle.com/es-ww/iaas/Content/data-science/using/overview.htm)¹.

🔹 No se soportan directamente:
- Archivos `.txt`, `.doc`, `.pdf`
- Imágenes sin procesar
- Estructuras como `list`, `tuple`, `range`

Pero ADS incluye un **módulo de extracción de texto** para convertir `.PDF` o `.DOC` en texto plano.

---

### 16. Cierre de la lección

Esperamos que esta lección te haya sido útil para aprender cómo acceder a datos desde fuentes comunes en Oracle Data Science.  
Este paso es esencial para iniciar cualquier flujo de trabajo de machine learning.

---

---

# 🔍 Lección: Data Exploration and Preparation  
## 📘 Exploración y preparación de datos en OCI Data Science

### 1. Introducción

Hola y bienvenido a esta nueva lección del curso de Oracle Cloud Infrastructure Data Science.  
Soy Himanshu Raj, científico de datos y líder de entrenamiento en AI/ML en Oracle.

En esta lección abordaremos el **segundo paso del ciclo de vida del aprendizaje automático**:  
👉 **Exploración y preparación de datos**.

Veremos:

- Por qué es necesario el preprocesamiento.
- Qué pasos incluye.
- Herramientas de transformación de ADS.
- Cómo dividir los datos en conjuntos de entrenamiento, prueba y validación.

---

### 2. ¿Por qué preprocesar los datos?

Los datos reales suelen tener:

- Valores faltantes.
- Errores.
- Outliers.
- Formatos inconsistentes.

🔧 Por eso, antes de buscar patrones, debemos **limpiar y transformar** los datos.

El preprocesamiento puede incluir varios pasos, según el problema y el tipo de datos.  
💡 Es común que esta etapa sea la más extensa del ciclo de vida de ML.

---

### 3. Operaciones básicas sobre datos

Cuando los datos provienen de múltiples fuentes, debemos **combinarlos**.  
ADS permite realizar operaciones como:

- Agregar o eliminar filas/columnas.
- Filtrar.
- Concatenar vertical u horizontalmente.
- Unir por columnas o índices.

📌 Las operaciones de `pandas` también se aplican a objetos `ADSData`.

---

### 4. Limpieza y validación

Es importante verificar:

- Formatos y unidades.
- Convenciones de nombres.
- Tipos de datos.
- Valores nulos.
- Duplicados.
- Estadísticas descriptivas.

---

### 5. Imputación de valores faltantes

Los valores faltantes pueden deberse a errores humanos o técnicos.  
Ejemplo: coordenadas GPS incorrectas por mal clima.

Opciones:

- ❌ Eliminar filas incompletas (no recomendado).
- ✅ Imputar con:
  - Media o mediana (para datos numéricos).
  - Moda (para datos categóricos).

---

### 6. Codificación de variables categóricas

- **Label Encoding** (`label_encoder`): convierte categorías en números.  
  ⚠️ No recomendable para datos ordinales.

- **One Hot Encoding**:
  - Convierte una columna categórica en varias columnas binarias.
  - Se puede hacer con `pandas.get_dummies()` o `fit_transform()`.

---

### 7. Detección de outliers

Los outliers pueden ser errores o datos válidos pero atípicos.

- Se detectan con:
  - Visualizaciones: scatterplot, boxplot.
  - Estadísticas: desviación estándar, distribución gaussiana.
  - Algoritmos de ML (supervisado o no supervisado).

📌 En aprendizaje no supervisado, se asume que los outliers son pocos y no siguen la misma tendencia.

---

### 8. Escalado de características

El escalado ajusta las variables a una misma escala.  
Es útil en algoritmos sensibles a distancias (ej. regresión).

- **Normalización (Min-Max)**: valores entre 0 y 1.
- **Estandarización**: media 0, desviación estándar 1 → distribución normal.

---

### 9. Reducción de dimensionalidad

La **dimensionalidad** es el número de variables de entrada.

- Alta dimensionalidad = mayor costo computacional.
- Dos enfoques:
  - **Selección de características**: elegir un subconjunto.
  - **Extracción de características**: crear nuevas variables a partir de las existentes.

---

### 10. Preprocesamiento de texto

Para datos textuales, se aplican técnicas como:

- Vectorización.
- Eliminación de stop words.
- Tokenización.
- POS tagging.
- Stemming y lematización.

---

### 11. Herramientas de transformación en ADS

#### a. `suggest_recommendations`

- Detecta problemas en el dataset.
- Sugiere transformaciones.
- Podés aceptar los cambios desde el menú.
- Luego se obtiene el dataset transformado con `get_transformed_dataset()`.

#### b. `auto_transform`

- Aplica todas las recomendaciones automáticamente.
- Imputa valores faltantes.
- Elimina columnas altamente correlacionadas.
- Maneja clases desbalanceadas (upsampling/downsampling).
- Elimina claves primarias y columnas sin valor predictivo.

#### c. `visualize_transforms`

- Muestra visualmente las transformaciones aplicadas.
- Solo funciona con transformaciones automáticas.

---

### 12. Ejemplo práctico

En un dataset de rotación de empleados:

- ADS detecta tipos de datos.
- Sugiere transformaciones.
- Muestra correlaciones fuertes y desbalance de clases.
- Visualiza el flujo de transformación.

📌 Los resultados varían según el dataset.

---

### 13. División de datos

Dividir el dataset en:

- **Entrenamiento**
- **Prueba**
- **Validación**

Permite evaluar la **generalización** del modelo.

Por defecto, ADS usa:

- 80% entrenamiento
- 10% prueba
- 10% validación

💡 En datasets pequeños, puede ser mejor usar 70% o 60% para entrenamiento.

---

### 14. Conclusión

Esta lección cubrió:

- Preprocesamiento de datos reales.
- Herramientas de transformación en ADS.
- Codificación, imputación, escalado y detección de outliers.
- División en conjuntos de entrenamiento, prueba y validación.

---
# 🧪 Lección: Demo de Preprocesamiento con ADS  
## 📘 Ejemplo práctico en OCI Data Science

### 1. Introducción

En esta demo realizaremos un ejercicio práctico de preprocesamiento de datos usando **Accelerated Data Science (ADS)** en una sesión de notebook de OCI Data Science.

Usaremos el dataset **Employee Attrition**, que contiene:

- **1.470 filas**
- **36 características**:
  - 22 ordinales
  - 11 categóricas
  - 3 constantes

Las variables incluyen información demográfica, nivel de compensación, características del puesto, satisfacción laboral y métricas de desempeño.  
📉 El dataset está **desbalanceado**: hay menos empleados que se van que los que se quedan.

---

### 2. Carga del dataset

1. Se importan las librerías necesarias, incluyendo ADS.
2. Se carga el `DataFrame` desde **Object Storage** usando el método de **resource principal**.
3. Se define el bucket, el namespace y se usa `DatasetFactory.open()` para acceder al dataset.
4. Se establece la **feature objetivo**: `attrition`.

---

### 3. Transformaciones sugeridas

#### a. `suggest_recommendations`

- Detecta problemas en el dataset.
- Muestra mensajes con variables afectadas, acciones sugeridas y código para aplicarlas.

#### b. `auto_transform`

- Aplica automáticamente todas las transformaciones recomendadas.
- Optimiza el dataset:
  - Imputa valores faltantes.
  - Elimina columnas altamente correlacionadas.
  - Maneja clases desbalanceadas.
  - Elimina claves primarias y columnas sin valor predictivo.

#### c. `visualize_transforms`

- Permite visualizar las transformaciones aplicadas.
- Muestra diferencias entre aplicar o no `auto_transform`.

---

### 4. Codificación de variables categóricas

Ejemplo con la variable `job_function`:

- Se observan tres categorías distintas.
- Se usa el codificador categórico de ADS:
  ```python
  from ads.dataset.labelencoder import LabelEncoder
  ```
- Las categorías se transforman en valores numéricos.

---

### 5. Balanceo de clases

- Se realiza **upsampling** usando:
  ```python
  from ads.dataset.helper import upsample
  ```
- Se observa la repetición de muestras en la clase minoritaria (`attrition = yes`).
- Se comparan los conteos antes y después del balanceo.

---

### 6. División del dataset

Una vez completadas las transformaciones:

- Se divide el dataset en:
  - **Entrenamiento** (80%)
  - **Prueba** (10%)
  - **Validación** (10%)

📌 Estos valores pueden ajustarse según el tamaño del dataset.

---

### 7. Recursos adicionales

- Documentación oficial de ADS  
- Laboratorios en GitHub: [oracle-samples/oci-data-science-ai-samples](https://github.com/oracle-samples/oci-data-science-ai-samples)¹  
- Ejemplos de notebooks en la sesión de Data Science

---


# 📊 Lección: Data Visualization and Profiling  
## 📘 Visualización de datos y perfilado en OCI Data Science

### 1. Introducción

Hola, soy Jon Stanesby. En esta lección aprenderemos sobre **visualización de datos** y **perfilado**.

La visualización de datos es una parte esencial de la **exploración y análisis de datos** en ciencia de datos moderna.  
Es uno de los primeros pasos para **extraer valor** de los datos, ya que permite identificar patrones y relaciones de forma rápida y accesible, incluso sin formación técnica especializada.

---

### 2. ¿Qué es Data Visualization (DV)?

DV es la **presentación gráfica de los datos** para ilustrar hallazgos y explicar resultados.  
Es clave para:

- Analizar datos.
- Tomar decisiones basadas en datos.
- Comunicar patrones y relaciones de forma clara.

---

### 3. Herramientas de visualización modernas

Las herramientas de DV suelen:

- Conectarse con fuentes de datos (bases relacionales, cloud, on-premise).
- Ofrecer múltiples opciones de visualización.
- Sugerir automáticamente el tipo de gráfico según los datos.
- Integrar IA/ML para facilitar tareas a usuarios no técnicos.
- Permitir acceso y colaboración en toda la organización.
- Ofrecer flexibilidad entre control manual y automatización.

🔹 Buscá herramientas con:
- Interfaz intuitiva (point & click, drag & drop).
- Capacidad de edición rápida.
- Visualización automática de datos.

---

### 4. Visualización inteligente con ADS

ADS ofrece herramientas de visualización **automáticas y personalizables**:

- Detecta automáticamente el tipo de datos.
- Genera gráficos óptimos para cada variable.
- Permite usar cualquier librería de visualización (Seaborn, Matplotlib, etc.).

#### Visualizaciones comunes en ADS:
- Estadísticas resumen.
- Gráficos de distribución.
- Mapas de correlación.
- Detección de anomalías (valores faltantes, alta cardinalidad).

---

### 5. Métodos automáticos en ADS

#### a. `corr` (correlación)
- Calcula matrices de correlación por tipo de variable:
  - **Continua-Continua**: coeficiente de Pearson (−1 a 1).
  - **Continua-Categórica**: ratio de correlación (0 a 1).
  - **Categórica-Categórica**: Cramer's V (0 a 1).

#### b. `show_in_notebook`
- Muestra una vista completa del dataset:
  - Tipo de problema (regresión, clasificación binaria o multiclase).
  - Número de filas y columnas.
  - Tipos de features.
  - Visualizaciones por columna.
  - Mapa de correlación.
  - Encabezado del dataset.

📌 Usa una muestra inteligente con 95% de confianza y 1% de intervalo.

#### c. `plot`
- Herramienta automática de gráficos.
- Se define `x` (y opcionalmente `y`).
- ADS elige el tipo de gráfico según los tipos de datos.

Ejemplos:

- `x = attrition` (categórica binaria) → gráfico de barras.
- `x = edad` (continua) → histograma.
- `x = categórica`, `y = continua` → violin plot.
- `x = continua`, `y = continua` → heatmap gaussiano + scatterplot.

---

### 6. Sistema de tipos de features

ADS extiende los `DataFrames` de Pandas para:

- Separar representación física vs significado de los datos.
- Almacenar propiedades y métodos por feature.
- Usar herencia múltiple para definir características.
- Validar y advertir sobre calidad de datos.

📌 `feature_plot`:
- Sobre una serie → gráfico univariado.
- Sobre un `DataFrame` → tabla con visualización por feature.

---

### 7. Visualización personalizada

ADS permite usar librerías externas:

#### a. `call` method
- Permite definir tu propia rutina de visualización.

Ejemplos:

- `Seaborn.pairplot(df)` → relaciones entre pares de features.
- `Matplotlib` → gráficos personalizados.
- Dataset de terremotos en California → visualización geográfica.

---

### 8. Conclusión

En esta lección aprendiste a:

- Generar visualizaciones automáticas con ADS.
- Personalizar gráficos según tus necesidades.
- Usar métodos como `corr`, `plot`, `feature_plot`, `show_in_notebook`.
- Integrar librerías externas para visualización avanzada.

---

# 🧠 Lección: Model Training  
## 📘 Entrenamiento de modelos en OCI Data Science

### 1. Introducción

Hola, soy Jon Stanesby. En esta lección aprenderemos sobre el **entrenamiento de modelos**, una etapa crítica dentro de la fase de modelado del ciclo de vida del aprendizaje automático.

---

### 2. ¿Qué es el entrenamiento de modelos?

El entrenamiento de modelos construye la **mejor representación matemática** de las relaciones entre:

- Las **features** y la **etiqueta objetivo** (en aprendizaje supervisado).
- Todas las **features** (en aprendizaje no supervisado).

🔹 El proceso genera un **artefacto** que captura estos patrones.  
🔹 Se selecciona el **mejor algoritmo** considerando múltiples dimensiones.

---

### 3. Componentes del proceso de entrenamiento

#### a. Función de puntuación (`score function`)
- Indica qué tan bien se ajusta el modelo.
- Puede ser una función de error o de máxima verosimilitud.

#### b. Función de pérdida (`loss function`)
- Compara las predicciones del modelo con los valores reales.
- Calcula una **puntuación de pérdida** como número único.

📊 Ejemplo gráfico:
- Puntos verdes → datos reales.
- Línea negra → predicciones.
- Flechas rojas → error (pérdida).

#### c. Función de actualización (`update function`)
- Ajusta los parámetros del modelo en cada iteración.

---

### 4. Frameworks y entornos de entrenamiento

En ciencia de datos, **open source** se refiere a código libre y modificable.  
Los frameworks open source:

- Son accesibles.
- Tienen comunidades activas.
- Fomentan la innovación y solución de bugs.

🔹 OCI Data Science combina frameworks **propietarios de Oracle** y **open source**.  
🔹 Podés instalar librerías externas desde la terminal o iniciar con tu propio set de herramientas.

---

### 5. Formas de entrenar modelos en OCI

Podés entrenar modelos de varias maneras:

- 🧪 **Notebooks**: escribiendo y ejecutando código Python en JupyterLab.
- ⚙️ **Entornos Conda**: usando ADS, MLX o AutoML (veremos más adelante).
- 🧵 **Jobs**: se cubren en el módulo 4.

---

### 6. Conclusión

En esta lección vimos:

- Qué es el entrenamiento de modelos.
- Cómo se representa matemáticamente la relación entre variables.
- Qué funciones intervienen en el proceso.
- Qué frameworks y entornos se pueden usar.
- Qué opciones ofrece OCI para entrenar modelos.

---

# 🚀 Lección: Turning AML Models on OCI  
## 📘 Entrenamiento y escalado de modelos AML en Oracle Cloud

### 1. Introducción

¡Felicitaciones por llegar tan lejos en el curso de ciencia de datos!  
Soy Himanshu Raj, líder senior de entrenamiento en AI/ML en Oracle.

En este video experto hablaremos sobre cómo **entrenar y escalar modelos de aprendizaje automático (AML)** en Oracle Cloud Infrastructure (OCI).

---

### 2. Entrenamiento básico de modelos AML

Podés entrenar fácilmente un modelo AML usando **jobs** del servicio de ciencia de datos.

🔹 ¿Qué necesitás?

- Código fuente alojado en **GitHub**.
- Resultados almacenados en **OCI Object Storage**.
- Definir recursos y ejecución con **ADS**:
  - Usando código Python.
  - O mediante archivos **YAML**.

---

### 3. Entrenamiento distribuido en OCI

Para escalar horizontalmente y paralelizar tareas de entrenamiento en datasets grandes o cargas intensivas:

✅ OCI Data Science permite **entrenamiento distribuido** con ayuda de ADS.

🔹 Frameworks soportados:

- **Dask**
- **PyTorch Distributed**
- **Horovod**
- **TensorFlow Distributed**

📌 Esto permite reducir tiempos de entrenamiento sin perder precisión.

---

### 4. Implementación y comunidad

- Podés usar **Docker** o **GitHub** para tus implementaciones.
- La documentación oficial detalla cómo configurar cada framework.
- Se recomienda compartir tus casos de uso en la comunidad **OU**.

---

### 5. AutoMLx en OCI

También cubrimos **AutoML** en el curso.

🔹 Te recomendamos explorar el paquete **AutoMLx**, disponible en el **conda pack** de OCI.

- AutoMLx proporciona un pipeline que:
  - Encuentra y ajusta automáticamente el mejor modelo.
  - A partir de una tarea de predicción y un dataset de entrenamiento.

Podés elegir el motor paralelo (`task` o `local`) usando la función `INIT`.

---

### 6. Recursos y seguimiento

- Consultá la documentación de **ADS** y de las clases alias.
- Revisá las **release notes** para estar al día con nuevas funcionalidades.
- Compartí tus avances y dudas en la comunidad **OU**.

---

### 7. Conclusión

En esta lección aprendiste:

- Cómo entrenar modelos AML en OCI usando jobs.
- Cómo escalar horizontalmente con entrenamiento distribuido.
- Cómo usar AutoMLx para automatizar el ajuste de modelos.
- Dónde encontrar documentación y cómo participar en la comunidad.

---



</br>
</br>
</br>
</br>
</br>































***********************************************************************************************************************************************


---

### 📘 Glosario de Términos Clave en OCI Data Science

| Módulo / Área         | Término clave            | Descripción breve                                                  | Ejemplo aplicado a hotel real                                     |
|-----------------------|--------------------------|--------------------------------------------------------------------|--------------------------------------------------------------------|
| Entorno de desarrollo | ADS SDK                  | Librería de Python que simplifica tareas en el ciclo ML            | Entrenar modelo para predecir cancelaciones                       |
| Entorno de desarrollo | Notebook Session         | Ambiente interactivo en OCI para ejecutar código y analizar datos  | Editar notebook para detección de anomalías en reservas            |
| IAM                   | Tenancy                  | Entorno raíz que agrupa todos los recursos en OCI                  | Tenencia “HotelCorp” con compartimientos separados                |
| IAM                   | Compartment              | Contenedor lógico para organizar recursos y políticas              | Compartimiento “Marketing” con notebooks y objetos                |
| IAM                   | Group / Dynamic Group    | Grupo de usuarios o recursos con políticas asociadas               | Grupo “Analistas” con acceso a métricas y logs                    |
| IAM                   | User / Principal         | Identidad que puede autenticarse y operar sobre recursos           | Usuario “AnaRecepcion” con acceso a modelos y buckets              |
| IAM                   | Policy / IAM Settings    | Reglas que autorizan acciones sobre recursos                       | Política que permite acceso al Object Storage                     |
| IAM                   | OCI CLI / Token          | Herramientas para operar OCI desde la terminal                     | Usar CLI para lanzar notebook desde cron semanal                  |
| Automatización        | Job / Pipeline / Workload| Ejecuciones automatizadas en infraestructura OCI                   | Job nocturno que actualiza predicción de ocupación                |
| Automatización        | Scheduler / Cron         | Programador de tareas para ejecución periódica                     | Ejecutar script todos los días a las 6 AM                         |
| Automatización        | Logging / Audit          | Registro de actividad y monitoreo del sistema                      | Ver quién modificó modelo de predicción ayer                      |
| Ciencia de datos      | ML Lifecycle             | Ciclo completo: ingestión, entrenamiento, despliegue, monitoreo    | Desde historial de reservas hasta API en producción               |
| Ciencia de datos      | AutoML / ADSTuner        | Entrenamiento automático y ajuste de hiperparámetros               | Entrenar 20 modelos y elegir el más preciso                       |
| Ciencia de datos      | Model Catalog / Deployment| Repositorio y endpoints HTTP para modelos ML                       | Compartir modelo con el equipo de recepción                       |
| Ciencia de datos      | Feature Engineering      | Transformar variables para mejorar modelos                         | Crear “temporada alta” desde campo fecha                          |
| Ciencia de datos      | Train-Test Split         | División de datos para entrenamiento y evaluación                  | Usar datos de 2021 para entrenar y 2022 para testear              |
| Ciencia de datos      | Metrics / Evaluation     | Indicadores para medir la calidad de un modelo                     | Ver precisión y F1 Score del modelo de ocupación                  |
| Visualización         | Feature Types / Heatmap    | Clasificación de variables y visualización de relaciones            | Ver correlación entre ocupación y día de la semana                  |
| Visualización         | Histogram / Distribution   | Gráfico que muestra frecuencia de valores                           | Distribución de estadías por cantidad de noches                    |
| Visualización         | Boxplot / Outliers         | Visualización de rango y valores extremos                           | Detectar precios fuera de lo común en reservas                     |
| Visualización         | Pairplot / Correlation     | Comparación cruzada entre variables numéricas                       | Relación entre tarifa, ocupación y tipo de habitación              |
| Almacenamiento        | Object Storage / Bucket    | Almacenamiento escalable en OCI para datasets y resultados          | Guardar CSV con reservas históricas                                |
| Almacenamiento        | Dataset / CSV / JSON       | Formatos de datos para análisis y entrenamiento de modelos          | Subir archivo “cancelaciones_2023.csv” al bucket                   |
| Almacenamiento        | Data Flow / Data Catalog   | Servicios para procesar y documentar grandes volúmenes de datos     | Catalogar datasets sobre temporada alta y baja                     |
| Seguridad             | Vault / Secret Keeper      | Gestión segura de credenciales y claves                             | Conectar notebook con base Oracle sin exponer claves               |
| Seguridad             | Encryption / Access Policy | Protección de datos y reglas de acceso                              | Definir política que prohíba modificar modelos desde marketing     |
| Redes                 | VCN / Subnet / NAT / SG    | Red virtual y componentes para tráfico interno y externo            | Acceder a Object Storage sin exponer IP pública                    |
| Redes                 | Public / Private Endpoint  | Configuración de acceso a servicios desde dentro o fuera de OCI     | API de predicción solo accesible desde subnet del hotel            |
| Redes                 | Internet Gateway / Route   | Permisos para que una red tenga salida a internet                   | Notebook con acceso a repositorios externos                        |
| Prácticas MLOps       | Escalado / Load Balancer   | Optimización de recursos para alta demanda                          | Aumentar recursos si el uso del modelo crece durante temporada alta|
| Prácticas MLOps       | Monitoring / Logging       | Seguimiento de métricas y eventos en producción                     | Ver cuántas veces se consultó el modelo desde recepción            |
| Prácticas MLOps       | Explainability / Feature Importance| Herramientas para interpretar el modelo                     | Mostrar que “tipo de cliente” impacta más en cancelaciones         |
| Prácticas MLOps       | Retraining / Drift         | Reentrenamiento y detección de cambios en los datos                 | Actualizar modelo si cambian patrones de reserva                   |
| SDK / Herramientas    | Python SDK / OCI SDK       | Librerías para interactuar con servicios OCI desde código           | Crear bucket y notebook usando Python desde script                    |
| SDK / Herramientas    | ADS SDK / ADSInterpreter   | Herramientas específicas para ciencia de datos en OCI               | Generar explicación de modelo con gráficos automáticos                |
| SDK / Herramientas    | OCI CLI                    | Interfaz de línea de comandos para operar servicios OCI             | Lanzar notebook o subir archivos directamente desde consola           |
| Infraestructura       | Terraform / Resource Manager| Infraestructura como código para automatizar configuración          | Crear compartimientos y políticas de acceso de forma repetible        |
| Infraestructura       | Stack / Plan / Apply       | Proceso de despliegue con Terraform: definir, previsualizar, ejecutar| Desplegar recursos para nuevo hotel sin errores manuales              |
| Organización           | Tags / Cost Tracking        | Etiquetado de recursos y seguimiento de costos                      | Ver cuánto cuesta entrenar modelos en entorno “TemporadaAlta”         |
| Buenas prácticas      | Modularización / Reusabilidad| Separar funciones para claridad y mantenimiento                     | Validaciones de reserva en módulo “utils”                             |
| Buenas prácticas      | Confirmación / Validación  | Evitar errores críticos con chequeos y confirmaciones explícitas    | Confirmar borrado de modelo con “¿Estás seguro? [y/n]”                |
| Buenas prácticas      | Documentación / Naming     | Uso de nombres claros y descripciones en código y estructura        | Bucket “datos_cancelaciones_hotelA_2023”                              |
| Bonus Ctrl+BA         | Ficha técnica / Glosario Ctrl| Recurso con términos clave y ejemplos integrados                    | Usar en mentorías dentro del servidor Ctrl+BA                         |
| Bonus Ctrl+BA         | Cuestionarios / Flashcards | Material para repasar y autoevaluarse en 3 niveles                  | Fichas para revisar IAM, ML y MLOps antes del examen                  |
| Bonus Ctrl+BA         | Presentación / Teaching Pack| Recurso didáctico para exponer temas en clase o comunidad           | Explicar el ciclo ML con ejemplos hoteleros y slides visuales         |




---

En un proyecto de Machine Learning en OCI (o en cualquier entorno cloud moderno), los actores o perfiles cumplen roles complementarios que permiten llevar una solución desde la idea hasta el despliegue y mantenimiento. Aquí te dejo una clasificación clara y modular que podés usar como base para documentar o planificar tus proyectos:

---

## 🧑‍💼 Actores en un Proyecto de Machine Learning

| Actor / Perfil | Rol principal | Funcionalidades clave |
|----------------|---------------|------------------------|
| **Usuario Visual / Analista** | Interacción con resultados y dashboards | - Usa la **OCI Console** para explorar notebooks y visualizar métricas<br>- Interpreta salidas del modelo para decisiones de negocio<br>- No programa, pero necesita claridad en los resultados |
| **Científico de Datos** | Desarrollo y entrenamiento de modelos | - Crea notebooks y scripts en Python<br>- Usa **SDKs** para lanzar Jobs, entrenar y evaluar modelos<br>- Experimenta con algoritmos y limpieza de datos<br>- Documenta y versiona experimentos |
| **Desarrollador / DevOps** | Integración y automatización | - Usa **SDKs**, **REST API** y **CLI** para automatizar flujos<br>- Despliega modelos como endpoints<br>- Configura pipelines y triggers<br>- Gestiona recursos y seguridad |
| **Integrador / Arquitecto de Soluciones** | Conexión entre sistemas y servicios | - Diseña cómo el modelo se conecta con otros sistemas (ERP, CRM, etc.)<br>- Usa **REST API** para integrar el modelo en apps externas<br>- Define arquitectura en OCI (compartimentos, redes, seguridad) |
| **Administrador de Infraestructura / Cloud Engineer** | Gestión de recursos y costos | - Configura entornos, compartimentos, políticas IAM<br>- Monitorea uso de recursos y optimiza costos<br>- Asegura cumplimiento y escalabilidad |
| **Stakeholder / Product Owner** | Visión estratégica y validación | - Define objetivos del modelo<br>- Evalúa impacto en negocio<br>- Participa en validación de resultados<br>- No técnico, pero clave en decisiones |

---

## 🧠 Ejemplo de colaboración

Imaginá que estás desarrollando un modelo de predicción de demanda:

- El **Científico de Datos** entrena el modelo con datos históricos.
- El **Desarrollador** crea un pipeline que lanza el Job cada semana.
- El **Integrador** conecta el modelo con el sistema de inventario.
- El **Usuario Visual** revisa los resultados en un dashboard.
- El **Administrador** asegura que todo corra en un entorno seguro y eficiente.
- El **Stakeholder** valida si el modelo mejora la planificación.

---

