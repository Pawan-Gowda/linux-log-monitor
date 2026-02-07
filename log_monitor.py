import time

LOG_FILE = "/var/log/auth.log"
KEYWORD = "Failed password"

def monitor_logs():
    with open(LOG_FILE,"r")as file:
        file.seek(0,2)

        while True:
            line = file.readline()
            if not line:
                time.sleep(1)
                continue

            if KEYWORD in line:
                print("Alert: Failed login detected!")
                print(line)

if __name__=="__main__":
  monitor_logs()
