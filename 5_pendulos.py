
# ================================================================================
# ANIMACION SISTEMA SOLAR
#
# Genera una animación a partir de un fichero de datos con las posiciones
# de los planetas en diferentes instantes de tiempo.
# 
# El fichero debe estructurarse de la siguiente forma:
# 
#   x1_1, y1_1
#   x2_1, y2_1
#   x3_1, y3_1
#   (...)
#   xN_1, yN_1
#   
#   x1_2, y1_2
#   x2_2, y2_2
#   x3_2, y3_2
#   (...)
#   xN_2, yN_2
#
#   x1_3, y1_3
#   x2_3, y2_3
#   x3_3, y3_3
#   (...)
#   xN_3, yN_3
#   
#   (...)
#
# donde xi_j es la componente x del planeta i-ésimo en el instante de
# tiempo j-ésimo, e yi_j lo mismo en la componente y. El programa asume que
# el nº de planetas es siempre el mismo.
# ¡OJO! Los datos están separados por comas.
# 
# Si solo se especifica un instante de tiempo, se genera una imagen en pdf
# en lugar de una animación
#
# Se puede configurar la animación cambiando el valor de las variables
# de la sección "Parámetros"
#
# Hecho por Rubén Hurtado
#
# ================================================================================

# Importa los módulos necesarios
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Circle
import numpy as np

# Parámetros
# ========================================
file_in = "0_2.dat" # Nombre del fichero de datos
file_in_2 = "0_201.dat"
file_in_3 = "0_202.dat"
file_in_4 = "0_203.dat"
file_in_5 = "0_204.dat"
file_in_6 = "0_205.dat"
file_out = "25_Especial" # Nombre del fichero de salida (sin extensión)

# Límites de los ejes X e Y
x_min = -2
x_max = 2
y_min = -2.5
y_max = 1

interval = 20 # Tiempo entre fotogramas en milisegundos
show_trail = False # Muestra la "estela" del planeta
trail_width = 1 # Ancho de la estela
save_to_file = True # False: muestra la animación por pantalla,
                     # True: la guarda en un fichero
dpi = 150 # Calidad del vídeo de salida (dots per inch)

# Radio del planeta, en las mismas unidades que la posición
# Puede ser un número (el radio de todos los planetas) o una lista con
# el radio de cada uno
planet_radius = [0.022,0.022] 
#planet_radius = [0.5, 0.7, 1.1]


# Lectura del fichero de datos
# ========================================
# Lee el fichero a una cadena de texto
with open(file_in, "r") as f:
    data_str = f.read()
with open(file_in_2, "r") as f:
    data_str_2 = f.read()
with open(file_in_3, "r") as f:
    data_str_3 = f.read()
with open(file_in_4, "r") as f:
    data_str_4 = f.read()
with open(file_in_5, "r") as f:
    data_str_5 = f.read()
with open(file_in_6, "r") as f:
    data_str_6 = f.read()

# Inicializa la lista con los datos de cada fotograma.
# frames_data[j] contiene los datos del fotograma j-ésimo
frames_data = []
frames_data_2 = []
frames_data_3 = []
frames_data_4 = []
frames_data_5 = []
frames_data_6 = []

# Itera sobre los bloques de texto separados por líneas vacías
# (cada bloque corresponde a un instante de tiempo)
for frame_data_str in data_str.split("\n\n"):
    # Inicializa la lista con la posición de cada planeta
    frame_data = []

    # Itera sobre las líneas del bloque
    # (cada línea da la posición de un planta)
    for planet_pos_str in frame_data_str.split("\n"):
        # Lee la componente x e y de la línea
        planet_pos = np.fromstring(planet_pos_str, sep=",")
        # Si la línea no está vacía, añade planet_pos a la lista de 
        # posiciones del fotograma
        if planet_pos.size > 0:
            frame_data.append(np.fromstring(planet_pos_str, sep=","))
    frames_data.append(frame_data)
            
for frame_data_str in data_str_2.split("\n\n"):
    frame_data = []
    for planet_pos_str in frame_data_str.split("\n"):
        planet_pos = np.fromstring(planet_pos_str, sep=",")
        if planet_pos.size > 0:
            frame_data.append(np.fromstring(planet_pos_str, sep=","))
    frames_data_2.append(frame_data)

for frame_data_str in data_str_3.split("\n\n"):
    frame_data = []
    for planet_pos_str in frame_data_str.split("\n"):
        planet_pos = np.fromstring(planet_pos_str, sep=",")
        if planet_pos.size > 0:
            frame_data.append(np.fromstring(planet_pos_str, sep=","))
    frames_data_3.append(frame_data)
    
