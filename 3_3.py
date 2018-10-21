from OpenGL.GLU import *
from OpenGL.GL import *
from OpenGL.GLUT import *
import sys
from pprint import pprint

currentPoint = (0, 0)
first_letter_points = []
first_letter_moves = []

second_letter_points = []
second_letter_moves = []

first_letter_angle = 30
second_letter_angle = -30


def load_letter(file_name, points, moves):
    with open(file_name) as f:
        content = f.readlines()
        content = [x.strip() for x in content]
        point_number = int(content.pop(0))

        for point in content[:point_number]:
            points.append(tuple([int(coordinate) for coordinate in point.split(' ')]))
        del content[:point_number]

        content.pop(0)

        for move in content:
            moves.append(int(move))


def main():
    global first_letter_moves
    global first_letter_points
    global second_letter_moves
    global second_letter_points

    load_letter('./data/3_3/first_letter.txt', first_letter_points, first_letter_moves)
    pprint(first_letter_points)
    pprint(first_letter_moves)
    load_letter('./data/3_3/second_letter.txt', second_letter_points, second_letter_moves)
    pprint(second_letter_points)
    pprint(second_letter_moves)

    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(800, 600)
    glutInitWindowPosition(100, 150)
    glutCreateWindow("OpenGL lesson 3")
    glutDisplayFunc(display_all)
    glutReshapeFunc(reshape)
    glutKeyboardFunc(process_normal_keys)
    glutSpecialFunc(process_special_keys)
    glutMainLoop()


def move_to(point):
    global currentPoint
    currentPoint = point


def line_to(point):
    global currentPoint
    glBegin(GL_LINE_STRIP)
    glVertex2i(currentPoint[0], currentPoint[1])
    glVertex2i(point[0], point[1])
    glEnd()
    currentPoint = point


def display(points, moves):
    for move in moves:
        if move < 0:
            move_to(points[abs(move) - 1])
        else:
            line_to(points[move - 1])
        glFlush()


def display_all():
    pprint('display_all')
    global first_letter_moves
    global first_letter_points
    global second_letter_moves
    global second_letter_points

    glClearColor(1, 1, 1, 0)
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0, 0, 0)
    glColor3d(1, 0, 0)

    display(first_letter_points, first_letter_moves)
    display(second_letter_points, second_letter_moves)


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
        display_all()
    elif key == b'+':
        pprint('Here1')
        glMatrixMode(GL_MODELVIEW)
        glScale(1.1, 1.1, 0)
        display_all()
    elif key == b'-':
        glMatrixMode(GL_MODELVIEW)
        glScale(0.9, 0.9, 0)
        display_all()


def process_special_keys(key, x, y):
    if GLUT_KEY_UP == key:
        glMatrixMode(GL_MODELVIEW)
        glTranslated(0, 100, 0)
        display_all()
    elif GLUT_KEY_DOWN == key:
        glMatrixMode(GL_MODELVIEW)
        glTranslated(0, -100, 0)
        display_all()
    elif GLUT_KEY_LEFT == key:
        glMatrixMode(GL_MODELVIEW)
        glTranslated(-100, 0, 0)
        display_all()
    elif GLUT_KEY_RIGHT == key:
        glMatrixMode(GL_MODELVIEW)
        glTranslated(100, 0, 0)
        display_all()
    elif GLUT_KEY_HOME == key:
        pprint('HOME')
        glMatrixMode(GL_MODELVIEW)
        glRotatef(-30.0, 0.0, 0.0, 1.0)
        display_all()
    elif GLUT_KEY_END == key:
        pprint('END')
        glMatrixMode(GL_MODELVIEW)
        glRotatef(30.0, 0.0, 0.0, 1.0)
        display_all()
    elif GLUT_KEY_PAGE_UP == key:
        pprint('PG_UP')
        glMatrixMode(GL_MODELVIEW)

        global first_letter_moves
        global first_letter_points
        global second_letter_moves
        global second_letter_points
        global first_letter_angle
        global second_letter_angle

        glClearColor(1, 1, 1, 0)
        glClear(GL_COLOR_BUFFER_BIT)
        glColor3f(0, 0, 0)
        glColor3d(1, 0, 0)

        glPushMatrix()
        glRotatef(first_letter_angle, 0.0, 0.0, 1.0)
        display(first_letter_points, first_letter_moves)
        first_letter_angle += 30
        glPopMatrix()

        glPushMatrix()
        glRotatef(second_letter_angle, 0.0, 0.0, 1.0)
        display(second_letter_points, second_letter_moves)
        second_letter_angle -= 30
        glPopMatrix()


main()
