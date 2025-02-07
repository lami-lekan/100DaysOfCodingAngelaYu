student_score = [24, 77, 29, 53, 33, 78, 76, 20, 15, 58, 94, 39, 93, 4, 62, 65, 1, 7, 200, 26, 52, 100]
max = 0
for score in student_score:
    if score > max:
        max = score

print(max)

sum = 0
for i in range(1, 101):
    sum += i
print(sum)

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        number = "FizzBuzz"
    if number % 5 == 0:
        number = "Buzz"
    if number % 3 == 0:
        number = "Fizz"
    print(number)