from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys

def init():
    """Inisialisasi pengaturan OpenGL."""
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glEnable(GL_DEPTH_TEST)

# Tambahkan variabel global
camera_angle_x = 20.0
camera_angle_y = 0.0
camera_distance = 40.0

# Tambahkan definisi ground
ground = [
    [-8,-0.5,60.0], [8,-0.5,60.0], [8,-0.5,-60.0], [-8,-0.5,-60.0],
    [-40,-0.6,60.0], [40,-0.6,60.0], [40,-0.6,-60.0], [-40,-0.6,-60.0],
]

def draw_geometry(vertices, gl_mode, color=None):
    glBegin(gl_mode)
    for i, v in enumerate(vertices):
        if vertices is ground:
            if i < 4: glColor3f(0.3, 0.3, 0.3)
            else: glColor3f(0.176, 0.623, 0.098)
        else:
            glColor3f(0.76, 0.10, 0.10)
        glVertex3f(v[0], v[1], v[2])
    glEnd()

# Update display() dengan kamera
def display():
    global camera_angle_x, camera_angle_y, camera_distance
    
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    
    import math
    camX = camera_distance * math.sin(math.radians(camera_angle_y)) * math.cos(math.radians(camera_angle_x))
    camY = camera_distance * math.sin(math.radians(camera_angle_x))
    camZ = camera_distance * math.cos(math.radians(camera_angle_y)) * math.cos(math.radians(camera_angle_x))
    
    gluLookAt(camX, camY, camZ, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0)
    
    draw_geometry(ground, GL_QUADS)
    
    glutSwapBuffers()
def reshape(w, h):
    if h == 0: h = 1
    aspect = w / h
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, aspect, 0.1, 1000.0)
    glMatrixMode(GL_MODELVIEW)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowPosition(200, 100)
    glutInitWindowSize(800, 600)
    glutCreateWindow(b"Car 3D Model")
    
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    
    init()
    glutMainLoop()

if __name__ == '__main__':
    main()