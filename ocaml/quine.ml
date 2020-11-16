(* let rec quine s = quine @@ (fun p -> Printf.sprintf p (string_of_format p)) *)
(* "let rec quine s = quine @@ (fun p -> Printf.sprintf p (string_of_format p))\n%S" *)

(fun p->Printf.printf p(string_of_format p))"(fun p->Printf.printf p(string_of_format p))%S;;";;
