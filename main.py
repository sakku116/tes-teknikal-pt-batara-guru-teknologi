import datetime

def main():
    waktu_awal = datetime.datetime.strptime(str(datetime.time(8, 52, 45)), '%H:%M:%S')

    #print(type(datetime.datetime.strptime(str(waktu_awal), '%H:%M:%S')))
    
    print(waktu_awal + datetime.timedelta(seconds = 5000))

main()