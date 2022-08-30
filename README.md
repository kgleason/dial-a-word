# Dial A Word
This script was inspired by an article in 2600 39:2 by N1xis10t. The formatting of the published script had some formatting issues, and I was never able to run it successfully as it was published. I made some guesses at what should be indented where, and I ended up with something that ran, but it felt really slow. It could very well be because of my decisions about the scoping.

In any case, it seemed like an interesting idea. So I took a stab at making something that approached the problem from a different perspective. In this case, the envisioned use case is one where you have a list of phone numbers, and you want to see what words may be in it. It runs perfectly fine with just a single number, but you can pass in multiple numbers as well.

For a test case, I used an 800 number that used to be quite prominent because it had multiple words in it.


   ```bash
   python dial-a-word.py -n "8003569377,8003568378" -u "https://raw.githubusercontent.com/first20hours/google-10000-english/master/google-10000-english-usa.txt"

   8003569377 , LOWER, 8003LOWER7
   8003569377 , FLOWERS, 800FLOWERS
   8003569377 , FLOW, 800FLOW377
   8003569377 , FLOWER, 800FLOWER7
   8003569377 , MYERS, 80035MYERS
   8003569377 , FLOYD, 800FLOYD77
   8003568378 , OVER, 80035OVER8
   8003568378 , LOVE, 8003LOVE78
   8003568378 , TEST, 800356TEST
   8003568378 , LOVES, 8003LOVES8
   8003568378 , LOVER, 8003LOVER8
   8003568378 , LOUD, 8003LOUD78

   ```

On my system (2020 M1 13" MacBookPro 16GB RAM), the execution above took 0.05s of actual users time.

With a file of 1936 phone numbers, calling the script like this: `time python dial-a-word.py -n $(paste -s -d"," Numbers.txt) -x 10 -u "https://raw.githubusercontent.com/first20hours/google-10000-english/master/google-10000-english-usa.txt" > output` took just under 9 seconds, and produced 1494 matches.
