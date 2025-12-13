"""
📋 Prerequisites

- Python 3.7 or higher
- PyOpenGL
- PyOpenGL-accelerate

📄 Install required dependencies: pip install PyOpenGL PyOpenGL-accelerate

🚀 Run the program: python uas_grafkom_kel8.py
"""

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys
import math

#  Variabel Global 
# Kamera
camera_angle_x = 20.0  # Sudut vertikal (atas/bawah)
camera_angle_y = 0.0   # Sudut horizontal (kiri/kanan)
camera_distance = 40.0 # Jarak kamera dari mobil

# Posisi & Arah Mobil (Baru)
car_x = 0.0
car_z = 0.0
car_heading = 0.0      # Arah hadap mobil (derajat)
speed = 0.0

# Mobil
steer_angle = 0.0       # Sudut belok roda depan
MAX_STEER = 45.0       

#  Variabel Animasi Pintu & Hood 
left_door_angle = 0.0
left_door_state = 0   # 0: Tutup, 1: Buka, 2: Terbuka, 3: Tutup
right_door_angle = 0.0
right_door_state = 0
hood_angle = 0.0
hood_state = 0

MAX_DOOR_ANGLE = 60.0
MAX_HOOD_ANGLE = 40.0

def init():
    """Inisialisasi pengaturan OpenGL."""
    glClearColor(0.0, 0.0, 0.0, 1.0) # Latar belakang hitam
    glEnable(GL_DEPTH_TEST)

