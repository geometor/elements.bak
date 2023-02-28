"""
Euclid 1.2

construct equal segments by extension


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

    c_1 = M.construct_circle(pt_1, pt_2, classes=['guide'])
    c_2 = M.construct_circle(pt_2, pt_1, classes=['guide'])

    pts = c_1.intersection(c_2)

    parents = {c_1:'', c_2:''}
    for pt in pts:
        M.add_point(pt, parents=parents) 

    return M.points()[-2:]


if __name__ == '__main__':

    NAME = 'construct equilateral triangle'

    M = Model()
    A = M.set_point(0, 0, classes=['start'], label='A')
    B = M.set_point(1, 0, classes=['start'], label='B')

    M.set_segment(A, B)
    
    C = M.set_point(sp.Rational(1, 2), 1, classes=['start'], label='C')
    D = M.set_point(1, 1, classes=['start'], label='D')

    M.set_segment(C, D)
    
    E, _ = construct_equilateral_poles(M, A, C)
    M.labels[E] = 'E'

    M.construct_line(E, A)
    M.construct_circle(A, B)

    F = M.points()[-1]
    M.labels[F] = 'F'

    M.construct_circle(E, F)

    M.construct_line(E, C)
    G = M.points()[-1]
    M.labels[G] = 'G'

    M.construct_circle(C, G)
    M.construct_line(C, D)

    H = M.points()[-1]
    M.labels[H] = 'H'

    M.set_segment(C, H)


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
