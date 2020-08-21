import setting as s
import os.path as op
import os as o

path_main = 'files/main.txt'
path_record = 'files/records.txt'
main_stak = []
record_stak = []


def record_load():
    f = open(path_record)
    for li in f:
        record_stak.append(li)
    for i in range(10):
        s.HONOR_STAK[i] = int(record_stak[i])
    f.close()

def record_save():
    record_stak = s.HONOR_STAK
    f = open(path_record, 'w')
    for li in record_stak[:10]:
        f.write(str(li) + '\n')
    f.close()

def start():
    f = open(path_main)
    for li in f:
        main_stak.append(li)
    s.GOLD = int(main_stak[0])
    s.HONOR = int(main_stak[1])
    s.BULLET_COUNT = int(main_stak[2])
    s.BULLET_SPEED = int(main_stak[3])
    s.BULLET_SIZE = int(main_stak[4])
    s.ROTATE_BUST = int(main_stak[5])
    s.RELOAD_BUST = int(main_stak[6])
    s.GOLD_BUST = int(main_stak[7])
    s.SPEED_BUST = int(main_stak[8])
    s.AMPLITUDE_BUST = float(main_stak[9])
    f.close()

def finish():
    main_stak[0] = s.GOLD
    main_stak[1] = s.HONOR
    main_stak[2] = s.BULLET_COUNT
    main_stak[3] = s.BULLET_SPEED
    main_stak[4] = s.BULLET_SIZE
    main_stak[5] = s.ROTATE_BUST
    main_stak[6] = s.RELOAD_BUST
    main_stak[7] = s.GOLD_BUST
    main_stak[8] = s.SPEED_BUST
    main_stak[9] = s.AMPLITUDE_BUST

    f = open(path_main, 'w')
    for li in main_stak[:10]:
        f.write(str(li) + '\n')
    f.close()

def tank_load():
    f = open(s.BASE_PATH)
    for li in f:
        s.TANK.append(li)
    f.close()



def check_path():
    if not op.isdir('files'):
        print("file allert !")
        o.mkdir('files')
    if not op.exists(path_main):
        print("main allert !")
        f = open(path_main, 'w')
        finish()
    if not op.exists(path_main):
        print("record allert !")
        f = open(path_record, 'w')
        record_save()
