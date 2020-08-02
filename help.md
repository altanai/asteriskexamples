## help

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

## List of applications
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

## Codecs Transalation

```commandline
*CLI> core show translation
         Translation times between formats (in microseconds) for one second of data
          Source Format (Rows) Destination Format (Columns)

          codec2  ulaw  alaw   gsm  g726 g726aal2 adpcm slin8 slin12 slin16 slin24 slin32 slin44 slin48 slin96 slin192 lpc10 speex8 speex16 speex32  ilbc  g722 testlaw
   codec2      - 15000 15000 15000 15000    15000 15000  9000  17000  17000  17000  17000  17000  17000  17000   17000 15000  15000   23000   23000 15000 17250   15000
     ulaw  15000     -  9150 15000 15000    15000 15000  9000  17000  17000  17000  17000  17000  17000  17000   17000 15000  15000   23000   23000 15000 17250   15000
     alaw  15000  9150     - 15000 15000    15000 15000  9000  17000  17000  17000  17000  17000  17000  17000   17000 15000  15000   23000   23000 15000 17250   15000
      gsm  15000 15000 15000     - 15000    15000 15000  9000  17000  17000  17000  17000  17000  17000  17000   17000 15000  15000   23000   23000 15000 17250   15000
     g726  15000 15000 15000 15000     -    15000 15000  9000  17000  17000  17000  17000  17000  17000  17000   17000 15000  15000   23000   23000 15000 17250   15000
 g726aal2  15000 15000 15000 15000 15000        - 15000  9000  17000  17000  17000  17000  17000  17000  17000   17000 15000  15000   23000   23000 15000 17250   15000
    adpcm  15000 15000 15000 15000 15000    15000     -  9000  17000  17000  17000  17000  17000  17000  17000   17000 15000  15000   23000   23000 15000 17250   15000
    slin8   6000  6000  6000  6000  6000     6000  6000     -   8000   8000   8000   8000   8000   8000   8000    8000  6000   6000   14000   14000  6000  8250    6000
   slin12  14500 14500 14500 14500 14500    14500 14500  8500      -   8000   8000   8000   8000   8000   8000    8000 14500  14500   14000   14000 14500 14000   14500
   slin16  14500 14500 14500 14500 14500    14500 14500  8500   8500      -   8000   8000   8000   8000   8000    8000 14500  14500    6000   14000 14500  6000   14500
   slin24  14500 14500 14500 14500 14500    14500 14500  8500   8500   8500      -   8000   8000   8000   8000    8000 14500  14500   14500   14000 14500 14500   14500
   slin32  14500 14500 14500 14500 14500    14500 14500  8500   8500   8500   8500      -   8000   8000   8000    8000 14500  14500   14500    6000 14500 14500   14500
   slin44  14500 14500 14500 14500 14500    14500 14500  8500   8500   8500   8500   8500      -   8000   8000    8000 14500  14500   14500   14500 14500 14500   14500
   slin48  14500 14500 14500 14500 14500    14500 14500  8500   8500   8500   8500   8500   8500      -   8000    8000 14500  14500   14500   14500 14500 14500   14500
   slin96  14500 14500 14500 14500 14500    14500 14500  8500   8500   8500   8500   8500   8500   8500      -    8000 14500  14500   14500   14500 14500 14500   14500
  slin192  14500 14500 14500 14500 14500    14500 14500  8500   8500   8500   8500   8500   8500   8500   8500       - 14500  14500   14500   14500 14500 14500   14500
    lpc10  15000 15000 15000 15000 15000    15000 15000  9000  17000  17000  17000  17000  17000  17000  17000   17000     -  15000   23000   23000 15000 17250   15000
   speex8  15000 15000 15000 15000 15000    15000 15000  9000  17000  17000  17000  17000  17000  17000  17000   17000 15000      -   23000   23000 15000 17250   15000
  speex16  23500 23500 23500 23500 23500    23500 23500 17500  17500   9000  17000  17000  17000  17000  17000   17000 23500  23500       -   23000 23500 15000   23500
  speex32  23500 23500 23500 23500 23500    23500 23500 17500  17500  17500  17500   9000  17000  17000  17000   17000 23500  23500   23500       - 23500 23500   23500
     ilbc  15000 15000 15000 15000 15000    15000 15000  9000  17000  17000  17000  17000  17000  17000  17000   17000 15000  15000   23000   23000     - 17250   15000
     g722  15600 15600 15600 15600 15600    15600 15600  9600  17500   9000  17000  17000  17000  17000  17000   17000 15600  15600   15000   23000 15600     -   15600
  testlaw  15000 15000 15000 15000 15000    15000 15000  9000  17000  17000  17000  17000  17000  17000  17000   17000 15000  15000   23000   23000 15000 17250       -
*CLI> 

```