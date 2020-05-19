#!/bin/sh
#
# parallel.sh
# Copyright (C) 2020 devel <hyphens@pm.me>
#
# Distributed under terms of the MIT license.
#


# Test-running multicore parallelism in haskell with ghc

ghc -O2 --make parallel.hs -threaded -rtsopts
time ./parallel +RTS -N2
