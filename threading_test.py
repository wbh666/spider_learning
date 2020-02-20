from multiprocessing import Process

ls = [1, 3, 4, 5, 6, 8, 6, 9]


def change():
    print("change0   ls:{}   id(ls)={} ".format(ls, id(ls)))
    ls[1] += 3
    print("change1   ls:{}   id(ls)={} ".format(ls, id(ls)))


def read():
    print("read   ls:{}   id(ls)={} ".format(ls, id(ls)))


if __name__ == "__main__":
    ls[1] += 10
    t0 = Process(target=change)
    t1 = Process(target=read)

    print("main0  ls:{}    id(ls)={}".format(ls, id(ls)))
    t0.start()
    ls[1] += 5
    print("main1   ls:{}   id(ls)={} ".format(ls, id(ls)))
    t1.start()

    t0.join()
    t1.join()

    print("main thread is over")

