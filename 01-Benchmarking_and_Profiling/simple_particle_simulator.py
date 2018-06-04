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
        TIMESTEP = 0.00001
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

    PARAMS:     
    RETURN:     
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
        """ """
        line.set_data([], [])
        return line, 

    def _animate():
        """ """
        simulator.evolve(0.01)
        X = [particle.x for particle in simulator.particles]
        Y = [particle.y for particle in simulator.particles]

        line.set_data(X, Y)
        return line,

    anim = animation.FuncAnimation(fig, _animate, init_func=_init, blit=True, interval=10)
    plt.show()

def test_visualize():
    pass

if __name__ == "__main__":
    test_visualize()            # Test visualizer for particle simulation and basic benchmarking