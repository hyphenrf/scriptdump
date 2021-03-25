type (_,_) eq = Refl: ('a, 'a) eq

let refl: type a. (a, a) eq
  = Refl
let symm: type a b. (a, b) eq -> (b, a) eq
  = fun Refl -> Refl
let trans: type a b c. (a, b) eq -> (b, c) eq -> (a, c) eq
  = fun Refl Refl -> Refl
