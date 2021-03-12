
let main = let open Sys in
  catch_break true; (* The important bit here *)
  try
    while true do () done
  with
    Break -> print_endline "\nWHY ARE YOU INTERRUPTING ME??"
