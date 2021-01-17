type record = { mutable dirs: int
              ; mutable fils: int
              ; mutable depth: int }

let r = { dirs = 0; fils = 0; depth = 0 }

let pipe   = "\u{2502}   "
let empty  = "    "
let branch = "\u{251C}\u{2500}\u{2500} "
let corner = "\u{2514}\u{2500}\u{2500} "

let rec descend ?(prefix="") ?(depth=1) dir = if depth > r.depth then ()
  else
    let depth = succ depth in
    let nodes = Sys.readdir dir in
        nodes |> Array.fast_sort String.compare;
        nodes |> Array.iteri
          (fun i node -> if node.[0] <> '.' then
               let rpath = Filename.concat dir node in
               let isdir = Sys.is_directory rpath in
               let pad, pre = if i = Array.length nodes - 1
                   then empty, corner
                   else pipe,  branch
               in
                   print_endline(prefix ^ pre ^ node);
                   if isdir then (
                      descend ~prefix:(prefix ^ pad) ~depth rpath;
                      r.dirs <- r.dirs + 1
                   ) else
                      r.fils <- r.fils + 1
          )

let _main =
  let argc, argv = Array.length Sys.argv, Sys.argv in
  let root, dir = if argc < 2 then ".", Sys.getcwd () else argv.(1), argv.(1) in
    r.depth <- 2;
  print_endline root;
  descend dir;
  print_endline
    ( "\n" ^
      string_of_int r.dirs ^ " director" ^ if r.dirs = 1 then "y, " else "ies, " ^
      string_of_int r.fils ^ " fil" ^      if r.fils = 1 then "e"   else "es"    )
