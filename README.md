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
