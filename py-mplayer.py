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

def local(filename, **kwargs):
    if verify(filename):
        play(filename, **kwargs)
    else:
        print "Please provide a valid file to play."

def youtube(url, **kwargs):
    os.system('youtube-dl -o "temp-output-video.%(ext)s" ' + url)
    play("temp-output-video.*", **kwargs)
    os.system('rm temp-output-video.*')

def get_args(args):
    return_arguments = {}
    if args.seek is not None:
        return_arguments['ss'] = args.seek
    if args.osd is not None:
        return_arguments['osdlevel'] = args.osd
    return return_arguments

def main():
    cli_parser = argparse.ArgumentParser()
    cli_parser.add_argument("--youtube", help="url to youtube video", type=str)
    cli_parser.add_argument("--filename", help="Path to local media file to be played. Cannot use with youtube flag.", type=str)
    cli_parser.add_argument("--seek", help="Specific time to play video. Format in seconds, or h:m:s", type=str)
    cli_parser.add_argument("--osd", help="Choose to show the on screen display for time. (0, 1, 2)", type=str)

    args = cli_parser.parse_args()

    filename = "temp-output-video.*"

    kwargs = get_args(args)

    if args.youtube is not None:
        youtube(args.youtube, **kwargs)

    elif args.filename is not None:
        local(args.filename, **kwargs)

if __name__ == "__main__":
    main()
