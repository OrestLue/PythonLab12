import re


def main():
    count = 0
    regex = '.*\.sportszone\..*\.gif.*'
    with open("con267.tweetie.799608879", "r") as file:
        data = file.readlines()
        for a in data:
            if(re.match(regex, a)):
                x = re.search(regex, a)
                print(x.group())
                count += 1
        print(count)


if __name__ == "__main__":
    main()
