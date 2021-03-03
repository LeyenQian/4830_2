import os, random, string
from pymd5 import md5
from multiprocessing import Process

def generate_hash(i: int):

    while(True):
        key: str = ''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for i in range(random.randint(7, 10)))
        md5_str: str = str(md5(key).digest(), 'utf-8', errors='ignore')

        if "'or'" in md5_str or "'Or'" in md5_str or  "'oR'" in md5_str or \
           "'OR'" in md5_str or "'||'" in md5_str or "'='" in md5_str:
            with open(str(i) + '.txt', 'a', encoding='utf-8') as ofs:
                ofs.write("key: " + key + '\n')
                ofs.write("raw: " + md5_str + '\n\n')

if __name__ == "__main__":
    process_handle: list = list()

    for i in range(10):
        t = Process(target=generate_hash, args=(i, ))
        process_handle.append(t)
        t.start()

    for t in process_handle:
        t.join()