(* 64Kx16: word addressable 16-bit arch, like a typical Forth *)
let s = Bytes.create (2 lsl 16)

let sp = ref 0

let push n = Bytes.set_int16_ne s !sp n; sp := !sp + 2
let peek _ = Bytes.get_int16_ne s (!sp-2)
let pop  _ = let out = peek() in
    sp := !sp - 2; Bytes.set_int16_ne s !sp 0;
    out

let ws = Str.regexp "[\t\r\n ]+"
let nl = Str.regexp "^[+-]?[0-9]+$"

let printf = Printf.printf

let rec loop () =
    print_string "RPN> "
    |> read_line
    |> Str.split ws
    |> List.iter (function
         | "+" -> binop ( + )
         | "-" -> binop ( - )
         | "*" -> binop ( * )
         | "/" -> binop ( / )
         | "." -> printf "%d\n%!" (pop ())
         | "=" -> printf "%d\n%!" (peek())
         | "?" -> printf "Stack Pointer: %d\nStack: %S\n%!"
                         !sp (Bytes.sub_string s 0 32)
         | s when Str.string_match nl s 0 -> push (int_of_string s)
         | any -> ()
       )
    |> loop
and binop f = let n = pop () in
    push @@ f (pop()) n

let () = loop ()
