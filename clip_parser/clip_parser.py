from pynput.keyboard import Key, KeyCode, Listener
import pyperclip
from utils.rexp import expand_ranges
from utils.translator import clean_where_clause
import re
import sys

# Copy a code range a automagically paste a SQL ready statement!
# SHFT-L
def parse_ranges(txt=None):
    if not txt:
        txt = pyperclip.paste()
    code_pat = re.compile(r"[a-zA-Z]\d{4}|\d{5}|\d{4}[a-zA-Z]")
    codes = re.findall(pattern=code_pat, string=txt)
    try:
        code_list = expand_ranges(codes)
    except:
        print("Could not iterate this range!")
        code_list = codes
    finally:
        msg = "(\n" + "".join(["'" + code + "',\n" for code in code_list]) + ")"
        pyperclip.copy(msg)
        return msg


# Copy the text from which you wish to extract the text into your clipboard and then execute this script.
# SHIFT-C
def grab_codes(txt=None):
    if not txt:
        txt = pyperclip.paste()
    code_pat = re.compile(r"[a-zA-Z]\d{4}|\d{5}|\d{4}[a-zA-Z]")
    txt = txt.strip()
    codes = re.findall(pattern=code_pat, string=txt)
    pyperclip.copy(",".join(codes))
    return codes


def kill_program(txt=None):
    print("Program stopped...")
    sys.exit(0)


# Create a mapping of keys to function (use frozenset as sets are not hashable - so they can't be used as keys)
combination_to_function = {
    frozenset(
        [Key.shift, KeyCode(char="c")]
    ): grab_codes,  # No `()` after function_1 because we want to pass the function, not the value of the function
    frozenset([Key.shift, KeyCode(char="C")]): grab_codes,
    frozenset([Key.shift, KeyCode(char="L")]): parse_ranges,
    frozenset([Key.shift, KeyCode(char="l")]): parse_ranges,
    frozenset([Key.esc]): kill_program,
}

# Currently pressed keys
current_keys = set()


def on_press(key):
    # When a key is pressed, add it to the set we are keeping track of and check if this set is in the dictionary
    current_keys.add(key)
    if frozenset(current_keys) in combination_to_function:
        # If the current set of keys are in the mapping, execute the function
        import inspect

        combination_to_function[frozenset(current_keys)](pyperclip.paste())


def on_release(key):
    # When a key is released, remove it from the set of keys we are keeping track of
    current_keys.remove(key)


def main():
    print("Running...")
    with Listener(on_press=on_press, on_release=on_release) as listener:
        try:
            listener.join()
        except KeyboardInterrupt:
            print("Program stopped.")


if __name__ == "__main__":
    main()
