## Gráficos Dinámicos con Django

![image](https://github.com/Jhonatan2022/Cruds-Multi-languages/assets/101368711/eb85a832-0bc2-473a-830a-c3917b75b8b7)


## Requisitos

* python instalado: [python](https://www.python.org/downloads/)


## Pasos a seguir
```sh
# Clonar el repositorio
git clone https://github.com/Jhonatan2022/Cruds-Multi-languages.git
```
```sh
```sh
# Accedemos al la carpeta del proyecto
cd .\Graficos-Dinamicos-Django\
```
```sh
# Instalamos virtualenv si no lo tenemos 
pip install virtualenv
```
```sh
# Damos los permisos necesarios por powershell
Set-ExecutionPolicy RemoteSigned
```
```sh
# Creamos un entorno virtual
virtualenv env
```
```sh
# Activamos el entorno virtual
env\Scripts\activate
```
```sh
# Instalamos los requerimientos
pip install -r requirements.sh
```
```sh
# Creamos las migraciones
python manage.py migrate
```
```sh
# Corremos el app
python manage.py runserver
```
```sh
# Accedemos a la ruta donde se encuentra el proyecto
http://127.0.0.1:8000/
```
