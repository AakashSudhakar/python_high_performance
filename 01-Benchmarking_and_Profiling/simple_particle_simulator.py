#!python3

"""
NAME:   Aakash Sudhakar
DATE:   Sunday, June 3, 2018
DESC:   Program containing basic particle simulator. 
        Purpose is to achieve rudimentary benchmarking/profiling.
DIFF:   ?/5
"""

from matplotlib import pyplot as plt
from matplotlib import animation

class Particle:
    """ Generic particle class with object position and velocity. """

    def __init__(self, x, y, angular_velocity):
        """ 
        Particle class initializer.

        PARAMS:     {x}: X-position of instantiated object.
                    {y}: Y-position of instantiated object.
                    {angular_velocity}: Directional velocity of instantiated object.
        RETURN:     N/A
        """
        self.x = x
        self.y = y
        self.angular_velocity = angular_velocity        # +/- sign determines rotational direction

class ParticleSimulator:
    """ Functional class that modifies Particle objects' positions and velocities. """

    def __init__(self, particles):
        """ 
        Particle Simulator class initializer.

        PARAMS:     {particles}: Instantiated Particle objects passed to simulator class. 
        RETURN:     N/A
        """
        self.particles = particles

    def evolve(self, dt):
        """ 
        Main method to parametrically modify particle positions and velocities. 

        PARAMS:     {dt}: Differential timestep for velocity modification.
        RETURN:     N/A
        """
        TIMESTEP = 1e-5
        num_steps = int(dt / TIMESTEP)

        for _ in range(num_steps):
            for particle in self.particles:
                # Calculates direction
                norm = (particle.x ** 2 + particle.y ** 2) ** 0.5
                v_x, v_y = -particle.y / norm, particle.x / norm

                # Calculates displacement
                dx = TIMESTEP * particle.angular_velocity * v_x
                dy = TIMESTEP * particle.angular_velocity * v_y

                particle.x += dx
                particle.y += dy

def visualize(simulator):
    """
    Global function to visualize particle simulations across given time intervals. 

    PARAMS:     {simulator}: Instantiated ParticleSimulator object containing data for particles. 
    RETURN:     N/A
    """

    X = [particle.x for particle in simulator.particles]
    Y = [particle.y for particle in simulator.particles]

    fig = plt.figure()
    ax = plt.subplot(111, aspect="equal")
    line, = ax.plot(X, Y, "ro")

    # Axial limits
    plt.xlim(-1, 1)
    plt.ylim(-1, 1)

    def _init():
        """
        Custom initializer closure for visualizer function.

        PARAMS:     N/A
        RETURN:     {line}, : Single subplot object. 
        """
        line.set_data([], [])
        return line, 

    def _animate(foo):
        """
        Helper closure for animating particle simulator using MatPlotLib's PyPlot library. 

        PARAMS:     N/A
        RETURN:     {line}, : Single subplot object with updated particle data.
        """
        simulator.evolve(0.01)
        X = [particle.x for particle in simulator.particles]
        Y = [particle.y for particle in simulator.particles]

        line.set_data(X, Y)
        return line,

    anim = animation.FuncAnimation(fig, _animate, init_func=_init, blit=True, interval=10)
    plt.show()

def test_visualize():
    """
    Global function to test particle visualization for profiling/benchmarking. 

    PARAMS:     N/A
    RETURN:     N/A
    """
    # Instantiate three particles for testing
    particles = [Particle(0.3, 0.5, 1), 
                 Particle(0.0, -0.5, -1), 
                 Particle(-0.1, -0.4, 3)]
    simulator = ParticleSimulator(particles)
    visualize(simulator)

def test_evolve():
    """
    ...

    PARAMS:     ...
    RETURN:     ...
    """
    particles = [Particle(0.3, 0.5, 1), 
                 Particle(0.0, -0.5, -1), 
                 Particle(-0.1, -0.4, 3)]
    simulator = ParticleSimulator(particles)
    simulator.evolve(0.1)
    p0, p1, p2 = particles

    def fequal(pos_act, pos_exp, eps=1e-5):
        """
        Test closure to check accuracy in particle evolution. 

        PARAMS:     ...
        RETURN:     ...
        """
        return abs(pos_act - pos_exp) < eps

    # Test cases for first particle
    assert fequal(p0.x, 0.210269)
    assert fequal(p0.y, 0.543863)

    # Test cases for second particle
    assert fequal(p1.x, -0.099334)
    assert fequal(p1.y, -0.490034)
 
    # Test cases for third particle
    assert fequal(p2.x, 0.191358)
    assert fequal(p2.y, -0.365227)

if __name__ == "__main__":
    # test_visualize()            # Test visualizer for particle simulation and basic benchmarking
    test_evolve()               # Test function for particle evolution accuracy