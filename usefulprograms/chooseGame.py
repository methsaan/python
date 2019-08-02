#! /usr/bin/python3

import subprocess as sp
directory = input("Enter language: ")
sp.call("ls ../../" + directory + "/games/" + ("nongraphical/" if directory == "java" or directory == "python" else ""), shell=True)
