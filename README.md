# Asterisk 

Asterix open-source telephony Server can be used to build multitude of applications . 

## Installation and setup 
check the asterisk available version  from https://downloads.asterisk.org/pub/telephony/asterisk/
use wget to download 

```commandline
wget https://downloads.asterisk.org/pub/telephony/asterisk/asterisk-17.6.0.tar.gz
tar -xvf asterisk-17.6.0.tar.gz
```

 libpri library allows Asterisk to communicate with ISDN connections.
 
 DAHDI ( Digium Asterisk Hardware Device Interface) library allows Asterisk to communicate with analog and digital telephones and telephone lines / PSTN
 
 dahdi-linux 
 ```commandline
wget https://downloads.asterisk.org/pub/telephony/dahdi-linux/dahdi-linux-current.tar.gz
tar -xvf dahdi-linux-current.tar.gz
```
dadhi-tools
```commandline
wget https://downloads.asterisk.org/pub/telephony/dahdi-tools/dahdi-tools-current.tar.gz 
tar -xvf dahdi-tools-current.tar.gz
``` 
 
Remember you make to make and install DAHDI and libpri before building asterisk 
 ```commandline
make
sudo make install 
make config 
```

## Build asterisk  
 
SIP stack ina Asterisk  
- chan_sip SIP channel driver ( old)
- chan_pjsip

Build with later using 
```commandline
cd asterisk-17.6.0
./configure --with-pjproject-bundled --with-jansson-bundled
```
output
```
config.status: creating makeopts
config.status: creating autoconfig.h
configure: Menuselect build configuration successfully completed

               .$$$$$$$$$$$$$$$=..      
            .$7$7..          .7$$7:.    
          .$$:.                 ,$7.7   
        .$7.     7$$$$           .$$77  
     ..$$.       $$$$$            .$$$7 
    ..7$   .?.   $$$$$   .?.       7$$$.
   $.$.   .$$$7. $$$$7 .7$$$.      .$$$.
 .777.   .$$$$$$77$$$77$$$$$7.      $$$,
 $$$~      .7$$$$$$$$$$$$$7.       .$$$.
.$$7          .7$$$$$$$7:          ?$$$.
$$$          ?7$$$$$$$$$$I        .$$$7 
$$$       .7$$$$$$$$$$$$$$$$      :$$$. 
$$$       $$$$$$7$$$$$$$$$$$$    .$$$.  
$$$        $$$   7$$$7  .$$$    .$$$.   
$$$$             $$$$7         .$$$.    
7$$$7            7$$$$        7$$$      
 $$$$$                        $$$       
  $$$$7.                       $$  (TM)     
   $$$$$$$.           .7$$$$$$  $$      
     $$$$$$$$$$$$7$$$$$$$$$.$$$$$$      
       $$$$$$$$$$$$$$$$.                

configure: Package configured for: 
configure: OS type  : linux-gnu
configure: Host CPU : x86_64
configure: build-cpu:vendor:os: x86_64 : pc : linux-gnu :
configure: host-cpu:vendor:os: x86_64 : pc : linux-gnu :
```
  
USe menu select option on Asterisk to install packages pick and choose application and other options such as music on hold , extra sound packages , PBX modules etc
```commandline
make menuselect
```  
output 
```commandline
 **************************************************
     Asterisk Module and Build Option Selection
 **************************************************

          Press 'h' for help.

      Add-ons (See README-addons.txt)
      Applications
      Bridging Modules
      Call Detail Recording
      Channel Event Logging
      Channel Drivers
      Codec Translators
      Format Interpreters
      Dialplan Functions
      PBX Modules
      Resource Modules
      Test Modules
      Compiler Flags
      Utilities
      AGI Samples
      Core Sound Packages
      Music On Hold File Packages
 ---> Extras Sound Packages
```

