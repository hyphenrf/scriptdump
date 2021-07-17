type 'a node = [] | (::) of 'a * 'a list
 and 'a list = 'a node lazy_t

let rec append (lazy l) r =
  match l with
    | [] -> r
    | x::xs -> lazy (x::append xs r)

let rec take n (lazy xs) = lazy (
  match xs with
    | [] -> []
    | __ when n = 0 -> []
    | x::xs -> x::take (n-1) xs
  )

let rec drop n xs =
  match xs with
    | lazy [] as v -> v
    | xs when n = 0 -> xs
    | lazy (_::xs) -> drop (n-1) xs

let rec force (lazy xs) =
  match xs with
    | [] -> List.([])
    | x::xs -> List.(x::force xs)

let cycle xs =
  let rec x = lazy (Lazy.force_val @@ append xs x) in x

let xs = lazy(1::lazy(2::lazy(3::lazy [])))
  (*structure the type in a way that makes this work more naturally *)

let test1 = force @@ take 10 @@ cycle xs
let test2 = let ys = cycle xs in
  ys == drop 3 ys

