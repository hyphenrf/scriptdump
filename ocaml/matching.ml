type chartype = U | L | N | S | X

let type_of_char c = match c with
    | 'A'..'Z' -> U
    | 'a'..'z' -> L
    | '0'..'9' -> N
    | ' '|'\t' -> S
    |  _       -> X

let () =
    ignore (type_of_char '9');
    ignore (type_of_char ' ');
    ignore (type_of_char 'a');
    ignore (type_of_char 'S');
    ignore (type_of_char 'd');
    ignore (type_of_char '	')