Compile asterisk on the system 
```commandline
make
```
outout 
```commandline
Building Documentation For: third-party channels pbx apps codecs formats cdr cel bridges funcs tests main res addons 
 +--------- Asterisk Build Complete ---------+
 + Asterisk has successfully been built, and +
 + can be installed by running:              +
 +                                           +
 +                make install               +
 +-------------------------------------------+

```

Install 
```commandline
sudo make install
```
output
```commandline
done
 +---- Asterisk Installation Complete -------+
 +                                           +
 +    YOU MUST READ THE SECURITY DOCUMENT    +
 +                                           +
 + Asterisk has successfully been installed. +
 + If you would like to install the sample   +
 + configuration files (overwriting any      +
 + existing config files), run:              +
 +                                           +
 + For generic reference documentation:      +
 +    make samples                           +
 +                                           +
 + For a sample basic PBX:                   +
 +    make basic-pbx                         +
 +                                           +
 +                                           +
 +-----------------  or ---------------------+

```

Install samples 
```commandline
sudo make samples 
```

Run Asterisk
```commandline
➜  asterisk-17.6.0 sudo asterisk -c 
Asterisk 17.6.0, Copyright (C) 1999 - 2018, Digium, Inc. and others.
Created by Mark Spencer <markster@digium.com>
...
Asterisk Ready.
*CLI> 
```
ports uses 
````commandline
> ps -ef | grep asterisk

asterisk  28922 altanai    5u  IPv4 3449570      0t0  TCP localhost:38108->localhost:postgresql (CLOSE_WAIT)
asterisk  28922 altanai    9u  IPv4 3451466      0t0  UDP *:40388 
asterisk  28922 altanai   10u  IPv6 3451467      0t0  UDP *:52092 
asterisk  28922 altanai   12u  IPv4 3449574      0t0  UDP *:2727 
asterisk  28922 altanai   14u  IPv4 3449575      0t0  UDP *:iax 
asterisk  28922 altanai   15u  IPv4 3451995      0t0  TCP *:cisco-sccp (LISTEN)
asterisk  28922 altanai   18u  IPv4 3449577      0t0  UDP *:5000 
asterisk  28922 altanai   19u  IPv4 3449578      0t0  UDP *:4520 

````

You can use safe_asterisk to enable auto restart after crash thus minimizing downtime . It also creates core dump file .

One can continue on the sandbox environment to run the modules I describe in this repo . 

## configuration 

Listen address for SIP in sip.conf , Listen on

specific IPv4 address.      Example: bindaddr=192.0.2.1
specific IPv6 address.      Example: bindaddr=2001:db8::1
IPv4 wildcard.              Example: bindaddr=0.0.0.0
IPv4 and IPv6 wildcards.    Example: bindaddr=::

## Modules 

asterisk/modules support teh modular structure of Asterisk

## Applications

such as 
app_dial.sio
app_playback.so
app_voicemail.so

## Resources 

Custom applications such as res_musiconhold.so

## Codecs and Formats 

convert media on disk and channel 

## Cli commands 

Interface with asterisk and issue commands

Other interface for asterisk control are AMI ( Asterisk AManger Interface) and AGI ( Asterisk Gateway Interface ) which operate on APIs like PHP , C++ , Java , Perl

