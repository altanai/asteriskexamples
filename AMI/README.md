# Manager  AMI

manager is a client/server model over TCP

control the PBX, originate calls, check mailbox status, monitor channels and queues as well as execute Asterisk commands.

;
; Authorization for various classes
;
; Read authorization permits you to receive asynchronous events, in general.
; Write authorization permits you to send commands and get back responses.  The
; following classes exist:
;
; all       - All event classes below (including any we may have missed).
; system    - General information about the system and ability to run system
;             management commands, such as Shutdown, Restart, and Reload. This
;             class also includes dialplan manipulation actions such as
;             DialplanExtensionAdd and DialplanExtensionRemove.
; call      - Information about channels and ability to set information in a
;             running channel.
; log       - Logging information.  Read-only. (Defined but not yet used.)
; verbose   - Verbose information.  Read-only. (Defined but not yet used.)
; agent     - Information about queues and agents and ability to add queue
;             members to a queue.
; user      - Permission to send and receive UserEvent.
; config    - Ability to read and write configuration files.
; command   - Permission to run CLI commands.  Write-only.
; dtmf      - Receive DTMF events.  Read-only.
; reporting - Ability to get information about the system.
; cdr       - Output of cdr_manager, if loaded.  Read-only.
; dialplan  - Receive NewExten and VarSet events.  Read-only.
; originate - Permission to originate new calls.  Write-only.
; agi       - Output AGI commands executed.  Input AGI command to execute.
; cc        - Call Completion events.  Read-only.
; aoc       - Permission to send Advice Of Charge messages and receive Advice
;           - Of Charge events.
; test      - Ability to read TestEvent notifications sent to the Asterisk Test
;             Suite.  Note that this is only enabled when the TEST_FRAMEWORK
;             compiler flag is defined.
; security  - Security Events.  Read-only.
; message   - Permissions to send out of call messages. Write-only


## List of all commands 

