import threading
import time

def download(filename):
    print(f"stated download of {filename}")
    time.sleep(3)
    print(f"Completed download of {filename}")
    
files = ["a.txt","b.pdf","c.html"]
threads=[]
if __name__== "__main__":
    start_time = time.time()
    for file in files:
        t=threading.Thread(target=download, args=(file,))
        threads.append(t)
        t.start()
        
    for t in threads:
        t.join()
        
    end_time= time.time()
    print(f"process completed: {end_time-start_time:.2f} sec")
    