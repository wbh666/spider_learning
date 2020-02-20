import multiprocessing
import time

def download_data(q):
    data = range(10)
    for i in data:
        q.put(i)
        print("进队{}".format(i))
        time.sleep(1)
    print("全部进队成功")


def get_data(q):
    while True:
        data = q.get()
        print("出队{}".format(data))

        if q.empty():
            time.sleep(1.5)
            if q.empty():
                break
    print("全部出队成功")

if __name__ == "__main__":
    q = multiprocessing.Queue(5)

    t1 = multiprocessing.Process(target=download_data, args=(q,))
    t2 = multiprocessing.Process(target=get_data, args=(q,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("主进程结束")


