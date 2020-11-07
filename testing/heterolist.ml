(* Type fuckery *)

module HetList = 
struct

  type ('ty,'v) t =
    | [] : ('v, 'v) t
    | (::) : 'a * ('ty, 'v) t -> ('a -> 'ty, 'v) t

  let empty = []
  let return x = [x]
  let cons x l = x :: l

  let hd
    : type a ty v.
      (a -> ty, v) t -> a
    = function
      | [] -> failwith "hd on empty list"
      | x::_ -> x
  let tl
    : type a ty v.
      (a -> ty, v) t -> (ty, v) t
    = function
      | [] -> failwith "tl on empty list"
      | _::xs -> xs

  let rec append
    : type a b c.
      (a, b) t ->
      (b, c) t ->
      (a, c) t
    = fun l1 l2 -> match l1 with
      | [] -> l2
      | h :: t -> h :: append t l2
end 
