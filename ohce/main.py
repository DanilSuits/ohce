import time
from ohce.v20220820 import V20220820


class Main:
    @staticmethod
    def run(*, stdin, stdout, epoch_seconds):
        interactive_loop = V20220820.interactive_loop(
            stdin=stdin,
            stdout=stdout,
            epoch_seconds=epoch_seconds
        )
        interactive_loop()


def main():
    Main.run(
        stdin=input,
        stdout=print,
        epoch_seconds=time.time
    )


if __name__ == '__main__':
    main()
