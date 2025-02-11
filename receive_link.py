#!/usr/bin/env python3

from probe_hdrs import *


def expand(x):
    yield x
    while x.payload:
        x = x.payload
        yield x

def handle_pkt(pkt):
    if ProbeData in pkt:
        data_layers = [l for l in expand(pkt) if l.name=='ProbeData']
        print("")
        for sw in data_layers:
            utilization = 0 if sw.cur_time == sw.last_time else 8.0*sw.byte_cnt/(sw.cur_time - sw.last_time)
            print("Switch {} - Port {}: {} Mbps".format(sw.swid, sw.port, utilization))
            f = open('h1.txt', 'a+')
            # 1;1;0.0009833938813989156 
            # 2;2;0.0008466832412470812 1
            # 3;3;0.0007099945900678177 3
            # 1;3;0.0005739211368169466 2
            # 3;2;0.00043732781395471585 2
            # 2;3;0.00030147837457934344 3
            # 1;2;0.00016581654283813856 1
            
            f.write("{}\n".format(utilization))
            f.close()
        

def main():
    iface = 'eth0'
    print("sniffing on {}".format(iface))
    sniff(iface = iface,
          prn = lambda x: handle_pkt(x))

if __name__ == '__main__':
    main()