Reload SIP
```commandline
*CLI> pjsip reload
[Jul 31 09:54:58] NOTICE[22399]: sorcery.c:1345 sorcery_object_load: Type 'system' is not reloadable, maintaining previous values
Module 'res_pjsip.so' reloaded successfully.
Module 'res_pjsip_authenticator_digest.so' reloaded successfully.
Module 'res_pjsip_endpoint_identifier_ip.so' reloaded successfully.
Module 'res_pjsip_mwi.so' reloaded successfully.
Module 'res_pjsip_notify.so' reloaded successfully.
Module 'res_pjsip_outbound_publish.so' reloaded successfully.
Module 'res_pjsip_publish_asterisk.so' reloaded successfully.
Module 'res_pjsip_outbound_registration.so' reloaded successfully.
```
Settings show 
```commandline
*CLI> core show settings

PBX Core settings
-----------------
  Version:                     17.6.0
  Build Options:               BUILD_NATIVE, OPTIONAL_API
  Maximum calls:               Not set
  Maximum open file handles:   1024
  Root console verbosity:      0
  Current console verbosity:   0
  Debug level:                 0
  Trace level:                 0
  Maximum load average:        0.000000
  Minimum free memory:         0 MB
  Startup time:                10:33:28
  Last reload time:            10:33:28
  System:                      Linux/4.15.0-62-generic built by root on x86_64 2020-07-30 15:33:43 UTC
  System name:                 
  Entity ID:                   7c:67:a2:eb:ff:a5
  PBX UUID:                    fc3a2e05-e800-47e7-aa27-36ad924f85e0
  Default language:            en
  Language prefix:             Enabled
  User name and group:         /
  Executable includes:         Disabled
  Transcode via SLIN:          Enabled
  Transmit silence during rec: Disabled
  Generic PLC:                 Enabled
  Generic PLC on equal codecs: Disabled
  Hide Msg Chan AMI events:    Disabled
  Min DTMF duration::          80
  Cache media frames:          Enabled
  RTP use dynamic payloads:    1
  RTP dynamic payload types:   35-63,96-127

* Subsystems
  -------------
  Manager (AMI):               Disabled
  Web Manager (AMI/HTTP):      Disabled
  Call data records:           Enabled
  Realtime Architecture (ARA): Disabled

* Directories
  -------------
  Configuration file:          /etc/asterisk/asterisk.conf
  Configuration directory:     /etc/asterisk
  Module directory:            /usr/lib/asterisk/modules
  Spool directory:             /var/spool/asterisk
  Log directory:               /var/log/asterisk
  Run/Sockets directory:       /var/run/asterisk
  PID file:                    /var/run/asterisk/asterisk.pid
  VarLib directory:            /var/lib/asterisk
  Data directory:              /var/lib/asterisk
  ASTDB:                       /var/lib/asterisk/astdb
  IAX2 Keys directory:         /var/lib/asterisk/keys
  AGI Scripts directory:       /var/lib/asterisk/agi-bin

```

channel types 
```commandline
*CLI> core show channeltypes
Type             Description                              Devicestate   Presencestate Indications   Transfer     
-------------    -------------                            ------------- ------------- ------------- -------------
Recorder         Bridge Media Recording Channel Driver    no            no            yes           no           
Announcer        Bridge Media Announcing Channel Driver   no            no            yes           no           
Phone            Standard Linux Telephony API Driver      no            no            yes           no           
Console          OSS Console Channel Driver               no            no            yes           no           
USTM             UNISTIM Channel Driver                   no            no            yes           no           
CBAnn            Conference Bridge Announcing Channel     no            no            yes           no           
CBRec            Conference Bridge Recording Channel      no            no            no            no           
PJSIP            PJSIP Channel Driver                     yes           no            yes           yes          
UnicastRTP       Unicast RTP Media Channel Driver         no            no            no            no           
MulticastRTP     Multicast RTP Paging Channel Driver      no            no            no            no           
Skinny           Skinny Client Control Protocol (Skinny)  yes           no            yes           no           
IAX2             Inter Asterisk eXchange Driver (Ver 2)   yes           no            yes           yes          
MGCP             Media Gateway Control Protocol (MGCP)    yes           no            yes           no           
Local            Local Proxy Channel Driver               yes           no            yes           no           
Surrogate        Surrogate channel used to pull channel f no            no            no            no           
----------
15 channel drivers registered.

```

Set verbosity level ( 0-4)
```commandline
*CLI> core set verbose 1
Console verbose was OFF and is now 1.
```

