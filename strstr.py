from typing import List

"""
    i = 0
    needleLen = 5
    haystack = "hello world this is khoubaib"
    needle = "is is"
"""

def strstr(haystack: str, needle: str) -> int: # time: O(n*m), space: O(m)
    if len(needle) > len(haystack):
        return -1

    i = 0
    needleLen = len(needle)
    while i <= len(haystack) - needleLen: # time: O(n) ==> n is the size of haystack
        if haystack[i:i+needleLen] == needle: # time: O(m) ==> n is the size of needle
            return i
        i += 1
    return -1
 
def main():
    haystack = "hello world this is khoubaib5"
    needle = "5"
    print(len(haystack))
    print(strstr(haystack, needle))

if __name__ == "__main__":
    main()
