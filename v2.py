import os
import argparse
import re

def play(video_file, **kwargs):
    command_list = []
    command_list.append("mplayer")
    command_list.append("-really-quiet")
    for arg in kwargs:
        command_list.append("-" + arg)
        command_list.append(kwargs[arg])

    command_list.append(video_file)
    os.system(' '.join(command_list))

def verify_local(filename):
    try:
        with open(filename):
            return True
    except IOError:
        return False

def verify_youtube(url):
    #regex used from youtube-dl's code by rg3.
    _VALID_URL = r"""^
                     (
                         (?:https?://)?                                       # http(s):// (optional)
                         (?:youtu\.be/|(?:\w+\.)?youtube(?:-nocookie)?\.com/|
                            tube\.majestyc\.net/)                             # the various hostnames, with wildcard subdomains
                         (?:.*?\#/)?                                          # handle anchor (#/) redirect urls
                         (?:                                                  # the various things that can precede the ID:
                             (?:(?:v|embed|e)/)                               # v/ or embed/ or e/
                             |(?:                                             # or the v= param in all its forms
                                 (?:watch(?:_popup)?(?:\.php)?)?              # preceding watch(_popup|.php) or nothing (like /?v=xxxx)
                                 (?:\?|\#!?)                                  # the params delimiter ? or # or #!
                                 (?:.*?&)?                                    # any other preceding param (like /?s=tuff&v=xxxx)
                                 v=
                             )
                         )?                                                   # optional -> youtube.com/xxxx is OK
                     )?                                                       # all until now is optional -> you can pass the naked ID
                     ([0-9A-Za-z_-]+)                                         # here is it! the YouTube video ID
                     (?(1).+)?                                                # if we found the ID, everything can follow
                     $"""
    return re.match(_VALID_URL, url, re.VERBOSE) is not None

def local(filename, ss=None):
    if verify_local(filename):
        if ss is not None:
            play(filename, ss=ss)
        else:
            play(filename)
        return True
    else:
        print "Please provide a valid file to play."
        return False

def youtube(url, ss=None):
    if verify_youtube(url):
        os.system('youtube-dl -q -o "temp-output-video.%(ext)s" ' + url)
        if ss is not None:
            play("temp-output-video.*", ss=ss)
        else:
            play("temp-output-video.*")
        os.system('rm temp-output-video.*')
        return True
    else:
        print "Please provide a valid youtube video to play."
        return False

def main():
    cli_parser = argparse.ArgumentParser()
    cli_parser.add_argument("--youtube", help="url to youtube video", type=str)
    cli_parser.add_argument("--filename", help="Path to local media file to be played. Cannot use with youtube flag.", type=str)
    cli_parser.add_argument("--seek", help="Specific time to play video. Format in seconds, or h:m:s", type=str)

    args = cli_parser.parse_args()

    if args.youtube is not None:
        if args.seek is not None:
            youtube(args.youtube, ss=args.seek)
        else:
            youtube(args.youtube)

    elif args.filename is not None:
        if args.seek is not None:
            local(args.filename, ss=args.seek)
        else:
            local(args.filename)

if __name__ == "__main__":
    main()
