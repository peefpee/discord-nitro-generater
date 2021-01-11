import random, string
print ('please subscribe bear bear team')
print ('https://www.youtube.com/channel/UCBnyGCWTYyeI9ebOvQzKdKw')
codes = int(input('Amount of nitro codes to generate: '))
value = 1
while value <= codes:
    code = "https://discord.gift/" + ('').join(random.choices(string.ascii_letters + string.digits, k=16))
    f = open('Codes  .txt', "a+")
    f.write(f'{code}\n')
    f.close()
    print(f'[GENERATED] {code}')
    value += 1
print ('finished generating codes  ')