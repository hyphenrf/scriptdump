let rec perm = function
  | [] -> []
  | [x] -> [[x]]
  | xs -> 
    let rec aux i ls =
      let (l,r) = splitat i ls in
      match r with
      | [] -> []
      | h::r_ ->
        let rest = l @ r_ in
        (* Avoid stack overflows by using rev versions of both append and map.
         * They cancel each other. *)
        let map, cons, (@) = List.(rev_map, cons, rev_append) in
            map (cons h) (perm rest) @ aux (i+1) ls
    in aux 0 xs

and splitat n xs = take n xs, drop n xs

and drop n = function
  | [] -> []
  | xs when n = 0 -> xs
  | x::xs -> drop (n-1) xs

and take n = function
  | [] -> []
  | _  when n = 0 -> []
  | x::xs -> x :: take (n-1) xs
