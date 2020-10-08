
# DO NOT EDIT

# Assignment for 18yz184

from lib204 import wff
P, Q, R, S, T = map(wff.Variable, 'PQRST')
s1 = (T|(S|Q))
s2 = ((S|Q)&(~S|Q))
s3 = ((Q|~T)&(Q|T))
s4 = (~T|(~Q|~S))

s5 = (~(~T|Q)|(~T>>(S&~Q)))
s6 = ((Q>>T)>>((T&~Q)|S))
