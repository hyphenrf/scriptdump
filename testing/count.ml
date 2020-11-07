open Printf

let rec countl xs =
  match xs with
  | [] -> 0
  | y::ys -> countl ys + 1

let countr xs = let rec count' acc ns =
  match ns with
  | [] -> acc
  | y::ys -> count' (acc+1) ys
  in count' 0 xs

let toy = List.init 1000000 (fun x -> x+1) 

let () =
  printf "%d\n" (countl toy); (*will overflow*)
  printf "%d\n" (countr toy);
