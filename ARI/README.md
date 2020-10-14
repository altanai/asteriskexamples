# ARI (  Asterisk REST Interface )

Exposes primitive objects in Asterisk like  channels, bridges, endpoints, media, etc over REST interface . Also conveys state of objects using Websockets and JSON. Used for building rich communication application. 

By default, ARI cannot just manipulate any arbitrary channel in Asterisk. That channel may be in a long running dialplan application; it may be controlled by an AGI; it may be hung up

## ARI and HTTP Status 

ARI status
```commandline
*CLI> ari show status
ARI Status:
Enabled: Yes
Output format: pretty
Auth realm: Asterisk REST Interface
Allowed Origins: *
User count: 1
```

HTTP status
```commandline
*CLI> http show status
HTTP Server Status:
Prefix: 
Server: Asterisk
Server Enabled and Bound to 192.168.1.114:8088

Enabled URI's:
/httpstatus => Asterisk HTTP General Status
/phoneprov/... => Asterisk HTTP Phone Provisioning Tool
/amanager => HTML Manager Event Interface w/Digest authentication
/metrics/... => Prometheus Metrics URI
/arawman => Raw HTTP Manager Event Interface w/Digest authentication
/manager => HTML Manager Event Interface
/static/... => Asterisk HTTP Static Delivery
/rawman => Raw HTTP Manager Event Interface
/amxml => XML Manager Event Interface w/Digest authentication
/mxml => XML Manager Event Interface
/ari/... => Asterisk RESTful API
/ws => Asterisk HTTP WebSocket

Enabled Redirects:
  None.
```

HTTP status Link - http://192.168.1.114:8088/httpstatus
![Sceen1](../screenshots/screenshot3.png)

Manager Link - http://192.168.1.114:8088/manager
![Sceen1](../screenshots/screenshot4.png)

### Login 

Can be tried visiting http://localhost:8088/manager
or using wscat

output
```

```

## Stasis Application

To hand a channel over to ARI, Asterisk uses a dialplan application called Stasis.
Inputs 
1. Name of the ARI application to hand the channel over to. 
2. Optionally, arguments to pass to the ARI application when the channel is handed over.



## TLS ARI

tlsenable	-	Enable HTTPS

tlsbindaddr	- 	The IP address and port to bind the HTTPS server to. This should be an IP address and port, e.g., 0.0.0.0:8089

tlscertfile	Path	 - The full path to the certificate file to use. Asterisk only supports the .pem format.

tlsprivatekey	Path -  The full path to the private key file. Asterisk only supports the .pem format. If this is not specified, the certificate specified in 
tlscertfile will be searched for the private key.

## Debugging Help 

**Issue 1** CORS block on runing ARI tester
```
Access to XMLHttpRequest at 'http://asterisk:asterisk@localhost:8088/ari/applications/hello-world/subscription?eventSource=channel:,endpoint:,bridge:,deviceState:' from origin 'null' has been blocked by CORS policy: No 'Access-Control-Allow-Origin' header is present on the requested resource.
ari_tester.html:521 http POST error
```
**Solution** Ensure you run ARI tester over http server such as 
```
http-server  -a localhost -p 8080 -c -1
npm install -g http-server
```
Add allowed origins in ari.conf
```
allowed_origins = localhost:8088
```
or can also add wildcard * to allow all channels 
```
allowed_origins = *
```

**Issue2** Unautheticated or  tried to authenticate with nonexistent user 'asterisk'
```
*CLI> <--- Examining AMI action: -->
action: login
action: 
command: 
username: asterisk
Secret: <redacted from logging>

[Aug 12 11:10:26] NOTICE[3881]: manager.c:3523 authenticate: 127.0.0.1 tried to authenticate with nonexistent user 'asterisk'
[Aug 12 11:10:26] NOTICE[3881]: manager.c:3560 authenticate: 127.0.0.1 failed to authenticate as 'asterisk'
```

**solution** Ensure user used in loggin is mentioend in ari.conf 
```
[asterisk]
        type = user
        read_only = no
        password = asterisk
        allowed_origins = *
        password_format = plain

```
Try relaoding 
```
core reload
```

**issue3** 	Trying to open POST URL such as 'http://asterisk:asterisk@127.0.0.1:8088/ari/applications/hello-world/subscription?eventSource=channel:,endpoint:,bridge:,deviceState:'
```
{
  "message": "Invalid method"
}
```
**solution** only GET requests can be opening via new tab in this way not POST


**Issue4** Missing action in request

**Solution**




**References**
 - Nodejs ARI https://github.com/asterisk/node-ari-client
 - ARI Tester https://github.com/daniele77/aritester