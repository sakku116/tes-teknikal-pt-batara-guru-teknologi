def main():
    n = list('368546748')
    output = ''
    index = 0

    for i in n:
        angka_sekarang = n[index]

        output += i
        if index+1 == len(n):
            break

        if int(angka_sekarang) % 2 == 0:
            angka_setelahnya = n[index+1]

            if int(angka_setelahnya) % 2 == 0: 
                output += '-'

        index += 1

    print(output) 

main()