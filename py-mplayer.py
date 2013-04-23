import os
import argparse

def play(video_file, **kwargs):
    command_list = []
    command_list.append("mplayer")
    command_list.append("-really-quiet")
    for arg in kwargs:
        command_list.append("-" + arg)
        command_list.append(kwargs[arg])

    command_list.append(video_file)
    print ' '.join(command_list)
    os.system(' '.join(command_list))

def verify(filename):
    try:
        with open(filename):
            return True
    except IOError:
        return False

def local(filename, ss=None):
    if verify(filename):
        if ss is not None:
            play(filename, ss=ss)
        else:
            play(filename)
    else:
        print "Please provide a valid file to play."        

def youtube(url, ss=None):
    os.system('youtube-dl -o "temp-output-video.%(ext)s" ' + url)
    if ss is not None:
        play("temp-output-video.*", ss=ss)
    else:
        play("temp-output-video.*")
    os.system('rm temp-output-video.*')

def main():
    cli_parser = argparse.ArgumentParser()
    cli_parser.add_argument("--youtube", help="url to youtube video", type=str)
    cli_parser.add_argument("--filename", help="Path to local media file to be played. Cannot use with youtube flag.", type=str)
    cli_parser.add_argument("--seek", help="Specific time to play video. Format in seconds, or h:m:s", type=str)

    args = cli_parser.parse_args()

    filename = "temp-output-video.*"

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

    else:
        print "Please utilize the --filename argument to play a local file, or the --youtube argument to play a youtube video."
        print "Use -h for more help"

if __name__ == "__main__":
    main()
