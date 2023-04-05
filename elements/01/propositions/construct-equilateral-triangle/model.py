"""
Euclid's first proposition in book I

construct an equilateral triangle on a segment


"""
from geometor import *

FIG_W = 10
FIG_H = 11

plt.rcParams['figure.figsize'] = [FIG_W, FIG_H]

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
    A = M.set_point(0, 0, classes=['start'], label='A')
    B = M.set_point(1, 0, classes=['start'], label='B')

    C, D = construct_equilateral_poles(M, A, B)

    M.labels[C] = 'C'
    M.labels[D] = 'D'

    t_1 = M.set_polygon([A, B, C])
    M.labels[t_1] = 't_1'
    demonstrate_equilateral(M, t_1)
    
    t_2 = M.set_polygon([A, B, D])
    M.labels[t_2] = 't_2'
    demonstrate_equilateral(M, t_2)

    M.summary()

    fig, (ax, ax_btm) = plt.subplots(2, 1, gridspec_kw={'height_ratios': [10, 1]})
    fig.set_facecolor('#111111')
    ax.axis(False)
    #  ax.grid(color='r')
    #  ax.spines['left'].set_color('k')
    #  ax.spines['right'].set_color('k')
    #  ax.spines['top'].set_color('k')
    #  ax.spines['bottom'].set_color('k')
    #  ax.tick_params(color='#999999', labelcolor='#999999', grid_color='#999999')
    ax.set_aspect('equal')
    ax.invert_yaxis()
    #  ax.set_xticks([-1, 0, 1], labels=[r'$-1$', '$0$', '$1$'])
    #  ax.set_xticks([0.5], labels=[r'$\frac{1}{2}$'], minor=True)
    plt.tight_layout()

    plot_model(NAME, ax, ax_btm, M)

    plt.show()
