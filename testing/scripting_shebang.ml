#!/usr/bin/env -S ocaml -I +Printf

open Printf

let () =
    fprintf stderr "%s" "\x1b[31mHello\x1b[0m\n";;