#  Definisi Vertex 
ground = [
    [-8,-0.5,60.0], [8,-0.5,60.0], [8,-0.5,-60.0], [-8,-0.5,-60.0],
    [-40,-0.6,60.0], [40,-0.6,60.0], [40,-0.6,-60.0], [-40,-0.6,-60.0],
]
frontBody = [
    [2.8,1.0,10.5], [3.0,1.0,8.0], [2.8,3.5,10.5], [3.0,4.0,8.0],
    [0.0,3.5,10.7], [0.0,4.0,8.0], [-2.8,3.5,10.5], [-3.0,4.0,8.0],
    [-2.8,1.0,10.5], [-3.0,1.0,8.0], [0.0,1.1,10.7], [0.0,1.1,8.0],
    [2.8,1.0,10.5], [3.0,1.0,8.0],
]
grill = [
    [2.8,1.0,10.5], [2.8,3.5,10.5], [0.0,1.1,10.7], [0.0,3.5,10.7],
    [-2.8,1.0,10.5], [-2.8,3.5,10.5],
]
frontLight = [
    [2.6,3.2,10.55], [1.6,3.2,10.6], [1.6,2.7,10.6], [2.6,2.7,10.55],
    [-2.6,3.2,10.55], [-1.6,3.2,10.6], [-1.6,2.7,10.6], [-2.6,2.7,10.55],
]
hood = [
    [3.0,4.0,8.0], [3.0,4.0,4.0], [-3.0,4.0,4.0], [-3.0,4.0,8.0],
]
insideHood = [
    [-3.0,3,4.0], [-3.0,4,8], [3.0,4,8], [3.0,3,4] 
]
leftTirePanel = [
    [-3.0,1.0,8.0], [-3.0,4.0,8.0], [-3.0,2.5,7.0], [-3.0,4.0,6.0],
    [-3.0,2.5,5.0], [-3.0,4.0,4.0], [-3.0,1.0,4.0],
]
rightTirePanel = [
    [3.0,1.0,8.0], [3.0,4.0,8.0], [3.0,2.5,7.0], [3.0,4.0,6.0],
    [3.0,2.5,5.0], [3.0,4.0,4.0], [3.0,1.0,4.0],
]
frontGlassRim = [
    [-3.0,4.0,4.0], [3.0,4.0,4.0], [3.0,6.0,1.0], [-3.0,6.0,1.0],
]
frontGlass = [
    [-2.8,4.0,4.08], [2.8,4.0,4.08], [2.8,5.9,1.14], [-2.8,5.9,1.14],
]
roof = [
    [-3.0,6.0,1.0], [3.0,6.0,1.0], [3.0,6.0,-3.0], [-3.0,6.0,-3.0],
]
rightBody = [
    [-3.0,6.0,-2.0], [-3.0,6.0,-3.0], [-3.0,4.5,-5.0], [-3.0,2.5,-5.0], [-3.0,1.0,-4.0], 
    [-3.0,1.0,-3.0], [-3.0,1.0,-2.0],
]
leftBody = [
    [3.0,6.0,-2.0], [3.0,6.0,-3.0], [3.0,4.5,-5.0], [3.0,2.5,-5.0],[3.0,1.0,-4.0], 
    [3.0,1.0,-3.0], [3.0,1.0,-2.0]
]
backInterior = [
    [-3.0,1.0,-2.0], [-3.0,6.0,-2.0], [3.0,6.0,-2.0], [3.0,1.0,-2.0], 
]
frontInterior = [
    [-3.0,4.0,4.0], [-3.0,1.0,4.0], [3.0,1.0,4.0], [3.0,4.0,4.0] 
]
rightDoorPanel = [
    [-3.0,4.0,4.0], [-3.0,6.0,1.0], [-3.0,6.0,-2],
    [-3.0,1.0,-2], [-3.0,1.0,4.0],
]
leftDoorPanel = [
    [3.0,4.0,4.0], [3.0,6.0,1.0], [3.0,6.0,-2.0], 
    [3.0,1.0,-2], [3.0,1.0,4.0],
]
bottom = [
    [-3.0,1.0,4.0], [3.0,1.0,4.0], [3.0,1.0,-4.0], [-3.0,1.0,-4.0],
]
rightGlassOne = [
    [-3.1,4.0,3.5], [-3.1,5.8,0.8], [-3.1,5.8,-0.8], [-3.1,4.0,-0.8],
]
leftGlassOne = [
    [3.1,4.0,3.5], [3.1,5.8,0.8], [3.1,5.8,-1.0], [3.1,4.0,-1.0],
]
actualRightHandle = [
    [-3.1,3.5,0.0], [-3.1,3.5,0.8], [-3.1,3.2,0.8], [-3.1,3.2,0.0],
]
leftHandle = [
    [3.1,3.5,0.0], [3.1,3.5,0.8], [3.1,3.2,0.8], [3.1,3.2,0.0],
]
backGlass = [
    [-2.8,5.9,-3.3], [2.8,5.9,-3.3], [2.8,4.5,-5.0], [-2.8,4.5,-5.0],
]
backGlassRim = [
    [-3.0,6.0,-3.0], [3.0,6.0,-3.0], [3.0,4.5,-5.0], [-3.0,4.5,-5.0],
]
backTirePanel = [
    [3.0,2.5,-5.0], [3.0,2.5,-7.5], [3.0,4.5,-5.0], [3.0,4.0,-7.0],
    [-3.0,4.5,-5.0], [-3.0,4.0,-7.0], [-3.0,2.5,-5.0], [-3.0,2.5,-7.5],
    [3.0,2.5,-5.0], [3.0,2.5,-7.5],
]
backBody = [
    [3.0,1.0,-8.0], [3.0,1.5,-10.0], [3.0,4.0,-7.0], [3.0,4.5,-10.5],
    [-3.0,4.0,-7.0], [-3.0,4.5,-10.5], [-3.0,1.0,-8.0], [-3.0,1.5,-10.0],
    [3.0,1.0,-8.0], [3.0,1.5,-10.0],
]
bumper = [
    [-3.0,1.5,-10.0], [3.0,1.5,-10.0], [3.0,4.5,-10.5], [-3.0,4.5,-10.5],
]
backLight = [
    [-2.6,3.5,-10.4], [-1.2,3.5,-10.4], [-1.2,4.2,-10.5], [-2.6,4.2,-10.5],
    [2.6,3.5,-10.4], [1.2,3.5,-10.4], [1.2,4.2,-10.5], [2.6,4.2,-10.5],
]

