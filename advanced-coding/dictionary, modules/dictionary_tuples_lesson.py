# expenses = [1200, 1400, 1700]
# tuples are immutable
def find_pe_pb(price, eps, book_value):
    pe = price / eps
    pb = price / book_value
    return pe, pb


pe_ratio, pb_ratio = find_pe_pb(100, 2, 4)
print(pe_ratio)
print(pb_ratio)


contacts = [('rachel', 77123456789), ('monica', 77198345986), ('joey', 77178153445)]
for contact in contacts:
    if contact[0] == 'joey':
        print(contact[1])

d = {
    'rachel' : 77123456789,
    'monica' : 77198345986,
    'joey' : 77178153445
}
print(d)
print(d['joey'])
print(d.get('mohan', 0))

d['rachel'] = 11200033444

print(d['rachel'])
d['satya'] = 22399867454
print(d)
del d['satya']
print(d)

var = 'abdul' in d
print(var)
var1 = 'rachel' in d
print(var1)

d1 = {
    'rachel': {'phone' : 1234, 'address' : '1 blue st.'},
    'joey': {'phone' : 4657, 'address' : '7 newton blvd.'}
}
print(d1['rachel']['phone'])

for name in d:
    print(name)
    print(d[name])

for name, number in d.items():
    print(name, number)
