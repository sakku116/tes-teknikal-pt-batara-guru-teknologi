import datetime

'''
waktu awal = 08 : 52 : 45
waktu 5000 detik kemudian....
pada jam berapa?
'''

def main():
    waktu_awal = datetime.datetime.strptime(str(datetime.time(8, 52, 45)), '%H:%M:%S')
    print(waktu_awal + datetime.timedelta(seconds = 5000))

main()