let ( .%[] )   = Bytes.get
let ( .%[]<- ) = Bytes.set

let () =
    let h = Bytes.of_string "HYPHEN" in
    print_char h.%[3]; print_newline ();
    h.%[3] <- 'P';
    print_char h.%[3]; print_newline ();
    print_endline @@ Bytes.to_string h
