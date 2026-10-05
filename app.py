VERSION = "1.1.1"


def handler():
    return {"status": "ok", "version": VERSION}


if __name__ == "__main__":
    print(handler())
