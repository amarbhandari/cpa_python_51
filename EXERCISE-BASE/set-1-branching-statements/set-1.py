print("Question 1:")
print("Hello World")
print("Python is fun!")

print("----------------------------------")
print("Question 2:")
x = 5
y = 3
print("x + y = ", x + y)


print("----------------------------------")
print("Question 3:")
name = "Alice"
age = 25
print("Name:", name)
print("Age:", age)

print("----------------------------------")
print("Question 4:")
a = 10
b = 4
print("a - b = ", a - b)
print("a + b = ", a + b)

print("----------------------------------")
print("Question 5:")
score = 85
if score > 80:
    print("Good Job!")


print("----------------------------------")
print("Question 6:")
temperature = 15
if temperature > 20:
    print("Warm Day")
else:
    print("Cool Day")

print("----------------------------------")
print("Question 7:")
x - 7
y = 7
print("x == y", x == y, x, y)
print("x != y", x != y, x, y)

print("----------------------------------")
print("Question 8:")
num = 12
print("num / 3 = ", num/3)
print("num // 3 = ", num // 3)

print("----------------------------------")
print("Question 9:")
value = 50
if value >= 50:
    print("Pass")

print("----------------------------------")
print("Question 10:")
a = "Hello"
b = "World"
print(f"a = {a}, b = {b}")
print(a + " " + b)

print("----------------------------------")
print("Question 11:")
x = 8
y = 3
print(x ** y)
print(x % y)

print("----------------------------------")
print("Question 12:")
age = 17
if age >= 18:
    print(age, "Adult")
else:
    print(age, "Minor")
print("Processing Complete")

print("----------------------------------")
print("Question 13:")
a = 5
b = 10
c = a + b * 2
print(f"a : {a}, b: {b}, c: {c}")
print(a < b and b < 20)


print("----------------------------------")
print("Question 14:")
score = 75
if score >= 90:
    print("A grade, score = ", score)
elif score >= 80:
    print("B grade, score = ", score)
elif score >= 70:
    print("C grade, score = ", score)
else:
    print("Need improvement")

print("----------------------------------")
print("Question 15:")
x = 12
y = 5
result = x > y or y > 10
print(result)
print(not result)

print("----------------------------------")
print("Question 16:")
num1 = 15
num2 = 20
if num1 > 10 and num2 > 10:
    sum_result = num1 + num2
    print("Sum is: ", sum_result)


print("----------------------------------")
print("Question 17:")
value = 0
if value:
    print("True")
else:
    print("False")
print(value == False)

print("----------------------------------")
print("Question 18:")
a = 6
b = 4
c = 2
result = a + b * c - 4
print(result)
print(result > a + b)

print("----------------------------------")
print("Question 19:")
temperature = 22
humidity = 60
if temperature > 20 and humidity < 70:
    print("Comfortable weather")
elif temperature > 20:
    print("Warm but humid")
else:
    print("Cool Weather")

print("----------------------------------")
print("Question 20:")
x = 3
y = 7
z = x * 2 + y // 2
print(z)
if z > 8:
    print("Greater than 8")
    z = z - 5
    print("New Value: ", z)

print("----------------------------------")
print("Question 21:")
a = 4
b = 6
c = 8
if a + b > c and a + c > b and b + c > a:
    print("Valid Triangle")
else:
    print("Invalid Triangle")
print("Sum of all sides:" , a +  b + c)

print("----------------------------------")
print("Question 22:")
x = 2
y = 3
z = 4
result = x ** y + z * (x+y) -z // x
print(result)
if result % 2 == 0:
    print("Even")
else:
    print("Odd")

print("----------------------------------")
print("Question 23:")
age = 25
income = 30000
if age > 21 and income >= 25000:
    if age < 30:
        print("Young professional")
    else:
        print("Experienced professional")
elif age >= 21:
    print("Young Adult")
else:
    print("Student")

print("----------------------------------")
print("Question 24:")
p = True
q = False
r = True
result1 = p and q or r
result2 = p and (q or r)
print(result1)
print(result2)
print(result1 == result2)

print("----------------------------------")
print("Question 25:")
num = 127
if num > 100:
    if num % 2 == 1:
        if num % 3 == 1:
            print("Special number")
        else:
            print("Odd but not special")
    else:
        print("Even and large")
else:
    print("Small number")

print("----------------------------------")
print("Question 26:")
a = 5
b = 0
c = 10
if a and b and c:
    print("All True")
elif a and c:
    print("A and C are true")
elif a or b or c:
    print("At least one is true")
else:
    print("All False")

print("----------------------------------")
print("Question 27:")
x = 3
y = 5
z = 2
max_val = x
if y > max_val:
    max_val = y
if z > max_val:
    max_val = z
print("Maximum value:", max_val)
print("Is it greater than average?", max_val > (x + y +z) / 3)

print("----------------------------------")
print("Question 28:")
score1 = 85
score2 = 92
score3 = 78
average = (score1 + score2 + score3) / 3
print("Average:", average)
if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
else:
    grade = "F"
print("Grade: ", grade)
print("Pass" if grade != 'F' else "Fail")

print("----------------------------------")
print("Question 29:")
year = 2024
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap Year")
        else:
            print("Not a leap year")
    else:
        print("Leap Year")
else:
    print("Not a leap year")
print("Year processed:", year)