help
```commandline
*CLI> help pjsip
pjsip dump endpt               -- Dump the res_pjsip endpt internals
pjsip export config_wizard primitives [to] -- Export config wizard primitives
pjsip list aors                -- List PJSIP Aors
pjsip list auths               -- List PJSIP Auths
pjsip list channels            -- List PJSIP Channels
pjsip list ciphers             -- List available OpenSSL cipher names
pjsip list contacts            -- List PJSIP Contacts
pjsip list endpoints           -- List PJSIP Endpoints
pjsip list identifies          -- List PJSIP Identifies
pjsip list registrations       -- List PJSIP Registrations
pjsip list subscriptions {inbound|outbound} [like] -- List active inbound/outbound subscriptions
pjsip list transports          -- List PJSIP Transports
pjsip qualify                  -- Send an OPTIONS request to a PJSIP endpoint
pjsip reload qualify aor       -- Synchronize the PJSIP Aor qualify options
pjsip reload qualify endpoint  -- Synchronize the qualify options for all Aors on the PJSIP endpoint
pjsip reload                   -- <no description available>
pjsip send notify              -- Send a NOTIFY request to a SIP endpoint
pjsip send register            -- Registers an outbound registration target
pjsip send unregister          -- Unregisters outbound registration target
pjsip set history {on|off|clear} -- Enable/Disable PJSIP History
pjsip set logger {on|off|host|add|verbose|pcap} -- Enable/Disable PJSIP Logger Output
pjsip show aors                -- Show PJSIP Aors
pjsip show aor                 -- Show PJSIP Aor
pjsip show auths               -- Show PJSIP Auths
pjsip show auth                -- Show PJSIP Auth
pjsip show channels            -- Show PJSIP Channels
pjsip show channel             -- Show PJSIP Channel
pjsip show channelstats        -- Show PJSIP Channel Stats
pjsip show contacts            -- Show PJSIP Contacts
pjsip show contact             -- Show PJSIP Contact
pjsip show endpoints           -- Show PJSIP Endpoints
pjsip show endpoint            -- Show PJSIP Endpoint
pjsip show history             -- Display PJSIP History
pjsip show identifiers         -- List registered endpoint identifiers
pjsip show identifies          -- Show PJSIP Identifies
pjsip show identify            -- Show PJSIP Identify
pjsip show qualify aor         -- Show the PJSIP Aor current qualify options
pjsip show qualify endpoint    -- Show the current qualify options for all Aors on the PJSIP endpoint
pjsip show registrations       -- Show PJSIP Registrations
pjsip show registration        -- Show PJSIP Registration
pjsip show scheduled_tasks     -- Show all scheduled tasks
pjsip show settings            -- Show global and system configuration options
pjsip show subscription {inbound|outbound} -- Show active subscription details
pjsip show subscriptions {inbound|outbound} [like] -- Show active inbound/outbound subscriptions
pjsip show transports          -- Show PJSIP Transports
pjsip show transport           -- Show PJSIP Transport
pjsip show unidentified_requests -- Show PJSIP Unidentified Requests
pjsip show version             -- Show the version of pjproject in use

```

## Applications 
Custom application that can be built - Call Queue monitoring 

Add a dialplan in extensions 
```
[internal_users]
exten => 6000,1,Answer()
exten => 6000,2,Wait(1)
exten => 6000,2,Wait(1)
exten => 6000,3,Playback(hello-world)
exten => 6000,4,Hangup()
```
Reload and see the dialplan 
```commandline
altanai-Inspiron-15-5578*CLI> dialplan reload
Dialplan reloaded.
altanai-Inspiron-15-5578*CLI> dialplan show 
...
[ Context 'internal_users' created by 'pbx_config' ]
  '6000' =>         1. Answer()                                   [extensions.conf:866]
                    2. Wait(1)                                    [extensions.conf:867]
                    3. Playback(hello-world)                      [extensions.conf:868]
                    4. Hangup()                                   [extensions.conf:869]
```

