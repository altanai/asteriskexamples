# Asterisk Queues

Reloading changes made in queue.conf or queuerules.conf
```commandline
queue reload all 
```

or 
```commandline
 module reload app_queue.so
```

Define queue for sales and support in queue.conf
- static member can be added from queue.conf members 
- dynamic member can be added via cli using queue add members
- Users can add themselves or remove themselves form queue using AddQueueMember or RemoveQueueMemeber from extension dialplan 

check the status 
```commandline
*CLI>  queue show
support has 0 calls (max unlimited) in 'rrmemory' strategy (0s holdtime, 0s talktime), W:0, C:0, A:0, SL:0.0%, SL2:0.0% within 0s
   No Members
   No Callers

sales has 0 calls (max unlimited) in 'rrmemory' strategy (0s holdtime, 0s talktime), W:0, C:0, A:0, SL:0.0%, SL2:0.0% within 0s
   No Members
   No Callers
```

Queue log 
```commandline
> tail /var/log/asterisk/queue_log 
1596191926|NONE|NONE|NONE|QUEUESTART|
1596191978|NONE|NONE|NONE|QUEUESTART|
1596257260|NONE|NONE|NONE|QUEUESTART|
1596264295|NONE|NONE|NONE|QUEUESTART|
1596272294|NONE|NONE|NONE|QUEUESTART|
1596510480|CLI|sales|SIP/0004f2040001|ADDMEMBER|
1596512941|1596512941.163|support|NONE|ENTERQUEUE||7000|1
1596513009|1596512941.163|support|NONE|ABANDON|1|1|68
1596513054|1596513054.164|sales|NONE|ENTERQUEUE||7000|1
1596513628|NONE|NONE|NONE|QUEUESTART|

```