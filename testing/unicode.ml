(*
 * unicode.ml
 * Trying to see how far OCaml supports unicode
 *)


(* let unicode…ident = 69 *) (* unicode identifiers are not allowed *)
let greetings = [ "Hello, world!"
                ; "¡Hola Mundo!"
                ; "Γειά σου Κόσμε!"
                ; "Привет мир!"
                ; "こんにちは世界！" ] (* unicode strings are fine *)

let print_list string_converter chan xs = 
    let rec aux = function
    | x::xs -> string_converter x ^ ";" ^ aux xs
    | [] -> ""
    in output_string chan ("[" ^ aux xs ^ "]")


let () = let open Printf in
    
    printf "%a\n" (print_list (sprintf "\"%s\"")) greetings;
    printf "%#x\n" (Obj.magic (List.nth greetings 3).[2]);
    (* should print 0x438 if it goes by rune, 0xd1 if it goes by byte *)
