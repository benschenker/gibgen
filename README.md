**Code Challenge: Gibberish Generator**
---------------------------------------

Challenge Overview
------------------

**Your response to this challenge can be used to supplement your SWEAP application.  If you plan to complete this challenge for SWEAP, ensure you meet the other minimum requirements by visiting [here](http://gecapital.com/sweap "SWEAP Home Page").  Whether you apply or not, you are welcome to fork this repository and complete as a personal project challenge.**


We are exticed taht you are intsereted in joiinng the Soawtfre Engreeniing Appsecitnerhip Prargom.  Weoclme to yuor fsrit prommarging chanellge.  Yuor chnellage is to courtsnct a prrgoam taht tekas an Enilgsh txet snirtg as iupnt and rerutns rebadale giirebbsh lkie tihs.  It dseno’t mtaetr in waht oerdr the ltteres in a wrod are, but an iproamtnt tihng is taht the frsit and lsat ltteer be in the rghit pclae. The rset can be a taotl mses and you can sitll raed it whotuit a pboerlm.  Tihs is bcuseae the huamn mnid deos not raed ervey lteter by istlef, but the wrod as a wlohe.

**The Basics:**
  
  - You may use *almost any* programming language... it's your choice.  See the supported options [here](http://ideone.com/).
  - Your program should leave the first and last letter of each word in place and scramble the rest.
  - Your program should not scamble punctuation (.,-'...etc.), numbers, or upper-case abbreviations.
  - For example gibberish, see the [/textfiles](https://github.com/sweap/gibgen/tree/master/textfiles) folder.  Two sample output files are provided: `xxx.txt.gib`

**Input/Output:**
 
  - Name your program as follows: `gibgen.xx` (where xx is variable based on the language you choose)
  - Your program should be able to read text input from a string passed into STDIN
      - `gibgen.xx "This is a String"`
      - `cat mystringfile.txt | gibgen.xx`
  - Your program should output to the console.

_Note: This challenge is based on a popular word gibberish meme. You can improve the readability by looking at a [researcher's take](http://www.mrc-cbu.cam.ac.uk/people/matt.davis/cmabridge/) on the truths/myths of this meme, but this is not required._

What to do
----------
1. [Download](http://git-scm.com/downloads) & install Git on your machine

2. <a href="https://github.com/sweap/gibgen/fork" class="btn grouped" data-method="POST" rel="nofollow" title="Fork">Fork</a> this project - Go [here](https://github.com/sweap/gibgen) and click the "Fork" button (located on the upper-right side of the screen)

2. Clone your new fork'd repository to your local machine - `git clone https://github.com/YOUR_USERNAME_HERE/gibgen.git`
3. Complete the code challenge and fill out the Quick Start & Questions in the the README (see below)
4. `git add` and `git commit` your local repository as you go
4. Push your code and README back to GitHub occasionally - `git push origin master`
5. Email [serp@ge.com](mailto:serp@ge.com) with the Commit URL to your fork'd repository that you want reviewed. It should include at least 2 files: (1) your updated README with Coding Questions answered, and (2) your program (gibgen.xx)
   - Go here: `https://github.com/YOUR_USERNAME_HERE/gibgen/commits/master`
   - Find the commit that you'd like us to review.  _The commit date must be on or before 11:59pm (central) on April 4, 2014!_
       - Click the "Browse Code ->" link for that commit
   - Copy and paste the URL into the email along with your name... it should look something like this:
       - `https://github.com/YOUR_USERNAME_HERE/gibgen/tree/73afe0c8fe2...hash.hash...e80afea72b6`

_Note: If you have any questions, email [serp@ge.com](mailto:serp@ge.com).  I will do my best to respond to any questions._

Judging Criteria
----------------

Your responses to the **Coding Questions** at the bottom of this README are the *Most Important* part of this challenge. A working, fully fault-tolerant program that we just can't break, albeit awesome, is the least important.  Why is that?  Remember, we don't expect you to be expert programmers (just yet)... We want to see how you think through a problem.  


For completion by applicant
===========================

Quick Start
-----------
To run this program you must have [python 2.7.6](https://www.python.org/download/releases/2.7.6/) installed on your computer.  

It will accept input as an argument or as STDIN
- 'python2 gibgen.py "This is a String"'
- 'cat mystringfile.txt | python2 gibgen.py'

This was written in Python 2.7.6

This implementation works well for all cases that I tried except when two separate words are separated only by a special character (e.g. hyphen), where it treats that as one word.  


Coding Questions
----------------

Question 1: "How did you approach the problem?" (500 words or less)

I approached the project at hand through a simplify-complicate strategy.  While the problem seemed trivial at first, I began to realize that the devil was in the details – the punctuation, the spaces, the first and last letters of each word, etc.  So I first simplified the problem to the base case – scrambling only the middle letters in a word while avoiding the first and last.  Once I worked out how to solve that I introduced the required complications one at a time until my solution fit the whole problem.  


Question 2: "What was the most difficult aspect of the solution?" (500 words or less)

The most difficult part of the solution was making sure that the punctuation within or around words would not become scrambled.    I started the problem by solving the simple case without having to do much work on the character level: I removed the first and last characters of a “word”, mixed up the rest, and put it all back together.  This actually worked quite well and was very simple but was not nearly robust enough to deal with punctuation.  After a bit of thought I realized that I just needed to generalize my existing solution: first filter out the characters that would need jumbling and then jumble them in place.  Once I did this the rest of the solution  came together quickly.  