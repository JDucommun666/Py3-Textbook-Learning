__author__ = 'JDucommun'
from math import sin, cos, radians

def main():
    angle, vel, h0, time = getInputs()
    cball - Projectile(angle, vel, h0)
    while cball.getY() >= 0:
        cball.update(time)
    print("\nDistance Traveled: {0:0.1f} meters.".format(cball.getX()))