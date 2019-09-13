#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) This is just a single loop , and I believe it's O(n) because of that. The size of n doesn't really matter.


b) This will be O(n^2) because of the nested loops. While is nested inside the for loop.


c) We have some recursion going on. I don't think the 2 in the return statement has anything to do with the runtime because it's not going to be used in bunnyEars when it runs again. I'd say it's O(n log n) where the first n is the initial amount of times you want to run bunnyEars (example bunnyEars(4)), and the log n part because of the recursion.

## Exercise II

I'm assuming that there isn't a difference between an egg that's thrown and an
egg thats dropped, it's going to break either way. So we have a building, lets
say 4 stories high with for example eggs that are dropped off floors two or more
break. According to the problem, eggs that would be dropped off of
say floor one wouldn't be broken.Eggs that are dropped off of floor two or
higher would be. They want us to determine what floor f is using the least
amount of eggs. 

What I want to do is just start from the bottom and drop eggs
until they break, then you'd have floor f. The better way to do it would be to split the building in half, so in my
example, you'd take the four floor building, break it in half. You'd have floors
3 and 4, and 1 and 2. You drop an egg off 2 and you drop an egg off 4. These
would be the highest floors in each new set of buildings. All you'd look for is
eggs that don't break, because you know that if an egg doesn't break, the floor
will always be higher than it. Whereas if an egg does break, you don't know if
the floor is higher or lower than that floor. For example, if we have a building
with 10 floors, and the egg doesn't break on floor 5. It's also not going to
break on floors 1,2,3,4,5. If we throw an egg and it breaks on floor 8, we don't
know if it breaks on 6 or 7. 

Basically you want to split the array in half (list of floors), throw an egg
from the max value of each of the two new arrays, see if it breaks or doesn't
break in the highest value of the lower array. So you have an array of 10,
divide by 2, check if it breaks in 5. If it does break you know 5-10 are out. So
now you have 0-4, divide and check again. It doesn't break on four. Then you
know the floor is four.  

You could probably get this to O(n log n) using recursion. The exit condition
would be when you find the floor where it doesn't break, and then the floor
above it breaks.
