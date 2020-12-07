# proyecto3-TET
UNIVERSIDAD EAFIT
INGENIERÍA DE SISTEMAS

STO0263 TÓPICOS ESPECIALES EN TELEMÁTICA, 2020-2
GRUPO 002

PROYECTO 3 – BIG DATA / SPARK

Enunciado Original del proyecto: 
https://drive.google.com/file/d/1YZTZwNu-8JUszI4TX9k3fq6ksVlm5DLE/view?usp=sharing

Documento de diseño e implementación (PDF) – 30%

Integrantes + emails:

Jenny Quiroz - jquirozm@eafit.edu.co
Nicolás Grajales Molina - ngrajale@eafit.edu.co
Santiago Escobar Mejía - sescobarm@eafit.edu.co

Códigos fuentes generados en el proyecto durante todas las etapas del ciclo de vida (en un github): URL: https://github.com/ngrajale13/proyecto3-TET

Descripción técnica Infraestructura tecnológica desplegada en AWS (más posiblemente en el DCA) – 40%:

Escogimos tomar como dataset el provisto por el gobierno frente a los casos de covis en el país, debido a que permite hacer análisis diversos y muy interesantes y es un dataset muy completo y constantemente actualizado.
El plan fue realizar una ingesta de datos automática con un programa que constantemente estuviera subiendo y sobrescribiendo los datos descargados de
https://www.datos.gov.co/Salud-y-Protecci-n-Social/Casos-positivos-de-COVID-19-en-Colombia/gt2j-8ykr/data a un bucket S3 , desde este S3 los datos serian tomados hacia una base de datos Hive en hadoop y puestos en una tabla donde de procesarian y se respoderia a distintas preguntas como, numero total de casos femeninos contra numero total de casos masculinos y otras. Con estos resultados se plantea una visualización por powerbi.

Arquitectura de referencia base para tener en cuenta:

Desarrollo de cada una de las etapas del proceso:

Fuentes: 
Datos COVID-19 de Colombia 2020
https://www.datos.gov.co/Salud-y-Protecci-n-Social/Casos-positivos-de-COVID-19-en-Colombia/gt2j-8ykr/data 

Ingesta:




Almacenamiento:



Procesamiento:

Visualización:













Otras consideraciones:
….
