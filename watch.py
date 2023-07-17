import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    try:
        if re.search(r"<iframe(.)*><\/iframe>",s):
            url = re.search("((http)(s)*:\/\/(www\.)*(youtube\.com)\/embed\/)([a-z_A-Z_0-9]+)",s)
            if url:
                return("https://youtu.be/"+url.group(6))
    except:
        sys.exit("Incorrect Input")


...


if __name__ == "__main__":
    main()