During Call 
```commandline
*CLI>   == Setting global variable 'SIPDOMAIN' to '192.168.1.114'
  == Spawn extension (internal_users, 6000, 5) exited non-zero on 'PJSIP/7000-00000000'
```

## debugging 

**Issue1** Cannot find sip commands 
```commandline
altanai-Inspiron-15-5578*CLI> sip show peers
No such command 'sip show peers' (type 'core show help sip show' for other possible commands)
```
\
**solution** First check is module is installed 
```commandline
module show like chan_sip.so 
```
When module is installed 
```commandline
altanai-Inspiron-15-5578*CLI> module show like chan_sip.so
Module                         Description                              Use Count  Status      Support Level
chan_sip.so                    Session Initiation Protocol (SIP)        0         
1 modules loaded
```

when modules is not installed 
```commandline
altanai-Inspiron-15-5578*CLI> module show like chan_sip.so
Module                         Description                              Use Count  Status      Support Level
0 modules loaded
```

If module is not loaded Make sure Asterisk is configured to load the module via modules.conf
There may be a case that res_pjsip is loaded inplace of chan_sip
```
; Do not load chan_sip by default, it may conflict with res_pjsip.
noload => chan_sip.so
```
In that case chan_pjsip would be loaded 
```commandline
altanai-Inspiron-15-5578*CLI> module show like chan_pjsip
Module                         Description                              Use Count  Status      Support Level
chan_pjsip.so                  PJSIP Channel Driver                     0          Running              core
1 modules loaded
```
On forcing loading of chan_sip module
```commandline
altanai-Inspiron-15-5578*CLI> module load chan_sip
Loaded chan_sip
SIP channel loading...
[Jul 31 13:25:30] WARNING[815]: chan_sip.c:35477 deprecation_notice: chan_sip has no official maintainer and is deprecated.  Migration to
[Jul 31 13:25:30] WARNING[815]: chan_sip.c:35478 deprecation_notice: chan_pjsip is recommended.  See guides at the Asterisk Wiki:
[Jul 31 13:25:30] WARNING[815]: chan_sip.c:35479 deprecation_notice: https://wiki.asterisk.org/wiki/display/AST/Migrating+from+chan_sip+to+res_pjsip
[Jul 31 13:25:30] WARNING[815]: chan_sip.c:35480 deprecation_notice: https://wiki.asterisk.org/wiki/display/AST/Configuring+res_pjsip

```

**Issue3** Unable to authenticate 
```commandline
*CLI> m[Aug  1 10:07:20] NOTICE[11076]: res_pjsip/pjsip_distributor.c:676 log_failed_request: Request 'REGISTER' from '<sip:phone-1@127.0.0.1>' failed for '127.0.0.1:56039' (callid: OgfL6JO~OO) - No matching endpoint found
[Aug  1 10:07:25] NOTICE[11076]: res_pjsip/pjsip_distributor.c:676 log_failed_request: Request 'INVITE' from '<sip:phone-1@127.0.0.1>' failed for '127.0.0.1:44672' (callid: c62tK1JzlDnDS9VFDGMQfg..) - No matching endpoint found
[Aug  1 10:07:25] NOTICE[11076]: res_pjsip/pjsip_distributor.c:676 log_failed_request: Request 'INVITE' from '<sip:phone-1@127.0.0.1>' failed for '127.0.0.1:44672' (callid: c62tK1JzlDnDS9VFDGMQfg..) - No matching endpoint found
[Aug  1 10:07:25] NOTICE[11076]: res_pjsip/pjsip_distributor.c:676 log_failed_request: Request 'INVITE' from '<sip:phone-1@127.0.0.1>' failed for '127.0.0.1:44672' (callid: c62tK1JzlDnDS9VFDGMQfg..) - Failed to authenticate
```
\
**solution** Define the extension context internal_users
extensions.conf
```
[internal_users]
exten => 6000,1,Answer()
exten => 6000,2,Wait(1)
exten => 6000,3,Playback(hello-world)
exten => 6000,4,Hangup()

```

