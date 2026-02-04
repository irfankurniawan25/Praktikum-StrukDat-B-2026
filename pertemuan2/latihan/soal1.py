angka = [10, 20, 30, 40, 50]

print(angka, 'sebelum perubahan') #sebelum perubahan

angka.append(60)
angka.remove(20)
tertinggi = max(angka)
terendah = min(angka)

print(f'angka tertinggi = {tertinggi}')
print(f'angka terendah = {terendah}')

total = 0

for x in angka:
    total += x
    
rata_rata = total / len(angka) 

print('rata rata setelah perubahan= ', rata_rata)
print(angka, 'setelah perubahan') # setelah perubahan