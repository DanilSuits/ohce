from ohce.v20220820 import V20220820


class Main:
    @staticmethod
    def run():
        interactive_loop = V20220820.live()
        interactive_loop()


def main():
    Main.run()


if __name__ == '__main__':
    main()
