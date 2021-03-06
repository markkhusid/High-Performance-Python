from random import uniform

# from matplotlib import pyplot as plt
# from matplotlib import animation

class Particle:
    def __init__(self, x, y, ang_vel):
        self.x = x
        self.y = y
        self.ang_vel = ang_vel

class ParticleSimulator:

    def __init__(self, particles):
        self.particles = particles

    def evolve(self, dt):
        timestep = 0.00001
        nsteps = int(dt/timestep)

        for i in range(nsteps):
            for p in self.particles:
                # 1. calculate the direction
                norm = (p.x**2 + p.y**2)**0.5
                v_x = -p.y/norm
                v_y = p.x/norm

                # 2. calculate the displacement
                d_x = timestep * p.ang_vel * v_x
                d_y = timestep * p.ang_vel * v_y

                p.x += d_x
                p.y += d_y
                # 3. repeat for all the time steps

def visualize(simulator):

    X = [p.x for p in simulator.particles]
    Y = [p.y for p in simulator.particles]

    fig = plt.figure()
    ax = plt.subplot(111, aspect='equal')
    line, = ax.plot(X, Y, 'ro')

    # Axis limits
    plt.xlim(-1, 1)
    plt.ylim(-1, 1)

    # It will be run when the animation starts
    def init():
        line.set_data([], [])
        return line, # The comma is important!

    def animate(i):
        # We let the particle evolve for 0.01 time units
        simulator.evolve(0.01)
        X = [p.x for p in simulator.particles]
        Y = [p.y for p in simulator.particles]

        line.set_data( X, Y)
        
        return line,

    # Call the animate function each 10 ms
    anim = animation.FuncAnimation(fig,
            animate,
            init_func = init,
            blit = True,
            interval = 10)

    plt.show()

def test_visualize():
    particles = [Particle(0.3, 0.5, 1),
            Particle(0.0, -0.5, -1),
            Particle(-0.1, -0.4, 3)]

    simulator = ParticleSimulator(particles)
    visualize(simulator)

def test_evolve():
	particles = [Particle( 0.3,  0.5,  1),
				 Particle( 0.0, -0.5, -1),
				 Particle(-0.1, -0.4,  3)]

	simulator = ParticleSimulator (particles)

	simulator.evolve(0.1)

	p0, p1, p2, = particles

	def fequal(a, b, eps = 1e-5):
		return abs(a-b) < eps


	assert fequal(p0.x, 0.210269)
	assert fequal(p0.y, 0.543863)

	if (fequal(p0.x, 0.210269) == True):
		print("[*] Particle 0 X test passed!")
		print("[*] p0.x = ", p0.x, " reference value = ", 0.219269, " difference = ", abs(p0.x - 0.210269))
		print("\n")

	if (fequal(p0.y, 0.543863) == True):
		print("[*] Particle 0 Y test passed!")
		print("[*] p0.y = ", p0.y, " reference value = ", 0.543863, " difference = ", abs(p0.y - 0.543863))
		print("\n"*2)

	assert fequal(p1.x, -0.099334)
	assert fequal(p1.y, -0.490034)
	
	if (fequal(p1.x, -0.099334) == True):
		print("[*] Particle 1 X test passed!")
		print("[*] p1.x = ", p1.x, " reference value = ", -0.099334, " difference = ", abs(p1.x - (-0.099334)))
		print("\n")

	if (fequal(p1.y, -0.490034) == True):
		print("[*] Partticle 1 Y test passed")
		print("[*] p1.y = ", p1.y, " reference value = ", -0.490034, " difference = ", abs(p1.y - (-0.490034)))
		print("\n"*2)

	assert fequal(p2.x, 0.191358)
	assert fequal(p2.y, -0.365227)

	if (fequal(p2.x, 0.191358) == True):
		print("[*] Particle 0 X tests passed!")
		print("[*] p2.x = ", p2.x, " reference value = ", 0.191358, " difference = ", abs(p2.x - 0.191358))
		print("\n")

	if (fequal(p2.y, -0.365227) == True):
		print("[*] p2.y = ", p2.y, " reference value = ", -0.365227, " difference = ", abs(p2.y - (-0.365227)))
		print("\n"*2)

def benchmark():
	particles = [Particle(uniform(-1.0, 1.0),
						  uniform(-1.0, 1.0),
						  uniform(-1.0, 1.0))
				for i in range(1000)]

	simulator = ParticleSimulator(particles)
	simulator.evolve(0.1)


if __name__ == '__main__':
    benchmark()