for frame_data_str in data_str_4.split("\n\n"):
    frame_data = []
    for planet_pos_str in frame_data_str.split("\n"):
        planet_pos = np.fromstring(planet_pos_str, sep=",")
        if planet_pos.size > 0:
            frame_data.append(np.fromstring(planet_pos_str, sep=","))
    frames_data_4.append(frame_data)

for frame_data_str in data_str_5.split("\n\n"):
    frame_data = []
    for planet_pos_str in frame_data_str.split("\n"):
        planet_pos = np.fromstring(planet_pos_str, sep=",")
        if planet_pos.size > 0:
            frame_data.append(np.fromstring(planet_pos_str, sep=","))
    frames_data_5.append(frame_data)

for frame_data_str in data_str_6.split("\n\n"):
    frame_data = []
    for planet_pos_str in frame_data_str.split("\n"):
        planet_pos = np.fromstring(planet_pos_str, sep=",")
        if planet_pos.size > 0:
            frame_data.append(np.fromstring(planet_pos_str, sep=","))
    frames_data_6.append(frame_data)


# El número de planetas es el número de líneas en cada bloque
# Lo calculamos del primer bloque
nplanets = len(frames_data[0])


# Creación de la animación/gráfico
# ========================================
# Crea los objetos figure y axis
fig, ax = plt.subplots()

# Define el rango de los ejes
ax.axis("equal")  # Misma escala para ejes X e Y
ax.set_xlim(x_min, x_max)
ax.set_ylim(y_min, y_max)

# Si solo se ha dado un radio para todos los planetas, conviértelo a una
# lista con todos los elementos iguales
if not hasattr(planet_radius, "__iter__"):
    planet_radius = planet_radius*np.ones(nplanets)
# En caso contrario, comprueba que el nº de radios coincide con el
# nº de planetas y devuelve error en caso contrario
else:
    if not nplanets == len(planet_radius):
        raise ValueError(
                "El número de radios especificados no coincide con el número "
                "de planetas")

# Representa el primer fotograma
# Pinta un punto en la posición de cada paneta y guarda el objeto asociado
# al punto en una lista
planet_points = []
planet_points_2 = []
planet_points_3 = []
planet_points_4 = []
planet_points_5 = []
planet_points_6 = []
planet_trails = list()

for planet_pos, radius in zip(frames_data[0], planet_radius):
    x, y = planet_pos
    #planet_point, = ax.plot(x, y, "o", markersize=10)
    planet_point = Circle((x, y), radius, facecolor='red')
    ax.add_artist(planet_point)
    planet_points.append(planet_point)
    
for planet_pos, radius in zip(frames_data_2[0], planet_radius):
    x, y = planet_pos
    planet_point = Circle((x, y), radius, facecolor='orange')
    ax.add_artist(planet_point)
    planet_points_2.append(planet_point)

for planet_pos, radius in zip(frames_data_3[0], planet_radius):
    x, y = planet_pos
    planet_point = Circle((x, y), radius, facecolor='yellow')
    ax.add_artist(planet_point)
    planet_points_3.append(planet_point)
    
for planet_pos, radius in zip(frames_data_4[0], planet_radius):
    x, y = planet_pos
    planet_point = Circle((x, y), radius, facecolor='green')
    ax.add_artist(planet_point)
    planet_points_4.append(planet_point)

for planet_pos, radius in zip(frames_data_5[0], planet_radius):
    x, y = planet_pos
    planet_point = Circle((x, y), radius, facecolor='blue')
    ax.add_artist(planet_point)
    planet_points_5.append(planet_point)
    
for planet_pos, radius in zip(frames_data_6[0], planet_radius):
    x, y = planet_pos
    planet_point = Circle((x, y), radius, facecolor='purple')
    ax.add_artist(planet_point)
    planet_points_6.append(planet_point)
    
    # Inicializa las estelas (si especificado en los parámetros)
    if show_trail:
        planet_trail, = ax.plot(
                x, y, "-", linewidth=trail_width,
                color=planet_points[-1].get_facecolor())
        planet_trails.append(planet_trail)
        
    planet_points = planet_points + planet_points_2 + planet_points_3 + planet_points_4 + planet_points_5 + planet_points_6
    
    line, = ax.plot([], [], "-", color="red")
    line2, = ax.plot([], [], "-", color="red")
    line3, = ax.plot([], [], "-", color="orange")
    line4, = ax.plot([], [], "-", color="orange")
    line5, = ax.plot([], [], "-", color="yellow")
    line6, = ax.plot([], [], "-", color="yellow")
    line7, = ax.plot([], [], "-", color="green")
    line8, = ax.plot([], [], "-", color="green")
    line9, = ax.plot([], [], "-", color="blue")
    line10, = ax.plot([], [], "-", color="blue")
    line11, = ax.plot([], [], "-", color="purple")
    line12, = ax.plot([], [], "-", color="purple")
