# Herramientas de traducción

## 1. Buscador
  **Descripción:**
  Recibe una serie de palabras y devuelve:
  <br /> &emsp;**Si se ha _encontrado una palabra_:** un archivo .txt con información respecto a los archivos y líneas donde se encuentran dichas palabras
  <br /> &emsp;**Si _no_ se ha encontrado ninguna palabra:** un cuadro de aviso informando que ninguna palabra ha sido encontrada
  <br /> <br />
  **Propósito:** Ayudar a la corrección, principalmente tras ver algún fallo ingame
  <br /> <br />
  **A tener en cuenta:**
  <br /> &emsp;Importante comprobar que el programa está en la raíz del directorio de la traducción
  <br /> &emsp;&emsp;Tratará de recorrer todas las carpetas y archivos presentes, lo que podría provocar que crashee de no estar en el directorio adecuado
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

