import time
from influxdb import InfluxDBClient

client = InfluxDBClient("host", "8086", "user", "password", "db")
client.create_database("db")

def send_influx_(call,req_time):
        print(req_time)
        print("done")
        try:
            json_body = [ { "measurement": "nginx_logs","tags": {"host": "","api": call}, "fields": {"request_time" : float(req_time)}} ]
            client.write_points(json_body)
        except:
            print("ERROR")


def follow(thefile):
    thefile.seek(0,0)
    while True:
        line = thefile.readline()
        if not line:
            continue
        logs = line.split(" ")
        print(logs)
#        print(logs[-3])
        if len(logs) >= 14:
           print(logs[-3])
           if "" in line: #any call 
                 send_influx_("collaborations",logs[-3])
                 continue
           elif "items?" in line:
                 send_influx_("items",logs[-3])


if __name__ == '__main__':
    logfile = open("nginx.log","r")
    follow(logfile)
