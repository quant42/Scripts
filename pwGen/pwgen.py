#! /usr/bin/env python
# -*- coding: UTF-8 -*-

from __future__ import division, print_function
import string, random

def genPwd(alpha, length):
    """
        Generate a random string (a password).

        ``alpha'' The characters that may be present in the password. Each character in alpha will be equally likely in the generated password.
        ``length'' The length of the password string.
    """
    # be sure that each character is exactly once present
    alpha = list(set(alpha))
    # return the created password
    return "".join([random.choice(alpha) for _ in range(length)])

def genAlphaNumPwd(length):
    """
        Generate an alphanumerical password.

        ``length'' The length of the alphanumerical password
    """
    return genPwd(string.ascii_letters + string.digits, length)

#print(genPwd("asdf", 10))
#print(genAlphaNumPwd(20))