```

*CLI> manager show commands
  Action                                       Synopsis
  ------                                       --------
  AbsoluteTimeout                              Set absolute timeout. 
  AgentLogoff                                  Sets an agent as no longer logged
  Agents                                       Lists agents and their status. 
  AGI                                          Add an AGI command to execute by 
  AOCMessage                                   Generate an Advice of Charge mess
  Atxfer                                       Attended transfer. 
  BlindTransfer                                Blind transfer channel(s) to the 
  Bridge                                       Bridge two channels already in th
  BridgeTechnologyList                         List available bridging technolog
  BridgeTechnologySuspend                      Suspend a bridging technology. 
  BridgeTechnologyUnsuspend                    Unsuspend a bridging technology. 
  CancelAtxfer                                 Cancel an attended transfer. 
  Challenge                                    Generate Challenge for MD5 Auth. 
  ChangeMonitor                                Change monitoring filename of a c
  Command                                      Execute Asterisk CLI Command. 
  ConfbridgeKick                               Kick a Confbridge user. 
  ConfbridgeList                               List participants in a conference
  ConfbridgeListRooms                          List active conferences. 
  ConfbridgeLock                               Lock a Confbridge conference. 
  ConfbridgeMute                               Mute a Confbridge user. 
  ConfbridgeSetSingleVideoSrc                  Set a conference user as the sing
  ConfbridgeStartRecord                        Start recording a Confbridge conf
  ConfbridgeStopRecord                         Stop recording a Confbridge confe
  ConfbridgeUnlock                             Unlock a Confbridge conference. 
  ConfbridgeUnmute                             Unmute a Confbridge user. 
  ControlPlayback                              Control the playback of a file be
  CoreSettings                                 Show PBX core settings (version e
  CoreShowChannels                             List currently active channels. 
  CoreStatus                                   Show PBX core status variables. 
  CreateConfig                                 Creates an empty file in the conf
  DBDel                                        Delete DB entry. 
  DBDelTree                                    Delete DB Tree. 
  DBGet                                        Get DB Entry. 
  DBPut                                        Put DB entry. 
  DeviceStateList                              List the current known device sta
  DialplanExtensionAdd                         Add an extension to the dialplan 
  DialplanExtensionRemove                      Remove an extension from the dial
  Events                                       Control Event Flow. 
  ExtensionState                               Check Extension Status. 
  ExtensionStateList                           List the current known extension 
  FAXSession                                   Responds with a detailed descript
  FAXSessions                                  Lists active FAX sessions 
  FAXStats                                     Responds with fax statistics 
  Filter                                       Dynamically add filters for the c
  GetConfig                                    Retrieve configuration. 
  GetConfigJSON                                Retrieve configuration (JSON form
  Getvar                                       Gets a channel variable or functi
  Hangup                                       Hangup channel. 
  IAXnetstats                                  Show IAX Netstats. 
  IAXpeerlist                                  List IAX Peers. 
  IAXpeers                                     List IAX peers. 
  IAXregistry                                  Show IAX registrations. 
  ListCategories                               List categories in configuration 
  ListCommands                                 List available manager commands. 
  LocalOptimizeAway                            Optimize away a local channel whe
  LoggerRotate                                 Reload and rotate the Asterisk lo
  Login                                        Login Manager. 
  Logoff                                       Logoff Manager. 
  MailboxCount                                 Check Mailbox Message Count. 
  MailboxStatus                                Check mailbox. 
  MessageSend                                  Send an out of call message to an
  MixMonitor                                   Record a call and mix the audio d
  MixMonitorMute                               Mute / unMute a Mixmonitor record
  ModuleCheck                                  Check if module is loaded. 
  ModuleLoad                                   Module management. 
  Monitor                                      Monitor a channel. 
  MuteAudio                                    Mute an audio stream. 
  Originate                                    Originate a call. 
  Park                                         Park a channel. 
  ParkedCalls                                  List parked calls. 
  Parkinglots                                  Get a list of parking lots 
  PauseMonitor                                 Pause monitoring of a channel. 
  Ping                                         Keepalive command. 
  PJSIPNotify                                  Send a NOTIFY to either an endpoi
  PJSIPQualify                                 Qualify a chan_pjsip endpoint. 
  PJSIPRegister                                Register an outbound registration
  PJSIPShowAors                                Lists PJSIP AORs. 
  PJSIPShowAuths                               Lists PJSIP Auths. 
  PJSIPShowContacts                            Lists PJSIP Contacts. 
  PJSIPShowEndpoint                            Detail listing of an endpoint and
  PJSIPShowEndpoints                           Lists PJSIP endpoints. 
  PJSIPShowRegistrationInboundContactStatuses  Lists ContactStatuses for PJSIP i
  PJSIPShowRegistrationsInbound                Lists PJSIP inbound registrations
  PJSIPShowRegistrationsOutbound               Lists PJSIP outbound registration
  PJSIPShowResourceLists                       Displays settings for configured 
  PJSIPShowSubscriptionsInbound                Lists subscriptions. 
  PJSIPShowSubscriptionsOutbound               Lists subscriptions. 
  PJSIPUnregister                              Unregister an outbound registrati
  PlayDTMF                                     Play DTMF signal on a specific ch
  PresenceState                                Check Presence State 
  PresenceStateList                            List the current known presence s
  QueueAdd                                     Add interface to queue. 
  QueueChangePriorityCaller                    Change priority of a caller on qu
  QueueLog                                     Adds custom entry in queue_log. 
  QueueMemberRingInUse                         Set the ringinuse value for a que
  QueuePause                                   Makes a queue member temporarily 
  QueuePenalty                                 Set the penalty for a queue membe
  QueueReload                                  Reload a queue, queues, or any su
  QueueRemove                                  Remove interface from queue. 
  QueueReset                                   Reset queue statistics. 
  QueueRule                                    Queue Rules. 
  QueueStatus                                  Show queue status. 
  QueueSummary                                 Show queue summary. 
  Redirect                                     Redirect (transfer) a call. 
  Reload                                       Send a reload event. 
  SendText                                     Sends a text message to channel. 
  Setvar                                       Sets a channel variable or functi
  ShowDialPlan                                 Show dialplan contexts and extens
  SKINNYdevices                                List SKINNY devices (text format)
  SKINNYlines                                  List SKINNY lines (text format). 
  SKINNYshowdevice                             Show SKINNY device (text format).
  SKINNYshowline                               Show SKINNY line (text format). 
  SorceryMemoryCacheExpire                     Expire (remove) ALL objects from 
  SorceryMemoryCacheExpireObject               Expire (remove) an object from a 
  SorceryMemoryCachePopulate                   Expire all objects from a memory 
  SorceryMemoryCacheStale                      Marks ALL objects in a sorcery me
  SorceryMemoryCacheStaleObject                Mark an object in a sorcery memor
  Status                                       List channel status. 
  StopMixMonitor                               Stop recording a call through Mix
  StopMonitor                                  Stop monitoring a channel. 
  UnpauseMonitor                               Unpause monitoring of a channel. 
  UpdateConfig                                 Update basic configuration. 
  UserEvent                                    Send an arbitrary event. 
  VoicemailRefresh                             Tell Asterisk to poll mailboxes f
  VoicemailUsersList                           List All Voicemail User Informati
  VoicemailUserStatus                          Show the status of given voicemai
  WaitEvent                                    Wait for an event to occur. 
  ```