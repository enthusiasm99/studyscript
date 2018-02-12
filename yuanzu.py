def get_error_details():
    return (2, 'details')

errum, errstr = get_error_details()

print(errum)
print(errstr)

a = 5
b = 8
print(a, b)

a,b  = b,a
print(a, b)
