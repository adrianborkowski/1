#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import os
zrodlo = '/home/adi/Downloads/*'
cel = '/media/adi/UUI'
polecenie = 'cp {0} {1}'.format(zrodlo, cel)
if os.system(polecenie) == 0:
    print("Zakończono kopiowanie")
else:
    print("Wystąpił błąd")