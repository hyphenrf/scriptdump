type 'a node = [] | (::) of 'a * 'a list
 and 'a list = 'a node Lazy.t

let unwrap : 'a list -> 'a node = Lazy.force
let wrap   : 'a node -> 'a list = Lazy.from_val

let rec append l r =
  match unwrap l with
    | [] -> r
    | x::xs -> lazy (x::append xs r)

let rec take n xs = lazy begin
  match unwrap xs with
    | [] -> [] | _ when n = 0 -> []
    | x::xs -> x::take (n-1) xs
  end

let rec drop n zs = begin
  match unwrap zs with
    | [] -> zs | _ when n = 0 -> zs
    | _::xs -> drop (n-1) xs
  end

let rec force xs =
  match unwrap xs with
    | [] -> List.([])
    | x::xs -> List.(x::force xs)

let cycle xs =
  let rec x = lazy (unwrap @@ append xs x) in x

let (@) h t = wrap (h::t)

let xs = 1 @ 2 @ 3 @ lazy[]

let test1 = force @@ take 10 @@ cycle xs
let test2 = let ys = cycle xs in
  ys == drop 3 ys

