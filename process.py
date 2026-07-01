from multiprocessing import Process
import time

def work(name):
    print(f"work {name} started")
    time.sleep(3)
    print(f"work {name} completed")
    
threads = []
if __name__ == "__main__":
    start =  time.time()
    for i in range(0,5):
        p_name = f"process{i}"
        t = Process(target=work, args=(p_name,))
        threads.append(t)
        t.start()
        
    for t in threads:
        t.join()
    end =  time.time()    
    print(f"process completed with {end-start:2f} sec")