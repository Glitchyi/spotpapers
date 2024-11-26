import os
import click

def validate_air(ctx, param, value):
    if value is None:
        print("NO API")
    return value

# print(os.getenv("GROQ_API_KEY"))
NIL = "GET A API KEY"

@click.command()
@click.option(
    '--air','-a',
    is_flag=False,
    flag_value=NIL,
    default=NIL,
    type=str,
    help='API key for the AI Rename (air) function. Can be provided using --air or set as the GROQ_API_KEY environment variable.'
)
def main(air):
    print(f"API Key: {air}")

if __name__ == "__main__":
    main()