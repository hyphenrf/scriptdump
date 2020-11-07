let id x = x

let encode n =
    if not (Uchar.is_valid n) then 
        raise(Invalid_argument((string_of_int n)^" is not a valid codepoint"))
    else
        let enc = Buffer.create 4 in
        Buffer.add_utf_8_uchar enc (Uchar.of_int n);
        Buffer.to_bytes enc |> Bytes.to_string


let () =
    try
      Printf.printf "%s\n" @@ encode @@ Scanf.scanf "%u" id
    with Scanf.Scan_failure s ->
             s |> String.split_on_char ':'
               |> (function [] -> ""
                  | x::xs as s -> String.concat "" 
                      (if x = "scanf" then xs else s))
               |> String.trim
               |> (^) "Error: "
               |> prerr_endline
       | Invalid_argument s -> 
               prerr_endline ("Error: "^s)
