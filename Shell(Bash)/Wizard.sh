#!/bin/bash

###

# So basically, I wanted to make this game a long time ago.And I only got around to it just now.
# The game is about The Wizard who wonders around the wonderful land. he overcomes a lot of obstacles 
# You're going to take care of The Wizard and make his choices for him.
# Or you may choose to  mischief and play games with The Wizard and basically kill him

# The game is written in bash, so I had limited features. But I went all out, 
# and I always want to add features and renew the game.
###




### greetings.

read -rep "Welcome, Hero! " manual_0
read -rep 'I am so happy to see you here again ! ' manual_1
read -rep '' manual_1
read -rep '' manual_1
read -rep '' manual_1
read -rep '' manual_1
read -rep '' manual_1




read -rep "So, What is your choice ? 
    Are you are not brave enough ? " first_step
case $first_step in
OK|ok)

;;

NO|no)

;;

*)
echo 'you chicken ! '
exit
;;
esac

echo -en 'Once upon a time, there was a great wizard.
the wizard would have traveled along the woods and the mountains.'
read -r woke_up
echo
echo 'One day in one of his walks the wizard found a mangeta lizard ! '
read -r lizard
read -rep "Continue? "  answer
echo "${answer}"

