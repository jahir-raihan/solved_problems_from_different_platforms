n = int(input())

odd_numbers = ((n//2) + (n % 2))**2
even_numbers = (n//2)*((n//2) + 1)

print(even_numbers - odd_numbers)