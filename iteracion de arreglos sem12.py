# Crear una matriz 3D para almacenar datos de temperaturas
# Primera dimensión: Ciudades (3 ciudades)
# Segunda dimensión: Días de la semana (7 días)
# Tercera dimensión: Semanas (4 semanas)
temperaturas = [
    [   # Ciudad 1
        [   # Semana 1
            {"day": "Lunes", "temp": 37},
            {"day": "Martes", "temp": 35},
            {"day": "Miércoles", "temp": 33},
            {"day": "Jueves", "temp": 36},
            {"day": "Viernes", "temp": 37},
            {"day": "Sábado", "temp": 38},
            {"day": "Domingo", "temp": 38}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 38},
            {"day": "Martes", "temp": 36},
            {"day": "Miércoles", "temp": 36},
            {"day": "Jueves", "temp": 36},
            {"day": "Viernes", "temp": 35},
            {"day": "Sábado", "temp": 36},
            {"day": "Domingo", "temp": 35}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 35},
            {"day": "Martes", "temp": 35},
            {"day": "Miércoles", "temp": 34},
            {"day": "Jueves", "temp": 32},
            {"day": "Viernes", "temp": 35},
            {"day": "Sábado", "temp": 36},
            {"day": "Domingo", "temp": 36}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 33},
            {"day": "Martes", "temp": 35},
            {"day": "Miércoles", "temp": 36},
            {"day": "Jueves", "temp": 36},
            {"day": "Viernes", "temp": 37},
            {"day": "Sábado", "temp": 36},
            {"day": "Domingo", "temp": 35}
        ]
    ],
    [   # Ciudad 2
        [   # Semana 1
            {"day": "Lunes", "temp": 28},
            {"day": "Martes", "temp": 25},
            {"day": "Miércoles", "temp": 26},
            {"day": "Jueves", "temp": 27},
            {"day": "Viernes", "temp": 27},
            {"day": "Sábado", "temp": 28},
            {"day": "Domingo", "temp": 28}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 28},
            {"day": "Martes", "temp": 27},
            {"day": "Miércoles", "temp": 27},
            {"day": "Jueves", "temp": 26},
            {"day": "Viernes", "temp": 27},
            {"day": "Sábado", "temp": 27},
            {"day": "Domingo", "temp": 25}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 25},
            {"day": "Martes", "temp": 26},
            {"day": "Miércoles", "temp": 26},
            {"day": "Jueves", "temp": 26},
            {"day": "Viernes", "temp": 27},
            {"day": "Sábado", "temp": 27},
            {"day": "Domingo", "temp": 27}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 27},
            {"day": "Martes", "temp": 27},
            {"day": "Miércoles", "temp": 27},
            {"day": "Jueves", "temp": 272},
            {"day": "Viernes", "temp": 26},
            {"day": "Sábado", "temp": 27},
            {"day": "Domingo", "temp": 28}
        ]
    ],
    [   # Ciudad 3
        [   # Semana 1
            {"day": "Lunes", "temp": 22},
            {"day": "Martes", "temp": 22},
            {"day": "Miércoles", "temp": 19},
            {"day": "Jueves", "temp": 19},
            {"day": "Viernes", "temp": 21},
            {"day": "Sábado", "temp": 21},
            {"day": "Domingo", "temp": 20}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 21},
            {"day": "Martes", "temp": 23},
            {"day": "Miércoles", "temp": 21},
            {"day": "Jueves", "temp": 21},
            {"day": "Viernes", "temp": 20},
            {"day": "Sábado", "temp": 20},
            {"day": "Domingo", "temp": 19}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 19},
            {"day": "Martes", "temp": 22},
            {"day": "Miércoles", "temp": 23},
            {"day": "Jueves", "temp": 23},
            {"day": "Viernes", "temp": 24},
            {"day": "Sábado", "temp": 22},
            {"day": "Domingo", "temp": 21}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 23},
            {"day": "Martes", "temp": 22},
            {"day": "Miércoles", "temp": 25},
            {"day": "Jueves", "temp": 25},
            {"day": "Viernes", "temp": 24},
            {"day": "Sábado", "temp": 23},
            {"day": "Domingo", "temp": 23}
        ]
    ]
]

# Calcular el promedio de temperaturas para cada ciudad y semana
ciudades = ["Guayaquil", "Esmeraldas", "Quito"]
for ciudad_idx, ciudad in enumerate(temperaturas):
    for semana_idx, semana in enumerate(ciudad):
        suma_temperaturas = sum([dia["temp"] for dia in semana])
        promedio = suma_temperaturas / len(semana)
        print(f"La temperatura en la semana {semana_idx + 1}, en la ciudad de {ciudades[ciudad_idx]} fue de un promedio de {promedio:.2f} grados Celsius")