def draw_geometry(vertices, gl_mode, color=None):
    RED_MAIN = (0.85, 0.10, 0.10)
    RED_DARK = (0.55, 0.05, 0.05)
    RED_LIGHT = (0.95, 0.25, 0.25)
    RED_ACCENT = (1.00, 0.35, 0.35)
    GLASS_DARK = (0.15, 0.15, 0.17)
    LIGHT_WHITE = (1.00, 0.95, 0.95)
    
    glBegin(gl_mode)
    for i, v in enumerate(vertices):
        if color:
            glColor3f(color[0], color[1], color[2])
        elif vertices is ground:
            if i < 4: glColor3f(0.3, 0.3, 0.3) 
            else: glColor3f(0.176, 0.623, 0.098)
        elif vertices is frontLight: glColor3f(1.0, 1.0, 1.0) 
        elif vertices is backLight: glColor3f(1.0, 0.0, 0.0) 
        elif vertices is frontGlass: glColor3f(0.15, 0.15, 0.17) 
        elif vertices is roof: glColor3f(0.55, 0.05, 0.05) 
        elif vertices is backInterior: glColor3f(0.55, 0.05, 0.05)
        elif vertices is frontInterior: glColor3f(0.55, 0.05, 0.05)
        elif vertices is frontGlassRim : glColor3f(0.55, 0.05, 0.05)
        elif vertices is backGlassRim: glColor3f(0.55, 0.05, 0.05) 
        elif vertices is grill: glColor3f(0.85, 0.10, 0.10) 
        elif vertices is hood: glColor3f(0.55, 0.05, 0.05) 
        elif vertices is insideHood: glColor3f(0.85, 0.10, 0.10) 
        elif vertices is leftDoorPanel : glColor3f(0.7, 0.15, 0.15) 
        elif vertices is rightDoorPanel : glColor3f(0.7, 0.15, 0.15) 
        elif vertices is leftBody or vertices is rightBody: glColor3f(0.76, 0.10, 0.10) 
        elif vertices is backBody: glColor3f(0.85, 0.10, 0.10) 
        elif vertices is bumper: glColor3f(1.00, 0.35, 0.35) 
        elif vertices is backTirePanel: glColor3f(0.7, 0.15, 0.1)
        elif vertices in (rightGlassOne, leftGlassOne, backGlass, leftHandle, actualRightHandle):
            glColor3f(0.15, 0.15, 0.17) 
        else: glColor3f(0.76, 0.10, 0.10) 
            
        # Gambar vertex asli relatif terhadap pusat mobil
        glVertex3f(v[0], v[1], v[2])
    glEnd()

def draw_tires():
    """Menggambar keempat ban dengan logika steering."""
    global steer_angle
    glColor3f(0.1, 0.1, 0.1) 

    # Posisi ban relatif terhadap chassis mobil
    wheels = [
        (3.0, 1.0, 6.0, True),    # Kanan Depan
        (-3.0, 1.0, 6.0, True),   # Kiri Depan
        (-3.0, 1.0, -6.0, False), # Kiri Belakang
        (3.0, 1.0, -6.0, False)   # Kanan Belakang
    ]

    for x, y, z, is_front in wheels:
        glPushMatrix()
        
        # 1. Posisikan roda di chassis
        glTranslatef(x, y, z)
        
        # 2. Jika roda depan, putar (Steering)
        if is_front:
            glRotatef(steer_angle, 0, 1, 0)
        
        # 3. Orientasi ban (Torus tegak)
        glRotatef(90, 0, 1, 0)
        
        glutSolidTorus(0.75, 0.75, 10, 10)
        glPopMatrix()

