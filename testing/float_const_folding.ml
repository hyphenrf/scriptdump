let ( *** ) f g = fun x -> f (g x)
let print_bool = print_string *** string_of_bool

let a = 0.1
let b = 0.2
let c = a +. b = 0.3

let d = 0.1 +. 0.2 = 0.3
(* OCaml does not fold float constants like C++ or D *)

let () =
    print_bool c; print_newline ();
    print_bool d; print_newline ();
