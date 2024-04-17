## Expresión regular que valida una Contraseña fuerte
- 1 minúscula
- 1 mayúscula
- 1 número
- 1 carácter especial
- 8 caracteres de longitud

~~~
^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^\w\d\s]).{8,}$
~~~

*Comprobacion*

![image](https://github.com/Marly-R/RepoNuevo/assets/160815306/4145418a-e598-46e9-8054-fee552bf51de)

![image](https://github.com/Marly-R/RepoNuevo/assets/160815306/e2776730-9bbf-461d-ab68-8441c6269962)


## Expresión Regular que valida un Nombre de usuario
- Longitud de 3 a 16 caracteres
- Letra o número o guion medio o bajo

~~~
^[a-zA-Z0-9_-]{3,16}$
~~~

*Comprobacion*

![image](https://github.com/Marly-R/RepoNuevo/assets/160815306/b00212dc-9d84-4611-a5b3-db7e75ed203f)

![image](https://github.com/Marly-R/RepoNuevo/assets/160815306/8d8d9432-d713-4b8c-a30a-a33a2409df27)


