# Conversão de tipos, coerção
# type convertion, typecasting, coercion
# é o ato de converter um tipo em outro
# tipos imutáveis e primitivos:
# str, int, float, bool

print(1 + 1) # int
print('a' + 'b') # str

# print('1' + 1) # Error
print('1', type('1'))
print(int('1'), type(int('1')))
print(int('1') + 1) ### resolve

print(type(float('1') + 1))
print(bool(1), bool(0), bool(''), bool(' '))