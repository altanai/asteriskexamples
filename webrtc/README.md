# Webrtc support for asterisk 

To connect video based webrtc endpoints ensure you load the codecs  and also libsrtp . 
Overwrite the selective conf in this folders with the existing conf of asterisk  to run a basic webrtc video call . 

These were tested with sipml5 on asterisk v17 . 

## Generating self signed certs

use the "ast_tls_cert" script in the "contrib/scripts" Asterisk source directory to
make a self-signed certificate authority and an Asterisk certificate.
```
sh ast_tls_cert.sh -C localhost -O "altanai" -d .
```

after creating the self signed keys start the server 
```
asterisk -vvvvvvc
```


channels 
```
Peer             User/ANR         Call ID          Format           Hold     Last Message    Expiry     Peer      
10.10.10.10     1060             e8ae107f-ce90-2  (ulaw)           No       Rx: ACK                    1060 
```


## Codecs 

core show codecs
Disclaimer: this command is for informational purposes only.
	It does not indicate anything about your configuration.
      ID TYPE  NAME         FORMAT           DESCRIPTION
------------------------------------------------------------------------------------------------
      31 image png          png              (PNG Image)
       6 audio g726         g726             (G.726 RFC3551)
       4 audio alaw         alaw             (G.711 a-law)
       2 audio g723         g723             (G.723.1)
      20 audio speex        speex            (SpeeX)
      21 audio speex        speex16          (SpeeX 16khz)
      22 audio speex        speex32          (SpeeX 32khz)
      24 audio g722         g722             (G722)
      25 audio siren7       siren7           (ITU G.722.1 (Siren7, licensed from Polycom))
      32 video h261         h261             (H.261 video)
      33 video h263         h263             (H.263 video)
       8 audio adpcm        adpcm            (Dialogic ADPCM)
      36 video h265         h265             (H.265 video)
      44 audio silk         silk8            (SILK Codec (8 KHz))
      45 audio silk         silk12           (SILK Codec (12 KHz))
      46 audio silk         silk16           (SILK Codec (16 KHz))
      47 audio silk         silk24           (SILK Codec (24 KHz))
      28 audio g719         g719             (ITU G.719)
      34 video h263p        h263p            (H.263+ video)
      35 video h264         h264             (H.264 video)
      19 audio g729         g729             (G.729A)
       9 audio slin         slin             (16 bit Signed Linear PCM)
      10 audio slin         slin12           (16 bit Signed Linear PCM (12kHz))
      11 audio slin         slin16           (16 bit Signed Linear PCM (16kHz))
      12 audio slin         slin24           (16 bit Signed Linear PCM (24kHz))
      13 audio slin         slin32           (16 bit Signed Linear PCM (32kHz))
      14 audio slin         slin44           (16 bit Signed Linear PCM (44kHz))
      15 audio slin         slin48           (16 bit Signed Linear PCM (48kHz))
      16 audio slin         slin96           (16 bit Signed Linear PCM (96kHz))
      17 audio slin         slin192          (16 bit Signed Linear PCM (192kHz))
       3 audio ulaw         ulaw             (G.711 u-law)
      18 audio lpc10        lpc10            (LPC10)
      27 audio testlaw      testlaw          (G.711 test-law)
      43 audio none         none             (<Null> codec)
      42 image t38          t38              (T.38 UDPTL Fax)
      39 video vp9          vp9              (VP9 video)
      38 video vp8          vp8              (VP8 video)
       5 audio gsm          gsm              (GSM)
      37 video mpeg4        mpeg4            (MPEG4 video)
      23 audio ilbc         ilbc             (iLBC)
      40 text  red          red              (T.140 Realtime Text with redundancy)
      41 text  t140         t140             (Passthrough T.140 Realtime Text)
      29 audio opus         opus             (Opus Codec)
      30 image jpeg         jpeg             (JPEG image)
       7 audio g726aal2     g726aal2         (G.726 AAL2)
       1 audio codec2       codec2           (Codec 2)
      26 audio siren14      siren14          (ITU G.722.1 Annex C, (Siren14, licensed from Polycom))




## Webrtc clients 

generate a client certificate for our SIP device.
```
./ast_tls_cert -m client -c ca.crt -k ca.key -C localhost -O "altanai" -d . -o malcolm
```
