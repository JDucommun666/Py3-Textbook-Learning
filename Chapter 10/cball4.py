__author__ = 'JDucommun'

from Projectile import projectile

def getInputs():
    a = eval(input("Enter the launch angle (degrees): "))
    v = eval(input("Enter initial velocity (m/s): "))
    h = eval(input("Enter initial height (in meters): "))
    t = eval(input("Enter time interval between position calculations: "))
    return a,v,h,t

def main():
    angle, vel, h0, time = getInputs()
    cball = projectile(angle, vel, h0)
    while cball.getY() >= 0:
        cball.update(time)
    print("\nDistance traveled: {0:0.1f} meters.".format(cball.getX()))

main()