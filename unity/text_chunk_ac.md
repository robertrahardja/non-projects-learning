e got grass center available or selected right now.
I'm going to go to snow and find the snow center and drag that in instead.
Now, it does say that it doesn't like that my thing isn't set to full wctck mode.
So, now I'm going to go into my snow folder, select all of them in here, control A.
Remember, if you have one expanded out, this it might give you a problem.
It's going to look like that.
So, you want to make sure that they're all collapsed and then you click and hit control A.
Once you do that, you should be able to switch this over from tight to full wrecked and hit the apply button.
Now that now that error is gone and we'll go over to the two grass mid pieces that I've got.
So, I've got that one and that one.
I'm going to replace these with snow mid.
Click snow mid and drag it up and drop it on there.
It's already looking quite a bit different, isn't it? Now, we need to make a couple other changes.
Look at our water right here.
Our water looks very strange.
It's got grass now in the background in both of those spots.
So, I want to make a change to it.
Let's click on the water, expand out the water, and find the grass background.
I want to make this into a snow background instead.
So, I'm going to click the little eyropper, click the color that's right above it.
There we go.
And now it looks like a snow background.
I'll take my water, hit the select button in my inspector so that I find my prefab.
Then I'll take my water and drag it down into the prefab section into this folder of prefabs, not on top of anything, but into the empty area and hit prefab variant.
This is going to create a new version of my water that's just a variant of the existing one where I've changed this one thing and nothing else has really changed.
I want to rename this though.
I don't like the name water variant.
I'm going to call this snow water.
So, this is water with my snow background.
And that's my snow background color.
Now, I've got my snow water existing.
I want to go over, find the other water object here, or just click on it, rightclick, choose prefab, and use that replace option.
Go find my snow water.
And look at that.
The water is looking much, much better.
All right.
Next, I want to do the same for these prefabs or these platforms up here.
Let's do grass platform 4.
I want to make this into snow platform 4.
So, the first thing I'm going to do is expand it out.
Look at all of my little uh sprites here.
I've got a grass left, a grass right, and I need to replace both of these.
So, I'll go into the snow folder with right selected.
I'll take snow right.
And it doesn't necessarily matter what the name is here.
So, I'm just going to leave it there.
And then in the base prefab, I'm going to rename these later.
So, I'm going to leave that named grass.
Right.
I'll select grass left.
Take snow left and drag that on as the sprite.
And here you can see that the two sprites are starting to show up and it's looking pretty good.
And then we'll go to the main one here, the center or the root object, grass platform 4, and take snow mid.
Look at that.
We've got a nice platform.
Let's rename this to snow platform 4.
And then we'll go to our projects prefabs folder.
take our snow platform 4, drag it down, and make this a prefab variant as well.
So now we've got snow platform 4, and it has the word variant.
I'm going to double click it, delete that out, and the extra space.
So now we just have snow platform 4.
All right.
Next, I want to challenge you to go ahead and make snowplatform five or six on your own, and then we'll go through the process and make the rest of them really quick.
So, go ahead and see how many of them you can do and then continue on and I'll run you through them all real quick.
All right, I'll assume that you're done with all of them or if you ran into any problems, let's just go through them again.
So, here's my grass platform 5.
I'm going to rename it F2.
Call this snow platform 5.
I'll replace the grass mid here with a snow mid.
And then I'm going to do the same for my right and the left.
Snow mid.
And oh, didn't click the right one.
So I'll click on that left again and grab the left.
Now I'll take my snow platform 5, drop that into my prefabs, and make that a prefab variant.
I'll remove the word variant, and do the same for number six.
So, I'll go find number six.
F2.
Rename it.
Snow platform 6.
We'll go find our sprites again.
So, I've got my snow mid.
I can also use the search box.
Why don't I do that on the next one? I'll use this one.
I'll search for snow, right? And I'll drag that over so you can see it.
So, we've got snow right.
In fact, I could even alternatively, let's do it.
Let's go for a cliff here.
So, on platform six, we're going to go with a rounded cliff edge.
And then on the left side of it, we'll go with uh let's see what else we've got here.
Snow.
Um let's go with we got an alternative cliff edge.
Let's go with that.
So our six wide one is going to look totally different than the others.
Let's go into the prefabs, drag that in, and make that another prefab variant.
So this is snow platform six.
And then the final one that I need to make is snow platform number two.
So this one doesn't have a center.
It just has the left and the right.
So I'm just going to search and I think I'll just take the normal left and the normal right.
So I'm going to click on that one.
Go select the the left side.
Drag snow left over there.
Oh, and then on this one I got the wrong one.
on the that side.
I need to have snow.
Right.
There we go.
We'll rename this to snow platform 2 and then drag that into the prefabs.
And I should have all of the prefabs that I want for my different snow platforms.
Now, let's see.
Prefab variant.
We'll remove the word variant and the extra space.
And then this platform right here is a grass platform 4.
But we can just remember rightclick and choose prefab and replace.
And we'll just choose our snow platform for.
I can't tell which one's for though.
So I'll go to list view by holding control and double click snow platform 4.
Look at that.
We now have a nice beautiful snow level to go along with our grass level.
Let's save our scene.
Go into plastic and take a look at all the files that we've changed.
So we've got all of our snow art files.
That's because we changed the modes to full wrecked.
We've got our level two and then we've got all of our new prefabs.
Just to be sure though, make sure you go to file and hit save project.
Double check that all of your prefabs are in there.
Now, let's add a comment and say that we added snow prefabs and redesigned level two to use snow graphics.
And we'll check our changes.
Now that we have an icy snow level, let's make it actually feel icy and snowy so that our character is kind of slipping around and not getting that same feeling that they're getting on the grass.
To do that, we're going to need to go modify our player script and make it a little bit aware of what it's on and maybe control the way that our character is moving a little bit more tightly.
So, we're going to open up our player script and we're going to find our movement code, which is inside of our update method.
We do our update grounding and then we read our horizontal input into this horizontal value.
I want to rename this value.
Now I think that horizontal is something that we're going to need to keep track of, but I want to use the horizontal value um not necessarily as the input or from the input, but I want to keep track of it the actual value that we're using.
So instead of having this underscore horizontal equals input.get get access horizontal.
I'm going to double click on horizontal here and I'm going to say var horizontal input.
I'm going to make a temporary variable and we're just going to keep horizontal around as its own variable.
Remember if I hit F12 on it, it's a float that exists inside of our class.
So it just kind of sits here and we can use it every frame or however we want.
But we're no longer assigning it to the input.
Now that's assigned to this horizontal input variable instead.
And now what I want to do is move our horizontal value from our current horizontal value towards the value that I actually want to be at.
So we're going to figure out a desired velocity and then use a math formula or a math calculation to go from that our current velocity to that desired one.
We're going to add in a line here on 69 and say var desired horizontal.
Did I spell it right? Yep.
Equals.
And we're going to use our horizontal input times our horizontal velocity, which is our horizontal max speed.
Actually, in fact, we're going to rename this now.
So, with horizontal velocity selected, I'm going to hit controlR or F2.
That's also a rename button.
And we're I'm going to call this max speed or let's call it max horizontal horizontal speed.
There we go.
So now we've got a max horizontal speed and our horizontal input and we've got a desired horizontal this is our desired velocity along that x and x axis.
So our desired horizontal is there and our current is right now getting multiplied by max horizontal.
That's not what we want at all.
Instead, what we want to do is assign our current horizontal value to be equal to.
So say equals and we're going to use math f.lurp.
This is a linear interpolation which is going to go from one value to another over some amount of time.
So we're going to give it our starting value which is the current horizontal value and then we'll give it a comma and the desired horizontal value as the ending value or the target value.
And then finally we'll give it an amount of time.
And for that we're going to use our time dot delta time.
And then we're going to give it some sort of acceleration value.
So, we're going to do times acceleration.
I'm going to go to the end and add a semicolon.
And then we'll generate a field for our acceleration.
So, I'll hit alt enter with acceleration selected.
Allow it to generate a field.
Hit F12, replace private with serialized field, add that square brace, and then I'm going to move this line.
And so select line 23, cut it with Ctrl X.
Go up here to line 11, hit enter, and paste.
And let's give our acceleration a default of 1.
So we've got an acceleration of one.
And now inside of our movement code, let's go find that again.
Where are you? Movement code.
We no longer do the old calculation of just multiplying our horizontal velocity and then setting our rigid body velocity to it.
Instead, we go we set our horizontal velocity to our current value lurped to some new value.
Now, let's talk a little bit about what this math f.lurp ma method is actually doing.
So, at when you call this method, you pass in a beginning value and an ending value.
Let's say we passed in a zero for horizontal and a 100 for desired horizontal.
Totally made up numbers.
Let's just imagine them for a moment.
The last value that we pass in is a percentage from 0% to 100% or how far along between those two values we want.
So if I had a zero for the horizontal and a 100 for the desired horizontal and I pass in a 0.5 or a 50% I'm going to get back a value of 50 because that's in between 0 and 100.
Now, if I had a value of say negative - 100 and positive 100 here, maybe I was going all the way to the left super fast 100 meters and and my desired is 100 meters to the right and I put in a value of 0.5.
Well, the value in between there right in the middle would be zero.
If I put in a value of one, the value that I would get back would be a positive 50.
And if I put in a value of negative one here, I would get a negative 50.
So a negative 1 or a zero sorry a zero will get you the first value.
A one here will get you the second value and a value in between 0 and one will get you some number in between the first and second value.
So this is going to slowly accelerate or decelerate us multiplied by some acceleration value.
So we have total control over it.
Let's go back into our game.
Press play and watch our acceleration on this icy level and see how it feels.
There we go.
You can see my character kind of doing that little slip there.
And if I adjust this acceleration down to like a 0.5, you'll see that they slip quite a bit more.
They'll go for quite a while.
And it takes a little while to speed up and get going the direction that you want to go.
That's the feeling that I want here.
Now, if I crank this up to like a 20, then you'll see that I've got nice snappy movement just like I had before.
I can control it exactly how I want.
Now, I want to do two little changes here.
First, I want to stop playing and I want to crank up my maximum horizontal speed.
I had it at three.
I think a five might seem a little bit better.
So, let's save.
Actually, let's go to our player script and let's change the default value of that to five as well.
So, we'll set it max horizontal speed to five.
Go back into Unity.
Play.
And I want to jump around.
Make sure that it feels good.
And then, let's figure out a number that we're going to want for when we're not on the ice.
Because right now, notice that we're slipping around no matter what surface.
We didn't do anything to check the surface.
We just made it so that our character slips around.
So, let's set it to we've got a max horizontal speed of five and right now an acceleration of one.
Let's see what that feels like.
Yeah, that's kind of kind of good and slippery.
I feel like this could go down to maybe even a 0.5 though on the ice.
Let's see.
Uh, no.
Let's go to a one.
So, one on the ice seems good.
I felt it.
It felt a little too slippery.
And then maybe let's try a 10.
Yeah, something like that.
Like a 10 or maybe even higher on non ice surfaces, I think, would be good.
I don't have a way to do that right now, though.
So, we're going to stop playing.
We're going to leave it at one.
Or let's crank it up to 10.
Actually, we'll save and then we're going to go into plastic.
And actually, let's go to our player script.
Before we do this, we'll go to our player script.
We'll change the default acceleration to be 10 as well.
And then we'll go back into plastic and we'll commit and say that we've added acceleration controls to our player.
And we're done this so that we can control it with the iciness effect or so we can add an iciness effect.
So, let's say added acceleration controls to the player and we'll check in our changes.
Let's separate out the slipperiness now so that our player only slips around on ice and not on grass.
And we're going to do that by using tags.
We're going to create our own new custom tag just like we've been using the player tag.
We'll compare against it and do some custom code based on that.
So, we're going to start by selecting our grass mid object, which is actually a snow.
Let's call this snow ground.
I think that's a better name for it.
And then let's go down and we want to change the tag right here in the tag section by going to the add tag option.
In the add tag option, we're going to get our tag and layer inspector.
Remember, we've added layers, we've added sorting layers here, and now it's time for us to add a tag.
We're going to hit the plus button and I'm going to call this snow with a capital S.
So now I've got a snow tag.
I'm going to select my snow ground and I'm going to tag this as snow.
Now let's go into our player and make our player use the snow.
Right now we have an acceleration value and I want to add a snow acceleration as well.
So I'm going to open up my player script, find my acceleration part, and then duplicate it with control or command D.
I'll add the word snow before acceleration and capitalize that A.
That way I'll get my camel case and watch what happens when I go back into the inspector.
Well, the words are going to be nicely separated.
One of the very important reasons to use proper casing.
If we don't use proper casing, our max horizontal speed would maybe not look like three words or our jump velocity and so on.
So, there we go.
We've got a snow acceleration and an acceleration.
Let's change this to be a one though instead of a 10.
I'm going to go into the code though and just change the default value in here so that I don't have to go change it in multiple levels.
We'll save off our code.
So now we've got our acceleration and our snow acceleration here.
And we're going to go down into our grounding code because when we check to see if we're on the ground and or if we are grounded or is grounded is true, we want to also check to see if we're on the snow.
So we're going to do that inside of our update grounding method.
And right now we've got some good opportunity to do what's called refactoring and separate this out.
But we're still not going to do it just yet.
We're going to add in our snow stuff.
We'll talk about that a little bit later.
So if our collider is hit, so if when we do our center check and we do our raycast downward, if we hit something and we get back a collider, this is going to be true.
And we want to do more than just set is grounded to true.
We're going to add in a brace and add a closing brace after the is grounded is true.
We'll add in one more line and we're going to add a line for on snow.
So say on snow with capital O and a capital S is equal to.
And here we're going to check that colliders tag and see if the colliders tag is the snow tag.
So we'll say hit collider compare tag just like we did with the player.
And we'll add in a parenthesis and a quotation.
Then put the word snow.
Go to the end and add a semicolon.
Now I'm going to click on on snow and we're going to generate ourselves a field.
I'll hit enter and then we're going to hit F12 to go to that field and we're going to make it public instead of private.
This is so I can see it in the inspector and that's pretty much the only reason.
We might want to view this later.
We might want to see it somewhere else.
For now though, we're just going to set it publicly and make it visible to us.
I'm going to add in another line here in between the public parameters or the public fields and the private fields here.
So, we've got a little space between our on snow and animator.
And then we're going to go back down into our code.
So when we do our grounding check, right now we're only setting on snow when we do a hit in the center um the center ray cast.
So right in the center of our body.
I want to do this for any hit that we get.
So I'm going to take lines 87 through 91 and copy them.
87 right here through 91.
Select and control C.
Then I'm going to replace my other two spots where I checked the collider.
So lines 96 and 97 where I check if hit collider then is grounded is true.
I'll just paste.
So that way I get my extra lines.
Now I could have just done the extra parts here and pasted but I took a little bit more.
So we're going to go with that.
Now I've got to do the same for 105 and 106 for my right side check.
So I'll select these two lines and again paste.
It's still on my clipboard.
And the final thing I need to do is at the top set on snow to be false.
So I'll say on snow equals false.
And you know what? I kind of want to rename this.
Instead of being on snow, I want to rename this to is on snow.
So I'm going to hit controlR and put in the word is.
And there are a couple reasons for that.
The biggest one is conventions and just cleanliness.
Is grounded is on snow.
It makes more sense.
Otherwise, it should be grounded and on snow.
If I'm going to have is for one, I should have it for both.
So now we've got our check our state here that'll tell us whether we're on the snow or not.
Let's go try that out and then we'll use it next.
So, I'm going to go into Unity.
We should have our snow platform right there.
And on our player, we should have an is on snow check box showing up right here.
Once I hit play, I expect that to get set to true when I fall onto the snow and then false as soon as I leave the snow.
Maybe I get unggrounded or I go up to another platform that's not tagged as snow yet.
So, let's check that out.
So is on snow is true.
When I jump, it's not true.
And if I jump up to this other platform that's not marked as snow, it's not true as well.
But if I change this platform, if I go select snow platform 4, change the tag to be snow, and then look at my character again, now I'm on snow.
So it is working.
It's getting that variable correctly.
Now I just need to use that for our movement.
So let's stop playing and make our final change.
We'll go back into the player and find the update method where we're moving our player around.
So right here where we set our horizontal, we use an acceleration value.
And we have two accelerations now.
We have a regular acceleration and a snow acceleration.
So let's decide which one to use one line before and then pass that in.
So on line 75, we'll add a new line here.
We'll say var acceleration equals and if we're on snow, so we'll say is on snow and we're going to use the conditional statement question mark.
We'll use the snow acceleration.
Otherwise, we'll use the default or the normal acceleration.
Now, we've got this new variable on line 75.
We'll copy it and paste it right here onto 76.
Essentially getting rid of that underscore.
Now, I don't like that these variables are named almost the same thing.
I think it's a little bit confusing.
So, we're going to rename acceleration to ground or normal acceleration.
Let's call it ground acceleration.
We'll hit control-R.
Add in the word ground right before and capitalize that a.
So, now our acceleration will either be the snow acceleration or the ground acceleration depending on whether or not we're on snow.
And we'll use that value down here in our lurp.
Let's save and watch the magic in action.
So, this bottom one should be slippery and the top one should not be because still haven't tagged it as snow yet.
Let's see if that's the case.
Start playing any second.
If I didn't hit the button twice, I do have my snow and ground acceleration values set the same on my player.
So, soon as it starts playing, I'm going to need to set that snow acceleration down to one.
There we go.
And then run around.
It's pretty slippery.
looking slippery there so far.
And if I jump and I'm in the air, it's not slippery at all.
And on this platform that's not marked as snow, it's not slippery at all either.
Got a tiny little bit of acceleration, but not not the slipperiness that I'm feeling here.
And if I put this down to a 0.5, I can see it's even slipperier.
And if I want to make it tighter on the ground, I can just crank this ground acceleration up to something like a 20 and then have super tight controls.
Now, you might be thinking, well, what about air acceleration? Definitely something we can do.
Let's stop playing, though, and go select all of our snow platforms and mark them as snow because we want them all to be marked right so that our character slips around on them.
So, we'll go find all of our prefabs, our snow platform 2 through six, and we're going to go change the tag from untagged to snow.
Now, let's go open up snow platform 4.
Go select the child objects here.
Grass right and grass left.
And look at that.
Those are not tagged.
When we set the tag, it doesn't set all of the children.
So, we need to go into each of these, select both of the children, and change the tag to be snow as well.
So, that's snow platform 4.
I'm going to open up snowplatform 5 by double clicking on it and hit save to allow that to save and modify my changes.
I'll go select these two, tag them as snow, and then I'll go open up snow platform 6.
I'm going to do the same.
Go select both of these sides and tag them as snow.
And we'll do the same for my snow platform, too, as well.
So, it's got a right and a left.
And I just want to tag both of these as snow objects or having the snow tag.
We'll hit back and save.
Now, everything in my scene should be slippery.
I can run around, slip on all of these objects, and have it work.
And then, if I go into level one, it should be a nice tight feeling.
Let's Oh, first one last thing I need to do.
I lied to you.
We're going to go back into the code and we're going to change the default values for the player.
Right now, we have the two acceleration values and they're both Oh, no.
They're not both set the same.
Okay, good.
We've got snow acceleration at one, ground at 10.
Let's go try it out.
So, I run over here.
Slippery.
Oh, no.
See, this is the problem.
My player version is set to not be on the default.
So, I'm going to stop playing, go back over here, and reset that snow acceleration back down to one.
And the reason for that is just that my default had been changed off.
So, it was no longer on the default.
I had accidentally saved with the value of 10 in there.
So, let's play again.
Got a snow acceleration of one, a ground of 10.
Should slip on level two, and be able to, you know, tightly control myself on level one.
There we go.
It's a little bit slippery.
and I hit the the flag and we've got nice tight controls.
Go back over here and it's slippery again.
All right, let's stop playing.
Save our scene.
Make sure that everything's in plastic that we added slipperyness to ice using the snow tag.
And we'll check that in.
Now, we're going to add a menu to our game.
I find that it's easiest to put a menu in relatively early so that way we can choose which level we want to be in and start to think about our players data persistence across levels because we'll already have that starting area.
So, we're going to begin by creating a new scene.
We choose file and new scene and I'm going to go with the lit 2D URP option.
We choose create and then I'm going to save this by hitting Ctrl S into our scenes folder and name it menu with a capital M.
Now that I've got my menu, I want to do a couple things.
I want to put a background in there and then put a couple buttons in there.
First, let's pull in the background.
You should be able to download that on the page below.
And then once you've got it downloaded, get it onto your clipboard.
Just right click on it and hit copy.
Let's go into the art and backgrounds folders.
I'm going to rightclick, hit show and explorer to pop up that window.
And then I'll paste it right inside this backgrounds folder.
Hit Ctrl +V.
And I should see my background appear here.
any second now.
There it is.
And then it'll jump back over to Unity and my new background is in.
So when I drop this background in, I don't want to just drag it and pop it out there because I want to do this as a UI element.
And if I do that, drop it drop it out there, it instead uses a sprite renderer and a sprite element and doesn't work with canvases and the UI stuff that I want to use.
So I'm going to delete this sprite renderer.
We're going to go to game object UI and then choose image.
Now that I've got an image here, I'm going to assign it.
So, I'll expand out this image section, the image component.
I'm going to collapse the recct transform for just a moment.
And then I'll assign the background to to this sprite of the image.
If it doesn't allow me to assign it, I can always go over to the texture, make sure that it's click on that background there, and make sure it's set to sprite 2D and UI and not default.
If it's set to default, it won't allow you to drop it in there.
Now, I'm going to go select that image again, and we want this to be bigger.
I want this to fill my entire background.
So, I'm going to go to the rec transform and we'll click right here at this anchor part where we've got the part that says middle and center.
And it's going to give us this anchor presets option.
I want to do this thing up here where it says hold shift to also set the pivot and hold alt to set the position.
So, I'm going to hold alt and shift.
And then look at what happens.
It it's telling me what it's going to do.
As I hold alt, it's telling me, hey, this is going to set the position up to the top left.
So, I can hold alt and click that and it'll move it up.
But I also want the pivot to be up at the top left.
I don't want this position to be based off the center.
I want the position to be based off the top left of this icon.
So I'm going to hold shift and mark that pivot as well.
So now I've got a 0 0 position and it's set to a width of 100 100.
That's not what I want though.
I don't want it up in the corner.
I want to fill my whole screen.
So I could do maybe this stretch one right here to stretch it.
But that just goes across the top.
You might have guessed which one is going to stretch across the full screen.
It's this bottom right one.
Hit that and it's going to stretch and take up the entire screen.
Now that we've kind of got an idea of how to stretch and set up some images, let's add a button.
We're going to add a button that's going to go up in the top left.
That's going to be a level one button.
So, I'm going to right click on the canvas, go to UI, and we're going to choose button text mesh pro.
When I click this, it's going to give me the tmp importer, and I'm going to need to click on both of these buttons.
First, the import tmp essentials, which is importing the text mesh pro or the very nice version of text for Unity into into our game.
Not every game needs it, so it's not included by default, but most games need text, so it's something that you're probably going to want to pull in nine out of 10 times.
Now that I've got the essentials in, I'm going to import the examples and extras.
Let's go to the text mesh pro folder first, though, and take a look.
If you look here, I've got documentation, fonts, resources, shaders, and sprites.
There's a little bit of stuff here.
There's not a whole lot though.
There's a couple There's one font.
If I go into the fonts and materials, and then there are a couple settings for the font.
But if I hit the import examples and extras, this is going to pull in a whole bunch of extra fonts.
Well, like five or six different fonts, and some really cool examples that show how to do some interesting different types of things with text that you can only do with Text Mesh Pro.
So, I've got those both imported, and I'm going to go over to my button.
My button right now is placed right in the center.
You can kind of see it there.
It's this boring little kind of default looking like the '9s button.
I want to make it bigger and dock it to the top left.
So, the first thing I'm going to do is adjust the width.
I'm going to make it 600 wide and make it 100 tall.
Then I'm going to change the color.
I'm going to just click the color dropper right here, the eyropper on the sprite if you or on the image.
If you don't see this, make sure you expand out the image.
So, hit the eyropper and I'm going to go with a color that looks like Oh, here.
Let's see.
Let's go.
Let's just type in the color here.
I'm going to go with a color that looks like about this.
So, put in a 7B D253 or right around here on your kind of green.
Something that looks kind of greenish.
It doesn't have to be the exact same color, but some sort of a green.
Now, I want to change the pivot of it or the lo and the location.
So, I'm going to click on the anchor tool.
Remember, hold alt and shift just like this.
Alt and shift and hit the top left.
Now, I don't want this anchored all the way to the top left.
I do want to move it over a little bit.
Have it maybe 50 pixels over and 50 pixels down.
So, grab this X position and just drag it till it looks about right.
See if the Yeah, 50 seems like a good number.
So, then I'll just type in a 50 to make it nice and round.
And do the same with the Y.
I'll just grab it and drag it down till it's looking good.
So, maybe.
Yeah, I think negative 50 seems good, too.
So, I'll just go with 50 and a 50.
Last thing I want to do to this button is make it well, not the last thing, but the next thing I want to do to this button is make the text not just say button.
Make it say level one and make it look nice and pretty.
I said that we brought in that text mesh pro thing.
We didn't actually use it yet.
It just kind of appeared and made an ugly text under here.
So, let's expand out our button.
Click the little arrow here.
And underneath it, you'll see that we've got the text tmp, which again is just short for text mesh pro.
It's because there used to be two text systems.
There was an old text that didn't look as pretty and then there's the new text mesh pro that's been around since like 2016 or 18 or something like that and it is now the default.
You should always use this, not the old one.
So, we've got our text tmp object here and it has the word button here in its text.
If I expand out the text mesh pro, if you don't see this area here, just make sure that you expand it.
You might just see the the shader down below.
So, if I expand this out, I see the word button.
I want to replace that with level one.
And then I want to replace the font.
I'm going to choose font the font asset here.
I'm if I click on it, I can see that it goes and selects it.
That's not the folder that the one that I want is in though.
So, I'm just going to hit the little search box, the little button there.
And then we'll go find the bangers font.
This looks a lot different.
But if I hit the auto size, you'll see, let's see.
Whoops.
Let's see.
Auto size.
Okay, I hit auto size, but for some reason, my auto size options are wrong.
And my max value is set to zero.
So, I'm going to set this to a 200.
That's actually never happened before where I've seen that where it popped up and had an invalid max auto size.
Didn't happen last time I did this.
So, if you do see that, just make sure that you put it up to it.
But it should say 72 by default.
So, if you see a 72 here, just change this up to something like a 200.
And we'll get a nice big font size of it looks like about a 94.
I can turn off auto size also and just kind of hardcode it at what I want.
But I like auto size because it fills it into the right spot or the right size for what I want.
Now, I'm going to change the color of this text by clicking the vertex color and just make it white.
And finally, I want to add an outline.
There are a couple ways to do this.
I can go down into the shader options here and find the uh where's outline right here? Outline option and just drag up this thickness.
But that's going to change all of the text in this bangers font to do that.
Instead, what I can do and what I want to do is use the material preset.
So, underneath the font asset, there are a couple different presets for this font.
There's a drop shadow, an outline, a glow, and a logo.
If I choose the outline one, I think that that looks pretty good.
And I've got a decent looking level one button.
So, I'm going to rename my button to be level one button.
And then I'm going to duplicate it and make a level two button.
So, I hit control D or command D.
Then I'll rename this second button from level one button one to level two button.
And I'm going to move the Y position down.
So, just drag it down.
Let's see what looks good.
Oh, about a negative 200 probably is looking about right.
And then we'll change the text here to say level two.
All right, we'll save our scene.
And before we add in any functionality, I just want to save this off and get it committed.
So go into plastic and we've added text mesh pro and we've also added a bunch of fonts.
So I'm going to make sure that everything is checked.
So say added text mesh pro and extras plus menu scene with level buttons and we'll check those changes in.
Now that we have our two buttons in our main menu scene, let's hook them up so that they actually do something.
First, let's take a look at the actual buttons.
If I click on the level one button, you'll see that I have the image where I changed the color and I can adjust that to be whatever I want.
And I can even change out the sprite, the background here to be some other sprite, make it have a different effect.
If you go download a cool UI pack, you can get a really nice looking button with borders and everything else.
Or you could change it out to be just about any icon.
I think that just using the default one looks pretty decent, though, so I'm going to stick with that for now.
Let's expand out the button component, though, because the button component is the part that does a lot of the work or is going to do the work for us.
Inside of the button, there are a couple options.
First, there's an option for whether or not this button is interactable.
If you uncheck it, you'll see that it kind of grays out and it makes it makes it essentially become unusable.
So, the button can't be interacted with or used.
I'm going to recheck that because I want both my buttons available.
You also see that you have some options for how to transition.
There's a color tint option, which does the tinting that you'll see in a second when I put it in play mode.
There's a sprite swap option which allows you to set a different sprite for when you're clicking on the button, when you're kind of hovering over it, that's the highlighted or when it's disabled.
Or there's even an animation one that'll allow you to do animations of the sprites.
The default though is color tint that has these nice little tints that kind of give you an idea of what's going on.
Let's hit play real quick and see those in action and then we'll talk about the onclick part, which is where we actually get to hook up code.
So here you can see that as I put the mouse over the color just changes a little bit.
As I hold the button down, the color changes pretty drastically.
And if I change them to be not interactable, obviously changes quite a bit.
And then it no longer is clickable or does a hover or anything.
So to use this on click part and actually have something happen when we f or when we click on one of these buttons, we're going to need to write some code.
You don't necessarily need to write code.
It is possible to do something without writing code.
I'll show you that first.
But for what we actually need to do, we're going to need to write code.
Let's start by doing something that doesn't require code though.
In this on click for the level one button, I'm going to hit the plus and we're going to take the background here, this uh image, and it's just named image right now.
I'm going to drag it into the target.
That's this part that says none object.
Then I'm going to choose the no function part and choose game object.
Meaning I'm going to run something on the game object of this image.
And we're going to choose set active which takes in a boolean parameter which is this checkbox.
True would be checked and false is not checked.
So when I click this button, it's now going to take this image and move its active property to be false or change it active property to be false.
Now I'm going to do the opposite on the level two button.
So I'm going to select the level two button, hit the plus.
We'll go take the image here.
We'll go to game object, choose set active, and I'm going to check the box.
Now, if I press play, you should be able to guess what's going to happen.
I want you to think about it for a second before you press play and before you see it.
Think about what's going to happen, but it should be pretty obvious.
We click the level one button and the background disappears.
We click level two and it reappears.
So, this is how we can hook up the buttons to do things, but now we want to hook it up to run our own code.
We don't want to turn the background on and off.
We want to just load a level.
So, we have a loadle script, and we can open that up and use that as kind of a starting point.
Our load level script is the one that's on a flag right now and it takes a level name and whenever we collide with the object, we load that level.
We want to do something similar, but we want to do it from a button.
So, we're going to create a new script.
And this time, we're going to create a new script inside of a script.
I'm going to show you the way that I create most scripts when I'm writing lots of code.
We're going to go down to the bottom of our loadle script.
Hit enter right after the braces.
You have to be outside of these braces.
and we're going to put in the word public class load level button.
Then we'll put a colon and mono behavior.
I'm going to hit enter to let that autocomplete.
Hit enter and then add in some open braces.
This is going to give me a new class inside the same file that's a loadle button.
This is our load level that's on a flag.
In fact, we'll rename it to loadle level flag in a little bit.
Don't do it yet though.
And then this will be our load level button.
So in our load level button, we're going to want to use a level name and have something that we can assign a level to for now at least.
So we'll copy line 8, Ctrl + C, go down to line 19, and paste it with Ctrl +V.
Now, I don't want to do an on collision enter in our load level button.
Instead, I want to be able to call this from some other script or essentially from our button.
Let's go take a look at that.
I want to be able to call it from our onclick listeners.
And to do that, we need to make it be something that's public on that script and then have that script be the or on the attached or the assigned object there.
Let's go back into that loadle script.
What we're going to do is make a public method public void and we're going to call this load.
Um, I think that's it.
Just load.
We'll add in open closing parenthesis and then some braces here.
And oh, I accidentally added an extra line on 22.
I'll delete that.
Inside of our load method, we're going to call scene manager.load scene level name.
So, I'm just going to copy line 13 and paste it right here on line 23.
Now, we need to do something.
So, if I save this off and I just go try to add this load level button, it's not going to let me.
Let's go take a look at that.
So, if I go over to my level one button, give it a second to finish compiling.
Probably going to give me a warning down there.
And then I minimize these components and go to add component.
Search for load level.
You notice that the loadle button option isn't there.
The reason for that is that for a component to be added to a game object, the script that it's in has to be in a file that's the main that is named the same as that script.
So load level works because it's in a file named loadle.cs.
Loadle button doesn't work because it's not in a loadle button.cs.
So, what we're going to do is with the class selected, the cursor on the class, you can just hit alt enter and then choose the move type to loadle button.cs.
There's always a move to file option in code editors and it'll just move it over, create a new file.
Let's see if we can find it.
There we go.
And then open that file up.
So, we've got our load level button, and as long as that's saved, I should be able to jump back over to Unity, see it be added right here, and then go assign it to my two buttons.
Let's see.
Once it finishes loading, I'll go select level one button.
We'll add the load level button script here.
And I'm going to put in the word level one with a space.
We'll go to level two button and drag in that script and put in the word level two.
Now, if I just press play, still not going to work because I haven't hooked up the buttons on clicks to my load level button.
So, here we are on level two button.
Let's expand out the button script and instead of on click changing the active property of the image, let's take the load level button and make that be the target.
Then we'll change the function here to be load level button load right there on the bottom.
Then we'll do the same for the level one button.
We'll just take in the script here.
Then we'll choose load level button and load.
Save our menu scene.
Press play and watch the magic of our level loading as soon as we click our buttons.
Let's go see if that works.
So, we press level one and it loads up.
Goes into level one.
Let's stop playing.
Play again.
Press level two and make sure that it goes into level two.
There we go.
It's going into level one.
It's going into level two.
I can still go back and forth between them.
And if I die right now, it's actually going to take me back to the grass level.
Let's see that.
So, I die and it goes back to the grass.
The last thing we need to do is make it go back to the main menu.
So, we'll hit file and go to build settings.
And we need to add our main menu to our build settings and make it be scene zero.
So, hit add open scenes.
Drag the menu up to the top.
And then when we do our load scene and pass in a zero, it's going to be that menu scene.
So, go to file, save project, press play.
Let's run over.
Die real quick.
Make sure that our game goes back to the main menu.
And then we can pick the level that we want to be in.
So I'm going to go over here, press level two.
Hey, I want to test level two.
Let's see how level two is working out.
And see if I hit a spike or something else.
Oh no, I died.
Okay, let's go try out level one.
All right, looks like it's working.
So I'm going to stop playing.
Make sure that we've saved everything.
Just go to file and save project.
And then we'll go into plastic SCM.
So go to plastic and we'll commit our menu with level load buttons.
So, menu works with level or load level buttons and checkin.
Now, I want to pause from the technical stuff for just a moment and show you something really cool that comes in really handy when you're building out games, especially if you don't have a full art team, and that's the AI image generation.
The background that we used in the menu scene was generated by MidJourney.
You can generate your own backgrounds that you can use as concepts or as background pieces.
and I found it to be extremely helpful.
We're going to use it for some game over scenes.
I also used it for some concept art that I had converted into actual characters that we'll be using later.
So, if you haven't tried it out yet, I recommend that you go log into MidJourney.
It's totally free.
Go to midjourney.com and you'll first want to hit join the beta, go through the process of logging in with your Discord server or sorry, with your Discord account and then you'll be able to generate images.
Once you generate images, it's free for up to 200 a month.
You can start putting them in.
You can see I've generated tons and tons of different stuff.
Everything from concepts to for different characters to logos to thumbnails and of course all of these very cool backgrounds.
I think that these things make really great just background shots.
Um nice menu scenes and transitions.
And it's very very easy to do and again totally free or cheap.
I I'm on the I was on the $10 a month plan and I think I've recently upgraded to the 30 because I just love it so much.
Let me show you really quickly how you would generate a background though.
Once you're logged into MidJourney and you're on the Discord server, what you need to do is open up the channel, open up your general one or any of these general channels and then you'll go down into the message part and start typing slash imagagine and then give it a prompt.
So, here I'm going to say a let's say concept art for a sci-fi platformer video game in space with robots and blasters.
And then we'll do a double slash or double dash AR3 col 2 to get a wider aspect ratio.
This will give me a 3x2 aspect ratio.
And it's going to generate an image.
And you're going to see a bunch of other people's images flying up and generating as it's waiting to generate mine.
You can see it still says it's waiting to start and other people's things are popping up that they've generated.
Everything from a what is this? A bird to an armadillo skydive black pen draw.
I don't know, all kinds of different stuff.
You'll see tons and tons of different things.
But you can see that my concept art is starting to appear and it's just loosely showing up.
It's going to get more and more detail.
It's at 62%.
When it gets to 100%, we should have some pretty nice detailed versions of it.
Let's see.
93.
We're almost there.
I'm already liking like this top right one.
So, once it's done, it's going to send me a new message and it'll be down here.
And then I've got a couple options.
I can see the image just by clicking on it and see these are my four different variations.
So, like, okay, I think I want to use this one.
And I kind of like this one.
Or maybe I like this for this first one because there's I I I kind of like the second one.
It's pretty cool.
It's this weird giant robot in the background.
So if I want to make a bigger version of that, I can hit YouTube and it'll upscale that one and give me a nice big wide 1080p version of it.
Or I can upscale number one.
Or if I maybe want variations of number one.
Maybe I like number one, but I want to see a couple different versions of it.
I can hit that V1 and then hit submit.
and or if you don't have it in the by default, you don't even have to hit submit.
Just hit V1 and it'll pop up.
Or I can hit this button and just generate a whole bunch of new ones.
This will actually generate me four new ones.
So, I have to scroll down to find the messages, but eventually I'll see my messages pop up here with the upscaled versions of the graphics and then the uh the new ones and the new variations.
And I start to pull these in.
Again, I think this is great for concept art, for coming up with ideas, for things to send over to artists to create.
I think I found it to be very helpful for sending over to artists on Fiverr because then I can say, "Hey, I want something that looks like this, but a character, and they don't have to come up with it and do the back and forth.
I can give them the one that's closest to what I'm thinking without having to try to translate that into words and then back into art.
I can actually give them something that I'm able to put together relatively quickly.
Here you can see I've got some more variations.
Oh, they just popped by.
That's the one thing that you'll run into is that they're constantly scrolling past.
There's so many messages in here.
Oh, yeah.
So, we've got lots of variations here.
Um, once I'm done with one though, and I really like it, I can download it either through Discord or I can go back over to the midjourney page and scroll up to the top and just hit F5 and refresh.
And after oh, two to three minutes, the graphics will start to appear on here.
and then I can download them.
So I can just click on them and then choose the save button and then download them to to my system and then import them into the game.
So I found this again to be extremely helpful.
I hope that you know it's useful for other people.
I know some concept artists really hate it, but it's nearly impossible to do the same kind of thing actually talking one-on-one back and forth trying to translate stuff if you're a solo developer and you don't actually have a team.
So, if you're a solo, small, you don't have a concept artist already, this is an amazing way to get lots of cool backgrounds or even just lots of placeholder and temporary stuff.
So, go try it out.
Pull stuff in.
Again, we'll be pulling more in, but I'll make those available for you to download just like this one, the last one was.
So, hopefully that's helpful.
Go check it out.
If you find something, come up with and make something really cool.
Um, put it in your game and let everybody know.
It's time for us to start looking at multiplayer development.
There's a lot that goes into games and if we want to build something that's multiplayer, it's important that we do it early on and that we don't try to slap it in later.
It's a whole lot harder to convert a single player game to multiplayer than it is to build multiplayer from the start.
So, we're going to start really early by adding multiplayer support.
We're going to change out our player and have our player use the new input system, which gives us some really great multiplayer capabilities out of the box.
So, we're going to start by importing the new import new input system and talking a little bit about it.
So, we're going to go to window and go to package manager and then we need to be in the Unity registry packages section and then scroll down until we find the input system.
You should be able to find it there or just search for it and then choose install.
Right now, it's on 1.4.4.
Expect there'll be lots more releases after this.
We'll hit the install button.
This should bring in the package and update our project really quickly.
And it's going to give me a popup asking me if I want to restart the Unity editor to add support for the new input system.
And I'm going to choose yes because that's a required thing to make this actually work.
We can't use the new input system until we allow Unity to restart.
So give it a second.
There it goes.
Popped up.
Do you want to restart to allow the backends? We'll choose yes and give it just a second.
Once it restarts, we'll have that new input system up and ready to go.
There it goes.
Oh, looks like it gave me a nice little crash and then it's going to reload.
This happens a lot when I bring in packages and allow Unity to restart or revert something and allow Unity to restart.
That time I had to manually reopen Unity and reopen my project, but it's okay.
Now it's up and running again.
I expect that to happen when I pull in certain packages or especially when I do reverting in source control.
It sometimes happens, doesn't happen every time, and shouldn't happen every time you pull in a package, but occasionally you're going to run into problems like that.
Just restart Unity.
All right, so I've got the new input system in, and nobody who isn't super familiar with it probably knows what that means.
That's okay.
And what it means is that we're going to have a brand new super powerful input system that allows us to do things that the current or existing input system doesn't allow us to do or at least doesn't make it easy for us to do.
The current input system is what we call a static class.
That's why we write input with a capital I.
Let's go take a quick look at it.
We write input with a capital I.get access.
That's because this is a static class with a static method on it.
That means that there's only ever one input and it has all of these methods on it that have string names for them that we can get.
So, if I want to have a player two, I'd need to have like a player two horizontal, I would need to go create that.
I would need to write the code to find a player two horizontal and I'd have to figure out how to map that all together in order to do that for every single player and every single button.
It's not there by default.
If I go into edit in my project settings and I go find the let's see go find project settings and input manager and I go look at these you'll see that there's horizontal, vertical and fire one two three but this is all just one player.
There's not stuff for another player.
The second horizontal and vertical here is just other inputs.
This is joystick versions versus keyboard versions.
We need something that's a lot more robust.
And the new input system is exactly that.
That's what it's there for.
So what we're going to do is collapse the sprite render.
I've got my player selected here in level one and we're going to add a new component.
Hit add component and we're going to search for player and look at that.
There's a player input and a player input manager script.
Now we're going to use the player input script.
That's the component that's provided to us by the input system.
And then expand it out in here.
You'll see that it has an actions field that's not assigned.
It says none a none there.
There's a button to create actions.
We'll click that in just a moment.
There's an option for the UI input module, for the camera, we'll talk about that in a moment, and for the behaviors.
First thing we need to do is choose create actions.
This is going to create what we call an action map.
We're going to give it a folder that we want to put it in.
I'll just I'm going to leave it in the default assets folder for now.
And then allow it to pop up.
So, it's going to give us this input actions dialogue window.
And this window allows us to create and do mappings.
Kind of like that ugly window you saw a minute ago with the horizontal, vertical, and fire 123 did.
But this one allows us to create multiple different action maps with multiple different actions and have them work differently across different devices.
If I expand out and move, you'll see that it works with the left stick on a gamepad WD, the primary 2D access controller on an XR controller, or the stick on a joystick.
look is going to be like your right thumb stick y and your pointer movement pointer delta.
So mouse look and the hat switch on the joystick and then fire is bound to right trigger left mouse primary touch or tap on a touchcreen trigger on a joystick or whatever the XR controllers.
You can see we've got quite a few different bindings here for different devices and it's much more um I guess clean and generic.
But the cool part that about this is that we're not going to need to have multiple action maps for multiple players.
We don't need to make a player two map or a move to action or anything like that.
We're going to be able to have a single player input with this action map hook up to multiple different players with different inputs work across keyboard and controller all kind of automatically and get split screen controls and everything as well.
So what we need to do next is well if we press play realize that nothing's going to happen.
Let's let's hit play and let's see what what it does.
We press play and we go in.
We've got our player input script and I can still move around just fine.
And that's because by default the input systems will now work together.
If you enable the new input system, the old input system can still give you back input.
You can still read the values and get the data out.
That can be disabled though.
It's an option in the player settings, but they've changed it looks like to be both of them on by default.
So, I want to now start using the actual player input here, though, instead of reading from the old input system.
So, we're going to open up our player script, and we're going to make a couple of changes.
The first thing that we need to do is get a reference to our player input in our awake method because we're going to be using it every frame.
So, right after we get our rigid body, we'll add a new line underscore player input equals get component, and we'll do of type.
So the less than player input with a capital P and a capital I and then close that out with a greater than open close parenthesis and our semicolon.
This is going to get our player input component from the same object our player's on and cach it in this player input field that doesn't exist yet.
So we'll click on it, hit alt enter and generate the field.
Should give us a field right up here by our other fields.
I'm going to delete that private keyword and add a space after it so that it's separated from our non-component fields.
So now we've got our player input.
Let's copy that onto the clipboard.
Double click it and click control C or command C.
And then let's go find the spots where we read input.
So we've got input.getaxis horizontal.
This is getting that X value of our hor or our horizontal.
So our X value of our movement.
Now if we want to read that from our new input system, we need to get it from the move action instead of the get axis.
So we're going to replace input.getax.
I'm going to just select it all and hit delete.
And then we'll paste in our player input.
And we want to first dotactions.
And then we'll do a square brace because the actions are actually an array that are indexed by name.
So we give it um well I don't know if it's actually an array.
It might be stored as a dictionary or something else underneath.
But it's some sort of a mapping that is indexed by array.
So we do actions and we put a square brace or by index and then we give it a quotation marks and the name of the action which is move.
Let's go take a look at that again.
So minimize our code.
We'll go back into that action map.
I'm going to go find our actions.
Just double click it and see that the name was move right here.
M OV with a capital M.
Now if we go back to our code, we need to go to the end of the part where we get our action.
So right now we've got our player input and we're going to reference the move action.
And so the next thing after the dot is going to be working on that move action.
So we'll hit dot and then we've got all of the properties and methods of the action or of that specifically of that move action.
And what we want to do is read a vector 2 value.
And that's because a move input is a vector 2 input.
It has an up and down or a left and right and an up and down or a horizontal and a vertical or an x and a y.
So we're going to say read value and we have to give it the type.
we have to tell it very specifically that we want a vector 2.
If we give it the wrong type, we will get an error.
So we have to make sure that this matches.
Then we'll add our open close parenthesis.
And the final thing that we need is that we don't actually care about the x and y input right here.
We just care about the horizontal or the x value.
So if we just do this right now, we leave it like this, we're going to have an error down here because desired horizontal is a vector 2, not a float.
So, we don't want this to be the vector 2 with the x and the y.
We just want to get the x and assign that to the horizontal input.
So, we'll just do ax.
Now, we could save this vector off if we want to use the y later, but right now we're not going to cuz we're not using it and it would just be extra code that would be extra confusion.
So, now we've got our move value read from the vector.
Let's go down and check the other two spots where we read our input.
I said from the vector I'm from the new input system from the player input.
So we've got our where's our inputs? So here's what I'll do.
Ah, there we go.
Just have it pop up right in front of me.
So for our fire one button or our beginning of our jump, we're going to replace the input.get button down.
Fire one all the way to there.
Do underscore player input.
And here again, we need to get the action for our fire.
So we'll do actions quote fire.
It's not fire one because we don't have a fire one.
We just have a fire action.
Let's go take one quick peek at that.
You look here, it's fire.
And we're going to add a jump action shortly after this, but we'll add a fire action.
We'll say dot performed.
Let's see this frame.
So there we go.
Was performed this frame.
There's already exists on there.
And this will tell us whether or not the fire action was performed on this frame.
So whether or not they started pressing fire during this frame.
Now, on line 74, we check to see if they're still holding the fire button down.
To determine that, we have actually a couple options.
There's an event system that allow us to know when they started and stopped pressing it.
But for now, we're just going to read the actual raw value of the fire button to see if the value is greater than zero, if the button is still being held down.
And we're going to talk about that in a moment.
Let's copy the code from player input all the way up to the end of the square brace for fire.
Ctrl + C.
And then I'm going to replace it over input.get button fire one.
So controlV.
It should look just like this.
Input player input.Actions and then square brace quotes fire with capital F and close in quotes and a square brace.
And then we'll say read value.
And we're going to read a float just like we read a vector 2 there.
We're going to read a float from our button.
And when you look at the button mapping, remember that the trigger is one of the buttons.
So buttons are actually going to return back a value between zero and one depending on how pushed down they are.
It's going to assume that every button has the capability to be dynamic or variable.
But all the buttons will work as a single button.
Even if they're just on or off, it'll just go from zero to one instantly.
So we've got our read value and we need to open close parenthesis to actually call that read value method telling it that we want to type a float.
And it still has an error here because we can't check to see if a float is true or false.
We have to make sure that this value is actually greater than something else.
So we'll check to see if the value from fire one is greater than zero and our jump time is still greater than end time.
So we can still continue jumping.
So this is just replacing our input reading to use that player input.
Let's save, get rid of the star there, and then jump over to Unity and see if it works and if our mappings are all working.
And then it's if it is, it should feel just about the same like there's not really much difference yet.
Let's see if that's the case.
In fact, there probably shouldn't really feel like any difference.
I can run left and right.
I can jump up and down.
Um, but interestingly, I can't Oh, there we go.
Now I can move on the controller once I get the controller on.
So, now I can bounce around and move on the controller or move on the uh keyboard and everything's working using the new input system.
Let's stop playing, go to plastic, and say that we've upgraded our game to use the new input system.
First, let's save our scene.
say um well, let's say switched game to use new input system and checking our changes.
Now, let's play our game.
Here I am.
I'm running around clicking and jumping and I go on to level two and a look at this.
My character can't move.
Why not? Well, let's go take a look.
Go expand out my level.
Go look at my player and oh yeah, it doesn't have that player input script.
Let's stop playing and go look at the scene.
So, if I go look at scene level two, my player does not have the new script on it because we added it in level one.
If I go back to level one, it's got that new player input script.
So, we need to get this input script onto the other player in level two.
What are our options here? Of course, we could open up level two, go copy that, and do all of the work for it.
But, I'm sure you know where we're going with this.
We've done enough prefab creation that it should have been something that's already kind of mulling around in your mind.
So, you're thinking like, "Hey, why haven't we made this into a prefab yet?" Well, now is the time.
Let's go to the prefabs folder.
I'm in level one.
I've got our player with the player input.
We'll take the player and drag them out into the prefabs folder.
We'll go into the scenes folder.
Go to level two.
Save our scene.
Make sure that level one gets saved.
Right click on our player, choose prefab, and replace.
And then we should easily be able to find our player prefab.
There he is.
And then save our scene.
Now, if I play, we should see that our character is consistent across both scenes.
Let's see if that's the case.
So, we run around and he's moving.
Yep.
Seems like he's working.
And then this one is working as well.
That's closer to what I what I should expect.
I want to have our player be reusable across multiple scenes.
and then mult well really across multiple players because we're going to be spawning a whole bunch of these in just a moment.
So let's stop playing and then go into plastic SCM.
We've created a pretty significant and important change.
It's important to just get this committed.
So say we created or let's say turned the player into a prefab and checking our changes.
Let's take a deeper look at the input action asset.
Now I've got my player selected and the player input and I'm just going to double click on the action map.
You could also go to the assets root folder and just double click on it here.
It's actually the input actions asset that has the action maps in it.
So inside of here we've got our player action map and it has our move look and fire actions and we've hooked up to move.
We've hooked up to fire.
But I really want to have a jump action as well.
I think this is a great opportunity to create a new one.
So we're going to go to the action section and choose the plus button.
It's going to allow us to create a new action.
We'll name it jump with a capital J.
And then underneath the action, we need to add some bindings.
So, by default, it's going to have this blank no binding.
And what we can do is click down here, click on it, and go to this path section and start searching.
The default key I want for jump, the thing I think of by default is space.
So, I'm going to search for the word space and then find my space on the keyboard.
I also want the X or the cross button on my PlayStation controller to be a jump button.
So, I'm going to hit plus and choose add binding.
And then I'm going to go down here and search for PlayStation and find the cross.
Now, if you have a different controller, you have an Xbox controller or something else, find a button that makes sense and bind it as your second button.
Now, once I'm done with that, I'm going to choose save.
Save the asset.
That's going to update this alien blaster input actions file.
I'll close this window and then we'll go back to our player, open up that player script, and in the spots where we looked for fire, let's look for jump instead because that's what our action should be.
So, I'll put jump there and jump right here on 65 and 74.
Minimize.
And then we'll go back into Unity.
And now I expect that instead of the right trigger being my jump and left click, it's going to be space and the X button on my controller.
So, let's hit play and see if that's the case.
I totally expect it to be, though.
So, we run around.
Oh, it's nice and slippery.
I can jump with the space key, and I should be able to, yep, jump with the X.
And the right trigger no longer does the jumping because that's doing firing for when we add in something for our player to actually fire.
So, let's stop playing and say that we've added a jump action in Plastic SCM.
added jump action and bound player to it.
And we'll check in our changes.
It's time to enable multiplayer.
To do that, we just need to add in the player input manager component and make a couple changes to our player prefab.
Let's start by creating an empty game object.
I'm going to do this in level two because it's the one that I have open.
So, I'll hit create empty.
We'll call this player input manager.
And then we'll hit the add component button.
and find the player input manager script.
I'm going to right click on the transform to just reset it so the position's all zeroed out.
It doesn't really matter, but it's a habit of mine.
And then I'm going to look at the options down here.
We have a couple things that we can choose from.
First, there's a notification behavior.
We're going to talk more about this in a little while when we start diving into the code and hooking into the code.
And same with that on the uh player or the player input script.
But we also have a joining section.
And there's a join behavior which has join players when button is pressed, when an action is triggered or manually.
When button is pressed means that as soon as I press a button on a controller that's valid, it will try to add a player for that device or that controller.
And that's what I want to happen.
I hit any button and then my new player will come in.
For the player prefab, I need to go assign the player.
So, I'm going to hit the little search box, go find my player prefab, and just assign it.
Now, there's an option here for joining enabled by default.
I want that on.
Just allows my players to hop in automatically.
And then an option to limit the number of players.
For now, I'm just going to limit it to two.
We could have any number that we want, but I'm just going to set a limit to two because um well, that's how many controllers I have set up right now.
I'm going to save my scene, press play, and let's watch our character jump into the game.
So, we should start with one character that's already there spawned.
I should be able to run around, use my space bar, and jump up and down.
And then press the X button, and have another character appear.
And this character is now bound to completely separate controls.
Notice that the camera's following him, though, and it's no longer following the other character.
It's because I've added a new one.
It's going to follow the most recent character that's been added into the game.
That's We haven't set up anything to deal with tracking multiple players yet, so it's just going to follow whatever is most recently added.
Let's stop playing though and try out one other option.
There's this enable split screen option that allow us to get a split screen view of both of our players.
If I just check that box and press play again, we should get our game starting up and I should be able to hit the X button or any button on here.
Let's see.
And get another view.
But I don't get the actual split screen.
And the reason for this, if we look down here at the errors, is it says player has no camera associated with it.
Let's click the error box so we get it in the console here.
It says the player has no camera associated with it.
Cannot set up split screen point player input camera to a camera for the player.
So what it's telling us is if we go to this player, the camera here is not assigned.
So we need to stop playing.
And what needs to happen here for our split screen setup to work is that the camera needs to be a child or associated with the player.
So, we need to have some way to associate the camera with our player.
And the easiest way to do that is to just take our main camera, drag it down to be a child of the player.
Then go to our player, hit overrides, and choose apply all.
Now, our camera will be a child of that player object, and we can assign it right here.
So, on the player input, we can take the camera and drag it in and assign it.
Then, choose overrides and hit apply.
In the last section, I worked on level two.
Let's go back to level one and make a couple of updates.
We need to make sure that our level one works and we should probably turn that player input manager into a prefab as well.
We're going to be making changes to that along the way and it should be its own prefab.
So, here I am in level one.
Let's start by just pressing play and see how things work and if there are any issues.
So, I hit play, hop on in, and start running around.
And first, I'm already noticing that my player's not being tracked.
If I jump and see that my player is not being followed by the camera.
If I hit another controller and jump in though, let's see what happens.
Oh, I get an error.
And if I look down here, it says that the player prefab must be set in order to um oh, in order to spawn new players.
So, somehow my player prefab even got cleared out here in my player input manager.
So, let's go turn this into a prefab.
Let's go into the prefabs folder.
I'm going to take the player input manager.
I'm going to drop it down into prefabs and then I'm going to go assign the player prefab in the player prefab manager or player input manager.
So, I've got the player input manager selected down here.
You can see it up here in the inspector.
And I'll just take the player and drag it onto the player prefab spot.
Now that I've got my player input manager updated, I should be able to see that the player is assigned in this one.
And if I load up level two, let's go right click on it and hit load scene.
I should be able to see that my player input manager here is not using that prefab.
And I can tell that it's not using that prefab because it's not blue.
I'm gonna right click on it, choose prefab, and hit replace, and then go find the player input manager.
There it is.
I'll double click on it, and now it's blue, and I'm going to save and get both of my scenes saved off so that I don't have that star there.
I'm going to remove level two again by right-clicking and hitting unload so that it's there.
I can access it and use it, but it's not loaded.
If I go to hit play right now, if I hit play, I'm just in level one.
I like to have both of my levels loaded sometimes and just go back and forth between them.
This is a nice little trick.
So, here we go.
I can run around and I'm still not tracked, but can I join with a new player? Yep, I can.
And this new player is tracked.
So, why is this player not being followed? Well, let's take a look at him.
Here's the player.
Or let's actually stop playing and play again so that we only have one player and see why he's not tracked.
I think it'll be a little bit more confusing if we have the second player in there.
So, here we go.
I run around and you can see that if I expand out the player, we have the camera here, but if you look down here, we still have that main camera in the route that we had from before.
This is the camera from that we drag into the player on level two, but it wasn't any part of a prefab setup.
So, in level one, we had a copy of that camera.
So, what we need to do is just delete that camera.
Then, my player will be followed and tracked around.
I did that in play mode, though.
So, I got to stop playing.
go find that main camera, delete, and then save.
Now I should be able to run around and see my player and join with another character.
Let's see if that's the case.
So, I run around.
Looks good.
I can jump and I can join in.
And everything seems to work.
Let's go over to the next level.
I go to this level and I can run around with my first character, player one.
And I can join as player two on the second controller just by hitting a button.
And everything seems to work.
So, let's go back over to level one.
Same thing.
Everything's looking good.
So, we'll stop playing.
Go to plastic and say it created a player input manager prefab.
Let's see if I can get a space in there and updated level one.
And we'll check that in.
Now that we have our multiplayer setup started, it's time to start adding some data to our players.
It's one of the most important things that you'll see in a game, keeping track of things like health, money, coins, or powerups or items.
So, we're going to build a system that allows us to keep track of all of that stuff across multiple players and then persist that, save off games, and do all of the cool things that you want to do in a regular game.
So, we're going to start by creating a coin.
I think that's one of the easiest things to comprehend and and start with and then we can build our systems on top of that and add in support for all different types of things that we want to store for our player.
So, we're going to begin by going into the items folder of our art folder.
So, we've got a subfolder items and we have three different coins here.
I'm going to choose the gold coin.
You can pick whatever color you want.
I'm going to drag mine right out here and take a peek at it.
You see that we've got a sprite renderer.
Let's see with the position.
It's at nine and 2.5.
Let's Let's change this to a solid nine exactly and a negative -2.
It's up there a little bit in the sky.
Now, I'm going to add a collider to it.
We'll start with a circle collider 2D.
And if I zoom in, you'll see that the collider is a little bit bigger than the actual coin.
It's got a radius of.5 m.
And I can drag that in to a value that looks right.
It looks like maybe about a three is good.
Oh, maybe like a 0.25.
There we go.
nice tight circle right around the sprite render.
You can just barely see it just barely matches.
All right.
Now, I want to check the is trigger box because I want this coin to not stop my play.
I don't want to have my player jump up, hit his head, and then fall down.
I want him to go right through the coin and pick the coin up.
So, I'll add the is trigger box.
And then we need to create a coin script, something to deal with the trigger enter.
So, we're going to go to the scripts folder.
I'm going to rightclick, choose create, choose C# script, and call it coin with a capital C.
I'll go select that coin.
Oh, it just opened up my code editor.
I'm going to minimize, though.
We'll go back into Unity.
I'm going to go select the coin and I want to attach the coin script to it.
So, I'm just going to drag the coin script over here.
And then I'm going to rename this to coin.
Actually, let's call it gold coin.
Maybe I'll add some other coins and use the other coins later.
We'll be a little bit more specific.
So, I've got my gold coin with the gold coin or the coin script on it.
Let's open up that coin script and then start by just deleting out our start and update methods.
In this coin script, all we want to do is deal with triggers and having our player kind of jump through us kind of like we did with spikes.
We deal on collision enter or in water we do the where's it at? On trigger enter, and we play an audio clip in the coin.
We want to disable the coin, maybe play some audio, and tell the player to get a point.
So, what we're going to do is delete out the start and update.
And we're going to add an ont trigger enter 2D.
Just start typing and find on trigger enter 2D.
Let it autocomplete by hitting enter.
And then I'm going to delete that private keyword just to get rid of it and keep things consistent.
And first check to make sure that the thing that went through us or the thing that entered our trigger was a player.
And we'll do that by trying to get the player component from the collision.
We could check the tag, but we're going to need the player component if we actually have one.
So, we may as well just try getting the component and skip the tag check.
So, we'll say if collision dot or actually I lied there.
We're not going to say that.
We're going to say var player equals collision.get component player.
And then we do our open close parenthesis.
Here's where the if statement comes in.
if player.
So, it's just is going to check to see if the player exists.
Then, we'll add our open braces on the next line.
And we want to do two things.
We want to tell the player to take a coin or to add a point.
And we'll have it do the audio playing inside of there.
The other thing we want to do is turn this game object off.
So, let's start by typing player add point.
I'll just call it add point for now.
We could call it add coin.
I think we'll start with point.
And we'll hit alt enter and generate a method for it.
That's going to create a method inside of the player class and that error should go away.
I can hit F12 to go to it.
I should see this little method here.
Then I'm gonna hit control and minus to go back.
I also have that bound to the third key on my mouse.
So I do that all the time.
I hit that button to go back.
You can go into your um options and your hotkeys and I believe it's under tools and options.
It's going to be in a different spot for every editor, but of that third button there bound to back so I can just constantly bounce back.
So we've got our add point method.
The other thing I said I wanted to do was turn this coin off.
So to do that, we call game object set active.
And look that it already knows what I want to do.
So I'll just hit tab tab and let it autocomplete.
Knows that I want to set this object to not active.
All right, let's save.
And then let's go into the add point method.
I'll hold control and click on add point.
Take me right in there.
F12 does that again as well.
So we need to not throw an exception, which is to log out an error and stop running stuff.
Instead, we want to just increase our number of coins.
So, we're going to create a variable named coins with an underscore and then increment it by one.
So, say underscore coins plus+ and a semicolon.
I'll hit home, alt enter, and generate a field.
And the other thing I want to do is replace this internal keyword with public.
Now, it doesn't necessarily matter, but I just like the consistency of keeping things public versus internal.
Now, the real technical difference technically internal was probably a better setting here or better value here, but I find that it confuses people a lot because that's another layer of protection.
And I I don't know if I really want to dive into the difference between public and internal, but the the core difference, I guess the high level difference for anybody who's curious is that a public method can be used by things outside of this library or outside of this DLL, which is something that we'll talk a little bit about later, but it's not something you really need to know too much about for a lot of game development.
Uh, and a internal method cannot be called outside of the library or outside of the DLL.
So, you can't use it across libraries if you import in a library.
Um, we don't necessarily need it to be public, but that's kind of the the default that I like to go with just so that we don't have the extra internal keyword that tends to confuse people.
Okay, so we've got our coins plus+.
And just know though that internal and public for all mo most of your use cases, it's not going to make any difference.
All right, so we've got our coins here.
Let's go take a look at it.
I'm going to hit F12, find our coins variable.
It should be right here after our other um floats because if we keep things nice and organized when we autogenerate things, they'll go into the right spot.
If you make the mess in your file and you have floats and everything defined everywhere, it's not going to know where to put them.
So, let's get rid of this private keyword.
That one we don't need.
It is very redundant.
And save.
We'll go back into Unity.
And what I want to do now is go pick up that coin and see if my score goes up.
I don't need a second player yet.
I'll just come in with my first player.
run around with the keyboard, jump up, and then go see what my coin value is.
So, I come over here, jump, get that coin.
The coin disappeared as I expect.
I'll go to the player, and then let's look at my coins value.
Collapse the sprite renderer, collapse the player input, expand out the player, and since I can't see it here, I need to go into debug mode to actually view it.
Got a couple options.
I can go up to the top here, hit the little dots, and choose debug from the drop down.
It's just off screen there.
And then I can scroll down.
I can see that coins is equal to one.
I don't generally like to do that, though.
I like to switch this back to normal.
And then right click on the player and go to the properties window.
And then have this nice properties window that I'm going to drag over here.
And then I'll set this one to be in debug mode.
So that way I have my normal inspector, but then I've got this extra window where I can see the value.
So, I can see that the coin's value right now is one.
And when I stop playing, let's hit play again.
It should go to zero.
And then when I jump up and get the coin, go back up to one.
Let's just double check that that's the case.
So, switch this to debug mode.
It was in debug mode, but it's not showing.
So, we're going to switch it out of debug mode to normal and then back to debug.
For some reason, it wasn't updating the view.
There we go.
It switched to one.
All right.
So, let's stop playing and go create this a pre prefab out of this gold coin.
So, we'll go to the prefabs folder.
I'll take the gold coin and drop it in here.
And I'm going to zoom out.
And I want to place a couple of these coins so I can pick them up with both players.
So, I'm going to select the coin and duplicate it with control D.
And hold control and just drag it up a little bit.
So, get these kind of spaced out.
Get a row of maybe four of them.
Grab this row of four.
So, I'll select the first one, hold shift, select the last one.
So, I've got all four of them selected.
Then, hit control D, and still holding control, just drag them over to kind of grid snap them.
Control D again.
Do it again.
And again, now I've got a 4x4 grid of coins.
I don't like that that my hierarchy now is getting polluted with all this extra junk, though.
It's filling up with coins.
And now all I can see is coins here.
So, I'm going to rightclick and create an empty game object.
Call this coins.
I'll reset the transform position and everything else.
Just reset on the transform.
Go select all of the coins.
Drag them onto coins.
And now I've got a nice collapsible folder of my coins.
Let's save.
And then what we're going to do is jump in with two players and make sure that the coin values are updating for both of the players and they both have their own scores.
Eventually we're going to turn these into UI elements, but we don't have those yet.
So, we're going to learn how to use the debug view.
So, I've got my player here.
I'm going to switch this to normal and back to debug.
This is player one.
Let's dock this down here on the bottom view.
Now, I'm going to rightclick or I'm going to join first with my second player.
There we go.
Then right click on that player or right click on the players player script.
So, select them, hit properties, get the second one here.
And I'm going to drag this side by side with my first player.
So, and I've got player one on the left, player two on the right.
I'm going to switch player two's view here to be in debug mode as well.
Scroll down so I can see the coins on both of them.
All right, they're both at zero.
Now, let's go run over here with player two.
Grab a couple coins and watch my coin value go up.
Look at that.
Coins two, three, four, five, six, seven, eight.
You can see player two's got some coins.
And player one's going to run over here, go grab some coins for himself.
And you can see now he's got six coins as well.
So, it is working.
We're collecting coins and we're collecting coins across both players.
So far, I think this is good.
So, we'll go into plastic.
Make sure that our scene is saved.
Everything else is saved off.
So, that we added gold coins or I'll just say added coins and checking our changes.
Now, let's add those coin sound effects so that when we pick up a coin, we get kind of a nice little feeling and some feedback outside of the data and the UI stuff that we'll eventually add.
So, here I am on Open Game Art and I've searched for coin and there's an 8bit coin sound effect pack.
Sounds pretty good.
So, I think I'll use that.
I'm going to download this pack, open it up, and copy out all of these 10 coin files.
So, I'll hit Crl + C, get them onto my clipboard, and then go into Unity.
We'll go to the project.
And actually, I'm going to go to window and layouts and go to default to just reset my layout.
Get rid of those two extra properties windows that I had.
And then I'm going to go to my audio folder, rightclick, choose show and explorer, pop up that little window, and then hit enter to go into the audio folder and paste in my coins.
Here I've copied all 10 of the coins.
I think that I've copied them and they're pasting.
There they go.
So, they should all pop up and appear in here.
We're going to start by just using one and then I'll show you how we can use multiple to add kind of that ramping up effect as we pick up more and more coins.
So, let's go select our player.
I'm going to go down in level one, find our player, and then open up the player script.
When we add a point, and our coins get it incremented, which is down at the bottom, let's for now just tell it to play a sound effect.
We'll say underscore audio source.
Remember, we have that reference to the audio source.
I'm going to go up home and just show you real quick.
We have that reference to the audio source that we get in awake.
So, we'll use that audio source down here.
And we're going to not use play like we did before.
We've used play for jumping, but we're going to use the play oneshot method.
Play oneshot allows us to pass in a specific audio clip or sound effect and just play it once.
It doesn't have to be the one that's assigned and we don't have to reassign or change the one that's assigned.
We can just call play one shot and pass it in the clip.
To do that, we need to give it a reference to an audio clip though.
And we're going to name this, let's call this coin sound effects.
And I'm going to start with an underscore because it's going to be a private serialized field.
So I'll call this underscorecoin sfx for sound effects.
And then I'll add a semicolon at the end.
Go over to the coin sfx.
Hit alt enter.
and we'll generate a field for it.
It's going to know what type because I'm passing it into play one shot which takes an audio clip.
So, it's going to know to generate an audio clip.
I can hold control and click on it or hit F12 and find it right up here.
Now, I don't like the position of this.
I want it to be up here with my serialized field.
So, I'm going to select line 29, cut it with Ctrl X, go up here and paste it right below that snow acceleration.
I'll add the serialized field attribute over the private keyword.
So, start with a square brace, serialize field, and ending square brace.
So, now I have a coin sound effect that I should be able to assign in the inspector and play whenever we pick up a coin down here with the play one shot method.
Let's go into Unity and assign that.
So, we'll go find our coin sound effect right here and let's go to the audio folder.
And I'm just going to take coin one, drag it in here.
Now, if I just do this and save, I should be able to hear my sound effect every and everything, at least on level one.
Let's go try it out.
So, I'll run over here.
Well, I got to hit play first.
Run over here.
Jump.
Oh, got to unmute so that I'm not muted.
Jump.
And I heard two coin sounds.
Let's try a second player, though.
Let's hit play.
Run over here.
Jump.
No sound effects.
So, why are there no sounds there? Okay, think about it for a little while.
I'm not going to tell you the answer yet.
Let's go to level two.
Let's run over here.
Oh, I don't have any coins on level two.
So, you can't figure it out with level two.
Think about it for just a moment on level one.
Why did player two not have any coins? See if you can figure out the reason.
And if so, fix the problem real quick.
If not, then hang on just a second and I'll show you the solution.
All right, hopefully you already figured it out and don't need my help.
But if not, or you might got a little stuck or just want some confirmation.
The problem here is that when we create our second player, let's hit play real quick.
And I'm going to spawn our player.
So, hit the button and our second player comes in and we go select this second player.
The second player's coin sound effect is not assigned.
The reason for that is because we didn't apply the change to the prefab that we made on this instance of the player.
So, if I go select the prefab, let's stop playing.
I go find my prefab here and go select it.
You'll see the prefab version doesn't have the coin sound effect.
If I go select my player, hit the overrides button though, you see there's an option to apply all.
If I click on this, let's see, I'm going to have to drag the inspector over to here.
And if I click on the overrides and then click on the player script, you'll see that I can actually see the difference right here.
The coin sound effect hasn't been applied.
So I just hit the apply button or apply all.
And now it's going to work for multiple players.
So now if I run over there with my second player or if I add some coins to level two, the players in both of those will be able to pick up and have a sound effect.
Let's go just double check that.
Sounds good.
Now I'm getting some cool sound effects on both players.
So I think it's time to save my scene.
Go into plastic.
Let's go find my plastic window.
Window and plastic SCM since I set reset to defaults.
So that we'll we've added coin sound effects and check in.
Now we're going to add some UI elements for our players so they can see their score and health without having to look at debug stuff.
And also just to make it a lot easier on us.
So you don't want to have to pull up debug windows all the time when you know you're going to want to have these on display anyway.
So let's start by creating a new canvas.
And we're going to use this canvas to show our player input or our player info for just the first player.
So we'll go game object and UI.
And we're going to start with an image which will automatically create a canvas with an image underneath it.
I'm going to dock this to the top left.
So, we'll click this set this anchor presets, alt and shift, and hit the top left there.
And then let's go to the game view so we can see it and get a good preview of what it looks like.
It's going to be right here at about a 100x 100.
That's probably a fine size for now.
I'm going to change the color of it.
The default color is uh white, and I don't particularly like that.
Let's go back to a default layout here.
I've messed up my layout just a little bit, and my inspector was too small.
So, in here, we'll go change this color to be something closer to my players color, one of these blues or something.
Go back to that game view.
Um, let's let's actually go select him just like that.
Get it exactly matching.
So, I've got this little panel up here.
And then underneath the image, I want to go add a text element.
So, we're going to rightclick and we're going to choose UI.
We're going to choose text mesh pro text.
And I'm going to call this score text.
And I'm going to set the value here in the text to be zero.
We're going to center it.
So I'm going to use the center alignment here and the center right here.
And then we're going to set the erect transform value to be a stretch.
So that it will just fill this area in with some value.
We'll change the font asset.
Instead of using that liberation sands, let's go use bangers again.
And then let's turn on auto size so it can get nice and big.
Right now it's just the coin counter.
It'll be big.
We'll shrink it down and add health and all that stuff later.
But since we only have one thing to show in there, let's make it nice and fat so we can see see it easily no matter what size our screen is.
All right, so let's go rename our image.
Now, this isn't actually going to be an image.
This is going to be a panel for our players.
We're going to bind this panel up to player one.
Then we'll make another one for player two and so on.
So, we're going to rename this from image to player panel.
And then we're going to create a script for it, a player panel script.
you might have guessed.
So, let's go into the assets folder and scripts.
Rightclick and choose create.
Create a new C# script.
Call this player panel.
Capital P's in both spots.
Again, no spaces in our script names.
Once that's created, it's going to pop up the code editor.
That's fine.
Not going to find my file.
I'll go back into Unity.
We'll go select that player panel and we're going to assign it.
Before we do anything else, we're just going to drag it on.
So drag the script onto that player panel object in the inspector so we can see it right there.
Then we'll open up that player panel.
Now player panel is going to be responsible for updating that text so that it shows our current score.
And we're going to start by doing it in a less than efficient way and then refactor it into a more event driven way shortly after.
So we're going to begin by adding in a way for our player to assign themsself to a player panel.
And we're going to use what we call a bind method.
So I'm going to take my start all the way to my update.
Delete them out.
And we're going to make a public method.
So write the word public void because it's not going to return anything.
Bind b i n d.
This is not a hard-coded keyword or anything.
It's just a very common pattern where we want to link two objects together or bind them together.
We're going to bind a player to a panel so that that player's health score and everything else shows on that specific panel.
So, we're going to add an open parenthesis and we're going to need a player to be to pass in.
And look at that.
Since it's named player panel, code's named bind, the AI is already able to determine that we probably want to pass a player in.
So, I'm going to hit tab and let it autocomplete.
We'll hit enter and add in our braces.
And we have a bind method that allows us to pass in a player.
What we're going to do here to start is just cache the player.
So, we're going to save the player into a private variable.
And we'll just use the variable name underscore player and we'll say equals player.
Add a semicolon.
We'll hit home and alt enter and generate a field.
Now, the reason for this again is so that we have this player after this method call.
So after bind is called, the player is saved off into this field that we can use later because we're going to want to use it again in our update method in just a moment.
So right down below, we're going to add an update.
I think we just deleted the update, but we're readding it and we'll remove that private keyword.
And in the update method, we want to update our text to just show the player's current core value or their current score.
We don't have a reference to our text though, so we're going to need to get our text mesh pro text.
And I know that this player panel is going to have multiple text objects.
So, I'm going to need a way to just assign one.
To do that, we'll add a serialized field attribute and then just a field for our text mesh pro text.
And to do that, we use the keyword or the class name tmp_ext.
So, that is the class name for a text object or the text component that you're seeing in Unity.
Technically, there are two sub versions of it.
There's a ui one and a um there's one for the UI and then one for worldsp space stuff, but the tmp_ext allows you to access all of the things that you need for both of those at least for setting the text and all of that stuff.
So, we have tmp_ext and we're going to call this underscore underscore score text the word score.
So, underscore and then the word score text.
This is the text object for our score.
I'm going to add an enter extra space there and then get rid of this private keyword just to clean it up.
I find that the less keywords I have in here, the the better and the easier it is to understand.
So in our update method, we'll say underscore score text, that's a very difficult one to say, do set text, which is going to change the text or what you see on the screen in that text object.
and we're going to set it to our player dot and here we need to get the current coin value.
So let's go look at our player again.
I'm going to hold controlclick on our player and right here we have our coins value and our coins value right now is private.
It can't be accessed outside of this player class.
If I go back in here, if I try to access underscorecoins and add a semicolon here, it's going to give me an error.
If I put the mouse over it, it says coins is inaccessible due to its protection level.
So I need to make this publicly accessible.
I can hit F12 and then just put the public keyword here and save and then go back and my error is actually different and it'll say that it can't convert from an int to a string.
And here it's saying, hey, set text requires a a string.
You can see the first parameter there, string source text, but you're passing in an integer.
So, we need to convert this integer to a string and we can do that with the tworing method here.
But that's not all there is because right now we've got a little bit of messy code.
Now, technically this is going to work.
Technically, there are no problems, but in a theory sense and in a keeping your code clean and keeping it so that you don't accidentally mess up in the future, there is a a big problem here in that our coins value is now accessible from anywhere and can be set from anywhere.
So that means that inside of our update method, we could actually say player_coins equals zero and our coin value would get reset to zero every frame.
Now, we probably wouldn't do that, but we might do something else accidentally with this coin value outside of our player class if we allow it.
Or somebody else on our team might go, "Oh, hey, I need to modify the player's coins and not know that we have an add coin or add points method that plays a sound effect and does all that other stuff." So, they might go bypassing that to modify our coin value and it can cause big problems and bugs in the future.
So, how do we fix that? Well, first we'll just crl x and get rid of that line.
And we're going to hit F12 and go to the coins field here.
And what we can do is turn this from a field into a property.
And we make it into a property that can only be set from this player class.
So we're going to add an extra space here.
And we're going to add after the word coins and going to delete that semicolon.
We'll add an open parenthesis.
And then we'll put look at that.
It's already trying to autocomplete.
get and a semicolon which means that the get part of the public value is now or the get part of coins is now public.
So reading it is now public.
Get is to read a value.
But the set value we want to make private.
So here you can see it's already recommending we do private set.
I'll just hit tab and let it autocomplete.
So now coins can only be set from inside of player, but it can be read from anywhere.
Let's save this off.
Go back over to that player panel and just rewrite that code.
So I do underscoreplayer.co_coins equals zero.
You'll see that now we have an error saying that it cannot be used in this context because the set accessor is inaccessible, meaning that the set is private and we can't get to it.
That's almost perfect.
I'm going to remove that line.
The last thing I'm going to do is rename this because since it's no longer a private field, it shouldn't have that underscore.
At least not by my naming conventions.
Go with whatever your company or whatever uses.
But if I use my naming conventions, public properties do not have an underscore.
That's only for private fields.
So I'll hit controlr control.
Get rid of the underscore and capitalize the C and go back to a Pascal case.
I'll save that off.
We'll do a build real quick.
And then we're going to jump into Unity, assign our text to the score text object, press play, and absolutely nothing's going to happen.
Why is that? because our player still isn't binding to the panel.
So, the last thing we're going to do is go into our player and just do a quick binding in our player before we set up a system for multiple players to bind to multiple panels.
We'll go right into the player script and inside of our awake, we're just going to do a quick and dirty find object of type and we'll give it the type player panel.
So, this is going to find the first player panel in the scene.
and it's going to search through all of our active scene and find a player panel.
And then we'll get our parenthesis in there.
And we want to say bind.
And here it takes in a player.
And we're on a player.
So we can use the keyword this to just pass in this current instance of the player.
Add a semicolon.
And I'm going to add an extra line here just to clarify and make this a little bit cleaner.
We'll save it off.
Jump back into Unity.
And I should now see that my player is bound up to that.
And as I grab some coins, the value goes up.
Let's let's go check that out.
And then when I come in on a second player, I expect them to bind over it and kind of take control of that panel because they haven't set up code to deal with multiple players in multiple panels.
We only have one panel right now.
So here we go.
We jump.
Coins are going up.
Looking good.
And if I come in here on another player, look at that.
It went to a zero.
And I jump.
And now coins are going up.
and the other character or other other player no longer affects that because he's no longer the one bound to it.
And if I go look at my player panel and go set this into debug mode, you can actually see in here the player that's bound.
You can see it's this player.
I can click on it and you can actually see that it's this specific player, which was our second one, not the first player.
Pretty cool, right? So, let's stop playing, go into plastic, and commit our changes.
So, I'm going to save our scene.
And here we'll say that we created the player panel in level one and found it to the first or most recent player.
And we'll check that change in.
Now, we're going to extend our UI and make it work for two players.
Of course, you can go on to four players or however many we want, but I think that two is a good point to get to.
So, we've got our canvas here.
Let's add in a new script.
We're going to add in a player canvas script that will allow us to bind multiple players to our player panels.
So, we're going to go to the scripts folder.
I'll rightclick and just choose create and choose C# script.
Put in the word player canvas.
Capital P, capital C, and no spaces again.
We'll open that script up.
And that didn't open.
There it goes.
Now it's open.
And inside of our player canvas, I want to have a way to have multiple player panels so that we can assign all of the player panels that are children to it and then have our players just try to bind to the player canvas and it'll know which player panel to give them.
So to do that, we're going to first delete our start and updates.
Something I almost always will end up doing.
We're going to add a serialized field.
And the serialized field is going to be of type player panel, but it's going to be an array of them.
So to make it an array, we're going to use the square braces.
That means that we can have multiple, any number of them really, and then we can go through or iterate through them or find them by index.
And we're going to call this underscore player panels.
Now, we're going to create a bind method.
So let's go look at our player panel.
Inside of our player Oh, there it is.
Our player panel, we have a bind method that takes a player.
We're going to take this definition right here, public void bind, and copy it.
I'm going to go right into player canvas, and paste.
We're going to have a public void bind that binds to a player right inside of here.
And what we want to do now is find the correct player panel and bind to that panel.
And we've got a couple of ways that we could do it.
We could maybe keep track of the last player panel that was bound up and then maybe store that in some variable or something.
Um, we could maybe put them into some list or some collection of them.
There lots of different weird ways that we could do it, but we're going to go with what I think is the smartest and simplest way.
We're going to get the player index from the players input play the player input script on the player and then we'll just get the player panel that matches at that index.
Check this out.
So, first thing we want to do is get the player input.
So, we'll say var player input equals player.get component and we'll get the player input.
Then we'll get the index from the player input.
say player input dot whoops player input dot player index.
So we've got this value and this is going to be either zero for the first player, one for the second player, two for the third player, three for the fourth player.
Essentially it's going to be a number starting with zero for the first player and counting up.
So we want to get the player panel at that index and then bind our player to it.
So we have this index and to get the player panel at that index, we just take player panels.
We'll put it right here at the front underscore player panels and add a square brace around this player input player index.
So we'll either get number zero or number one or whatever number.
And then we will bind to that number.
So call the bind method and pass in our player.
We'll save this off.
Let's go into Unity and see what these indexes look like on the player panels and go assign them real quick.
Might make a little bit more sense if you're a little bit confused.
So, we'll jump back into Unity.
Go to this canvas.
Let's rename it to be player canvas so that it matches the name of our script.
We'll assign the player canvas script to it.
I'm going to collapse these other components here.
And then we've got our player panels on our player panel.
So, we'll just drag the first player panel on, drop it on, and you can see this is element zero.
So, this is at index zero.
Now, we don't have a second player panel.
So, we're going to need to create one.
To do that, we'll select our player panel, hit control or command D to duplicate it, and then expand out that rect transform that I just collapsed.
There we go.
We want to anchor and dock this to the top right.
So, I'll click on the anchor control, alt, and shift, and hit the top right.
And there we go.
I've got one up at the top right.
This will be player panel 2.
I'm just going to rename it.
And then let's rename the first one to be player panel one, just so that we have nice, clean names and we can see them when we're in our canvas.
Let's go back to the canvas.
We'll drag player panel two on.
And you see that that has an element of one.
So player index one is going to get assigned to that.
Let's save.
Press play.
And now when we go into Unity, we should see, let's see.
Well, first we're going to see some errors in the console.
But let's run over here, grab a couple coins.
And you can see that I've got some points on one of my players.
Let's go grab some coins on the other one.
And you can see that uh well that's interesting.
Oh, I've got coins on the other player.
Now, the reason for this is that inside of my player script.
Oh, let's go take a look inside of my player script.
When we call the bind method, we didn't actually call into the new player canvases bind.
We're still just binding the player panel.
So, we'll change player panel to be player canvas and save.
And that should fix our binding issue so that both players get their own canvas.
Let's check that out.
and then we'll check out the error message that's in the console.
So, we'll press play.
Now, I expect the first player to be bound to the left one and the second player to be bound to the right one.
So, come over here, get a couple coins.
Looks good.
And I come over on player two, grab some coins, and it's looking pretty good.
Things are looking solid.
So, this is good, but we do have an error here.
The error's gone away, though.
You can see that it was logging out an If I uncheck this collapse, there's a whole bunch of them.
I have 347 of that error specifically.
If you don't see them, just make sure that the error is not disabled.
You can disable and enable them right here.
I've reenabled it, and you can see them right here.
So, why did it stop? And what was causing it? Let's stop playing and play one more time.
And look at the errors.
They just keep going and going and going and going.
Watch what happens when I join with player two.
The errors go away.
Now, let's take a look at what this error message is saying.
I'm going to hit collapse, and you see that they're all the same error message, meaning that it's the same thing happening every single frame happened 994 times.
Let's go double click on it.
We can see it's in player panel.cs on line 19.
An object is not set to an instance of an object.
So, we're trying to use something that doesn't exist.
We'll double click on it.
And if you look here on line 19, the thing that doesn't exist is probably the player because we haven't assigned or bound a player to this object yet, but we're still trying to update it.
So imagine we've got our second player panel there.
Our first one's got player one already kind of assigned automatically and instantly, but player two isn't assigned until they come in.
But every frame until they come in, we're trying to use that player and read a coin value.
But there's no player assigned.
So we need to add in a check here on line 19.
We'll copy the word player underscore player, add in a new line.
We'll say if player, and then add the closing brace, and then add in a tab here just to clean up our formatting.
So now it's only going to do this code if we actually have a player bound.
If we haven't bound a player yet, we won't see that code running.
We won't get the error.
Let's try it out.
We'll press play.
And look at that.
No more error.
All right, let's stop playing and go into plastic SEM.
Actually, before we do that, let's turn this into a prefab.
Let's take our player canvas, go into our prefabs folder, drag it in.
So, we now have a player canvas prefab.
And then, let's load up level two.
So, I'm going to hit load scene.
We'll drag our player canvas into there as well.
So, we have a player canvas in both of our levels.
So, that way our game is going to work across levels.
We don't have to worry about it yet.
We're going to talk more about how to deal with this across a whole bunch of levels later, but for now, we're just going to make sure that it's in both of them.
save so that both of our levels are saved.
Remember, if you don't know how to get both of these levels out here, let me just show you one more time.
So, if you double clicked on a level and it just opened one, you can just click and drag and add another level there.
You just don't want to have them both loaded when you play.
Just make sure that you hit unload to unload the scene that you don't want to play.
Or you can always rightclick and hit remove to unload it completely and just get it out of there.
Let's go into plastic now and say that we've added multiple player player canvases or that yeah, we added the player canvas.
Added player canvas and support for UI on multiple players and we'll check that in.
In this section, we're going to learn about data persistence and data management because it's something that a lot of people really struggle with when it comes to game development.
And that's partially because it's just so easy to save data off in any way that you want.
It's really easy for us to add data to just about any type of object when we're writing code in C.
Like you saw with our coins, we added a data for coins onto our player just by adding a coins field.
Remember, let's go open up our player and take a quick peek at it.
We just added this coins.
Technically, it's a property with a backing field, but we added this coins property, and we just keep track of how many coins our player has right there on the player object.
And it seemed like it kind of worked.
But you probably noticed that when we actually start playing and go from level to level and stuff like that, that our data is getting reset.
Let's go check it out real quick and talk a lot more about this and then we'll go into some really interesting solutions.
So here I can come over, pick up some coins, go to my next level, and my coins are back to zero.
And if I go back to level one, my coins are still at zero.
Go pick up coins, and my coins get their values again.
So the reason this happens is pretty simple.
It's because this player object with the number of coins that we have, let's go expand out our debug mode here and take a look at it.
our player with the number of coins, which is right now set to six.
And if I jump up, it'll be a seven.
That player object is going to be destroyed, and a new one will be created when I go into level two.
Let's go take a look.
Go into level two.
And well, we've got a totally different player object.
In fact, I can make this even more obvious by going to my level two.
Let's go into scenes.
Go to level two.
And I could do something different to this player, like maybe change his default color.
Or let's go out of debug mode into normal mode.
And I'll just make him like a 50% larger.
So on level two, we've got a big fat tall player.
And on level one, we have a smaller well smaller scale down normal scale.
So here's my level two version of the character and the level one version.
So got two separate objects.
It's not the actual same object being recre or being reused even though it shares a prefab.
It's actually two separate instances of that object.
So, what we need to do is get our data to persist across different versions of our character.
Let's reset this back to a one and a one.
And uh I'll leave the position there.
And we'll talk a little bit about what what our options are here.
We first we could just maybe keep a player around and keep a player object that we keep from scene to scene and just move them around.
But you're going to notice that that'll cause some issues as your game gets bigger.
If you got something small and you've just got one player object, it's not too difficult to keep them around and keep them from scene to scene as you load in.
Maybe using something like the don't destroy onload method, which will keep an object around even when you load into a new scene.
But I found that in general there's a better way to do it.
And the easier way to manage data and the easier way to make it so that you can keep building on your project later, do things like saving and loading, having multiple players and all that, is to separate that data off of your player or separate it off of the objects that care about it into a system that can just persist that data.
give you back a player or do all of the things that you might want to do in a nice clean way that doesn't kind of bloat and make your player script get nice and big or cause other issues along the way.
So, let's start by opening up our player script.
And the first thing that we're going to do is create a new player data object.
We're going to create a new class that will store data for our player and store this coin info there and then kind of wrap that or hide it.
We're going to do this in a way that seems like it's not changing anything at all.
And then we're going to do a little switch and you'll see the magic kind of appear.
So, let's start by creating a new class.
Um, let's do this down at the bottom of our player script.
And we're going to put in a value for coins and we'll add in a value for health as well.
So go down to the bottom with control and end.
Go down and just start typing.
We'll put public class player data.
Inside of it, we're going to put a public int coins not in coins and a public int health.
So now I've got a public class player data with a coins and a health value.
I'm going to copy the word player data.
Go all the way up to the top of our class.
And right here, um, right above our coins, actually, we'll put a private or we won't need to put the word there.
We'll just put player data data player data.
And let's initialize it to be have a new value at start.
So, we'll say equals new player data.
This will give us a brand new blank player data with a zero for the coins and a zero for the health.
Now, when we access our coins, instead of just directly accessing this integer, let's modify the coins on our player data object.
To do that, we've got a couple options.
I could write this out as a big U property, or I can use my expression body property syntax to simplify things down.
And after the get, instead of having it be automatic, we'll add a lambda statement.
So, that's an equals and a greater than.
and we're gonna have it get back or return back the player data's coins.
So to do that, we do underscoreplayer data coins.
So now this coins value whenever we read it, it's actually going to read from player data and it's going to read its coins value.
Kind of confusing if you're not sure what we're doing yet, but don't worry, it's going to make a lot more sense really soon because we're going to split this player data off so that it's not just part of the player.
We can see it other places and rebind it and stuff.
So we've got our get method.
But what if we want to set it? Well, for the set, we need to add a lambda statement as well.
We do the equals and greater, which means that when we want to set, we just want it to run the code after this lambda statement.
That's all this is doing here.
When we read this, when we read the coins value, it's saying, hey, when you try to read this, just return back out this value instead.
That's what this weird little get syntax does.
This private set means that only set it from inside this class.
And when you call set, you say coins equals something.
Then instead, technically underneath do this code, which is going to be player data.coins equals.
And here we use the special magic keyword value, which is the one that's being passed in here.
You can see that it's blue because it's a kind of a keyword or a special word.
So this has now wrapped my coins data in this player data.
Let's save, minimize our code editor, and then go back into Unity.
and we should expect to see exactly the same behavior.
That's what we're looking for right now.
And then in the next section, we're going to figure out how we can split that off and have that player data persist even when our player doesn't persist.
So, let's see.
We play.
Run over here.
I've got zero coins.
Yeah.
Yeah.
Yeah.
Run over here.
Jump up.
Get some coins.
Go into the next level.
No coins again.
Go back over here.
And got my coins again.
All right.
So, we're going to stop playing and we're going to commit this to plastic again.
We should have exactly the same functionality.
We've just added a player data layer.
We haven't actually taken advantage of it.
So, we're going to say that we added player data layer to the player, but didn't hook it up completely yet.
And we'll check those changes in.
Now, we're going to go back into level one and start to set up our game management and data persistence system.
To do that, we're going to create a new script.
And this script is going to be our game manager.
And the game manager is going to be responsible for a few things, but the key thing it's going to do is bind our players data to the player.
And then we can bind other things up later.
Let's start by going to the scripts folder.
And we're going to create a new script, a new C# script called game manager with a capital G and a capital M.
And we'll even get that special little logo or icon on it.
Let's see.
We should get the little gear icon that appears because game manager class name is associated with a little gear.
It's just kind of a a built-in thing.
And you can actually go into these icons.
So, if I select a class, you can actually go in and select the icon, go search for an icon, pick whatever you want, or change the specific one there.
Game manager just happens to have a gear assigned to it by default by the name.
That's because most games are going to have a game manager and they just I think thought, hey, why not give that one a cool icon? All right, let's go to the player input manager component now or game object.
So, in level one, we've got a player input manager that has our player input manager component on it.
And we only need one of these in our game, and we only need one game manager in our game.
Well, two things.
So, what I like to do here is combine these into a single object.
So, I'm going to take my game manager script, drag it onto the player input manager, and then apply the override.
So, go to overrides, and hit apply all so that it gets applied to the prefab.
Then, I'm going to rename this to player input manager and game manager.
And then hit, let's see.
No, there's nothing to apply now.
I just wanted to update that.
But I do want to copy the name here.
And then go select the prefab and rename the prefab as well, just so that its name matches.
And to do that, just select it, hit F2, and then paste in the new name.
So now it's got a new name here.
I should see in plastic SCM that it's got it as moved, which just means that I renamed the file.
So if you rename a file in source control, you're generally going to see that as a move.
Some source control systems will show it as a rename.
A lot of the time though, you'll just see it as a move.
So we've got a moved item here.
We've got our new changed item, which is kind of changed and moved.
And we have our game manager.cs script.
Let's go modify that script now.
So, I'm going to go to my player input and game manager and open up the game manager script.
The game manager script's got a start and an update.
And I'm going to delete both of those out of here.
The first thing that I want to do with my game manager is just make it be a singleton.
I want it to be an object that's going to be only one instance.
So, there's only ever going to be one game manager around.
And I want to make sure that if there is a game manager in a scene and I load into another scene, I don't end up with two game managers.
So let's write the code to do that.
Now, we're going to add an awake method.
And the first thing that we're going to do is set our instance to this object.
So we'll say instance equals this.
Now we'll generate that property.
So I'll hit alt enter with instance selected and create generate property or click generate property.
We should get a public game manager instance with a public getter and a private setter.
What this is going to do is allow us to keep track of whether or not our game manager has already been spawned.
We'll do that by checking to see if the instance is already set.
But to do that, we're also going to need to add in the static keyword here before game manager.
And that's so that every game manager that spawns, if we have a game manager in level 1, 2, 3, 4, 5, 10, and so on, all of them will always share this same instance.
So if a game object the game manager gets destroyed and a new game manager comes up, well this instance would be here.
It' be kind of a problem.
Not exactly what we want.
But if we spawn multiple game managers, like we go from level one and it has a game manager to level two and it has a game manager, then we're going to know that this has already been set by level one's game manager.
So we can add a line here before the instance equals this and say if instance is not equal to null.
So if it has been set, then what we want to do instead is just destroy this new game manager.
So we'll say destroy game object and then return.
So now we've got an object that should only allow us to have one of and it will well right now it won't persist across levels.
So we need to add in one more line of code down here on line 17 and say don't destroy onload.
There we go.
I spelled it right.
And we'll pass in our game object.
Let's save.
Go set this up in Unity and see what it does and how it feels before we dive into how we're going to bind the player data up to it.
So, we've got our game manager here.
It's assigned.
And if I save my scene and just press play, I should see that it moves now down into the don't destroy unload section.
And that's because we've added that don't destroy unload.
So, I've got it right here right next to my debug updater.
So, I've got my player input manager and my game manager here.
And if I go over to the flag or here, let's go grab some coins first.
Go grab the flag, you'll see that I still have my game manager, my player input manager.
My inspector did not clear out.
That's because this object is the same exact object and it's still selected.
Go down here.
I can see I don't have a game manager and player manager cuz they got destroyed.
And if I go into level one, that's the ones that were placed in level two.
If I go back to level one, the ones that were placed there got destroyed.
And the one that I already had from before is still around.
So now I've got an object that persists across multiple levels and I need to use that object in my singleton my game manager here to keep track of this data and start to bind it up to players so that we can have our player continue their game across multiple levels.
So first though let's go into plastic and commit our change because we've added a singleton game manager and we need to have that in here before we start hooking up player data to it.
So, we'll go in and save our scene, make sure everything is saved and updated, and then check in our changes.
Now, let's take a look at our game manager and our player input manager.
What we want to do is have our game manager know whenever there's a player added and then have it hook up or bind up data to that player.
And we're going to do that by calling or tying into the player input managers on player joined event.
So, we're going to start by opening up the game manager.
And in the part where we do our awake, where we set our instance, we've already got our player game or our player input manager right here on this object.
We're just going to need to get a reference to it.
We'll get a reference to it and then register for an event that will fire off whenever our a player joins.
So, to do that, we're going to open up our game manager.
We're going to say get component and we want to get that player input manager and we'll have open close parenthesis and then we want to register for an event on it.
So we can do that by either saving off this player input manager to a variable and then referencing it that way or I can just put the dot right after and search for the event that I want.
Now if you look down here at the bottom you'll see that there are actually a couple different options that allow me to filter things.
If I click the lightning bolt, it'll actually show me all of the events.
Or at least it's supposed to.
I don't know why it's not showing me all of the events.
There we go.
I clicked it twice and now it showed up.
So, we've got an onplayer joined and an on player left.
These are things that will get fired off or called or we can tell it to do something essentially when this event happens or when this thing happens.
So, when a player joins, we want to run some code.
So, I'm going to just double click on it and hit plus equals, which is going to add a method to be called after or whenever a player joins.
So, do plus equals.
And then we need to give it a method name.
I can hit tab to get a game manager on player joined.
But I'm just going to type in the name of the method that I like instead, which is going to be handle player joined.
I'll add a semicolon.
Hit the left arrow once so that my cursor is on handle player joined.
Hit alt enter.
and then we'll generate a method for it.
So what's going to happen is every time a player joins with this player input manager, which remember is going to be the same one because it's on this game object that we're not destroying.
It's on the singleton that we're keeping around.
So whenever a player joins, we're going to call our own special code handle player joined and it will give us the player input of the player that joins in a variable named OBJ, which I don't like.
So I'm going to rename that to player input.
and then it's going to throw an exception which is not very handy.
So let's start by just logging out a debug log so we can make sure that all of this is kind of making sense that we're getting an event when a player joins.
We can see it and we can maybe do something with it afterwards.
So we'll start by writing the code debug.log and we'll add in some open parenthesis.
And here I'm just going to write handle player joined and then let's add in a space a plus and we'll put in player input.
two string so that way I can see the the name of the player or whatever some input about the player.
We'll put a semicolon and I said some input but really some data about that player input is what I mean.
So we'll save that off.
I've got my semicolon at the end.
We don't necessarily need the two string by the way.
We can delete that and it'll do the exact same thing because what happens is when you combine a string with another object, it automatically implicitly calls to string on that object which just converts it to a string.
All right, let's save.
And we'll talk more about overwriting that and some cool things you can do with that later.
Let's save though.
Get rid of the star.
And oh, first let's go get rid of these private keywords that I don't like to have.
Those two right there in front of the methods.
Remember, we do need it here because we don't want other things setting this game manager instance.
All right.
Now that I've saved that, I'll go into Unity.
And we're going to open up the console window here.
Make sure that it's cleared and press play.
Now, I expect we'll see our player here.
So, we we're in I'm in and nothing happened.
If I go over to the next level, you'll see that nothing happens.
I'm not getting these player joined events.
And the reason for that is actually right here.
It's this notification behavior on the player input manager.
By default, it's set up to use the um kind of old send me.
I call it old, but it's this older default send message system in Unity, which would call events or it would call methods by their name kind of magically.
And when I say that, I mean that there's no hookup in the code.
The hookup was all done kind of right here.
Here you can see it will send messages to the game object on player joined and on player left.
Which means that if I had a method in there named on player joined with the right player structure.
So with a player input parameter and an on player left with a player input parameter, it would call those.
But it won't call the things that I've registered for like on player joined.
These are C events and by default they're not on.
What we need to do instead is change this notification behavior to invoke C events.
Now, if I change my level, you'll see that I got the notification down here that a player joined when I went into a level.
And if I go back to the other level, I'll get another notification.
Now, if I stop playing, that's going to reset.
So, I need to make sure that I stop playing, switch it over to invoke C# events, go to overrides, and apply all so that it gets applied to my prefab.
I can select the prefab, and it should show just like this that I've got invoke C# events.
Now, if I press play, it should clear my log.
Or maybe it's just going to add on and I'll get a third and fourth entry depending.
Okay, that's clearing.
I get get my entry and you can see that every time I join I get a player joined message or every time I enter I get a player joined.
All right, let's stop playing and we're going to do well our final bit of code here.
We're going to hook up our player manager or our game manager to our player data.
To make that happen, we'll add a new line right here after our debug.
And we'll say player data.
Player data equals get player data.
And we'll pass in player input dot player index.
So, we're going to create a method that will give us back the player data for a specific player based on their index or their number.
Remember, zero is going to be the first player, one will be the second, and so on.
So, I hit alt enter, and we'll generate a method for that.
We'll figure out how to get that player data in just a moment.
For now though, what do we want to do once we have the player data? Well, I want to get our player object and tell them to use this player data.
So, we'll say player input.get component and we'll get the player object.
And then let's save this off.
Actually, let's say var or let's say player player equals and we'll get that component just so we can make this a little bit more explicit and a little bit more obvious what we're doing.
So, we're getting our player data from this method.
We haven't figured out how yet.
And we're getting our player by calling get component.
Remember, our player input is on the same object as our player script.
Let's just go take a real quick peek at that just so that it makes sense.
We got our player here and our player input there.
All right, let's go back into that game manager script.
Game manager.
And then in here, let's bind our player to the player data.
So, we'll say player.bind bind player data.
Now, this method does not exist, but it is a very common syntax that you're going to see throughout this course and throughout game development and all programming in general.
We want to bind up this player data to this player, which essentially means that we want to associate them together so they're they're linked together.
We're going to hit alt enter and generate a method for bind.
And then we're going to hit F12 and go into it.
Now, our bind method doesn't have to be complicated.
It just needs to set our local player data object to be this player data.
So, we'll say underscore player data equals player data and save.
I'm going to go back, go into our game manager.
The final thing we need to do is determine how to get a player data.
So, what we'll do for that is store off some list of player datas.
And if we don't have one for the current player, we'll just make a new one.
So, let's create a list.
I've deleted out my throw statement, but let's make a list down here at the bottom.
make a list of player data and we'll call this underscore player datas and let's initialize it.
I'll just hit tab so that by default it's a new list and it's not a null list.
We don't want it to be null.
We want it to exist.
So we've got a list of player datas and then in our get player data method we'll check to see if we have one for our player index.
So we'll say if player datasc count is greater than our player index.
So we have some left or let's let's say that we don't have any left.
Let's say that our count is less than or equal to our player index.
And we'll talk this through in just a second.
So if our player data's count is less than our player index, we want to make a new one and add it to the list.
So let's do that and then talk through the code.
We'll say var player data equals new player data data data and then player datas add and we'll add in that player data.
Just hit tab and it autocompleted for me.
Final thing that we want to do is return player datas at player index.
There we go.
It's autocompleting.
So let's talk this through.
On line 34, if we have no player datas in our list at all, count is zero, which is equal to our first player, which is index zero.
So, it's less than or equal.
It's it's equal.
So, it will get a true statement here, and we'll create a new player data, and it'll get added to this player data list.
If we call it again though, say we go to level two, and we try to get player data for index zero, well, then player datas is going to have a value in it.
So this will be false and we'll just return back the player data at index zero cuz that's the first player.
So we'll get back the first player data if we add it put in a one here.
So we get the second player then we would go against count of one and we would say hey um we actually are equal to one.
So our player index is equal to the count.
We've got one player here.
Second player comes in with an index of one.
We create a new one and so on.
So, let's save and let's go into Unity and see what this magic does for us.
So, we'll press play.
We should be able to run over, grab some coins, watch our coin count go up, go to the next level.
We still have eight coins.
Let's go back to level one.
Go grab some more.
And look at that.
Our coin count is persisting across levels because it's now being saved in our game manager.
Let's go into the plastic and commit our changes.
And then we're going to add a little bit of debug stuff so we can see it slightly better.
So we'll save and we'll say that we've added player data to the game manager and hooked up bindings.
And we're checking our changes.
One of the few things we can't do right now is see our data outside of the UI.
There's no easy way to go in and view what we've got right now.
So, if I go into debug mode and look at my game manager, you'll see that I don't actually see my player data there.
Even if I press play, it's not going to just magically appear.
And I'm I'm not able to easily debug it because of that.
If something's going on with my coins and I want to see what the values are at, let's go find this thing again.
I can't really see anything there.
So, what I need to do is make two little changes to the player data class.
Well, one change to the class and one change to the reference or the use of it.
So, let's stop playing.
I'm going to go into the game manager.
And the first thing I want to do is just add a serialized field attribute here.
So, we're going to serialize out the player datas.
And this is just so that I can see them in the inspector temporarily.
So, we'll save that off.
And then let's go look at the inspector and see what it shows now.
So if we go find our game manager, got to make sure I select the actual game manager.
See that it still doesn't show up.
And that's not a bug.
That's not something wrong here with what I've done.
It's actually a side effect of my class not being serializable.
So what we're going to do next is go to the player data class.
I'll just hit F12.
And right at the top of the class, we need to add the serializable attribute.
Let's see if I can spell that right.
I can't.
So I'll just let it autocomplete.
So it'll add the serializable attribute which of course needs the using system name space.
So if I move this player data into its own file which I'm going to do right now, alt enter and hit move to file.
You'll see that inside of my player data class or script.
Let's go find it.
Here it is.
We have using system.
We've got the serializable attribute and the player data with our two public fields.
Let's go check that out now and see if our two public fields show up.
Well, we've got player datas that's showing up here.
Let's hit play now and see what we get in the first player data.
All right, here we are.
And it it's not showing up right, but I think if I go select and reselect.
There we go.
My game manager.
I can see it.
So, if you get it kind of weird and bugged out, I think it's from the level loading and the object moving.
It's not updating the inspector.
If you see that, that just reselect the object.
And let's go check it out.
I've got my player datas with an element zero, some coins.
You can see my coins going up.
And if I join on player two, here we go.
So, I run over here, go get some coins.
And if I look at this second element, you see that I've got coins in there as well.
So, now I'm getting coins in both of them.
I don't need to be in debug mode.
I can see that in normal view.
And my coins are tracked independently across levels.
Let's go to the next level.
You can see that this character, player two, isn't in.
They haven't rejoined yet.
But if they rejoin, they've still got their 11 coins.
And if I click through, you'll see that they've got the same amount of coins here once I rejoin again.
I got to rejoin the level every time.
We haven't dealt with that yet.
But everything else is uh I think pretty much just working and keeping track of of our data.
And hopefully you're starting to see some of the benefits here.
Now we've got an easy way to rebind up our player data to a player without having to do any complicated stuff in our saving and loading of data is also going to be easy as well.
So I'm going to stop playing.
We'll go into plastic SCM.
Make sure that I've saved my scene.
And then we'll say that we made the player data serializable and check it in.
Now that we've got coins and health on our player, let's start implementing health so that our player can actually take more than one hit without going to a new level.
Nothing would suck more than having a two-player game and the second player dies instantly and game's over.
So, let's put in another way for our player to die and take some damage or maybe an easy way to take damage so that we can start putting in some health points or health bars and then see see that system kind of come together without having roaming enemies that we have to run into.
We're going to begin by creating some lava.
So, all you need to do is in fact, let's do this as a little mini challenge.
Create a new lava object off to the left of our ground.
So, I want you to create an a lava that's about the same size as this water, but just over here to the left.
I want you to start doing this on your own.
See if you can go through the process and make it kill the player on touch at first.
Once you're done with that, resume the video.
I'll run you through that process and then we'll start talking about how we're going to change our player to not just die every single time they touch stuff.
So, go ahead and go through that process.
Make your lava right here.
Make it kill the player on a single touch for now.
and then we'll run through the the rest of it afterwards.
All right, I'll assume that you've either gone through it or you don't want to and you just want to be guided through.
So, let's find the water object and create a new lava object off of it.
I'm going to actually just start by duplicating my water, hitting W and holding control and dragging it over here.
So, I've got a object right in the same spot where I'm going to put my lava.
I'll rename my water to be lava.
And then I'm gonna rightclick on it and hit prefab and choose unpack completely.
I want to just make a new prefab out of this lava.
So I want to remove that com that prefab reference completely and make some totally different type of object.
First thing I want to do is remove this buoyancy.
I don't need that.
I'm not using buoyancy.
This thing's going to kill the player when they touch it.
I think I want to uncheck the is trigger box as well and uncheck the water or remove the water script.
Don't need that.
Oh, and I don't need this.
Well, maybe for the audio source, I'll add a lava effect.
So, I might leave that audio source on for a while.
Now, we'll add a component.
I'm going to add the spikes component so that it kills the player.
And then expand out my sprite renderer and change this water top high to be a lava top high.
Let's see if I can find lava top high.
And drag it on over.
Look at that.
I've got some nice, beautiful lava.
I need to change my bottom part here.
So, I'll rename this from water bottom to lava bottom.
And then change the graphic here.
Oh, actually, look, I've got lava right there.
I just drag it right over.
So far so good.
I think um let's see if I got anything else missing.
I don't think so.
Let's hit save and press play.
I should be able to run over now and I think kill myself on that lava.
Unless I've missed anything.
Let's see.
I run over here.
I jump and yep, level one.
Go back over.
Here we go.
Bam.
I'm dead again.
All right, so we've got some lava.
That's exactly what I wanted.
Now I've got something that I can use to kind of bounce my player off and have them take some damage.
So let's go into our prefabs folder, turn this into a prefab first.
We'll take our lava, drag it right out here into prefabs, and then we'll save our scene, go into plastic, and say that we've created a lava prefab and placed in level one.
And we'll check that in.
Now that we have our lava set up, let's actually take a look at our spike script because right now we're using that to kill our player.
And it's not on spikes, so it seems like it doesn't make a lot of sense.
Maybe we should turn this into something more reusable and then figure out how we can have it actually damage the player without killing the player.
So, let's take a look at our spikes script.
The spike script right now checks for a collision enter.
And if we collide, it checks to see if we hit the player.
If so, we load scene zero.
Instead of doing that, let's have our player just take some damage and then our player can decide what to do from there.
Maybe they took some damage, their health went down, they bounced up, maybe they ran out of health, and we need to kill that player or maybe load up another scene or go back to the menu.
We'll let the player decide instead of a spike script that's just randomly attached to objects.
So, we're going to add in some braces here and we're going to delete out that scene manager load scene zero.
And instead of doing that, we'll get the player object.
So we're going to say var player equals collision collider.get component and we'll get the player.
If that player is not equal to null.
So essentially assuming that we have a player there, which we should because we're getting that with the tag.
We can actually remove that tag check in a moment.
But if we have a player, then we're going to tell our player to take damage.
And that's it.
We'll start with just having them take damage.
We'll create a method for that by hitting alt enter and hitting generate method.
Now let's start our take damage method by just having it load scene zero.
So we'll say scene manager load scene and we'll pass in that zero.
Save and make sure that everything works.
Again, we've done no functional change, which is the way I like to do it before we make a a big change.
We'll make a structural change here so that we change what's doing the thing.
And then after we make sure that that works, we'll change what that thing is.
So right now, the player is going to call load scene zero instead of the the spike.
Let's see if that works.
So we should be able to hit play, run over, jump on that lava or a spike or anything else, and go to our menu.
There we go.
We're to the menu.
That's working just as expected.
Let's go back into our spike script and then we'll go to the take damage method of the player.
So, I just went in, hold control, and click on take damage to go to our take damage method.
Remember, this internal word is essentially the same as public.
I'm going to put public here over both of these internal keywords just to make it a little bit less confusing.
Less keywords.
All right, so we've got our take damage method.
And instead of loading scene zero, what I want this to do is just reduce our health.
And if our health gets below zero or two zero, then we could load scene zero.
So, we'll say health minus minus but we don't have a health right so instead we need to say underscoreplayer dataalth minus minus then we'll say if our player data oh is it going to autocomplete for me player data health is less than or equal to zero then I want to do this load scene so I'll take line 508 and put it up here in between the parenthesis and then we'll return so we lo we'll load scene zero and then exit out because that means that we've died.
Otherwise, well, we probably just want to make the player do something special like play a sound effect or bounce them or maybe flash the screen or do a screen shake or something else.
But for now, let's just save and not do anything.
We'll just say, "Hey, if you take damage, we'll reduce your health and if your health gets down below zero, we'll kill you." But right now, our health is always going to be zero.
So, we need to come up with some sort of a default value for our health.
And I'm going to do that right inside our player data.
We'll just assign it to let's go with a value of six for now.
So imagine we've got six little hearts and we're going to go through six of those.
We'll bind this all up and kind of figure out a better place for this later.
But for now, if we just default initialize it to six.
Whenever we get a new player data, it should have a value of six.
Let's go try that out.
So we're going to hit play.
We'll select our game manager so we can see all of the data across our game.
Well, specifically our player.
Good.
There we go.
We've got six health.
And I'll go run over here.
Jump on the lava.
Bam.
I've got five health.
Four health.
Three.
Two.
And notice when I walk on it, I can even kind of bounce myself cuz I go up and down off of the lava.
But there we go.
I'm down to zero, even negative one, and totally dead.
Go back in.
And I'm actually still going to be dead here the second I touch anything because my health doesn't reset when we start a new game.
So, something else that we're going to have to deal with is resetting that data.
For now, though, let's go into our plastic SCM setup.
Make sure that everything is saved.
So, that we added take damage method to player and hooked it up in spikes.
And we'll check that in.
in.
in.
Now that we have our player taking damage from the lava, let's make it a little bit more interesting.
Let's make it so that our player bounces off or gets knocked off of the lava or anything that they hit that causes them to take damage.
Going to knock them back and then maybe even add in a sound effect.
To do that, we're going to open up our player script again and we'll take a look at the part where we take damage.
When we take damage, what I want to do is have our player kind of fly back the opposite direction of they hit something.
So, if they hit something straight up and down, they kind of go up.
So, if they land on something, they go up.
they had something at an angle that kind of go up and at some sort of an angle kind of off the way that they should bounce back.
So to do that, we're going to need to know the angle of the collision that our player came in at and then tell them to bounce in the opposite direction of that angle.
So what we're going to do is take a parameter in our take damage method.
Right now it takes no parameters.
That's why the parenthesis is open.
But we're going to make it something like the bind method where it will actually take in a parameter that's a vector 2.
So put vector 2.
And what we want here is the hit normal or the kind of collision normal which is the angle that we've come in and collided at.
So this is going to be a vector 2 representing the angle that we collided at.
And I'm going to call this hit normal.
And then down here on line 159, we're going to tell our rigid body to add some force in the opposite direction of our impact so that we bounce back the opposite way that we hit.
To do that, we'll call underscore RB add force and we'll give it our hit normal.
And we want to multiply it by some velocity amount, some knockback velocity, but we want it to be the negative value of that knockback velocity because we want the opposite of our hit normal.
So we can do a negative hit normal here or star equals negative knock let's call this knockback velocity.
In fact I'm going to move the negative over to hit normal just so that it's a little bit more obvious.
So we've got our knockback velocity.
Now it doesn't exist.
We're going to generate a field for it and that'll be a serialized field.
So I hit F12 to go up to it.
Replace private with serialized field.
And we want to replace this vector 2 as well.
By default, it just assumed that I want a vector 2.
And that's because we were multiplying a vector 2 times that number.
So it just says, hey, you probably want another vector 2.
But we really want a static or a floating point variable.
Not a static, but a single variable or value that we can multiply our hit normal by.
So we can have some sort of a magnitude or intensity for that velocity.
So we're going to place replace vector 2 with float.
And then we'll give it a default value of I'm gonna go with 200.
I'm gonna move this up by my other serialized fields.
So I'll cut it and then paste it right up here by my coin sound effects.
And then we'll save.
Now I should be able to go back into Unity and see my value right here of 200 right below my coin sound effects.
Oh, if I Oh, I have an error though.
So I don't I'm not going to see that.
Let's take a look at this error here.
It says that spikes.cs CS has an error saying there is no argument given that corresponds to the required formal parameter hit normal of player.take damage vector 2.
And here it says this is on line 15 at column 24.
The line number is always good.
The column number usually okay but not always the not always 100% accurate.
Line 15 though.
So let's double click on it.
And here you can see that we're calling line take damage.
And it looks like column is correct too.
But we're calling the take damage method.
And it now has an error because we didn't pass in that parameter that it wants, the hit normal.
I hit F12 to go to this.
Let's go back and just pass that in.
To get the hit normal, we actually can grab it from our collision data.
We'll pass in collision.
And the contacts are all of the different points that our collision hit.
So most of the time our contacts is going to be an array with one entry.
And it'll be like, hey, right here at this specific point on my finger is where the contact is.
It'll tell me the exact point.
and that normal if I hit in two spots in the exact same frame though I might have contacts like this where I've got or technically if it was yeah I could end up with two contacts or maybe they're like this and they're like side by side and two I'm touching at two spots on on my hand with this this other hand object I could have two in there but by default we're always going to have at least one so we can access it by index zero and then get the normal so we're going to pass in the normal of the first contact if they have multiple context, we're just going to ignore it and assume that the first one is the correct one.
Most of the time we're only going to have one though.
So, let's save.
At least most of the time with our normal character on a normal surface.
We're going to have one contact.
So, here we'll save.
And now we should no longer have that error.
If I hit control shiftb, I should get a build succeeded in the bottom left.
And I should be able to go back over to Unity, see my knockback velocity, press play, and now run over to this lava and start bouncing off the top of it.
Let's see if that's the case.
So, I run over here, jump, and bounce, bounce, bounce.
You can see I'm getting knocked up.
Let's change this to a 300.
And let's give myself some more health.
I'm going to go select the player input manager and game manager.
Grab my health and crank it way up.
Look at that.
I got 405 health.
Now, I bounce.
And that feels like a more reasonable amount.
Thinking 300.
Let's go with a 400 and see what that looks like.
Yeah, I think um I might even be good with a 400.
So, I'm going to stop playing, put in a value of 400 here for my player, save or go to overrides and apply all.
And then I'll even go into the code and just change that default.
That's one of the things that I like to do a lot.
If I come up with a new default value that I think I'm going to use, I just go into the code and change it right away.
So that way I don't have these overrides in two different values and have to try to remember which one did I actually want to use.
Now I've got my knockback velocity in there.
We'll go in save our scene one more time.
Go to plastic SCM.
Say that we've added a knock back to taking damage.
And you're going to notice that this happens when we hit the springs as well.
Anything that causes damage is now going to knock us back.
Now that our player can bounce, let's add some sound effects as well, so that when we take damage, we hear a little grunt or some feedback that our player can see or hear, I guess, not necessarily see, but kind of get that into more of their senses.
We've got a coin sound effect, and I already like using that.
So, let's take a look at what we've got there and see how we can maybe use that same or similar code to do a sound effect for taking damage.
So, go open up our player.
We've got our coin sfx here and let's just duplicate this line.
We'll take line 16, duplicate it, and call this hurt sfx.
So, this will be our sound effect for when we get hurt.
Now, let's find where we're calling our coin sound effects and see how we were doing that.
Again, to find all references to our coin sound effects, I can select it and hit shift F12 or rightclick and there should be a find usages or find all references option.
Find all references right there.
Shift F12.
That'll bring up a dialogue down on the bottom of my code editor, my IDE, and it'll allow me to find all of the usages, which there's only one of.
So, when we add point, we call this audio source.play oneshot coin sound effects.
So, you can probably already guess what to do here to play a her sound.
I'm going to give you a couple seconds to go figure it out, put it in yourself, and then I'll run you through it.
So, go ahead and do that.
And now I'll run you through the solution.
So we're going to cut line 146 or not cut it, just copy it.
Select it and copy it.
Go down to our take damage.
And when we take damage, we'll paste.
And we'll call the hurt SFX.
We'll save that off.
Minimize Unity.
And then we'll go download a sound effect.
So I've got these five hit sounds from Open Game Art.
I think that these sound pretty good.
I'm going to download this one.
And then we'll pull in those sound effects.
So, I'll go open up that pack, go into the MP3 folder, and I'll just take hit um let's just take hit one for now.
We'll take hit number one.
We'll put it right into our audio folder.
Right click, create.
Actually, you know what? I'm going to take all of these.
I'm going to take hit one through five and die.
Copy them.
And I'm going to paste them all inside of my audio folder.
So, go back to my audio folder.
Right click, show and explore.
I think I accidentally created a new window in there.
A new folder.
I don't want to do that.
I'll delete that and just paste instead.
There we go.
I've got my hits and my die.
Let's see them all appear right here.
And then we'll go assign one of the hits to the player for now.
So, we'll just take hit number one and drag it in as the hurt SFX.
Go to overrides and apply all so that it gets updated in our prefab.
If I select our prefab here, we should be able to see that we've got that hurt SFX there.
Looks good.
Let's press play now.
Go jump over there, take some damage, and see if we hear a little bit of a noise, some audio feedback that we're taking damage.
All right, four, five, and six.
Okay, and we're dead.
Did I take one extra hit? I've lost track now.
Go to my game.
Yep, I did take one extra hit.
So, we didn't die when we got to zero health.
Let's go open up that game manager.
Not the game manager, the player script, and see why did we not die when we got to zero health.
This is, I think, going to be the final challenge of this lesson here.
So, take a look at this code and tell me if you can figure out why our player lived until they got to negative one health.
If you can figure it out, go ahead and fix the problem right now.
If not, then hang on just a moment and I'll show you.
All right, hopefully you already fixed it or paused it and found the solution.
But the problem here is actually pretty simple.
On line 157, we're doing a check to see if the player data.health is less than zero instead of less than or equal to zero.
So if it gets equal to zero, we'll just subtract one.
It'll go to negative one.
It'll play the damage.
They don't actually die.
We want this to be a less than or equal to zero.
So just add in the equals to the right hand side of that less than statement.
I'm going to get rid of this extra space that we don't need.
Save.
Go back into Unity.
And let's go to plastic SEM and commit our changes.
So, we fixed health and we added hit sound effects.
So, let's put this in added hit SFX.
And I'm going to uncheck this new folder that I don't want added that I didn't mean to create.
So, we added hit sound effects and fixed player dying properly at zero health.
Then, we'll check in our changes.
Now that our player's health system is working, we need to hook it up to the UI and give them some sort of a health indicator, like a health bar or some hearts.
Right now, the only way to see the health is to look in the inspector.
And here you actually have to make the player data public to even see it.
I can watch my health go down as I jump on things.
Oh, and got to go reselect him.
There we go.
I can see my health there.
Jump on things and watch it update.
If you don't see it updating, just make sure you go reselect your player object.
But that again only shows up if I make my player data public.
And using the inspector or the editor like that is obviously not what we want to do.
Instead, I'm going to remove that public keyword that I just temporarily added.
We'll watch this turn gray and disappear so we can't see the player data.
And then we're going to modify our UI, our player canvas and our player panels specifically to give ourselves the ability to um have health bars on here.
So, let's start by going to our player canvas.
We're going to open up that prefab.
I'm just going to hit the arrow right here to open the prefab in context and go to the scene view.
Now I should just see the prefab edit mode.
I can zoom in and out with my mouse wheel and get that left mouse button to pan around.
And the first thing I want to do is update this player panel.
This player panel one, I want to make it four times the size.
So twice as tall, twice as wide, and then give it some room for health bars or for health hearts.
First, I'll switch out of debug mode on my inspector into normal mode.
She's in the little hamburger menu or the three dots there.
And then we'll modify the size.
So, I'll set this to 200 by 200.
So, just type in a 200.
Tab and 200.
Go select the score text.
And this one I only want to cover like the top 75 pixels or so.
So, I'm going to set the bottom here to what is it going to be like? 125.
So, that way I've got 125 below it.
And now you can see I've got my number up here.
And if I go to the game view, well, you can't see anything cuz it's in context in the prefab edit mode, but you can see right here about the size that I've got.
I've got 75 pixels for the top and 125 to spare for the bottom.
Now, I'm going to go to the panel, right click on it, and choose UI, and we'll create another panel.
That's going to be this bottom panel here.
We'll set the top to 75 so that it covers the bottom except for the top 75 pixels.
This is the offset from the top, assuming that it's filling out and stretching everywhere.
And then I'm going to disable the image because I don't want a background image for this part.
Underneath this panel, I'm going to rightclick and choose UI and image.
And we're going to add a heart.
So, I'll once I've got the image here, I'll name it heart.
And I'll name it heart_1.
And we're going to use that name specifically because you'll see why in just a moment.
And then go to the source image and we're going to search and we're going to find the heart.
This should be included with the assets that we got.
And I'll just take the full heart right here.
Now I'm going to go up to this panel and we're going to add a new component to it.
What I want is multiple hearts to appear in a grid.
Either a 3x two grid or a 4x2 grid or 2x two, whatever size it is you end up deciding you want to go with.
But I'm going to go with I think a I think I'll do a 3x two grid.
So to do that with the panel selected, well first let's rename this panel to hearts.
And then with the hearts object selected, we'll hit add component and add a grid.
Just search for grid and find not grid itself though.
Grid layout group.
Look for this one right here.
Grid layout group.
And add that component.
We'll change the cell size to thinking 66x 66.
So that's 200 / 3 like 66.66 right around there.
Give us the right width.
And then I want the height to match so that I keep the right ratio.
So, I don't want this to be like um 100 tall and stretch out or anything.
I want it to match.
So, change that back to a 66x 66.
Then, I'm going to go to this heart and I'm going to duplicate it.
Now, the first thing I want to notice if I duplicate it right now, the name gets kind of weird.
It's heart_1 and parentheses 1.
I'm going to delete this heart and we're going to go into our options or preferences.
We'll go to edit and go to I believe it's under project settings.
And then we need to look for Let's just search for duplicate.
Let's see if it shows us our text.
Nope.
Um, let's see.
I think it's under editor.
We'll find it right here.
We'll find the option uh right here under editor in project settings.
You'll see the game object naming and it's got prefab and then the parenthesis and one.
You can choose a couple options.
There's prefab one or prefab_1.
and we're going to go with the underscore one.
If you prefer dots, go ahead and use dots.
It doesn't matter.
I just don't like using the parenthesis because it ends up being a mess.
So, here I've changed it to one underscore one.
I'm going to close that window, go to file, and save project, which is going to update my project settings.
If I go to plastic SCM, you see that now my editor settings and project set, I think it was the project settings specifically, they got updated for that.
Now, let's go back to our heart.
So, I'm going to go select my heart and I'm going to duplicate it with control D again.
Now I've got a heart two, a heart three.
One more time.
Keep doing it.
D, d I've got all of my hearts lined up here.
I've got a nice row of six hearts, which is just about what I want.
Now I need to do this for my other player panel as well, player panel two.
But I don't want to recreate all of this work and have it become a mess and, you know, possibly mess up one and have to do this work multiple times if I go to three or four players.
I don't want to have to do it over and over either.
So, what we're going to do is create a nested prefab.
Now that we have our hearts created here, what we can do is create a prefab out of our player panel and then have our player canvas.
Use multiple of that prefab.
So that way, we don't have to modify both of these panels.
We just have to do the one.
Now, to do that, we're going to go to the prefabs folder here.
We'll take the player panel one, and I'm just going to click it and drag it in to turn it into a prefab.
Now, now it'll become a prefab.
obviously see that it's turned to blue and it shows up down here.
I'll rename the prefab instead of it being player panel one to just be player panel.
We'll still leave this one here as player panel one because this is the one for player number one.
Then we'll go to player panel two, select it, just leftclick and then right click on it and find the prefab menu and hit replace.
Now we'll choose the player panel and check that out.
We now have a panel that's here but it looks a little bit weird.
And the reason it looks a little bit weird is that right now we are overriding the width and the height.
If I go to overrides, you can't really see it there.
It's actually not really overriding.
It's kind of at the one level up.
So, what we need to do is select the width, put in a 200.
Select the height, put in a 200, and tada, everything is fixed.
So, now you can see we've got both of our player panels.
I'll rename this one to player panel 2 since it's for our second player.
And then we'll save off our player canvas by going back, hitting save, and then let's go back into game view.
And we should see both of these.
Let's just press play, and make sure that the coins are still working, and we've got both of the UI elements there before we start worrying about code.
So, we've got it here.
I can run around.
I can still go grab some coins.
Watch my UI update.
And my health bars should not update yet when I go over here, but I should still be able to die.
So, there we go.
We got I'm still taking damage.
No updates yet because we haven't hooked up the code.
But we do have these panels here and we have our nested prefabs.
Let's take a look at those prefabs one more time.
So, if I go into my level, you can see I've got my player canvas here.
If I select it, I can see the prefab data on it.
It's referencing this player canvas prefab.
And I can go select it by hitting the select button and finding that canvas.
If I select one of these panels underneath it, though, these are referencing the prefab.
That's the player panel prefab instead of the player canvas.
They're children of the player canvas because now we're using the nested prefabs.
And you hear about nested prefabs, which you'll probably hear about a lot with Unity.
Just remember that they're essentially a prefab that's reused underneath another prefab.
And almost or most of the time, not I'd say almost always in the experience that I have, they end up being UI related type things.
Occasionally you'll have some nested prefabs with characters, but most of the time they end up being UI related because it just makes a lot of sense with UIs because you're creating these components and those prefabs are getting put in as components of other bigger components and you're building up these systems.
So now that we've got our nested prefabs, I want to go into plastic SCM and just go commit our changes really quick.
I can see though that my player is showing here has changed.
So, I'm going to right click on it and hit diff just to make sure cuz I don't think I changed anything in it.
Let's scroll through.
It says the files are identical up here.
So, it looks like I didn't actually change anything.
I must have just uh opened and modified the file accidentally.
So, I'll just hit right click on that one specific file player and hit undo changes.
And then I'll check in my changes that we added.
Nested player panel prefabs.
We have our hearts now in the UI.
So, let's bind up to them or use them in our player panel binding.
I've got my player panel one selected here.
And let's go open up the player panel script.
First thing we're going to need is a reference to those hearts because I want to either change the sprite or toggle them on and off based on what our current health is.
We can maybe use the empty health image or just turn the sprite completely off.
Let's go up to line eight.
add a new line after it on nine and we'll add a serialized field which it's nicely autocompleting.
And here we're going to add an image array.
So we'll put image image g.
And if I hit enter right now or tab or anything that's going to autocomplete to the wrong one.
What I want to do is go up and find this image that's unity engine.
I'm not even going to do that though cuz I want to show you how to manually do it in case you can't find that.
So I'll hit escape here and add in our two square braces.
That tells it that it's an array, not a single image.
And I'm going to call this underscore hearts.
Now I'm going to pull this up to the other line just by going up to the end of the line and hitting delete.
And just kind of re it'll re realign it.
And then let's hit alt enter.
What's going on here is it's saying, hey, I don't know what image you want me to use.
There are a bunch of different types of images all defined in different libraries and namespaces.
There's one here in the media types, the net my media types.
There's one for the Visual Studio editor.
There's one for the Unity engine UI.
And there's one in the Unity engine.
Uuielements namespace.
The one that we actually want to use because the UI that we're using isn't UI elements is the Unity engine UI.
And as soon as I click on this, it's going to add a statement right up at the top that says using Unity Engine.UI.
Let's hit it.
And you can see that got added.
If it doesn't pop up, you can't get the popup to appear.
You can of course just type that text right in.
But if you have multiple of them, like say let's duplicate this and say that I also have the UI, what was it? UI elements.
Now, it's going to give me an error because I'm going to say, "Hey, I don't know which image you want.
Do you want the one from UI or from UI elements?" If I just get rid of this UI elements because that's the new UI system that we're not using.
It's it's a slightly different UI system.
We're not using it right now.
So, we don't need that in here.
We remove it and the error is gone.
So, let's go to our update method.
Now that we have our hearts here, let's say we have all of our hearts assigned, all six of them or however many there there are.
What we want to do is in our update just update the hearts that are visible or change the sprites.
Again, we'll go through optimizing this in just a moment.
But first, let's make it work exactly like our score text does.
So, we'll add a new line here, and I'm going to add an open brace because I want it to do more than one thing after the if statement.
We'll delete that close brace.
Go down here, hit enter, and add in a closing brace.
Now, I've got braces around my set text.
And after we set the text, what I want to do is loop through each one of these hearts.
So, we're going to iterate on them with a for loop.
And we want to just toggle whether or not they're enabled based on how much health the player has.
And it's a pretty easy thing to do, but it's kind of a a unique I guess it's it's a cool thing that you should definitely remember how to do.
Let's just type out the code.
Let's start with the for loop.
So, type four and then hit tab.
It'll kind of autocomplete for me.
If it doesn't autocomplete, you can of course just type out the entire thing.
But we got the int i equals zero with the parenthesis.
The semicolon here, the i less than length, which got not selected yet, but will be in a moment.
And then it gave us some braces.
So I'm going to hit tab a couple times, go over to the word length, and what we want to do is loop up to the number of hearts that we have.
So we'll go from zero to hearts hearts.length, which is however many hearts are in that array.
If we put nothing in there, it'll be zero.
Nothing will happen.
And if we put one in there, it'll run through this loop one time with I being zero.
If we put two in there, it'll run through this loop two times with I being zero the first time and I being one the second time.
So let's write some code inside of this loop to do what we want it to do.
So first thing we want to do is check to see well the first thing we really want to do is modify whether or not this thing's enabled.
There's really only one thing we want to do.
I'm saying the first thing, but there's really one thing we want to do.
So, what we'll do is get Well, first let's let's split this out just a little bit.
Let's say heart spelled that wrong.
Um, oh, it's image heart equals underscore hearts at index i.
So, this is going to get us the heart for the number that we're on.
So, zero will get us the first one, one will get us the second one, and so on.
And you'll see these indexes match when we're looking at them in the inspector.
So, we'll get the heart, and then we'll say heart.enabled enabled is equal to I greater than player.alth.
Oh, health.
There we go.
And I actually said that wrong.
It should be less than.
And then we are done.
Except we have an error.
So let's first evaluate what this code is doing and then we'll fix the error.
So on line 27, we set enable to be either true or false based on whether or not this I value is less than the health.
So if it's heart number zero and our health is at one, then it will be set to true.
If our health is at zero, then we're dead and it's set to false.
If it's if our health is at three, heart zero will be true.
So the first heart, heart one will be true enabled and heart two will be true enabled.
So I'll have three hearts enabled with three health.
But heart three will be I index would be three which is not less than our health.
So that one would not be enabled.
So that's the logic here.
But we don't have access to this health.
We can't actually read it.
It says hey player does not contain a definition of health.
Oh no.
What do we do? How do we possibly get this? Well, all we need to do is kind of expose this variable to our player.
Right now it's in our player data and we want to make it read only accessible to our from our player.
So we'll hit alt enter and generate a property.
Now if that doesn't work for you, you can of course manually type it in, but I'm going to hit F12 and go to that property.
It should have put it right below my coins.
And if you don't have your things organized, your properties aren't all together and stuff.
It's it's kind of going to be a crapshoot.
Who knows where it's going to end up.
If you keep things organized and clean, it'll show up in the exact same spot.
So, we've got our health here, and we don't want to have this setter part.
We We kind of want this getter like we have here, but we don't necessarily want the setter.
So, I could copy this getter part, paste it right in here, and then replace coins with health.
Now, there's also a shorter way to write this, though, because if we don't want to do a a setter at all, and we just want to get her, we can actually remove the parenthesis and the get and just do it like that.
And this will give us a property that can read this health, but it cannot write or modify it.
And that's because we don't want our UI modifying it.
So I'm going to save with control S.
Go to our player panel.
Save with control S.
I'll do a build with control shiftB.
And just make sure that it succeeded, which you can see right down here.
Build succeeded.
And we'll go back into Unity.
Let's take a look at our player panel.
We should now see our hearts appear here.
See, we did expose those as a serialized field, right? Yep.
There we go.
any second now.
I expect it to recompile unless I've got an error here.
It's not picking it up yet.
So, I'm going to go to my scripts folder, rightclick, and just hit the reimpport.
Where's that at? Reimport.
See if that recompiles.
It should force a reload, and then have this code re-update.
Let's see if that works.
There we go.
Now, I've got my list of hearts.
Now, I'm going to go into my player panel prefab.
I'll just hit the open prefab button.
And what with the prefab open, I'm going to have the player panel selected.
I'm going to choose the lock.
Just go hit the lock so that my inspector doesn't change.
And now if I go select a heart or anything else, see that the inspector stays the same.
Now I'll select heart number one, hold shift, select all the way down to my last heart, heart number six, and drop it right on the word hearts.
And I should get element zero all the way through five with hearts 1 through six in that exact order.
So remember this is that I index of 0 1 2 3 4 5 that I was talking about.
Let's go back.
Hit save.
That should save our prefab.
And if I go look at the other player panel, it should also have hearts.
But I don't know.
Yeah, I'm not in lock mode.
Make sure that your lock turned off.
When you got out of prefab mode, it should have turned off that lock, though.
Now, if we press play, I should be able to run over and watch my health just drop down.
Let's see if that's the case.
I run over here.
Boing.
Look at that.
Health is going down.
And let's add in another player.
So, I run over here with player two.
And it still works.
Everything works.
And it's all hooked up and bound using the same binding that we had on on our coins.
Oops, I can't run over there and get a coin.
All right, let's stop playing.
Go into plastic SCM and say that we set up a basic coin U or not coin, basic health UI.
setup basic health UI bound to the player and we'll check that in.
Now I want to have a little discussion about performance.
Our current setup for the player panel pulls the player and updates the UI every frame.
If we take a look at our player panel script again, I'll go find my player canvas, go grab a player panel, and just pop it up right here.
See, in our update method, if we're bound to a player, we basically update the text every single frame and then update the hearts every single frame.
And while that works and it's not really causing us any problems right now, there are some things to think about with this.
A lot of the time when we have UI data or just data in general that isn't going to change often like our health or our number of coins.
And when I say isn't going to change often, I mean isn't going to change, you know, more than once a second or or very rapidly or very commonly.
It's not something that's going to be changing like every single frame or multiple times a second.
If we had some timer or some count up thingy, that that would be a little bit different.
But if we have something that's kind of a a semi- rare event, at least taking damage should be a semi- rare event in this game, then what we can do instead of polling and reading the data is get notified with an event and update based on that.
And there are some real big benefits to it.
But first, I want to show you the performance characteristics of what we have right now.
Because you might be thinking, looking at this, oh no, this is a nightmare.
We definitely have to fix this.
We can't be just updating and reading things every single frame.
But if I go into our code or sorry into our project and press play and then open up our profiler window which we'll find under the window menu.
Let's let's start playing under window and then analysis and profiler.
I'll grab the profiler window and I'm just going to dock it right in here with the game view.
And remember that our code for the player panel is running every frame in the update.
It does not care about anything that I do.
If I go grab another coin, it's not going to change anything with the way that it's running.
Let's take a look at the code though or the performance data.
Do that just to verify that I'm not making stuff up.
And then talk about how we can optimize what little there is to optimize right now.
So if I let this run and I just click on any frame, it's going to pause the game.
I'll go back to my profiler tab.
A lot of the time I'll just pull the profiler down to the bottom, by the way, so you can see it.
In fact, let's do that.
Pull the profiler down here.
So, if I select a frame, it's going to tell me exactly how long everything took for that specific frame.
Right now, things are not taking very long.
I'm going to hit unpause and just go to the stats window.
See that things are not taking long at all.
We've got what am I getting? 40 frames a second.
I was getting a lot more than that a moment ago, but I think because I started profiling it dropped, but if I go click on a frame and then expand out the player loop down here.
So, with CPU usage selected, I go click on any one of these frames, expand the player loop section, and then I want to look for the update script run behavior update.
That's the part that's running my code.
Script run behavior update.
That's running all of the things that's in our update loops or in our update methods.
There are other things that show up here in our own code, but this is the one that we're going to worry about now and the main one that you're going to see.
So, I'll expand this out again.
you'll see behavior update and below it, expand it out again, just hitting the right arrow, by the way, and the down arrow to go down.
Below that, I lost it.
You'll see that we've got our player update.
And then down here, we have our player panel update.
If I look at the time for the player panel update is the code, the time that it's running here is 04 milliseconds.
That's extremely small.
It's low enough to not really care about.
It's being called two times because we have two player panels.
the one over here on the right and the one on the left.
But it is doing something bad that might not be as obvious and that's this GC alloc.
It's doing 24 bytes.
And if I scroll through frames, you see that it's about the same every single frame.
We get a low number in the milliseconds and 24 bytes.
If I press play, let's see, and then just run over.
I said I would run over here, grab some coins, you see that nothing's really spiking here.
There's a couple little spikes right here, but they're not in this code.
They're around the audio source playing.
If I scrolled up, I could see a little bit more data on there or some rendering stuff and editing things.
But if I look at the actual code for my player panel here or the timings for it, you'll see that it stays about the same.
It's not changing.
So, what is this allocation and how do we change all of this? Let's go back to the player panel script.
So, in the player panel script, the worst part that we have here is actually this right here, this two-string method that's changing our integer value of coins into some text to pass it into the set text method.
There's no easy way to optimize that and to get rid of that.
There are some hacks that you can do, but the best thing that we can do is just only update the coins when um our coins actually change.
And we can do the same for our hearts.
So, let's start by adding an event for our coin updates so that we can get notified when coins change and then update the number of coins that we have.
To do that, we're going to go back to our player script and let's find the part of our code where we modify coins.
Right here, we set the player data coins in the coins section.
So, let's hit shift F12.
See where we set the coin data.
And you see it's right here on player line 145.
we do coins plus+.
So this is the part where we're adding a coin.
So right after we add a coin or change the number of coins, we want to call an event or invoke an event that our player panel can listen to.
This will be something that will fire off or invoke every time our coins change.
So let's go up to the top and we're going to declare this event.
I think we should do this right before our properties.
So, I'm going to add a line right here on line 34 and get a little bit of spacing.
We'll add a public event with a lowercase E and then action with a capital A.
We'll call this coins changed and add a semicolon.
Now, this is going to just allow us to invoke something called coins changed and have any number of things listen for when that coins changed is invoked.
You can have events with parameters.
This is not an event with parameters.
If we had parameters, we would put the type right here, but maybe do like an int and then we would be able to pass in an integer value.
Or we could do an int and a string or something else and pass in multiple parameters.
I don't want any parameters for this though, so I'm going to delete both of those and just have public event action coins changed.
I'll copy the word coins changed.
And let's go find the part where we modify our coins with coins++.
Right here on after line 147, we'll add a new line called coins changed.
And we want a question mark invoke.
Now, we could do just ainvoke, but what that'll do is fail or blow up and or really it's going to give us a null reference exception if nothing is registered for this event.
If we add a question mark here, it's going to check to see that something is registered before trying to invoke it.
You might think, hey, shouldn't that be the default behavior? But hey, this is actually a pretty new thing.
The way that you used to have to do it before was say if coins changed.
Let's see if I can get that spelled out right.
Then here we go.
If coins change is not equal to null, then invoke it.
But this new syntax of just doing it with a question mark, I think uh is quite a bit easier and works a lot better.
Well, it doesn't work a lot better, but makes it less code.
So now we've got our coins changed event here being fired off when we add a point.
Next thing we need to go do is go to our player panel and tell it to listen to that coins changed event.
We'll do that in the binding.
And this is where you'll usually set up your event registrations in some sort of a binding method like this.
So we'll say underscoreplayer.coins changed.
There we go.
Got to spell it all right.
Plus equals.
And we don't do an equals.
We do a plus equals because we want to add something that's listening to this.
Coins changed is an event.
And with events you either add or remove things.
You don't generally set them.
There's there's some hacky ways you can do setting, but we want to do coins change plus equals to add something to listen to this.
And we could have other things listening to coins change, too.
Audio systems, um, event systems like, uh, I can't get my word right.
Um, achievements.
Achievement systems like that could be listening every time coins change.
Let me know see if we broke a record or something.
You could have multiple things listening here.
We're going to listen with a method called update coins.
I'll just type in the word update coins, add in my semicolon, go back to it, hit alt enter, and generate a method.
I said we're going to have a meth use a method named update coins because that's what seems like a good name for it.
We'll remove the word private because I don't need the private keyword.
And instead of throwing an exception and giving an error, let's delete that.
We'll take our line 30 code here, cut it with controlx, and paste it into update coins.
So now whenever our coins change our update coins method should call.
The last thing that we want to do is call update coins when we do our binding so that we get our coin value set immediately when we bind and we don't have to wait for it to change the first time before we actually set it in our UI.
So I'll copy the word update coins here with our parenthesis.
Put it on to line 19 so that we invoke it right after we register.
So now we'll bind to our player.
We'll cache that player into the player variable.
will register for that player's coins changed event.
So in the future when the player's coins change, we'll get notified and the coins well really we won't get notified but the update coins method will be called.
That's the notification.
And then we call the update coins method after we register for that event just so that we have a good default initial value and we have the correct number of coins.
Let's save, jump into Unity, and see that in action.
And then we'll look at the profiler and see if that cleared up our GC allo, which is a garbage collection allocation, which I didn't even talk about the reason it's bad.
So, let's talk about that while it's loading.
Garbage collection allocation or GC alloc memory being allocated by your computer to be used for something and um needing to be cleared up later.
There we go.
Look at that.
We're getting coins and the UI is updating.
Let's go look at this here, though, and see if we're getting a bunch of GC alloc.
So, I go down here to my player panel here, and you see that we've got zero bytes.
I should be able to scroll through eventually and find the one where um where my coins changed.
Let's see if I can do that.
I don't know how many frames ago that was.
Somewhere in here.
I maybe I'm not going to be able to find this specific frame, but there should be a frame where I generate it.
Every time I actually hit a coin, I should be generating 24 bytes of garbage.
Now, the reason this is a problem is specifically on mobile devices.
Re reathering all of that memory that you keep allocating over and over causes those little spikes and hiccups that you see on mobile devices.
It's a lot more pronounced on older devices, and it's definitely not going to be an issue with 24 bytes on this little thing, but it does build up.
So, garbage collection allocations are one thing that you definitely want to worry about.
We're going to be talking a lot more about that when we dive into pooling as well.
The time though is pretty good.
So, no real noticeable difference there.
You see it's still at 0.0.
It's actually faster.
It went from 0.02 to 0.0 because we're no longer doing anything of any real work.
So, small optimization, not extremely useful right now, but it's going to come in handy to start understanding these concepts and to see what other kinds of stuff we can do with events in the next section.
Now, let's go into plastic and commit our changes.
Say that we switched the coin interface to use an event and we'll check that in.
In this lesson, we're going to start with a challenge.
What I want you to do is exactly what we've done with the coin system, but do it with the health.
So, switch over the health so that it only updates in the UI when the health actually changes on the player.
You're going to need to make changes to both the player panel script, not the player data script.
Let's find the player panel script and the player script.
You'll want to add in a new event and hook it all up.
Now, I'd like you to try this on your own and then when you're done, or if you run into any problems, get confused, just continue on and I'll help you with it.
One thing that I want to note is that you should not pass a parameter for this.
Don't add in a parameter for the player's health.
Instead, try exposing the player's health as a readonly thing.
Well, actually, it already is exposed as a read only.
So, don't pass it as a parameter.
That's over complicating things.
And you don't need to do that.
You can do it completely without.
So, go ahead and give it a try and then continue on once you're ready.
All right.
I'll assume that you've either uh paused and done it all or you ran into some issues or you're just ready to kind of go through and want to see the process the way that I'll do it.
So, let's take a look at our action for coins change.
First thing I want to do is add a new event for health change.
So, I'm just going to duplicate it with control D.
Replace the word coins with the word health.
And then let's find the place where we modify our health.
So, I'll copy the word health change.
Get that onto my clipboard.
Select the word health and hit shift F12 to find all references.
That's going to give me the place where I modify it, which it looks like is right here on line 159 of our player script when we take damage.
So after we take damage, right at the end of the method, I'll just paste in my health changed and call the question mark.invoke to fire that off.
Now, if you're wondering what about when our health dies or gets below zero and we die and all that and we load another scene, I probably don't care about things that are in this scene invoking and updating UIs of stuff that's not there.
If that needs to change and rearrange and I need to have something when a player dies and still update the UI, which may very well happen in a moment because we've got multiplayer stuff, then I might move that up there or rearrange things a little bit.
But for now, since if we're loading into a new scene when we die, doesn't make any sense to call this event.
So, we'll save and then let's go into the player panel.
In the player panel, when we bind, just like we do the coins changed registration, let's duplicate that line.
Add a health changed event and call update health.
We'll replace the word coins in both sections.
Hit escape, alt enter, and generate a method for update health.
Now, I can take this line of code right here, or these lines right here, the for loop essentially, 38 through 42.
Crl + X and then replace the throw exception.
Now look at my update method.
It no longer does anything.
It checks to see if I have a player and then does nothing.
So we can completely delete it.
Now our player panel is not running anything every frame.
It only runs something when something changes.
There's one piece that's still missing though.
Look here.
We call update coins when we do the reg after we do the registration.
We're not calling update health.
So let's copy update health.
add it right below with our parenthesis and semicolon.
We'll do another build.
Control shiftB.
Make sure that it succeeded.
There are no typos here.
We'll go back into the editor.
Let's go press play and watch our health work.
Totally bound up.
And we're no longer calling that update method at all.
We've removed some minor performance things, but we've removed them completely.
Look at that.
Our health is updating.
I'll put in player two here.
Here he comes.
Player two, jump, jump, jump.
And the same thing.
So, the health is working for both players.
When we die, we should go back into the menu.
And things are looking pretty good.
Now, I'll go into our profiler real quick.
Let's just take a look at the data that we had from the last profiling session.
I could rerun, but this is just showing me all of the data from the last one.
You can see here in our um do we have any there? Yeah, there's actually nothing there because the update for player panel doesn't run.
Let's let's hit play one more time.
Just look at it again.
Since there's no update method in player panel, it's not even going to show up in the behavior update.
It's completely cleared out of here.
Let's just go click and just double check.
So, all we have now is our player update, which is doing the raycasts, which is totally fine.
All right.
So, I think we're good.
We'll stop playing.
We'll go into plastic SCM.
So, we added events for health changed and bound to the UI.
and we'll check that in.
Now, we're going to take a look at another one of the benefits of events.
Since we'r