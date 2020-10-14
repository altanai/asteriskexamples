# Debug 

## Logs

```commandline
asterisk -c
```

## traces for asterisk 

Besides tcpdump , Wireshark GUI one can use asterisk cli to output SIP debug traces like below 
Edit pjsip.conf
```
[global]
debug=yes
```
### Registration traces 
```commandline
<--- Received SIP request (581 bytes) from UDP:192.168.1.114:44672 --->
REGISTER sip:192.168.1.114;transport=UDP SIP/2.0
Via: SIP/2.0/UDP 192.168.1.114:44672;branch=z9hG4bK-524287-1---0cd28d05218bdddf;rport
Max-Forwards: 70
Contact: <sip:7000@117.201.86.200:10073;rinstance=5ebb4f0eacdf670e;transport=UDP>
To: <sip:7000@192.168.1.114;transport=UDP>
From: <sip:7000@192.168.1.114;transport=UDP>;tag=a3f73442
Call-ID: _cFTfJZhM3snf2Y-ZGlaHA..
CSeq: 1 REGISTER
Expires: 60
Allow: INVITE, ACK, CANCEL, BYE, NOTIFY, REFER, MESSAGE, OPTIONS, INFO, SUBSCRIBE
User-Agent: Z 5.3.8 rv2.9.30-mod
Allow-Events: presence, kpml, talk
Content-Length: 0


<--- Transmitting SIP response (507 bytes) to UDP:192.168.1.114:44672 --->
SIP/2.0 401 Unauthorized
Via: SIP/2.0/UDP 192.168.1.114:44672;rport=44672;received=192.168.1.114;branch=z9hG4bK-524287-1---0cd28d05218bdddf
Call-ID: _cFTfJZhM3snf2Y-ZGlaHA..
From: <sip:7000@192.168.1.114>;tag=a3f73442
To: <sip:7000@192.168.1.114>;tag=z9hG4bK-524287-1---0cd28d05218bdddf
CSeq: 1 REGISTER
WWW-Authenticate: Digest realm="asterisk",nonce="1596353907/5cd80a4f9b9c6f17153716a929f8708e",opaque="7bb42eb41330688c",algorithm=md5,qop="auth"
Server: Asterisk PBX 17.6.0
Content-Length:  0


<--- Received SIP request (874 bytes) from UDP:192.168.1.114:44672 --->
REGISTER sip:192.168.1.114;transport=UDP SIP/2.0
Via: SIP/2.0/UDP 192.168.1.114:44672;branch=z9hG4bK-524287-1---1b66270a34dfae60;rport
Max-Forwards: 70
Contact: <sip:7000@117.201.86.200:10073;rinstance=5ebb4f0eacdf670e;transport=UDP>
To: <sip:7000@192.168.1.114;transport=UDP>
From: <sip:7000@192.168.1.114;transport=UDP>;tag=a3f73442
Call-ID: _cFTfJZhM3snf2Y-ZGlaHA..
CSeq: 2 REGISTER
Expires: 60
Allow: INVITE, ACK, CANCEL, BYE, NOTIFY, REFER, MESSAGE, OPTIONS, INFO, SUBSCRIBE
User-Agent: Z 5.3.8 rv2.9.30-mod
Authorization: Digest username="7000",realm="asterisk",nonce="1596353907/5cd80a4f9b9c6f17153716a929f8708e",uri="sip:192.168.1.114;transport=UDP",response="23e07c48e6c9e35cb26b30b15b7bcdd5",cnonce="392bac57b62a696f35942d26059548a8",nc=00000001,qop=auth,algorithm=md5,opaque="7bb42eb41330688c"
Allow-Events: presence, kpml, talk
Content-Length: 0


<--- Transmitting SIP response (495 bytes) to UDP:192.168.1.114:44672 --->
SIP/2.0 200 OK
Via: SIP/2.0/UDP 192.168.1.114:44672;rport=44672;received=192.168.1.114;branch=z9hG4bK-524287-1---1b66270a34dfae60
Call-ID: _cFTfJZhM3snf2Y-ZGlaHA..
From: <sip:7000@192.168.1.114>;tag=a3f73442
To: <sip:7000@192.168.1.114>;tag=z9hG4bK-524287-1---1b66270a34dfae60
CSeq: 2 REGISTER
Date: Sun, 02 Aug 2020 07:38:27 GMT
Contact: <sip:7000@117.201.86.200:10073;transport=UDP;rinstance=5ebb4f0eacdf670e>;expires=59
Expires: 60
Server: Asterisk PBX 17.6.0
Content-Length:  0

  == Endpoint 7000 is now Reachable
```

