(********

Since everyone and their mother took a turn on explaining what a monad is,
I wanted to join the party. sit tight.

Below this point I assume you're a programmer. Otherwise.. Are you lost?
Or worse..... Are you a mathematician?

Anyway.. You don't need to be familiar with functional programming ideas. You
need to know just the basics to hopefully understand this. Here goes..!


Monads, in the context of strongly typed programming languages, are a universe
in a box, and a set of governing functions specifically defined for it.

The box (the monad itself) can take inside of it any value.
Any value, even other monads.

The functions need not care what's the nature of the value inside the box.
That's an important bit. They act on the box itself and pass it around.
The only way to enter or exit* the boxed universe, or move from point a to b
inside of it, is via those functions. They are the laws that govern box-
universes. Example governing functions are "return" and "lift".

(the monadic ascended plane)    [value] -[lifted function]-> [new value] -> ...
                                 /          |
                       return __/     lift _|
                               /            |
(our mortal universe)    value          function

* in some contexts exiting is not allowed, or is the property of a comonad;
  we discuss this later.


So the idea is that you teleport your computations to a universe, manipulate
them with governing functions, and then get a result on the other side.


> That's dumb why would anyone do that

Remember, you were the one to define the rules of that universe, and you were
the one to define what kind of info boxes may carry. So, how the computations
behave is automatically customized to fit those rules and that info. This is
where monads can be powerful — you define your own control flow.
Monads aren't THE way, they're just another way to express control flow.. And
they happen to have their strengths and weaknesses.

For example, sequencing inside an error monad the computations a, b, c, d, e
where each of those could fail, would automatically propagate the error without
computing whatever comes after:

    value -[teleport-in]-> [a; b; c; d; e] -[teleport-out]-> value_or_error

without you necessarily writing error-handling code in any of a, b, c, d, e

The functions a..e might not be even aware of the monad. They may be lifted to
act in that universe. The teleport-in, teleport-out, and semicolon (;)!! are
the functions responsible for maintaining how this control's semantics work.

Any function, guised as an operator (like our smart semicolon) or not, that is
defined to compose computations inside a monad can take those three's place.
The idea is that an arbitrary function binds computations together and gives the
monad its characteristics on each binding point.
Some languages (Haskell, F#, ...) would even implicitly insert that "semicolon"
function for you so you don't have to think about it.

In case of the error monad, it does the error propagation.
In case of the option monad, it provides type-safe nullables.
In case of the sequence monad, it provides delayed computations for stuff like
iterators.
In case of the async monad, it provides asynchronous calls and promises.
In case of the [...] monad, it provides [...]

All the behaviours above may be vastly different, but the mechanism is identical
between them. You can implement them yourself without waiting for the compiler
to support them, And they'd still be *all type-safe*.

The language doesn't need to know or care about your semantics. There's no need
for special support of these features except for maybe optimizations carried
through the compiler internally for the more commonly used monads.

All the language needs to provide you is a nice, simple, consistent blueprint
to create your own tools. A blueprint that you can customize, compose, and
extend infinitely.


--------------------------------------------------------------------------------
Below this point is more implementation centric notes; I assume you know how to
read type signatures but not more than that. it's still newbie-friendly but now
with more Functional Jargon™

The simplest monad is the identity monad: m a (m is the box, a is the value)
And the functions that govern it:

    unit: a -> m a               (*1*) enter
    map:  (a -> b) -> m a -> m b (*2*) compute
    join: m m a -> m a           (*3*) compose
    get:  m a -> a               (*4*) leave

1* aka return, pure, wrap, box, point, ..., this is how we enter the universe.
   Alternatively in most functional languages a constructor can take this job.
2* aka <$>, fmap, ..., this is how we perform computations within the universe
   ..We lift functions to it.
3* aka flatten, concat, ..., this is what allows composition of computations,
   creating a pipeline.
4* aka extract, deconstructors.... usually not a function. Rather, a pattern 
   match takes that role. Some languages would have you not leave once you enter
   a monad, in the name of purity. Haskell is an example of that. Instead of
   leaving with possible state, you transform to the next monad, etc..  it's no
   big deal to focus on these details. Even haskell still has facilities for
   exiting: Comonads which are the inverse operations of a conventional monad in
   evil-twin fashion.

All monads inside all programs use functions similar in type signature to these
four. Remember, the customization of those functions is what gives different
monads different powers.

Examples of monads:
    - a List
    - a Tree
    - Result monad 
    - Option (aka Maybe) monad
    - Reader monad
    - Writer monad
    - State monad
    - IO monad
    - Async monad
    - ...

I leave it open to research how they're different and how the essence of their
definition is the same.

A note on functors and applicatives: they're less powerful than monads, thus
can be implemented with a subset of a monadic interface.
********)

(** The pure monad type template **)
module type MONAD = sig
    type 'a m
    
    val unit: 'a -> 'a m
    val fmap: ('a -> 'b) -> 'a m -> 'b m
    val join: 'a m m -> 'a m
end

module Identm: MONAD = struct
    (* The monad that does nothing. It isn't even boxed. *)
    type 'a m = 'a

    (* How to construct it *)
    let unit a = a

    (* How to compute on it *)
    let fmap f a = unit (f a)

    (* How to compose computations *)
    let join m = m
end

(* Totally useless extensions and functor play *)
module Syntax (M: MONAD) = struct
    (* example of "smart semicolons" *)
    let (|>*) m f = M.join (M.fmap f m) (* Haskell's >>= *)
    let (|>+) m f = M.fmap f m
end

module Const = struct
    (* A monad that's just boxed, nothing more. It's more practical to look at
     * how this one works though. *)
    module M = struct
        type 'a m = C of 'a
        let unit a = C a
        let fmap f (C a) = unit (f a)
        let join (C C a) = C a
    end
    module Syntax = Syntax(M)

    (* example of a composition *)
    let bind f m = M.join (M.fmap f m) (* check that out.. the good ol' bind *)
    let bind = Fun.flip Syntax.(|>*) (* wha'dya know, >>= is a flipped bind *)
end


(* totally useless demonstration *)
open Const.M
open Const.Syntax

let (%>) f g = fun x -> f (g x)
let () =
    5 |>  unit
      |>+ (+) 1
      |>* (unit %> (/) 18)
      |>  (fun (C x) -> x)
      |>  print_int
      |>  print_newline


(* Bonus *)
module List = struct
    (* Lists are just a monad, here it is :D *)
    type 'a m = Nil | Cons of 'a * 'a m

    let nil = Nil
    let cons a m = Cons(a, m)

    [@@@ warning "-8"] (* Can't be bothered to do those properly sorry *)
    let hd (Cons(a, _)) = a
    let tl (Cons(_, m)) = m
    [@@@ warning "+8"]
    
    let unit a = cons a nil

    let rec fmap f = function (* AKA map *)
        | Nil -> Nil
        | Cons (a, m) -> Cons(f a, fmap f m)

    let rec join = function (* AKA concat *)
        | Nil -> nil
        | Cons (a, m') -> append a (join m')

    and append l r =
        match l with
        | Nil -> r
        | Cons (a, l') -> cons a (append l' r)

    (* fun fact, a list's bind would be concat+map *)
    let bind f m = join (fmap f m)
end

module ListSyntax = Syntax(List) (* compiles because List implements MONAD *)
