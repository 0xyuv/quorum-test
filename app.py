VERSION = "1.0.0"


def handler():
    return {"status": "ok", "version": VERSION}


if __name__ == "__main__":
    print(handler())