and edit sip.conf or pjsip.conf and reload 

sip.conf
```
[7000]
    type=friend
    host=dynamic
    context=internal_users
    secret=1234
```

pjsip.conf
```
[7000]
 type=endpoint
 context=internal_users
 disallow=all
 allow=ulaw
 transport=transport-udp
 auth=7000
 aors=7000

[7000]
 type=auth
 auth_type=userpass
 password=1234
 username=7000

[7000]
 type=aor
 max_contacts=1

```
reload 
```commandline
sip reload 
pjsip reload
```

**Issue3** Unable to play hello world via playback
\
**solution** check if application is registered 
If registered 
```commandline
*CLI> core show application playback

  -= Info about application 'Playback' =- 

[Synopsis]
Play a file. 

[Description]
Plays back given filenames (do not put extension of wav/alaw etc). The playback
command answer the channel if no options are specified. If the file is
non-existant it will fail
This application sets the following channel variable upon completion:
${PLAYBACKSTATUS}: The status of the playback attempt as a text string.
    SUCCESS
    FAILED
See Also: Background (application) -- for playing sound files that are
interruptible
WaitExten (application) -- wait for digits from caller, optionally play music
on hold

[Syntax]
Playback(filename[&filename2[&...]][,options])

[Arguments]
options
    Comma separated list of options
    skip: Do not play if not answered

    noanswer: Playback without answering, otherwise the channel will be
    answered before the sound is played.
    NOTE: Not all channel types support playing messages while still on hook.


[See Also]
Background(), WaitExten(), ControlPlayback(), stream file, control stream file,
```

If not registered 
```commandline
altanai-Inspiron-15-5578*CLI> core show application playback
Your application(s) is (are) not registered
```

