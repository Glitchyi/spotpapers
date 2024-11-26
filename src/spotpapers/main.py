from spotpapers.AI.groq import image_name_suggestion
from os import listdir, mkdir, environ, path
from shutil import move
from json import loads
import click

USERPATH = environ.get("USERPROFILE")
PATH = rf"{USERPATH}\AppData\Local\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets"

NIL="NO API KEY"

if not path.exists(rf"{USERPATH}\Pictures\Spotlight Wallpapers"):
    mkdir(rf"{USERPATH}\Pictures\Spotlight Wallpapers")


def validate_air(ctx, param, value):
    if value is None:
        return environ.get("GROQ_API_KEY")
    return value

@click.command()
@click.option(
    '--air',
    default=None,
    required=False,
    is_flag=False,
    flag_value=NIL,
    metavar='<GROQ_API Key>',
    help='API key for the AI Rename (air) function. Can be provided using --air or set as the GROQ_API_KEY environment variable.'
)
def main(air):
    "Simple program that helps extract windows spotlight wallpapers"
    
    if air == NIL:
        if environ.get("GROQ_API_KEY") is None:
            click.echo(
                "An API key is required. Provide it using --air or set it as the 'GROQ_API_KEY' environment variable."
            )
            return
        else:
            air = environ.get("GROQ_API_KEY")
    
    if air is not None and "gsk_r" not in air:
            click.echo(
                "Enter a valid API key. Provide it using --air or set it as the 'GROQ_API_KEY' environment variable."
            )
            return
    
    wallpaperlist = listdir(path=PATH)
    print("doing shit")
    for i in wallpaperlist:
        IMAGENAME=i
        if air:
            response = image_name_suggestion(PATH + "\\" + i)
            response_json = loads(response)
            IMAGENAME = response_json.get("name", "No name found")
        NEWPATH = rf"{USERPATH}\Pictures\Spotlight Wallpapers\{IMAGENAME}.jpeg"
        move(rf"{PATH}\{i}", NEWPATH)
        print(IMAGENAME)

if __name__ == "__main__":
    main()
