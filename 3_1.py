from OpenGL.GLU import *
from OpenGL.GL import *
from OpenGL.GLUT import *


def reshape(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, 700, 0, 700)
    glMatrixMode(GL_MODELVIEW)


def display():
    glClearColor(1, 1, 1, 0)
    glClear(GL_COLOR_BUFFER_BIT)
    glBegin(GL_QUADS)
    glColor3f(1.0, 1.0, 1.0)
    glVertex2i(250, 450)
    glColor3f(0.0, 0.0, 1.0)
    glVertex2i(250, 150)
    glColor3f(0.0, 1.0, 0.0)
    glVertex2i(550, 150)
    glColor3f(1.0, 0.0, 0.0)
    glVertex2i(550, 450)
    glEnd()
    glutSwapBuffers()
    glPushMatrix()
    glLoadIdentity()
    glBegin(GL_LINES)
    glColor3f(0, 0, 1)
    glVertex2i(0, 350)
    glVertex2i(700, 350)
    glVertex2i(350, 0)
    glVertex2i(350, 700)
    glEnd()
    glutSwapBuffers()
    glPopMatrix()
    glDisable(GL_CLIP_PLANE0)


def process_normal_keys(key, x, y):
    if key == 27:
        return
    if key == 65:
        glMatrixMode(GL_MODELVIEW)
        glTranslated(20, 20, 0)
        display()


def process_special_keys(key, x, y):
    if GLUT_KEY_UP == key:
        glMatrixMode(GL_MODELVIEW)
        glTranslated(0, 100, 0)
        display()
    elif GLUT_KEY_DOWN == key:
        glMatrixMode(GL_MODELVIEW)
        glTranslated(0, -100, 0)
        display()
    elif GLUT_KEY_LEFT == key:
        glMatrixMode(GL_MODELVIEW)
        glTranslated(-100, 0, 0)
        display()
    elif GLUT_KEY_RIGHT == key:
        glMatrixMode(GL_MODELVIEW)
        glTranslated(100, 0, 0)
        display()


def main():
    glutInit(sys.argv)
    glutInitWindowSize(800, 600)
    glutCreateWindow("OpenGL lesson 5")
    glutReshapeFunc(reshape)
    glutDisplayFunc(display)
    glutKeyboardFunc(process_normal_keys)
    glutSpecialFunc(process_special_keys)
    glutMainLoop()


main()