### SIP Call Traces 
```commandline
*CLI> <--- Received SIP request (953 bytes) from UDP:192.168.1.114:44672 --->
INVITE sip:6000@192.168.1.114;transport=UDP SIP/2.0
Via: SIP/2.0/UDP 192.168.1.114:44672;branch=z9hG4bK-524287-1---265e5d2714e8ade6;rport
Max-Forwards: 70
Contact: <sip:7000@117.201.86.200:10073;transport=UDP>
To: <sip:6000@192.168.1.114>
From: <sip:7000@192.168.1.114;transport=UDP>;tag=588c5369
Call-ID: cthQp0qIbkW74p6JwNGM8A..
CSeq: 1 INVITE
Allow: INVITE, ACK, CANCEL, BYE, NOTIFY, REFER, MESSAGE, OPTIONS, INFO, SUBSCRIBE
Content-Type: application/sdp
User-Agent: Z 5.3.8 rv2.9.30-mod
Allow-Events: presence, kpml, talk
Content-Length: 392

v=0
o=Z 1596353755723 1 IN IP4 117.201.86.200
s=Z
c=IN IP4 117.201.86.200
t=0 0
m=audio 23706 RTP/AVP 106 9 98 101 0 8 3
a=rtpmap:106 opus/48000/2
a=fmtp:106 maxplaybackrate=16000; sprop-maxcapturerate=16000; minptime=20; cbr=1; maxaveragebitrate=20000; useinbandfec=1
a=rtpmap:98 telephone-event/48000
a=fmtp:98 0-16
a=rtpmap:101 telephone-event/8000
a=fmtp:101 0-16
a=sendrecv

<--- Transmitting SIP response (505 bytes) to UDP:192.168.1.114:44672 --->
SIP/2.0 401 Unauthorized
Via: SIP/2.0/UDP 192.168.1.114:44672;rport=44672;received=192.168.1.114;branch=z9hG4bK-524287-1---265e5d2714e8ade6
Call-ID: cthQp0qIbkW74p6JwNGM8A..
From: <sip:7000@192.168.1.114>;tag=588c5369
To: <sip:6000@192.168.1.114>;tag=z9hG4bK-524287-1---265e5d2714e8ade6
CSeq: 1 INVITE
WWW-Authenticate: Digest realm="asterisk",nonce="1596353755/321ce9f745903982a6ff41d5fef519af",opaque="6ecb4c30500d7a74",algorithm=md5,qop="auth"
Server: Asterisk PBX 17.6.0
Content-Length:  0


<--- Received SIP request (353 bytes) from UDP:192.168.1.114:44672 --->
ACK sip:6000@192.168.1.114;transport=UDP SIP/2.0
Via: SIP/2.0/UDP 192.168.1.114:44672;branch=z9hG4bK-524287-1---265e5d2714e8ade6;rport
Max-Forwards: 70
To: <sip:6000@192.168.1.114>;tag=z9hG4bK-524287-1---265e5d2714e8ade6
From: <sip:7000@192.168.1.114;transport=UDP>;tag=588c5369
Call-ID: cthQp0qIbkW74p6JwNGM8A..
CSeq: 1 ACK
Content-Length: 0


<--- Received SIP request (1251 bytes) from UDP:192.168.1.114:44672 --->
INVITE sip:6000@192.168.1.114;transport=UDP SIP/2.0
Via: SIP/2.0/UDP 192.168.1.114:44672;branch=z9hG4bK-524287-1---8e4e0db2ecfb8f77;rport
Max-Forwards: 70
Contact: <sip:7000@117.201.86.200:10073;transport=UDP>
To: <sip:6000@192.168.1.114>
From: <sip:7000@192.168.1.114;transport=UDP>;tag=588c5369
Call-ID: cthQp0qIbkW74p6JwNGM8A..
CSeq: 2 INVITE
Allow: INVITE, ACK, CANCEL, BYE, NOTIFY, REFER, MESSAGE, OPTIONS, INFO, SUBSCRIBE
Content-Type: application/sdp
User-Agent: Z 5.3.8 rv2.9.30-mod
Authorization: Digest username="7000",realm="asterisk",nonce="1596353755/321ce9f745903982a6ff41d5fef519af",uri="sip:6000@192.168.1.114;transport=UDP",response="73346e41c5aeacf4bd607a9c16eba5af",cnonce="9ca37c36716346b3990eb0f67dbac234",nc=00000001,qop=auth,algorithm=md5,opaque="6ecb4c30500d7a74"
Allow-Events: presence, kpml, talk
Content-Length: 392

v=0
o=Z 1596353755723 1 IN IP4 117.201.86.200
s=Z
c=IN IP4 117.201.86.200
t=0 0
m=audio 23706 RTP/AVP 106 9 98 101 0 8 3
a=rtpmap:106 opus/48000/2
a=fmtp:106 maxplaybackrate=16000; sprop-maxcapturerate=16000; minptime=20; cbr=1; maxaveragebitrate=20000; useinbandfec=1
a=rtpmap:98 telephone-event/48000
a=fmtp:98 0-16
a=rtpmap:101 telephone-event/8000
a=fmtp:101 0-16
a=sendrecv

  == Setting global variable 'SIPDOMAIN' to '192.168.1.114'
<--- Transmitting SIP response (313 bytes) to UDP:192.168.1.114:44672 --->
SIP/2.0 100 Trying
Via: SIP/2.0/UDP 192.168.1.114:44672;rport=44672;received=192.168.1.114;branch=z9hG4bK-524287-1---8e4e0db2ecfb8f77
Call-ID: cthQp0qIbkW74p6JwNGM8A..
From: <sip:7000@192.168.1.114>;tag=588c5369
To: <sip:6000@192.168.1.114>
CSeq: 2 INVITE
Server: Asterisk PBX 17.6.0
Content-Length:  0


<--- Transmitting SIP response (808 bytes) to UDP:192.168.1.114:44672 --->
SIP/2.0 200 OK
Via: SIP/2.0/UDP 192.168.1.114:44672;rport=44672;received=192.168.1.114;branch=z9hG4bK-524287-1---8e4e0db2ecfb8f77
Call-ID: cthQp0qIbkW74p6JwNGM8A..
From: <sip:7000@192.168.1.114>;tag=588c5369
To: <sip:6000@192.168.1.114>;tag=d8e62d5b-e5f3-473f-ba97-99a20b808e0a
CSeq: 2 INVITE
Server: Asterisk PBX 17.6.0
Contact: <sip:192.168.1.114:5060>
Allow: OPTIONS, REGISTER, SUBSCRIBE, NOTIFY, PUBLISH, INVITE, ACK, BYE, CANCEL, UPDATE, PRACK, MESSAGE, REFER
Supported: 100rel, timer, replaces, norefersub
Content-Type: application/sdp
Content-Length:   230

v=0
o=- 2920888907 3 IN IP4 192.168.1.114
s=Asterisk
c=IN IP4 192.168.1.114
t=0 0
m=audio 13626 RTP/AVP 0 101
a=rtpmap:0 PCMU/8000
a=rtpmap:101 telephone-event/8000
a=fmtp:101 0-16
a=ptime:20
a=maxptime:150
a=sendrecv

<--- Received SIP request (416 bytes) from UDP:192.168.1.114:44672 --->
ACK sip:192.168.1.114:5060 SIP/2.0
Via: SIP/2.0/UDP 192.168.1.114:44672;branch=z9hG4bK-524287-1---fbcd000f069d39ce;rport
Max-Forwards: 70
Contact: <sip:7000@117.201.86.200:10073;transport=UDP>
To: <sip:6000@192.168.1.114>;tag=d8e62d5b-e5f3-473f-ba97-99a20b808e0a
From: <sip:7000@192.168.1.114>;tag=588c5369
Call-ID: cthQp0qIbkW74p6JwNGM8A..
CSeq: 2 ACK
User-Agent: Z 5.3.8 rv2.9.30-mod
Content-Length: 0


---------------- Tring Tring -------
  == Spawn extension (internal_users, 6000, 5) exited non-zero on 'PJSIP/7000-00000035'
<--- Transmitting SIP request (417 bytes) to UDP:117.201.86.200:10073 --->
BYE sip:7000@117.201.86.200:10073;transport=UDP SIP/2.0
Via: SIP/2.0/UDP 192.168.1.114:5060;rport;branch=z9hG4bKPj0f846ed8-95c2-419d-93ce-b313d7fda906
From: <sip:6000@192.168.1.114>;tag=d8e62d5b-e5f3-473f-ba97-99a20b808e0a
To: <sip:7000@192.168.1.114>;tag=588c5369
Call-ID: cthQp0qIbkW74p6JwNGM8A..
CSeq: 5999 BYE
Reason: Q.850;cause=16
Max-Forwards: 70
User-Agent: Asterisk PBX 17.6.0
Content-Length:  0


<--- Received SIP response (419 bytes) from UDP:117.201.86.200:10073 --->
SIP/2.0 200 OK
Via: SIP/2.0/UDP 192.168.1.114:5060;rport=5060;branch=z9hG4bKPj0f846ed8-95c2-419d-93ce-b313d7fda906;received=117.201.86.200
Contact: <sip:7000@117.201.86.200:10073;transport=UDP>
To: <sip:7000@192.168.1.114>;tag=588c5369
From: <sip:6000@192.168.1.114>;tag=d8e62d5b-e5f3-473f-ba97-99a20b808e0a
Call-ID: cthQp0qIbkW74p6JwNGM8A..
CSeq: 5999 BYE
User-Agent: Z 5.3.8 rv2.9.30-mod
Content-Length: 0

```

