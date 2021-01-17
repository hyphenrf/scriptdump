
let main argv = let open Sys in
    set_signal sigint @@
        Signal_handle (
            fun _sig ->
                print_endline "\nWHY ARE YOU INTERRUPTING ME??";
                raise_notrace KeyboardInterrupt
        )
    ; while true do () done

let () = main Sys.argv
