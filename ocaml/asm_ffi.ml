(* asm_ffi.ml
 * nasm -felf64 asm_ffi_stub.S &&
   ocamlfind opt -package unix -linkpkg asm_ffi.ml asm_ffi_stub.o -o asm;
   rmf -rf *.cm? *.o *)


external maxfast: int -> int -> int = "max"
    [@@immediate][@@noalloc]

let time comp =
    let start = Unix.time() in
        comp ();
    let endtm = Unix.time() in
        endtm -. start

let wrap f x = fun () -> f x

let test1 n =
    for i = 0 to n do
        ignore(max i (i-1))
    done

let test2 n =
    for i = 0 to n do
        ignore(maxfast i (i-1))
    done

let _main =
    print_float @@ time @@ wrap test1 500_000_000; print_newline ();
    print_float @@ time @@ wrap test2 500_000_000; print_newline ();