# Función que actualiza la posición de los planetas en la animación 
def update(j_frame, frames_data, planet_points, planet_trails, show_trail):
    # Actualiza la posición del correspondiente a cada planeta
    for j_planet, planet_pos in enumerate(frames_data[j_frame]):
        x, y = planet_pos
        planet_points[j_planet].center = (x, y)

        if show_trail:
            xs_old, ys_old = planet_trails[j_planet].get_data()
            xs_new = np.append(xs_old, x)
            ys_new = np.append(ys_old, y)

            planet_trails[j_planet].set_data(xs_new, ys_new)
            
    for j_planet, planet_pos in enumerate(frames_data_2[j_frame]):
        x, y = planet_pos
        planet_points_2[j_planet].center = (x, y)

    for j_planet, planet_pos in enumerate(frames_data_3[j_frame]):
        x, y = planet_pos
        planet_points_3[j_planet].center = (x, y)
        
    for j_planet, planet_pos in enumerate(frames_data_4[j_frame]):
        x, y = planet_pos
        planet_points_4[j_planet].center = (x, y)

    for j_planet, planet_pos in enumerate(frames_data_5[j_frame]):
        x, y = planet_pos
        planet_points_5[j_planet].center = (x, y)
        
    for j_planet, planet_pos in enumerate(frames_data_6[j_frame]):
        x, y = planet_pos
        planet_points_6[j_planet].center = (x, y)
    
    # Actualiza la posición de la línea
    x1, y1 = frames_data[j_frame][0]
    x2, y2 = frames_data[j_frame][1]
    x3, y3 = frames_data_2[j_frame][0]
    x4, y4 = frames_data_2[j_frame][1]
    x5, y5 = frames_data_3[j_frame][0]
    x6, y6 = frames_data_3[j_frame][1]
    x7, y7 = frames_data_4[j_frame][0]
    x8, y8 = frames_data_4[j_frame][1]
    x9, y9 = frames_data_5[j_frame][0]
    x10, y10 = frames_data_5[j_frame][1]
    x11, y11 = frames_data_6[j_frame][0]
    x12, y12 = frames_data_6[j_frame][1]
    line.set_data([x1, x2], [y1, y2])
    line2.set_data([0, x1], [0, y1])
    line3.set_data([x3, x4], [y3, y4])
    line4.set_data([0, x3], [0, y3])
    line5.set_data([x5, x6], [y5, y6])
    line6.set_data([0, x5], [0, y5])
    line7.set_data([x7, x8], [y7, y8])
    line8.set_data([0, x7], [0, y7])
    line9.set_data([x9, x10], [y9, y10])
    line10.set_data([0, x9], [0, y9])
    line11.set_data([x11, x12], [y11, y12])
    line12.set_data([0, x11], [0, y11])

    return planet_points + planet_trails + [line] + [line2] + [line3] + [line4] + [line5] + [line6] + [line7] + [line8] + [line9] + [line10] + [line11] + [line12]

def init_anim():
    # Clear trails
    if show_trail:
        for j_planet in range(nplanets):
            planet_trails[j_planet].set_data(list(), list())
            
    # Inicializa la línea vacía
    line.set_data([], [])
    
    line2, = ax.plot([], [], "-", color="black")

    return planet_points + planet_trails+ [line] + [line2]

# Calcula el nº de frames
nframes = len(frames_data)

# Si hay más de un instante de tiempo, genera la animación
if nframes > 1:
    # Info sobre FuncAnimation: https://matplotlib.org/stable/api/animation_api.html
    animation = FuncAnimation(
            fig, update, init_func=init_anim,
            fargs=(frames_data, planet_points, planet_trails, show_trail),
            frames=len(frames_data), blit=True, interval=interval)

    # Muestra por pantalla o guarda según parámetros
    if save_to_file:
        animation.save("{}.mp4".format(file_out), dpi=dpi)
    else:
        plt.show()
# En caso contrario, muestra o guarda una imagen
else:
    # Muestra por pantalla o guarda según parámetros
    if save_to_file:
        fig.savefig("{}.pdf".format(file_out))
    else:
        plt.show()