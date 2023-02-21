"""
Euclid's first proposition in book I

construct an equilateral triangle on a segment


"""
from geometor import *

def construct_equilateral_poles(M, pt_1, pt_2):
    """\
    From two points, return the equistant points on either side

    :M: the model
    :pt_1: first point of the segment
    :pt_2: second point of the segment
    :returns: list of two pole points

    """
    M.construct_circle(pt_1, pt_2)
    M.construct_circle(pt_2, pt_1)

    return M.points()[-2:]

def demonstrate_equilateral(M, polygon):
    """TODO: Docstring for demonstrate_equilateral.
    :returns: TODO

    """
    pass


if __name__ == '__main__':

    NAME = 'construct equilateral triangle'

    M = Model()
    # TODO: add label to Models
    A = M.set_point(0, 0, classes=['start'])
    B = M.set_point(1, 0, classes=['start'])

    C, D = construct_equilateral_poles(M, A, B)

    t1 = M.set_polygon([A, B, C])
    demonstrate_equilateral(M, t1)
    
    t2 = M.set_polygon([A, B, D])
    demonstrate_equilateral(M, t2)

    print(M)
    M.summary()


    # PLOT *********************************
    #  print_log(f'\nPLOT: {NAME}')

    fig, (ax, ax_btm) = plt.subplots(2, 1, gridspec_kw={'height_ratios': [10, 1]})
    plt.tight_layout()

    plot_model(NAME, ax, ax_btm, M)

