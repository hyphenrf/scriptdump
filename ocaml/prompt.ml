(* prompt.ml
 * Copyright (C) 2020 devel <hyphens@pm.me> *)


open Unix
 
type mode = Prompt | Input
 
let original_mode = tcgetattr stdin
let set = function
  | Prompt -> tcsetattr stdin TCSAFLUSH {original_mode with c_icanon = false}
  | Input -> tcsetattr stdin TCSAFLUSH original_mode
 
let getchar buf = 
    if read stdin buf 0 1 = 0 then raise End_of_file
    else Bytes.get buf 0
 

let _main =
  let buf = Bytes.create 1 in
  let rec prompt () =
      print_string "Prompt? [Y/N]: ";
      flush_all();
      set Prompt;
      match getchar buf with
      | 'n'|'N' -> ();
      | 'y'|'Y' -> print_endline ": Ok."; prompt ();
      | _ -> print_endline ": Invalid."; prompt ();
      set Input;
  in
  prompt ()
