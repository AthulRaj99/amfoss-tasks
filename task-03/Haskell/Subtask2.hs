import System.IO

main = do
    -- Read the content of "input.txt" into a variable called "content"
    content <- readFile "input.txt"
    
    -- Write the content into the file "output.txt"
    writeFile "output.txt" content

