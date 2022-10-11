def minimal (v1,v2,v3,v4):
    min_value= v1
    if v2< min_value:
        min_value= v2
    if v3< min_value:
        min_value=v3
    if v4< min_value:
        min_value=v4
    return min_value
print(minimal(7,29,15,33))