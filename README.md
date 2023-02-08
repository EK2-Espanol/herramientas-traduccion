# Herramientas de traducción

## Detalles
Todas las herramientas están escritas en Python 3.11.1 y compiladas con PyInstaller 5.7.0
<br />Las herramientas están listas para ser usadas desde la sección "Releases" a la derecha -->

## Herramientas
### 1. Buscador
  **Descripción:**
  Recibe una serie de palabras y devuelve:
  <br /> &emsp;**Si se ha _encontrado una palabra_:** un archivo .txt con información respecto a los archivos y líneas donde se encuentran dichas palabras
  <br /> &emsp;**Si _no_ se ha encontrado ninguna palabra:** un cuadro de aviso informando que ninguna palabra ha sido encontrada
  <br /> <br />
  **Propósito:** Ayudar a la corrección, principalmente tras ver algún fallo ingame
  <br /> <br />
  **A tener en cuenta:**
  <br /> &emsp;Comprobar que el programa está en la raíz del directorio de la traducción
  <br /> &emsp;No distingue entre mayúsculas y minúsculas
  <br /> &emsp;No distingue entre palabras y sílabas; En caso de buscar "Escarcha" devolverá también "Rompescarcha"
  <br /> <br />
  **Cómo usarlo:**
  <br />
  1. Introducir las palabras a encontrar y darle al botón de buscar
  <br />![image](https://user-images.githubusercontent.com/77066213/217523835-c27c403b-3eea-46d5-8fc1-b074390ce992.png)
  <br /> <br />
  2. Se abrirá el archivo "resultados.txt" creado en el mismo directorio
  <br />![image](https://user-images.githubusercontent.com/77066213/217523961-4ee951da-aa75-4fd2-8088-e051b16e1037.png)

