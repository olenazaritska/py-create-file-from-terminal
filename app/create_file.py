import argparse
import datetime
import os


def main() -> None:
    directories, file_name = get_args()
    create_directories(directories)

    if file_name:
        full_path = get_full_path(directories, file_name)
        with open(full_path, "a") as file:
            current = datetime.datetime.now()
            file.write(current.strftime("%Y-%m-%d %H:%M:%S") + "\n")
            while True:
                line = input("Enter content line: ") + "\n"
                if line.strip() != "stop":
                    file.write(line)
                else:
                    file.write("\n")
                    break


def get_args() -> tuple:
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", nargs="+")
    parser.add_argument("-f")
    args = vars(parser.parse_args())
    return args["d"], args["f"]


def create_directories(directories: list | None) -> None:
    if directories:
        dir_path = os.path.join(*directories)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)


def get_full_path(
        directories: list | None,
        file_name: str
) -> str:
    path_parts = []

    if directories:
        path_parts.extend(directories)
    path_parts.append(file_name)
    return os.path.join(*path_parts)


if __name__ == "__main__":
    main()
