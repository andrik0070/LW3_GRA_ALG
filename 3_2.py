from OpenGL.GLU import *
from OpenGL.GL import *
from OpenGL.GLUT import *
import sys
from pprint import pprint

currentPoint = (0, 0)
points = []
moves = []


def main():
    with open('./data/3_2.txt') as f:
        content = f.readlines()
        content = [x.strip() for x in content]
        point_number = int(content.pop(0))
        global points
        for point in content[:point_number]:
            points.append(tuple([int(coordinate) for coordinate in point.split(' ')]))
        del content[:point_number]

        content.pop(0)

        global moves
        for move in content:
            moves.append(int(move))

        pprint(points)
        pprint(moves)

    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(800, 600)
    glutInitWindowPosition(100, 150)
    glutCreateWindow("OpenGL lesson 3")
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutKeyboardFunc(process_normal_keys)
    glutSpecialFunc(process_special_keys)
    glutMainLoop()


def move_to(point):
    global currentPoint
    currentPoint = point


def line_to(point):
    global currentPoint
    pprint(point)
    glBegin(GL_LINE_STRIP)
    glVertex2i(currentPoint[0], currentPoint[1])
    glVertex2i(point[0], point[1])
    glEnd()
    currentPoint = point


def display():
    glClearColor(1, 1, 1, 0)
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0, 0, 0)
    glColor3d(1, 0, 0)

    global moves
    global points

    pprint(moves)
    pprint(points)

    for move in moves:
        if move < 0:
            move_to(points[abs(move) - 1])
        else:
            line_to(points[move - 1])
        glFlush()


def reshape(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-500, 500, -500, 500)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def process_normal_keys(key, x, y):
    pprint(key)
    if key == 27:
        return
    elif key == 65:
        glMatrixMode(GL_MODELVIEW)
        glTranslated(20, 20, 0)
        display()
    elif key == b'+':
        glMatrixMode(GL_MODELVIEW)
        glScale(1.1, 1.1, 0)
        display()
    elif key == b'-':
        glMatrixMode(GL_MODELVIEW)
        glScale(0.9, 0.9, 0)
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


main()
