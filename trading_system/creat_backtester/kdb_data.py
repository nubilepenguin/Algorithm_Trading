from pyq import q
from datetime import date

#googdata:([]dt:();high:();low:();open:();close:();volume:(),adj_close:())

q.insert('googdata', (date(2014,1,2), 555.263550, 550.549194, 554.125916, 552.963501, 3666400.0, 552.963501))
q.insert('googdata', (date(2014,1,3), 554.856201, 548.894958, 553.897461, 548.929749, 3355000.0, 548.929749))

q.googdata.show()


# f:{[s]select from googdata where date=d}

x=q.f('2014-01-02')
print(x.show())