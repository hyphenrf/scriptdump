let print_bool n = 
    if n
    then print_string "true"
    else print_string "false"

module List = struct
    include List
    (* try blocks are obsolete.. SINCE 4.02 WE CAN MATCH ON EXNS !! :D *)
    let hdo l = match hd l with
        | exception _ -> None
        | a -> Some a
end

let () = 
    print_int @@ Option.get @@ List.hdo [1;2;3;4];
    print_bool @@ Option.is_none @@ List.hdo [];
    print_newline ()
    
(* The benefit is: better TCO
 * 
 * in a recursive call, if the function is wrapped in try...with block, it
 * cannot be TCO'd.
 *
 * a common solution was:
 *     let rec f x = match begin
 *         try Some x 
 *         with _ -> None
 *     end with
 *     | Some x -> f x
 *     | None   -> x
 * which is admittedly clunky as hell and creates an intermediate wrapper type.
 *
 * This eliminates both issues and is the recommended de facto standard now.
 *)
