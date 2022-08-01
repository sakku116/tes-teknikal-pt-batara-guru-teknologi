


'''
menggant angka menurut pola tertentu dengan karakter '*'
'''




n = 20

result = ''

pattern1 = 2
pattern2 = 3

index_change = pattern1

state = '1'

temp = []
for i in range(1, n+1):

    if i == index_change:
        result += '*'

        if state == 1:
            state = 2
            index_change = index_change + pattern1
        else:
            state = 1
            index_change = index_change + pattern2

    else:
        result += str(i)

    result += ' '

print(result)