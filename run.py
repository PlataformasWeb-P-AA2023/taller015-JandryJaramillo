import pandas as pd
import requests

propietarioss = pd.read_csv('data/propietarios.csv', delimiter='|')
print(propietarioss)

for index, row in propietarioss.iterrows():
    cedula = row['cedula']
    nombre = row['nombre']
    apellido = row['apellido']
    
    data = {
        'cedula': cedula,
        'nombre': nombre,
        'apellido': apellido
    }
    
    r = requests.post('http://127.0.0.1:8000/propietarios/', data=data, auth=('jandry', '1234'))
    
    if r.status_code == 201:
        print(f"Propietario '{nombre} {apellido}' creado exitosamente.")
    else:
        print(f"Error al crear el propietario '{nombre} {apellido}'. Error {r.status_code}: {r.text}")

edificioss = pd.read_csv('data/edificios.csv', delimiter='|')
print(edificioss)

for index, row in edificioss.iterrows():
    nombre = row['nombre']
    direccion = row['dirección']
    ciudad = row['ciudad']
    tipo = row['tipo']
    
    data = {
        'nombre': nombre,
        'direccion': direccion,
        'ciudad': ciudad,
        'tipo': tipo,
    }
    
    r = requests.post('http://127.0.0.1:8000/edificios/', data=data, auth=('jandry', '1234'))
    
    if r.status_code == 201:
        print(f"Edificio '{nombre} {tipo}' creado exitosamente.")
    else:
        print(f"Error al crear el edificio '{nombre} {tipo}'. Error {r.status_code}: {r.text}")

propietarios = requests.get("http://127.0.0.1:8000/propietarios/", auth=('jandry', '1234')).json()
print(propietarios)

edificios = requests.get("http://127.0.0.1:8000/edificios/", auth=('jandry', '1234')).json()
print(edificios)

departamentos = pd.read_csv('data/departamentos.csv', delimiter='|')
print(departamentos)

for _, row in departamentos.iterrows():
    propietario_url = None
    for p in propietarios:
        if p['cedula'] == str(row['Propietario']):
            propietario_url = p["url"]
            break

    if not propietario_url:
        print(f"Error: Propietario not found for '{row['Propietario']} {row['Cuartos']} {row['Costo']}'")
        continue

    edificio_url = None
    for e in edificios:
        if e['nombre'] == row['Edificio']:
            edificio_url = e["url"]
            break

    if not edificio_url:
        print(f"Error: Edificio not found for '{row['Edificio']}'")
        continue

    data = {
        'propietario': propietario_url,
        'costo': row['Costo'],
        'num_cuartos': int(row['Cuartos']),
        'edificio': edificio_url
    }

    r = requests.post('http://127.0.0.1:8000/departamentos/', data=data, auth=('jandry', '1234'))
    print(r)
