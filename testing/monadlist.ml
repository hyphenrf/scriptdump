let flip f = fun x y -> f y x
let (=<<) = List.concat_map
let (>>=) = fun f mx -> flip List.concat_map f mx (* Need to Eta-expand *)
