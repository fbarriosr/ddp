# DDP

Genera archivos .cub visualizables con el programa GaussView o cualquier otro capaz de leer archivos .cub provenientes de Gaussian. Corresponden a los campos escalares del potencial de las funciones de Fukui nucleofílica, Fukui electrofílica y del descriptor dual. No son los mismos archivos que genera el código dualDescriptor, de hecho ddp está en investigación pues ddp se basa en el cálculo del potencial electrostático molecular. Por cada sistema molecular, requiere como alimentación de tres archivos .fchk correspondientes al sistema con N, N+p y N-q electrones.
Utilizable solo en servidores con sistema operativo Linux y siempre tenga instalados y operativos
los programas Gaussian y sus complementarios cubegen y cubman.


## Requerimientos

Requiere python 3.

## Installation

Descarga el proyecto desde Github usando la opción zip o git clone. Mueve el proyecto DDP a una carpeta en tu computador. 

Descomprime el archivo zip mediante consola o usando las herramientas del sistema operativo (click derecho descomprimir)
```
$zip ddp.zip
```
También puedes crear un alias en $ .bashrc. (en MAC OS se llama "bash_profile") Utiliza un editor de texto (vi, vim, nano u otro)
```
$ nano ~.bashrc
```
Y agrega esta ultima linea: 
```
alias ddp='python /home/user/DDP/ddp.py'
```
la ruta es donde esta guardado el proyecto en tu computadora

## INSTRUCCIONES DE USO DE DDP

Se basa en resultados obtenidos desde cálculos mecano-cuánticos (a niveles de teoría Hartree-Fock, DFT así como también Post-Hartree-Fock) mediante el paquete de programas de química cuántica Gaussian 16.

Procure tener en un mismo directorio los archivos .fchk del sistema original (con N electrones) y del mismo sistema con N+p y con N-q electrones (misma geometría y mismos valores de coordenadas cartesianas o internas, ver archivos de ejemplo .gjf), donde p y q corresponden a los grados de degeneración de orbitales de frontera LUMO y HOMO, respectivamente. Los nombres de los archivos .fchk deben terminar en guion bajo seguido del numero de electrones en la forma N, N+p y N-q. Cada archivo .fchk debe proceder de un cálculo de punto sencillo (single point) y no de cálculos de optimización geométrica.

El estilo de como denominar a los archivos .fchk puede ser como el que se muestra a continuación:

Molecula_N+p.fchk, Molecula_N.fchk y Molecula_N-q.fchk

En el nombre pueden ir guiones bajos o medios, por ejemplo: Molecula_isomero-2_N+p.fchk, Molecula_isomero-2_N.fchk y Molecula_isomero-2_N-q.fchk

Como se puede apreciar, la raíz del nombre debe ser la misma en los 3 archivos (en este ejemplo es Molecula_isomero-2). Otro  ejemplo más concreto y simple: C6H6_N+1.fchk, C6H6_N.fchk y C6H6_N-2.fchk

 Ud. como usuario debe conocer de antemano los valores de p y q. Como recomendación, en el caso de compuestos organometalicos y metalo-organicos, la degeneracion en orbitales de frontera puede estimarse si, simultáneamente se cumple lo siguiente:

1. La diferencia energetica entre HOMO y los orbitales ocupados vecinos inmediatamente anteriores es inferior al 2% de la brecha HOMO-LUMO.
2. La diferencia energetica entre LUMO y los orbitales virtuales vecinos inmediatamente siguientes es inferior al 2% de la brecha HOMO-LUMO.

El porcentaje mencionado es arbitrario y se basa en experiencias con algunos compuestos de ese tipo, aunque podría ampliarse el valor hasta no más de un 5% de la brecha HOMO-LUMO. De todas maneras es un criterio mucho más flexible que la exigencia diferencia de energía igual a cero entre orbitales lo que es más común de cumplirse en compuestos orgánicos.

Si desea crear archivos .cub con las dimensiones del archivo .cub correspondiente a la densidad electrónica de la estructura molecular con mayor número de electrones (N+p electrones, luego se trata de considerar al archivo cuyo nombre debe finalizar en _N+p_den.cub), coloque en el mismo directorio donde se encuentran los archivos .fchk el archivo de la densidad electronica con N+p electrones, es decir, el de nombre finalizado en _N+p_den.cub. Ese archivo lo puede crear mediante el comando cubegen (por favor, remitirse al manual de Gaussian para generar el archivo _N+p_den.cub)

Si no posee ese archivo _N+p_den.cub y desea que sea creado dentro de la misma secuencia de acciones que ofrece DDP, entonces siga las instrucciones del menu interactivo que le ofrece DDP.

Si no desea por ningún motivo dimensionar los tamaños de los archivos .cub en base al tamaño del archivo _N+1_den.cub, DDP le ofrecerá un menú donde Ud. podrá dimensionar los archivos de potential electrostático molecular (archivos del tipo MEP) en base al tamaño del archivo .cub MEP con N electrones, o en base al archivo .cub MEP con N+p electrones o en base al archivo .cub MEP con N-q electrones.

Al final, el programa siempre se producirán los archivos siguientes:

Potencial de la función de Fukui nucleofílica
Potencial de la función de Fukui electrofílica
Potencial de la función de Fukui
Potential del descriptor dual

Adicionalmente se generan los archivos de potencial electrostático molecular (MEP) con N, N+p y N-q electrones, respectivamente.
Y dependiendo de la opción 2 del menú del programa, también se obtendrá el archivo de densidad electrónica del sistema con N+p electrones (si es que no lo tenía antes y decidió generarlo con este programa).
De todas maneras, estos archivos MEP y de densidad electrónica se pueden generar mediante el uso directo del comando cubegen que ofrece Gaussian.

Version Linea de Comandos:
```
$ ddp
```
