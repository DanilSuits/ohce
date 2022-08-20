import time


class Main:
    @staticmethod
    def run(*, stdin, stdout, epoch_seconds):
        pass


def main():
    Main.run(
        stdin=input,
        stdout=print,
        epoch_seconds=time.time
    )


if __name__ == '__main__':
    main()
