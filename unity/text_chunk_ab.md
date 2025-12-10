offset.
This is going to be a floating point variable that we can adjust in the inspector so that we can determine how far out we want our feet to be kind of at runtime in the editor and not have to guess in code.
So, this is going to give us a foot offset and we'll generate a serialized field for it by hitting alt enter and choosing generate field.
Oh, it didn't give me the serialize option.
That's okay.
We'll generate a field.
Hit F12 and then go add the serialized field attribute.
I'm going to do that over the private keyword.
So double click the private keyword, hit the square brace, type in serialize field, just enter and close brace.
I want to move this line up.
So I'm going to cut it and put it right here below the layer mask.
I'll add in an extra line here, too, so we have some space and clean that up a little bit.
All right, I think we're also going to delete out this default sprite on line 18.
While we're up here, let's hit control X or shift delete and get rid of that line because we're no longer using it.
Remember, our animator is controlling that.
That also means that we need to get rid of line 26 that was assigning that.
It's always good to delete extra code when you're not using it so that it doesn't confuse you later.
And it's important to note that when it was grayed out like that, this light gray, it means it's not used.
So, we can probably delete it.
Most code editors will catch Unity stuff and tell you whether or not it's used now.
And that was a good usage for it.
Okay.
So, we've got our foot offset now created.
We need to give it a default value.
I'm going to give it a 0.5.
So half a meter out each way seems like a a good value.
And then we're going to go back down to our draw gizmos and let's do the right foot.
So this should draw our left foot.
In fact, let's add a comment here.
Right after or before line 36, we'll do a double forward slashdraw left foot.
And then I'm going to select all of line 36 through 38.
And again control or command D.
Hit the left arrow and enter.
Enter again.
And this will be draw right foot.
So draw right foot is going to be exactly the same as draw left foot, but instead of subtracting our foot offset, we will add to our foot offset.
And that's because the bottom left or the left side of the screen is like 0 0 and the right side, the numbers go up.
As you go to the right of the screen, the numbers go up.
As you go to the left, they go down into the the negatives and so on.
So we've got draw right foot and draw left foot.
Let's save, go to Unity, and see if our feet are now drawing.
We should expect to see three red lines, one in the center, one off to the left, and one off to the right along with a variable here that we can modify for the foot offset.
So, I go to my player and take a look at that.
I've got three feet or three lines drawing and a variable.
I can drag this variable in and get it to oh, what's a good val value? It's a little hard to do dragging.
How about a point three somewhere right around there so it's just outside the feet.
Give myself a little bit of extra room.
And I think we're so far doing so good.
Right now we're not using these values though, but let's save and uh run around and just make sure that it looks okay.
Then I think in the next section we'll start using these in our raycast.
So we run around.
Looks good so far.
I'm going to put my game view down here, dock it, and go double click on my player.
And then let's just I just want to see what they look like when we're animating.
Seems good.
Okay, so far I think it's pretty good.
Let's stop and pause right here.
go to the player because I got myself kind of hung there.
And you can see right here, I would not be able to jump.
My player's not grounded.
So, I'm thinking maybe I need to pull out this foot offset just a little bit more.
Maybe like a 0.35 and then I would be able to jump.
So, then I can jump when I'm still pretty pretty far down.
But remember, our check isn't actually doing that right now.
So, let's stop playing.
I'm going to save off that value of a 35 for our foot offset.
Save our scene.
go to our plastic window, say we added gizmos for left and right foot grounding, and we'll check in our changes.
Now that our raycast gizmos are drawing for the left and right foot, we need to hook them up so that they're actually used in our code because drawing them in gizmos is just for visualization and debugging.
It doesn't actually affect gameplay.
To do that, we're going to open up our player script again.
We're going to go find the part where we do our grounding, which is actually right at the beginning of update.
We have lines 48 through 53 that do all of the grounding checks.
And the first thing that I want to do, and this is, I think, a very important step and a very important phase of development, is refactor or extract this little bit of code.
If you look at our update method, right now, we do a lot of grounding stuff.
We do some input stuff, and then down here at the bottom, we do the sprite stuff.
And we've already extracted out that update sprite method that handles all of our sprite stuff.
So why not do the same for our grounding? Let's take our bit of grounding code and we'll extract this out into a new method that we'll call update grounding.
So I'm going to select all of the code from 48 to 53.
Hit alt enter and choose extract method.
And then we'll name this method update grounding.
Now if you had a hard time doing that, you can also just copy and paste all of that code.
Cut it all.
Make a method named void update grounding.
You don't need the private keyword.
And then paste the code inside of there.
Just like this.
And then call the update grounding with a semicolon right here at the beginning of the update.
Now I don't have to look at this entire update method.
I just have to look at this update grounding method for our ground updates.
It makes it a lot easier for me to kind of comprehend what I'm looking at all of the code and to reason about it without having to see all of the extra stuff.
In fact, I can even collapse down this update sprite.
And I'm going to get rid of that private keyword while we're at it.
So, in our update grounding method, right now, we do a check from the center.
That's we get our origin.
We use our position X, which is the center of our character's X position, and then we get the bottom part of our character's Y, by using the center, and then subtracting the extents of the sprite renderer.
So, basically half the height of the sprite renderer to give us the bottom of our character.
So, we need to now get a position that's off to the left and the right by foot position and check those as well.
So, to do that, we're going to make a couple minor minor changes to well, I guess they're not that minor of changes.
The first thing that we're going to do is remove this else statement.
We're going to kind of do three if checks.
And we don't want to do else if, else if, else.
It'll get very confusing.
So, we're going to delete out line 72 and we're going to cut line 73.
Take line 73, put it on the clipboard, shift delete or control X, move it right up to the top on line 68.
So now at the beginning of every frame, we're going to set is grounded to false.
Don't worry though, because before anything else can process it.
If we are grounded, we'll set it right back to true.
Nothing will even know that it was changed.
So on line 68, we'll set is grounded to false.
And then we'll check to see if everything is good in the center.
I'm going to save this off.
And we're just going to make sure that nothing has broken, everything still works.
We should have changed zero functionality yet and everything should be the same.
It's always important when you refactor to test things, make sure that it all still works before you actually dive in and um start making changes.
So, we want to make sure that it works with the refactor first.
All right.
So, we jump in.
I want to make sure that my layers still correct.
My player is set to the correct layer.
The layer mask is still correct.
Missing the player.
And I should be able to jump but still not see those two left and right feet.
Let's make sure that that works.
Well, I can see them but not use the left and right feet to jump.
So, I can jump.
Looks good.
And then if I jump up on this other platform, I can't keep jumping.
Yep, looks all right.
Seems okay.
And I can't double or triple jump or anything like that.
Okay.
So, we'll stop playing.
Let's go back into the code and now hook it up.
Hook up our new part.
So, instead of just checking the center, we want to check the left and the right as well.
Let's add a comment here on line 70.
Check center.
And then let's do the same down here.
We'll go check left on line 76.
And I'm going to copy lines 71 all the way through 74.
Then we'll paste them after 76.
And then we've got a couple of issues.
We've got two errors here.
Now, if you remember what the cause of these errors is, awesome.
Please just go ahead and fix it right now before I even tell you how to fix it.
If you don't remember, don't worry.
I'm going to explain it again.
So what happens here is that origin is defined on line 71.
So we can't redefine the origin variable.
We can however reassign it by just getting rid of that part that's defining it or the class type or the basically the type that you wanted to define it as.
The part that was in that nice little light blue.
We get rid of that and it'll the error will go away.
The same is true for line 78.
And by the way, we're here we're using a word var.
This could also say raycast hit 2D.
It's exactly the same.
Var is just shorter and it autocompleted.
But it's still going to be an issue because we can't redefine it.
We have to just remove that completely.
And we could put raycast 2D up here if we wanted to.
Raycast hit 2D like that.
So that'll give us a another copy of our check, but it doesn't actually check against the left position.
Remember in our gizmos, we're just subtracting the foot offset to get a left position.
So I just take this minus foot offset, hit Ctrl + C, go down to the end of our position X, and paste it in.
So now we're going to have a check that's off to the left of our foot offset or subtracted our foot offset, which is like 35 to the left.
Now select this checked left part from line 76 all the way to the end of 80.
Again, control or command D.
Hit the left arrow, enter, enter.
Get some new lines.
And let's replace the word left here with right.
And then let's make it actually check the right by instead of going to the left or subtracting our foot offset, we will add our foot offset.
So we'll hit plus.
And now we should be checking in the center right here.
That's this position right here.
Transform position X.
Off to the left, which is our position X minus.35 or I think it's 0.35 that we have.
And then to the right, which is plus.35.
If any of those returns back a hit, we will say that they're grounded.
Now, there are a couple of things going on here that are not the most inefficient.
For instance, if we hit in the center, we probably don't need to check the left and the right.
We could probably bail out early and probably a couple other little optimizations that we could do.
But for now, I think that this is plenty fine.
We're not going to have any actual performance issues.
There's no real big benefit in updating it or modifying it or making it any faster.
So, we're going to leave it and make sure that it actually works because that's the important part.
minimize our code editor, jump back into Unity, and press play.
And I expect that now, if I can get my scene view up over that platform a little bit, I should be able to jump up and have my foot kind of hanging off and then continue jumping.
This is going to be a much better feeling and more realistic character controller for a game.
So, I can jump up and there we go.
I can now jump even when I'm kind of like hanging off the edge there.
Still got plenty of room to jump.
Things are looking a bit better.
And I think I I like that feeling quite a bit more.
Now, you can modify that again by going to the player and just dragging in and out that foot offset, but I think that 0.35 is where I want to leave it for now.
So, now that I've got that done, I'm going to save, go to file, and make sure I've saved my project to.
Remember, file, save project.
Make sure that the main reason for that is we want to make sure that our tags have been updated and saved in in the uh update, which they should have been in the last one, but if you missed them, and make sure that you do that.
So here we've added raycasts for left and right foot and we're checking our changes.
Now we're going to add one of the most commonly requested features and that's double jumping.
It's actually a very simple thing to set up if you do it right.
Let me show you the process of figuring out when a player can jump and how many jumps they have left.
The first thing that we want to do is go to our player and open up our player script.
And we're going to start with a player that can jump two times.
And that's it.
We'll make it so you can adjust it later, but you'll see it's very simple to have any number of jumps that we want to have.
And the first thing that we want to do is when we're on the ground and actually landed, we want to just give our player some number of jumps.
So, we're going to want to store an integer or a number, a whole number of jumps that are available.
And I'm going to do that right after this line 86.
I'm going to add two more lines here.
and we'll say if is grounded and we want to make sure that our player is not falling downward.
So we need to do something with the rigid body and look at the velocity.
So we'll say get component and we'll get the rigid body 2D component and we want to check the velocity.yvalue.
We want to make sure that the y value on that velocity is either zero or negative like we're falling down.
It's pushing down.
So we'll say less than or equal to zero.
So if we're on the ground and we're going downwards or we're touching the ground and not moving at all, whatever it is, we're not moving up.
That's the main thing.
If velocity y is positive, it means we're jumping.
Then we want to increase or set our number of jumps available.
So we'll say underscore jumps available equals two.
Or maybe maybe we'll call this jumps remaining.
Let's do that.
We'll generate a field for jumps remaining since it doesn't exist yet.
And this how I generate all of my field variables.
Enter.
And then we'll hit it's alt enter and then enter to generate.
F12 to go to it.
And get rid of that private keyword.
We don't need it.
And it's just kind of extraneous.
We don't need to give it a default value though because it's going to get set in our grounding to two every time we're on the ground and pushing downwards.
The next thing we need to do is in our jump detection.
Instead of checking to see if we're grounded, let's just check to see if we have jumps remaining.
So, we'll replace the is grounded here on line 15 with jumps remaining is greater than zero.
And then the last thing we need to do is just remove a jump from our jumps remaining whenever we use one.
So, if we use a jump, we need to decrement our jumps remaining.
To do that, we're going to modify this little chunk of code here on line 56 and put it inside of braces.
So if they start a jump by pressing fire when they have jumps, we want to do two things of code.
So we'll add some braces around this.
And we'll set the jump end time still for when our jump has to end.
So we have our maximum time.
And then on the next line, we'll say underscore jumps remaining.
And we want to remove one.
So just like plus+ removes or adds one, minus minus removes one.
So that will decrement it or reduce it by one.
So it'll go to two and then it'll go down to one and then it'll go to zero.
So, we'll be able to jump twice in the air.
Let's save.
Get rid of the little star there.
Take a look at our entire script again.
And then go try it out.
We should now be able to jump two times.
And if we change that code that of jumps remaining from two to three, we could jump three times or however many times you want.
Or we could put that in a variable.
But for now, I think two is probably good.
Let's try it out and make sure that it works, though.
So, I come in here, I jump, and I jump again.
Look at that.
jump and jump again.
And I have no more jumps.
Can't jump.
Jump.
Jump.
It's looking good.
You can actually look at our jumps remaining value, too.
You can't see this in the player right now, but let me show you a cool trick so that we can view it and kind of debug it if you're curious or if maybe you're not seeing your jumps remaining, right? So, what we can do is go to this player, click on the three dots, and then choose the properties.
Oh, it's a little bit off screen.
Let me drag it over so it pops up on your screen.
So click here on the three dots and properties right there.
That'll bring up this nice properties window that shows me everything that I was already able to see.
But now I can right click or click up here on this little dot and choose debug and see all of the hidden variables as well.
So I can see my jumps remaining is at two.
When I jump it goes to one and I jump again it goes to zero.
And now what you do with this window is up to you.
I like to just have one of these kind of off to the side that I can see and view and kind of debug stuff without having to go modify my inspector.
Again, remember, you just go to rightclick and choose properties.
It'll bring up a window and then just put that window into debug mode if you want to see the private things on there.
You can see the public things by default, but you can see those in the inspector anyway.
All right, so our double jump is working.
I'm going to make sure that we are saved.
go to the project view or the plastic view and commit that we've added double jump and check in.
Now, we're going to add a little punch to our jump and we're going to do that with audio.
We're going to add a jump effect that plays whenever we jump and change this so that we can tell which jump we're on, if it's our first jump or our last jump.
So, if we've got multiple jumps, you can kind of get a little bit of variation in there.
It's going to be very cool and a lot of fun.
The first thing we're going to need to do though is find a jump sound effect that we can use.
My recommendation is to go to Open Game Art.
And on Open Game Art, there are a whole bunch of different free sound effects that you can use.
The one that I like the best so far was this platformer jumping sounds.
It's got quite a few jumps.
Can hear them.
They play quite differently, but I'm going to go with this first one.
jump one just the first very basic default jump.
Feel free to use whatever jump effect you want, but we are going to do a little bit of pitch variation here.
So, just kind of be ready to play with it and be ready to swap it out.
So, first thing I need to do is download my platformer jumping sound effects.
So, just click on it, download it, and get myself a nice big zip.
The zip of my platformer effects, I believe, is full of different wave files.
There we go.
We've got a jump 01 all the way through a jump 11.
And I should be able to just double click on these and play them in whatever my media player is.
Let's see.
There we go.
It played.
But now I need to get them into my game.
And the best way for me to do this is just select the one or ones that I want.
And right now I just want this first jump.
So I'm going to take this jump01 wave and copy it in my zip file.
You can extract these however you like, but this is the way that I like to do it.
I'll copy it out of there, put it onto my clipboard, and I'll go back into Unity, and I'm going to make an audio folder.
So, I'm in my project view, go to the root assets folder right here, right click in the empty space, create a new folder.
I'll name this audio.
Whoops, I got to go down to it and name it audio.
So, F2 to rename and AUDIO.
I'll hit enter to go into it.
And then rightclick, hit show and explorer, which will bring up the window.
And then I can just hit enter to go into that folder.
Since I've copied that audio file onto my clipboard and I haven't hit control + C again, I should be able to paste it with controlV and have it just extract the file right into that folder.
And then remember when I tab it back into Unity, as soon as I click over here, it should show up.
It'll import the file and pop up.
And now I have a Jumbo 01.
And if I click on it, I can play it.
It'll autoplay.
But when I click the little button in the corner, it'll also allow me to just kind of replay it as many times as I want.
So now I need to add this to my player.
To do that, we'll select the player and then just kind of collapse some of these components down in the inspector.
And I'm going to drag my audio file onto this empty spacer.
So I'll click, hold, don't release the button, drag and release, and we should get an audio source automatically added.
Now, if you're having a hard time with that, you can't get it to work for some reason, try just adding it manually.
You can hit the add component and type in the word audio, and you should see an audio source here down at the end.
It's the one with the little speaker.
Make sure you get the right one.
And then you can drag that clip into there or hit the little search button and find the jump clip.
So now I've got a jump sound effect attached to my player.
In fact, I've got a sound effect and a sound effect player or an audio source that's going to play the sound effect for me.
If I just press play right now, I should hear a jump sound right when the game starts.
And that's because this play on awake button is checked.
Let's check.
Let's press play and check.
and it said button, but it's really a checkbox.
That checkbox is checked.
So, we play and I heard the sound effect.
Now, if you didn't hear a sound effect, you might have your audio muted right here.
See this little box? It's a toggle to mute audio in your game view.
If it's muted, you're not going to hear anything.
So, make sure that you unmute that.
Now, what happens if I check the loop box? Well, nothing right now because it's not playing.
But if I turn my audio off and on like that, you hear that it just kept looping.
I'm going to stop playing though because I don't want either one of those things happening.
I don't want it to play on awake and I don't want it to loop.
So, we'll stop playing.
Uncheck both of those boxes and let's open up our player script.
So, inside of our player script, what we want to do here is when we run our update and we do the jump, as soon as we jump, we just want to play the sound effect.
To do that, we're going to need to reference our audio source and tell our audio source to play sound.
We can get the audio source component just by calling get component and give it the type.
So we do that lesser than which is again shift in the comma.
Give it audio source.
Close that off and do our open close parenthesis.
And we do a dot at the end and say play.
Hit enter.
Open close parenthesis and a semicolon.
What this will do is get the audio source on this same object.
So on the player object and tell it to play.
Let's save and see if that works.
So, Crl S get rid of that star.
Go back into Unity.
I also want to make sure that we save our scene here.
So, we get rid of the star as well.
Crl S any second now.
As soon as it finishes reimpporting, hit Crl S and play.
And now, whenever we jump, we should expect to hear a sound effect.
Let's see if that's the case.
There we go.
I jump and every time I jump, I hear a sound.
If I keep clicking, I don't get anything.
Just when I actually jump.
All right.
So far, that's pretty good.
I I like it.
We've got a sound effect.
It works.
But there are a couple of minor changes that I want to make.
First, I said that I wanted it to sound differently depending on how we um how many jumps we have left.
But I also don't really like having this line right here.
And I want to talk a little bit about this because we've got another one up here.
We have these get component calls that are being made in our update method.
And really, most of the time, we don't want to do this.
Generally, my rule of thumb is don't do get component calls in an update method.
If you're going to get a component and that component is going to be the same component every single time, then you should do it once and save that value off.
So, that's the case for our audio source and our rigid body.
Let's let's take a look at that.
We'll zoom in.
And if we want to get rid of this git component call and just cache our audio source, what I'll do and what I would do is hit controlx.
So, I've selected it all and then type in the word underscore audio source.
Again, the underscore is just a personal preference thing letting me know that it's a member variable, something at the class level and not part of the method.
So, I've got an audio source.play and that gives an error because audio source doesn't exist.
So, I'll hit alt enter and well actually I'm not even going to generate a variable.
What I'm going to do is go up to the awake method.
Watch this.
This is even better.
I'll type underscore audio source equals and then I'm going to paste because we have that get component audio source already on my clipboard and I'll add a semicolon.
Now click on the audio source again and hit alt enter and enter to generate a field.
And now I've got a private audio source named audio source and my error down here is gone because it's correct.
And the reason I didn't generate it from here and I did it from up here is because if I generate it after I've written the code to do the assignment, this get component part, it's going to know to make it an audio source.
If I had done it from the other spot, let me show you.
Don't don't do this.
Just let me show you real quick.
If I had done it from down here and hit generate a field, go to generate field, it's going to give me an object.
And that's just because it doesn't know that I want it to be an audio source.
again on the other part because I'm define defining it and assigning it right here on line 28.
It's able to determine, oh, you're going to assign it to an audio source.
So, it should be defined as an audio source.
So, I'm going to redo that code.
Get that audio source back in there.
Remove that private keyword that I don't need.
I'm also going to add a space in between my public variable and all of my five private variables here.
Now, we'll save.
We'll go back into Unity and make sure that it still works because we've done a little refactor where we moved code around and changed it and make sure that everything's good before we make another change to the pitch.
So, press play.
We should be able to jump twice and hear the exact same sound effects.
Looks good.
And then we'll stop playing.
Let's drag this window back out a little bit.
bit.
bit.
And then we'll go over to plastic and let's do another commit.
First I want to make sure that I've saved and then we'll say that we added basic jump sound to player jumps and check in.
Now we're going to play with the pitch of our jumps and give our player some feedback on how many jumps they have left, but do it audibly.
Let's take a look at our player again.
I've got the player selected and we're in play mode already running.
got the audio source kind of expanded here.
If I jump, I hear my sound effect.
But if I play with this pitch value, listen to how it changes much higher or Oh, that's too low.
Can't go down below zero.
Let's go with like a 0 2.
0 2.
0 2.
You can hear that it changes quite drastically.
So, one is the default.
And what I'd like to do is go to maybe like a 1.1 or a 1.2 two for the second jump so that we jump and then the second jump is a little bit higher saying hey this is your last jump or indicating that so let's stop playing my values should reset on the audio source and we'll open up the player script in the player script when we do the jump right before we play the audio source we need to set the value of the pitch so what we're going to do is start with an if statement we'll say if jumps remaining is greater than zero so if we still have some more jumps left then we're going to set the audio sources pitch equal to one.
I got to spell pitch right, but if I spell pitch correctly, there we go.
That should work.
And we'll say else.
So, if we don't have more than zero jumps remaining, we're going to set the audio source pitch.
And I don't want to set it equal to zero, but I want to set it equal to something slightly higher, like a 1.2.
And I might need to add that F there to indicate that it's a float.
So now when we have more jumps remaining, it'll give us that normal sound until we're on our last jump.
That'll be slightly higher pitched.
Let's go try that out.
Make sure that we saved and let it reload our code and we'll play.
And watch that pitch value in here, too, because that's going to change.
You're going to notice the pitch value visually changing as we hear the effect when we jump.
So we click So you guys can hear that, right? Sounds good.
You've got an actual pitch modification.
And this should be enough to really give your players some good indication of what's going on.
Now, I want to show you something else very cool, though.
This is something not really related to audio, but something related to if and else statements.
You're going to find that this is a scenario that you're doing often where you need to write some code that does one thing if a if a certain condition is met and then does something else if that condition is not met.
It's very very common where you have a true or a false value.
So if we have extra jumps remaining, we're using a one.
If we don't have extra jumps remaining, we're setting the pitch to a 1.2.
Now, the way to do this in a shorter, slightly easier to use syntax is to convert it into what we call a turnary assignment.
And I believe I can alt enter.
Yep.
Turn it into a conditional expression.
That's what that's what I was thinking.
A turnary assign conditional expression.
We hit enter.
And then we get a pitch is equal to and then we've got a statement here.
So, let's take a look at what this is doing.
Says audio source.pitch pitch is equal to and then it's not assigning it to jumps remaining greater than zero.
That's not what's happening.
What's happening is this bit of code is getting checked.
So it's saying we're going to assign this pitch to some a value of something.
First do a check on this is jumps remaining greater than zero because if jumps remaining let's put this in some parenthesis real quick.
Make it even more explicit.
If the part in parenthesis is true then you use the first value after the question mark.
Otherwise, use the value after the colon.
That's essentially what this means.
It's a shortened down way to write out all of that if statement into a single oneliner.
So, it'll check this statement here.
Doesn't have to be in parenthesis, but it can be.
I put it in parenthesis just to make it easier to read.
So, if jumps remaining is greater than zero, it'll use a one.
Otherwise, it'll use the value after the colon or a 1.2.
Very common way to write code.
You're going to see this very often.
So, it's important that you understand it, see it, and just start writing it.
If you start to see a lot of else if statements in your code, look to see if you can turn them into conditional assignments like this.
It'll clean things up.
It be a little bit easier to understand most of the time, and it'll make it so that when you see this in the wild, it's easier for you to kind of grab right away.
You're not you're not thinking about it.
All right.
So, with that done, I'm going to save.
We're going to jump back into Unity.
make sure that we haven't broken anything, that the assignment wasn't backwards and we're not starting with a high pitch and then going to a low pitch or anything.
And if that's good, then we'll do our commit.
So, let's go check it out.
We press play.
And any second now, we should get our game view and jump.
Sounding good.
Let's try going on a platform.
And now let's try jumping without a double jump.
All right, sounds good.
Looks good.
Let's go commit.
So go into plastic SCM and we'll say that we um added pitch change to double jump and check in.
It's time for us to add more props and grow our level.
and we're going to add some props that allow us to keep working with the physics system and do some really cool stuff and then bring in some interesting new requirements like being able to see a much bigger world.
So, let's start by taking a look at some of the props that we have available.
If you look inside of our items folder and our Yeah, it looks like the items folder has a couple of them.
We've got some flags and some keys and some other things, but there's also one, I believe, in tiles.
We've got some locks.
We've got some lava, some ladders, some switches, and other things.
And the one that we're going to start with today is the spring.
So, we're going to take the spring object.
Just search for spring.
It should be under art and tiles.
Or go to the project view and search for the word spring.
SP R.
There we go.
Iing.
There's also a spring.
Don't use that.
That's the one that's already popped up.
The popped up version of the spring.
We're going to use the spring.
So, for the spring, what we're going to do is well, first just drag it out into our scene.
Uh, before I even do that though, I do want to double check that my pixels per unit is correct.
So, it's set to 128 pixels per unit here.
I'm using the fullsized version of it.
It goes all the way up to the top and it matches at that 128.
So, I should be able to just drag this in and see a nice looking spring.
Now, I'm going to add a collider to it.
Let's start by trying adding a box collider 2D and see what that does.
So add a box collider 2D.
And notice that this collider is kind of big.
It goes all the way up to the top above the size of our sprite.
And that's again because our sprite is bigger than the actual image.
It's taking up that full space so that it's the full 128x 128.
If we want to use a collider on here, we've got two options.
We can either shrink this in half and then move it down about 0.25, a negative 0.25.
That'll give me a pretty good box collider.
Or I could alternatively add a polygon collider 2D and that would give me a good collider that matches up perfectly too.
I'm going to go with removing the polygon collider and just having a box collider.
So I've got a nice square collider that matches and it's pretty good.
I don't need a polygon collider to to recreate this shape.
I think that that is just about close enough for me.
So we've got a spring in here.
And if I press play, I should be able to run into it and jump on top of it.
Let's go see.
All right.
Any second now, it should finish building and we'll be able to run over there.
Let's see it.
There we go.
Our player runs over.
I can run into it.
You can see I just kind of run into it and keep running.
And I can jump on it and walk on it just like a normal object.
Collider looks good.
So far, it seems okay.
I can even jump off of it.
That's perfect.
But I want to modify this now and make it so that when I land on this spring, my character bounces up really, really high.
To do that, we're going to add in a physics material.
We don't have to do any special code or anything like that.
We're just going to use the physics m system in the way that it's meant to be used and take advantage of some of the cool properties and and things that it can do.
So, I'm going to go to the assets folder of the project window, go to the root assets folder, rightclick, and create a new folder here.
and we're going to call this one physics.
This is going to store some physics related assets or data, specifically some physics materials.
I'll hit enter to go into it and then rightclick again in this physics material f or this physics folder.
And we'll choose 2D and we're going to find a physics material 2D.
I'm going to name this spring.
I could also name it bouncy, but I feel like naming it the thing that I'm going to put it on makes a little bit more sense.
And over here in the inspector, notice that we've got two fields, a friction and a bounciness.
You can probably guess which value we're going to crank up and which value we're going to turn down.
We're going to turn bounciness up to one, which is the same as 100%.
You can't go higher than one.
It won't matter.
And we're turn friction down to zero, which is obviously 0%.
Let's save.
And then let's attach this to our spring.
So I'll go to the spring.
I I saved a little too early.
And then we'll drag the physics material 2D into this material section of the box collider.
Make sure it's on the box collider or you can hit the little search and then go select spring.
Now I'll save one more time since I actually assigned the material.
And then press play and let's see if we can jump and bounce on our spring.
All right, look at that.
It bounces and I just kind of bounce.
And if I bounce from a higher spot, I'll bounce back up to that that same height.
So, here we go.
I've got some pretty good bouncing.
I've got a nice little spring here that I can use in some future development.
Now that the spring works, though, let's commit it to plastic.
So, go into plastic and make sure that we've saved our scene and say added spring with bouncy material and check in our changes.
In the last section, we just set up a spring and it bounces our character.
But what if we want to show that sprung version of it so that we can show that the player actually kind of bounced up and add a little bit more fun and feel to it? Well, we're going to need to do something a little bit different.
And in fact, it's time for us to start writing a second script.
So far, we've written all of our game code on the player.
And that's fine when we're starting out and when the game is small, but as things grow, we're going to want to write code for multiple different types of objects.
In fact, we're probably going to want to write multiple scripts just for our player as well.
So, we're going to need to create a new script for our spring that can do some visual swapping that can maybe change the way the sprite looks when the player bounces.
It's relatively simple to do, but we've got to get past that concept of multiple scripts.
So, we're going to need to add a new script to our spring.
We're going to go into our scripts folder first and create it.
So, we'll go to assets, go up to scripts.
I'm going to rightclick and choose create and choose a new C# script or just C# script right here.
We'll name this spring with a capital S.
S P R I N G and hit enter.
This should generate my file and I'll open it up in my code editor.
Just hitting enter should open up the code editor and find it.
If it doesn't, um, what I recommend is usually go back to Unity and then do it again.
most of the time the second time through it will find the actual file.
All right, so we've got our file right here, our spring class.
And if yours doesn't match, just remember that the class name right here has to match the file name here.
Make sure that they match.
If you messed it up, changed it, just make sure that they match afterwards, including the casing.
Get that exactly right.
So in our spring, we want to be able to change out the sprite on our sprite renderer.
So, what we're going to do is get a reference to our sprite renderer.
Check when we're colliding with a player, and when we are, we'll swap the sprite, and then when we're no longer colliding with a player, we'll swap the sprite back.
So, first, we're going to get rid of our start and update methods because we're not going to use either one of these in this class at all.
And there's really no benefit to having them here.
The well, the key benefit is that they're here automatically when we create a new script.
So, we have like a good starting point.
we know where to put things if we're new to Unity or we're just kind of getting started, not sure what to do.
But if we know what we're going to do, and here I do know what we're going to do, we can take all of that code right there and just hit delete and have a nice empty public class with no extra stuff in it.
So, what are we going to put in here? Well, we're going to start with some collision methods.
In Unity, we can get callbacks or method calls whenever an object collides with another object.
In this case, we want to check when anything collides with our spring.
and we're gonna want to know if it's the player.
And if it's the player, we're going to want to do some fancy flashy graphics things.
Well, there's semi flashy and fancy.
Let's take a look at what that looks like.
We're going to start with the on collision enter 2D method.
So, I'll begin by typing on collision enter and just let it autocomplete.
I didn't worry about the casing because I know autocomplete's going to find it.
I'm going to choose on collision enter 2D and hit enter.
I'll get this nice method private void on collision enter 2D with a collision 2D parameter named collision.
First, I'm going to delete the private keyword just because I don't need it.
And then I'm going to go down into our method on line 9.
And what we want to do is check the collider of this collision 2D object.
This thing is just some data that tells us what the collision was and gives us more information about the collision, like what hit it, what object it hit, what angle it hit at, and what point in the world, and so on.
But all we really care about is what hit it.
So, we're going to say if collision collider compare tag, and then we want to put in the word player.
So, if the collider has a tag of player, and we're going to talk about that in a moment, then we want to show our sprung version.
So, we're going to need to modify our sprite renderer and show a sprung sprite.
We'll do get component and get the sprite renderer.
And then we're going to set the sprite on that sprite render.
So, we'll say the sprite renderers.
equal to.
And here we're going to assign like a sprung sprite.
So let's say underscore sprung.
Now we're going to need to generate a field for our sprung sprite.
So I hit alt enter and generate a field.
And then we're going to make this a serialized field so that it shows up in the inspector.
If I do it just like this, sprung will be null or nothing or not assigned.
And this is just going to empty out our sprite.
That's not what we want.
We want a serialized field so that we can then assign a sprite to it.
Let's save, get rid of the star, go into Unity, and test this out and see what we've got so far, how it works, and then make a couple modifications.
So, we've got our spring class here.
We're going to need to attach it to the spring object.
Let's go select the spring.
I'll minimize my box collider and drag the spring script over here, and that will attach it here.
If you had a hard time with that, remember, you can hit add component and just start typing the word spring, and you'll find it as well.
Just make sure you only have one.
You don't want two.
Now, on our spring, we have a spot for the sprite.
And I told you I wanted the sprung sprite.
So, I'm going to hit the little search box and search for the word sprung.
Spr U N G.
And then go select it.
I can also remember use control and the mouse wheel to zoom in and see the the graphics of these.
But I'm going to choose sprung.
I will save and then play with control P because I don't want to click the mouse right now.
And then we'll go over there and touch that thing and see if the graphic changes.
You should expect to see though that the spring graphic on that sprite renderer right here is going to change to sprung and the visual will look different.
Well, not yet.
So, why didn't it look different? What happened? Why isn't it changing? Let's take a look at our code one more time.
We're comparing and checking for this player tag.
And we haven't talked about tags yet.
So, where are tags? Why is that tag not assigned? And what does it mean? Let's go look at our player.
Notice this untagged keyword up here.
This is the default tag that's on every game object when you create when you create an object.
It has no tags assigned just like it has the default layer.
It comes with untagged.
I'm going to go back to the player now.
Click the drop down and choose the player tag.
That tag exists by default.
It's one of the most common things people need to use.
So, it's just there.
You can, however, create your own tags.
If you go to add tag and then hit plus, you can start putting in your own special tags like environment or whatever.
And then when you go select your character, you'll see that tag show up.
Now, I'm going to go delete that tag because that's not a tag I actually want.
We will go through and do some tagging later.
For now, I'm going to clear out my tags, go back to the player, and make sure that he has the player tag assigned.
We'll save.
Press play again.
And now only when I collide with the player should I get that visualization change.
If I collide with another object or something, I shouldn't expect to see that that change on the spring.
So, let's run over.
Look at that.
As soon as I hit it, it changed.
Now, that's a problem, though, cuz it's staying permanently like that.
And that's not really what I want.
I want this to modify a little bit and uh just like change and then switch back when I leave the collision.
So, as soon as I'm no longer touching it, I want to kind of like bounce back down.
Let's go back to the spring code.
And just like we have an on collision enter 2D, you might have guessed there's an on collision exit 2D.
So I'll just go down here and type on collision exit.
And so I just typed on NC and I could find exit 2D right there.
I'll hit enter.
Delete that private keyword again.
And then here, let's just take lines 11 and 12, copy them, Ctrl + C, and go down to 17 and paste with Ctrl +V.
Now, I don't actually want to do that.
I don't want to set the sprite back to sprung if I leave.
I want to set it to the default sprite or the normal sprite.
And I got a couple ways that I can do that.
I could add another serialized field here and have like the default sprite.
But then I'm kind of setting it twice.
I'm setting it in here.
Let's take a look at what that would look like.
If I said default sprite and I saved, I would come over to Unity and then I would have two sprites down here and one up here that I have to assign.
Got to assign the one that's there and then I've got to assign the one that gets kind of reassigned or reapplied when I exit.
So there's the the one when we start, the one when we spring, and any second now, yeah, the default.
And I don't like that.
Instead, I want to take this value and have my spring just know about it and kind of fill in this default instead of having it be serialized.
So, let's go back to the spring.
I'm going to remove the serialized field from my default sprite.
And then I'm going to add an awake method.
An awake method is where we do a lot of our setup and initialization just like in the player.
And we're going to do that for our spring as well.
So, I'll type in awake.
I'll get rid of my private keyword.
Control and delete.
By the way, get rid of that whole word if I'm at the beginning of it.
And in our awake, we're going to say underscore default sprite equals.
And here I want to do something.
Get it from the sprite renderer.
And you might have noticed I've got get component sprite render.
Get component sprite render.
And I'm just about to write another get component sprite render, let's see, renderer, and get the sprite from there.
But that's not what I want to do.
I want to just save this sprite renderer off so I don't have to make this call multiple times.
So, I'm just going to take this get component part, cut it, add a new line, say underscore sprite renderer equals, and I'll paste in my git component call.
Hit home, alt enter, and generate a field.
And now I've got a cached sprite renderer in my spring class.
Delete that private keyword.
Just double click it, and hit delete a couple times.
And then let's take that sprite render, copy it, control C, the underscore sprite renderer, paste it right before the sprite.
So now we've got the sprite renderer, we've cached the default sprite right here.
And then in our other two parts where we call get component, let's just replace those with underscore sprite renderer so we don't have to make that semi-expensive call more than once.
The last thing that we need to do is reuse our default sprite.
So on collision exit, instead of going to the sprung sprite, we'll go to the default sprite.
We'll just paste that in.
So copy it from here and paste with crl +v.
And we'll jump back into Unity and jump around.
And let's see our spring bounce up and down.
At least that's what we should expect to see.
And this default sprite field could completely disappear.
All right, it should start playing.
And we jump over there.
Boing.
And you can see it bouncing.
And now we're getting that effect.
All right.
So, that is exactly what I wanted.
I'm going to stop playing, go into plastic, and commit that we've added a sprung effect.
Actually, first, let's make sure we've saved.
Go to file, save project as well.
Make sure that our tag manager and everything are in there.
Say added spring visualization.
And we'll check in our changes.
Now that we've got a spring, we have a little bit of a problem that our player can get pretty far offcreen.
If I take my spring and I drag it up here onto one of these higher platforms, and then I go jump onto that, you'll see just how far off screen I end up.
So, we're going to need to do something to address this.
Let's go reproduce it, though.
Make sure that it all makes sense, and then we'll dive into some possible solutions.
So, here we go.
I jump up.
I jump up and I jump on that spring.
And yeah, my character's way off the screen.
You can see that I'm just flying way up here outside of this camera view.
Remember, this white box is showing us the camera.
If you don't see it, you can turn the gizmos on and off right here with the little world looking icon.
And we need to make it so that our camera now shows our player all the time because what's the point of showing a game where we can't see our own player? Need to be able to see our own player.
And to show our player, we've got a couple of options.
The first option is actually really, really simple.
If we have our player kind of where we want them to be in the world all the time, like they want to we want them maybe centered.
Let's move them over to a zero.
And right at about that height, we can take the main camera, drag it down to be a child of the player by dragging it and dropping it on top of the player, and then press play.
And now the camera will move along with the player.
This is somewhat effective.
Let's go try it out.
So, we're in and any second now.
There we go.
I can run around and yep, you can see I can definitely see my character all the time.
I can't really see the bottom of the world and it's not a perfect camera setup, but it's a definitely a little bit better than what I was seeing before.
There is a better solution though, and we're going to dive into that now.
So, let's take the main camera, drag it out, and then we're going to go to the window menu and choose package manager.
The package manager window should pop up and it should look something like this.
In the top left, you've got a couple options.
There's in project, there's my assets, and then there's a Unity registry option.
Choose the Unity registry option from the drop down.
And then scroll all the way down.
So, you've got all these options up here, features, these big packs full of stuff, and all of these packages.
You can see some are already installed.
The green check mark means that that package is already installed in this project.
And you see we've got a lot of the 2D ones already there cuz we're building a 2D game and they came with our 2D template.
So we need to scroll down until you find Cinem Machine.
If you don't find it, you can always search for it here.
Cinem Machine.
And currently it's on version 2.9.
There is a version 3 that's just about to release, but it's still in a beta.
So I'm not going to jump into it yet.
But just know that it simplifies things a little bit when you get into the deeper Cinem machine controls and makes it easier to write code with it, but it still has all of the same functionality.
So, we're going to choose the install button and install the Cinem Machine package.
This is a camera management system to do super advanced or super basic or whatever type of cameras you want.
You can do cameras where you're following multiple players, where it's transitioning and fading between them, where it's, you know, doing cinematics, all kinds of interesting, cool stuff.
But we're going to start with something very basic that gives us still a lot of just nice feel and a really good look for our game.
So, we've got our Cinem Machine package.
It just finished importing.
And I'm going to go save my scene.
And then go to window.
No, game object.
I lied.
I'm going to go to my player, right click, and I'm going to choose camera, Cinem Machine, and 2D camera right here.
So, I'll go to Cinem Machine, 2D camera, and it's just going to create a child object that's a camera of our player.
And it's going to have a follow field on it, a look at field, and a bunch of other stuff.
I'm going to now take my player and drag that into this follow field.
Look at that.
My player is now centered right in the middle.
And if I press play, this alone is going to give me a decent camera control.
I'll be able to see my player and move around.
Let's go check it out.
All right, there we go.
As you can see, I can jump around and there's a little bit of smoothing there.
It's not just instantly super tight with my character.
Feels quite a bit better and it flows, I think, quite a bit better.
But I don't like how high up I am.
So, I'm going to make a little modification.
I'm going to expand out the body section.
And now I can see where my character is moving around and where it's kind of locking in and see where the center of the screen is.
And we're going to modify this tracked object offsets Y value.
I'm going to put a value of about 1.5.
And now my character is down kind of closer to the bottom of the screen.
I think that that looks pretty good.
I'm going to stop playing now.
Read my 1.5 because I was in play mode.
So my changes didn't save.
Go select my player so that I stopped seeing the preview.
Save.
Press play.
And try one more time.
and see what my character looks like and feels like kind of moving around with the new camera control setup on.
There we go.
I can run, jump, jump, jump, and bounce and start to bounce higher and higher and higher and so on.
Look at that.
Now I can bounce up super high to the sky and still fall down and see the ground as I'm falling.
With that, I'm going to save my scene again and do another commit and say that we added cinem machine camera control or camera system.
Say that and we'll check in our changes.
In this lesson, I want to present a small challenge to you.
The challenge is pretty simple.
Take the spring and make it so that when our player jumps on the spring or bounces on the spring, remember they're not actually doing a jump.
We hear a sound effect.
This sounds kind of like our jump, but much deeper.
See if you can figure out the code and the setup process to do that.
You shouldn't need to import any new files, but you're welcome to if you want to.
And then come back when you're done and I'll show you the process on kind of my way to do it and see how well it lined up.
Also, if you get caught, you have any problems, get stuck, or any questions, feel free to just press play and follow through.
All right, let's dive into the solution.
The first thing I want to do is select my spring.
We want to add an audio source so it can play some sound effects when it's hit.
And I'm going to do that by just choosing the add component, typing in audio source.
Go choose audio source at the bottom.
And then we've got to put in an audio clip here.
So I'll hit the search box and go find my one audio clip that's in my game right now, the jump 01.
I'm going to uncheck play on awake because I don't want this to make a sound from the start.
And I'm going to turn the pitch down to something like 0.5.
Now, I should be able to hear this thing sound super deep when I land on it.
We haven't written the code to make that happen yet, though.
So, let's open up the spring and do that.
In the spring code, when we get a collision, we'll just get a hold of our audio listen or our audio source and tell it to play.
So, we can add in some braces here after line 19 and before 23.
And then after we've set the sprite, we can get our audio source.
So get component.
See if I can spell get component.
Get component.
Audio source.
And we'll tell it to play.
This should do it.
This should make our spring start playing whenever we jump on it and land on it if it's a player.
Let's go see if that's the case.
So we jump back into Unity.
I want to make sure that I've saved my code and my scene.
gotten rid of both of those little stars there.
Soon as it finishes recompiling and then press play, it should be able to bounce off that spring and then hear a nice deep boing or something similar to that.
Let's go check it out.
All right, we run over.
Jump.
Jump.
Whoops, missed my jump.
Let's do a bigger jump.
Jump.
There we go.
And I can of course modify this by turning the pitch down even more if I want.
Go to like I think I kind of like that better.
025.
So I'm going to stop playing, change this to a 0.25.
Save my scene and then go back and make one other change because we've been caching a lot of components lately.
We did it right up here.
We cached the sprite renderer, but we didn't do it for this audio source.
So, let's cache our audio source as well.
Even though we're only calling it on collision enter, I feel like it's a little bit cleaner to just cache this in awake since we're caching our sprite renderer too.
So, we'll take the get component call, select it all, hit Ctrl X, go right up above, right at the end of line 12, and hit enter and say underscore audio source using that camel case again.
So, source is capitalized equals and then paste and semicolon.
Hit click on the audio source part here.
Hit alt enter, generate that field.
Should give us a nice private field that we can double click the word private and delete.
And then put the audio source by double clicking it, copying it, and pasting it right before the play.
So now we have the audio source gets cached in awake and saved.
So we can just reuse it instead of having to tell the Unity system to give it to us every time we need it.
We'll save, go back in, test it one more time, make sure that it works before we commit because we don't want to commit it if we accidentally had a typo or broke something.
Any second now it should finish and we'll play.
Oh, I probably should add some more springs and start bouncing around between them.
But for now, let's just play jump up and make sure that it sounds right and jump.
All right, so that looks good.
and sounds good.
The last thing I want to do is just move this spring.
I don't like the position of it.
So, I'll go to the scene view.
Select the spring.
I'm going to drag it down here.
Holding control.
Let's get it to a negative 4.5 and a negative what? Three.
No.
Whoops.
I put I hit the wrong key there.
-3.
Let's zoom in a little bit.
I think it might be negative 3.5 that I want to go to.
So, I'll hold control and drag with the mouse right here.
Remember, this is W to get into move mode.
W here.
E for rotation, W for move.
And you can see this is pretty perfect here.
So I've got a negative 4.5, negative 3.5, and then in my game it looks like it's nice and flat on the ground.
So we'll save.
We'll go into plastic and say added sound effects to the spring and checking our changes.
Now we're going to do some level building.
We'll start by pulling in a background, tiling it out, and then add some platforms, some things to kill our player, and try to make this kind of fun so that we've got some challenges and we can start tuning things.
Let's start by going to the art and backgrounds folder.
And then in here, we've got, I believe, eight different backgrounds to choose from.
I'm going to go with colored grass.
I think the one with the giant mushroom looking things.
And drag it right out into my hierarchy.
I'm going to drag it right here into the center or this empty area so it gets positioned at 0 0.
Now I'm going to switch it over to be tiled instead of simple on that draw mode.
Remember that's on the sprite renderer.
And here I'm going to change the tile size from being eight on the width to maybe like an 80 so that it's nice and wide.
If I go to my scene view, I can zoom out and see, okay, I've got lots of room to work with.
If I want to make this bigger though, I want to make my level giant, I can of course just continue to crank that number up.
I can make it 800 or something else.
And yeah, look at that.
That's just way too big.
So, I'll drop it back down to 80 for now.
It's easy to adjust, though.
It does say that the thing might not appear correctly because it's not set to full wct mode.
You can tell that it does appear correctly, but I'm still going to go back over and set all of these over to full wctck mode anyway.
So, I'll go from tight on the mesh type to full wctck, which is just going to make it pull in the entire thing and not try to crop anything.
There's nothing for it to crop.
So, it shouldn't have an issue.
It shouldn't get any weird stuff, but I just like to set it up so that the error goes away at the very least.
Now, we don't have that warning there.
And if something changes with that background, we'll know about it at least.
All right.
So, we've got a background here.
And what happens if your background is showing up in front of stuff? Cuz it's very possible that you drag it out and your background is showing up in front of one of your platforms or in front of your player or something else.
Well, look down here at this additional settings section of the sprite renderer.
Here, I'm still on the colored grass.
Got additional settings expanded, and I've got an order in layer.
If this value is set to something like one, it's going to appear in front of everything else that shares the sorting layer with it.
If it's set to zero, it's going to be kind of random.
Everything that shares the sorting layer with it will be placed there, and you don't really have a lot of control.
You're not really controlling what's on top of another thing.
Some things may be on top of others.
Some things may be below others.
We can also set it to a negative one.
Get rid of that zero.
Just put in a negative one.
That would force it to be back behind anything that was a zero or higher in the order and layer.
Let's set this back to a zero real quick and take a look at one of the other objects like this platform here.
So, if I go select my platform, you see that it has an order and layer of zero as well.
So, it's showing up just kind of randomly in front.
If yours isn't showing up in front, you can go set this to a one and then it would show up in front.
If I set this to a negative one, again, look, it disappears, but my other platforms and everything else are still in front.
Now, this is not the way that we want to do it.
We don't want to go through order and layer for all of the sprites and set them to the correct layer or anything.
Instead, what we want to do is add in a new sorting layer.
So, when we click on the sorting layer option, we've got default and add sorting layer.
I'm going to choose add sorting layer.
And don't worry that I'm on grass mid right now.
I'm just going to hit add sorting layer and it's going to pop up my dropdown.
And do you remember how we added a player here? This was for physics.
So the physics layers are called layers, which is a little bit confusing.
It'd be nice if they were just called physics layers probably.
But since there weren't sorting layers before, they were the only type of layers.
So our player is not what we want.
We'll minimize that again.
And we're going to go to our sorting layers again.
Sorting layers are the layers that we use for ordering sprites and determining what's on top of another.
You can see we've got a default one in here kind by default, but we can hit plus and type in a new name for our new one.
I'm going to call this background.
And then we're going to assign it to our background.
So, let's go find the background, the colored grass, and then we'll go to the sorting layer and choose background.
And notice that it popped up right in front of everything.
And that's because our background layer is set to draw on top of our foreground layer.
Let's go back to the sorting layer menu again.
I'll just hit add sorting layer.
And this gives us our tags and layers window.
And here we can just take layer 1 and drag it up here so that background is now layer zero and layer 1 becomes the the default.
And now background will draw and then default.
And I I'm going to definitely want to add more layers here, but we'll do that as we add things that need to be on layers.
For now, we're going to save our scene.
make sure that we've saved our project as well so that our layered file gets saved.
You can see that this got marked as checked out and then we'll go into plastic SCM and we've got all of our backgrounds that have changed to full wreck the level the tag manager and ready for a commit message.
So say we added a tiled background to level one and checking our changes with the background in.
You'll probably notice some weirdness at the bottom and top of our level.
Let's go check it out.
If I run around, you see that uh right at the top of my tiled level, I've got this big blue area.
And then down below my level, I've also got this big blue area.
Let's stop playing, look at the scene view real quick, and see what we've got here.
So, that blue area isn't something that's being drawn.
You can tell that's just the background or the default.
That's why you don't see anything here.
But what could we do to fix this? The first thought might be to go to our colored grass background and just tile the background.
Maybe we go 80 and 80.
But you can see that well that doesn't look right at all.
Even if we went with a value that got that center in the middle for us, I think what like a 75ish maybe or somewhere, it's still not going to look right because we've got more ground up above and more ground down below.
So let's set that back to an eight and look for another solution.
Now the background that we're seeing right here, this blue, is actually being drawn by our camera.
So, if we select that camera in our hierarchy, we can actually modify it.
Look down here on the right.
We've got our camera.
We've got projection rendering stack.
And right here, environment.
If this is collapsed, just expand it out.
And look at the background type.
We've got a couple options here.
Skybox, solid color, or uninitialized, which means don't do any background.
We don't want solid or skybox or uninitialized.
We do want a solid color.
And the solid color we want is going to be something that matches with the top of our sky.
So, we want to go with a color that kind of matches the top there.
To do that, I'm going to click the little eyropper and then put my mouse right over here so that I get a color.
You can see it kind of previewing in the background section and click.
And now I've got that matching color as my background.
You can see it's showing up in the preview here on the bottom.
I'm going to save my scene with Ctrl S.
Press play.
And then let's go jump around and see how that looks.
If we've got some cool looking sky.
Oh, we've got sky down below.
Not quite what we want, but up above.
I think that's looking pretty good.
We've got a nice big big blue open sky.
And if I go to my scene view, or I guess you can't really see it in the scene view, but in the game view, you know that we have it pretty much going on indefinitely.
The ground, however, is unimpressive.
I don't want the sky down below me.
I mean, you might want the sky down below you depending on your game, but in my game, I don't want that.
So, I'm going to add some ground down below as well.
Let's do that by finding our ground tiles.
First, we'll select the grass mid and go click on the sprite to find it.
It finds my art ground and grass folder.
And if we scroll and zoom in, remember control and the mouse wheel.
Look for this grass center.
This is a perfectly set up tiled sprite to allow us to do big ground pieces kind of underneath the grass.
Says grass center.
It kind of looks like dirt, but you get the idea.
Let's drag this into our scene view.
I'm going to drag it right about here and see where it drops into.
And notice that it's not going to be at some even value on our position.
The x and y are this 9.55604 and 5.73.
And these are negative values as well.
So I'm going to just kind of round these off.
I'll take nine and go to 9.5.
Ah, that looks about right.
And take change this 5.72.
Let's go with maybeg -6.
No, 5.5.
So that it comes up a little bit.
Now that this is in place, I'll switch it over to be a tiled sprite.
And then let's maybe adjust the width here.
So, what's the width on our tiled sprite here? This grass mid 20.
I'm going to change this one to be 20 as well.
It's going to move though.
Watch this.
So, I go 20 and oh, it's no longer centered to where I want it to be.
So, I can just hit W, click on it, hit W, and then hold control and drag it over here.
This will allow it to move and snap by quarter unit increments.
You can adjust that snap setting right here.
in the where's it at? One of these ones has grid and snap settings allow you to modify it, but I want to leave it all just at the defaults for now.
So, we've got our ground here underneath.
And if I go to my game view, you can see that it looks better.
But if I fall down, let's hit play and see if I fall down or jump a little bit.
I'm still going to see underneath that.
So, I'm probably going to want more.
But I I want to show you.
There you go.
See the camera drops.
We still see some ground there.
So, let's stop playing.
Go back to the scene view.
Select this bottom ground piece.
this grass center.
Hit T.
And then I'm going to hold control and grab on the bottom here.
This is going to allow me to adjust the tiling.
Watch the height here as I drag it.
The height and the position really because the position is going to change along with the height so that it keeps tiling and staying at the same locked spot so that it doesn't move.
So there we go.
I've got it to Let's go to Oh, I'm going to I've got it at a five.
I think I'll go to a height of like 10 so that it goes down nice and deep.
That way, if I want to add some water or some lava or other stuff down below, I can do that and it'll it'll still look cool.
All right, so there we go.
I've got ground and deep or deep ground here along with my grass.
I want to add one more thing, though.
Well, first I want to change this sprite tiling issue.
So, I'm going to select all of the sprites in my ground grass folder.
Let's go to list view here so that I can see them all.
Make sure they're all collapsed because if they're expanded, it won't work.
I'll hit control A, select all, and then we're going to change this mesh type to full wreck, and hit apply.
That way, I'll get rid of that warning that was popping up here.
Now, I'm going to save my scene one more time, and then I'm going to go to plastic SCM and say that we've added deep ground and commit.
Oh, get rid of that extra letter there.
And commit.
Now that we've added some deep ground, let's add an obstacle for our player to jump over.
Let's add some water right here to the edge.
We'll go back to our project view and we're going to find our water.
We've got that in here somewhere.
I can kind of scroll through and look for it.
I think it might be under tiles.
Let's see.
Is it in tiles? Yep, there we go.
In tiles.
And I've got a water, a water top high, and a water top low.
Let's zoom in so we can get a better look at these.
The water is that solid view kind of like we've got for the ground for deeper water.
The water top high is a full water that goes all the way up to the top and low is obviously a low one.
We're going to start with water top high.
Drag it out here right next to the grass that I've got.
So I'll drag it out and kind of snap it into place.
Again, I'm going to just even out these positions.
So I've got a position of 1049045.
So, I'll change that to 10.5 so that it's snapped perfectly into place.
Watch what happens when I do that, too.
Look at the position right there.
Change that to a 4.5.
And now it's perfectly lined up.
And I'm going to change this to be -4.5 -4.5 -4.5 so that it's perfectly lined up as well.
Now, we're going to tile it.
To do that, we've got to switch over to tiled mode, of course, and then drag it out.
So, when it's in tiled mode, actually, you know what? This time, let's not drag it out.
Let's do it the other way.
Let's set this to a value of maybe eight.
Not eight, not 58, but eight.
I'll select eight there.
And then I'm gonna hit W.
Well, click over here on the water.
Hit W, hold control, and drag it over here.
So now I've got this water that I think is probably about the width that I want it to be.
I'm going to add some water down below it by clicking on the water here and dragging that down.
Let's just drop it right about here.
Find the correct tiled snapped position.
So we've got a 10.5 here.
It looks like we've got some extra ones.
So, we'll just get rid of those and go to 10.5.
And here on the Y position, we'll go to 5.5.
And again, I just look for the closest value that's within my snapping.
I want to snap by.5s or whole numbers.
So, I try to find the closest number in there that makes sense.
And if I guess wrong, I go the opposite direction.
All right.
So, I've got that in.
I want to tile this sprite as well.
I'm going to change the draw mode over to tiled.
Click on it and hit T, which is going to put us into our rect tool mode so I can hold down control and drag and snap it.
So, first I'm going to go to the right, click and drag and let it tile out.
Then I'm going to go downward.
Before I go down though, I'm going to hold the middle mouse and just kind of scroll down a little bit.
There we go.
And now click, left click, controll, and drag.
And let's go a little bit more.
I'm going to zoom out and do the same.
Controll leftclick and drag until it lines up.
Now I've got some beautiful water there.
Let's save.
Press play.
Go run into the water and see what happens and and how that all works.
So we run run.
Come on.
Come on character.
There he goes.
He goes running running and falls down.
So we're going to need to make a little change to our water.
Add something to allow him to bounce or float or something so that he's just not falling down through the ground.
The first thing that we're going to do is add a collider.
We'll start with a simple polygon collider.
A polygon collider 2D.
If I zoom in, this is again on the water top.
We don't need this on the bottom part.
If I zoom in, you can see that we've got this collider here, but it doesn't line up with our entire object because we haven't checked the autotiling box.
If I check autotiling, now I've got a collider that lines up with my sprite renderer kind of pretty closely and will allow me to run on this thing.
Let's try that.
Let's go turn on the sprite renderer.
Hit play.
Run over there and make sure that we can run across the water.
That's what we should kind of expect to see now.
So, we go over here.
We get onto the water.
And there we go.
We can run on it.
It's a little bit bouncy.
That's pretty good, but not quite what we want.
We want this water to be bouncy like actual water.
So, to do that, we're going to add in another component.
This is a built-in component part of Unity that makes this really, really easy to do.
We're gonna first well first let's go to the water the water top high and the water top low and change all three of these to be full wrecked and hit apply.
So that way our warning here goes away.
When I select the water top high we no longer have that warning there.
Now I'm going to collapse the sprite renderer and we're going to add another component.
We're going to add anector and we want to add a buoyancyector specifically.
So I'm going to clear this out.
Hit just hit the backspace there to remove the search.
Go to physics 2D and we're going to look for buoyancy 2D.
This is anector or a special component that you can add on to a collider that will make it allow you to well it makes it act like buoyant water that will bounce objects back up that fall in it.
So let's click the buoyancyector 2D and take a look at what it says here.
So we've got a use collider mask check box that's checked and a collider mask checked everything.
Okay.
We've also got this warning here.
It says the aector will not function until there's at least one enabled 2D collider with used byector checked on this game object.
What that means is that for this aector to work, it has to know which collider to use.
And you can have multiple colliders on a game object.
So we have to check the used byector box on the collider that we want to use for our water or our buoyancy.
So, I just check this box, used byector, and then we should be able to press play and run over and have our character bounce along in the water.
Let's go try it out.
Notice that we've also got a density and a surface level.
Those are variables that you can adjust to determine how buoyant it is and how high up the character sits.
Now, there's one issue still going on here, and it's that I haven't checked the is trigger box.
If I check his trigger, like that, my character starts to fall down and everything is looking pretty close to how I want except for my character kind of shows up in front of the grass or in front of the water.
I can jump out of here.
Everything looks pretty good.
Let's jump out and then let's figure out how we can fix this.
But also, don't forget the is trigger checkbox when I stop playing is going to get unchecked.
So, first let's recheck the as trigger checkbox.
And then let's figure out how we can move this water to the front so that it's in front of our player.
Remember our sprite layers.
Let's go to the sprite renderer.
Let's go to the sorting layer and hit add sorting layer.
We'll hit the plus.
We'll add a water layer.
And then let's even add a player layer.
Let's take the water layer and make it draw after the player layer.
And then we'll go select both of our water objects here.
change them over to be on the water layer.
And then we'll find our player and let's change our player to be on the player sorting layer.
Save again.
Crl S.
So again, we've got our water, both waters on that water sorting layer.
Let's go hit the add sorting layer again.
Take one more look.
Background default player and then water.
Hit that plus button to add them.
And then we've got our player set to the player sorting layer.
If I press play now, I expect that my player will kind of disappear behind the water.
Let's see if that's the case.
So, I run over here, get to the water, and look at that.
I'm kind of back behind the water.
I can run around and bounce around and eventually fall off the edge of the world because that's as far as I've gone.
Let's now save and go into plastic and say that we've added water to our game.
So, added water to level one and check in our changes.
Now that we've got bouncy water, let's make it a little more interactive and add some sound effects to it as well.
To do that, we're going to need to download some sounds.
And I like this effect set right here, this 40 CC0 water splash and slime effects.
So, I'm going to download this slime effects sound pack.
It's really for the splashes.
And then we'll open up that zip file.
I'm going to look in here, and I think what I'd like to grab is splash number 11 or 12.
I think I'll go with number 12.
So, I'm going to rightclick on it and choose copy or hit control or command C.
Now, I'm going to go back into Unity.
So, I'm going to minimize all of my windows.
Go down to my assets folder and then go to audio, rightclick, choose show in explorer to get this window open and go to the audio folder, rightclick, and paste.
Of course, if you don't see this or you have a different way that you like to do these, um, feel free.
But I'm going to choose paste right there.
If you have a better way that that you like to get files out of zips.
Feel free to do it however you like.
You just need to get it into your audio folder.
Once you do that, you jump back over to Unity.
You should see the sound effect here and be able to click the button here to play it.
There we go.
Now, I want to add this to my water.
I've got a bunch of different ways to do that.
I've got my water here.
I could go down to the bottom and hit the add component option.
I could drag the splash onto it right over here.
I can also drag it onto the scene view here and drop it right on top of this.
I want to show you that, but just be wary when you do this because if you drop it onto another object or there's something in front of it, it's very easy to pop it onto the wrong thing.
But since there's nothing in front of this, I knew it was going to be okay.
And my audio source went down right on the object I expected.
Now, if I hit play, all I'm going to hear is that sound effect play once when we start because play on awake is checked.
Let's hear that.
Cool.
But not what I want.
So, we're going to uncheck play on awake, minimize our audio source, and we're going to need to add a new script, something that plays an audio clip whenever we enter the trigger.
To do that, we'll go to our scripts folder.
So, go up to assets, go to scripts, going to rightclick, choose create, make a new C script, and let's just call this water with a capital W and name it for what it is.
If it becomes something more generic later, we can always rename it.
That's one of the cool things about code.
you can easily or usually pretty easily rename and adjust things to match the new context as stuff changes.
So, we've got our water script created.
I want to attach it to the water top high object.
So, I've got water top high.
I'm going to hit add component.
And look at that.
I've already searched for water, but if I search again, water should show up.
I've got my water script now added on.
And I'm going to save my scene.
Last thing I want to do is open up my code editor.
I'll do that by double clicking the water script.
I can do that right here or down here.
Let's just do it in this spot.
And I should get my code file just like this.
Again, if it doesn't open up the first time, just go back to Unity, double click it again, and it should find it.
Sometimes it doesn't get to the file initially or immediately when you double click on it the first time.
Seen it happen quite more than once at least.
All right, so now we've got our water script.
And our water script by default comes with this start method and this update method.
We don't want to use either one of them.
So, we're going to begin with something that I do often when I'm creating new scripts, which is deleting the start and update method.
So, we're going to select here from the beginning of line seven.
So, I'll hold down the left mouse button, drag all the way down to the end of line 17 so that it's all selected, everything except for those braces, and hit the delete key.
Now, we have a nice empty tiny little class.
We've got a class that does absolutely nothing, but it's ready for us to start writing some code in it.
And the code we want to write is a trigger enter check.
So, we'll say on trigger enter 2D.
And I'm not going to type in the casing because I know it's going to allow me to autocomplete.
But we do need to have capital O N capital T R I G E R and then capital E for enter.
And then 2D with a capital D.
You also have to have the collider 2D part and the collision parameter here.
I'm going to delete the private keyword here.
And then we're going to deal with our trigger enter.
So this code will get called whenever our water's trigger area, that buoyancy area is entered by any object.
So the first thing that we want to do is make sure that we only splash for the player.
Actually, do we want to only splash for the player? No, let's splash for anything.
Let's just make it so that whenever anything enters our trigger, we'll play a sound effect.
So to do that, we'll get our audio source.
We'll say get component audio source.play.
Save that off.
And now if we jump back over to Unity, I think that's really all we needed.
We could add a lot more.
We could make it more complicated, but as it is now, if anything lands in our water, I want to play a sound effect.
So, let's hit play.
We've got a sound effect gizmo on there.
Remember, if you don't see the gizmos, the little button was up there.
Let's run over here, though, and jump in the water and see if we get a sound.
Pretty cool, right? And if anything lands in the water, it's going to get the sound effect as well.
So, let's stop playing, make sure that we've saved our scene, go into plastic SEM, and say that we've added splash sound to water and check that in.
Now that we've got water and a little bit of an obstacle and some ways to jump, let's set up a little level where we can jump across the water and try to get to the end.
So, I want to do that by making some more platforms.
And I've got a couple of platforms here.
I've got my grass mid, grass mid 2 that I've duplicated.
And I could just hit control or command D, duplicate another one, hold control and drag this platform over.
Hold control and hit D again, make another one, and make another one.
And so on until I've got platforms kind of going across the top.
Okay, now let's add some on the ground.
I'm going to take my grass mid and I'm going to take the select it and hit control or command D.
Hold down control and drag it over till it snaps right over here to the right side of the water.
And then I'm going to do the same for the bottom, the grass center here.
I'll hit control D with it selected.
Hold down control, drag it over, and you can see the position looks like -28 and then -10.
So now I've got this nice, beautiful level with a couple platforms I can save.
I should be able to now run across and get all the way from one side to the other.
Let's see.
So, I come over here.
I jump.
Jump up.
Jump.
Jump.
Jump.
Jump.
Oh, almost didn't make that one.
Let's see.
Can I make all these jumps? That's pretty easy.
And I land down here on the other side.
So, this is working.
Okay.
And I can also kind of wiggle through the center.
And I could keep building out my level like this for as long as I want, but it's going to get very problematic very soon.
As you can see, my scene hierarchy is already starting to fill up.
If I start to make a whole bunch more of these grass objects and just keep dragging them out here.
Don't don't copy this part, by the way.
And dragging out more of these platforms and duplicating them and duplicating them.
See that this part's going to get really filled up really quickly.
We're going to have a ton of stuff in our hierarchy.
it's going to get hard to manage and maintain, but we're also going to run into some other issues the second we want to do some updates to our game or change anything in it.
So, we're going to make a couple of minor changes to our workflow.
Now, first thing I'm going to do is delete out a couple of these extra platforms that I've just made.
I'm going to leave this grass center and we'll we'll leave those pieces here for now.
And in our scene hierarchy, we're going to rightclick in the empty area and we're going to choose create empty.
What we're going to do is create an empty game object that's going to work like a folder for our environment.
I'm going to name this thing environment, not game object.
And then we're going to reset the transform.
So go to the transform, rightclick, and choose reset, which should zero out the position, rotation, and set the scale back to one.
So now that I've got this environment object, I'm going to take all of my sprites that are part of my environment.
So that's all of my grasses all the way.
All of my waters and my grass center and the colored grass.
So click here on the bottom one, hold shift and click on colored grass up here.
If you have other things in the way, it's okay.
You can hold control andclick them.
Now I've got all of these selected.
I'm going to drag them and make them children of the environment by dropping them on the environment.
The second they become children of the environment, you'll see that there's an arrow here.
They're expandable.
And now I only see them when I expand out the environment.
I'm going to take these other grass pieces and drop them on environment.
Make sure that you don't drop them on the wrong thing.
If I drop it on colored grass or something, it's going to be not where I want it.
So, I'll click and drag it up to environment.
Drop it onto environment.
I want to make sure that they're all just children of this environment object.
So, now everything except for my player, my spring, and my main camera are children of this environment.
And we're going to do this going forward.
You'll find this a lot of the time in game development projects where especially in Unity.
The game objects are used as folders for organizing your scene hierarchy.
You could have, you know, a thousand things in this list view and if you have to scroll through everything, it's going to make it very difficult to find anything and make it kind of useless.
You'd have to use the search box every time to find anything.
If you have a thousand objects in there, unless you've got a hierarchy that kind of allows you to drill down and expand and find the specific things you want.
So, I know that all of my environment things, the the background and world are going to be in this environment folder.
The spring I've left out because it's more interactive and it's a little bit different.
I want to make sure that that's in its own section.
Now that I've got my environment section, I'm going to save my scene.
We'll go into plastic SCM and then we'll say that we added environment folder and more platforms plus ground.
and we'll check that in.
Now, we're going to continue building, but we're going to dive into one of the most important Unity system.
That's the prefab system.
We're going to start by replacing some of our platforms and creating some platform prefabs.
Let's start by clicking on this platform over here, the one that's directly over my player.
Looks like it's named grass mid one.
Right now, what I'd like to do is add some rounded corners to it so our player can jump up and have it look a little bit better and feel a little bit better.
Have that kind of curve on there.
First thing I want to do is adjust the tile size of this thing.
I want to shrink it down.
I'm thinking I'm going to make it four wide total, including the two blocks in the middle.
So, I'm going to adjust this width from three to two.
And then I'm going to go find the sprites for the edges.
So to do that, I'll click on the sprite here, this grass mid, and it should pop up in the project view down below.
I'll take my grass right that's next to it, and I'm going to drag it on to be a child of this grass mid, the one that I have selected.
This should place it right up here at the top, which is not really where I want it to be.
So I'm going to hold control, grab the little blue bar here, the little blue box, and drag it down where I want it, which should be at a 1.5 on the X and a zero on the Y.
I'm going to do the same for the grass left.
drag it onto this grass mid object so that it becomes a child of that object.
And here I'll go over and type the values.
And I'm going to put it at a negative 1.5.
Move it over that other half a meter because the center of this object is right here.
So it's one meter over and then another half for the center.
And then we'll set that Y to a zero.
That should not two zeros, just one zero is enough.
That should give me a nice pretty platform.
Now I'm going to go to my grass mid and I'm going to rename it.
I'm going to click one more time, hit F2, and I want to call this grass platform 4 because it's four units wide.
Now, let's turn this into a prefab.
We're going to go to the assets folder.
We're going to rightclick on the empty space, choose create, and choose folder.
We're going to name this prefabs.
And you're going to see this a lot in Unity projects.
There are very often prefab folders.
Sometimes it's off the root of the project.
Sometimes there are prefab folders in subfolders, but we've got a prefabs folder.
Now we're going to hit enter to just go into that folder or double click on it and then take the grass platform 4 and drag it in and watch what happens to it.
It turns blue.
It turns blue because now it is referencing a prefab.
And if we go click on this platform, you'll see over here that in the inspector, we now see the prefab that we're referencing.
We have an overrides option, a select option, and an open option.
And I can click on this to kind of go find it in there.
I can click select to find the object and select it in the inspector or find the prefab.
Or I can hit open to go into prefab edit mode.
If you find yourself in here, don't know how to get out, just hit the back arrow right over here in the hierarchy.
Knock you out of prefab edit mode.
We'll talk more about prefab edit mode later, though.
For now, we want to modify our other game objects or our other platforms.
We want to make them be objects that are just like this grass platform.
And to do that, well, I could maybe go in and select all of them and then delete them and then maybe duplicate and put this object in those places, but that's probably not the best way, especially since now I can just have them all selected.
Rightclick, choose prefab, and hit replace.
This will pop up a dialogue that shows me all of my prefabs available, and I can choose the grass platform 4 right there.
Double click it.
And now I've got platforms all the way.
Let's save, press play, and go see if we've got any weird issues or problems, though.
So, we're in play mode.
We run over here.
We jump.
And oh, look at that.
There's no collider on that edge piece.
And that's the same for all of these.
The collider is missing there.
So, let's stop playing and think about how we can fix this.
The best way to do this, well, there are actually a couple ways to do it, and they're all kind of the same, but one of the most interesting and newest ways to show you to do this is to just go to our prefab and doubleclick on it.
If we double click on it, this will show us our prefab edit mode.
This is the one I was just telling you about.
We can expand out the prefab here and see the left and right child.
I can also zoom out and notice that there's nothing around here.
This is just a view to show me just this prefab with nothing else.
So the left and right objects don't have colliders.
All we need to do is select them both.
So I'll select grass left and right.
And I'm going to do them both at the same time so I don't have to do it twice.
And I'll choose add component.
And oh look, I've already got a polygon collider selected.
If you don't have that there, just type in p.
And you'll see polygon collider 2D pop up.
Click on that.
You should get polygons popping up around there.
You can kind of see them.
If I turn off the sprite renderer, you can see them very well.
I'll turn the sprite renderer back on.
And now I'm going to hit the back arrow.
As soon as I do that, it's going to pop up and say, "Hey, do you want to save the changes that you made to this prefab?" If I messed up, then I would hit discard changes.
But since I didn't mess up and it looks right, I'm going to hit save.
And then let's go look at our platforms that are out here in the world.
So now our platform, look at the child object here, the left and right, they all have polygon colliders.
If I go select another one, they have polygon colliders as well.
Let's press play and try this out.
Make sure that it's rounded off.
and our character can jump on these awesome new platforms.
There we go.
Look at that.
It works.
We've got a working pretty cool prefab.
So, let's stop playing and go commit our prefab into plastic.
Say we've added a grass platform prefab to level one.
And we'll check it in.
Now, we're going to look into making more prefabs, some different versions or different sizes of our existing prefabs.
and then eventually some totally different looking versions of our prefabs.
So, let's start by making a larger version of our platform.
Right now, we've got one that's four wide.
And let's say that I want to have a platform that's also five wide.
I don't just want to have them all four wide.
Maybe I want them two, four, six, whatever.
Let's say I want one that's slightly bigger.
Let's make a change to grass platform 4 here.
This second one.
And let's just modify it.
First thing I want to do is just rename it to grass platform five.
So I know that's the one that I'm changing to be five wide.
Then we'll adjust our tile size to be three instead of two.
And notice that it's kind of there, but it's just kind of back behind the ground.
You can't really see our new tiling.
If I go over to the view wall, you can kind of see it breaks the tiling.
Looks weird, but it doesn't look right.
So we need to go back to grass platform 5.
And I'm sure you've probably guessed we need to move these two children, the grass right and left over about another half meter.
So if I grab and control drag, I can snap it over or I can go select it and then choose a value of -2.
So now I've got one that is five units wide.
1 2 3 4 5 units.
So I want to make this into a prefab as well.
I've got a couple of different options here.
First thing I could do is I could hit overrides and hit apply all.
But if I do that, what's going to happen is all of my platforms are going to change to be five wide.
That's not what I want to do.
So I'm going to hit control Z or command Z, whatever your hotkey is, and we're going to instead create a new prefab.
We'll take our grass platform and drag it down here.
And we get a couple options.
We can either do an original prefab or a prefab variant, which might sound kind of tempting, but I'm going to tell you to just avoid that temptation for now.
We're going to look at prefab variants later, but we're going to use them slightly different.
We don't want to use them for the sizes.
We'll use them for our visuals instead.
So, we're going to choose an original prefab.
And now we've got a grass platform 5 and a grass platform 4.
Okay.
Let's say we want one that's six wide.
Here's a quick challenge.
Go ahead and try to make one that's six wide.
I'll let you pause, make that platform, and then resume and I'll show you.
We'll make one that's six and then another one that's two.
In fact, if you want to make the one that's too wide, go ahead and try that as well.
All right, I'll assume that you've already done them.
Let's go through the process.
So, I've got my grass platform 4 here.
I'm going to just rename this and hit F2.
We'll name this grass platform 6.
I'm going to hit F over the scene view to go focus that object and zoom out.
We'll adjust the tile size to be four because I want this to be six wide, which is four plus the two on the edges.
So, I'll adjust that to be a four.
Expand out the children.
Change this child value to be at 2.5 on the right.
And on the left, we'll make it be um negative - 2.5.
Now, I'll go to my grass platform, drag it down, and make this again an original prefab.
Now, for the second platform or the two wide platform, I'm going to do it totally differently.
Instead, I'm going to double click on my or I'm going to single click on my grass platform.
I'm going to duplicate it with control or command D.
This is down here in the project view.
Now, I have a grass platform 7.
I'm going to rename this though to grass platform 2.
We're going to double click on it to open it and view it in prefabedit mode.
This time I want to modify it slightly differently.
We'll do it in prefabedit mode.
Now, to have one that's too wide, I actually don't need anything in the center.
I just need the these two edge pieces.
So, I'm going to disable the sprite renderer and disable the box collider.
I'm going to take the grass right and I'm going to change the value to be 0.5.
And I'll change the grass left to be a value of negative.5.
Now, we've got two little boxes right next to each other.
We have these other components here.
I've left them on just in case we decide we need them later.
But as it is right now, we don't need them.
So, they're kind of extra just sitting there just in case we decide, hey, we're going to go do something with them.
Probably though, what we'll really do is just remove them later.
But for now, we'll just leave them disabled because I want you to see that it's going to work exactly the same.
Now, we're going to go back out of prefab edit mode by hitting the back arrow here and hit save.
And now, we don't have any of those two wide grass platforms in our scene yet.
So, let's go add one.
In fact, let's go select this one.
I'll take this grass platform 4 and let's go replace it.
We'll right click on it, choose prefab, and choose select or no, replace, not select asset, and we'll choose the platform 2 right here.
We can also go to list view if you want to see them by name, but I can tell that this is the two wide one because it it's quite a bit narrower or less wide.
And I can see the name down below.
So, I'll just double click on it.
And now I've got my two wide platform there.
I'm going to save my scene, press play, and run around on these platforms just to make sure that everything is still working kind of as I expect.
So, here we go.
go.
go.
Oops.
Jump and run and jump.
Jump.
This is that two- wide platform.
Yep, seems good.
And so far, I mean, it seems like everything is working pretty good.
Let's go check out our water one more time.
All right.
So, we'll stop playing and we're going to go into plastic SEM and say that we've well make sure we've saved our scene.
We've added three more grass platforms.
Added three new grass platforms.
Or is it three or four? Yeah, three.
And then we'll check in our changes.
Now that we've gone through the process of making prefabs a little, let's do it again.
Let's make a couple more prefabs out of some of our existing objects.
For example, let's take our spring and make that into a prefab so that we can place multiple springs and have them work the same way.
And then if we want to make any changes to them later, we can.
Or if we want to use them across different scenes or levels like we will do, we'll be able to do that as well.
So, first thing we're going to do is rename our spring.
I'm going to go select it, rename it with F2.
Go up here and type S with a capital or capital S.
Just replacing that lowercase S with a capital one.
Then I'll take the spring and drag it down into my prefabs folder.
Now I've got my spring here as a prefab and I've got it down here in the prefabs folder available to drag out here.
So I'm going to drag a spring oh let's say right up here.
Maybe drop it right on top of this platform here.
I'm going to even out or level out my position to a three.
I just like to go in and type out the exact position.
And then here, I think I'm going to go to like a 7.5 and go a little bit to the left there so that it's perfectly lined up with the edge.
And I've got a spring there on the edge.
I'm going to move some of these platforms around so I've got a little bit more space.
I'll hold control and just drag that guy over here.
And I think I'm going to drag this one maybe way over to the right.
I'm going to also increase the size of my background.
I mentioned that we could just adjust this tiling size.
So, let's double it.
And then instead of figuring out the number that's double, which is 160, I'm going to type in the formula for it.
In fact, let's triple the size instead just to make it a little bit harder.
To do that, we'll go to the end of the width here, which is 80.
I'm going to put a star, which is the key for multiplication or the character for multiplication, and then a three.
And then look at that.
It already got wider.
If I hit enter, it'll calculate it out and give me a 240.
Just a cool little thing that you can do in any of the calculated fields.
For small numbers like that, it maybe isn't as useful to you, but for bigger stuff, I found that it can be pretty handy if I need to especially divide things by pi or whatever, you know, some other weird stuff like that.
So, here we go.
I've got my nice wide background.
And now I want to add a little bit more water and maybe some more obstacles.
But I don't want to just duplicate this water.
Again, I kind of want to have um a prefab for this.
And here I've got some options.
I've got to decide, do I make the water on the bottom be part of the prefab or do I just have the top part be the prefab? And in this situation, my general thought is that I want to take my water that's the bottom of this object and make it kind of all be one thing.
I don't like having multiple objects that I have to place.
If I need to do them differently and modify them, I can modify this prefab once it's placed or hide this part or something.
But generally, I'm going to have visible water below my top water.
So, I'm going to make this be a child of the top water.
So, that might sound a little bit confusing, but all you really need to do is click on this water.
Let's rename this to water bottom with a capital W and a capital B because we want to have nice clean names.
And let's go to the top part and name this water.
This is the water.
That's the top.
It's the top part is now just named water.
We're going to take water bottom, make it a child of water.
In fact, let's rename water to be uh no, let's not rename it to be water top.
We'll just name it, we'll leave it as water.
So, now we've got water with water bottom and we're going to turn this water object with its child into a prefab.
To do that, we'll take the water, drag it into our prefabs folder again into the empty space, and tada, we've got another water prefab or another prefab.
Now, we're going to duplicate this water.
And we're going to see something really cool that prefabs allow us to do.
We're going to take this water, gonna duplicate it.
Control D.
So, I selected it.
Control or command D.
I have two water objects.
If I hold control and drag with the red arrow, I can see my second water was just stacked right on top of the other one.
I'm going to drag it right over here so that it snaps right in line with my ground.
Now, if your ground isn't snapping in line, then make sure that this is at a like snapped position, you know, not a decimal point there or at a 0.5 maybe.
And then you have your values, right? Like this.
You've got a solid number here or whole number there.
All right.
So, let's go take a look at it.
If I unselect, you see that I've got my water here, but I still have this ugly line here where I'm not seeing any grass.
Like, I don't see that background view at all.
And I think it looks pretty terrible.
Let's hit play and see what it looks like in game, though.
So, I'm going to make sure that I'm not crazy and it actually looks terrible.
But, we should be getting kind of that uh Yeah, we get the sky blue there.
That doesn't make any sense.
Kind of ruins the water effect.
Makes it look messed up.
So, I want to fix that.
Let's stop playing again and go select our original water, the one that we had here, and let's fix the problem.
To fix it, I want to add something in the background that kind of matches our background of our level.
And we've got really a couple of ways that we could do this.
I could add a sprite onto here.
In fact, this is what we will do.
We'll go to 2D object, go to sprites, and go to square.
And now I've got a background square object.
Look at this a little bit better.
You can see that I've got this square kind of sitting back there behind the water.
Now, if I change the color of this with the eyropper and go pick the same color as my background, now it just kind of blends in.
And I could, of course, just adjust the size of this by hitting tiled mode and then changing the tiling out to be the same size as my water.
Now I've got a background that shows up and kind of looks a little bit better, but there are a couple of issues.
First, let's rename the square to grass.
Background.
I'll call this grass background.
And let's um change this.
Oh, actually, we don't want to do anything with the full rect mode.
We just want to save.
So, now let's go look at our other water.
Ah, look at that.
Our other water does not have this grass background.
We don't see that.
And it's, you know, we've got it here.
It looks like it's probably going to be okay.
But on the other one, it looks like it's going to be messed up.
In fact, let's go play.
Make sure that it looks right before we try to get this to apply to all of our ground or all of our waters.
So, we come over here and it looks okay.
Look at that.
I can kind of bounce in front of it.
Looking good.
And I can jump over here.
And you can see this one's still messed up.
So, let's stop playing and see how we can fix this.
So, since I've made changes to this water prefab, you notice that there's a little green plus here.
This green plus means I've added something to the prefab on this version of it or this object that's placed.
This water down here, the one that doesn't have that, notice it doesn't have the green plus.
Doesn't have this other gray part either, the grass background.
And also notice that this part is gray.
That's because it's not part of the prefab, this grass background here.
So what we need to do is go to the override section of our water.
So I select the water here, the one that we've added the new background to.
Let's just go double click it again.
Go to overrides.
And here you can see we've got the same little highlight, the plus saying that we've added a grass background.
That's what the plus means.
And then we just hit the apply all.
And this is going to apply the changes to our water prefab.
Watch what happens.
I hit apply all and look at the other water here.
It now has a grass background.
And if I zoom out, you'll see that it's got this background showing up.
Now, I'm gonna save my scene and press play again.
I want to run around and just make sure that everything looks okay.
And then I want to show you one more minor thing that I'd like to change before we commit.
So, run over here and look at that.
We can kind of bounce around.
Everything looks okay.
Let's go to the next one.
It looks good.
Okay, cool.
But now there's one issue that you might have run into and I want to show it to you because if you have, it could be a little bit confusing.
If you're looking at your grass background, your sorting layer could be set to water right now.
And if it is set to water, look what happens to your player.
Your character shows up behind the grass and it looks very, very strange.
We don't really want it set to water.
If it's set to default, it'll show up okay because that's behind the player.
But really, we want this grass to be in the background.
We want to set that to the background layer.
So, I'm going to stop playing and we're going to make this change to our object again.
This time, we'll do it on the second water object.
Instead of the first water, let's go to the grass background of the second object.
We'll change the sorting layer to be background.
And then, we'll go to the root object of it, this water, the parent, and go to overrides.
Here you'll see that it now says we have a change.
It doesn't say we have a plus, just a change.
And it's saying that something is modified in our sprite renderer.
If I click the little I there, I'll get a popup that shows me exactly what.
Let's see if I can drag this over and give you a nice preview of that.
So, click the I and we can get a preview showing what has changed.
And it's still a little bit off screen.
So, we're gonna drag this way over.
We'll hit overrides and hit this.
So, what we're seeing here is the original version of the prefab and then what we've done to change it.
And you can see what's changed.
And it doesn't do a great job of calling out everything that's changed, but you can tell right here with the bold text.
It's just the bold text isn't very bold.
So, it's not the most obvious thing.
But, we changed the sorting layer.
That's why this is bolded.
And everything else is that default.
Now I just need to hit the apply button and hit apply to prefab water.
Drag my window back out so you can see it again.
And then let's go check out our other water.
Our other grass background is also set to background layer.
Now I'm going to go to plastic SCM.
And now I'm going to say that we've added a spring and water prefabs.
And we'll check in our changes.
Oh, we got to make sure we Let's hit cancel.
Save the scene.
And now check in our changes.
So far, our prefabs have been somewhat complex, but I've been guiding you through them.
Now, I want to give you a little challenge to build a prefab on your own.
But first, I'm going to give you some functionality for that prefab.
We're going to create a spike that kills the player whenever they touch it.
And your job will be to turn that into a prefab that we can use to reuse throughout our game.
So, to find our spike, we're going to go to the art and tiles folder.
Then down somewhere near the bottom, let's see if we can find them.
We've got a spikes object.
I'm going to zoom in on the scene view a bit.
Let's go over here to the big part between my two waters.
And I'm going to drag a spikes over to our scene.
Now, if it's not set to the right scale, make sure I've selected it and the pixels per unit is 128 and matching the scale here.
I'm gonna go select my spikes and then I'm going to reset the position to let's about a 26 and a negative 3.5 to be just on the ground.
We'll add a polygon collider 2D.
So I'll search for poly 2D and then we'll um I'll set it to tileable mode.
Now that it's in tileable mode, I'll set it to be too wide and then make sure that the autotiling checkbox is on.
The final thing I need to do is make it kill my player when they touch it.
So, I'm going to create a new script that kills the player when you touch something.
I'm going to go into my scripts folder and I'm going to rightclick, create a new car script, and I'm going to call this spikes cuz that's what it is.
It's a set of spikes.
So, we'll create our spikes script.
We'll go to the spikes object and drag the spike script onto it as soon as it finishes recompiling.
Got to give it a second.
that happens when we create a new script.
So, I've got my spikes script there attached to my spikes object.
I'm going to capitalize the S here because I want my naming to be nice and clean.
And then we'll go open up the spikes script.
Inside the spike script, we're going to do the same thing that we did with the other script that we created.
We're going to delete our start and update method.
So, I'll select at the beginning of line seven all the way to 17 at the end of 17 and then press delete or backspace on the keyboard.
Now, we're going to check for a collision enter.
Remember in our water, we checked for a trigger enter to see if we went into the water.
Spikes aren't going to be triggers.
They're going to be actual colliders that things could land on.
And if a player lands on it, well, it'll kill the player.
So, let's go back to our spikes and instead of adding an on trigger enter, let's add an on collision enter.
So, I'll type O N C L and find that on collision enter 2D.
We got to make sure it's the 2D version.
I'm going to delete my private keyword because I just don't need it.
It's private by default.
And then we're going to check if our collision 2D was a player.
So we'll say if collision dot and here we need to get the collider.
We don't we're not able to do a compare tag because collision 2D isn't the same as a collider 2D.
A 2D collider is the object that you're colliding with.
A collision 2D is like this data object that has that collider, but it also has some extra info like how you how the object collided, where they collided, like what the specific points were.
In a trigger, we don't get that info.
So, you get back the simpler object of just the collider 2D.
In fact, if I go look at the water, you see that we get this collider 2D.
But in the spikes, that's not what we're getting.
We're getting the collision 2D that has a collider on it.
again because we've got more information on a collision than we have with a trigger.
So if the collision collider compare tag because we can get the tag from the collider here and we pass in player.
So this is going to tell us if the collider has the player tag on them.
Then what we want to do is kill the player.
And to kill the player, the easiest thing we can do, the the kind of default starting thing we can do is just reload our current level.
So to do that, we'll say scene manager.load load scene and then we just pass in a zero.
It's going to reload the first scene in our scene index.
And we'll talk about our scene index and our build indexes and all that stuff in just a moment.
First though, let's save.
Make sure that everything looks good.
We'll go back over to Unity and then we're going to run over and touch those spikes and see what happens.
So, we'll save our level here.
We need to make sure that we've saved our scene.
Press play.
We run over to our spikes and go touch them and we reload into our level.
Now, if you're not reloading into the level, what you're going to need to do is go to file and build settings.
And you may have something else in your scenes and build.
If you're loading into some other scene, you're seeing, you know, something weird, some demo scene or something else, it's because you have something else in your scenes to build.
Perhaps you have the old sample scene.
So, what you need to do now is while you have this window open, and even if you haven't had no problem and yours looks just like this, hit the add open scenes button.
And then let's make sure that this first entry here is deleted.
So, I'm going to go select it and hit delete.
We want our scenes and build to just contain scenes level one.
And that's it.
Then we'll close it.
We don't need to do a build or anything else.
We're going to go to file and save project.
That should in plastic SEM update our editor build settings.
We should have our level one saved or our level one showing up there and our spikes.
Let's do a commit.
Say we added spikes and level one to build settings.
And we'll check in our changes.
And now your job is to turn your spikes into a prefab that you can reuse so that you can have it scale all the way across here or be a tiny little spike up here that you place however you want.
So go ahead and give that a try.
I'll let you pause right now and then continue on and I'll show you how to do that.
All right, I'll assume that you're done.
Let's go through the process.
So, let's go back to our project view.
Let's go to the assets folder and go to our prefabs folder.
I'm going to go select my spikes.
And the first thing I'm actually going to do here is adjust the tiling.
I'm going to set the tiling down to one because I don't want the default to be two tiled wide.
I want to start with a very small one on my prefab and then just allow my user or my designer or myself to scale it up to whatever I want.
So, I'm going to take my spikes now.
I'm going to drag this into the prefabs folder.
And tada, I'm pretty much done.
Now, I can take this spike object.
I can drag it up here on top of this platform if I want.
Then fix up the position.
So, we're looking at like a 24.5 and a three.
And then just adjust this scaling here by modifying the the tile size.
So maybe I want to set this to a four like that.
Now I've got one that fits all the way across a 4x4 platform.
I don't need to make another prefab for it because it just fits.
This is kind of the benefit of a prefab.
I don't have to make an object for every size.
I can override and modify the specific parts that I want.
Now when it came to our platforms, this not such that not so much the case because we had those two edge pieces.
But with the spikes, we don't have that problem.
We can just make it whatever size we want and place it wherever we want and then scale it up without having to create multiple different prefabs.
I like this.
So, I'm going to save my scene, go into plastic SCM, say that we've created our spike prefab, and check it in.
In this section, we're going to learn how to use source control to see what we've done, review what we've learned, and kind of get a good overview of what our project looks like.
The first thing I want to do is go to our plastic SCM window.
And right now, we've got pending changes open.
I want to go to the change sets tab.
It's kind of hard to tell that these are tabs, but that's what they are.
And if you look in here, you'll see that you've got quite a few change sets.
Your count might be slightly different from mine.
I've got 40.
I've probably added a couple extra that you haven't seen.
I'll show you what those look like in a moment.
But overall, you should have just about the same number with probably very similar commit messages.
You can scroll all the way through all the way down to the bottom and see even the first commit message which was at zero which kind of happened automatically.
And number one, added packages and project settings.
This happened automatically too.
So the first commit that we did was our art imported and level one.
And if I click on that commit here, you'll see that it shows that we added 457 files.
This was our biggest commit when we pulled in the entire art package from Open Game Art.
Remember, you can also go to Kenny Enl's page.
She's got a whole bunch of great art available there.
You can download lots of cool stuff and pull it in later, but for now, this is the one that you need.
So you've got this one in and we pulled this in in pack number or in in commit number two.
We also went on to add in a player script.
And here you can see this is where I actually have more commits than you do because I added my player script and then I moved it to the correct folder.
So I had to delete it and then read it and I had some extra commits that I didn't put on camera and I forgot to delete beforehand.
So let's take a look at our first commit where we've added a player.
So, you've got the one where you say added player script and attached it in level one or something similar.
You should see over here to the right you've got added and you've got a scripts and a plus meta and then you've got player.cs plus meta.
So, when you find this part and it's probably a commit message looking something like this.
It's one of our first ones.
Right click on it and hit the diff button.
Not diff meta but just diff.
This is going to pop up a source control diff tool that'll show us the difference between our previous version which didn't exist and our first version or the version that we've clicked on which was version right here.
Mine was at number five.
And here you can see that we added the line that logs updated at the current time which remember time is the current time the game has been running in seconds.
So at 0 seconds in, it's zero.
At 1 second in, it's one.
At 10 seconds in, it's 10.
And so on.
But there's usually some long decimal there.
So this was our first version.
There was nothing to compare.
Let's close this.
Let's go up a little bit further.
Let's go find the part where we added jump velocity and duration variables to our player.
And then let's right click on the player and hit diff.
This will show us the difference between the part where we added these variables and the part the version of it that we had before we added the variables.
So this is when we added our two serialized fields for jump velocity and jump duration.
This allowed our player to jump up higher or further.
Well, really it allowed us to do that to control that through the inspector.
So we could control how high they jump without having to hardcode it.
Come back in here and change the values.
Let's go take a look at what that commit was like.
Let's say we want to go vi revisit that commit.
I'm going to go right click on commit number nine and I'm going to hit switch workspace to this change set.
I hit switch and that's going to change my local version of the game.
I'll hit reload over to exactly what we had on commit number nine.
Don't worry though, everything's still available.
I can get back to my previous one.
I'll show you how to do that in just a moment.
Let me hit play though and go check it out.
Make sure that we've got those jump variables working.
That's what we added in this version, right? So, I could jump and I could go left and right.
But remember, there's unlimited jumps when we started out.
So, those are available.
And if I go over here and select my alien, I can see, let's see, where are my fields? Right here.
Jump duration and jump velocity.
Yep.
So, that that seems about right.
I could change this to like a 15.
And oh, yeah, he goes flying.
So, that's cool.
Now I remember that's what those fields were.
And I if I want I can even double click on the player script, allow my code editor to reload it and go see that version of the code right here, go modify it or maybe share it with somebody or whatever it is I need to do with it.
I now need to just go back to Unity though and see something slightly newer.
Let's go back to my change sets.
Any second now, we should be able to click on change sets.
There we go.
And let's scroll through and find another commit.
So there was the part where we added our walk animation to the player.
In this commit, we can see that we added our animation folder.
We added that controller and we added the walk animation that we recorded it.
Let's go take a look at it.
Let's switch our workspace to that.
Or at least I'll switch mine.
We'll reload and we'll go take a look at that player and the animator controller that we added to the player.
So, we've got the player here.
The player has underneath it the animator and it has the controller on it.
The player's animator controller has this player walk animation.
And at first, remember, it just looped.
It just played over and over.
If I press play, remember it just continued to go and go and go.
Let's see what that looked like.
Oh, remember no matter what I did, it just constantly walked.
Do you remember how we fixed that or how we changed it? Let's go back into plastic and take a look.
We'll go back to our change sets.
Let's go find one slightly newer.
We can find the one that we're on.
It's bolded here, line 16.
Let's say that we want to go to the next one where we've added animator controls to jump for jump and idle.
So here we'll switch the workspace to that change set.
And let's also do a diff on the player.cs file and see how we modified the way that we interacted with the controller.
So I've got to go back to change sets.
It is kind of annoying how it bounces over like that.
But I go back to change sets, reselect my change set here where we added animator controls.
And I'll hit diff again.
We'll pull up the script and then we'll go look at it.
So here remember in our update sprite method we actually just called into our animator and we told it to set a boolean of whether we are grounded or not.
So we set is grounded to true or false and then we set the float for our horizontal speed to the absolute value of our horizontal speed which as you remember just removes the negative sign if there is one.
Let's go take a look at what that was like in game or in our editor I guess really cuz what we care about is the animator.
Remember the animator has our grounded check and our horizontal speed parameter.
We added those by hitting the plus button and choosing the parameter type and then naming them.
And then we've got transitions.
We start by going into player walk.
If we're not walking, so if our horizontal speed is less than 0.1, we go into idle without has exit time on so that we can skip past and go instantly.
We don't want to blend.
If we start walking, our horizontal speed gets greater than zero.
We go back into walk.
And then for our walk to jump, we just check to see if we're not grounded.
And if we are grounded, we go back into walk.
And then from idle to uh to jump, it's the same except when we leave jump, if our speed is less than 0.1, we go into idle instead of to walk.
And we've got, of course, the has exit time.
Oh, has exit time is actually checked on these.
Probably shouldn't be.
And if it is in our latest version, we should uncheck that.
So let's see how we get back to our latest version of the code.
or the our project.
We go up to our top commit here, rightclick, and hit switch workspace to this change set.
And of course, tada, we're going to be at the latest version.
So, oh, we've got to let it reload.
Let it reload here.
Our level one will reappear.
Our scene view should show us everything.
It might It's reinstalling the Cinem Machine package.
So, it takes a second to do that.
Bounce between.
And remember, we added our Cinem Machine package, too, to control our camera and have it follow our player around.
Now, I want you to just go ahead and take a look at a couple of your other commits.
Maybe go check them out.
Go switch your workspace to them and take a a quick peek at them.
Whatever you do, don't go delete them.
You can't do that from in here.
You have to do it from the plastic SEM tools, the external one.
Don't go modifying and deleting them.
But inside of Unity right here, just go switch to them.
See what you want.
Don't hit the revert button.
Just hit switch or hit diff and see what you can kind of glean from it.
Even if you don't completely understand what it's showing you or what you're seeing at at all, just play with it a little bit and see kind of what comes from it.
I think that you'll start to understand it more and it's going to become a very important skill long term for you.
And then in the next section, we're going to dive into a lot more of the code and talk through some of that some more.
I'm back on the latest version of our project and now I want to talk through the code a bit.
I want to make sure that everything kind of makes sense or maybe totally makes sense and hopefully answer some questions that might have been bouncing around in your head.
So, we're going to take a look at our four scripts that we have and see what we can learn that maybe we haven't learned already or what we can kind of figure out from these just reviewing them.
We're going to start with the water script.
We'll start right at the bottom and work our way up to the top.
So, our water script was very basic.
It doesn't have a lot to it.
It's got a couple lines up at the top that we haven't really talked about at all.
It's got the definition of the class, the public class water, and that colon and the mono behavior, which if you remember before I told you is the thing that we need to make it be possible to have it as a component.
If I don't have the word mono behavior in there, this water just won't work as a component.
I won't be able to put it onto my objects.
In fact, let's see what that looks like.
Let's delete out the colon and mono behavior.
I'm going to save.
And look at this.
I've already got an error.
It says get component doesn't exist in the current context.
And that's because git component is part of the mono behavior.
So, let's let's just comment this out, too.
I'll just put two forward slashes.
And I'll save again to make it so that I can compile.
We don't have an error at least.
And go back over to Unity.
If I go into here now and I select my water, I'm going to see that my water component has disappeared.
Oh, it says, yep, there's now a no missing or a missing script.
I guess it didn't completely disappear.
It says the associated script could not be loaded.
Please fix any compile errors.
If I remove this component because it's no longer working and I try to read add the water by dragging it over, it's going to tell me that I can't add the script water.
The script needs to derive from MonoBehavior, which means that it needs that colon MonoBehavior.
So, I'm going to reopen it.
Actually, let's go into source control and I'm going to undo my change in plastic SCM.
So, I'm going to go to plastic SCM, find my pending change, rightclick on the water, and hit undo changes.
That's going to revert or undo my water deletion or my my water line model behavior part deletion.
If I go back to the water script, let's go find that water script.
Here you can see it's reattached and the code is back.
So, we've got the colon mono behavior which again tells it that it's a component that can be added to a game object.
And then inside of here inside of the braces, which is inside of our class, this brace is the start of our class.
This braces the end of our class.
We have one method, the on trigger enter 2D method.
Again, if we build a 3D game, we'll use 3D components.
So, we'll use a rigid body and on trigger enter and a collider.
In 2D, we always have to use the 2D ones.
We have the ontrigger enter 2D that passes in a collision or an object named collision.
That's actually a collider 2D.
And a collider 2D is any of these colliders, a polygon collider 2D or if you look at our player, a capsule collider 2D, anything that's a collider 2D like that will could be an object that's passed in.
And that's because all of these classes, these capsule collider, polygon collider, etc., they all also inherit or derive from a collider 2D class.
Now, you can't see that.
Well, you can if you try to dig into it, but you don't need to see that.
It's not something that's visible.
But they essentially look like something collider 2D colon collider 2D in their code.
So, it's going to pass that collider in and then we just play the audio because we don't care what hits the water.
So, we get the audio source component and then we tell that audio source component to play.
Now, what happens if we don't have an audio source component here? Think about this for a moment.
If we don't have an audio source component attached to our water, what's going to happen on line 9? Well, if you think about it for a moment, what's actually going to happen is get component for audio source is going to return back nothing.
It's going to return back null or no object or nothing at all.
And then it's going to try to play on nothing and that's just not going to work.
You're going to get an error saying there's a null reference exception.
It's the most common error that you're ever going to see.
So, it's something that you're going to want to address.
So, why don't we just make a quick change here and make sure that we have an audio source.
And to do that, we can add a question mark and save.
What that will do, and this is a cool little trick, is check to make sure that the thing to the left of the question mark is not null or does exist so that we actually get one back.
and it will only run this play method if we have an object here.
So, if we got something back.
So, I guess cool little review and a little tip or trick.
Something that you should probably understand and we're going to be using quite a bit throughout our game development.
And if you've never seen that question mark there and you've only seen the dot, hopefully this clarifies it quite a bit.
It just checks to make sure that the component or the thing doesn't necessarily have to be a Unity component exists before calling the method on it.
Let's save that off and then go commit our change to plastic.
So, we've added a null check to our water script.
That's what we're going to say.
Go to plastic SCM.
Say added a null check to the water script when playing audio on trigger.
Enter.
And check that in.
So, let's go on to our next script.
We'll go back to the project view and take a look at our spring.
Our spring was a little bit different.
Our spring doesn't get the audio source every time we touch it.
In fact, we cache our audio source, which is something we might want to consider doing for our water.
It also caches our sprite renderer and our default sprite right here in this awake method.
So right at the beginning of our execution or our life cycle of our spring object, we save off all of these different components.
And we do that well for ease of coding in case we want to use it multiple times, but primarily for performance.
Calling this get component every single time will eventually cause performance issues.
It's not going to cause performance issues for our game even if we did it every single time.
But it's a very important habit to get into just caching this because if we build anything bigger, we start to scale up or we want to start to target smaller devices, lighter platforms, and we really need to get into the per the habit of optimizing this performance.
And it's very easy to do.
We're going to talk a lot more about performance later on.
So we cache all three of these things in awake.
And one of those things is not a component.
It's actually the current value of our sprite renderers sprite.
So our sprite renders the component and we get the current sprite and use that as the default.
Remember that's the unsprung version of our sprite.
And then we use the on collision enter 2D methods instead of on trigger enter because we have these set up as actual colliders and they're colliders that are set up to be bouncy.
So when we land on it, it bounces our player.
And remember how we do that in just a moment.
We'll go take a look at it.
But when we hit the object, we actually check to see if the thing that hit was the player by using the compare tag method.
And if so, we swap the sprite and then ch play play an audio boing sound.
And then when we leave the collision, so when our player bounces off away from the spring, we set the sprite back to its default value.
So that's why we cached the default sprite.
Let's go take a look at that spring again.
We go look at our spring.
We've got our box collider and its material.
Remember we created a physics 2D material is set to spring and that value has a bounciness of one and a friction of zero.
Let's go look at that spring one more time.
See what other components we've got.
So we've got our box collider.
We've got our spring with that sprung sprite on it.
And then we've got the audio source.
That's pretty much all we needed for the spring.
It's nice.
It's pretty tight.
It's a simple little script.
So, let's jump over to one more script.
We'll take a look at our spikes.
Our spikes are very simple.
They also use the on collision enter 2D.
And here we check to see if a player hit again using that compare tag.
And if so, we load scene zero, which is again just loading the first scene in our build index.
Let's go take a look at both of those things.
First, let's see our player.
And remember that we've got this player tag in the tag section.
Remember that's different from layers.
Layers are used for collisions and physics.
And tags are used for game logic.
We can also access layers for game logic if we want, but usually tags are kind of the default for that.
At least the player tag.
That's very common tag to have.
So we've got our player tag here.
And then we've got our file file file build settings and our scenes to build.
This is where we got that load scene zero.
Notice the zero right here.
That's the build index.
So level zero was this one.
We could also load it by calling the name saying load scene and then passing in quotes level one.
But we're going to do more level loading in our next setup set of sections.
So, for now, we're just going to close that out.
And I think we'll wrap it here and then continue on to the player script in the next section.
All right, it's time for the big script, the player, the one that's doing most of the work in our game.
Let's open up the player script and start at the top.
So, up at the top, we've got these using statements.
And I've mentioned them a couple times.
We've kind of ignored them, but I want to briefly talk about what they are.
These statements allow your code, all of the code below them, to use specific libraries or systems.
They allow your code to use things that it might need to use that you wouldn't want to have to write yourself.
Things like lists of objects or random number generators or Unity components, which is why we have the Unity engine one here.
If we didn't have this using Unity engine statement here, if I just deleted it, the MonoBehavior reference is going to disappear.
Serialized field, sprite, layer mask, all of these things, the game is no longer going to know about them because they're all in that library.
They're all in the Unity engine library.
So, I'm going to undo that, bring that using statement back in, and make sure that my code knows about all of these things.
And you might see these two gray ones here and wonder, why are they light gray? That's because these ones just aren't being used right now.
So, I can actually delete them just by holding shift and hitting delete and shift delete and removing them.
The reason that they were there though is that those are very common ones that are often used in game development and writing code.
So, it just puts them there kind of by default.
We can remove them though because we're not using them right now.
So, let's get rid of them.
Let's take a look at the next line.
We've got line four, our public class player inherits from MonoBehavior.
I think we've talked a little bit about that.
Probably don't need to talk more about it.
And then we've got a private float jump end time.
Now, one thing I'm noticing is that this float is surrounded or kind of like followed by some serialized fields.
And then there's more floats and other private variables down here.
So, I'm inclined right now to just move this line down here to line 21.
So, I'm going to hit shift delete and move it down to line 21 so that it kind of lines up and is in in line with my other jump private fields.
Then I'll delete line six here.
I like to keep my code nice and clean and organized so that it's easier for me to find things.
So now on line six, I have a starting block of serialized fields.
And remember this attribute here with the square braces makes it so that our variable will show up in the inspector.
If I save, go over to the inspector, I should see horizontal velocity, jump velocity, jump duration, jump sprite, layer mask, and foot offset all in that order on my player.
Let's go double check.
make sure that I'm not crazy and we're seeing the same things.
So, we go look at our player.
We expand out the player script and there we go.
We've got all of those fields in the same order and we have is grounded.
So, let's go back to our code down here.
We've got that is grounded right afterwards.
And remember that this is public which also shows up as or in the inspector just like the serialized field.
Now, the reason that this is public, well, we haven't talked about that yet.
We're not going to talk about it right now.
We we'll talk about public and private stuff a little bit later, but for now, we're going to continue on.
And just know that when we have something that's public, it can be accessed by other code outside of the player.
And when we have something that's private, it cannot be accessed by other code outside of the class.
And that matters, well, it matters for this because some things are going to want to know if the player is grounded.
But nothing else shouldn't need to know about our foot offset or our jump duration or jump sprite or anything else.
Some objects might need to know if we're on the ground though, so we make that publicly available.
All right, next up we have our private field.
Starting on line 15, we've got a sprite renderer that we're caching in our awake.
We've got an audio source that we're caching in our awake.
And we've got an animator that we're caching in our awake.
I'd like to keep all three of these components in the same kind of order or next to each other.
So, I'm going to move this animator right up here and then delete out line 19 just to keep them kind of in order.
And in fact, since they're components, I'm even going to add a space to separate them.
This is something I highly recommend you do with your code.
Keep it clean, keep it organized, and just go through and when you just need a break from thinking too much, just start cleaning up your code.
Just reorganize things.
Just make sure that it works and that you've got source control so if you accidentally delete the wrong thing, you can go back and undo it and fix your problem.
All right.
So, we've got our three components that we cache in our awake.
And then we've got our horizontal value for where we're p pushing left and right, our jumps remaining, and our jump end time.
So, this is when our jump is going to end and how many jumps we have left.
We've already talked about awake enough that I don't think we need to explain what caching looks like or what we're doing there.
So, we're going to minimize that and look at the gizmos.
Remember, gizmos only show up if you have that little world popped on, and they don't interact with the world at all.
They're just for the scene view.
And in our onraw gizmos, we do a couple of things.
First, we get the sprite renderer.
And I guess it's kind of important to note that we can't just use the sprite renderer from awake because awake isn't necessarily called every time when on draw gizmos is.
If we are not running, we're just in the editor, awake's not going to be called.
So, we need to actually get the sprite renderer.
Then we set the color of our gizmos to whatever color we want to draw in.
Whatever color is set is the color that the next gizmos draw line will be in or gizmos draw anything.
Then we've got our origin right below that on line 35.
We declare an origin and we use our current position minus our bottom or our extents of our our bottom there.
So we get the position right at the bottom in the center and we draw a little line from our origin downwards 0.1 m.
We do the same for the left and the right foot just by subtracting and adding the foot offset.
Then we've got our update method.
Remember this is where all of the magic kind of happens.
This is the core of our game logic right now.
We've got an update grounding method that updates whether or not we're on the ground.
If we look at it, it has the is grounded value getting set to false.
And then we do a raycast downward just like we did with the gizmos, but we're doing a raycast instead where we get back a raycast hit.
If we hit something, anything at all right now, then we set is grounded to true.
Otherwise, we just leave is grounded to false.
So, first we check in the center, then we check in the left by com just doing that same ray cast, and then we check on the right.
Now, theoretically, if we've hit once, we probably don't need to check all the other ones.
If we hit in the center, we don't need to check the left and the right.
It's somewhat inefficient, but for now, we're not worrying about speeding that up and optimizing it.
It is something that we'll be addressing soon, though.
And then on line 97, we just check to see if we are grounded and we're not um we're not flying upwards, then then then yes, if our or so if our velocity is less than or equal to zero.
So, we're either at zero or falling downwards.
So, not flying upwards.
Then we set our jumps remaining to two so that we can jump again.
Now, let's go back up to our update.
And the next thing that we do is read our horizontal input.
And again, we're using the old input system, but we're very soon going to switch to the new input system.
And it's going to look a little bit different.
So, we've got the old input systeming using get input or input.get get access horizontal which gives us the left and right value which is the arrow keys A and D or remember it also is the thumb pad or the thumb stick here the left thumb stick on a normal controller.
So it gives us a value of negative 1 to positive one depending on if we're pushing all the way to the left or all the way to the right.
We log that value out which we probably don't need to keep doing really.
It's kind of obnoxious.
So I'm going to delete that line right here.
Line 53.
And then we'll go down to line 54 where we get the rigid body component.
And then we set the ver or we get the current y velocity of our rigid body and set that in vertical.
But don't we already cache the rigid body up in our awake? Let's go take a look.
So we don't cache our rigid body in awake.
And that's something that we should probably do as well.
So we're going to make that change now.
We're actually going to go up to the top and we'll replace this code here and say underscore rigid body.
Actually, let's do RB since that's what we've done before.
RB equals get component.
And we'll put in a rigid body.
But we don't want a rigid body.
We want a rigid body.
2D.
Very important that we get the 2D one.
I'm going to generate a field for it.
And then we'll add another space.
We'll get rid of that private keyword.
And then we'll scroll down.
So now we've got a cached rigid body.
And we'll delete line 56 and add an underscore to our vertical.
Look at that.
I already feel better about our code.
You'll see down here on line 72, we've got an error.
We'll talk about that in a moment or we'll fix it in just a moment.
So, we get our vertical velocity from the rigid body, our current vertical.
So, if we're going up, we know that value.
If we're falling down, we know what that value is.
And then we check to see if the player has pressed the fire one button because we're using that to jump.
That's our left click or left control.
And they have some jumps remaining more than zero.
So if the value is greater than zero and they've pressed the jump button and remember get button down in the old input system is the frame when they've pushed the button.
So it's not if they're holding the button but if they push the button this frame then we set their jump end time to the current time plus the duration of a jump.
So if it's 1 second jump then we would set it to the current time plus 1 second.
So that way we know hey that at 2 seconds in the game if we start did this at 1 second we add another second at 2 seconds in their jump needs to end and we'll use that later on in our code remember then we decrement their jumps remaining by using the minus minus which just removes removes one or reduces it by one.
We set the pitch of our audio source so we can get that cool effect based on how many jumps we have.
And here we're using that conditional operator.
So if jumps remaining is greater than zero we set the pitch to one.
If it's less than zero, so it's not greater than zero or equal to zero, then we set it to 1.2.
And then we make the audio source play.
We could probably delete that space on line 64.
I'm going to do that.
Line 67, we check to see if they're still holding down the fire button.
Remember, this is the frame that they clicked it.
This is the button any every frame that they're holding it down.
Get button will return true.
And it's still an okay time.
and we determine it's an okay time by saying that the end time is sometime greater than the current time.
So if we haven't gotten to the end time, they're still holding the button down, we let them keep going up.
So we keep setting their vertical value to jump velocity.
And imagine that their vertical value is like a positive three.
So they're going up 3 m/s.
As long as they're holding the button, they're going up 3 m/s.
Otherwise, they're going to start falling down based on the rigid body.
It's going to start pulling it down with gravity and falling on its own.
And so it'll be three, then it'll be like 2.9, 2.8, 2.7, and so on till it starts to get to negative values and falling down.
Then on line 71 where we've got our error, we set the velocity of the rigid body to our newly calculated value.
Let's uh add an underscore there.
Oh, and talk about line 70 where we multiply our left and right speed by our horizontal velocity value.
And remember that was a serialized field controls essentially how fast we run.
I'm going to go back and then take a look at the last bit of code here.
Line 72, we call update sprite.
If I hit F12, you see that it actually updates our animator and our sprite.
So, it probably needs a rename, but we're not going to do that yet.
The animator gets a boolean set for whether or not it's grounded to modify its jump sprite mode.
So whether or not which shows a jump sprite and then it gets a float for its horizontal speed which passes in that absolute value of the horizontal speed which is just that value without the minus sign.
Then if they're going to the right we flip or we set flip X to false so that the sprite's not flipped and it's at the normal mode.
And if they're going to the left we set flip X to true so that it flips over.
And if they're not going anywhere, they're not pushing left or right, then we don't flip it.
So they stay whatever direction they were facing.
That is the entirety of our player script.
So hopefully we now understand everything that's in here because we've got a lot more code to write, a lot more really cool stuff to do, and things are going to get a lot more, I think, interesting and fun.
All right, let's save this off.
We'll go back into Unity into the plastic SCM window.
We should have a couple of changes here to commit.
So I want to get this window open.
We'll do a diff now since we've been doing those.
We'll right click on this player and hit diff so we can see our changes before we commit them.
The minor modifications we've added, we moved the jump time down so that it was in a better space.
We removed some unused using statements.
So this is showing us that those were removed.
They used to be there.
Now they're not.
It's showing us that our animator kind of got moved around.
It got deleted and then readded down here.
And let's see, our rigid body component is now being cached.
If we scroll down further, we'll see that we're using the cache rigid body in both of those places.
And that's pretty much all of our changes.
So, I'm going to close this window.
We'll go add in a commit message that we cleaned up the player class a little.
And we'll check that in.
Before we add more complexity to our game, we're going to add a service to make things easier.
Specifically, we're going to make it easier for us to share our game with friends, family, or other students.
and we're going to do that by automating our build process.
To start, we need to go to the services window and we're going to hit explore.
This should bring up the packages manager with all of our services available.
It's going to go to this services tab and I want to find the cloud build package that's inside the DevOps section and then choose install.
This is going to install the build system that allows me to automatically get a build whenever I do a commit with plastic.
So, I'll do a commit or a checkin and a build will happen automatically that I can share with other people without me having to go through a manual process, upload a file or anything like that.
So, once I've started and I've imported it, I'm going to get this link Unity project option.
I'm going to need to go to my project settings and set up my project with my Unity account.
So, let's do that now.
I'll hit the project settings button and I'm going to choose new link.
I'll select an organization.
I'll use my organization that I have and hit create project ID.
This is going to give me a project named Alien Blaster.
And it's going to ask me right down at the bottom whether or not this is targeted at children under age 13.
I'm just going to say no because it is definitely not.
It's not really targeted at anybody.
And then we'll hit the save button.
Now I'm going to go to my cloud build section.
So now notice that we have a cloud build option underneath project settings.
And right up here in the top right corner you can see that it's not turned on yet.
So I need to check it and enable cloud build.
Once it's enabled, it'll update in here and it's going to give me the option to upload a build, add a target, or add or look at my build history.
But what I really want to do is I need to add a target.
And I want to do that well here.
Let's just hit the add target button.
It'll open up my dashboard.
Say I want to do it through the dashboard.
But that's what it's going to do.
It's going to open up my dashboard.
So I'll open up the dashboard.
It's going to have me sign in.
And if yours initially looks like this, it's fine.
Just hit that take me home button and it should look like this.
And if you see this section right here, it says latest builds, no builds, and you've got a cloud build section.
I can just click on this, go back to my build section, and then I need to set up a build target.
It says no build available yet.
So I'll hit set up a build target.
And then I do have source control.
So I'm just going to hit get started.
And then we need to choose our source control type which is going to be plastic SCM right up at the top.
And next we need to put in our source control provider URL.
And you put the mouse over you see that it wants your organization atcloud and mine is gamecourses atcloud.
Yours is going to be different though.
If you're not sure what yours is, make sure that you go to your project and look down here at the bottom right.
Mine's alien blaster at gamecourses atcloud.
Yours is going to be something else.
Whatever you set up the name of your organization as, that's what it's going to be.
So, it could be Alien Blaster if you use that, but only one person could have that.
So, I'm sure it's something else.
So, make sure that you put in the correct organization there.
And so, your organization name at cloud.
We'll leave authenticate with Unity ID on everything else default.
And hit the save button.
This should create or link up our source control.
There we go.
says, "Our settings have been successfully saved.
Now, I'm going to go over to the configurations window.
I'm going to hit the quick target setup and we're going to choose a WebGL setup.
What we're going to do is have this build us a WebGL version of our game so we can play it in a web browser and then just share that with other people very easily without even having to send them an executable.
Now, it's got the option here.
Well, it has a couple options.
First, there's a repository option.
I've got lots of projects.
It knows which one I want, though.
Alien Blaster.
So, we're going to use that.
And then it wants to know which branch to use.
We only have one branch, which is main, and we're going to stick with that.
We don't need a subfolder, and we can allow it to use the latest 2022 or build with the one that we have.
I'm just going to allow it to use the latest.
And then we'll hit next.
And we can let it build from a Mac.
I don't really care what system it's building from.
It's for a WebGL build.
And then we've got some options for scheduling.
Do we want to auto build whenever we get a new repository update? Do we want to auto cancel? Which the answer to that is yes.
So I'm going to check it.
Do we want to auto cancel if we have a build pending and a new build is triggered? Probably.
So if we check in and we check in again, do we want to build all of those versions or we just want the latest? I think just the latest.
And then do we want a recurring or repeating build schedule? So if we don't want one every time, we might want to have like a daily build or every two hours or whatever.
I don't want that though.
I just want every every time I commit to do a new build.
So we'll hit save configuration.
And we are done.
That's all we need to do to set up our build automation.
Now, I want to actually force a build though.
To do that, I'm going to click the build button.
And then we'll choose the latest.
Oh, I don't need to choose a chain set.
We'll just hit the build button.
It'll use the latest.
That's if you want to specify a specific change set to build instead of doing the latest.
So, I'm going to have it kick off a build for the latest version of our game.
And that is going to take a while.
I'll hit build view details.
Just remember that when you do these builds um on the especially on the free version, it's going to take a while for the build to complete.
It's not something that happens instant.
It's not automatic.
It's not nearly as fast as if you run it locally, but it is very easy to share with other people.
Look down here.
We've got an auto share button.
We can hit view settings and we could even start to share this.
I'm going to talk about sharing our project later, though.
For now, we'll let it build and let it finish.
And then we'll take a look at the end results as soon as it's done.
Now that my build is finished, let's take a look at it.
The first thing I want to notice or point out is that this is actually build number four.
And that's because after I started the build, I committed a couple changes and then had more builds kick off and cancel my first build.
So, I hit replay and got a new build of the first version.
Now, I've got a couple options when I open this up, though.
There's a play button right here and a share button.
I can hit play and actually load up our game in a WebGL player.
I can choose the resolution.
I'm going to choose 1920x 1080.
Hit apply.
And then look at our character running around, jumping.
Look at this.
Everything is working just like it is in our editor.
We've got a full working version of it running in a web browser.
Oh, except for the part where we kill our player.
For some reason, that's not in here, but it's probably has something to do with our build settings.
For now though, I want to also show you the share button because if you want to share this with friends, you can just click that share button, get this link right here, and send it off to whoever you want, and then they can go play your game whenever you want.
So, you don't have to keep um sending them new builds and stuff.
You can just send them your link instead.
All right, with that said, I just want to say that this is a very cool system.
It makes it very easy to do builds um and to share them automatically.
It's not completely free though.
There's some free amount that comes with the Unity Cloud system, the Unity Plus and Pro memberships.
I don't remember what that amount is, and it changes relatively regularly.
So, you may or may not want to have builds on for every build.
You may want to go into your build settings, go to the configuration.
In fact, I would probably recommend doing this.
go to your build configuration and go to your auto build and just uncheck that until you're ready to actually start sending out and sharing those builds.
Once you have builds that you want to send out and share, then go back, reenable that, and have it start giving you those builds.
But until you're doing that, you can always just come in here and hit build and do a quick build on demand.
So whenever you're ready to share, you can hit that button, get your link, and then send that out.
So you don't have to do the whole process every single time and add, you know, it it's only a couple cents each time, I think.
And like I said, there's a free amount, but it does add up and there's no reason to add it up if you're not actually using it.
It's time for us to start building enemies.
And we're going to start with a simple one that bounces back and forth.
A basic frog that will jump back and forth over the spike or wherever we want.
And we'll make sure that it's customizable and reusable.
So, we can have the frog bounce across anywhere or maybe even change him out with a grasshopper or something else later on.
So, let's take our frog.
I'm going to go to my assets, art, and enemies folder.
Find the frog graphic.
And I'm just going to drag it right out here into the scene kind of next to my spikes.
I'm going to go click on it.
Just make sure that the pixels per unit matches 128 and 128.
And then I'll zoom in and go select my frog.
My frog's going to need a couple of different components.
I'm going to want a collider on it for hitting things and landing on the ground and stuff.
And I'm also going to want a rigid body for jumping.
And then probably some sort of a frog script for jumping and handling that kind of bouncing around part.
So, first let's add a collider.
We're going to just start with a box collider 2D.
Something relatively simple that we can fit over our character.
We're going to shrink this thing down because it's probably too large.
Let's go check our sprite render.
Let's see.
Where's our box collider? Adjust the size down.
We can see the the white lines right there.
I can I can actually see them with the sprite render on or off.
So, it didn't matter.
I didn't need to turn it off.
So, I'll leave it on.
And let's get a value of about 0.5 on the size of the box collider.
And a value of about 0.25, but negative.25 on the um the Y offset there.
I think that's pretty close.
I think I want this to be a little bit taller, though.
Let's go 5.5.
Or let's go to maybe like a 6 and a.3.
No, 2.
There we go.
22.
Sometimes it's a little bit of just messing around and not a lot of exact perfection.
So, I'm going to go with a 6 and a negative.22 for the offset and the size there.
Now, I've got my frog set up.
I want to add a rigid body to him so he can bounce around and fall.
We'll use the rigid body 2D.
Of course, it was already found there because I had BO on my search and rigid body has a BO in it.
So, it kind of kind of fit and matched.
All right, let's save and press play.
I should expect to see my frog just kind of sit there, not really do anything.
But, he's going to be a little bit far away, so I'm going to have to run over there and go visit my froggy.
Say, "Hey, little frog.
Where you at?" There we go.
Look at that.
My frog is there.
He's ready to start jumping.
So, let's stop playing and go create a frog script that will allow our frog to jump back and forth.
I'll go into my scripts folder.
I'm going to rightclick, choose create, and choose C script.
We're going to name this frog because that's what he is.
And then we're going to attach the frog script to the frog.
Now, when I created the script, it automatically opened up my code editor.
Sometimes that happens.
I'll just minimize it.
Go back over.
Select my frog.
I'm going to rename him to capital frog because I want it to be nice and clean.
Minimize our rigid body.
Drag the frog script over to the frog so it's on him.
Save my scene and then open up the frog script by double clicking on it.
There we go.
We're in our frog script.
So here we're going to need to write some code to do some jumping.
We want our frog to jump and then turn around and jump again and then jump and then turn around and jump again.
And to do that, we're going to need to access the rigid body component and probably the sprite renderer component.
So, let's save those off right at the beginning.
Let's start by deleting out our start and update methods.
So, let's at least delete out our start methods.
Let's leave the update method there.
If you already deleted the update method, just hit control-z.
Let's delete out the start method and we'll add an awake instead.
So, I'm going to say awake and then let it autocomplete.
Get rid of that private keyword.
You can stop it from autogenerating that private keyword.
I'm not going to dive into how to do that yet, though.
So, if you got your awake method here, we're going to need to save off our rigid body.
And remember, we do that by going underscore RB, which is short for rigid body.
Just a little bit easier to type.
It's one of the few that I actually abbreviate.
In fact, it's probably the only one I abbreviate.
Equals.
And if I hit tab, it's going to autocomplete, but it's going to get me the wrong one.
I want the rigid body 2D.
So, I need to add in that 2D.
Then I hit the home key, alt and enter and generate our rigid body field.
Now we need to get the sprite renderer as well.
So we'll say underscore sprite renderer.
And you might be wondering like why don't you abbreviate that? And it's because generally I'm not lazy but with rigid bodies for some reason.
I've stolen the habit of abbreviating them like everybody else does.
So we generate the code to get component for our sprite renderer.
I'll hit alt enter and generate the field for the sprite render.
Remember, we have to click on it first and get rid of these private keywords.
Double click.
Delete.
Delete.
And now, let's look at how we're going to jump.
And let's look through a couple different options.
There are a few different ways that we could do a timed jump.
I've got a frog and I want him to jump every 3 seconds or every 5 seconds or some number of seconds.
I could do that through the update method.
Remember, in our update, we keep track of when the player's jump has to end.
And we could do something similar to keep track of a timer for when the frog should jump again and put put that into our update method.
But there's another way to do something when we need to do something very simple like that on a specific timer.
And I think that this is a perfect time to introduce that.
So we're going to add in a new line here after our sprite renderer caching on 14.
And this is going to be an invoke repeating call.
We'll call in Nv repeating.
There are two versions of invoke.
We want the repeating one.
And here we need to give it the name of a method, the amount of time to wait for the first time that it calls it, and then how long to wait in between each time afterwards.
We're going to give it the name of a method called jump.
And we have to give this in quotation marks.
So put quotes Jump M with a capital J.
We're going to add a comma and put in our first parameter, which is the duration or the delay.
And I'm gonna use a variable here.
I could put in a hard-coded value like maybe three and three, but I want to make this variable.
So I'm going to put underscore jump delay and then we'll put another comma for our repeat rate.
We'll use that jump delay again.
We'll add a ending brace or ending parenthesis and a semicolon.
Then we'll generate the jump delay field.
So I'll hit alt enter and we'll hit generate variable and generate a field.
Don't generate a method.
We want to if you hit just alt enter and generated a method, you're going to get some bad invoke repeating method.
Just hit undo.
Make sure that you go generate variable and choose field.
We've got our field here for our jump delay.
We'll replace the private keyword with the serialized field attribute.
Get that closing square brace.
And I'm going to give it a default value of three.
So we've got a 3se secondond jump delay.
Now this is going to try to call the jump method every 3 seconds.
But we don't have a jump method.
So let's delete our update method and add a jump method instead.
I'll delete out line 19.
I'm just going to hit shift delete and delete that whole line.
And then replace the word update here with jump.
There we go.
I've already got the void, the parentheses, and the braces.
Why recreate them? So, now I've got my method here to do the jumping.
And the jumping just needs to tell my rigid body to go flying off in some direction.
And to do that, we add force.
And we call RC RB add force.
There we go.
I typed it wrong, but autocomplete found it for me.
And then open parenthesis.
And we need to give it a vector for our force.
So we need to tell it how much force to give in what direction.
So we're going to just call this force.
And then we need to figure out what that force variable is.
So our force is going to be some jump force that maybe we should expose to the inspector.
Why don't we do that? Let's instead of calling this force, let's call it underscore jump force and then hit alt enter and generate a field.
We'll make that a serialized field by copying that attribute, pasting it over the private keyword, and saving.
Let's go back over to Unity and see what this looks like.
Now, let's clean up our frog's visuals.
Right now, our frog just kind of bounces back and forth while staring to the left.
And we do have a jump animation.
So, let's use it.
And let's make our frog face the correct direction as well.
We're going to select the frog and we're going to open up the frog script to start.
And when we do a jump, the first thing I want to do is just change our jump direction.
So every time we jump, after we jump, we'll turn our jump around.
And to do that, we're going to add a new line after our add force.
And we're going to say underscore jump force star equals, which is going to multiply it by some number.
And we're going to multiply it by a new vector 2.
And the first value of our vector 2 is going to be a negative one.
So this is going to flip our x of our jump force.
So if we're going to the right, we're going to go to the left.
If we're going to the left, we're going to flip it to the right.
So it's going to go from negative to positive or positive to negative.
The second value we're going to pass in is a one because we don't want to change our y.
Our y should stay the same for every single jump.
If we wanted to change that, we could do that here, but we don't.
We're going to add a semicolon after our parenthesis and then save.
And this should make our character jump back and forth.
Let's go make sure that that's correct before we continue on.
So, we go back in.
We'll press play.
I'm going to take my game view and drag it down here so I can watch the frog without having to run over there because I'm feeling a little bit lazy.
I don't want to run my character over there.
So, we watch our frog and he jumps any second now.
And then I expect him to turn and jump back the other direction.
All right, looking good.
So, he's doing his little bounce.
That looks cool.
But I want him to now face the correct direction as well.
So let's go back to our frog and let's change his sprite renderers flip X value.
Remember we use that to swap the direction that our player was facing.
If we go find our player and look for flip, we should be able to see that we use our flip X value depending on if we're going to the right or the left.
So we're going to go back over to our frog and do the same.
When we jump, we'll say sprite renderer.flip flip x equals.
And here we're just going to do the opposite of what it currently is.
To do that, we use the not sign.
So shift and one, which is the exclamation or not.
It's kind of weird.
It means a whole lot of things, but it means the basically the inverse or the opposite of the value that we're going to give it.
And the value we're going to give it is sprite renderer.flip x.
So we're going to set the value to whatever the opposite of the current value is.
We'll save that off.
Let's go back into Unity and try it again.
We should be able to press play and watch our character kind of do a flip.
Let's see if that's the truth or if if I'm just making things up or if he bounces and looks right.
So, he flips and he looks right.
So, he jumps, notice, and he switches directions at the same time.
So, it actually works out kind of perfect.
The last thing I want to do though is show that sprite.
I want to show the jump sprite because why not use it? We have a cool jump sprite.
We should be showing it while we're in the air.
So, let's add a reference to a jump sprite right here in line 12.
I guess we'll add a serialized field and we'll call this will be a sprite and we'll call this underscore jump sprite.
This is something that we're going to assign.
And then when we're jumping, we'll put that sprite in here.
So, we'll go down to line 25 and we'll say sprite renderer.sprite equals_jump sprite.
So, when we start jumping, we'll put in that sprite.
Let's save that off.
Go back into Unity and assign our jump sprite to our frog.
Now, it should appear here as a field.
And we can hit the little search box, find all of our sprites.
I'm just going to search for Oh, not for a frog.
There we go.
Frog move.
That's the jumping one.
Ah, I clicked too many times.
There we go.
I've got my frog selected.
I should be able to save, press play, and watch my frog switch to a jumping sprite.
Let's see.
see.
see.
Come along, little froggy.
Jump, jump, jump.
There we go.
He jumps.
And okay, it's close.
Except when he lands, he doesn't switch back to the normal sprite.
So, the last thing we need to do is make him switch back to his normal sprite.
And I'm going to leave this as a little challenge for you.
Go ahead and see if you can figure out the code to make your frog switch back to the normal sprite when he lands on the ground.
Don't do anything too complicated.
You shouldn't need to do any ray casts or anything.
Keep it relatively simple.
And then once you're done, or if you get stuck, just unpause, continue on, and I'll show you the solution.
All right, I'll assume that you've gone through it or you got stuck.
No problem either way.
So, what we're going to do is go into our frog and just listen for our collision enter.
If we hit anything, we'll go to the idle mode.
Even if we smack something on our head, it'll be fine.
We'll just switch because we don't really have a sprite for that anyway.
So, we're going to add an on collision enter right in between.
Oh, actually, let's do it after our jump.
Right after our jump, we'll do an on collision enter 2D because we're doing 2D graphics, 2D physics.
We'll delete that private keyword.
And here we're going to set the sprite renderer sprite back to its default sprite.
So say sprite renderer.sprite equals_default sprite.
Now go wait, we don't have a default sprite.
Where did that come from? Oh, we just have to generate it.
So we'll hit alt enter, generate a field for it, and we'll now have a sprite up here.
I'm going to move that to be well, let's delete the private keyword and move it to be up here, right below my sprite renderer, but with a space since it's not a component.
it is a cached property of a component or a cached field of a component.
I want to have it a little bit of spacing there.
Just the way that I like to organize my things.
So now we need to set this default sprite.
And we can do that right here after line 19 on line 20.
Say underscore def Oh, look at that.
It already knew what I want.
Well, it kind of knew what I wanted to do.
We want to say underscore default sprite equals sprite renderer.sprite.
So this is going to get the sprite that we had before.
I'm adding an extra space there.
get the sprite that we start with as the default.
When we land on the ground, we'll switch back to that.
So, we'll save or really when we hit anything, we're going to switch back to it.
But that's good enough for now.
We don't necessarily need to worry.
If we hit a player, we want to kill the player.
If we hit something else, we don't have a really a sprite to deal with that.
And if we're hitting our head on something, we probably placed our frog wrong.
So, let's let the frog jump and see if he does his thing.
There we go.
He bounces to the right.
Looks good.
He bounces to the left.
So far, I'm loving it.
All right, we'll stop playing.
I'm going to save my scene, go to plastic, and say that we've added or up.
How do I want to put this? Frog Frog Frog flips graphics and um I think that's Oh, and sprite.
Yeah.
Ah, frog flips graphics.
That's probably enough.
I I'm not sure what to put for my check in.
So, I'll put that and hit the button.
Now, let's talk about killing players again.
Right now, we've killed our player with the spikes, and our frog should probably be something that kills the player as well, because what's the point of an enemy that isn't a threat? So, we need to add a way for our frog to kill the player.
And we've got a couple of options here.
Just like anything with code, we can go about this multiple different ways.
We could go into our frog and modify our on collision enter so that if we hit a player, we also kill ourselves or we al or kill the player, not ourselves, but kill our player.
The frog will kind of die too cuz the level reloads, but you get the idea.
We don't need to do that though.
There's actually something quite a bit simpler that we could do.
Since we already have a spike script that kills a player on collision enter, we can just go to our frog and drag the spikes on top of it.
Now, our frog has spikes and our frog will kill players when it touches them.
Don't believe me? Hit save, press play, run over, and go touch your frog and see what happens.
Let's go try it out.
I want to see it in action myself.
So, I run over here and I go find my frog.
And any second now.
Oh, look at that.
I touched him and I died.
Now, I didn't actually touch him.
You might have noticed that I got kind of close to him and and it happened.
And that's because his box collider is just too big.
So, I'm going to minimize that.
We'll stop playing.
We'll go select it and we're going to shrink down the width of his box collider.
We could also alternatively just swap him over to use a polygon collider 2D if we want, but I think that just shrinking the size of his box collider to maybe a point 75.
There we go.
And get it nice and tight so I don't have to worry about accidentally rubbing up against them.
But again, if I want, I can just uncheck that.
Go add component.
Add a polygon collider 2D.
And now I'll have an even tighter collider.
In fact, let's do that.
Let's remove the box collider.
Have the polygon collider.
Save.
Press play.
and go try it out.
This way when when a kid jumps on it and says, "Hey, I just didn't even touch that thing.
My head barely it went over the head and I still got the hit.
That sucks." Um, we won't have that problem.
Or at least we won't have that problem nearly as much as we would have with a box collider.
So, come over here.
Check it out.
Our frog comes.
He lands.
Oh, I hit a spike.
Let's try one more time without landing on the frog.
There we go.
The frog killed me.
I collider on my player is also a little big.
So if I stop playing and go find my player, I can shrink down his width of his collider, too.
See how it kind of goes out to the edge a little bit too far.
Let's go grab the size here and put this down to a 75 so that it's quite a bit tighter and I don't have to worry about those early hits where I can't see it and it doesn't look right.
So we'll save.
We'll go into plastic and we're going to make sure that everything is saved.
We've got our frog saved, our player saved.
So, we adjusted frog colliders and made frog kill the player on touch with spikes script.
And actually, we adjusted the player and frog colliders.
So, I should put that in my check-in message.
Before we turn our frog into a prefab, let's make him a little bit smarter.
Let's give him the ability to jump some set number of jumps instead of just once back and forth.
To do that, we're going to need to open up our frog script and make some minor changes.
And what I'd like to present to you first is a quick challenge.
See if you can come up with the solution of how to make your frog jump two jumps instead of one or maybe some variable number of jumps.
If you're up for the challenge, go ahead and give it a try right now.
If not, then go ahead and just unpause right after I say to pause and continue on and I will show you the process.
All right, let's go ahead and I'll show you the process.
Now, hopefully you either found the solution or you're just ready to go through it.
The first thing that we're going to need to do is set some number of jumps that our frog can make.
And I'm going to do that by going up above line 12 and adding another serialized field.
I'm going to make this an integer so that it's whole numbers and I'm going to call this underscore jumps.
I'll set it to two so that our frog will default to having two jumps.
We're also going to create a variable that we're going to use to keep track of the number of jumps remaining.
So, I'm going to do that after line 10.
I'll say int jumps remaining.
Now, in our jump code, we're going to do a little bit of checking.
We're going to see if we have any jumps remaining.
And if we don't, we're going to flip around.
If we do, then we won't flip around.
That's pretty much all there is to it.
So, we'll add some lines here.
Line 28.
Right after line 28, say if underscore jumps remaining is less than or equal to zero.
Somehow, if we get below zero, we're still going to want to run this code, but we should only ever get to zero.
So, if we're less than or equal to zero, then we want to run some code.
And the code that we want to run is the code that flips our jump force.
So, we're going to take jump force star equals new vector 2 and cut that line out.
So, select the whole line, hit X, and put it right here on line 31.
And then after that, we need to reset our jumps remaining.
So, I'll say jumps remaining equal Oops, if I get that right, remaining equals jumps.
So, when we run out of jumps, we'll flip directions and then reset our number of jumps remaining to however many jumps we allow.
I'm going to add another line here so we have some space.
Not add an else like it's recommending.
And then let's save.
Get rid of our star here and go back into Unity.
We should see our frog in here with a new field for a number of jumps.
There we go.
I've got two jumps available.
And if I press play, I expect to see it not be perfect.
Let's see it, though.
Let's hit play and watch our frog jump and see what we've got going on here.
So, our frog is there and he'll jump.
and he jumped, but he's looking the wrong direction and he's jumping kind of far and then he went into the water.
Okay, so got two little issues there.
One, he went way too far and now I've lost my poor froggy.
He's falling through the world.
And two, um, he's not looking the correct direction.
So, step one, we're going to just reduce the jump force.
So, I'm going to change this to about 150 on the X so that he doesn't jump as far in that direction.
But first, I want to or after that, I want to go into my code and make sure that he actually jumps to the right so that he actually starts jumping to the right because I have it at 150.
He doesn't instantly flip to the left.
If I open up my code again, you'll see that we don't ever set our jumps remaining to jumps when we start.
Initially, we just kind of have a zero and we get reset and flip over.
So, the first time we call jump, jumps remaining is at zero because it's never set and it gets flipped over to the opposite direction.
I don't want that.
I want it to go the direction that I had it facing or the direction that my velocity is set to by by default.
So in awake I'm going to say underscore jumps remaining is equal to underscore jumps.
So that way we get set to the value that we have by default and we stay going in our correct direction.
The other code that I want to fix is with our flip x.
Now our flip x value before was just swapping back and forth because it made sense.
it's a boolean and we're toggling back and forth based on the direction we're going.
That no longer makes sense.
Now, we want to set it to true if we're going to the right and false if we're going to the left.
And we can do that just by looking at our jump force.
So, we'll say flip x is equal to underscore jump force.x greater than zero.
So, if the x value of our jump force is greater than zero, we're going to the right, then flip x will be true.
Otherwise, it'll be false.
We'll save this off.
Let's go look at our sprite, though, because remember our frog by default is looking to the left.
So that's why that makes sense.
We have to flip it to look to the right if our character is going to the right.
If our character was going the opposite direction, the logic of that code would need to be inverted or swapped.
Let's save our scene, press play, and watch our froggy do some jumping.
He should go hop hop hop or hop hop and then hop hop.
Let's see if that's true.
So he jumps any second.
There we go.
hop and a hop and then he should flip around.
Oh, three hops.
Let's see if he's going to flip on this third.
So, he's never flipping around.
He's never actually turning around.
Let's go back to our frog and take a look at what's going on here.
So, why is he never turning around? Well, we never decremented his jumps remaining.
So, let's copy jumps remaining and let's say jumps remaining minus minus on line 35.
We'll minimize.
Go back into our Unity editor.
Press play one more time.
And now our frog should jump two times and not some unlimited number of times.
He should actually obey our frog jump count.
Let's see if that's true.
So we play.
Our frog should jump and then he'll jump again.
And then he's going to turn around and jump back.
Look at that.
We've got a frog now that goes back and forth any number of jumps that we specify.
Right now it's on two.
Let's say we want to go to three and have them jump back three instead.
I go one, two, two, two, and three.
And look at that.
We've got a nice cool bouncing back and forth frog.
Let's stop playing, save our scene, and turn our frog into a prefab.
So we'll go to the frog the prefabs folder.
We'll take our frog, drag him down into there.
We'll save our scene, save our project, and then go to plastic and say that we've added the jumping frog prefab with variable jump count and distance.
And we'll check in our changes.
Before we make any more enemies, let's add some sound effects to our frog.
Let's add a weird sound that we found on Open Game Art, or at least that I found on Open Game Art that I think will work pretty well.
There's this mutant frog sound.
I think that those work pretty good.
So, I've downloaded this zip and I'm going to open it up and then we'll copy the files into the project.
So, I'll grab my zip file.
Open it.
Oops.
Let's go.
Open it.
Select the two frog sound effects, the two OGs.
I'm not going to grab the wave that has both of them.
And then I'll close that window.
I've got them both copied onto my clipboard with C.
Go back into Unity.
Go to my audio folder.
Show in explorer.
I should see my audio folder right there.
I can double click it and paste with CtrlV.
Once those files start to appear, I'll close this window, jump back into Unity, and I should see my two frog sound effects.
I'll select my frog, take that frog one sound, drop it right on them, press play, and make sure that I hear a frog sound right when my game starts up.
There we go.
So, that's working.
Now, I want to make this sound effect play continuously.
or not maybe continuously but perhaps when the frog is about to jump or maybe just when the frog is landing.
Let's uncheck play on awake.
Go to our frog script and then in our frog script when we do our on collision enter let's tell our audio source to play.
So we could call get component audio source oops not audio behavior audio source and tell it to play just like that.
But since we're already caching things we should probably do that here as well.
So, I'm going to copy this get component part.
Put it right onto my cursor.
Hit controll X.
Go up to awake right up at the top.
Put underscore audio source equals.
And then I'll just paste and hit semicolon.
Click on audio source.
Hit alt enter and generate a field.
And I should get a field right up here at the top.
It's a private audio source named audio source.
I'll double click private and doubleclick delete to get rid of that keyword.
Now, down here at the bottom in on collision enter, I'll just say underscore audio source.play.
Now, if I go back into Unity, I should hear my frog bouncing around making sounds.
Oh, I think I rechecked play and awake.
I'm going to have to make sure that I uncheck that.
So, let's listen.
So, he jumps and we hear the sound and we hear the sound again.
But this is a little strange, right? He is kind of far away for me to be hearing that.
I probably should only hear him when he's on screen.
So, how can I do that? Well, there's actually a really easy way to do that and it'll add a really cool effect as well.
So, let's stop playing.
I'm going to minimize some of these scripts on my frog.
Uncheck the play on awake option and let's scroll down to 3D sound settings.
It may be collapsed for you.
If it is, just expand it out by clicking the little arrow or on the text.
And what we want to do here is use 3D positional sound.
Unity has a 3D sound system built in, and we really just care about whether the thing's off to the left or the right.
So, we can set this up to use just our 3D position based off the the left and the right.
What we need to do first is change this from logarithmic roll to linear roll.
We can use logarithmic if we want, but I like a linear roll off because it'll make it nice and easy for you to see what's going on, and I feel like it makes a little more sense when we're building a 2D game.
Of course, you can change this later.
Use whatever you like, but I want you to use this just to start.
I'm also going to change the max distance to be about 10.
Look at the circle here.
Now, you can see the range of our audio effect or of our audio distance.
If I just press play, though, it's not going to work.
It's going to give me the same sound effects.
Watch.
Let's just hit play and make sure that I'm not crazy that we do hear the same sounds.
Yep.
See, it still played the sounds.
When it lands again, it's going to play the sound again.
Yep.
So that's not what I want to happen.
What I want to happen is it for it to use the 3D sound effect.
So I need to take the spatial blender slider and drag it all the way over to one.
Now it will use 3D sound.
But there's one big big problem with this.
Now if I press play, let's watch what happens.
So I play go run over here.
I don't hear anything from the frog yet.
Okay, seems okay.
My player sounds are good.
Let's come over here.
I'm still I'm inside the frog range.
Why don't I hear anything? Well, the reason for that is because we're using 3D sound in a 2D game.
And this sound systems really built for 3D.
So, if we go into 3D mode in our scene view, go to the scene view, check the 3D 2D button, and go look at our frog.
We can see that our frog's audio circle is that big blue circle.
That's the whole thing.
If I collapse or here, let's uncheck it.
You'll see it's turning on and off.
That big circle is the audio part.
Where's our audio listening device? Where's the thing that we pick up audio from? You might think it's the player, but it's actually not.
By default, it's the camera.
It's this object way out here placed outside the world, kind of back far away.
So, let's go select that frog and the camera at the same time.
And you might see why it's not working, why we're not hearing anything.
The frog's circle isn't overlapping with the camera.
So, we need to do something about this.
We've got a lot of options.
We can move the camera.
Maybe we could move the audio source or maybe expand out the range of this frog.
We could maybe make this like 20.
So, if we set this up to like a 20, then it's going to be in range.
But when I go to 2D mode, I can't really tell what the range is anymore.
and it's like half the range that I see and I don't really like that.
So instead, we'll stop playing.
And what I want to do is go to my main camera and find the audio listener component.
There's only supposed to be one of these in your scene.
So I can't just add a new one.
Instead, I want to remove the one that's on my main camera.
Go down to my player and minimize this audio source.
Hit add component and add an audio listener.
Oh, look.
I've already got it typed out and selected.
So, just choose audio listener and add that onto the player.
Now, the listener is going to be at the same 2D space or the same Zdepth as our frog.
So, they'll both be lined up and I should hear it as soon as my player gets within 10 meters or within that circle.
Let's go try that.
Here's my player.
You can see him in both views.
Come over here.
I'm just about in range.
I can hear him bouncing.
There he went.
And you may or may not be able to hear it, but there's actually spatial audio.
I can hear the side he's on.
So, if you have stereo speakers set up with your left and right setup, you should be hearing him jumping from the left to the right.
If you don't have that, or maybe just go put some headphones on and hear it.
You'll hear the cool effect.
It's pretty neat and extremely easy to get working as you can tell.
So, let's stop playing, go into plastic SCM, save our level, make sure that that's in here.
So, we added 3D frog sound effects.
and check in.
It's time for us to add a second level to our game.
But before we can do that, we really need a way to get to our second level.
So, let's start there.
We're going to begin by going to our art and tiles folder.
And let's look for a flag or something that we can use to bounce up to the next level.
In fact, I think is it perhaps in items? Ah, there we go.
In items, we have some flag options.
I'm going to take flag blue one and just drag it right out here into our scene view.
I'm going to set the position to six and -3.5 so that it's perfectly grounded.
That looks good.
And then we're going to add a collider.
We'll add a polygon collider 2D.
Not a polygon 2D, Jason.
Remove that.
We'll add a polygon collider 2D.
And then we're going to add in a script that will allow us to load up a level.
Let's call this a loadle script.
To do that, we'll go into our assets folder.
We'll go to the scripts folder and we'll hit create and choose C script.
I'm going to call this script load level.
No spaces, but two capital L's, not three, just two.
Capital L for load and capital L for level.
L O A D L E Vel.
Hit enter.
That should generate my script.
And it does not open it up the first time.
Like I said, a lot of the time it just opens up whatever you had last.
So, I'll go back into Unity.
Once it finishes recompiling, I'll double click the load level script again.
There we go.
And in here, all I want to do is check to see if the player has entered this object or touched this object.
And if so, load up the next level or load up a specific level that I've maybe laid out by name.
So, I'm going to take all of the code from line 7 to 17, select it, and delete it because we don't need a start method, and we don't need an update method.
And instead, we're going to add an on collision enter 2D.
There, where is that at? On collision, enter 2D.
Now, when we get our collision, we want to check to make sure that it's a player that touched this.
So, we'll say if collision collider.
Now, do you remember the way to check a player? If so, go ahead and type that out right now.
If not, hold on just a second.
That's right.
We're going to do compare tag and we're going to put in parentheses and quotes player.
So, if we hit a player, then we want to call our load scene method.
And if you remember from the way that we kill players, that's in our scene manager.
We say scene manager with a capital S and a capital M dot load scene.
And here, we're not going to give it a zero or a number.
Instead, we're going to give it a name.
Let's say underscore level name.
I'll put a semicolon at the end.
Go over to level name.
Hit alt enter and generate a field for it.
Now, we need to do two things.
First, delete this extra private keyword cuz I don't want to have it there.
Not cuz we need to, but just cuz it's extra.
And then go to this private keyword up here and replace it with the serialize field attribute.
Now, I'm going to save.
Control shiftb to do a build.
And then we'll go into Unity.
The build is just to force it to save as well.
Control shiftB.
And then it pops up.
If I typo something, it gives me real quick feedback.
But we're back into Unity.
Let's go find our loadle script and attach it to this flag.
I'm going to minimize the sprite renderer, minimize the polygon collider, drag the load level script over here, and let's put in the level name level two.
I will save my scene.
press play, run over, and expect to get a nice big error in my console.
Let's see if that's the case.
So, we play, we run over, we touch this flag, and you can't see it.
It's just off screen.
But if I drag it up, there's the error.
And if I go into the console, you see that it says level two could not be loaded because it has not been added to the build settings or the asset bundle has not been loaded.
So, says we need to go add it to build settings.
So, I'm going to stop playing, go to file, go to build settings, and go, "Oh, I don't have a level two." So, I need to make a level two.
Next, I'll go into my scenes folder so I can see where I've got my level one, and think like, okay, I need a level two.
Let's uh how am I going to make a level two? Let's start by just doing this file, save as.
Go into my scenes folder.
Put in the word level space 2 because that's the way that I typed it in my loadle method or in my low-level uh component.
And then let's add the loadle 2 script.
So, or the load level 2 scene.
And now I can do that by hitting add open scenes because I now have that scene open.
Or I can drag it from here and drop it right onto my scenes to build.
Now I need to go to file and save project to make sure that my build settings gets saved and go into plastic SCM and I'll see that my editor build settings asset is updated.
I can close this window now.
Press play and when I run up to that flag, what's actually going to happen is it's going to just load me into level two when I'm already in level two.
Let's see.
So I run up and bam, it reloads level two and it reloads level two.
So let's change this up just a little bit in level two.
So, I've got level two open.
I'm going to select the flag.
I'm going to go to my project view and I'm going to expand out the sprite renderer.
I'm going to change this from flag blue to flag green one.
I'm going to drag that right up there.
And then I'm going to change the level name from level two to level one.
I'll save.
So now in level two, I have a green flag that takes me to level one.
In level one, I have a blue flag that takes me to level two.
Let's press play and see if I can go between the two levels now.
All right, we've got level two and we're in level one.
You can see it up there in the hierarchy and I can go between my two levels.
Right now, they're very similar.
They're exactly the same except for the flags.
But I've now got a very simple way to bounce back and forth and I can start adding some things to level two and thinking through my scene management setup.
Let's stop playing.
Make sure that everything is saved.
go into plastic SCM and say that we added level two and flags to get between levels and we'll check that in.
Now that we have a second level, let's begin by making it look quite a bit different.
First, we'll change out the background.
So, I'll select the background over here, the colored grass.
Let's rename this to background and then give it a new image.
We'll select click on the colored grass and I want to use the blue shroom for our background here instead.
I've swapped that out just by dragging it onto the sprite.
Now I'm going to zoom in and let's change out the ground here.
So we've got this grass center and this grass center here.
I'm going to just call these ground pieces.
So, I'm going to select both of them with control, rename them to ground by clicking up in the inspector, and then we're going to replace the grass center here with a snow center.
So, I'v