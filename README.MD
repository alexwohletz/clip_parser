# Clip Parse

A simple tool to parse your clipboard contents into formatted text

## Description

This tool allows you to parse various strings into the desired format using a hot key + control v pattern.

## Getting Started

### Dependencies

* pandas,pyperclip,pynput

### Installing
```
cd clip_parser

pip install .
```

### Executing program

* ```python -m clip_parser```
* Control-C on whatever you'd like parsed to copy the contents to your clipboard.
* SHIFT-L activates range parsing which allows you to copy a range and paste a full code list in SQL ready format.
* SHIFT-C activates simple code parsing which allows you copy any test containing codes and paste only the codes.
* Control-V after activating the desired hot key.

## Help

This is pre-alpha and contains no testing.  You may add additional hotkeys and functions easily! To end the program you need to kill the terminal, for some reason Control-C will not send interrupt.

```
command to run if program contains helper info
```

## Authors

Contributors names and contact info

Alex Wohletz

## Version History


* 0.1
    * Initial Release
