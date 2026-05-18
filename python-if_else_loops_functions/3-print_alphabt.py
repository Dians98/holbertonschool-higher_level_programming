#!/usr/bin/python3
print("".join("{:c}".format(97 + i)
      for i in range(26) if ("{:c}".format(97 + i) != "q" and "{:c}".format(97 + i) != "e")), end="")
