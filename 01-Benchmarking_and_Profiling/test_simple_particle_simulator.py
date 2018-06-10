#!python3

from simple_particle_simulator import Particle, ParticleSimulator

def test_evolve(benchmark):
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

    benchmark(simulator.evolve, 0.1)