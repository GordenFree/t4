def apply_discount(product, discount):
    price = int(product['цена'] * (1.0 - discount))
    assert 0 <= price <= product['цена']
    return price

shoes = {'имя': 'модные туфли', 'цена': 15690}

print (apply_discount (shoes, 1))

with open('hello.txt', 'w') as f:
    f.write('привет мир')
