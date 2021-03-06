(* A monad is just a monoid in the category of endofunctors, what's the problem? *)
module type MONOID
= sig
  type m
  val  e : m
  val (+): m -> m -> m
end

module type MONAD
= sig
  type 'a m
  val pure: 'a -> 'a m
  val join: 'a m m -> 'a m
  val fmap: ('a -> 'b) -> 'a m -> 'b m
end

module MonoL (P: sig type t end): MONOID with type m = P.t list
= struct
  open List
  type m  = P.t list
  let  e  = []
  let (+) = append
end

module MonaL: MONAD with type 'a m = 'a list
= struct
  open List
  type 'a m = 'a list
  let pure = fun a -> [a]
  let join = concat
  let fmap = map
end


(* concrete monoids,
   a list's append and empty aren't really monadic, are they?
   they feel like more primitive building blocks *)
let _ = 
let open MonoL(struct type t = int end) in

let a0 = e + [1] = [1] + e && e + [1] = [1]    in
let a1 = [1] + ([2] + [3]) = ([1] + [2]) + [3] in
    assert (List.for_all Fun.id [a0;a1])


(* monads as monoids in the category of endofunctors (heh) *)
let _ = 
let open MonaL in

let a  = pure 1                                                  in
let a0 = join (pure a) = join (fmap pure a) && join (pure a) = a in
let a  = pure (pure a)                                           in
let a1 = join (join a) = join (fmap join a)                      in
    assert (List.for_all Fun.id [a0;a1])

