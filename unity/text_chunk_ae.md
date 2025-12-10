d.
And then once that script completes, I'm going to add it to my ladybug prefab.
Once we're done with that, I think we could probably move out.
No, there's one more component we want to add, then we'll move out of prefab edit mode.
So, let's go get our ladybug any second now once it finishes compiling and we'll add the ladybug script.
And then the final component that we want to add, I'm going to give you a second to just go ahead and guess and add it yourself.
See if you can think of what component we might add to move our 2D character around.
Go ahead and assume you've got it.
We've added the rigid body 2D component.
So, go ahead and add a rigid body 2D and then back out of prefab edit mode.
And we should have a ladybug that we're ready to start working with.
Now, if I just press play, all I expect to see is maybe it's going to animate, assuming that the animator is turned on and checked.
Let's press play and see if that's the case.
So, any second now, we should get our little ladybug doing his animation.
Let's see.
There it goes.
Loading.
Loading.
Loading.
And our ladybug is animating but not moving.
So, I'm going to stop playing and we're going to adjust the code now so that our ladybug can go left to right or just move off to the side and then maybe turn around when it hits something.
First though, let's get a hold of a couple components.
We're going to need to use the collider component here.
We're going to need to reference the rigid body component, and we're also going to need to reference the sprite renderer component because we're going to want to be able to flip that sprite over.
So I'm going to delete the start method and add in an awake.
Inside the awake, we'll get the sprite renderer.
So we'll call sprite renderer equals get component sprite renderer and then generate a field for it.
It's giving me the first field.
Then I'll duplicate that and let's add in one for our collider.
So say underscore collider.
And here we're going to get a collider 2D.
Now, we could get a capsule collider 2D, but I want to make this code be a little bit more um extens not really extensible, but a little bit more versatile.
So, if I decide to change the collider type to a box collider or circle collider, that this code will still work.
And since the capsule collider 2D inherits from the collider 2D class, we can assign a capsule collider here and get that component just by calling collider or using collider 2D instead of using the very specific type of 2D collider.
Now generate a field for that.
Just give me a collider 2D up here.
And then the final thing that we want to get is one for the rigid body.
So I'll say underscore rigid body equals.
And again, we need to get a component, but we need to make sure very that we're very careful to get the 2D rigid body component, not a regular 3D component because the 3D one won't exist, just the 2D.
We need to add a field for that as well.
Now, we've got all three of our fields.
I'm going to delete all of these private keywords by holding Alt, clicking, and dragging over them, and then hitting delete twice.
That's the box delete or box select.
And that's one of the things I love to do when I have a lot of privates or a lot of stuff that I just need to delete out all at once or modify all at once.
I'll get rid of this private keyword here as well.
And then we'll go down into our update method.
In our update method, I want our ladybug to just move in its current direction.
So, it's either going to go left or right and then turn around if it bumps into something.
So, we'll just say that our rigid body velocity is going to be equal to our direction and then maybe times some speed.
So, we'll say times a speed variable.
Now, we don't have a direction or a speed.
So, we're going to go up here and create both of those.
First, we'll create a direction.
This is going to be a vector 2, 2, 2, which will be our direction that we're going, which is really just going to be for left and right, but we could use the x and y if we or the y if we needed to maybe to go up and down.
And then we're going to add in a serialized field for the speed.
So serialized field here that's going to be a float named underscore speed.
And we'll default it at one.
Now, if we just run with this code, it's obviously not going to move because our direction isn't set.
We've got a 0 0 for our direction.
And so our velocity would always be 0 time some speed.
So what we want to give it is some default direction.
And the one that I want to use cuz my ladybugs are going left.
In fact, most of my enemies are probably going to go left is vector 2.
So I'll set it to equal be or be equal to vector 2.
So now it should move off to the left indefinitely.
But I do want it to stop when it hits something.
Let's go just double check that it moves off indefinitely.
And then we can add in the code to check for things off to the side so that it can turn around.
So we'll go back into Unity and we'll play and we should expect to see our our little ladybug guy just go right off the edge and actually kind of keep floating off the edge.
Let's see if that's the case.
So, ladybug goes and walks and just kind of hovers off the edge spinning in circles.
So, let's fix that up real quick.
First, we'll go to the ladybug and we're going to make it so that our ladybug doesn't rotate on its own.
We'll go to the ladybug's rigid body 2D component and check the freeze rotation Z so that it can't rotate on its own.
Next, we're going to go into the ladybug script.
And in the part where we're setting the velocity, what we really want to do is set the horizontal velocity, not the vertical velocity.
If we're falling down, we want to keep falling.
And if something's launching us up, we probably want to keep going upward.
So instead of setting it to equal the direction time speed, we're going to make it equal to a new vector 2 where the x value is equal to the direction.x* speed.
And the y value is going to be our rigid body velocity.
I so that we're not overriding or changing that Yvalue.
We're just going to keep the Yvalue and modify the X.
That should stop our character or our ladybug from falling oddly and make them just kind of fall right down into the lava.
Let's see if that's the case.
So, we'll play and watch.
I expect this ladybug to just drop right down into the lava and then not die because it's not set up to die yet.
Let's see if that's true.
Any second now, as soon as it finishes reloading and we'll run over here, watch that little ladybug go right down onto the lava.
All right, let's stop playing, go into plastic, and commit our initial ladybug and get ready for making our ladybug turn around in the next section.
So, so we've added ladybug that walks into lava and commit.
Now, we're going to make our ladybug a little more intelligent.
First, we're going to make it look for targets or collisions or things in front of it that are blocking it so that it can turn around.
If it hits a wall or hits a block or something, I don't want it to keep going.
So, to do that, we're going to add some raycasts to our ladybug script.
Well, really, we just need to add a single ray cast to it that's going in the forward direction.
So, we'll open up the script.
And before we set our rigid body velocity, let's add a few lines.
And let's first figure out where we want to shoot a ray from on our character.
Let's go take a look at our ladybug right now.
So, on our ladybug, we want to shoot a ray out right from the eyeballs or right from kind of the front or the edge of this collider is even fine.
Like right here.
If we if this thing touches at all, we can probably turn around.
We don't need to go all the way up and bump.
So, I want to figure out what the point is right about here.
And to do that, we can use the collider.
I'm going to go back into the ladybug script, and we're going to create a vector 2 for our origin.
We'll say vector 2 origin.
This is going to be the origin or the starting point of our raycast.
And it's going to be equal to our transform position plus and then we want an offset in our direction.
But we want it to be the direction um times the colliders bounds extents.
But let's actually do that on a new line up above because I think that'll make it even more explicit and more obvious what we're doing.
I'm going to call this a vector 2 named offset.
and we'll use we'll assign it to our direction which is going to be either negative -1 on the x or positive one on the x and we're going to multiply that by our bounds of our collider or the extents of our bounds of our collider.
So say colliderbounds.extense and um oh yeah we want the x.
So we want that far that width off to the x times our direction.
So that's going to give us an offset either positive or negative equal to the extents.
And if you look at extents in the Unity documentation, you'll see that it's always equal to half the size of the bounds.
And this is essentially going to give us the distance from the center of our collider to the edge of our collider.
If we get the extents dox value, that's what it's giving us.
So that's why we're able to get that exact left edge.
Now that I've got that, we can you add that to our transform position to get our origin.
And we've now got a point right on the edge, except that it's giving us an error here because it doesn't want to combine a vector 2 and a vector 3.
So just like before, we're going to cast our position as a vector 2.
Now we've got a origin that should work perfectly fine and it's offset.
So we need to now add our code for the raycast.
For our raycast, we have two different options.
We can do a raycast that finds one object.
Well, there are actually a couple options, but we can do a raycast that returns one object, or we can do a raycast that returns multiple objects.
And there are ways to do multiple object ones that are even more efficient, and we'll talk about those in a little while.
But what we want to do here is actually scan or search for more than one item.
And the reason for that is that when we do the raycast, there's a good chance that we're just going to catch our own ladybug in that raycast.
We might, you know, even if we're right on the edge, we still might end up colliding with ourselves.
It it happens a lot.
It's not going to happen consistently.
And we could, of course, move this off to the edge.
But I think that getting a raycast of everything and then just ignoring ourselves is a slightly easier and cleaner solution.
And it shows you how this stuff works without having to get really tweaky with your exact variables and sliding out, you know, one 0001 further so that you avoid a collider.
So what we're going to use is the physics 2D raycast all method.
So let's scroll down a little bit and we'll say var hits equals physics 2D.cast all.
all.
all.
Now, we need to give it an origin, which we've already created.
An origin.
Origin.
There we go.
Look at that.
I spelled it right.
Then, we need to give it a direction, which we already have.
And then finally, we need to give it a distance.
So, let's call this the raycast distance.
We need to add that as a variable, though.
So, we'll add a serialized field for it.
So, generate a field.
I'll hit F12.
And we'll go up and replace the private with a serialized field attribute.
Let's go fix that s and then cut it.
So shift delete and move it right up here to by our speed.
I'm going to give this a default value of maybe like 0.2.
It's like 2/10enth of a meter out.
A little bit further than one/10enth of a meter out.
And then we've got our hits.
Now we should be able to get back a list or a collection or really it's an array of raycast hit 2D objects.
And then we'll loop through all of those and see if any of them are not our own ladybug.
So to loop through each of our raycast hits, since it returns back an array, and you can tell it's an array there, by the way, because of the two little braces right after the raycast hit 2D, the square braces say, "Hey, this is an array." And raycast all needs to return back an array.
There are also versions of it where you pass in a parameter and that gets filled.
We'll talk about those later, but for now, we're going to loop through each hit.
We'll do that with a for each loop.
So you just type for each var hit in hits.
This is going to loop over or iterate over every single hit in our array and then allow us to run some code on it.
So, I'm going to hit enter, add some braces, and then figure out what that code is.
The code that I want to do here is really to check to see if the thing that it hit was myself.
If it wasn't myself, then I want to flip my character around and just switch the direction and maybe flip that sprite.
So we'll say if hit.c collider is not equal to null and hit.c collider is not orgame object let's get the game object is not equal to our own game object.
Now we could also theoretically compare the collider.
So we could say if hit collider is not equal to the collider that we've cached here.
That would work as well.
Unless I end up adding multiple colliders to my my ladybug, then we'll run into a problem.
So, I'm going to compare the game objects instead of the colliders, and then we'll just run some code.
If I've hit something that's not me, and that code is going to flip the direction.
And to flip a direction or flip a vector 2, all we have to do is multiply it by negative 1.
So, we'll say direction or underscore direction equals, which is going to multiply it by the value after it, and we'll put in a negative 1.
So if it was 1 and 0, it'll become negative 1 0.
If it was negative 1 and 0, it'll become positive 1 and 0.
Zero is that y value.
The x is what's really flipping here.
The next thing that we need to do is flip the sprite renderer.
So we'll say underscore sprite renderer.
If I can spell that right.
Flip x.
And we want to set it to true if our direction is right.
Because our ladybug is facing to the left by default on that sprite.
We want to flip it over if our ladybug's direction is right.
So we'll say it's true equal or if direction is equal to vector 2.ight.
Oh, I got one extra equals there.
So we're assigning it and then doing a comparison.
A double equals there.
That was the error that just disappeared.
So that should do it.
Now if this happens and I find something that's not me, I want to break out of this loop.
I don't want to do this multiple times if maybe I find two colliders there.
So, we'll just add a break.
What that'll do is if this ever we'll loop through each hit.
Any hit that actually meets the condition that's not us, we'll flip it around, change the sprite, and then break out of the loop so that we don't continue on and try to find another hit.
Let's save that and go test it out.
We should now be able to watch our ladybug go back and forth as long as it's hitting something.
Although, right now, our ladybug is going to walk off to the edge.
So, I probably need to add another block over there to the edge to stop him.
Let's do that before we hit play.
We'll load it in.
I'm going to grab one of these bricks, duplicate it, and hold control and just drag it right over.
We'll save.
Press play.
And let's see if our ladybug will do its walking back and forth.
Come on, little ladybug.
All right, there it goes.
And it's walking around.
It's getting pretty close to the edge and stopping when it gets about 0 2 m out.
And I can of course turn this down to like a 0.1.
Let it get a little bit closer.
And um I can turn this up to something like a one and make it turn away much earlier so that it keeps about a meter away from things.
So it seems to be working.
I'm going to put that back to a 0.1.
adjust the speed just to make sure that that's working too.
Looks like a value of two works fine or a value of 0.5 might work as well.
Have a nice slowm moving snail.
But now that I've got my snail moving and turning around on walls, I want to commit it before I worry about making it turn around on cliffs.
So, let's go into plastic.
Make sure that we're saved up and say that ladybug turns around when hitting a wall.
And if you're running into an issue with it, you're having a problem with it, in the next section, we're going to add gizmos to help debug that a little bit more and make it a little bit more explicit and obvious where our ray is happening.
So just continue on to there and see it and hopefully solve any issues that you have.
Hopefully there are no issues, though.
It should just work.
So let's check that in.
Now, one of my favorite things in Unity is the gizmo setup.
It makes it really easy for me to tell what's going on with my characters and my other objects without having to try to figure it out and hold it all in my head.
So, what we're going to add now to our ladybug are just a few gizmos for the ray casts that it's doing.
Right now, it does a raycast forward, but we're going to need another raycast that goes downward to check for the ground as well.
And I want to make that all visualized.
And if you've run into any issues in the last section, should also help you see exactly what's going on with your ladybug.
So, let's open up our ladybug script and we're going to add an ondraw gizmos.
I'm going to do this right after awake.
I'm going to get rid of this update comment because I already know that updates called once per frame and I'll put in an ondraw gizmos.
Now, I'm going to delete that private keyword and then we're going to draw a ray or a line for our raycast.
So, I'm going to get this line this code here for our offset and our origin and I'm going to copy it into ondraw gizmos.
Then right below it, we'll do a gizmos.draw a line which will be essentially like drawing array.
It's going to give us our origin or start at our origin and then it's going to go in some direction or to a destination.
So what we want to do is our origin plus our direction times our raycast distance.
Now my direction got wrong in there.
I got the uppercase thing.
I want to lowerase my underscore direction so that we're actually drawing in the correct direction times our distance.
And now if I save this off, I expect that it's not going to work.
Now there's a good reason for it.
Let's go check it out and see what that reason is.
is.
is.
So we jump into Unity and then when it doesn't work, we'll go look at the error console.
Here it goes.
So we any second now I don't see any lines coming out of here.
Maybe it's just because it's blue or something.
But no, the actual reason is if we look at our console right here, we have an unassigned reference exception.
The variable collider of Ladybug has not been assigned.
And if I double click on it and look at the code, you might be able to figure out why.
Think about this for a moment and see if you know the reason that the collider is null here and not being found in the gizmos.
If you've thought about it, you probably realize that the actual reason for this is that our collider is cached in awake and we can't use this cached reference to it if it's saved off in awake.
So, we've got two options.
We can either move this to on validate so that we save all of these off and serialize those fields and we don't have to grab them in awake or we can just grab this collider at gizmo draw time which will work just as fine.
So, I'm going to copy the get component part right here.
Collider 2D.
Copy it and paste it over the reference to the collider.
This is good enough for now.
And until we get to the point where we've got ridiculous numbers of gizmos drawing, we're never going to notice this get component call.
Changing the way that we serialize this is probably a bigger jump than we need to make right now for there will really be no noticeable performance benefit.
So, we're going to save and come back into Unity and hit clear.
And if it recompiles, we should see it update.
Let, you know, let's go back in and let's change the color of our gizmo first.
Right here on line 29, we'll say gizmos.color equals.
And we could use yellow.
I want to use red because I think that red shows up really well.
So, we'll change the color to red.
Go back into Unity.
Let it recompile.
There we go.
And then we expect to see a laser beam or a gizmo ray just shooting right out of the front.
Let's see.
Come on.
Pop up my little gizmo.
Are my gizmo's off? Oh, there it is.
I just missed it.
I was blind because the ray is right up here.
So, the reason that it's up here, by the way, and if you were curious about that, is that we're using the center or the origin X value of our character to shoot out of instead of the actual kind of center of our sprite or the center of our collider's height.
So, there's the ray.
It just happens to be on a grid line.
If I press play, go into scene view, you should see it moving around.
Let's watch.
Let's see.
There it goes.
And let's watch it in scene view.
Now you can see that red line.
And as soon as the red line touches, it turns around.
So that's our ray that we're using.
And we've got a nice visualization for it.
Now, before we complicate this with our second ray that's going down, let's check in our code that we've added gizmos for our ladybug ray.
added gizmos for lady bug raycast and check that in.
Now let's create the gizmos for our downward raycast.
Then we can see it before we hook it up in our code.
I'm going to start by opening up our ladybug script.
And we're going to use the bounds of our collider this time instead of using our center or well actually we're going to take the bounds and we're going to do a little bit of math with it I should say cuz we are using the bounds already but we're going to use it in a slightly different way.
So first thing I want to do is just cache this collider component because I'm going to be using it in just a moment to get the bounds again.
So I'm going to cut this and replace it with collider and then one line up I'll say var collider equals and then paste.
Now I'll just get it once per gizmo draw instead of multiple times and it'll shorten out my code a little bit.
Now the next thing I want to do I add a little space there is go down here and we're going to get the bounds of that collider.
So we'll say varb bounds equals collider.bounds.
And this is going to give us the positions in world space of all of the edges or the corners of our collider and the center of our collider.
Then we're going to get the bottom left corner of our bounds.
And to do that, we're going to say var bottom.
Let's call it a vector 2.
Let's call it what it is.
Vector 2 bottom left.
And it's going to be equal to a new vector 2.
And the x position is going to be our bounds.
Minus we want the bounds.extense.x.
So this is going to give us a position all the way off to the left for the x.
Then we need to figure out our y position where we'll use the bounds dot set.
I I lied.
I said center.
It's center.x.
We use the bounds.center.y and our y value.
And we'll subtract the bounds.extense.y.
Hey, look at that.
It already knew what I wanted.
So, I'll just let it autocomplete.
That should give me the bottom left corner.
Now, if I wanted the top right corner, I could put plus here and a plus there.
Or if I wanted the bottom right corner, I could hit a plus for the X.
So I get the right hand side and the bottom would be the minus for the Y.
So this is giving me that bottom left corner and I'm going to draw a gizmo in that bottom left corner.
So I'm going to select line 32, copy it, paste it in here, and we'll go from bottom left, paste over origin to bottom left plus vector 2 down times our raycast distance because we don't care about the direction.
Now, this is going to work partially, but it's only going to be good for that bottom left.
Let's go check it out.
When our snail gets to the edge, that ray is still going to be showing on the wrong side or on that left side.
So, let's try that and make sure that that's the case first.
Oh, there we go.
You can see that little red line there.
If I hit play and watch it in scene view, I expect that red line to just stay there on that left of that character.
Let's see.
It is named bottom left.
So, it probably shouldn't be switching until we've renamed it and updated the code at least.
All right, we go into the scene view.
You can watch that ray going along.
Looks good, but it's doing exactly what I expected.
Now, we'll go back into the ladybug.
And what we want to do is determine if we're going to use the bottom left or the bottom right based on the direction.
So, we could actually just multiply this bounds.extense.x times our direction.x.
So that way it'll either be it'll get flipped over to an inverse or negative if we've switched directions.
But I feel like that's probably a little bit confusing.
So instead, what I'm going to do is create a new vector for the bottom right.
And then we'll just use either the bottom left or the bottom right based on our direction.
So if we we've got our bottom left one, I'm going to duplicate that.
We'll add a bottom right.
We'll duplicate, add a new line on our gizmos to draw on the right.
So now we'll draw one on each side when we're doing our gizmos.
But we're only going to do the one that we care about for the direction that we're currently moving.
So I'm going to add some new lines here.
And I'll say if direction is equal to vector 2.
Then we'll run these two the bottom left and the gizmo for that.
Let's cut cut that line and paste it in.
And then we'll say else will run on the bottom right.
So now we've got code that runs for bottom left or bottom right depending on which direction we're going.
Let's go double check that in our code or in our editor.
Make sure that it actually shows the correct gizmo.
And then we can start worrying about how we're going to hook this up to a raycast and check for some ground below.
But that should be probably the easiest part.
I feel like the hardest part is figuring out where these raycasts go and getting them drawn in place.
So let's play.
Watch our ray cast bounce back and forth ideally assuming that nothing went wrong.
Go to scene view and oh our ray is not switching directions.
So we are changing directions but for some reason it's not actually drawing on that that left side direction.
Let's go double check that I actually committed my code or saved my code.
Oh, here's the problem.
I didn't change the code on the bottom right to actually go off to the right.
So, we'll go select that code, change it to be a plus on the extents, and then we'll jump back into Unity and it should do the correct direction.
This is exactly why I wanted to do the gizmos because I feel like it's very easy to accidentally miss a little thing like that and then get stuck forever trying to debug it and not be able to visualize it.
So, the visualization makes a huge difference in speeding that process up.
Any second now, I've got to restart my computer.
got too many things running right now.
So, my compilations are killing me.
But as soon as I hit play, I should expect to see that ladybug switching back and forth with the gizmos shooting out of its face kind of downward down below so that we can do our raycasts.
All right, let's see.
There goes our ladybug.
And look at that.
The gizmo's changing.
We can see it back and forth.
It's looking pretty good.
I think it's time for me to go into plastic and commit that we've added gizmos for downward for our downward ray.
And we're ready to add in that ray next.
Now, let's turn our ray into an actual array or turn our gizmo into array so that we can actually have our ladybug turn around.
and we'll do a little bit of cleaning up and refactoring along the way.
We're gonna open up our ladybug script.
And the first thing I want to do is modify our gizmo code where we're figuring out what bottom corner we want to use.
Let's turn that into a reusable method so that we don't have to copy and paste this code and this direction checking code and all of that.
So, first we'll actually start by just copying and pasting it.
I'm going to copy line 36 through 45.
And then we're going to add a new method right below that returns back a vector 2.
I'm going to name this I think uh what do I want to call it? A get down ray position.
Something like that.
Let's let's go with that.
Get down ray position.
And then we'll paste in our code.
What I want to do here is instead of drawing a gizmo, I just want to return back one of these vector 2s.
So I'm going to delete out both of the gizmo lines here.
And instead of assigning a vector 2 here, I'm just going to replace this with the word return.
So, we'll return back a new vector 2 that's off to the left if our direction is left.
Although, we do have an error here saying that it can't find our bounds.
So, we're going to need to copy line 35 and paste it in here.
and then replace the collider with the underscore collider because here well actually to be honest this is going to be an issue because if we just use the collider here we're going to run into a problem of in the gizmos this may or may not work.
So let's make it so that we can pass in a collider instead.
We'll take a collider here as a parameter and now our error is gone.
Now, the last thing we need to do to get rid of our error is make sure that we return something even or in all of our paths.
Right now, it's saying that not all code paths return a value.
That's because if it's left, we return a new vector 2.
If it's right, right now, we assign a variable.
That's not what we want.
We want to return that right variable or that right offset.
Now, I don't need these braces here because there's only one thing happening in each of these lines.
So, I'm going to delete the brace.
Delete the braces.
just shift delete to get rid of them all.
Now I've got a ray position method that'll give me back array position and I want to use it in my gizmos first.
So I'll copy get down ray position and I'll just put that oh let's put it right here.
I'll say var down offset or down origin.
Let's call it down origin equals get ray down ray position and we'll pass in our collider.
I'll delete out this bounds code and delete out everything except for that one gizmosdraw line.
Shift delete.
Shift delete.
Shift delete all the way until I've got it lined up.
And then we'll replace bottom left with down.
Double click paste.
And double click paste with down origin.
Crl Krl D should fix up my formatting.
And now I've got a method that I can use to get that downward ray position.
and it should still draw that downward origin um or that downward ray in my gizmos.
Let's just go double check it in gizmos.
Make sure that it still works, that it's still showing in the right position, that our refactor didn't break something when we extracted that code out into its own method.
And if it is good, then we'll jump back in and we'll finish up with the ray casting.
So, we play, we should expect to see our character do exactly the same thing that it was doing right before, just moving back and forth and changing that uh that ray position from the left to the right, but not actually using that ray yet.
So, let's see.
We'll go into the scene view.
Yep, it's still working fine.
It's getting the position and it's swapping back and forth.
So, let's make the final change in our ladybug, which is going to happen down in our update.
First, let's add a space here after the get down ray position and update.
I don't like to have no space between methods.
I always like to have one space, exactly one space actually, between each method.
So, in our update method, before we check to see if we've hit something off to the right or we've hit something off to the left, let's make sure that there's actually ground in front of us to continue walking.
So, we're going to add a couple new lines here.
And first, we're going to just add in a boolean variable for whether or not we can continue walking.
We'll say bull can continue walking equals false.
And if we don't find any ground in front of us, we'll never set that to true.
And we'll just return.
So let's uh say if we can't continue walking, if can continue walking is equal to false, then what do we want to do? Well, we want to switch directions.
Let's copy all of this line 66 through 68.
We want to switch directions, flip the sprite render, and we don't want to break because we're not in a loop, but that's not what we're trying to do.
Instead, we just want to return.
So, how do we set can continue walking to true? Well, we're going to need to do array cast next.
So, we'll do that just like we did down here on line 63, but we'll do it on what is this 55.
We'll say var down hits.
This is going to be our downward hits equals physics 2D.cast ray cast all and we'll give it our downward origin which is going to be calculated from our get down ray position.
So I can pass in get down ray position and give it our collider as the first parameter.
And then for the second parameter we'll give it a vector 2down.
Oh, I need to add the underscore to our collider.
That's why we've got an error here.
And then finally, we'll give it a distance, which is our raycast distance.
Now, personally, I like to split this method out and give it another parameter or another variable here.
So, it's a little bit more explicit and just spells out what we're doing here.
And I'll do that by taking this get down ray position and just cutting it onto my clipboard, adding a new line, and say var down origin equals and paste.
Then I'll put down origin here just so that it's a little bit more explicit.
Again, works exactly the same, but I like to see the variables here.
I can debug it a little bit better and understand what's going on a little bit better.
Now that I've got my down hits, we need to loop through them just like we did before.
So, say for each var hit in down hits.
And we can't name this hits, by the way.
It has to have a unique name so that it's not um redefined down here.
We could, but we'd have to remove this var part.
And I like to use a separate name because I think it makes it a little bit clearer and cleaner understanding what we're doing.
So, we're going to loop through each hit and we're going to do the exact same check here.
If the hit collider is not null and it's not our game object, so I'll copy line 72 and paste it.
If it is not null and it is not our game object, then we can continue walking.
So, can continue walking will get set to true.
Otherwise, we'll just uh not ever set it to true and we won't be able to continue walking.
This should do it.
This is enough to get us walking.
Let's go test it out.
We'll jump over here.
Go find our ladybug again.
And what we're going to want to do is turn this block off so that the block isn't there blocking it.
Or the block isn't there stopping the ladybug from walking over.
Let's go find that brick, uncheck it, press play, and let's watch.
Our ladybug should now walk to one edge, turn all the way around, bump into something, and turn around again.
Let's see if that's the case.
All right, it's loading up.
There goes our ladybug walking over to the edge and turning around.
Let's go.
Let's go break these bricks, too.
So, it's going to turn around until it runs out of bricks.
And then it should walk all the way to the edge.
There's nothing going on with the laser to interact with it.
Right now, the raycast stops on it and ends there.
And our laser blaster doesn't have a collider in it, so it should just walk right through over to the edge and then turn around.
It's looking pretty good.
And I think if I turn the um if I adjust that platform a little bit so that it's slower, we can still kind of bug him out so that he'll walk on it and fall off because he won't stick to the platform yet.
But so far, I think this is working pretty well.
So, I'm going to go into plastic and commit that our ladybug now um walks doesn't fall off of ledges or doesn't walk off of ledges.
So, I'll save my scene.
The ladybug no longer walks off edges.
and check it in.
Now, we're going to make our ladybug interact with the laser.
Currently, the laser just shines onto the ladybug and doesn't do anything to them.
So, let's make a little modification to the laser script so that it can stop a ladybug in its tracks and then talk about how we can abstract that out a little bit.
Let's go into the laser script.
And in our laser script right now, we look to see if we've hit a brick.
And if we have, we tell it to take damage.
Let's add in some code to also hit a ladybug.
We'll copy lines 36 through 38 and paste them down below.
And I'm going to replace brick with ladybug.
We'll copy ladybug over the three other instances, including the type here.
So, lady, I got to spell it out here.
Bug bug with a lowercase B.
This one needs to be that capital because it's the actual type.
Now, we've got an error here.
It says that ladybug doesn't take laser damage.
There's no method on it.
So, we're going to need to add one to take laser damage.
I'm going to hit alt enter and just generate a method.
We'll hit F12 and go into that method.
And I'm thinking for the ladybug, instead of killing it like the um bricks die, I want to make it just freeze the ladybug.
So, if it hits the ladybug, the ladybug just doesn't move until the laser's off.
It just keeps them totally still.
And obviously, we could easily just change it to do death or something else.
But for now, I'm going to say rigid body.locity equals vector 2.0.
I'm going to replace internal with public and then save this off.
Now, my expectation here is that once the laser hits the ladybug, the ladybug should just stop working.
Though, I don't particularly like the code.
And we're going to talk about why that is and talk about how we can improve it in a moment.
First though, let's just play and make sure that this is the case, that the ladybug actually stops when it gets hit hit with the laser.
So, as soon as we finish reloading, we'll play, we'll run over, turn on that laser, and then make sure that it's updating or I said updating, but really it's freezing, right? All right.
Any second now, it should load up.
and we'll go flip on that switch.
So, our ladybug should be walking back and forth.
Turn the switch on.
I'm going to kind of jump over here and watch.
And look at that.
Every time it hits the ladybug, the ladybug freezes.
So, it is working.
It's doing the expected thing.
But we have a problem here, or at least what I would perceive as a problem, and that's that every time we want to add something new to our laser, we're going to be copying and pasting this code, adding a take laser damage or maybe some other type of method to this thing so that we can make it deal with laser damage.
And I don't particularly like that.
I don't want our laser to need to be updated every single time we add something else that needs to take damage from our laser.
We shouldn't have to go back in and modify it every time.
This is part of that open closed principle that our class should be open for extension but closed for modification.
Really meaning that if we add new things that interact with and use it, we shouldn't necessarily have to go in and change this class.
Now, there might be scenarios where we've done so much where we change it so drastically that we we just have to.
But most of the time, we can avoid this.
And we can avoid this by using one of two things.
Either abstract classes or interfaces.
And in this scenario, an interface is probably the perfect option.
So, we've got this take laser damage method, and both our brick and our ladybug can both implement it.
They implement it totally differently.
And really, all our laser cares about is that the thing that it's hitting can take laser damage.
So, what we're going to do is add an interface that's common and shared between our brick, ladybug, and anything else that needs to take laser damage called I take laser damage.
then we can add that on and simplify this code here.
So to do that, we're going to go into our ladybug first and we could do the extract interface option.
So if I hit alt enter, I can hit extract interface and I can choose the members that I want to have here.
There's the I or the take laser damage is the only public method that we have.
So that's the only option available.
And the default name for it is I ladybug because it's going to put an I for an interface and the default or the existing class name.
I want this to be a take laser damage interface though.
So I'm going to make it a little bit more generic by putting I take laser damage here.
I'll hit enter and that's going to generate a new public interface named I take laser damage with a void take laser damage method.
Notice that it doesn't say public here.
That's because everything in an interface is going to be public by default instead of private by default because that's the way interfaces are made to be the publicly facing interface for this type of thing or this type of object.
So now that I have this I take laser damage, let's go back into our laser and instead of calling it our code on a ladybug, let's replace this with I take laser damage.
Now, I'm going to replace the word ladybug with damageable or let's say uh laser damageable.
And then we need to also add something on line 40 because we're using an interface now and not a class, not a specific mono behavior or something that is definitely a class.
When we do our null check here, we can't just check it like this.
We have to actually say if it is not equal to null instead of if it's true.
And that's just because of the way that it does the overloading of that if statement.
If you just pass in an object, it will return true if that object exists or and false if that object is null or doesn't exist.
But with an interface, that's not the case.
We actually need to do the check there.
The overload doesn't exist like that.
So, we'll save.
And now I've got a take laser damage method on a laser damageable.
But I still have this brick one here.
And I want to get rid of the brick part, too.
So, I'm going to select lines 38 through 36 and just delete them.
But now, my bricks aren't going to take laser damage.
And that's because they don't implement the I take laser damage interface.
But I can make change that.
I can make it so that they do just by copying the interface name.
I'm going to save so I can get rid of that star.
Go over to our brick and right after the mono behavior, we're going to add a comma and add in our interface.
You may have noticed that on the ladybug that happened automatically.
And what what this is is telling us that this is a mono behavior as its class, but it implements this I take laser damage interface.
And you might notice in some other code that you write that you can actually have multiple interfaces.
I could have an I take laser damage, I take hits from above or whatever other type of interface that I want to add.
I that doesn't exist right now.
So I'm going to delete it out and save off our ladybug.
Now that we've got our ladybug and our brick both taking laser damage or implementing this method or this interface, we should be able to run into Unity and have it work.
Now, this only works because this method existed and had the exact same name.
If this was named like brick take laser damage, then we're going to get an error here.
The interface is going to say, "Hey, brick does not implement the interface member take laser damage because I renamed it to brick take laser damage." And then I would have to hit alt enter implement the interface down here and then go put in the code for the method.
I don't need to do that though because I've already implemented it.
I just renamed it and broke the name.
If I remove that brick word again, just put it back to take laser damage and that name matches the method in here.
It should work.
Let's jump into Unity, go play, and see that we get the exact same behavior but with a little bit less code.
And then we now have an interface that we can start adding on to other things that we want to deal with lasers.
If we got something that we want to warm up or move or other things that we want to just die or blow up, we can just add that interface and then have them deal with the code however the specific object wants to.
So, let's go try it out.
We run over here.
We should be able to turn that on.
Watch it go.
Seems like it works.
The bricks blew up and the snail stopped in its tracks.
Let's go into plastic SCM and make sure that we've saved our sandbox scene and say that we added the I take laser damage interface and we'll check that in.
It's time for another challenge.
I want you to try using some of the things that we've already learned to add in a new visualization for our laser.
Right now, our laser just kind of ends at the thing that it lands on.
And I'd like to modify that.
So, if we go to the laser folder, you should see some laser blast.
What is this called? Laser yellow burst.
And I'd like you to implement a laser burst that shows up at the edge of the sprite.
So, it shows up right where the laser is hitting and then pulses and gets bigger and smaller.
So, go ahead and try to do that on your own.
Whenever you're done or ready, just continue on and I'll run you through the steps and show you the the easiest, simplest solution that'll work and get this done for you.
But I want you to give it a try on your own first.
See if you can figure it out and then continue on.
So go ahead and now I'll assume that you've either done it or decided not to.
So we're going to rightclick on our laser and we're going to add in a new game object.
I want a new sprite that's going to be a child.
I'll just use a square and I should get a big fat square there.
I'll drag the laser yellow right here.
This little laser yellow burst into there.
And then I'm going to just drag it over to the side so I can see what it looks like.
If I drag it right to this position, I can tell that it's behind the sprite renderer because my sorting layer is not set.
I want to put this on props.
And I'll just set the order and layer up to a one so that it's up above my laser beam.
Now, this will work fine as long as my laser beam doesn't move, but my laser beam is definitely going to move.
So, I need to modify the code so that it can move this object to wherever I've hit my laser point.
So, let's rename this object to laser burst.
And then let's open up the laser script.
We'll give ourselves a reference to that laser burst.
So, we'll add a serialized field that's a sprite renderer.
And we'll call this laser burst laser burst.
And then I'm going to copy that laser burst.
And down in our code where we set the end point, let's just set the position of this laser burst to be exactly at that end point.
So I'll say laser burst.t transansform.position equals end point.
This should move that laser burst directly to where we want it to be whenever it's whenever it hits something.
I do want to however turn the laser burst off if our laser is not on.
So I'm going to expand out our is on code.
add some braces and before the return I'll paste in laser burst and putten enabled equals false and then down here where we set the laser burst position I will say laser burst enabled equals true.
So we'll turn it on if we've got a valid position and we'll turn it off if we don't have a valid position.
Now if we don't hit anything it's really up to you to decide.
Do you want to leave the laser burst sitting on the laser or do you want to get rid of it? If you want to get rid of it, you could just copy this line here, add an else statement, and paste it in and replace the true with false.
Now, we won't get a laser burst until it actually hits something.
Let's save, check that out, make sure that it works, and then figure out the pulsing part next.
So, we'll go in, we'll press play.
Oh, we've got to assign the laser burst before we press play, though.
Otherwise, we're just going to get a null reference exception.
So, as soon as it's done compiling, we'll drag the laser burst onto that laser burst field.
That's going to be this child right here.
And then we'll press play and watch that burst end up at our end point.
So, any second now, we'll take that.
Oops, I just clicked off the object.
Let's go click my laser again and then drag that laser burst down.
I'm going to save my scene just to make sure that I don't forget to save before I do any committing.
And press play.
And my laser burst should now appear at the end of the beam.
Well, right now it's kind of it's cheated because I moved it into that position beforehand, but whenever it starts playing and we actually see the laser beam going out, we should see that burst matching up with the end point.
All right, we're entering play mode and we'll run on over.
And that burst is showing up there.
If I get out of here, I can see that.
Yep, it goes to whatever thing it's supposed to land on.
Now, let's stop playing and add in the code so that it can pulsate.
I want this thing to get bigger and smaller over time so that it kind of feels a little bit more alive.
To do that, we're just going to modify the transform scale.
And we can do that right here on line 42.
We'll say laser burst.transform.local scale.
And we want to set it to vector 2.1 or vector 3.1 really times some variable.
And remember when we used the math f.ping pong and time dot time.
We can do the same here.
So we're going to set it equal to vector 3.1 times.
And here we'll do math f.pingpong just like we did before.
and we'll give it time dot time as the first parameter and 1F so that it goes between zero and one over a 1 second period.
Now if I just do this I'm going to get a variable laser blast that goes all the way down to 0000 which is going to cause some problems and then back up to one.
Instead of that though I want it to be slightly different.
I want to go from 0.5 to 1.5.
So, I'm going to add some parentheses here and I'll say 0.5 plus our math f.ping pong.
Oh, I think I need to add an f right here.
Be a little bit more explicit that it's a float so that I can add my float to the floating value from the ping pong.
So, this is going to give me a value from 0.5 at the smallest to 1.5 at the largest and it's going to go over one second with that iteration or that looping.
Let's try it out.
out.
out.
Hopefully, you were able to remember and use the math f.ping ping pong when you were trying to figure this out.
By the way, that's one of the key things that I want to make sure that you remember these things exist.
And remember that it's a lot easier most of the time.
We don't necessarily need to add an animation and an animator or do a bunch of crazy code.
A lot of the time we can just do a simple oneliner like this to modify things over time and do these cool little visualizations.
So, let's play.
Make sure that our laser is pulsing and then once we're good with that, we can check it in.
All right, let's see.
Here it goes starting up.
And again, my startup times are slightly slow right now because I'm copying a million files off my hard drive and just beating up my system while I record so that I don't keep running out of space while I'm recording.
All right, we press play play play and the laser is off.
So, we'll turn it on.
And look at that.
The laser is growing.
It's pulsing.
And I think that that looks pretty freaking cool.
So, let's go into plastic and make sure that we've saved our scene and say laser has or we'll say that we added laser burst to the laser beam and we'll check that in.
Now, we're going to make our ladybug both deadly and useful.
I want to make it so that our player can bounce on the top of the ladybug to get to different places, but also make it so that there's some danger if they touch the ladybug from the front or the back.
The easiest way to add in some damage would be to just add our spike script that we've already created that damages anything that touches that component.
So, let's go add a spike script right now.
Let's go double check what that spike script does so we can remember.
And just look here that we look for an on collision enter.
And if we hit a player, then we tell that player to take damage and we give it the normal so that it can bounce back.
So, let's go back into Unity now.
Now, if we play and try this out, we should expect to see that the ladybug doesn't actually run up and touch us because it's doing that ray cast.
It's finding us and turning itself around.
Now, I can still land on it and take damage, which not what I want to happen yet.
And I can kind of run up behind it and take damage.
So, it is dealing damage, but it's not dealing damage by walking into me.
So, I want to modify the ladybugs ladybug script just a little bit so that it will ignore my player when it's determining if it should turn around.
To do that, we'll stop playing and open up the ladybug script.
And then in the part where we check to see if we've found anything in front of us, which is down here, we want to do an extra check to see if the thing is on the player's layer or if the thing is is a player.
We have multiple ways to do that.
First though, I want to reorganize this code just a little bit.
Let's take the code for can continue walking, the part that's checking the ground in front of us to see if the ground exists in front of us.
And let's just select all of that and move it out into its own method.
So I'm going to take everything from 55 down to 69 which is from the part where we initially get our can continue walking our two downward variables or vectors or this is a vector and that's our raycast hit array.
So we've got our down origin and our down hits our loop and then our check here.
So let's take all of that and hit alt enter and oh looks like extract method's not popping up.
So what I'll do instead is settl x and then we'll write the name of a method and I'm thinking that we'll call this check ground in front.
We'll add the semicolon at in the two parenthesis.
Then I'll hit alt enter and generate the method.
Inside of that method I'll paste over this throw exception all of my code.
This should work exactly the same.
But now my update method is a little bit easier to understand.
I can see that in update I get some vectors.
Then I check the ground and then I do some stuff with those vectors.
So next I want to rearrange this a little bit.
Let's move the check ground in front up.
So I hit control X and move it to the beginning of my update because these two variables aren't used by that and they're not used until we get down to this code that's checking for things that are in front of me.
Next, I'll get rid of these extra spaces and I'm going to take this code that checks for things in front of me and let's extract that out as well.
So I'll select it all.
See if alt enter pops up.
Ah, there we go.
The extract method option is now available.
I'll hit enter there.
And we'll call this check in.
Oh, do I want to call this check in front? Yeah, let's call it check in front.
And then I think we're good.
I like that.
So I've liked this little refactor where both of our methods exist and the code is a little bit easier for me to understand.
And now in my check in front, I have to decide how I want to determine if the thing is a player.
I've got again two options.
I could check right here to see if the player has a or if the collider has a player component on it and if so just not do this code or I could add a layer mask here so that I can ignore specific layers and make it um just continue walking into those layers.
I'm kind of torn on it because really it's about the same either way, but performance-wise, it's a little bit better for me to do the layer mask check.
So, that's what we'll go with.
And to do that, we're going to add a new parameter to our raycast all.
So, when we do our physics 2D raycast all in that forward direction, our fourth parameter will be a let's call this a forward raycast layer mask.
So, we'll have a forward raycast layer mask and we'll hit alt enter and then we're going to generate a field for it.
I'll hit F12 and it's going to give me the wrong type.
It always does this when you generate a layer mask.
Instead of giving a layer mask, it gives an int, but we can just replace this with layer mask and then replace the private keyword with the serialized field attribute.
Now, I'm going to move this up.
So, select the whole line, hit controlX or shiftde, and then move it right up here below my raycast distance.
I'll save that off.
Let's go back into Unity.
Well, first let's do a build.
Control shiftB and make sure that the build works.
Oh, looks like Oh, weird.
Somehow I got an extra weird using statement up here.
I'm going to go hit shift delete.
And I'm going to hit shift delete on all these extra using statements that I've got up there, too.
Not sure what added that.
Something in Visual Studio must have gotten confused.
We'll do another build.
Make sure that it succeeds.
There are no errors, no missing braces or anything.
Then we'll jump back into Unity and let's go check out our ladybug script.
We should now have that layer mask.
And if I press play, it's going to do something a little bit strange.
Let's watch.
So, there goes my ladybug.
And it's walking, walking, walking.
And when it gets to that brick, it's just going to keep going and keep trying to push the brick and not not stop.
So, we're going to change the layer mask to be everything.
That'll make it turn around, and that'll also make it, of course, turn around when it gets to the player.
And then if I change that layer mask to not have the player on it.
Bam.
Bam.
Look at that.
The player is starting to take some damage.
All right, that is closer to what I was looking for.
Let's let our player die.
We'll stop playing.
I'm going to go back to that ladybug.
I'm going to adjust that layer mask while we're not playing.
Unset the player so that it's mixed with everything except for the player.
And then I'm going to go to the overrides and apply all so that our changes get applied.
Next, we'll go into plastic and say that our ladybug turns around with the forward raycast layer mask and deals damage to players or ladybug deals I think deals damage to players is probably enough.
And I'll check that in.
Oh, I haven't checked in saved my scene.
So, we'll save our scene and we'll make one more checkin.
say added sandbox scene from previous commit and we'll check that in as well.
Now let's stop this bug from damaging us on the top and do a little bit more refactoring and renaming.
We're going to go to the ladybug script and find the spikes script.
And the first thing I want to do is write the code so that we don't take damage if we hit it from above.
We've done this a few times already using that dot product.
And I'd love for you to go ahead and try to do it yourself.
Give yourself a few minutes.
See if you can write the code to ignore hits from the top.
It should be about three lines of code.
And then when you're done, go ahead and continue on.
Or if you just want, go ahead and continue on as well.
All right.
So to do this, what we'll need to do, assuming you haven't done it already, is add a serialized field with a boolean for ignore hit or let's say ignore from top, not from, from top.
So we've got a boolean there that we'll just check against.
So I'll add in an extra space here.
And then in our on collision enter, we'll check to see if that ignore from top is set.
And if so, we'll check to see if um well I if we hit from the top.
So we'll say if ignore from top and then we want to check the vector 2 dotproduct of our collisions normal which is that collision contacts zero.
And this is again an array of different contacts.
If we somehow have a collision where we have two things touching at the exact same frame or maybe we're in an on collision stay where that's more likely where we have two different points touching we'll have more than one contact but most of the time we'll have one contact at index zero.
So we've got contacts 0normal which is going to give us the direction of that contact or the direction of that collision.
The dotproduct will then compare that to vector 2 down.
So we'll compare the direction that we hit to the downward direction.
And if those exactly match, we'll get a value of one.
If those are exact opposites, we'll get a value of negative 1.
And then we'll get a value somewhere in between if they're not matching.
So zero would be completely perpendicular.
So what we can just check to see is if it's greater than maybe like a 0.5.
That way if we hit it on the edge pretty good, we don't hit it directly top on, we'll still bounce or we'll still not take damage.
Um, so if we've hit it somewhere from the top like that, we'll add in a closing parenthesy that lines up with that closing parenthesy.
Then we'll return.
That's it.
That's all we need.
That should prevent us from taking damage.
Let's go see.
So, we'll jump back over here.
We'll turn that option on for the spikes on the ladybug.
And we'll press play.
And I should be able to walk up to him, take some damage, and then jump on top of them and not take damage.
In fact, let's just jump on him first.
No damage.
And then if I let him walk up to me, ooh, take some damage.
But if I land on him, he's pretty safe.
So, it is working.
That's exactly the behavior that I want.
But now I've got an issue that I really don't like the way that this code looks.
This right now has a ladybug with a spikes script on it.
And the spikes were intended to be those spike objects that obviously completely take hits from the top.
So, having this thing be named spikes and be reused against on multiple objects.
I've got it on my ladybug.
I've got it on, I think, on my frog and I've got it on my um my actual spikes and I think even on is it on the the lava, too.
There's a lot of things.
So, I'd like to change this.
Now, I'd like to rename our spike script to be something that makes a little bit more sense for what it is.
And I want to do that without completely breaking my project.
So, the first thing that I need to do, well, let's save my scene and then go find my spike script.
So, I'm going to click on it and select it.
Go right over here, find the file, and rename this by hitting F2.
Got it selected.
There we go.
F2 or a single click should do it.
And I'm going to rename this to damage player.
Now, that's not going to do it alone because now my script is named damage player in the file, but the class is named spikes.
it opened up in the code editor to show me that.
But I if you didn't open up your code editor, just double click that damage player file and it should open up.
And if it still doesn't open up, you can always go to assets and then look for the open C project and that should force it to reload and hopefully find your project or go over to the solution explorer which is right here on mine and then find it in your list.
Once you found your damage player script, you need to find the class name right here where it says spikes.
Hit controlr controlr and name this damage player.
Need to match the casing and the name exactly with the file.
Now, if you use um rider, it'll actually automatically do that for you.
If you rename here, it'll rename the file for you.
I don't think Visual Studio does that, though.
If you just go in here and rename the class, it won't just go rename the file automatically.
But either way, we've got it matched up now.
We've got damage player, damage player.
Let's go back into Unity.
Haven't touched anything yet since I've been letting this change.
And I can see that my damage player script is still here.
It looks like it's working.
I'm going to go take a look at one of my other scenes.
Let's go look at level one and make sure that the damage player script is still on the things that I expect to damage the player.
Like uh did my lava have that? I'm trying to remember now.
I believe it did.
Yeah, damage player.
Perfect.
And it should of course not ignore from the top.
And my spikes also have the damage player script.
So now it's looking a lot better.
I think that the script makes a lot more sense.
And the last thing we need to do is make our guy actually bouncy.
But I think we'll do that in the next section.
For now, let's save.
Make sure that our sandbox is saved.
Got our damage player now checked in or ready to move.
Notice that there's a move now in here.
When we rename a C file, or really if you rename any file, it's going to count as a move in your source control instead of a rename.
There isn't usually a rename thing there.
It counts as like moving the file from one path to a new path.
So, we're going to say that we made the spikes into a damage player script and gave it an option to ignore hits from the top and check that in.
Now, let's start bouncing on our ladybug.
We've got a couple options just like always for how we could accomplish this.
We could add that bounciness factor in the material or the physics material like we did with the spring.
Maybe go select the spring material and then have it be somewhat bouncy.
But that's not going to give me the exact behavior that I want because this thing is kind of running up to things and it's going to be bouncing itself.
That's going to make this object bouncy.
And I don't really want this guy to be moving around, bouncing on things or acting bouncy at all.
I just want to be able to bounce when I land right on the top of them.
So, I'm going to undo that change and instead we're going to open up the damage player script.
And then we're going to copy it.
We're going to use this damage player script as a template to create a bounce player script.
So, I'll take all of this code from line 25 up to line six, copy it, and then go down below, hit enter a couple times, and paste.
We'll replace the word damage with bounce cuz that's what I want it to do.
And then, when I think about bouncing a player, I probably want it to bounce from the top only.
I very rarely want to ignore the top.
Instead, I probably want it to have maybe an only from top option or always be only from the top.
But I can see reasons for allowing it to bounce from other sides.
So let's add an only from top instead of an ignore from top.
In fact, let's just rename this to be only from top.
And then we'll have to change the code.
So if we're checking to see that it's only from the top and our vector here is greater than.5, then we're actually doing something incorrect.
We're checking here to see if it's uh only from top.
But then if we are from the top or I can't get my words out here that means that we'll have to reverse this arrow here to check that we're less than.5 so that if we're not from the top and we have the only from top option selected we'll return.
Otherwise we'll do the bounce.
And to do the bounce we can just call a method called bounce on our player.
Let's say player.bounce.
And then we'll pass in the normal.
And let's also give it some bounciness factor.
So, I'm going to call this underscorebounciness.
And then I'll generate a field for my bounciness.
I'm not sure if I spelled that right or not, but it'll work.
I'll add add it here and make it a float.
And then we'll make that a serialized field.
I'm going to give it a default value of something like um let's go with like a 200.
This is going to be an amount of force that's going to get added to the player.
Now, I need to implement this bounce method.
So, I'll go to the bounce right here, select it, and hit alt enter to generate the method.
It's the first option there.
I hit enter again, and my method should be generated.
I can hit F12 to go to it.
And then I just need to implement it.
Now, if you look here, when we take damage to deal with a knockback, right now, we're just adding some force in the opposite of the normal times some knockback velocity.
So, I can just copy this line, paste it right in here on 177, and instead of using the hit normal variable that doesn't exist, I'll use the normal that's passed in.
And then here, we'll use the bounciness instead of the knockback velocity.
That way, the objects that I'm bouncing off of can control how bouncy they are.
Let's make this public.
And then we'll go back into our damage player script.
And the final thing we need to do is move this bounce player script to its own file.
So select the class up here, right on the class name, hit alt enter, and choose move type to bounce player.cs.
That should move it into its own script.
Maybe even open that script up.
If it didn't, you can always go to the solution explorer and go find that script right there.
But we don't even need to do that right now.
We just need to go to the ladybug and add the bounce player component.
So I'm going to collapse everything else.
We'll add the bounce player.
I'll check the only from top option.
And let's press play.
I expect now to be able to run over there and bounce off the top of it.
And then I think we can probably add this to our spring as well if that works.
So there we go.
I can bounce.
The bounce is kind of weak.
So let's try turning that up to about a 400.
Okay, there we go.
I'm getting a nice strong bounce, I think.
Look at that.
I like that quite a bit more.
So I'll stop playing.
I'll set that value back to a 400 while we're not playing.
And then I'm going to go to overrides and hit apply all to update my prefab there.
Next, I want to go modify my spring so that my spring uses this bounce player script as well.
That way, my spring won't knock me back.
Let's go find the prefab for our spring and just drag it right out here.
Let's put it just somewhere over here to the right.
I'm going to put this at a negative -3.5 and oh, a seven.
I'll save my scene.
I'm going to press play.
Use the spring as it is existing and then we'll figure out um what we might want to change here.
Let's So, let's run over here.
Oh, I'm going to get rid of this platform first.
Stop playing.
I'm going to Oh, you know what? I'm not going to completely get rid of it.
I just want to slow it down because it is obnoxiously fast and it's making me dizzy.
So, I'll put the speed 2.1 for now, and then we'll press play.
Now, I'm going to go over here and bounce without this thing kind of knocking me in the head constantly.
So, right now, you can see that I walk up to it and it kind of is that wiggly bounce.
And if I jump on it, it bounces me some amount.
Um, but this is the maximum bounce that I could have with that bounciness.
Except that the bounciness is also based off of how far I've fallen.
So, let's stop playing and switch the script now.
So, instead of using that bounciness factor on the collider, we'll go find the spring.
We'll set that material to none.
And then we'll add the bounce player script instead.
Oops.
What have I done? I accidentally typed a backslash there.
There we go.
The bounce player script.
I'm going to give this a value of maybe 400 as well.
So, I'm not sure how how much I want springs to bounce, but I do know that I want to be able to control how much they're bouncing.
I'll check the only from top option again.
Press play.
And now I should be able to bounce right off of that spring as well.
And always bounce the same amount now instead of bouncing some amount based on how far I fell.
So, I bounce and if I jump super high and I fall down, I still bounce up the same amount.
And that's the tighter control that I wanted.
Now, of course, if you want to use bounciness, you can.
Um, if you want to use the collision data, you can also speed up the bounce based off of how fast you hit it, but or or based off of the velocity of the thing that hit it.
But I like that I have a nice tight control here because now I can say exactly how far away things need to be and how much of a jump I need to make to be able to make it across somewhere or something else.
I especially like that for things like this ladybug where now I can use the ladybug as essentially a mobile spring that I can control with the lasers by freezing him whenever he gets to the wrong or the correct spot.
So now that I've got that done, I'm going to stop playing, save my scene again, make sure everything's in there.
Go into plastic so that we added the bounce player script and we'll check in our changes.
One of the key things I wanted to teach in this course that's not coding is how to go about finding art for your actual game.
Now, there are a lot of different processes and ways and places that you can get things.
The Unity asset store is of course one of the easiest and then there are a lot of 3D art sites.
But if you want to get custommade work, the process is usually super expensive and really really time consuming.
But I found a little hack that makes it quite a bit cheaper and quite a bit easier and actually I think viable for a smaller or indie developer.
And that's using some AI generated concept art in sites like Fiverr.
Well, specifically Fiverr.
That's my favorite.
And what I wanted to show you now is some of the AI art that I've generated using MidJourney.
Here you can see a bunch of different characters that I came up with.
Just trying to come up with a nice robot that we could battle or some other different type of robotic creatures.
Got some robotic mice and other things.
You can see if I click on them, I can see the actual query that I put into MidJourney to generate these things.
And I'll show you how I did that in just a moment.
But I want to scroll up through and show you some of the cool ones that I found.
One of the characters that we'll actually be using very soon is this cartoon robot dog that I thought came out very, very cool.
I'll show you the end result of that in a moment.
But there are just lots and lots of things in here and it's extremely easy to do.
Let me show you how you generate these things real quick.
Once you log in to Midjourney, which you can do with your Discord account, you'll be in the newbie channel or at least you'll be able to join these newbie channels.
You'll see something like these newbie 106 or some other random number.
Go join that room by double clicking on it and then you need to use the imagine prompt.
You type / imagine or slash I and enter and then give it your prompt.
So say I wanted a robotic grasshopper, a cartoon robotic grasshopper that's in 2D.
I would say imagine a 2D robotic grasshopper cartoon style um video game sty may I'll just leave it cartoon style and I just hit enter and what'll happen is an image will start to appear or a set of image it'll it'll give me four images that I can choose from that I can either make variations on or upscale.
You can kind of see some of the other people's images that are going by.
If I scroll up, I can see mine start to generate.
It gets hard to scroll up if there are lots of things generating at once.
And I just let it go and eventually it's going to show me something here.
And if I like one of them, I'll be able to get a bigger better version of it or get a bunch of variations of it.
And that's what you saw on the other midjourney page here.
I haven't just typed in the command many, many times.
I found one that I liked and then I hit upscale on it or I found one that I liked and I hit the variation button on it.
Got a couple more variations and a couple more variations until I found one that I thought was good enough.
Once I find one that's good enough and let's go back into Discord real quick and see if it's finished generating so we can see what the new ones look like.
Did it generate? Where is it? Got to scroll through.
A lot of time it'll pop up or pop down at the bottom as soon as it's done.
So, oh, there it is.
And see my robotic grasshoppers.
But let's check out how we can upscale these, do variations, and then see how we turn the variation into something that we can actually use.
I really like this yellow one.
I think that that guy looks pretty cool.
So, what I'm thinking is I'll hit the upscale on it.
U4 will upscale number.
This is 1 2 3 and four.
So, that yellow one's four.
And V on it will give me variations.
I hit submit.
I can actually add in some extra context there if I want.
And then I can hit this button to just regenerate a whole new set of them.
They'll appear down here below as new images.
And once I found one that I like, what I do is I go on to the midjourney page.
They'll show up here shortly after I've finished.
And then I go select that image of the one that I like.
Maybe it's one of these bees.
And I actually did do one of these bees.
You'll see that a little bit later.
I go find the image.
And then I can uh oh, right here.
Hit the save or rightclick and just download the image.
Hit save as.
Then I take that image and jump over to my favorite art site, Fiverr.
Fiverr is not a free site, but it is very cheap, or at least relatively cheap compared to paying an artist somewhere at an actual gamedev company.
You can find outsourced artists who are interested in building things and they'll tell you their rate and a lot of the time their rate is really, really good.
Here you can see one of the artists who I sent over the game art to.
I sent the dog prototype to them and they generated and created this dog and I also sent them a cat and they generated and created this cat.
It's fully animated and available and you'll be able to download those both right below in one of the upcoming lessons after I show you how to do the import and export and all of the setup.
But you can see that this is a pretty simple setup.
At least I think it's a very easy way to get art and it's drastically drastically cheaper.
got a premium package is what 120 and I think the total cost on those was like $200 which is really really cheap when it comes to getting 2D animated art or getting any game art.
In the past I've paid up to thousands of dollars just for a single concept or a single image that's going to be the splash screen for a game.
Art gets really expensive especially if you've got to pay artists who live in very expensive places.
So, if you can find some art that you can generate or um let's cut and if you've got big studio money behind it, then that's not unreasonable.
But when you're an indie dev, that's just really not realistic.
And it makes it so that this is really, I think, the best way to get art or one of the best ways to get art.
It's my favorite way to get stuff that's custom, really cool, and matches for your game.
Just find a couple artists on here, figure out who can work well with your art style and what it is that you want, and then start giving them concepts.
Those concepts from Midjourney make a huge difference.
It makes it very easy to just con um what's the word here? Communicate.
There it is.
Communicate what it is that you're looking for, what you think is cool, and not have to go back and forth and spend hours or days of their time trying to track that down.
So, use MidJourney, generate some concepts, find a good artist on Fiverr, and I'll link this one down below, and see if you can come up with some cool stuff for your own game.
And just to be real clear, don't do that for this project.
Do it for whatever game or games you might be building of your own that you actually care about and want to invest in.
Just want to make sure that was really clear.
Now, one of the key things you're going to find out when working with artists online is that their file structure, their naming structure, and the way that they give you things is going to vary drastically.
If you've got your own art department, you've got an art lead who can manage and keep that all in line, then it's not a big issue.
But when you're working solo or you're working in a small team and you've got to outsource art or you're not just don't have somebody that's actually in charge of art, keeping things tight, it gets to be somewhat messy pretty quick.
And one of the things that I really recommend you do is set up a new project when you're importing art to make sure that you figure out what's in there, what should be there, rearrange it, and get it into a good package, and then pull it into your actual project.
So here you can see I've got a character import project.
This is a totally empty blank project.
And I'm going to pull in that cat and dog package that I was just showing you.
Now, you can see that it's got an animations folder on the root with a cat folder, a character folder, a dog, an effect, and then some prefabs, and a scene.
And there's a bunch of stuff here.
So, I'm going to import it.
Let's pull it in and see what it looks like.
And go look at my scene.
I'm going to go open up this animation scene and press play.
Looks like we've got a nice sample here that we can take a look at.
Okay, it looks pretty good.
I can see the animation's playing.
Everything is going around.
Let's go check out this dog.
If I expand out the dog, I could see the animator underneath it.
And I'm going to go double click on that animator.
And notice that it's using an animator override controller.
So, they've got it set up with a character that's got some animations.
And then this dog is overwriting it.
So this is some generic character controller.
I can double click and open that up and see it right here.
It's got idle, jump, move, duck.
A couple things.
Let's drag it down here so that we can dock it.
Select the dog and then see what it's doing.
So I can see that it's going through the idle.
And then do we have any parameters? So there's one blend parameter.
If I set that up to a one, what does it do? Add.
Doesn't seem to do anything at all.
Let's go to the layers and adjust the layers now.
So, if I adjust the layer here on the action, what is this one doing? Oh, that's the shoot.
And then we've got a hit action.
What is this one doing? If I adjust the weight here, I can drag it up.
Oh, okay.
And then he's going to keep taking hits.
So, it's got layers for the hits so that I can looks like take damage and uh shoot at the same time.
And then if I go to the mobility section, I can probably force it to start moving by finding this transition, adding a condition to the blend being greater than zero, and then go find that parameter and turn that blend back up to greater than zero.
Ah, there we go.
And now it walks.
So now we can see that it can walk.
It can't doesn't look like it's going to be able to walk and die at the same time, which I think Oh, I guess it kind of can, but be a little bit weird.
They don't really stack well.
Um, but it can walk and shoot at the same time.
And then I think that there was one other cool thing it could do, which was this duck.
So, let's add in a transition here for the blend being greater than zero.
Let's see what it does.
Go find it here.
Let's go find that parameter.
Set the value up to one.
It should go into move.
Ah, and then it goes up to the sky.
So, this is a raise up and down.
But we don't have a good animator controller for this.
As you can tell, we've got a bunch of animation going on.
The controller is a bit of a mess.
And the project structure here is definitely not what I want.
If I pull this in, all of these animation folders.
Oh, these might be okay.
We'll be all right.
And then I'm going to get these weird prefabs that are these animated characters.
They they might actually be okay, too.
Let's see.
And let's see.
What do we have in sprites? Oh, okay.
These things will definitely be in the wrong folder in a sprites folder.
So, I'm checking it out and I'm thinking I might just import everything here except for renaming a couple a couple spots.
So, let's go take a look at our project again.
If we jump back over to our main project and look at our project structure, we've got an art folder and underneath it, we have some enemies which has all of our list of enemies.
And then we've got an animation folder up here.
And we've got a prefabs folder up here.
If we pulled that one in, we'd also get a um sprites folder here, which I think I'd like to be in my art folder.
And we get some stuff in animation, which I think I I'm okay with.
So, we'll jump back over to the other project, and we're going to just take this sprites folder and move it into an art folder.
So, I'll go to the assets, rightclick, create a new folder, and I'll name this art.
Now, if you have a different project structure, of course, make this match your project structure instead.
I'm going to take the sprites and drop that into here.
And then I'm going to open it up and I'm going to rename this from sprites to enemy sprites.
And then I want to expand that out.
And I want to just make these folders be uppercase.
So the cat's going to be uppercase C, dog's going to be an uppercase D, and effect will be an uppercase E.
I think I want to rename the animation folders as well.
Um, I'm not sure that I want to keep this animator controller in here.
Although I think that um, well, let's see.
No, I think that we'll probably just delete out the animator controller and we'll add in a brand new animator controller for it because when we pull this in, it's going to have all of the stuff on here that I don't really want it to do.
So, I'm going to delete out that character subfolder.
We'll rename this dog folder with a capital D and rename the effect folder with a capital E.
The last thing I want to do is check my prefabs and just rename these so that they are cased correctly and don't have underscores.
So this is a bullet.
This is a cat bomb.
I'll just name this cat bomb.
And then I'll name this dog laser.
And we'll name this dog with a capital G and cat with a capital C.
Now I think I've got everything neatly lined up.
The last thing I want to do is rename my animation folder here to dog cat animation.
Although now it's not going to work anymore because I've deleted that animator folder.
Let's hit reload.
Let it reload that.
If I press play now there's no more animator controller on them.
So they're not going to animate.
They're just going to do exactly that just like I expected.
And then the final thing I need to do is export this as a package.
So, I'm going to rightclick and I'm going to choose export package.
And then I get to choose all of the files that I want to include in this package with my newly restructured format that doesn't include that extra character folder.
Oh, you know, I also want to get rid of these override controllers.
So, let's stop playing and go delete those as well.
I'm going to go find that cat override controller, delete it.
And I'm going to go find that dog override controller and delete that as well.
Go back into the assets, rightclick, and export.
And this is why we go through that process.
So, I want to find all of the stuff that I'm not going to use and just get it deleted out of here.
This effect is for that laser.
I'm not sure if I'm going to use that, so I'll leave it in.
And we've got the prefabs here for everything.
And I don't need these settings, so I'll uncheck those.
I don't need the sample scene.
Don't need this universal render pipeline setting.
I think that looks good.
So, I'll choose the export option.
And I'll call this dog cat clean.
And I'm going to put this into my Alien Blasters root folder and not inside of the assets folder so that I've got my package here.
In fact, I think I'll make a new subfolder in here for my um art packs.
And then I'll save it right into there.
Once that's done, I'll import that pack into my actual project.
Once that's done, I'll open the Alien Blaster project and go import that.
So, I'm going to go through assets and import package and custom package and then just go find my dog cat clean.
This should show me all of the things that I've got.
So, it's going to say that there's already an art folder, but it's okay cuz we're not add or not replacing anything.
There's already a prefabs folder, but that's okay because none of the files in there getting replaced either.
They're all new.
So, I'm going to hit hit the import button, and I expect that all of my characters are going to now appear here.
So, I've got inside of my animations folder, a folder for my dog, my cat, and effect.
Oh, I've messed up my name of this folder, though.
So, I'm going to take all of these and drag them into anim.
Oh, you know what? I'm going to actually take these animation ones and move them into animations because I like that name better.
It's plural and it makes more sense.
Let's get rid of the default animation folder that I had or the previous animation folder.
And now I've got my cat and dog, which have all of their own animations cuz they have multiple.
And then I've got my other characters that have very few.
They don't need a subfolder yet.
So, let's take a look at our prefabs.
Now, the prefabs are also updated.
It doesn't show in here that there's something changed because it's not a new folder, but you can see it right here in the prefab section.
Or if we go to plastic and see all of the new files that we've got.
Let's go back into the project view, though, and we take a look at the dog.
Got the dog right here.
And I want to make this be our next enemy.
So, I'm going to drag it right out here.
But he's looking pretty huge.
Now, before we go about adjusting him and resizing him or anything like that, let's save off our scene, go into plastic, and say that we've imported our cat and dog.
Want to get these all committed before we start making changes and modifying things.
And we'll check that in.
Now, we're going to set up our dog.
But before we do, I noticed that I have a commit down here in plastic showing my art packs folder.
And that's because I accidentally put it in one folder too low or one folder too deep.
So, I'm going to hit open in Explorer.
Pop open the window here, this art packs folder.
I didn't want it to be in my Alien Blasters folder.
I want it to be one folder up in my project.
So, I'm going to paste it up there so that it's not actually in my project.
It's not something I want to be part of the project.
It's already included in there when I've imported it in.
So now I should be able to go back in and see my pending change gone.
All right.
Now that I've done that, let's go modify our dog.
The first thing I want to do is shrink this dog down a little bit.
But I don't want to do that on this root dog right here.
Instead, I want to go down to the base object that has the animator.
And I'm going to set the scale here to about 0.5 on the X and a.5 on the Y.
Now, if I go change the pixels per unit, that will shrink everything down on this setup of textures.
But because of the way that the character is set up with all of these different body parts, if I do that, the animations are all going to instantly break.
Let's go take a look at that real quick.
I'll show you what that looks like so that you can see and then we'll go through the scaling.
So, if I went to the dog and I changed all of these pixels per unit to maybe be 200 so that it shrunk down and see I get small sprites, but everything's separated and far apart.
And if I press play, actually, I don't think there's an animator on here, so probably nothing will happen at all.
But if I did press play, all the parts will animate, but they're just going to be offset in the wrong spot.
So, we're going to undo that change.
Hit apply.
Set them all back to one or 100.
And then we'll change the scale here of the child object instead.
And then we're going to flip this around as well by changing the rotation to 180.
I want all my enemies to face the left by default.
At least most of them.
This one definitely.
And I want to have that I just kind of want that to be the default direction.
So that way I'm running to the right and the enemies are to the left.
I of course have dogs that are flipped around, but I'll do that by flipping the base parent object instead of this child one.
So now I've got my dog there and I want to make him animate.
I don't have an animator controller because we deleted out that override one and the character one that was there to kind of show off what it could do but didn't make sense for what our character was actually going to do.
So I'm going to go into the dog folder, rightclick, choose create, and we'll create an animator controller here.
I'll name it dog and we'll assign it to our dog.
So, select the dog and oh, got to select the base object though, the one that has the animator, and drag it on.
Then I'll double click.
That'll open up my animator window.
If yours is docked up here or over here or somewhere else, just dock it down below so that you can see it.
Actually, you know what? Dock it.
Dock it up here instead.
I lied.
Dock it up at the top so that you can see the animations instead.
Now, with the animator window open, let's take the dog idle or idle dog and drop it right into the blank canvas.
That should be our default animation.
And I don't want this dog to walk forward right now.
I just want it to go up and down and shoot lasers.
That's my thought.
I don't want him to be moving.
I want him to be a kind of a standing still but up and down blasting um target that's kind of a problem like that and acts differently than some of the other enemies.
So, I've got this idle dog animation, and the animation I want to go into is the rising dog animation.
So, I'm going take the rising dog animation and drag it out as well.
Next, I'll create a transition by right-clicking on idle dog, hitting make transition, and then choosing rising dog as the target.
So, it'll transition between idle and rising, and then I'll make a transition back from rising to idle.
Now, if I go into my scene view or into my game view and press play, I should expect to see my dog just going up and down back and forth between those two animations.
Let's see.
There he goes.
He's up and he's down.
If I take my animation window and just drag it down, we can actually see it kind of happening as he goes through the idle.
Up and down, up and down.
And he's playing his animation just like I expect him to do.
Now, I also want him to play his laser blast animation.
and I want him to play that constantly as well.
So, what we're going to do is add a new layer.
We'll go to the layers section.
We've have this base layer, which is dealing with our going up and down.
Let's hit the plus button and add a new layer and call this attack layer.
In our attack layer, we're going to add in two more animations.
So, I'm going to take my animator and I'm going to drag it up.
I think I'll dock it up here so I can see all of these windows at the same time.
I've got the base layer that has that movement on it or the idle and the rising up and down.
Use the middle mouse to pan around.
By the way, go back to the attack layer and I'm going to add first a blank state.
So, we'll rightclick and choose create state and choose empty.
This is going to be a default state that does absolutely nothing.
And then we'll add a shoot dog state or a shoot dog animation right below it.
Drop that in.
And then we'll add a transition.
Let's zoom in a little bit.
Right click, make transition, and drag that down to shoot dog.
I'll right click and make a transition back up to that blank state from shoot dog.
And then we're going to go on to the transition for shooting.
And I don't want this to necessarily shoot constantly, but I'm going to start it off shooting constantly and then add a condition.
So before we add in our condition here, let's go to the layer, hit the little gear, and drag this weight all the way to the right.
I'm going to save.
Make sure that I've saved my project as well.
Press play.
And I want to watch my dog and make sure that he's animating, going up and down, and shooting at the same time.
I think it looks like he's doing it.
Let's make this thing uh nice and big.
I'm going to stop playing and let's rightclick um and hit maximize.
There we go.
And play.
And I can see my dog is going up and down doing what he's supposed to do.
Now, there is an error here saying base animation event has no function name specified.
So, there's an error that we need to address.
And I want to start adding some control over this so that maybe we can control when our dog goes up and down.
But first, let's take a look at what that error is.
Now, if I stop playing and I unmaximize my game window and I go down to the console window, we can see that it says base animation event has no function name.
And it's saying base because that's the name of this object.
And it's saying that there's an animation event that's playing that has no function name specified.
So, one of these animations has an animation event on it where it's trying to call into code, but it doesn't know what code to call into.
And the animation that's doing that is the shoot dog one.
We can take a look at the shoot dog animation by double clicking on the motion here, and we'll get the animation window, but I need to go click on the base character to actually see it.
So, if you don't click on that, you're not going to get it to show up.
And now once you have this animation window showing up, if you don't have the correct animation showing, you can just hit the drop down and find shoot dog.
Here I can scroll through and actually see the animation playing on my little dog.
There you can see it lighting up on him.
But I can also get to this point right here where this little bar is.
And that bar is indicating the animation event.
So, right at this point of the animation is when it's supposed to do something, which is probably the time when it's supposed to be spawning that laser so that it visually matches.
And if I look at the function, you see it says no function selected.
So, I need to add a function here that we can call into from our animation event because I want it to tie in exactly with what the animator and the artist had set up so that it looks right and feels correct.
And to do that, I'm going to go to my dog, the base component here, and we're going to add a new script.
So, let's take this animation window, dock it down below, go to the project window, and go to our scripts folder.
We'll create a new dog script, name a new C# script named dog.
And we're going to at first attach it to this base object.
Not to the dog because that won't get the animation event call back, but instead to the base object.
And we'll talk about how we can adjust that in just a moment.
First though, we're going to drag the dog onto here.
And now, if we go back into the dog or not back into, but first into the dog script, we can add a public method that we can now call from our animation event.
So, say public void shoot.
And it doesn't have to do anything.
We can just uh let's write a log debug.log shooting and add a semicolon.
Now, if we go back into our animation event in the animation window.
So, go find my animation window and make sure that I've got my base character selected.
It's my animation window.
With that base character selected, go find shoot and we'll go find that animation event and hit the function dropdown.
And now shoot is an option because shoot is at the same level on this same object.
Now, let's press play.
We should no longer have that error.
And every time he shoots, we should see a little log down in the console.
I'm going to drag the animator window down here.
Take the console window here.
Hit clear and watch.
And every time it goes up and blasts, we should expect to see some sort of a log.
Oh, there it is.
Shooting.
Shooting.
The editor just hadn't updated my log entries.
There we go.
It's adding one entry each time he he goes up and shoots.
So, now it's working and I'm ready to tie in the actual shooting part.
But I want to stop playing and go commit my changes because I've just added quite a bit to my animator.
Um, these changes for our files here.
These meta changes are actually not changes.
What happened was we modified them and then changed them right back.
Or at least I did.
So, I'm going to go select them all.
Rightclick.
Well, first let's just go double check that I haven't selected anything that's not an image here.
Okay.
Yep.
I'm going to go select all of them except for that sandbox file.
I don't want to select that.
the ones that are not new, the ones that I've changed that were just the sprites.
Right click and just hit undo because there was no actual difference there.
And then I'll commit my changes that we've added the dog animator controller and check it in.
Now that our dog is animating properly and even calling that animation event, let's hook it up so that he actually does damage to the player and let's use that laser effect that we have.
We'll stop playing first and I'm going to go find my dog laser.
It looks like it's right here.
If I take a look at it, it's this big long laser beam.
I think this will work perfect for a weapon that can just hit the player and knock them up, do some damage, and kind of keep them at bay.
be really cool for a horiz or vertical level where we're going up and you got to dodge things, I think.
So, I'm going to go find my dog now and expand them out.
If I go through the hierarchy of my character, you should be able to find this blaster sprite.
That's the one that's showing up.
Then, when it kind of animates and pops out, I don't need to enable it because it's not going to show up.
All of the children and everything else are all disabled as well.
Or I think they might be just off in position and tiny tiny scale.
Let's see.
Oh yes, they're scaled down to zero.
So if I scale it up, you can see that they get nice and it's that laser thing right there.
So I'm going to leave that scale at one for just a moment.
And then we're going to take our laser blast and drop it into there.
We actually have to set the scale up to one because if we don't, when we drop in our laser blast, it'll get scaled down to a zero.
So let's go find that dog laser blast.
Where was that? Should be in my prefabs.
Dog laser.
Here it is.
and I'll drag it as a child of the blaster.
I'm going to reposition it with W.
So, just move it over so that it's right on top there.
Looks like about a.465 or maybe a negative.4.
Maybe or.5.
That looks right.
I said negative.
There was no negative there.
So, about a.5.
I go back to this blaster.
We can set that scale back down to a zero now.
And then even disable the object like it had it before.
Now, if I press play, that laser should appear.
When I blast, the laser should just kind of show up.
I don't need to spawn anything.
It's just going to enable.
There we go.
It's popping out.
And it enables pretty much instantly.
Looks pretty good.
It blasts and then it blasts, then it blasts, and then it blasts.
Now, I want this thing to do damage.
So, if I run over here, right now, the laser doesn't do anything to me.
So, let's make a change to our laser again.
We'll go to the laser object, go expand it out, and expand out some more.
First, let's turn this thing back on so we can view it.
Turn on the blaster.
Set the scale back to one.
And then, let's find the object that's the beam.
So, it looks like it's this 21 object.
We've got the one one is or one two is that circle.
One is this tighter circle.
and 22 is this bigger area outside or the kind of glow around the beam.
I'm going to go select the actual beam object which is just this sprite renderer.
And then we're going to add a component to it.
We'll add a box collider 2D.
Box collider 2D should allow us to knock back players and and hit players and do damage to them.
The next thing we just need to add is a damage player script.
So, we add the damage player script that we just created or just started kind of generalizing.
add it to our box collider.
We'll save.
Press play.
Let's run over, hit that laser, and see what it does.
Oh, look at that.
I'm getting knocked back.
I get shot.
I get bounced.
If I hit the top of the laser, I'll kind of bounce off of it.
Let's see.
Can I Can I hit the top? I'm not very good at that.
There we go.
And I can bounce off of it and start taking damage.
So now I'm taking damage from my dog without having to really write any custom code for it.
And this is generally what I want to do, unless I have some special use for the dog where I want it to do something else.
But right now, this collider is automatically growing.
It's adjusting.
It's not the most optimal thing, but I don't expect to have more than two, three, four dogs on the screen at most.
But it's adjusting.
It's going to knock me back and hit me automatically without me having to do raycasts or figure out anything else to to get this code working.
So, I'm going to stop playing.
And also, it's worth noting that we added that animation event call back on our dog.
We haven't even needed to use it yet.
And it's important to note that we didn't just dive right in there and start writing code because we don't always need to do that.
That's not always the best thing to do.
In fact, we may never even need that animation event.
The way that things are hooked up, the way that the animator set it up and created it might not be ideal for our code.
And you're going to find that often is the case that the animators and designers aren't necessarily setting things up in the simplest way.
They're setting things up in the way that they've done it before and know how to do it.
So, here we go.
We've got our dog with a working attack.
I'm going to go into plastic.
Well, first I'm going to update my prefab.
I'll go to the dog overrides and hit apply all so that that one gets applied.
And I'll go to the laser.
Oh, I don't need to apply the laser.
It got applied on my dog prefab.
I think we're good.
So, we'll say that dogs deal damage with lasers and check that in.
Oh, got to recheck it in.
We got that error that pops up on occasion and do a check in.
So, I hit check in again.
And there it goes.
For this next section, I just want to do a small assignment.
I want you to do a little experimentation with the NPCs that we have so far.
We've got our ladybug that we can bounce off of, assuming that you made a ladybug and not a spider or something else.
We've got the dog going up and down.
We've got the frog jumping back and forth that we're going to replace with a laser grasshopper.
And you've even got a cat that you could start pulling in and importing and possibly coming up with some ideas for.
It's got a few attacks, but I think the key one is the grenade launch, which we'll dive into later.
But for now, I want you to take the characters that you already have set up and do a little bit of experimenting with a new level.
Make a level three or whatever level you're on right now, the next one, and build something going vertical so that you're going up instead of to the side.
Use the dogs and the ladybugs as possible tricks or ways to go up and down.
and even play with maybe using multiple lasers.
Perhaps create a blue laser and a yellow laser and a red laser and have them in different spots so you can maybe toggle your ladybugs to get up and down.
If you're able to build something cool, then make sure that you export a WebGL build and share it with us all in Discord.
You can go check out and see what it is that you built and, you know, get it in front of people, get some feedback, and have a little bit of fun with it because I think that people build all kinds of really cool things when you start giving them a little bit of tools.
It's amazing to see the kind of creativity and the ideas that start popping up.
So, go ahead and do that.
Have some fun with it.
And then if you're up for it, share your experience and share the results of what you've got, like I said, in Discord or email them over to me.
Now, we're going to make a slightly bigger change to the game.
We're going to replace our player character so that it kind of lines up with the visuals of the robot and the other characters and so that we can go through the process of building a player where we can modify and change out those visuals pretty easily.
So, the first thing we're going to do is pull in the robot package.
You should be able to down that download that right below.
Download that down below.
You get the idea.
So, grab the robot package and drag it into the project.
This is another one of the packages just like the dog except this time I just pre-organized it for you so that you don't have to watch me go through that process.
Same exact thing though, just found the robot in my temporary project and then I exported that to a robot project.
By the way, when you're exporting things, you can also just select specific prefabs or objects.
And that's what I did here.
I just selected the effect and the robot and exported just those.
So, here you see I've got a robot, an explosion, and a blue bullet.
Those are the ones that I'm going to use for my character.
So, I can have a character that runs around and blasts back at these things.
So, let's hit import.
And we should get our new character pulled in.
I think it went so fast that I didn't even see it.
All right.
Yep.
We've got an explosion, a bullet here, and a robot here.
So, let's go to the scene view, and we're going to go find the robot first.
Before I actually pull anything into the scene view, let's just go double click on the robot and see what it looks like.
So, here it is.
You can see we've got this little character with a weapon, an antenna on its head, and uh it looks like a bunch of different little parts.
It's built up of a bunch of pieces.
I can turn the pieces on and off and see this is not just a single sprite.
It's actually just a full-on animated character.
It's got a character controller here that is using that character controller that we saw before.
And then it has some idle and jump and run and duck animations.
They're not hooked up right now, though.
So, if we go put them in game, we're not going to see any of that happening.
Let's go take a look at the animations folder.
I think that Oh, I'm already in it.
See, we've got dead, a duck, we've got a hurt, an idle, a jump, and oh, three jumps, a run, and a shoot.
So, let's get this character hooked up.
Let's grab the prefab in the prefabs folder for the robot, and we're going to make it a child of our player.
So, I'm going to drag it onto my player.
So, click and drop it right onto the player.
Now, you see I've got this giant robot sitting on top of this little tiny player.
The first thing that I want to do is scale this robot character down because it's way too big.
Now, if I just go in and start modifying the pixels per unit, you saw what happens with the dog.
The whole thing will fall apart.
Instead, I can just scale this character right here to about 0.5 and.5.
I'm going to move the position down, the Y position, just by holding, clicking, and dragging so that it lines up perfectly with the bottom.
But it should be about negative one.
And a negative one should line it up just about perfectly.
I might have to move it up just a little bit though once I see the collider.
Yeah, it looks like maybe it does need to go up just a tiny bit.
Right about maybe like a negative.9 or 85.
I mean it we'll see how it looks.
Oops, I meant 0.95.
We'll see how it looks once it's animating though.
So I'm going to go with a negative.95 and a.5 on the scale.
Then we'll go back to the player.
I'm just gonna disable the sprite renderer.
So, sprite renderer is not showing up.
And right now, the capsule collider doesn't actually align with my character.
So, I think I'll um increase the size of that as well.
Let's go find our capsule collider.
And we're just going to grow this.
So, I'm thinking it's going to be closer to 2 m tall and a zero.
Yep, there we go.
So, that's about right.
about 2 m tall and a zero on the offset, which by the way is about the size of a normal game character, at least in 3D games.
I think that that looks good.
I could probably extend out the X size, but I think I I'll keep it tight like this for now.
I'm going to save and then press play.
And let's watch our robot run around.
And theoretically, everything should still for the most part work except for animations and visuals because we've not no longer using that sprite renderer.
We're no longer using this animator.
Let's see.
Um, and yeah, our character is going to do his whatever his default animations are.
So, I can run around.
I can jump.
I can see that my layer is a little bit off.
Um, your layer could be completely off.
We might have to adjust that before you can see it.
But, it looks like the character is partially working.
This is nice.
So, I'm now ready to start setting it up so that it animates properly.
Well, and to start fixing these these layers, let's finalize this by turning this into a prefab or updating this prefab and modifying the visual layers.
So, I'm going to go to the robot.
I'm going to open up the prefab for the robot, this child prefab.
And then we're going to find all of the sprite renderers in here.
So, I'm just going to scroll down and select this sprite renderer.
I'm going to hold shift and hit the down arrow until I get no something that's not a sprite renderer.
So, it looks like this hand is not a sprite renderer.
So, I'm just going to control-click that off.
Then, I'm going to control-click the rest of the way until I find things that are not sprite renderers.
Those ones I'll just turn off.
That hand is not a sprite renderer, but these children are.
I'm going to find everything that has a sprite renderer.
Looks like that's it.
So, everything except for these two hand objects.
And then I'm going to change the layer to be our player layer instead of the default.
I'm going to go back out of this prefab, save our robot prefab that's a child of our player prefab.
Then I'm going to go to the player prefab, go to overrides, and we're going to apply these three things that we've disabled the sprite renderer, we've modified the capsule collider, and we've added the robot child prefab.
We'll hit apply.
And then I'm going to save my scene and go to plastic and commit that we swapped the robot visuals.
We haven't fixed the animations, but we've done the visuals.
So say swapped robot visuals, not animations, and check in our changes.
Now, we're going to dive into the animations of our player, this robot specifically.
Right now, he's just playing the same animation over and over, which looks like an idol.
and a chute.
Let's go take a look at them.
The animator for this robot is underneath the robot and on this base object.
Looks like the name of it is Robo, which is, I think, a terrible name, but that's actually an animator override controller.
That's using this character one.
I can tell because if I double click on it, it says animator override controller.
And then it references this character controller.
Let's go to the character controller and open it up and see what it has.
So, here's our controller and I've got the robot with the animator selected.
Again, we've got one parameter named blend.
And if we go to the layers tab, we'll see that there are three different layers, mobility, action, and hidden.
I don't really like the names, but we can modify these.
Let's hit play real quick and watch it in action again.
So, on the layers, I can modify the action layer to stop it from shooting.
The shoot action is happening right there.
I can go to the hit layer if I want.
I could drag up the weight and make it start taking damage and dying.
Doesn't do a very good job of not looping back over though.
Obviously, I'm not going to want to control it that way, but we can change it later.
And then in our mobility tab, we've got quite or layer really.
We've got quite a few different options.
We've got a duck, we've got a run, and we've got a jump.
We have one parameter here named blend, and that's actually for this jump blend tree.
So we can blend between our jumps so that we can have a nice smooth jumping animation.
But we can't even get into our jump yet because we don't have any transitions.
So we need to go up to the mobility level of our or our mobility layer.
And here we have a bunch of transitions set up to go from one state to another.
But there are no conditions to allow this to happen.
So let's stop playing, add some parameters, and set up our conditions.
First, I'm going to rename our jump parameter.
This jump blend is named blend, and I think that's too generic and really easy to get confusing what's going on there.
So, I'm going to call this jump blend with a capital J and a capital B.
Then, I'm going to add in a parameter for speed.
I'll make that a float.
And this will be for how fast we're going or for if we're moving.
In fact, you know what? Let's just change this instead.
Since we're not going to be blending anyway, let's use a bool for our movement.
So, let's add a new boolean and let's call this move.
We'll add another new boolean and we'll call this one jump.
And then another one for ducking.
I was thinking of adding a float, but really that only helps if we're doing some actual blending between different animations.
Otherwise, a bull makes it quite a bit simpler, makes a lot more sense.
So, for our idle tor run transition, we just need one condition.
We need a condition that move is equal to true.
For our run back to idle, we'll select the transition with that arrow going from run to idle.
We'll add a condition again by hitting plus and choose move is equal to false.
Now, if I accidentally delete one of these transitions, like this idle to run transition, like oh, I accidentally deleted that.
I can always right click on the idle, hit make transition, and then drag to the end point or the destination and leftclick.
That'll give me the transition here.
I just have to hit the plus button and then choose my transition condition again.
If I do it like this though, there's going to be a minor issue.
Let me show you what that issue is.
Let's hit play and watch our character.
So, he's just idling, doing his thing.
And if I hit move, watch what happens.
So, he starts running, but watch when I stop him running.
He stops instantly.
The start has a delay.
Look at that.
It doesn't start until it finishes or until it gets all the way to the end there.
The reason for that is this has exit time checkbox.
If I uncheck that, then when I hit move, it's going to instantly start transitioning instead of waiting.
Has exit time will make it go all the way to the end before it exits out essentially.
So, let's add in our other transitions.
We're going to add one from idle to jump.
We'll hit the plus on the condition.
choose our jump being equal to true.
For the return, we'll choose jump equal to false.
Now, we also want to be able to go from jump into run.
So, we'll hit plus and add a jump equals false here.
But we're going to add an additional condition here that we're also not moving.
So, we'll say move.
Oh, whoops.
I clicked the wrong one.
So, jump is equal to false and move is equal to true.
Now, that also means that on our condition or transition from jump back into idle, we probably want to have another condition that checks that we're not moving.
So, if move is false, we'll go this way.
Otherwise, we'll go that way.
The last one we need for jump is from run to jump.
We're going to want a condition again just that we are jumping.
The jump is set to true.
All right.
Now, let's do the final ones for duck.
So we'll go to the duck, hit plus, we'll choose duck is equal to true and move is equal to well actually we don't need the condition for move equal to false.
This is going into duck.
Almost did the wrong way.
Also for run we'll hit plus and choose duck is equal to true to go from run into duck.
Now to go from duck into idle, of course we want duck is equal to false and move is equal to false.
Now notice that we're doing all of this again while we're playing.
That's because this is a scene level or a project level asset, not a scene level asset.
So this the changes will save.
Although we do have to hit save project.
All right, the last change we need or transition is from duck to run if duck is false and move is equal to true.
All right, let's hit the duck button and see what happens.
We duck down.
Look at that.
He can now duck and start shooting.
And he can stand back up.
If I've got move on, he'll move and duck and then go back to moving or to go to jump and then go back to um moving or jump and then go to idle.
Now for the jump blend, let's see.
We'll put them in jump mode.
We'll crank this up to maybe like a 0.5 and maybe a one.
Let's put in a one here and kind of see it happening.
If I go into this jump though by double clicking on it, I can actually slide the blend right up here and I can see how it's going to do that that jump animation.
Now, let's stop playing, save the animator off, and then hook up our code.
To do that though, we need to go into plastic and notice that there's no pending changes.
Then, what I want you to do is hit file and save project.
And you should start to see that your character controller updates.
Again, this is a project level asset.
It's not a scene level asset.
So, it doesn't save when you hit Ctrl S or file save and save your scene.
It does save when you save your project or when that project autosaves.
And that also means that you can modify it while you're playing.
So, now that that's updated, let's say that we've modified the player character controller.
And eventually, I want to rename this and and get it kind of cleaned up more.
But I want to get this committed before we have any issues.
Make sure that we've got all our changes in there.
Now, we're going to hook up the animations for our new player in code.
So, I'm going to stop playing and go find my player script.
And actually, first I'm going to remove the animator that's on here.
So, I've got an animator on my player.
I don't want that there.
I'm going to remove it and then open up my player script.
I just want to make sure that I remember to remove that animator.
Then, I'm going to go up to our animator field, which looks like to me is on line 23.
Remember our animator is found in the awake method.
By calling the get component method, it gets an animator for us.
Since our animator is now a child object, we've got multiple Well, we have an issue.
First, that our animator is not going to be found.
And we have two options for how we can assign this animator.
We can either call the get component in child method which will get the animator from our child down our hierarchy or we could assign the animator with a serialized reference.
And in this case both will work.
But we need to remember that if we end up with multiple things on our player, then adding a serializ or multiple animators on our player, perhaps like a weapon has a separate animator or some other thing, then we may be more inclined to go with a serialized reference where we're assigning and being very specific with it.
Since we only have one, my preference is to just go with get component in children and leave it at that.
Now, if I want to be able to go back and forth between these two types of players, again, we'll have to find a different solution or between these two types of graphics, that is.
But since I don't want that, I just want to be able to get that one animator.
This change will do it.
That'll get me my animator from the child component.
Now, I need to go down to the part where we're updating our animator, which is actually in a method named update sprite.
Let's Well, this probably needs a new name.
Let's rename it to update sprite.
and animation.
And then we could probably refactor it out to have an update sprite and an update animation method separately.
But first, let's fix the parameters.
The first parameter we have here is an is grounded.
We're no longer using that old character controller.
We're using this new one that now checks to see if we're jumping.
So, we're just going to check to see if we're or set the jumping variable jumping to the opposite of is grounded.
And we can do the opposite just by adding the exclamation mark which does an inverse or a not of the is grounded.
So if it's true, it'll put in false.
If it's false, it'll put in true.
Now for our speed, we actually got rid of using a float and went to a bool.
So I'm going to delete line line line and duplicate line 136.
We name the parameter move.
Did I name it move or moving? Let's go take a double check.
I need to make sure that I've got the correct name in there.
Move, move, jump, and duck.
I've got to singularize these and get rid of that uh ing.
So, there we go.
Let's change jumping to jump.
There we go.
And move to move or horizontal speed to move.
Now, the variable that I want this to be set to is a variable just telling us whether or not we're moving.
So, that would be whether or not our horizontal is not equal to zero.
So say horizontal not equal to zero.
All right, let's go try that out.
So jump back into Unity and it should be true moving if our horizontal is less than zero or greater than zero.
Should be false by default.
Looks like it is.
If I jump, it goes into that jump animation.
We don't do the blend yet, but the jump animation seems to be happening.
And if I walk, oh, we get some animation.
We get some animation.
And I stop walking.
Well, we still keep getting animation.
Let's see how long it animates for.
Let's go look at the layers real quick.
Go look at our mobility layer.
Go up one level.
We can see that we're in run.
Oh, there we go.
And we went back to idle.
Let's look at the parameters here.
So, our move parameter, I start moving and we're still moving even though my horizontal shouldn't be moving.
I'm not actually pressing the button to move.
Let's take a look at what's going on there.
If I go look at my player and I go to my properties and then I go into debug mode here, I should be able to see my horizontal value.
Where is that at? Right here.
It's at zero.
Let's start moving and then watch the value.
See how it's not getting to zero.
It's getting close to zero.
It's a tiny tiny little number that e is the exponent.
So, it's getting closer and closer to zero, but it's taking forever to actually reach zero.
And the reason for this is what we're going to cover in the next section.
So, let's stop playing, jump into plastic, and commit our changes that we hooked up the player to um um um hooked the player animator to code.
And let's save our scene.
Make sure that that's in there as well.
Let's take another look at our animation issue, which is really an acceleration and a deceleration issue.
If we go find our robot, go take a look at his animator one more time.
Remember, you can see that he's sitting in this run and eventually he'll start kind of switching back and forth between idle and run and then finalize in idle.
After a little while, it does take quite a bit.
I think he's almost there, though.
Let's see.
Is it going to happen soon? I'll dra Oh, there we go.
It's starting to happen.
Okay.
And he went into idle.
Looks like he just stayed in idle that time.
So, here I've got a player debug window.
In fact, let's open up a new one.
Let's close this tab again.
And we're going to go select the player, right click on it, or yeah, let's just rightclick and hit properties.
This opens up a new window that's kind of like an inspector, but it's locked to the player.
I'm going to switch it to debug mode, and we're going to take a look at that horizontal value again.
Let's go find just the player script and take a look at that.
So, we've got the horizontal value right now is a zero.
If I go over here and I run to the right, it goes positive and then it drops down to these insanely small numbers.
These e numbers are just the number of zeros before it.
It's a the exponents.
It's a tiny tiny tiny number that's still not quite zero.
So, we've got two options here.
one, we could have our animator check to see if it's like less than 0.1 or something in our horizontal and then have it switch over and maybe switch away from a move.
We could have the move variable get set to true only if the horizontal is greater than 0.1 or we can fix this horizontal so that it actually just gets to zero properly instead of being something that's going slow.
The reason that it's never getting to the exact number or here it looks like it's never going to get to the right number and not just getting there slowly.
Oh, and there it got finally got there.
It's really slow.
The reason for it is that we're using the lurp method.
And the way that we're using the lurp method in here is um not ideal.
It is something that you'll see often.
You'll see it in documentation all the time and in a lot of examples.
And it's this line right here where we're going from a start value to a desired value.
And we're always passing in a a small value.
We're never passing in a full one.
So here we're going to go from like zero to one and we'll do move it a tiny bit and then we'll move from 0.01 0.01 0.01 or whatever to one and we'll move it a tiny bit more and then we'd go from like 0 2 to one a tiny bit more and so on.
In fact, let's log this out and see what it looks like so you can get a better understanding of what's happening here.
I'm going to put a debug.log and we'll log out the horizontal value.
First, let's add a dollar sign so we can put in variables here.
That allows us to do string interpolation.
We'll put in the squiggly braces, which allows us to put a parameter in.
I'm going to put in the horizontal value.
Then I'll put in the desired horizontal value.
And then I'll put in the amount that we've moved, which is the time.
delta time times the acceleration.
So, I'm going to copy that, put in more squiggly braces, and paste it in.
Add a semicolon to the end.
Let's save, go play, and see what we're getting in the log and see how that value is changing, how it's actually going up.
So, if we go to the console, I'll clear out my logs.
We'll press play.
All right.
So, here we are playing.
And you can see my horizontal and my desired are both zero.
The delta doesn't really matter cuz it's not changing yet.
So, let's move a little bit and see what happens to these values.
I'll just move a little bit to the right and then I'm going to pause almost instantly.
All right.
So, I press to the right and pause.
Let's scroll down here and look at the logs.
Oh, I've got a lot of logs down here.
So, you can see here I'm seeing my velocity.
The first value here is that uh current one.
That's my horizontal.
Let's scroll up to where it was zero.
So, here's where I started moving.
Right here I was at 0 0 and then the next frame I had a desired speed of five and moved up to a 0.417.
The next frame I had a desired frame of speed of five and moved up to a 1.01.
Then I went to a 1.27.
That's this again this first number before the five.
And I keep going.
You can see that number went up up up up up up up up up up up up up up up up up up up up up up up up up up up up up up up up up.
And it kept going up and up up up up.
And it kept going up and up up up up.
And it kept going up and kept going up, but then it eventually stopped.
And it stopped going up probably because I pressed pause, but it was never actually going to get up to five.
And the reason for that is the same reason that it's never going to get down to zero.
Let me unpause it and pause again.
And look at the number now.
You see how the number kept dropping smaller and smaller and smaller? It's down into more and more zeros.
The amount that it's changing by is also dropping.
It's changing by 0.03.
Where before up here, if I scroll up high enough, you see that it was changing by 0.5.
0.5.
0.5.
And here's some 0.1 at the first point and 0.8.
You can see that the numbers, it's hard to tell initially, but what happens is the numbers keep getting smaller and smaller.
the amount that it's changing by to get to that value just keeps dropping.
So, what we want to do is modify this a little bit so that instead of using lurp and not getting to the desired value that we have, we're just going to modify the value instead.
Lurp is useful if we have a start and an end value and a time like we do with our moving objects that are moving back and forth.
But for this, there's an easier or alternative solution.
It just requires a slightly bit slightly more code to write.
Now, let's go open up our code on line 93.
I'm gonna zoom this out just a little bit.
And instead of using the lurp value or the lurp method here, I'm going to comment that out.
We're going to add in a few lines.
First, we'll check to see if we need to accelerate.
We'll do that by checking if the desired velocity is or desired horizontal is greater than our horizontal.
If that's the case, then we're going to add some braces here and we'll say that the horizontal or underscore horizontal plus equals our acceleration times time do delta time.
Now, if our horizontal gets greater than our desired horizontal, we're just going to snap it to that.
So, we'll say if the horizontal is greater than desired horizontal, then horizontal equals desired horizontal.
Now, we'll go down and add an else if statement.
So say else if our desired horizontal is less than horizontal, well then we're going to decelerate or really it's just going to slow down from the opposite direction or move towards that opposite direction depending on what we're going.
We're going either towards zero or maybe towards neg five.
Who knows? So we could be going either way.
This is going left or right.
So we'll say horizontal minus equals acceleration time time do delta time.
I mean we know we'll see when when our code's running.
That's who knows.
Say if horizontal is less than the desired horizontal then horizontal equals desired horizontal.
That'll give us some nice snapping and nice smooth control over our acceleration.
Let's go try it out.
So we should be able to press play.
And now our acceleration should be I think really in meters per second or in units per second how fast we accelerate instead of some semiarbitrary number.
So, here we go.
I can accelerate and decelerate pretty good.
I think that that looks and feels just about how I want.
The final thing that I want to do, though, is make this character spin around so that he actually faces the correct direction.
So, let's go back into our update method here and the update sprite and animation.
Hit F12.
And when we flip the sprite renderer here, let's instead flip the animators transform.
That's that child object that's down in the hierarchy.
So I'll say underscorean animator.transform.rotation.
Oops.
Rotation equals quatronian.identity if it's going to the right.
That's our default.
And I'm going to copy line 154 on to 156.
And here we'll use quatronian oiler or eule e r.
And we'll put in a zero and a 180 to flip it around.
180 on the y-axis and a zero on the z.
Now we'll have an animator that flips back and forth.
Let's see if that works.
Jump back in.
Press play one more time.
We should be able to run back and forth, have our character animate properly, and uh look pretty cool, I think.
Let's see.
So, he runs to the left, runs to the right.
I can jump.
Everything is looking pretty good.
Now, one thing to notice that when I turn, the turning happens visually when the character actually starts moving.
If we want, we can also just tie in our animation part here to the um the input instead.
We can tie directly into the input and it might feel a little snappier even though it's not actually turn it's not actually moving yet.
We can also just turn up the acceleration though.
So if we want to make this a lot tighter of a feel, turn that up to like a 50.
And now we accelerate at about 50 units.
Yeah, I feel like that's probably a little too fast.
How about a 25? Yeah, I'm thinking I might go with like about a 25 now on my ground acceleration.
So, I'm going to stop playing, set that to 25.
I'm going to override my prefabs.
Just hit apply all.
Go save my scene.
Go into plastic.
And we'll check in our changes.
The player animates properly now or animates move and jump.
Let's hit that.
move and jump and faces the correct direction.
We'll check that in.
Now, we're going to give our player the ability to shoot back so that we can have some enemies that are tough to deal with without just trying to land on their heads.
And we're going to do that by adding a new blaster script.
First though, let's take a look at the blaster objects that we're going to use.
We have this blue bullet prefab and we have an explosion that we can use for when it lands.
The plan is to use this blaster that he already has in his hand, spawn some shots, and have them go flying off at our target, and then deal some damage or kill that target.
To start, we're going to go to the player and well, actually, we'll go to the scripts folder, rightclick, choose create, and create a new blaster script.
Then, we'll attach that script and open it up.
Our blaster script will do two things.
It's going to listen for player input and see when the player wants to shoot.
And then it'll spawn the prefab for our bullet and launch that out.
Now, to start, I'm going to get rid of the start method and replace it with an awake because I want to grab a few components and cache them.
I'll get rid of this comment line on line 7 with controlx or shiftde.
And then in awake, I'm going to cache the player input component with underscore player input with a capital I there.
keeping the camel case equals and we'll get component of type player input.
We'll save that off by generating a field.
Hit home alt enter and enter.
And now we've got a field.
Double click that private keyword and get rid of it.
That player input script is right here on the player just above the blaster.
And remember, we've got our action map that we can double click on to bring up our available actions that we've created.
We have a fire action here, and that's what I want to tie into.
So, let's go back to our blaster script, find our fire action, and when it's performed, let's launch a projectile or at least spawn one.
So, to do that on line 13, we'll say underscore player input dotactions.
And we need to not action events, actions, and then we use the square brace so that we can reference something in this collection or this array.
I don't know if it's actually an array or a list.
It's some sort of a collection here that we're going to reference by string name.
And the name is going to be the same as that action name, which was fire with a capital F.
So, this is going to get us the action.
And on that action, there's an event.
So, we can hit the dot, go find the little lightning bolt down here, see all of the events, and choose performed.
Now, that's going to fire off whenever the fire method is performed or that event will be invoked whenever the fire method is or whenever the fire action is performed, which I think is our left click or control.
We can go look at it again in the action map in a moment.
Let's hit plus equals though and tie this into a method.
I'm going to call this try fire.
T capital T and a capital F.
We'll generate a method for it.
We should get a private void try fire with a input action call back context parameter.
Now in our try fire method, we're going to start by just spawning one of those bullet prefabs.
So we'll say instantiate insta.
There we go.
Instantiate.
and we'll put an underscore and I'm going to call this blaster shot prefab.
We don't have a prefab for it yet.
So, we're going to generate a field for it first.
And then we'll make this of type game object.
We'll change private to serialize field so that it can be modified in the inspector, but only in the inspector.
Then I'm going to move it right up here above my other private field so that my serialized fields are at the top, just the way that I like to organize them.
All right.
Now, we've got our trifire method.
It doesn't have a semicolon at the end, and it doesn't know where to instantiate this blaster shot.
This instantiate method is going to spawn a blaster shot, but it'll just go out whatever the position is stored on that prefab.
So, let's add in another parameter.
Let's just do it at transform.position as the second parameter, and we'll use quatturnian.identity as the third.
This is going to end up using not transform.parent, transform.position.
There we go.
This will spawn it at the position where we've given it.
So, at our player's position, essentially, wherever this blaster is facing the default rotation, which is going to be just all zeros.
Let's save this off.
Go back into Unity.
Assign the blaster shot prefab.
Make sure that that spawns.
And then we'll start building up this blaster script.
So, here's our player with the blaster script, and we've got that blaster shot field.
Let's go find the prefab.
And let's start by just taking this bullet blue and dropping it right in there.
I should be able to press play now, run around, click fire, and have bullets kind of spawn awkwardly on top of me.
Let's see if that's the case.
And here we go.
Look at that.
I can spawn bullets wherever I am.
They spawn as fast as I click and they're giant facing the wrong direction and don't move.
Before we fix that though, let's go to plastic and commit our first version of the blaster.
So, blaster spawns game object projectiles that don't move yet.
And we'll check that in.
Now, we're going to fix this bullet problem.
Our bullets are too big and they face the wrong direction.
We're going to start by creating a new prefab.
Instead of using this visual model, the bullet blue, we're going to create a player blaster shot.
I'm going to do that by dragging my bullet blue out so that I've got a nice visual representation.
It's at 0 0.
Let's move it down so that I can see it a little bit.
And then I'm going to give it an empty parent.
I'll rightclick and choose create empty parent.
I'm going to name this robot or let's call it player blaster shot.
I want it to be very obvious.
This is the player's attack.
Now, I want to change a couple things on it.
Well, let's see.
What do I want to change first? The scale.
This is way too big.
Set this down to maybe a 0.25 and a 0.25 instead of a 0.5.
And if I move the parent shot, make sure that the child shots at 0000 relative.
But if I move the parent shot right about here, I can see that.
Yeah, that looks pretty good.
I can see that as a good position and a good size and scale there.
I do need to change a couple more things, though.
First, I think I want to set that order for my sprite layers.
Let's go to the sprite.
Expand it out.
Expand out some more.
And expand all the way down to this number one.
Find the sprite renderer.
And let's change the sorting layer to be on the player layer for now.
I think I'll bring the order and layer forward so that it's at like a 10.
And then it'll always be in front of my player.
My player values should all be zero right now.
So 10 should be nice and far in front.
I'm going to go find my player blaster shot root object here and then drag it in to become a prefab.
Now that it's a prefab, I'll assign it to the player's blaster.
So take the bler here, find that blaster shot prefab, and very importantly want to make sure that I get the one from the project view.
Let's see, where is it? Player.
Did I Did I rename it? No.
Did I name it wrong? Ah, there it is.
I'm just blind.
So, I'll go find it, grab my player blaster shot, and drag it onto the players blaster shot prefab section right there.
So, it should say player blaster shot, and when I click it, it should select the one down here.
If it selects the one up here, you've made a big mistake.
And if you delete this one, and your player blaster shot now shows as uh invalid, well, then you still need to go fix it.
So, make sure that the correct blaster shot is showing up.
I'm going to save, press play, and make sure that we get a blaster shot that looks about the right size and scale in the right direction near the right place.
I don't expect the position to be exact, but I do expect it to look about right, somewhat close, near the center of my body though, instead of at the weapon point.
Let's see what happens when I play.
All right, we click and yep, I get a bullet right near the center of my body.
Now, if I'm facing the other direction, the bullet doesn't change, but it is showing pretty close to where I want it to be.
Now, I want to change the spawn position of this bullet.
So, it spawns right where my weapon is.
To do that, we're going to stop playing, expand out, or maybe just click.
If I just click over here on my weapon, I should be able to find the gun.
And I want to spawn it not necessarily right at the rect or the transform position of this.
I want to be right out here at the end of my weapon.
So, I'm going to add a new transform child to this object.
I'll rightclick and hit create empty.
I'm going to call this fire point.
Capital F and a capital P.
And then I'll drag it over so that it's right on top of the weapon.
Next, I'm going to go to my player and go to that blaster script.
We're going to create a field for that fire point that we can assign on our blaster.
So we'll add a serialized field and this will be of type transform and I'll call this underscorefire point.
Then we'll use that firepoint when we instantiate.
Instead of using our transform position, we'll use the firepoint.position.
Let's save that.
I'm not going to change the rotation at all.
Now we'll go back into Unity and we need to go to our player and assign that firepoint to our new firepoint field.
We'll drag that on.
Save our scene.
Press play.
And we should expect to see that our shots now appear at the fire point.
There we go.
We spawn.
And look at that.
The shots are appearing at the right place.
If I go this direction, they're still appearing at the right spot.
Notice that they do go up and down as uh as my weapon moves, though.
So, if I happen to click when my weapon's up high, that position is up nice and high, and it's firing up there.
Now, before we start writing code for the blaster shot, let's check in our initial prefab.
So, say initial blaster shot prefab with firepoint working.
Now that we have our blaster shot prefab, let's create a script to control it and give it a rigid body and collider so it can move around and hit things.
We'll start by going into the blaster shot prefab edit mode and I'm going to hit add component and I'm going to find a rigid body 2D.
I'm going to expand it out and set the gravity scale to zero because I don't want this thing to drop or drift down over time.
And I'm going to set freeze rotation so that my blaster shot doesn't start spinning around or doing anything strange like that.
Next, I'll add a collider.
And I'm thinking that a circle collider 2D makes the most sense.
The default radius is obviously way too big.
But if I grab the radius and just click and drag, I can find a value that looks okay.
I am thinking probably about 12 or maybe even a 0.1.
Something right around there.
And then that looks close enough.
I could move that collider a little bit to the left, but I think that that's probably good enough.
You hit it right on that edge.
That'll count as a collision.
The next thing I want is a script.
So, I'm going to go to the scripts folder and we're going to create a blaster shot script.
So, rightclick, create car script, and call this blaster shot.
We'll add that to our blaster shot object.
soon as it finishes recompiling and then we'll open our script up.
So, we've got the blaster shot there.
Actually, let's exit out of prefab edit mode.
Let that save our prefab and then open up our blaster shot script.
So, the first thing I'm going to do with our blaster shot is just make it fly off to the right and then maybe disable itself or destroy itself as soon as it hits something.
So, the first thing we'll do is get the rigid body.
We'll do that in an awake method.
Let's all replace start with awake again.
Hit Ctrl X on that line 7 and clear that e extra comment out.
I'll say underscore RB equals get component and we want to get a rigid body but not a rigid body regular kind.
We want the 2D kind.
Then we'll hit home alt enter and generate a field for it.
I'll double click that private keyword and delete it.
Now I've got a rigid body that I can modify in the update method.
every update frame from now until we've destroyed our object.
We're going to just set the velocity to be vector 2.right.
So say RB dove velocity equals vector 2.ight.
The last thing I want to do is make this thing just disable itself or destroy itself when it hits an object.
So we'll add an on collision enter 2D.
And here I'll just say game object setactive false.
Get rid of that private keyword again.
And now I've got a very simple blaster shot that should just fire off to the right until it touches another object and then turn itself off.
Let's go see if it works.
So, I'll go back into Unity and we should be able to press play now and then watch our blaster shots fire off.
Let's go to the game view, press the play button, and see if we can actually shoot things.
The shots aren't going to kill anything or do any damage or anything like that, but they should just fire off like that.
They fire off to the right and they just keep going and going and going and going and going.
Eventually there you see that they got hit by the laser and turned off.
It's kind of cool.
So the laser is turning them off or hitting that other object just turned them off.
If I jump up here and shoot things so that eventually they just turn off as soon as they bump into something.
All right, that's pretty cool.
But my blaster shot moves way too slow.
So next step is to speed it up.
We're going to open up the blaster shot script.
We're going to add a serialized field at the top.
So serialize field.
Where is that at? Oh, it was already right on it.
And we'll call this is well, first we got to give it a type, which is going to be a float because we're going to want a decimal.
We'll call this underscore speed and I'll give it a default of well, we'll start with a one.
Now we'll copy that speed and multiply that times our vector 2.right.
So it'll move at whatever speed we've given it.
Now I know one is actually too slow cuz that's what it's doing already.
So, I'm going to crank it up to a default of something like three or let's even go with five.
That seems like a better speed.
I want my shots to go faster than I'm running.
And that'll give me lots of speed or lots of room to run up to 5 m a second or maybe 4.5 so that I'm not catching up to my own bullets.
Let's press play and see what that feels like.
And then remember that we can go modify it on our blaster shot prefab.
So, I can fire my shots and if that feels good, then cool.
If I feel like that's a little bit too slow though and go find my player blaster shot right here, modify this prefab and maybe turn this up to an eight.
And those shots look nice and quick.
Might be a little too fast.
Maybe like a seven.
And yeah, I think maybe let's let's try running.
So, I'm going to run towards my shots.
Yeah, I'm thinking maybe a seven or an eight.
Let's let's try running towards the shots with an eight.
Yeah, I'm going to go within a value of eight.
So, I'm going to leave an eight on my blaster shots.
I'm going to open up the script real quick.
Change the default to be the value that I think I'm going to use.
So, that way if my prefab gets reset or anything, I don't have to remember this in two places, and I don't have two numbers stored off trying to remember which one I want to actually use.
So, I'll make that match, but still leave it adjustable in the inspector.
And now the last thing I want to add to this is a way to set the direction so that it can go either left or right instead of always going to the right.
And I'm going to do that with a new method.
We're going to add a launch method.
We'll make a public void launch that'll take in a direction.
So we'll go vector 2 direction.
And this will get stored off into a direction variable.
U direction equals direction.
We'll add a field for that.
And then in our update, instead of going to the right, we'll go to the direction.
So we'll just copy direction and replace vector 2.ight.
I'm going to probably give it a default value of vector 2.ight.
So if we don't have something in there, it's just going to go off to the right.
And then we'll get rid of that private keyword as well.
So we need to call our launch method.
Now when we'll do that from the blaster since the blaster spawning this.
So we're going to go find our blaster.
And when we instantiate our shot, we'll get a reference to our blaster shot and then call launch and tell it to go in our current direction.
So say var shot equals that instantiate, which is going to return back right now a game object because the type that we have here is game object.
If I put blaster shot here, it's going to say, hey, this is an error because instantiate returns back a game object and it can't just implicitly convert it to that type.
Now, the way that we can fix this, there are two options.
We could do get component on it and try to get the blaster shot.
But if we just make the type that gets serialized here blaster shot instead, then we can actually get back that specific component.
Now that we have that component, we'll just say shot.launch.
And we want to launch in our current direction.
And we don't have a way to get our current direction yet.
What we want to do now is get that from our player.
So I'll say underscoreplayer dot direction.
and had to hit backspace there to get rid of that input that it tried to auto add.
We don't have a player stored off and there's no direction on the player.
So, let's cache our player in awake and then go add the direction variable to it.
So, copy player and right here above the player input part, we'll say underscore player equals get component and we're going to get a player, not a player input, but a player.
We'll hit alt enter generate a field and we should get that right by our player input.
I'm going to double click player, hit enter so I get a new line, and get rid of all that at the same time.
The final thing we need to do is have our player know which direction it's facing.
And we could just grab the um the rotation, the quadrian rotation from this player and then convert it.
But I want to show you an easy way that I think works a little bit better for controlling our inputs.
We're going to hit alt enter and we're going to generate a property on our d for direction.
We'll hit F12 to go to it.
And here you see that we've got a vector 2 with a public getter and an internal set.
We're going to change the set to be private.
So this is going to be a variable that says which way we're going left or right and can only be set by the player but can be read by everything else.
That's why it's public with a getter and private with the set.
So the set is kind of overriding the public part over here to the left.
Now, when we flip direction of our character, which is right down here in update sprite and animation, we could actually flip this variable as well.
Be nice and easy.
So, then it just lines up with our actual inputs so that we fire off in the direction that we're pressing, not necessarily the direction that we want to move.
So, I'm going to add some braces around our horizontal part.
And we'll say direction equals vector 2.ight if horizontal is greater than zero.
And then if horizontal is less than zero, we'll switch direction.
Equal to vector 2.ft.
We'll save that off.
And right now, this is a little bit confusing because the name of this method no longer matches what it does.
So, I'm going to take this little bit of code, the part that updates our direction.
Select it.
So, it's 155 through 164.
Hit alt enter.
And we're going to extract a method.
And I'm going to call this update direction.
Now I'm going to take this code out of update sprite and animation.
So I'll select line 155 and cut it.
Then we're going to find the reference to update sprite and animation.
So I'll click this line right here and it'll show us the references or I can hit shift F12 or rightclick on it and hit find all references.
Lots of different ways to pop them up.
Once I find the one place where it's called, which looks like it's on line 111 in the player script.
So it's oh, literally it already went to it because I double clicked it.
That's what happened.
So now that I found that line, I'm just going to add in update direction as well.
So I'll paste that right below.
So update sprite and animation, then update direction.
And update sprite and animation is actually just updating the animation.
So now I'm going to rename it to be update animation.
Delete out these extra two lines here.
155 and 156 that were there.
And now I've got slightly cleaner code that does exactly what it's supposed to do and says what it does.
It's named right.
Let's get rid of that private keyword there.
Save.
Do a build.
Control shiftB.
Get rid of all the errors.
And it looks like something added a weird using statement here.
Ah, line six blaster got a using static experimental graph view line.
I don't know what added that, but I'll hit shift delete and delete it.
We can delete all of these other unused using statements as well.
Save.
Go back into Unity.
And now we should be able to launch in the direction that we've chosen.
It's not going to flip our blaster shot around, but it should at least move in the correct direction.
Let's go test it out.
So, press play.
So, we move to the right and shoot.
Goes to the right.
And if I move to the left and shoot, my shots go to the left.
I think if I stop playing and play again, if I don't move at all, I've never set my direction on my player.
So, it's probably going to shoot.
Yeah.
Not in any direction at all.
So, we need to give oursel an initial direction on that player value.
Let's just go open up that player script, find the direction, go select it, controllclick, and then right at the end of the property declaration, we can do an equals vector 2.ight.
That's our default direction for this game.
So, with that done, I'm going to go back into Unity and we're going to commit our changes for our blaster shot that now fires in the proper direction.
Although, it doesn't quite look that way yet.
It doesn't rotate the right way, but it moves in the correct direction.
So, blaster shot script added to the prefab and it now fires in the correct direction.
No S at the end or backspace and check in.
Now, we're going to have a small challenge.
What I'd like you to do is write the one line of code that'll make our blaster shot face the direction that it needs to face.
You can figure out where you should put that code, think it through, and then do the code, test it out, see if it works, and then at the end, resume.
And let me show you my solution.
It should be very simple.
It should be pretty straightforward.
And the goal here is really to see two things.
Can you find the best place to put this code? and can you figure out what that code is? So, go ahead and give it a try and then if you need help or at the end again just resume and we'll go through.
All right, I'm going to assume that you've either gone through it or don't want to.
And now I'm going to show you the solution.
So, let's go find our blaster shot.
Oh, first let's make sure that I've saved my sandbox scene.
Apparently, I hadn't saved my scene off.
Let's go find our blaster shot script, though.
And inside of our blaster shot script, we have our launch method.
And in this launch method, we have the direction that we want to go.
All we need to do is set our transforms rotation based on this direction.
So we're going to say transform.rotation is equal to and here we want to do a check to see if direction is to the left.
So we'll say let's just do like this underscore direction double equals vector 2.ft LFT.
So if that's true, then we'll do the first value after the question mark.
And that first value is going to be quatian.
Ooiler e u l e r.
And we're going to give it the value that we want in vector values.
So the numbers that we would put into the inspector.
And if we go over and look at the inspector, let's see if we can go check that out real quick.
And go find one of those blaster shots.
Let's go find a blaster shot.
Drop it out into the scene view.
Where's our player blaster shot? If we want it to face the opposite direction, we need to flip 180 on the Y.
So, we're going to give it a zero, a 180, and a zero.
So, we'll put in zero here for the X, 180 for the Y, and zero for the Z.
Now, if it's not to the right, we just want to use the default quatronian, which is just quatronian.identity, which is essentially just the same as this with 00 0.
So, if we save that off, we should now have a blaster shot that either looks like it's going left and fires to the left or looks like it's going right and fires to the right.
Either way, it should look correct and not look weird like it's flying backwards.
Let's check that out.
So, we go in here.
We got a shot firing off.
We got another shot firing off the opposite direction.
Things are starting to look up in my opinion.
All right, let's stop playing now that challenge is done and our scene is saved.
Let's make sure we've saved the scene again.
Go to the player and override our player changes as well so we get that fire point added in.
We'll hit apply all and then we'll check in these three files.
We got our blaster shot, the sandbox, and the player preaps.
Say blaster shot faces the correct direction.
And then on a new line and say updated the player prefab for blaster weapon.
And we'll check that in.
Oh, make sure we save again.
Apparently, I had one more.
Oh, my update for my prefab wasn't in there yet.
Now, we're going to make our blaster shots actually deal some damage.
Let's get to the fun part.
We're going to open up our blaster shot script.
And in the part where we deal with collisions instead of just setting our object to not be false, let's see if we've hit a dog.
Let's first find a dog component.
We'll say var dog equals collision.
game object.get component and we're going to try to get a dog component.
So say get component, let's see if I can spell it right of type dog.
Oh, I need to capitalize my G there.
Now, this will return back a dog if we've hit a dog.
So I'll say if dog is not equal to null, then we'll tell our dog to take some damage.
So say dog.take damage.
And right now I'm just going to assume that my shots always deal one damage.
I can make that a variable amount and pass it in, but I don't have plans for that yet.
So, I'll just tell the dog to take damage.
We'll hit alt enter and generate a method on the dog to take damage.
And then inside of this dog take damage method, let's just start by disabling the dog.
So, we'll say game object set active to false.
We can give it some health, let it take damage over time and all that in a moment.
But first, let's just make sure that when we hit it, the dog just kind of disappears.
And then afterwards, either way, no matter what we hit, we should still be setting our object to false.
So even if the dog is null, we hit a brick or a rock or a player or something else, we still want to turn our blaster shot off.
Now go back into Unity.
And for this to actually work, we're going to need to make sure that we have a collider on our dog as well.
And right now, our dog is on this child object.
We're going to be moving that up soon.
Right now, it's here just for the animator for that shoot call back.
But let's add a capsule collider to the dog.
Let's move it up a little bit.
Move that offset up.
You can see the scale is all kind of wonky and weird.
I'm gonna drag it up so that it's a little bit bigger.
Let's make it a scale of two.
And set that offset to one.
And then we'll do a size of one there.
And I think I I'll just leave it right there.
So, we've got a capsule that we can shoot.
And then again, we're going to move that up and build out a better collider for our dog in a moment.
Let's go to the dog, though.
Go to overrides and apply that change.
And then I want to delete out that extra laser blast prefab that's sitting here, the laser blast shot.
Save our scene.
Press play and then shoot and see if my shot goes through.
If I can get it past that laser and knock out the dog.
Let's see.
Shot the dog.
And the dog has died.
All right, let's stop playing and let's go into plastic and say that our blaster shot kills dogs.
And we'll check that in.
So, we can shoot dogs now, but what if we want to shoot bricks or ladybugs and have them do something? Right now, I can have my shots hit them, but it doesn't really do much other than push them through the physics system.
Well, let's go back to the blaster shot and see what the initial way to do this would be and then see if we can find an alternative or better way to do it.
So, say we didn't hit a dog.
We could of course just say var ladybug equals and then do a look at that.
It auto completed for me.
Collision.gameobject.getcomponent ladybug.
And then say if ladybug is not equal to no, then ladybug take damage.
See, oh, we have a take laser damage.
Let's call take damage though.
We don't have a take damage method there yet.
So generate a method for take damage.
Then on that take damage method here, maybe we want our ladybug to use this laser.
Um, no.
Well, let me think.
No, we don't.
Let's Let's just make it die.
We'll say game object set active to false.
And then let's go to the brick and let's do the same thing on the brick.
Or let's add the same code for our brick, too.
So, we've got a ladybug here.
I'll say var brick equals and hit tab and just let it autocomplete.
And if brick is not equal to no null, then brick damage.
And here we might want to make it take some laser damage or something, but let's do that inside of the brick.
Let's generate a method for take damage.
And remember that our brick has this laser destruction time for how long it takes to blow it up.
Let's add in a number of blaster shots that it takes to blow it up, too.
Let's add a serialized field um ints to destroy.
And I'm going to set it to three so that it takes three shots to destroy a brick.
Now, I'm going to go down into our take damage method, and instead of just destroying our object, I'm going to modify our taken laser damage time or our taken damage time to be our total amount of time divided by the number of shots that it takes to destroy it.
So, if this was two, it would be, you know, half of the time of the first shot, half the time in the second shot, or on three, it's going to be one/ird of the time for each shot.
So here I'll say damage time or taken damage time plus equals and then we've got that variable for the amount of time that it takes laser destruction time and we'll just divide it by shots to destroy.
So say underscore laser destruction time divided by underscore shots to destroy.
Now we can shoot this thing three times and have it blow up.
Let's go test all of these out.
I'm going to do a build.
Control shiftb.
Make sure that my blaster shot got saved, my ladybug, and my brick.
And now I'm going to run around, play, and see if I can blow up all three different types of things and have that slightly different behavior on the brick.
Remember, the ladybug and the dog are just going to disappear on one shot for now.
And the brick is set to take three and tie into the laser damage.
Oh, lady, that guy died.
Let's go try the ladybug.
She died in one shot.
Looking good.
And these bricks.
I shoot one, two.
Oh, that one's on the second shot.
Got two shots on that one.
One on that one.
Shoot, shoot, shoot, shoot, shoot, shoot, shoot, shoot, shoot, shoot.
My shots are not working.
So, why are these shots not working? I assume that the reason is pretty simple, and it's because of the calculation here for the time that's getting added, the taken damage time.
Oh, no.
I know what the problem is.
When we take damage time over here, we're not actually checking to see if we've taken too much damage and then exploding.
So, I'm going to copy this bit of code here on line 26 and 27.
And then we'll paste it right after line 64.
So, if we've taken too much damage, we need to actually explode.
We'll minimize the brick script one more time.
Press play.
And now, I expect that my bricks are actually going to blow up when they take their their hits instead of not taking anything.
And we should probably add some visuals.
We'll add some particles and impacts and other things in a moment.
But first, let's go see that this thing actually blows up.
Let's jump.
Oops.
Let's see if I can get up there.
There we go.
That brick did blow up.
Let's try one more time though from the other side without turning on the laser just so that we can double check and see it.
It's always good to just be sure that everything is working as we expect.
So, come over here and jump up.
Shoot that ladybug.
Jump up again.
Shoot a brick.
Shoot a brick.
Shoot a brick.
Shoot a brick.
Shoot a brick.
If I could hit the same brick three times, it would be great.
All right, there we go.
I can see my bricks are blowing up after a few hits.
That looks right.
So, I'm going to go back into plastic, make sure I've saved my scene, and uh blaster shots, hit bricks, and ladybugs now.
And we'll check that in.
So, you may have noticed while we're building up this blaster shot that the on collision enter method is growing and growing.
And for every single thing that we need to damage, we're going to have to keep adding more and more code.
So, if I want to add in eight more enemies, this is going to get quite a bit longer.
If I want to add in a couple other things that I can shoot, just going to keep growing and growing and growing.
Now, there is a very good solution for this.
there's an easy way to simplify this to remove a lot of this code and make things a lot easier to extend in the future.
And again, we're going to have a little challenge.
This challenge is going to be a little bit bigger than the other ones.
What I'd like you to do is come up with the solution so that we can cut this on collision enter method down to maybe three, four, or five lines.
something really short that deals with damaging any type of thing that we want to hit and uses some special trick or some special code that we may have covered in the past or we definitely have covered in the past.
So using the same type of thing that we've used before.
So if you're not sure what that is, go ahead and just continue on and I'll give you some clues.
But if you have a good idea, you got something in mind, you think that you know what to do, go ahead and try to solve the problem right now and then continue on.
If again, if you need a couple clues, I'll give you some of those and then we'll dive into the solution.
All right, I'll assume that you either are ready for clues or want the solution.
Let's start with a couple of clues.
Remember when we wanted to deal with lasers and we added a I take laser damage event or interface? This made it so that we could damage multiple different types of things.
We've got three references to it.
We have one on our ladybug or there's two types of things.
One on our ladybug and one on our brick right here.
I take laser damage.
This defined a method that we could call and then we use this from our laser.
Our laser looks for things that you implement I take laser damage.
Let's see if we can find that right here.
And then tells them to take laser damage.
So with that in mind, continue on.
see if you can find the solution.
All right, it's solution time.
What we're going to do is create an I take damage interface.
So, I'm going to create a new script.
Call this I take damage.
We'll open it up.
And it's going to have a bunch of stuff in it that I don't need.
So, I'll delete out everything except for the word I take damage.
So, say public interface and I'll paste in I take damage.
We'll add a void take damage method that has no parameters and returns nothing.
save and then copy I take damage back onto my clipboard.
I'm going to go to the blaster shot and in the blaster shot instead of finding a dog, I'll find an I take damage and then I'll delete all of the code for the ladybug and the brick.
I'm going to replace the word dog with damageable and then get rid of these braces because I don't need them.
Now, we're down to three lines and all I need to do is add the I take damage interface to my three different classes.
my dog.
So, I'll add it right up here.
And we'll make this word public instead of internal because the interface needs it to be public unless I mark it as internal in there.
But making it match and making it public matches with everything else I've done.
So, we're going to do that.
And then we'll go back to the brick.
We'll add the I take damage.
So, we add a comma after the other interface and I take damage.
And again, we're going to have that problem of it saying internal instead of public.
I'll just replace it with public.
And then the final one is in the ladybug.
Well, again after the I take laser damage, paste in a comma or put a comma and then I take damage and then just go make sure that this says public and not internal.
I'll save.
Do a build with control shiftb.
Make sure all those little stars disappear.
We'll press play.
And now we'll have a much more generic, a lot easier to extend way for us to take damage or to make things take damage.
Let's shoot.
The dog takes damage and dies.
Let's go kill this ladybug here.
She takes damage and dies.
And if I blast these bricks, they still take damage and die.
But I don't need to modify my blaster shot script anymore.
When I want to add in new objects, I'll just make them implement that I take damage interface.
Let's go to the plastic and add our notes that we've added the I take damage interface and check it in.
It's time to add explosions.
We're going to add an impact particle when our projectile lands.
So, we're going to take that blaster shot and whenever it hits something, we're going to spawn one of these explosion blue prefabs.
Let's drag this out and see what it looks like.
You can see here it's kind of huge, but if I press play, it does this neat explosion effect.
Let's watch it real quick and then we'll figure out a size that looks better.
So, that's cool, but way too big.
If I scale it down to about 0.25, though, now it looks about the size that my blaster shots were at.
So, I'm going to pick that as my size that we'll use.
I'm going to go down to my explosion prefab and change it to 0.25 and 0.25 on the X and the Y.
The Z doesn't matter because it's completely flat.
As long as it's not zero, it's fine.
So, I'm just going to leave it at one.
Now, we need to go to our blaster shot and make this thing spawn one of these explosion objects.
To do that, we'll open up the blaster shot script.
And in the on collision enter, we're just going to instantiate a blaster explosion or an let's call it an impact explosion.
So say var explosion because we're going to do something with it afterwards.
Equals and we want the instantiate method.
So we'll call instantiate and we'll give it a name of a new field that we're going to create.
And what did I say we're going to call this? Impact explosion.
And then we're going to spawn this at the point of the collision.
And so we don't want to use our projectiles position.
That's like the center of it.
We want to use the collision contacts.
Let's see if I can spell contacts right, not contracts at zero.
So the first contact and we want the position or the point of that.
And then the final thing we need is a rotation.
We'll just use quatronian.identity.
Add the semicolon at the end.
And now we need to create an impact explosion field.
So, I'll hit alt enter and generate a field.
Got to go down to variable and choose field.
Hit F12 to go to it and I'll replace private with serializ field.
There we go.
I'm going to cut it and move it up by my other serialized field and put game object instead of object so that I can add a serialized game object or my explosion.
I'm going to save.
And then I did mention that we want to do something with this explosion because once it spawns, I do want it to kind of kill itself over time.
But uh let let's spawn it for now and then we'll take a look at that next.
First, we'll go into Unity.
We'll go find our player, which has our blaster on it.
Make sure we got everything selected.
There we go.
And then I'm going to go select um my prefab for my blaster shot.
There we go.
That's what I was really looking for.
I could have just gone down to the prefabs folder.
So, we'll find the player blaster shot and we're going to assign the impact explosion.
So, I'm just going to drag the impact explosion over there like that.
Press play and let's start shooting things.
So, we play and shots hit.
And you can see my explosion got there, but it's just repeating over and over.
Let's go shoot a couple more things.
I shoot that.
Shoot a couple more shots out there.
And every time a shot lands, we're spawning these these explosions.
But the explosions just keep playing over and over and over.
So, we've got to make these explosions disappear or go away.
And the quickest way to do that is going to be right after we do the instantiating.
We can call the destroy method.
So, we call destroy.
And we need to pass in not the explosion, but the explosions game object.
And then another field for the delay or the amount of time that we want to wait.
Now, I know that this explosion ends at about 1 second.
So, I want to be a little tiny bit less than that cuz I know that if I put in a one here, but I get a little flash of that extra bit of particle.
So, I'm going to put in a 0.9 and a semicolon.
Now, if that number doesn't work, I can always just come back and change it.
But, let's try that out.
Got it at a 0.9.
What's going to happen now is we'll spawn this projectile or this explosion when the projectile lands.
And after 9/10 of a second, we'll destroy the object.
Let's go back into Unity, press play, and start blasting stuff.
See if we get a cool explosion that shows up visually, but um doesn't uh stay around and doesn't keep looping.
There we go.
Looks like it worked.
That one is not destroying cuz nothing is set to destroy.
That's just placed in the world.
Let's go shoot a couple more things.
Hit that guy.
You can see that my projectiles are landing, the shots are spawning, and they look right.
They're not uh they're not repeating or doing anything strange.
So, I'm going to stop playing, make sure that I've saved my scene, go into plastic, and say we added our initial explosions on impact.
And in just a moment, we're going to actually start to talk about some of the performance characteristics of what we've just done and how we can improve upon that as well.
So, get ready for that.
But for now, let's check in our changes.
Now, I want to bring our second player back in.
I've got my controller here.
We're already in play mode, so I'll hit the button and try to join in once I give the window focus.
There we go.
I've got my character here, and I can jump them around.
Looks like they're both working fine.
Let's shoot, though.
So, I blast and look at that.
My shots are able to hit each other.
I'm going to shoot the other robot with this controller.
And yeah, my shots hit him as well.
So, I want to make a couple little changes here.
I want to make it so that our blaster shots can go through each other so that we can help each other and take out enemies.
I also want to go away from the split screen mode.
Split screen's pretty interesting and it's easy to set up.
But the mode that I'm thinking is more like a Cuphead where we're running along blasting and shooting stuff and I want to get into that side byside view where the camera is automatically adjusting.
So, we're going to make a couple of changes to make both of those things possible so we can have a nice fun faster pace sides scrolling game where we're blowing up and blasting lots of different things.
Let's start by making our projectiles go through our players and our players go through each other.
To do that, we're going to go to edit and go to our project settings.
And we'll start by going to physics 2D and just unchecking player and player collisions so that our players can run right through each other.
Now, if you're on the physics tab and you're scrolled down, there's also a player and player.
That's not going to help here.
it won't work and you're going to get some well unexpected behavior of the collision still happening.
So here we've got player and player unchecked.
I'm going to move this away.
Press play and I should now see that my players no longer run into each other.
Let's check that that's the case.
So we press play and I run right here and I can run right through my other character.
All right, that's looking pretty good so far.
Now we need to make it so that our projectiles do the same thing.
And to do that, we can just go find our projectile prefab, go find our player blaster shot, and change the layer right here to be on the player layer.
I'll hit yes to change the children.
Let's press play again.
And when we start shooting, our shots should go right through each other.
Let's see.
Got to get our character in.
There we go.
We run over here, we shoot, and my shots go right on through them, just like I expected.
Now, we could have added a separate layer for our player shot, but there's really no need for it right now.
We just don't want our blaster shot to interact with the exact same things that our player shouldn't interact with.
If we have to change that matrix, we have to modify it later, we need to do something special for the blaster shots versus the players, then we can always split them out.
But there's no need to now.
No reason to make it overly complicated or add any extra confusion there.
So, let's stop playing.
Let's save our project and make sure that our prefab is updated and then go into plastic and let's first in or update and check in our blaster shot.
So, we've let's see made players and blaster shots not collide with each other.
Got a nice simple commit.
We'll check this in and then dive into cameras.
Now, we're going to disable our split screen setup.
I think split screen's cool.
It makes a lot of sense for some types of games, but what I want to build doesn't work with split screen.
So, we're going to disable it and allow ourselves the ability to reenable it pretty easily if we decide we've changed our minds later.
So, let's stop playing.
We're going to go find the player prefab and open it up.
Underneath the player prefab, we have a main camera and a virtual camera.
And these are the two objects that we use for doing our split screen setup.
I'm going to right click or select both of them holding shift and leftclick.
Right click then and hit create empty parent.
I'll name this object by hitting F2.
Split screen camera.
And then go back out of or no, not going to go back out.
First, I'll uncheck it to disable it so that my split screen camera is off.
And then I'll go back out of prefab edit mode and save.
Now, my camera view is going to be completely black.
My game view shows nothing.
And the reason for that is I no longer have a camera in my scene.
So, we're going to create a new camera.
We're going to create a new Cinem Machine camera.
And we want to go with a target group camera.
This target group camera is going to follow our player or players and lock onto them and also show enemies or other points of interest that we might want to highlight.
Let's hit the plus button on the target list here with target group camera selected and then drag our first player in.
Still nothing shows.
The reason for that is if we go to our Cinem Machine brain, there's no camera attached to it.
When we had our player and underneath our player, if we expand it out and expand out the Cinem split screen camera, look at the main camera object here.
There's a Cinem Machine brain, but there's also a camera here.
a camera that's set to orthographic mode with a projection size of five.
So, let's go add one of those to our Cinem Machine brain down here.
We'll hit add component, add a camera.
We'll set the projection mode to orthographic and the size to five.
Now, we're going to go take a look at that virtual camera.
In the virtual camera, we've got two parts for our tracking.
And we've got the body and the aim.
The body is going to move the camera around to keep things in line and the aim is going to tilt the camera.
We don't want any tilting happening.
So, we're going to change aim to do nothing.
We're in a 2D game.
We don't want to be tilting around or anything.
And we're going to change the body to be framing transposer, which is the transposer that you want to use for a 2D orthographic game.
It's going to keep the objects in view by moving the camera in and out physically.
It's going to just move it away back and forth.
Now, if we look down in the corner, you'll see that we've got a minimum ortho size, and this is the furthest away or the closest that it can get.
Remember, one is really, really close.
That's what you're seeing here.
And if we put it up to about a five, it's going to be right at what our camera was at before.
So, now we've got a tracked camera that should follow this character around.
Let's press play.
And we're going to see that so far we don't really have anything new.
We should just have our camera working for player one and probably completely broken for player two.
So, there we go.
I can run around on player one.
Seems to track fine.
I can run, jump.
Everything's going okay.
And if I join in on player two, well, player two is no longer visible.
They can just run off screen.
So, let's add player two to the target group.
I'll select my target group, hit the plus button, and go find our second player.
Where are you, player two? There you are.
I'll drag player two in there.
And now I've got two players being tracked.
Let's run around.
And you can see that both of my players are tracked.
And right now, we've got absolutely no limits on our distance.
I think we've got the max size to 5,000 or something.
So, we can get pretty far away.
Obviously, I think this is a little too far.
I'll add some restraints later or constraints later.
But for now, I like that it's able to track and follow my players, but I don't like that I have to drag these in because that's just not a realistic option.
I can't go dragging players into a target group every time.
So, what we're going to do is have our player automatically add themselves to the target group.
And then we'll figure out a more advanced target group filtering system later when we have some other things to add into there.
Let's start with the player though.
We'll go into our player script.
And when we enable our player, let's just find the target group if there is one and add oursel to it.
So, we're going to go right below our awake method and add an on enable.
In our on enable, we'll just search and find the object of type that is the Cinem machine target group.
Did that find it? Did I type it right? Let's see.
There we go.
Now, if you don't get it autocompleting, make sure that you add the using Cinem Machine statement up here.
That automatically added when I typed it out and hit enter.
That's why it went from black to blue.
If it doesn't happen and you don't see that, if it looks like this, then just go up here and add that statement using Cinem Machine manually if you can't get it to add automatically.
Now, if we find that object, so we're going to put a question mark dot.
If we find it, we're going to add a member, which is going to be our transform.
And then we need to give it a weight, which we'll put in a one, and a radius, where we'll just put in a one.
We'll put a semicolon at the end.
And then we're going to add an on disable.
And remember real quick that this question mark is going to make sure that we only call the ad member if we find a Cinem Machine target group.
If we don't find one in our scene, this code behind it won't get called.
So we won't get an exception or an error saying, hey, we couldn't find a target group.
All right, let's go add an on disabled.
Before we do that, though, I'm going to delete my private keyword.
Go to the end of line 56.
So I just go down and hit the end key, hit alt enter and hit use expression body methods to shorten this up and make it into a oneliner.
Then I'll duplicate it with control or command D and change the enable to disable.
And then we'll instead of adding a member, remove a member.
We don't need the two parameters after the transform.
So we'll just put in the transform and remove those two after the the first comma.
We'll save and do a build.
And now our player should get automatically added and removed from that list as they enable and disable.
Let's see if that works.
So we press play and our first character's here.
Our second character comes in.
We run around and it looks like everything is tracking.
Let's go take a look at that target group.
One thing to note is that our first player is actually in the target group twice.
Um that's just because we had them added manually and then they're adding themselves again.
So, it does get double added.
That's something we can address later, but as you can tell, it's not actually causing any real issue.
We still have both of our players tracked perfectly fine.
All right, let's stop playing and let's save our scene and then we'll commit this into plastic before we start working on having it set up for our other scenes.
say that we've added split or added um multi-player target group view instead of split screen and we'll check that in.
Now that we've taken split screen out, if we open up level one or level two, we're going to see that we have no camera around.
So, we need to add our camera setup to our other scenes.
And first thing that we're going to do is turn it into a prefab.
We have this Cinem Machine brain that has the camera on it and the brain component, the virtual camera and our target group that right now has a player assigned to it.
Let's select all three of these objects, rightclick, and add an empty parent by choosing the create empty parent.
I'm going to call this um multiplayer camera setup.
And then I'm going to drag that into my prefabs folder.
Now I've got a multiplayer camera set up that I can add to my other scenes.
So I'll go into level one.
I'll make sure that I save my sandbox scene.
Go to the prefabs folder and take out my multiplayer camera.
Now I can see it in here.
I'll save that and I'm going to go into level two as well and just grab that camera in so that I've got the same camera setup for both of them.
Right now I could of course have a different camera setup and that's something that happens very often in games.
So, we'll have a slightly different camera setup for each different level, but base them off of a single prefab.
Let's go back into the sandbox scene, though, and do a little bit more work.
So, we've got our multiplayer camera set up.
Let's press play.
Make sure that it's all working with the prefab that we're able to track both players.
I've got my controller right here, so I should be able to jump in any second.
All right, so run over here.
Run over here.
And things are tracking.
Oh, Steam popped up.
Let's run over here again and let things track.
It looks like my characters are tracking just fine.
I can get nice and far away and uh I can blast that guy.
It's looking pretty good.
So, now that that's working, I want to stop playing and I want to go into level one and test out level one.
Let's press play here and then we'll add in our second character.
And I'm going to run over player one to the right.
Go grab those coins.
Keep them running.
Keep them running.
Come over here by this frog.
And notice that we're not hearing any frog sounds.
And the reason for that is pretty simp.
Oh, it's pretty simple though.
The reason was that player one wasn't playing the sounds.
It was only the most recent player because I have multiple audio listeners.
And if you look at our log, you'll even see there are some logs like this where we've got multiple entries, one per frame saying that we have multiple audio listeners in the scene.
And what's going on is that each of our players, if we look at them, has this listener object on it.
If we select it, we've got a listener right here.
So, they're both trying to listen at the same time.
And only one can actually listen.
So, only the most recently added one is actually going to pick up any sound.
So, we need to stop playing and change our audio setup just a little bit.
We're going to remove the audio listener from our player and put it onto our camera setup.
Let's go into player prefab edit mode.
remove the audio listener.
I'll just right click and hit remove component.
Go back out.
Hit save.
And I'm going to go find my multiplayer camera setup and expand it out.
And on the virtual camera brain.
So, this is the object that's following or that's that's being moved around.
This is where the camera is.
We'll add an audio listener.
Audio listener.
There we go.
We now have an audio listener component.
We'll add that to the prefab, though.
So, we're going to go to overrides on the prefab and hit apply all.
see that it's got the little plus saying that we've now modified this on the prefab.
We're hit apply.
And now if I go into any of my scenes, that should Let's hit save.
Then we should see the audio listener is on that child right there because we applied it to the prefab.
All right, let's go back into level one.
We're going to press play and we're going to see first if that error is gone.
So let's see.
The multiple audio listener error is not there.
I add in a second player.
It's still not there.
Let's run over here, grab some coins.
Remember, the coins don't have positional sound on.
Go over by my frog.
And I still don't hear anything from him.
Now, let's get the other player over there.
And we'll listen some more.
And notice that we still don't hear anything.
The reason for that is if we go to our camera, let's go find our multiplayer camera.
We go find the Cinem Machine brain here.
We're going to go into 3D mode and hit F.
And look at the position of this camera.
Right now, it's at -11 because it's moving out and it's moving away.
So now our positional check that we were using here for the frog where we had that range of what was it 10 m away on the audio source.
Where did we put that uh on our 3D sound settings? Yeah.
On our max distance of 10, that's no longer in range.
So if I crank this up to a 20 Let's see that.
Now we can start to hear it because it's actually kind of pulling out.
And if we get closer together so that we're closer to the character or this guy, it should be even louder.
And I can run away, of course, and stop hearing him eventually.
But for now, I'm going to stop playing, save our scene, and then we'll commit our changes.
Let's make sure that we've got that frog's max distance cranked back up to 20 so that we'll be able to hear him when we get somewhat in range.
We'll save our scene, go to plastic that we added, multiplayer camera setup, and we'll check our changes in.
It's time for us to start talking performance.
Right now, we have two players in our game that can shoot an unlimited number of bullets that just keep flying around forever.
So, we can see that bullets are flying.
I can look over to my left side in my hierarchy and see new shots going off constantly.
And when shots land and hit things, I can see that I get a shot that appears and disables itself over time.
Now, right now, this isn't going to cause any problems.
I can run around, shoot many hundreds of times, and my game's probably going to run fine.
But eventually, it's going to slow down.
Depending on the system, the problems are going to come faster and faster.
If you're on a mobile device, they're going to come much, much quicker than if you're on an extremely high-end development system.
But let's make it a little bit easier to reproduce the upcoming problems that we're just about to solve and to view them in the profiler.
We're going to stop playing.
And what I want to do is open up our blaster script.
We're going to go find the blaster on our player and we're going to make a quick modification.
Instead of firing when we pull the trigger down, we're going to fire every frame that we're holding the button down.
We'll do that by going into our update method.
And I'm just going to copy line 17 up to the dot part, everything up to the end of the fire in the braces and paste it in here.
I'll put that inside an if with some parenthesis.
And it'll say if that get or no it's read sorry I lied read value and it's of type float not get it's a read value we're going to read a floating point value that's going to be 0 to one if it's greater than zero then we're going to try firing or just do a fire so we'll just try fire and we don't have an object or a context a callback context to pass in so we're just going to pass in null.
Actually we can't even pass in null.
we're going to have to pass in a new call back context.
So instead of doing that, we'll just take this line here, 22 and 23, and we'll add some braces and paste it in.
A lot better than calling it and creating a new context.
We don't want to start causing other issues.
So there we go.
We've got our launch code inside of the update.
And I'm going to comment outline 17 so that we don't ever call try a fire.
We just call it in update right now.
And we're again going to call this every single frame where we're holding the button down.
So we can spam out shots and then take a look at the performance characteristics of that and see how we can optimize it.
So let's jump back into Unity.
Now we're in play mode and let's hold the button down and look at those shots start firing.
I'm going to get my other player in, hold this trigger down, and look at all those shots go blasting off.
Lots and lots of firing.
So what's the issue? Well, if I hold it down for long enough, eventually I'm going to start to see my frame rate dip.
But like I said, that's going to probably take quite a while on this system.
It's got a lot of memory and a very, very, very beefy CPU and video card.
So, it might be pretty difficult for me to see the slowdown just shooting these, but I can see that the frame rate is starting to drop.
It's going down into the 20s and 30s.
It was in the ' 50s and 60s a moment ago.
Let's take a look at the profiler though to see this data I think even quicker and a little bit more visual representation of what's going on.
If we go to window and we go to sequencing, no analysis right below sequencing and go to profiler, this will pop up the full-on profiler window.
This may or may not be docked.
I'm going to grab it and just dock it down below right next to our console.
I'm going to drag it up just a little bit once I've got it selected and make it just a little bit bigger.
Now, if you scroll down here, you see that there are actually quite a few different profilers.
It starts with the CPU one that shows just what our CPU usage is and shows us each thing that we're running each frame.
So, it'll tell us what thing took the most amount of time.
If I go through and sort by time, I can find each frame and see that well here we're actually getting a little bit of work in the physics 2D fixed update.
That's actually taking 9 milliseconds.
And if I scroll through, you can see that the time on that.
It looks like it might be going up, but it's a little bit hard to Oh, there's one where it's at 18 milliseconds, which is really, really high for a single colon there.
But let's scroll down and see the part that I think is more interesting and even more apparent.
If we go to memory, and then we choose this option to see the current frame and then unpause, we can actually see the memory allocations live.
Well, let's go back to that profiler tab.
Drag it.
If I could click and drag, this would be a lot easier.
We can actually see the allocations happening.
If we look down here at the other, we can see how much memory we're using with our own objects.
And if I just start holding the buttons down, watch as those memory allocations just go up, up, up, up, up, and up.
We're going to keep eating up more and more RAM, and eventually our game is going to blow up.
We'll run out of system memory or something else or the whole thing again is going to slow down.
Ah, look at that.
But we can see our our performance is actually dropping quite a bit now even on this high-end system.
So we need to do something about that.
We've got to fix the problem.
Now one solution is just to destroy all of those objects that were appearing and have them get kind of cleaned up instead of disabling them.
So let's go through that next.
Let's open up the blaster shot script.
See if I can find my blaster shot.
There we go.
And instead of disabling our game object here on line 40, let's destroy it.
We'll say destroy.
and we'll pass in our own game object.
Now, we'll add a semicolon at the end, and this will immediately destroy our object.
So, we shouldn't end up with all of that physics work that going on.
We're just going to have all of our objects being created, landing, hitting, and then getting destroyed.
It also should reduce the amount of memory that we're using because we're not going to keep those objects around.
We're going to create them, and then destroy them.
That does, however, cause one other issue, which is going to be memory fragmentation.
Let's check this out, though.
We'll press play and in just a second, we should be able to get our player in here, start shooting, and look at the memory usage.
You see that it's going oh about the same.
It's going up a little bit.
It's going to drop a little bit.
Let's shoot some more.
And look at the memory usage staying right around what is it about 410 412.
It's no longer doing that skyrocketing and kind of going up up up and away, which is what it was doing before.
Also, our performance isn't dropping nearly as fast.
Let's face the other direction, though, just so we can get more more shots going and staying around for a little bit longer.
But what and that's another thing to note.
Once we shoot off to the left, our shots aren't getting destroyed.
So, we need them to actually self-destruct as well.
So, we'll stop playing and we'll add in one more bit of code in here to our blaster shots to make them self-destroy after some certain amount of time.
So, we'll go up into our awake method and right after we launch ourselves or right after we get created, let's just say destroy and we'll destroy our game object and then we'll give it a delay of some maximum lifetime.
I'm going to make that a variable and call it underscore max lifetime.
And then we'll generate a field for it.
Alt enter and go down and generate a field.
F12.
We'll go back, replace the private with serializ field.
And then I'm going to cut this line with shift delete and move it up and paste.
So we've got a max lifetime that needs a default value.
I'm going to give it a value of 4 seconds.
So that after 4 seconds, our object will automatically destroy even if it hasn't hit anything.
Let's go check that out.
And now we should be able to see that our memory usage won't go up even if we're shooting off to the left where our shots just go off forever and ever and ever.
Let's see.
So we press play.
We'll face to the left, keep shooting, and our hierarchy should also stay about the same size instead of growing indefinitely.
So, let's check it out.
We aim to the left and shoot.
And I'll come in on another player.
Aim to the left and shoot as well.
And we can see that the hierarchy, it's growing a little bit, but eventually it's going to stop.
And see that the size of it isn't changing anymore.
And you can tell just by looking at this that the size isn't changing.
Now it's shrinking and growing again up until I get however many shots it is that I can fire over 4 seconds out.
And once those disappear, as we can see, they'll start kind of cleaning up out of the hierarchy and disappearing.
And then eventually they're all gone.
If I go to the scene view and go to 2D mode, let's see.
We can actually zoom out and watch the shots disappearing.
Let's do it from just the other player.
So watch the shots from this player going out.
And you see that over time once they live for 4 seconds they end up disappearing and that's why our hierarchy ends right about here and our memory usage is kind of peaked or capped right there.
So this is working.
This helps a little bit but again it does cause one other problem which is our garbage collector is going to be working overtime because we're constantly creating and destroying objects.
Now on W