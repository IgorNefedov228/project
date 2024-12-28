from question import *


if q4 == 'm':
    day0 = 88.36 + (13.4 * q4) + (4.8 * q5) - (5.7 * q2)
else:
    day0 = 447.6 + (9.2 * q4) + (3.1 * q5) - (4.3 * q2)


if q6 == 'low':
    day0 *= 1.2
elif q6 == 'low-mid':
    day0 *= 1.35
elif q6 == 'mid':
    day0 *= 1.5
elif q6 == 'mid-high':
    day0 *= 1.65
else:
    day0 *= 1.8    


if q1 == 'gain':
    f_kkal = day0 * 1.2
else:
    f_kkal = day0 * 0.8            #кол-во которое надо набрать

if q1 == 'gain' or 'dry':
    bel = q4 * 2
else:
    None