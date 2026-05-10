# This is a sample Python script.
import readjson as rd
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import sys
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("we are in main program")

    schema_path=sys.argv[1]
    data_path=sys.argv[2]
    resultpath=sys.argv[3]

    print("schema",schema_path)
    print("data", data_path)
    print("res", resultpath)

    rd.read_json(schema_path,data_path,resultpath)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
