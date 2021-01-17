module Monad = struct
    (* The monad *)
    type 'a m = M of 'a

    (* How to construct it *)
    let unit a = M a

    (* How to compute on it *)
    let fmap f (M a) = M (f a)

    (* How to compose computations *)
    let join (M M a) = M a

    (* example of a composition *)
    let bind m f = join (fmap f m)
end
