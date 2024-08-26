main :: IO ()
main = do
    putStr "Enter a number: "
    n <- readLn
    -- Top half including middle line
    mapM_ (\i -> putStrLn (replicate (n - i - 1) ' ' ++ replicate (2 * i + 1) '*')) [0..n-1]
    -- Bottom half
    mapM_ (\i -> putStrLn (replicate (n - i - 1) ' ' ++ replicate (2 * i + 1) '*')) [n-2, n-3..0]

