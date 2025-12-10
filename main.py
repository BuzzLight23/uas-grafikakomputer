from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys

camera_angle_x = 20.0
camera_angle_y = 0.0
camera_distance = 40.0

def init():
    """Inisialisasi pengaturan OpenGL."""
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glEnable(GL_DEPTH_TEST)


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
    glBegin(gl_mode)
    for i, v in enumerate(vertices):
        # Penentuan warna (Sama seperti kode asli)
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