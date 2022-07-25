from modules.app import App


def main():
    app = App([500, 500], 60, "SnakeGame")
    app.run()


if __name__ == "__main__":
    main()
