class Divisible:

    def by_seven(self,n):
        for number in range(n+1):
            if number%7==0:yield number

divisible=Divisible()
generator=divisible.by_seven(int(input("Please input a number.--->")))
for number in generator:
    print(number)

