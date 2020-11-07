let incr ?(option_arg=1) a = a + option_arg

let () =
    ignore(incr 5);

    let option_arg = 2 in (* notice how if the name and arg match you can reduce
                             the ~arg:name to ~arg *)
    ignore(incr 5 ~option_arg);
