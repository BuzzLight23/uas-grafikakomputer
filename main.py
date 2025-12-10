from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys

def init():
    """Inisialisasi pengaturan OpenGL."""
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glEnable(GL_DEPTH_TEST)

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
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