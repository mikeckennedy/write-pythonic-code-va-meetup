# HTTP POST
# /store/order/1?source=ad
# { name: 'michael', cc: 293838383}
#

route = {'id': 1, 'action': 'order'}
query = {'source': 'ad'}
post = {'name': 'michael', 'cc': 293838383, 'id': 7}

merged = {}

# least pythonic (loops)
for k, v in query.items():
    merged[k] = v
for k, v in post.items():
    merged[k] = v
for k, v in route.items():
    merged[k] = v
print(merged)

# pythonic (update)
merged = {}
merged.update(query)
merged.update(post)
merged.update(route)
print(merged)

# def fun(**kwargs):
#     print(kwargs)
#
# fun(name="Michael",id=7)

# 3.5+ syntax:
merged = {**query, **post, **route}
print(merged)
