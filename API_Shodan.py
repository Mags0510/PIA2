import shodan

APIKEY = input("Introduce tu API Key de Shodan: ")
API = shodan.Shodan(APIKEY)
consulta = 'apache 2.4.49'

try:
    resultados = API.search(consulta)
    print(f'Resultados para la consulta "{consulta}": {resultados["total"]} encontrados')
    with open("resultados_shodan.txt", "w") as archivo:
        archivo.write(f'Resultados para la consulta "{consulta}": {resultados["total"]} encontrados\n\n')
        
        for resultado in resultados["matches"]:
            ip = resultado.get('ip_str', 'N/A')
            puerto = resultado.get('port', 'N/A')
            organizacion = resultado.get('org', 'N/A')
            pais = resultado.get('location', {}).get('country_name', 'N/A')
            
            info = (
                f"IP: {ip}\n"
                f"Puerto: {puerto}\n"
                f"Organizacion: {organizacion}\n"
                f"Ubicacion: {pais}\n"
                f"- - - - - - - - - - - - -\n"
            )
            print(info)
            archivo.write(info)

        print("informacion guaradad en resultados_shodan.txt")

except shodan.APIError as e:
    print(f"Error: {e}")