def display():
    global camera_angle_x, camera_angle_y, camera_distance
    global car_x, car_z, car_heading
    global left_door_angle, right_door_angle, hood_angle

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    #  PENGATURAN KAMERA BARU 
    camX = camera_distance * math.sin(math.radians(camera_angle_y)) * math.cos(math.radians(camera_angle_x))
    camY = camera_distance * math.sin(math.radians(camera_angle_x))
    camZ = camera_distance * math.cos(math.radians(camera_angle_y)) * math.cos(math.radians(camera_angle_x))

    # Kamera selalu melihat ke posisi mobil saat ini (car_x, 1.0, car_z)
    gluLookAt(car_x + camX, camY, car_z + camZ,  # Posisi Kamera
              car_x, 1.0, car_z,                 # Titik yang dilihat (Pusat Mobil)
              0.0, 1.0, 0.0)                     # Up Vector

    #  GAMBAR GROUND (Lantai) 
    draw_geometry(ground, GL_QUADS)

    #  GAMBAR MOBIL 
    glPushMatrix()
    
    # 1. Pindahkan mobil ke posisi dunianya (Physics Update)
    glTranslatef(car_x, 0.0, car_z)
    
    # 2. Putar mobil sesuai arah hadapnya
    glRotatef(car_heading, 0, 1, 0)
    
    # Body Utama
    draw_geometry(frontBody, GL_QUAD_STRIP)
    draw_geometry(grill, GL_QUAD_STRIP)
    draw_geometry(frontLight, GL_QUADS)
    draw_geometry(leftTirePanel, GL_TRIANGLE_STRIP)
    draw_geometry(rightTirePanel, GL_TRIANGLE_STRIP)
    draw_geometry(frontGlassRim, GL_QUADS)
    draw_geometry(frontGlass, GL_QUADS)
    draw_geometry(roof, GL_QUADS)
    draw_geometry(leftBody, GL_TRIANGLE_FAN)
    draw_geometry(rightBody, GL_TRIANGLE_FAN)
    draw_geometry(backInterior, GL_QUADS)
    draw_geometry(frontInterior, GL_QUADS)
    draw_geometry(bottom, GL_QUADS)
    draw_geometry(backGlass, GL_QUADS)
    draw_geometry(backGlassRim, GL_QUADS)
    draw_geometry(backTirePanel, GL_QUAD_STRIP)
    draw_geometry(backBody, GL_QUAD_STRIP)
    draw_geometry(bumper, GL_QUADS)
    draw_geometry(backLight, GL_QUADS)
    draw_geometry(insideHood, GL_QUADS)

    # Hood (Kap Mesin)
    glPushMatrix()
    glTranslatef(0.0, 4.0, 4.0) 
    glRotatef(-hood_angle, 1, 0, 0)
    glTranslatef(0.0, -4.0, -4.0)
    draw_geometry(hood, GL_QUADS)
    glPopMatrix()

    # Pintu Kiri
    glPushMatrix()
    glTranslatef(3.0, 0.0, 4.0)
    glRotatef(-left_door_angle, 0, 1, 0)
    glTranslatef(-3.0, 0.0, -4.0)
    draw_geometry(leftDoorPanel, GL_TRIANGLE_FAN)
    draw_geometry(leftGlassOne, GL_QUADS)
    draw_geometry(leftHandle, GL_QUADS)
    glPopMatrix()

    # Pintu Kanan
    glPushMatrix()
    glTranslatef(-3.0, 0.0, 4.0)
    glRotatef(right_door_angle, 0, 1, 0)
    glTranslatef(3.0, 0.0, -4.0)
    draw_geometry(rightDoorPanel, GL_TRIANGLE_FAN)
    draw_geometry(rightGlassOne, GL_QUADS)
    draw_geometry(actualRightHandle, GL_QUADS) 
    glPopMatrix()

    # Ban
    draw_tires()
    glPopMatrix() 
    glutSwapBuffers()

def reshape(w, h):
    if h == 0: h = 1
    aspect = w / h
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, aspect, 0.1, 1000.0)
    glMatrixMode(GL_MODELVIEW)

def time_callback(x):
    global left_door_angle, left_door_state
    global right_door_angle, right_door_state
    global hood_angle, hood_state
    
    # Animasi Pintu & Hood
    if left_door_state == 1: 
        left_door_angle = min(left_door_angle + 2.0, MAX_DOOR_ANGLE)
        if left_door_angle == MAX_DOOR_ANGLE: left_door_state = 2
    elif left_door_state == 3: 
        left_door_angle = max(left_door_angle - 2.0, 0.0)
        if left_door_angle == 0.0: left_door_state = 0

    if right_door_state == 1: 
        right_door_angle = min(right_door_angle + 2.0, MAX_DOOR_ANGLE)
        if right_door_angle == MAX_DOOR_ANGLE: right_door_state = 2
    elif right_door_state == 3: 
        right_door_angle = max(right_door_angle - 2.0, 0.0)
        if right_door_angle == 0.0: right_door_state = 0

    if hood_state == 1: 
        hood_angle = min(hood_angle + 1.5, MAX_HOOD_ANGLE)
        if hood_angle == MAX_HOOD_ANGLE: hood_state = 2
    elif hood_state == 3: 
        hood_angle = max(hood_angle - 1.5, 0.0)
        if hood_angle == 0.0: hood_state = 0

    glutPostRedisplay()
    glutTimerFunc(int(1000/60), time_callback, 0)

