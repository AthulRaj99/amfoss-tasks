import System.IO (readFile, writeFile)

main :: IO ()
main = do
    content <- readFile "input.txt"  -- Read the input file
    let n = read content :: Int  -- Convert content to integer

    let diamond = unlines [ replicate (n - i - 1) ' ' ++ replicate (2 * i + 1) '*' | i <- [0..n-1] ]
                   ++ unlines [ replicate (n - i - 1) ' ' ++ replicate (2 * i + 1) '*' | i <- reverse [0..n-2] ]

    writeFile "output.txt" diamond  -- Write the diamond pattern to output file

