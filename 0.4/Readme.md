# SPEECHBIRD
#### Video Demo:  <URL HERE>
#### Sources, Installation and Usage Manuals:  <URL HERE>
#### Description:
**SPEECHBIRD lets you do (nearly) everything on your computer, hands free.** SPEECHBIRD brings (a lot of) extra functionality, speed and accuracy to Speech Recognition, so you can operate your computer entirely with **your voice** instead of your hands (but with speed (and sanity)).

* Craft beautiful documents for business or school
* Write emails
* Browse the internet
* Play games
* Control any Windows application, and Windows operating system itself
* Write code
* Fully operate your computer!
If you want to do all this while using your keyboard or mouse less, or not at all: SPEECHBIRD is for you.

SPEECHBIRD is free software released under the GNU / GPL3 terms.

#### Key Details:
SPEECHBIRD comes with a set of 100's of new commands which simulate keyboard/mouse actions and direct control of applications and operating system functions. SPEECHBIRD commands are designed for a quick, accurate and pleasant voice control experience:
* Intuitive and memorable: "Bold" means bold ... "Copy" means copy. Easy, right?
* Fun, quick and low-effort to pronounce: "Yep" replaces WSR's tedious and boring "Click that". Say "Click that" out loud as many times as you clicked your mouse in the last hour... Now, try "Yep".
* Logical and modular: When you learn a new SPEECHBIRD command, you actually learn a powerful piece of logic that applies everywhere, giving you access to many other new commands. Example: Adding an "s" to editing commands will automatically select the previous word(s), and apply an editing action to them. Other Speech Recognition solutions require you to say "select last word" (or: "select last 3 words"), and then the user can say "Cut" or "Copy", etc. With SPEECHBIRD, "Cuts" will select and cut the previous word. Saying "Cuts 3" will cut the last words. Having learned this piece, you can fly with all editing commands, such as "Bolds 5" (Make last 5 words bold), "Underlines" (Underline last word), "Copys 2" (Copy last 2 words), etc.
* Reduction of misrecognitions: Similar-sounding words have been avoided when choosing words for voice commands.

SPEECHBIRD adds **Command Streaming** capability. Without SPEECHBIRD, you have to pause after speaking each voice command to allow the computer to perform it:
"Select last 4 words" (pause...) "Copy" (pause...) "Press up 3 times" (pause...) "Select next 2 words" (pause...) "Paste" (pause...).
With SPEECHBIRD's Command Streaming, you can say it all in one breath: "Copys 4, up 3, pastes 2" -- Done!
(v0.4 and up. Previous versions use "4 Copys, 3 Up, 2 Pastes")

SPEECHBIRD's command structures are built to play nicely with SPEECHBIRD's Command Streaming. If you need to pause to think in the middle of a stream, that's fine! A half-spoken stream will not cause havoc, it will just mean only half the actions get performed. This is helpful to reduce stress and wasted time, giving you the freedom to stop to consider what you want to do next, or the oppotunity to remember a command you forgot. To use the above example, if you say "Copys 4, up 3" (and then need a moment to gather your thoughts, before proceeding to "Pastes 2") -- no problem!

Head over to the SPEECHBIRD Dictionary for a complete manual of the SPEECHBIRD Dialect.

####All required & recommended apps are free.
#####Required:
* Microsoft's "Windows Speech Recognition"
WSR is a Windows built-in. Activate through Control Panel.

* Microsoft's "WSR Macros"
Download from Microsoft or other sources, such as:
https://windows-speech-recognition-macros.software.informer.com/download/

#####Recommended: 
* Cesar Mauri's "Enable ViaCam"
Control your mouse by moving your face. Requires a regular webcam.
https://eviacam.crea-si.com/index.php

* Chris Mallett and Steve Gray's "Auto Hot Key"
https://www.autohotkey.com/
SPEECHBIRD's AHK scripts enhance mouse control, adding Drag & Drop, Right-button Drag & Drop, Continuous Scrolling. Say "Drag" to hold-down the left mouse button, "R Drag" to drag with the right button. Say "Drop" to let go (either/both L/R buttons). Say "Scroll <Up/Down>" to start scrolling, "Yep" to stop.

* Microsoft PowerToys
Enable showing when (and where) the mouse clicks (and whether it was Left or Right click).
Say "Mouse Dots" to turn this feature On / Off.
https://learn.microsoft.com/en-us/windows/powertoys/

* Some users like using Click By Voice (Chrome/Edge add-on)
Find it on your browser's app store.
SPEECHBIRD's Web Browser extensions trigger Click By Voice when you speak any 1-4 digits while Chrome / Edge are active. Eg. if you want to click link #234, just say "Two Three Four".

* To reduce errors and increases accuracy, use a quiet workspace and a head worn microphone. No need to shell out big $$'s, the microphones that come free with most cell phones are usually excellent for speech recognition. Best to keep your mic about 2-4 cm from the corner of your mouth. Noise cancelling mic's, bluetooth mic's and apps that I tested have so far proved to only reduce accuracy, so I recommend **simple, wired microphones**.

#####Tips on dealing with background noise:
1. Place your mic near your mouth, which in turn allows you to lower its input gain, thus naturally eliminating lots of room noise.
2. Use a uni-directional microphone ("passive noise cancellation"). This is good but not necessary. If using uni-directional, note: Accurate mic-placement is less forgiving as they are more sensitive to bass-booms with plosives like "buh" and "puh", and hyper-uni-directional mics are also prone to a "blocked nose" sound signature if none of the sounds that come through your nose during speech (Yes! ...certain elements of your voice do come out through your nose :)
3. Experiment by recording yourself saying the same test-paragraph on any mic's you have handy, using various placements. Listening to the playback (best done with earphones) to sample how your computer is hearing you.

I've gotten great accuracy from a simple heaset mic that came with my old Nokia phone, as well as a relatively cheap "JK Mic" from Amazon. I get distracted from stuff touching my face, so I've mounted these mic's on a hard wire that attaches to my glasses' frame, and keeps the mic near my mouth.