def specialKey(key, x, y):
    """
    KONTROL KAMERA (ORBIT)
    Panah Atas/Bawah: Rotasi Vertikal
    Panah Kiri/Kanan: Rotasi Horizontal mengelilingi mobil
    """
    global camera_angle_x, camera_angle_y

    if key == GLUT_KEY_UP:
        camera_angle_x += 2.0
        if camera_angle_x > 89.0: camera_angle_x = 89.0 # Batas atas
    elif key == GLUT_KEY_DOWN:
        camera_angle_x -= 2.0
        if camera_angle_x < 5.0: camera_angle_x = 5.0   # Batas bawah (biar ga tembus tanah)
    elif key == GLUT_KEY_LEFT:
        camera_angle_y -= 2.0
    elif key == GLUT_KEY_RIGHT:
        camera_angle_y += 2.0
        
    glutPostRedisplay()

def keyboard(key, x, y):
    global steer_angle, car_x, car_z, car_heading
    global left_door_state, right_door_state, hood_state
    global camera_distance

    key_str = key.decode("utf-8").lower()
    
    move_speed = 0.5
    
    #  LOGIKA GERAK MOBIL & BELOK 
    if key_str == 'w': # MAJU
        # Jika ban belok, ubah arah hadap mobil perlahan
        if abs(steer_angle) > 1.0:
            car_heading += steer_angle * 0.05
        
        car_x += math.sin(math.radians(car_heading)) * move_speed
        car_z += math.cos(math.radians(car_heading)) * move_speed

    elif key_str == 's': # MUNDUR
        # Jika mundur, arah belok mobil terbalik efeknya
        if abs(steer_angle) > 1.0:
            car_heading -= steer_angle * 0.05
            
        car_x -= math.sin(math.radians(car_heading)) * move_speed
        car_z -= math.cos(math.radians(car_heading)) * move_speed
    
    # Steering 
    elif key_str == 'a':
        steer_angle += 2.0
        if steer_angle > MAX_STEER: steer_angle = MAX_STEER
    elif key_str == 'd':
        steer_angle -= 2.0
        if steer_angle < -MAX_STEER: steer_angle = -MAX_STEER

    # Animasi
    elif key_str == '1': # Pintu Kiri
        left_door_state = 1 if left_door_state in [0, 3] else 3
    elif key_str == '2': # Pintu Kanan
        right_door_state = 1 if right_door_state in [0, 3] else 3
    elif key_str == '3': # Hood
        hood_state = 1 if hood_state in [0, 3] else 3
    
    glutPostRedisplay()

def scroll(button, dir, x, y):
    global camera_distance
    if dir > 0:
        if camera_distance > 10: camera_distance -= 1.0 # Zoom In
    else:
        if camera_distance < 100: camera_distance += 1.0 # Zoom Out
    glutPostRedisplay()

def main():
    print(" KONTROL BARU ")
    print("[Arrow Keys]     : Rotasi Kamera Mengelilingi Mobil")
    print("[Scroll]         : Zoom In/Out")
    print("[W] / [S]        : Gas (Maju) / Rem (Mundur) -> Mobil akan berbelok jika ban miring")
    print("[A] / [D]        : Putar Setir (Belok Ban Depan)")
    print("[1] / [2]        : Buka Pintu Kiri / Kanan")
    print("[3]              : Buka Kap Mesin")
    
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowPosition(200, 100)
    glutInitWindowSize(800, 600)
    glutCreateWindow(b"Mobil: Physics Belok & Kamera Orbit") 

    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutSpecialFunc(specialKey)  
    glutKeyboardFunc(keyboard)  
    glutMouseWheelFunc(scroll) 
    glutTimerFunc(0, time_callback, 0)

    init()
    glutMainLoop()

if __name__ == '__main__':
    main()