Alternatively you can even check the list of applications
```commandline
*CLI> core show applications
    -= Registered Asterisk Applications =-
        AddQueueMember: Dynamically adds queue members. 
              ADSIProg: Load Asterisk ADSI Scripts into phone 
                AELSub: Launch subroutine built with AEL 
            AgentLogin: Login an agent. 
          AgentRequest: Request an agent to connect with the channel. 
                   AGI: Executes an AGI compliant application. 
         AlarmReceiver: Provide support for receiving alarm reports from a burglar or fire alarm panel. 
                   AMD: Attempt to detect answering machines. 
                Answer: Answer a channel if ringing. 
      AttendedTransfer: Attended transfer to the extension provided and TRANSFER_CONTEXT 
          Authenticate: Authenticate a user 
            BackGround: Play an audio file while waiting for digits of an extension to go to. 
      BackgroundDetect: Background a file with talk detect. 
         BlindTransfer: Blind transfer channel(s) to the extension and context provided 
                Bridge: Bridge two channels. 
             BridgeAdd: Join a bridge that contains the specified channel. 
            BridgeWait: Put a call into the holding bridge. 
                  Busy: Indicate the Busy condition. 
  CallCompletionCancel: Cancel call completion service 
  CallCompletionRequest: Request call completion service for previous call 
       CELGenUserEvent: Generates a CEL User Defined Event. 
         ChangeMonitor: Change monitoring filename of a channel. 
           ChanIsAvail: Check channel availability 
       ChannelRedirect: Redirects given channel to a dialplan target 
               ChanSpy: Listen to a channel, and optionally whisper into it. 
             ClearHash: Clear the keys from a specified hashname. 
            ConfBridge: Conference bridge application. 
            Congestion: Indicate the Congestion condition. 
         ContinueWhile: Restart a While loop. 
       ControlPlayback: Play a file with fast forward and rewind. 
              DAHDIRAS: Executes DAHDI ISDN RAS application. 
             DAHDIScan: Scan DAHDI channels to monitor calls. 
              DateTime: Says a specified time in a custom format. 
             DBdeltree: Delete a family or keytree from the asterisk database. 
               DeadAGI: Executes AGI on a hungup channel. 
                  Dial: Attempt to connect to another device or endpoint and bridge the call. 
               Dictate: Virtual Dictation Machine. 
             Directory: Provide directory of voicemail extensions. 
                  DISA: Direct Inward System Access. 
              DumpChan: Dump Info About The Calling Channel. 
                  EAGI: Executes an EAGI compliant application. 
                  Echo: Echo media, DTMF back to the calling party 
              EndWhile: End a while loop. 
                  Exec: Executes dialplan application. 
                ExecIf: Executes dialplan application, conditionally. 
            ExecIfTime: Conditional application execution based on the current time. 
             ExitWhile: End a While loop. 
              ExtenSpy: Listen to a channel, and optionally whisper into it. 
           ExternalIVR: Interfaces with an external IVR application. 
              Festival: Say text to the user. 
                 Flash: Flashes a DAHDI Trunk. 
              FollowMe: Find-Me/Follow-Me application. 
               ForkCDR: Forks the current Call Data Record for this channel. 
              GetCPEID: Get ADSI CPE ID. 
                 Gosub: Jump to label, saving return address. 
               GosubIf: Conditionally jump to label, saving return address. 
                  Goto: Jump to a particular priority, extension, or context. 
                GotoIf: Conditional goto. 
            GotoIfTime: Conditional Goto based on the current time. 
                Hangup: Hang up the calling channel. 
      HangupCauseClear: Clears hangup cause information from the channel that is available through HANGUPCAUSE. 
         IAX2Provision: Provision a calling IAXy with a given template. 
                  ICES: Encode and stream using 'ices'. 
             ImportVar: Import a variable from a channel into a new variable. 
            Incomplete: Returns AST_PBX_INCOMPLETE value. 
                   Log: Send arbitrary text to a selected log level. 
         MailboxExists: Check to see if Voicemail mailbox exists. 
           MessageSend: Send a text message. 
             Milliwatt: Generate a Constant 1004Hz tone at 0dbm (mu-law). 
         MinivmAccMess: Record account specific messages. 
          MinivmDelete: Delete Mini-Voicemail voicemail messages. 
           MinivmGreet: Play Mini-Voicemail prompts. 
             MinivmMWI: Send Message Waiting Notification to subscriber(s) of mailbox. 
          MinivmNotify: Notify voicemail owner about new messages. 
          MinivmRecord: Receive Mini-Voicemail and forward via e-mail. 
            MixMonitor: Record a call and mix the audio during the recording.  Use of StopMixMonitor is required to guarantee the audio file is available for processing during dialplan execution. 
               Monitor: Monitor a channel. 
             Morsecode: Plays morse code. 
             MP3Player: Play an MP3 file or M3U playlist file or stream. 
                  MSet: Set channel variable(s) or function value(s). 
           MusicOnHold: Play Music On Hold indefinitely. 
                NBScat: Play an NBS local stream. 
                 NoCDR: Tell Asterisk to not maintain a CDR for this channel. 
                  NoOp: Do Nothing (No Operation). 
             Originate: Originate a call. 
                  Page: Page series of phones 
                  Park: Park yourself. 
       ParkAndAnnounce: Park and Announce. 
            ParkedCall: Retrieve a parked call. 
          PauseMonitor: Pause monitoring of a channel. 
      PauseQueueMember: Pauses a queue member. 
                Pickup: Directed extension call pickup. 
            PickupChan: Pickup a ringing channel. 
              Playback: Play a file. 
             PlayTones: Play a tone list. 
        PrivacyManager: Require phone number to be entered, if no CallerID sent 
            Proceeding: Indicate proceeding. 
              Progress: Indicate progress. 
                 Queue: Queue a call for a call queue. 
              QueueLog: Writes to the queue_log file. 
           QueueUpdate: Writes to the queue_log file for OutBound calls and updates Realtime Data. Is used at h extension to be able to have all the parameters. 
        RaiseException: Handle an exceptional condition. 
                  Read: Read a variable. 
             ReadExten: Read an extension into a variable. 
            ReceiveFAX: Receive a FAX and save as a TIFF/F file. 
                Record: Record to a file. 
     RemoveQueueMember: Dynamically removes queue members. 
              ResetCDR: Resets the Call Data Record. 
             RetryDial: Place a call, retrying on failure allowing an optional exit extension. 
                Return: Return from gosub routine. 
               Ringing: Indicate ringing tone. 
              SayAlpha: Say Alpha. 
          SayAlphaCase: Say Alpha. 
             SayDigits: Say Digits. 
             SayNumber: Say Number. 
           SayPhonetic: Say Phonetic. 
           SayUnixTime: Says a specified time in a custom format. 
              SendDTMF: Sends arbitrary DTMF digits 
               SendFAX: Sends a specified TIFF/F file as a FAX. 
             SendImage: Sends an image file. 
              SendText: Send a Text Message on a channel. 
               SendURL: Send a URL. 
                   Set: Set channel variable or function value. 
           SetAMAFlags: Set the AMA Flags. 
                   SMS: Communicates with SMS service centres and SMS capable analogue phones. 
            SoftHangup: Hangs up the requested channel. 
  SpeechActivateGrammar: Activate a grammar. 
      SpeechBackground: Play a sound file and wait for speech to be recognized. 
          SpeechCreate: Create a Speech Structure. 
  SpeechDeactivateGrammar: Deactivate a grammar. 
         SpeechDestroy: End speech recognition. 
     SpeechLoadGrammar: Load a grammar. 
  SpeechProcessingSound: Change background processing sound. 
           SpeechStart: Start recognizing voice in the audio stream. 
   SpeechUnloadGrammar: Unload a grammar. 
              StackPop: Remove one address from gosub stack. 
      StartMusicOnHold: Play Music On Hold. 
                Stasis: Invoke an external Stasis application.
        StopMixMonitor: Stop recording a call through MixMonitor, and free the recording's file handle. 
           StopMonitor: Stop monitoring a channel. 
       StopMusicOnHold: Stop playing Music On Hold. 
         StopPlayTones: Stop playing a tone list. 
            StreamEcho: Echo media, up to 'N' streams of a type, and DTMF back to the calling party 
                System: Execute a system command. 
            TestClient: Execute Interface Test Client. 
            TestServer: Execute Interface Test Server. 
              Transfer: Transfer caller to remote extension. 
               TryExec: Executes dialplan application, always returning. 
             TrySystem: Try executing a system command. 
        UnpauseMonitor: Unpause monitoring of a channel. 
    UnpauseQueueMember: Unpauses a queue member. 
             UserEvent: Send an arbitrary user-defined event to parties interested in a channel (AMI users and relevant res_stasis applications). 
               Verbose: Send arbitrary text to verbose output. 
        VMAuthenticate: Authenticate with Voicemail passwords. 
             VMSayName: Play the name of a voicemail user 
             VoiceMail: Leave a Voicemail message. 
         VoiceMailMain: Check Voicemail messages. 
      VoiceMailPlayMsg: Play a single voice mail msg from a mailbox by msg id. 
                  Wait: Waits for some time. 
             WaitDigit: Waits for a digit to be entered. 
             WaitExten: Waits for an extension to be entered. 
          WaitForNoise: Waits for a specified amount of noise. 
           WaitForRing: Wait for Ring Application. 
        WaitForSilence: Waits for a specified amount of silence. 
             WaitUntil: Wait (sleep) until the current time is the given epoch. 
                 While: Start a while loop. 
            Zapateller: Block telemarketers with SIT. 
    -= 167 Applications Registered =-

```

**Issue 4** Public / private address conflicts 
![Sceen1](screenshots/screenshot1.png)
\
**solution** Change bidn addr from 0.0.0.0 to private IP and reload 
![Sceen1](screenshots/screenshot2.png)