# Importamos las 2 librerías que necesitaremos para este proyecto
import requests
import pyfiglet

# Utilizaremos Pyfiglet para crearnos un Banner para el programa
banner = pyfiglet.figlet_format("Russoski Tools \n Subdom Enum")
print(banner)

# Creamos una variable donde solicitar al usuario el Dominio (ejemplo: google.com)
dominio = input("-> Introduce un Dominio para enumerar: ")
print("-> Estamos comprobando todo...")

# La variable Archivo se encargará de almacenar y leer el contenido del diccionario
# La variable Subdominios contendrá el contenido de Archivo pero dividido en líneas
archivo = open("subdomains-top1mil-5000.txt").read() 
subdominios = archivo.splitlines()

# Iniciamos un bucle For que recorrerá cada línea del diccionario en busca de Subdominios válidos
for subdominio in subdominios:
    # Realizaremos en cada vuelta una petición web con el Dominio que ingrese
    # el usuario y la línea del diccionario correspondiente a dicha vuelta
    linea_enumeracion = f"https://{subdominio}.{dominio}" 
    # Emplearemos un Control de Excepciones en donde realizaremos las
    # peticiones web con el contenido de la variable Linea_enumeracion
    try:
        requests.get(linea_enumeracion)
    # La Excepción se producirá cuando haya un error de conexión al servidor, lo que será ignorado
    except requests.ConnectionError: 
        pass
    # En caso contrario, de que sí devuelva una respuesta el servidor,
    # se considerará que el Subdominio existe y se mostrará por pantalla
    else:
        print("--------------------------------------------------------------------")
        print("<EMILY> encontró un Subdominio válido: " + linea_enumeracion)
print("--------------------------------------------------------------------")