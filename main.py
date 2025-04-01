import sys
from services import *

def main():
    if args.dir:
        if args.json:
            generate_by_json(args.json, output_dir=args.dir)
        elif args.text:
            generate_by_text(text=args.text, output_dir=args.dir)
    else:
        if args.json:
            generate_by_json(args.json)
        elif args.text:
            generate_by_text(args.text)


if __name__ == "__main__":
    main()
    print('qrcode created')
