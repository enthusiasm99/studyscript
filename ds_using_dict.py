# "ab"是地址（Address）簿（BOOK）的缩写

ab = {
    'Swaroop': 'Swaroop@swaroopch.com',
    'Larry': 'larry@wall.org',
    'Matsumoto': 'mztz@ruby-lang.org',
    'Spammer': 'spammer@hotmail.com'
}

print("Swaroop's address is", ab['Swaroop'])

# 删除一对键值-值配对
del ab['Spammer']
print('\nThere are {} contacts in the address-book\n'.format(len(ab)))

for name, address in ab.items():
    print('Contace {} at {}'.format(name, address))

# 增加一对键值-值配对
ab['Guido'] = 'guido@python.ort'

if  'Guido' in ab:
    print("\nGuido's address is", ab['Guido'])