


def alg_A(xs):
    return len(set(xs)) < len(xs)

# best case = worst case


def alg_B(xs):
    for i in range(len(xs)):
        if xs[i] in xs[i+1:]:
            return True

# best case: [0,0,....]     meteen duplicaat
# worst case: [1,2,3,...]   geen duplicaten

def alg_C(xs):
    seen = set()

    for x in xs:
        if x in seen:
            return True
        seen.add(x)
    return False

# best case: [0,0,....]     meteen duplicaat
# worst case: [1,2,3,...]   geen duplicaten

import time
import simpleplot

measurements_A = []
measurements_B = []
measurements_C = []
for N in range(0,1000,20):
    xs = list(range(N))

    start = time.perf_counter()
    alg_A(xs)
    end = time.perf_counter()
    measurements_A.append((N,end-start))

    start = time.perf_counter()
    alg_B(xs)
    end = time.perf_counter()
    measurements_B.append((N,end-start))

    start = time.perf_counter()
    alg_C(xs)
    end = time.perf_counter()
    measurements_C.append((N,end-start))

simpleplot.add_line(measurements_A,'alg A')
#simpleplot.add_line(measurements_B,'alg B')
simpleplot.add_line(measurements_C,'alg C')
simpleplot.show_plot()

#=> algoritme A is het snelste behalve als de kans op duplicaten groot is (kies dan C)