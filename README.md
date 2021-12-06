# Vision artificial: Final
## Safety Camera

### Nuestro proyecto
Este proyecto se creo con la idea de crear una camara que solo permita que se saque una foto si las personas detectadas 
en el cuadro estan sonriendo y con los ojos abiertos. Si se quiere sacar la foto y una de estas dos cosas no se cumplen,
no lo permite, y se avisa en la pantalla cual es el problema por el cual no esta sacando la foto. Si se cumplen ambas 
condiciones, saca la foto y la abre en una nueva ventana. En el caso de querer repetir la foto simplemente se vuelve a 
la ventana original y se vuelve a apretar la tecla s.

Este codigo se armo con las referencias de los tutoriales de Geeks for geeks 
[smile detection](https://www.geeksforgeeks.org/python-smile-detection-using-opencv/)
y [eyes detection](https://www.geeksforgeeks.org/python-eye-blink-detection-project/)

El codigo utiliza Haar-cascades que son clasificadores que se utilizan para detectar caracteristicas especificas 
de la cara. Estos se utilizan descargandolos en formato XML y superponiendolos en la imagen para detectar, en este 
caso, la cara, los ojos y la sonrisa, segun el clasificador que se utilice.

Primero detecta la cara con el face_cascade, se la define en un area con un rectangulo, y este area se utiliza como 
region de interes para detectar los ojos y la sonrisa con los clasificadores eye_cascade y smile_cascade respectivamente.

Una vez que se corre el codigo, si en la imagen no se detecta una cara, se indica con un texto en rojo: "No face 
detected". De la misma manera, si se detecta la cara, pero no se detectan los ojos, la sonrisa o ambas dos juntas, 
se informa de la misma manera (con un texto rojo). Al contrario, si se detecta la cara, y luego los ojos y la sonrisa,
se informa con un texto en verde "Eye and smile detected! Press s to begin", y al apretar la tecla "s" se toma la foto
y se guarda en una ventana nueva. 
Si se vuelve a la ventana original y se toma una nueva foto, cumpliendo con los requisitos para tomarla, se guardara 
esta en la otra ventana, eliminando la foto anterior.

Ademas, lo que se le incorporo al codigo es que si aparece mas de una persona, se tienen que cumplir las condiciones 
en todos los participantes para que se permita tomar la foto. Esto se logro detectando cuantas caras se encontraban,
con  amount_of_people = len(all_faces), y utilizando el clasificador de ojos y sonrisa en cada una de las caras. Si hay 
la misma cantidad de caras que de pares de ojos y sonrisas, entonces permite sacar la foto. Si hay mas caras que 
sonrisas o pares de ojos, quiere decir que alguno no cumple con los requerimientos para permitir sacar la foto y aparece
en la pantalla la razon por la que no se deja sacar la foto.

