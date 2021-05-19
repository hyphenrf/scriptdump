(*
   Haskell's applicative solution for palindromic lists goes like this:
   palindrome = (==) <*> reverse
   in which <*> :: ([a] -> [a] -> Bool) -> ([a] -> [a]) -> [a] -> Bool

   or the more general type:
      (a -> b -> c) -> (a -> b) -> a -> c

   This type is possible thanks to Haskell's type-instance Applicative ((->) r)
   in which arrows are treated as constructors. We'll have to make our own here
   probably...

   this file's job is to find a way in ocaml to equate
      (a -> b -> c) -> (a -> b) -> a -> c
   to
      Applicative p => p (x -> y) -> p x -> p y
*)

module type Functor = sig
  type 'a t
  val fmap : ('a -> 'b) -> 'a t -> 'b t
end

module type Applicative = sig
  include Functor
  val pure    : 'a -> 'a t
  val ( <*> ) : ('a -> 'b) t -> 'a t -> 'b t
end

(*
   first let's try and morph the arrows in the second form to mimic the first form

   (a -> (b -> c)) -> (a -> b) -> (a -> c)
   x t = (a -> x)
   (b -> c) t -> b t -> c t                  (* looks correct *)

   so what we need is a type function that takes x t and returns (a -> x) t
   but how do we express this in ocaml? where would x t = (a -> x) fit?

   comes second, ocaml's type system wrestling...
*)

module AppF (R:sig type r end): Applicative with type 'a t = R.r -> 'a
= struct
  type 'a t = R.r -> 'a
  let fmap f g  = fun x -> f (g x)
  let pure x    = fun _ -> x
  let (<*>) f g = fun x -> f x (g x)
end

(*
   because ((->)r) is a type constructor parametrised with an additional r, we
   need r from outside and 'a for Applicative.t defined. We use a functor for r.
   We also need `with type ...` to expose our abstract Applicative type's
   specification for this instance to the outside world
*)


(*
  an explicit (type a) is a locally abstract existentially quantified typevar
  introduced for the functor instantiation.
  to my understanding, this shouldn't act like higher rank polymorphism. Why
  does it act like higher rank polymorphism? Beats me. Perhaps this is value
  restriction kicking in.
  to give this function universally quantified polymorphism, we need to
  eta-expand it. Although expansion defeats the purpose of (<*>) combinator.
  Luckily there's another way to keep it pointfree: objects and records.
*)

let o = object
  method palindrome: type a. a list -> bool =
     let open AppF (struct type r = a list end) in
         (=) <*> List.rev
end


let () = ()
  ; Printf.printf "%b\n" (o#palindrome ['m';'o';'m'])
  ; Printf.printf "%b\n" (o#palindrome [1;2;3])
  ; Printf.printf "%b\n" (o#palindrome [1])
  ; Printf.printf "%b\n" (o#palindrome [])

(*
  Veridict:
    - typeclasses are equivalent to ML signatures (both are an interface)
    - instances are modules
    - parametrised instances are parametrised modules aka functors
    - ocaml doesn't have a type-level solver like that of haskell, which is why
      we need to be explicit about our type relationships
    - ocaml's functions can't afford to be "oblivious" about the modules they
      handle (as long as the compiler doesn't support modular implicits), so we
      must explicitly state the correct relationships between types and
      "typeclases"
    - implicit typeclass resolution may explode compile times and increases
      compiler complexity on the flip side.. Although a language that has
      typeclasses but not ML modules may be less complex tbh.
    - also on the flip side: for each type there can only be one typeclass
      instance defined. this isn't an issue when you're explicit and limited to
      a scope instead of having classes pervasively. Modules are more powerful.
    - ocaml programs tends towards direct-style helper functions on call site
      instead of too many abstractions and design pattern hiearchies, or even
      just resolving the extra general lifta2 function to its local callsite
      implementation:
        let palindrome xs = List.rev xs = xs
*)
