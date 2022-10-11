(* Binary Search Tree *)
type 'a t =
  | Leaf
  | Node of {v: 'a; left: 'a t; right: 'a t}
let fns = []

(* Naive *)
let rec preord = function
  | Leaf -> []
  | Node {v; left; right} -> v :: preord left @ preord right
let fns = preord :: fns

(* With accumulator *)
let preord t =
  let rec pre_acc acc = function
    | Leaf -> acc
    | Node {v; left; right} -> v :: (pre_acc (pre_acc acc right) left)
  in pre_acc [] t
let fns = preord :: fns

(* CPS *)
let preord t =
  let rec aux a t k =
    match t with
    | Leaf -> k a
    | Node {v; left; right} ->
        aux a right (fun a ->
        aux a left  (fun a ->
             k (v :: a)
        ))
  in aux [] t Fun.id
let fns = preord :: fns

(* Defunctionalization process, explained more precisely:

   1. write out the free variables of every continuation that you'd like to
      defunctionalize.

   2. give a unique name to every lambda expression, and replace every lambda
      expression with a constructor in an inductive type like so:
      type cont =
      | The_unique_name of (types of the free variables, k's type is cont)
      | ...

   3. write a function `apply` that turns `the_unique_name(...)` back into the
      lambda expression (with every inner lambda expression remaining a constr)

   4. replace every `k x` with `apply k x`, including in the definition of
      `apply` itself
*)

(*
   continuations:
   K1 - (x @{} -> x); no free variables captured
   K2 - (a @{v, left, k} -> aux a left (<K3>))
   K3 - (a @{v, k} -> k (v :: a))
*)
type 'a cont =
  | K1
  | K2 of 'a * 'a t * 'a cont
  | K3 of 'a * 'a cont

let preord t =
  let rec apply = function
    | K1          -> fun x -> x
    | K2(v, t, k) -> fun a -> aux a t (K3(v, k))
    | K3(v, k)    -> fun a -> apply k (v::a)
  and aux a t k =
    match t with
    | Leaf -> apply k a
    | Node {v; left; right} ->
        aux a right (K2(v, left, k))
  in aux [] t K1
let fns = preord :: fns


let test = Node { v = 5;
  left = Node { v = 3;
    left = Node { v = 6;
      left = Leaf;
      right = Node { v = 2; left = Leaf; right = Leaf };
    };
    right = Leaf;
  };
  right = Node { v = 0;
    left = Leaf;
    right = Node { v = 1; left = Leaf; right = Leaf };
  };
}

let default = List.(hd @@ rev fns) (* naive *)

let _main =
  fns |> List.map     ((|>)test)
      |> List.for_all ((=)(default test))
      |> fun b -> assert b
