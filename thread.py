import threading
import time
def download(filename):
    print(f"Download started for {filename}")
    time.sleep(3)
    print(f"Download completed for {filename}")

def upload(filename):
    print(f"Upload started for {filename}")
    time.sleep(3)
    print(f"Upload completed for {filename}")

def process_file(filename):
    print(f"Processing started for {filename}")
    time.sleep(3)
    print(f"Processing completed for {filename}")   

if __name__ == "__main__":
    t1 = threading.Thread(target=download, args=("file1.txt",))
    t2 = threading.Thread(target=upload, args=("file1.txt",))
    t3 = threading.Thread(target=process_file, args=("file1.txt",)) 
    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()
    print("All threads are completed")  