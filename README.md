# ft-benchmark

Este benchmark compara los protocolos `http`, `https` y `ftp` en su velocidad
para descargar conjuntos de ficheros numerosos. En particular, se prueba contra
una carga real, consistente en 333 archivos de música pesando 3GB en total.

La **carga** consiste en las obras de órgano de Bach, licenciadas en Creative
Commons y
tocadas por James Kibbie, como pueden descargarse aquí:

[http://www.blockmrecords.org/bach/download.htm](http://www.blockmrecords.org/bach/download.htm)

Sin embargo, se provee también con un script (`load.py`) que escribe archivos
aleatorios que simulan la carga.


## Preparación

Este benchmark se realizó contra servidores `apache` para http y `vsftp` para
ftp. Deben instalarse antes de iniciar el experimento. Además, debe permitirse
el uso de `https` en el servidor apache, lo que requerirá de configuración
especial.

La carga debe colocarse bajo un directorio de nombre `bach/` sobre la raíz del
servidor. En particular, el script buscará en las direcciones:

```
ftp://localhost/bach
http://localhost/bach
https://localhost/bach
```

## Ejecución

El script sólo requiere la intervención del usuario para introducir el usuario y
contraseña de `ftp`. Una ayuda a los parámetros que requiere el script puede
consultarse ejecutando:

```bash
python3 benchmark.py --help
```

En particular, el script puede aceptar la contraseña como argumento o dentro del
propio script, para evitar que el usuario deba escribirla en texto plano como
argumento.

El script informará del avance del experimento, pero puede tardar varios minutos
en terminar cada una de las fases.


## Scripts auxiliares

Con el script principal, se incluyen una serie de auxiliares que ayudan a su
ejecución:

* `load.py`: crea una carga sintética similar a la real usada en el experimento.
* `timer.py`: calcula el tiempo completo y crea el archivo `time.csv` con los
  datos.
* `stat.r`: ejecuta los tests estadísticos ANOVA y LSD sobre `time.csv`.
* `download.sh`: utiliza un protocolo dado para ejecutar una descarga.
