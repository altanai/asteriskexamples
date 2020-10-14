# Voicemail application 

To see details 
```commandline
*CLI> core show application voicemail
```

[Synopsis]
Leave a Voicemail message. 

[Description]
This application allows the calling party to leave a message for the specified
list of mailboxes. When multiple mailboxes are specified, the greeting will be
taken from the first mailbox specified. Dialplan execution will stop if the
specified mailbox does not exist.
The Voicemail application will exit if any of the following DTMF digits are
received:
    0 - Jump to the 'o' extension in the current dialplan context.
    * - Jump to the 'a' extension in the current dialplan context.
This application will set the following channel variable upon completion:
${VMSTATUS}: This indicates the status of the execution of the VoiceMail
application.
    SUCCESS
    USEREXIT
    FAILED

[Syntax]
VoiceMail(mailbox[@context][&mailbox[@context][&...]][,options])

[Arguments]
options
    b: Play the 'busy' greeting to the calling party.

    d([c]): Accept digits for a new extension in context <c>, if played during
    the greeting. Context defaults to the current context.

    g(#): Use the specified amount of gain when recording the voicemail
    message. The units are whole-number decibels (dB). Only works on supported
    technologies, which is DAHDI only.

    s: Skip the playback of instructions for leaving a message to the calling
    party.

    u: Play the 'unavailable' greeting.

    U: Mark message as 'URGENT'.

    P: Mark message as 'PRIORITY'.

