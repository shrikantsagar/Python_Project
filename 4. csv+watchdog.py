import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
import csv
import pandas as pds

csv_file_list = ['raw/file1.csv', 'raw/file2.csv', 'raw/file3.csv']
for csv_file in csv_file_list:
    if csv_file == 'raw/file1.csv':
        read_csv_file = pds.read_csv(csv_file, index_col = False)
        column = False
        read_csv_file = read_csv_file.drop(column, axis =0)
        read_csv_file.to_csv('processed/2017-10-01-processed.csv', mode='a', index = False)
        read_csv_file.columns = ["Date"]

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%Y-%M-%D %H:%M:%S')
    observer = Observer()
    observer.schedule(LoggingEventHandler(), path = './', recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(0)
    except:
        observer.stop()
        observer.join()

