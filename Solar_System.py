Web VPython 3.2 

from vpython import *

sun = sphere(
    pos=vector(0,0,0),
    radius=10,
    color=vec(252/255,122/255,42/255)
)
mercury = sphere(
    pos=vector(15,0,0),
    radius=1,
    color=vec(150/255,133/255,112/255),
    make_trail=True
)
venus = sphere(
    pos=vector(20,0,0),
    radius=1.225,
    color=vec(211/255,69/255,22/255),
    make_trail=True
)
earth = sphere(
    pos=vector(25,0,0),
    radius=1.25,
    color=color.green,
    make_trail=True
)
mars = sphere(
    pos=vector(30,0,0),
    radius=1.2,
    color=color.orange,
    make_trail=True
)
jupiter = sphere(
    pos=vector(40,0,0),
    radius=4,
    color=vec(201/255,144/255,57/255),
    make_trail=True
)
saturn = sphere(
    pos=vector(50,0,0),
    radius=3.5,
    color=vec(234/255,214/255, 184/255),
    make_trail=True
)
saturn_ring = ring(
    pos=saturn.pos,
    axis=vector(0,0,1), 
    radius=4.5,         
    thickness=0.3,      
    color=vec(190/255,175/255,145/255)
)
uranus = sphere(
    pos=vector(60,0,0),
    radius=3,
    color=vec(172/255,229/255,238/255),
    make_trail=True
)
uranus_ring = ring(
    pos=uranus.pos,
    axis=vector(0,1,0), 
    radius=4.5,         
    thickness=0.1,      
    color=vec(172/255,229/255,238/255),
)
neptune = sphere(
    pos=vector(70,0,0),
    radius=2.85,
    color=color.blue,
    make_trail=True
)
earth_moon = sphere(
    pos=vector(27,0,0),
    radius=0.5,
    color=color.white,
    make_trail=True,
    retain=15
)
f_arrow = arrow(
    pos=earth_moon.pos,
    color=color.red,
    shaftwidth=0.5
)

scene.background = vec(0,0,0)

m2 = 100
m3 = 100
m4 = 10
m5 = 100
m6 = 31800
m7 = 30000
m8 = 30000
m9 = 30000
m10 = 1
#a=planet.pos.x-sun.pos.x
#b=planet.pos.y-sun.pos.y
#r=vector(-a,-b,0)
r=sun.pos-earth.pos
r1=sun.pos-mars.pos
r2=sun.pos-mercury.pos
r3=sun.pos-venus.pos
r4=sun.pos-jupiter.pos
r5=sun.pos-saturn.pos
r6=sun.pos-uranus.pos
r7=sun.pos-neptune.pos
r8=earth.pos-earth_moon.pos
v2=vector(0,10,0)
vm1=vector(0,10,0)
vhg1=vector(0,10,0)
vv1=vector(0,10,0)
vj1=vector(0,10,0)
vs1=vector(0,10,0)
vu1=vector(0,10,0)
vn1=vector(0,10,0)
vem1=vector(0,10,0)
c=(r.x**2+r.y**2)**(0.5)
c1=(r1.x**2+r1.y**2)**(0.5)
c2=(r2.x**2+r2.y**2)**(0.5)
c3=(r3.x**2+r3.y**2)**(0.5)
c4=(r4.x**2+r4.y**2)**(0.5)
c5=(r5.x**2+r5.y**2)**(0.5)
c6=(r6.x**2+r6.y**2)**(0.5)
c7=(r7.x**2+r7.y**2)**(0.5)
c8=(r8.x**2+r8.y**2)**(0.5)
#c=math.sqrt(r.x**2+r.y**2)
Fc=m2*mag(v2)**2/c#magnitude
Fc1=m3*mag(vm1)**2/c1
Fc2=m4*mag(vhg1)**2/c2
Fc3=m5*mag(vv1)**2/c3
Fc4=m6*mag(vj1)**2/c4
Fc5=m7*mag(vs1)**2/c5
Fc6=m8*mag(vu1)**2/c6
Fc7=m9*mag(vn1)**2/c7
Fc8=m10*mag(vem1)**2/c8
ac=Fc/m2
ac1=Fc1/m3
ac2=Fc2/m4
ac3=Fc3/m5
ac4=Fc4/m6
ac5=Fc5/m7
ac6=Fc6/m8
ac7=Fc7/m9
ac8=Fc8/m10
r_vec=norm(r)#normalize
r_vec1=norm(r1)
r_vec2=norm(r2)
r_vec3=norm(r3)
r_vec4=norm(r4)
r_vec5=norm(r5)
r_vec6=norm(r6)
r_vec7=norm(r7)
r_vec8=norm(r8)

dt = 0.01


while True:
    rate(100)
    f_arrow.pos=earth_moon.pos
    f_arrow.axis=(earth.pos-earth_moon.pos)*0.5
    r_vec=norm(sun.pos-earth.pos)
    r_vec1=norm(sun.pos-mars.pos)
    r_vec2=norm(sun.pos-mercury.pos)
    r_vec3=norm(sun.pos-venus.pos)
    r_vec4=norm(sun.pos-jupiter.pos)
    r_vec5=norm(sun.pos-saturn.pos)
    r_vec6=norm(sun.pos-uranus.pos)
    r_vec7=norm(sun.pos-neptune.pos)
    r_vec8=norm(earth.pos-earth_moon.pos)
    v2= v2+ (ac*r_vec)*dt
    vm1=vm1+ (ac1*r_vec1)*dt
    vhg1=vhg1+ (ac2*r_vec2)*dt
    vv1=vv1+ (ac3*r_vec3)*dt
    vj1=vj1+ (ac4*r_vec4)*dt
    vs1=vs1+ (ac5*r_vec5)*dt
    vu1=vu1+ (ac6*r_vec6)*dt
    vn1=vn1+ (ac7*r_vec7)*dt
    vem1=vem1+ (ac8*r_vec8)*dt
    earth.pos = earth.pos + v2 * dt
    mars.pos = mars.pos + vm1 * dt
    mercury.pos = mercury.pos + vhg1 * dt
    venus.pos = venus.pos + vv1 * dt
    jupiter.pos = jupiter.pos + vj1 * dt
    saturn.pos = saturn.pos + vs1 * dt
    saturn_ring.pos = saturn.pos
    uranus.pos = uranus.pos + vu1 * dt
    uranus_ring.pos = uranus.pos
    neptune.pos = neptune.pos + vn1 * dt
    earth_moon.pos = earth_moon.pos + (vem1 + v2) * dt
