(*inline is one of many ocaml attributes*)
(*see: http://caml.inria.fr/pub/docs/manual-ocaml/attributes.html*)
let id x = x
    [@@inline]

let () = print_endline @@ (id[@inlined]) "Hello"
(* Errors if not inlined --------^ *)
