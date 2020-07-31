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

You can use safe_asterisk to enable auto restart after crash thus minimizing downtime . It also creates core dump file .

One can continue on the sandbox environment to run the modules I describe in this repo . 

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



## Applications 
Call Queue monitoring 

