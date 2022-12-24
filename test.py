
from wsnHybrid import WsnHybrid

wsn_xmode = "event-driven"
threshold_xtemp = 50
threshold_start = 5
threshold_stop = 4


mode_counter = 0


a = WsnHybrid(wsn_xmode,threshold_xtemp,threshold_start,threshold_stop)
x = a.orchestrator(60,0)
while True:
    x = a.orchestrator(60,x)




