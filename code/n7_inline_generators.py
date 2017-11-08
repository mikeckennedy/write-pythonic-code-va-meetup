import collections
import uuid

Measurement = collections.namedtuple('Measurement', 'id x y value')

measurements = [
    Measurement(str(uuid.uuid4()), 1, 1, 72),
    Measurement(str(uuid.uuid4()), 2, 1, 40),
    Measurement(str(uuid.uuid4()), 3, 1, 11),
    Measurement(str(uuid.uuid4()), 2, 1, 90),
    Measurement(str(uuid.uuid4()), 2, 2, 60),
    Measurement(str(uuid.uuid4()), 2, 3, 73),
    Measurement(str(uuid.uuid4()), 3, 1, 40),
    Measurement(str(uuid.uuid4()), 3, 2, 90),
    Measurement(str(uuid.uuid4()), 3, 3, 90)
]

# C-style (loops)
high_measurements1 = []

# list of high values via comprehension
high_measurements2 = []

# via generator expression
# high_m_gen = ()
# print(high_m_gen)

# process the generator to get something printable.
high_measurements3 = list(high_m_gen)

# high values lookup dict via comp
high_m_by_id = {}

# high values distinct via set
high_values_distinct = {}

print(high_measurements1)
print(high_measurements2)
print(high_measurements3)
print(high_m_by_id)
print(high_values_distinct)
