function ansi(n)
    return function(s)
        return string.format("\x1b[%dm%s", n, s)
    end
end

function reset(s)
    return s.."\x1b[0m"
end

black = ansi(30)
red = ansi(31)
green = ansi(32)
yellow = ansi(33)
blue = ansi(34)
magenta = ansi(35)
cyan = ansi(36)
grey = ansi(37)

