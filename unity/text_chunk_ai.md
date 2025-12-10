r available attack points that we have.
And we're going to fill this by grabbing it from our spline attack points.
Let's do that in the start method.
We'll add a start.
I just deleted it, but we'll add a new start.
And inside that start, we'll add a method called refresh attack points.
This is going to give us a new queue, a new set of all of our attack points available that we can start just pulling objects out of.
We can start pulling them out one one after another.
We could use um a list or an array or an index as well.
I just felt like using a Q this time.
So, we're going to put them into a Q and then just pull from there.
So in our refresh attack points, we'll say underscore attack points equals and we'll give it a new Q.
And we're just going to pass in our or actually let's get this directly from let's get this from the spline attack points.
So we'll say attack points equals spline attack points.get as Q and then we'll generate a method to get that back as a Q.
So select the get as Q, hit alt enter, generate a method, and then here we'll return a new Q and pass in our attack points.
What this will do is give us a new set of all of our attack points in just a collection that we can pop and pull things from until it's empty.
Again, we could use integers and an array based thing, but I want to show one other slightly less memory optimized way to do things as well.
So, we've got our attack points here, and the first thing that we're going to need to do is grab the first attack point out of there, and make that be our next attack point.
So, we'll say underscore next attack point equals attack points.
DQ.
That's going to pull the first one right out of that list.
Now that we've got our next attack point, we can just check in our update to see if we've passed that attack point.
If we have, we can fire off an attack and grab the next point.
If we haven't, then we don't really have to do anything.
So to do that, we're going to need to figure out how far along the spline we are.
So we'll say var elapsed equals, and we want to get this data from our animator or our spline animate script.
So we'll say spline animate, and there's a normalized time on here.
This will give us a value of how long it's gone all the way across.
So it'll be zero at the beginning, one at the end, but on the second loop through, it's going to be two, and on the third loop through, it's going to be three, and so on.
So if we want to go halfway through the second loop, that would be at 1.5.
And we really want a value of 0.5.
We're not storing all of the every loop value in our attack points.
We're just storing the 0ero to one value.
So to do that, we'll use the modulus statement or the percent and a one.
That's going to get rid of everything before the decimal point and just give us back the decimal for how much is elapsed.
Then we'll say if elapsed is greater than or equal to our next attack point, well then we want to do an attack.
So we'll tell our animator to set its attack trigger.
So say set trigger.
And remember we named that attack.
And then we want our next attack point to be set.
But we only can set that if we actually have attack points available.
So we'll say if_attack points.
Make sure that we add the using system.link statement up there.
automatically added for me here.
So if we have attack points, then we'll say next attack point equals attack points.d dq.
And if we don't have any, so we'll say else, well then we should probably refresh our attack points and just get some new attack points.
Let's get rid of those braces.
Save and do a build.
And now we should expect to see our fish playing his animation.
Let's go check it out.
Of course, first we'll need to add the fish script and then assign our references like the spline animate, our animator child, and the spline attack points that we're going to be following.
We'll save and press play.
And here we go.
We can see our fish swimming along.
Let's watch him animate.
See, he does his animations, but there's a little bit of a delay there, too.
One thing we want to make sure that we don't have is the has exit time checked for this animation transition.
We want to make sure that he does the transition immediately.
It doesn't keep getting reset back out of it.
Now, the final thing to do is make our fish actually shoot.
We can see here that he's got an animation event that's firing off and nothing listening to it.
If we go look at our animation, let's go find that attack roll fish animation real quick.
Go to our animation window, select the fish, and go to attack roll.
Let's move this animator controller out of the way.
You can see that we've got an animation event right here, which is, I believe, right at the point where he's Let's stop playing.
Right at the point where he's doing the actual attack, where he does that kind of a spin move where he should actually be firing it off.
So, it's right there.
So, let's hook this up to an attack.
And remember, we have that shoot animation wrapper.
So, we'll go to our base object here, add the shoot animation wrapper, and then we can select our animation and just go find shoot animation wrapper methods shoot to call that shoot, and then pass it up to our fish object.
We'll go up to our fish now.
And then in our start method, we can just register for that just like we did with the other ones.
Say get component and children shoot animation wrapper.onshoot plus equals shoot spikes.
And then we'll generate a method for it.
And here we'll say debug.log shoot spikes.
Let's save that off.
See if our log entry comes.
And then in the next section, we'll add our spikes and finish up our fish.
First, we want to make sure that he's actually trying to fire off and the animation is all working properly and everything's hooked up.
Let's go check it out one more time.
There's our fish reloading as domain.
Go back into the scene view.
We see our fish doing a spin and he's calling shoot spikes.
Looking good.
Let's stop playing.
Go into plastic and commit.
Fish is ready to shoot spikes.
And I'll check that in and save our scene.
Okay, let's try checking that in one more time.
There we go.
To let our fish shoot, we're going to need to give him a weapon first.
So, let's go find the spike that came with him, the bullet spike object, and just drag it right out into the scene.
We're going to set this one up to be his projectile.
We'll add a rigid body 2D first so that it can go flying around.
We'll leave all the settings on default for now.
And then we're going to add in another component that's going to be a collider.
So, we're going to need to find a collider 2D, but we want a polygon collider that'll allow us to make a collider that kind of matches up with our actual sprite.
Here, I'm going to modify this by going into edit mode.
If I expand out the polygon collider, I can hit the edit mode.
And you can see the green lines appear nice and bright and click on the points and drag them right to where I want.
I want one point there, one about there, one about there.
I'm going to pull this one in just a little bit.
And then I'm going to delete out those extra two points that I've got down here, the two at the bottom.
So, I'll go select element three, hit delete, and select element three again.
Hit delete one more time.
Ah, looks like my elements got rearranged.
That's okay, though.
I'm just going to drag this point right back over there.
I've got a nice little triangle that should work well for my collider on this spike.
I don't want it to go over the edge.
It's just kind of staying right inside.
I'm going to make sure that that's saved off.
So, we'll go to our bullet spike prefab.
Scroll up to the top.
Go to overrides and hit apply all.
And now we need to add this into our pool manager.
If we go to our game manager and pool manager, remember we've got a pool for our blaster shots, our explosions, and our cat bombs.
Let's expand out the code a little bit more to also handle things like well our spikes.
To do that, we're just going to take our catbomb pool right here and duplicate it.
We'll call this a spike pool.
So, we're going to create a class called Well, maybe we don't even need a spike yet.
Let's just start with a return to pool and we'll call this underscore spike pool.
Now that we've got that, we should be able to copy all of the other places that are using catbomb pool.
So, we'll just find them all.
We hit Crl + F and hit enter to go to the next spot here.
Looks like line 37 where we initialize it.
We'll duplicate all of those lines.
So I'll select them all.
Ctrl D.
Left arrow.
Enter.
Enter.
And then we'll paste.
So we've got our spike pool is going to be an Iobject pool.
That was our type.
Oh no, it's an object pool, not an object pool of return to pool.
Oh, here I've got my type in the wrong spot.
There we go.
That's what we're looking for.
an object pool of type return to pool.
Now, we don't want to return or instantiate a catbomb prefab.
We want a spike prefab.
And then we're going to want to add in the spike pool as its pool.
We'll have it return back out the shot, which seems right.
We just need to generate the spike prefab as a return to pool object now.
So, let's generate the field for it.
Make sure that it's right up here by our other prefabs.
So, I'll move that up.
Control shift alt and move my lines right up here.
And we'll call this a return to pool.
Not spike pool, return to pool.
So now we've got our spike prefab right below our cat bomb prefab.
We've got our spike pool right below our cat bomb pool.
And we've got the instantiation of our spike pool right below the instantiation of our cat bomb pool.
The next thing we need is just a method to get a spike.
So we'll add a public spike or return to pool because we haven't given this a class yet.
call it get spike and we'll return back out the spike poolool.getit.
That's all we need.
We'll generate our code or do a quick build, not generate our code with control shiftb.
And then we're going to need to go into the editor and actually assign our spike.
So, first thing we'll need to do is go to our bullet spike here, and we're going to need to add a return to pool script.
And then we're going to need to assign that.
So, we we'll make this into an a prefab.
We'll apply our prefab changes.
Get my words there.
Hit select to go find that prefab.
Then we'll go find our pool manager and add in the bullet spike right there.
And then apply our pool manager prefab as well.
So that applies across all of them.
Now we've got a bullet spike that we should be able to spawn and instantiate in our attack method.
Let's go back to our shoot spikes method now and instead of doing a log, let's instantiate a bullet or a spike.
We'll say var spike equals pool manager.instance.getspike.
And then we'll just set that spike's position to our current position for now.
So we'll say spike set position or spike.t transform set position and rotation.
We'll set it to our position and um let's just use a default rotation right now.
So we'll I think our our just use quatronian identity.
We're gonna set rotations in a moment so that we can do a bit of a spread.
But this should give us a spike, just a single one facing up.
Let's go try it out.
All right, here we are with our fish ready to shoot.
But I think I want to delete out this first attack point before we do.
So, let's go find on my spline attack points.
I've got this one at element zero.
And I think if I go in here, can I delete this element array? Let's see.
Ah, there we go.
Right clicking deletes it.
And now I've got got rid of that.
I should be able to press play.
Oh, do a little cough.
And let's see if our spikes start spawning at the attack points.
There we go.
You can see spins, does a little spawn of a spike, does a spawn, does a spawn.
So, I think I might want to move those attacks forward just a little bit because the attack animation is so slow, too.
But that's looking good.
The last step will just be to launch those things up.
Now, let's modify our shoot code to launch out multiple spikes.
We're going to add a loop.
We'll do a for loop and we'll go from one to let's call this underscore spike count.
I'll generate a field for that and I think I'm going to default it to a value of five.
So we'll get one spike up and then two off each direction off to the side.
Now we're going to inside of that loop do our spawning and setting position.
So I'm just going to move those up into the loop.
Let's cut and paste.
But the position or the orientation is going to vary based on which spike it is.
If it's the one, the first one, I want to go kind of like off to the left and then a little bit more straight and then straight up and down and then to the right and then more to the right.
So, we're going to need to get that angle.
We'll say var angle equals and here let's get we'll use I minus and we want to use half of our spike count.
So, spike count divided by two.
So, we'll start off with a a negative number and then we'll go up to a positive number that's halfway the bottom of spike count and then halfway above or halfway to spike count.
So, we'll get a negative 2, a negative 1, a zero, a one, and then a two.
Those are the values that we should expect to see.
Next, we want to use that and multiply it by some um spread offset.
So, we'll say var um offset equals spread time angle.
We'll generate a variable for that spread.
Let's call this underscore spread.
And we'll make that a serialized field.
I'm going to set this to oh 15.
And we could use floats here, but I'm just using ins to keep things somewhat steady on my um my angles and and values there.
It could be a float, though.
There's no reason for it to necessarily be an int here.
So, we've got our offset now.
Um, and then we need to give that some like base origin.
So, zero would be off to the right.
And we're probably going to want to go, you know, off to the or start at like a 90 or a 90.
So, we'll say var final angle equals or underscore origin, which we'll make a variable plus offset.
We'll generate a field for that origin as well.
And we'll just leave that at zero for now.
We'll be able to adjust that inside the inspector.
Now that I've got my final angle, we'll use quatronian oiler.
We'll give it a zero for the x, a zero for the y, and then pass in our final angle on that Z so that we're rotated the right way.
And then we want to oh, need to add that closing parenthesis there.
And we also want to give some force to our spike.
So we're going to say spike.get component.
And we'll get the rigid body 2D.
And we're going to set its velocity equal to its right direction.
So sprite spike.t transansform.right times some fire speed.
So let's call this a fire speed.
And this be how fast it's going to actually launch it.
We'll generate a serialized field for that as well.
And I'm going to set this to like a five.
Might be a little bit too high, but we can just adjust it right in there.
All right, I think that we're done.
We just need to go back into Unity real quick.
Make sure that our fish spike is set up right and uh not set to a 0.5 on the cleanup.
Let's go find that real quick.
Bullet spike and our delay right here.
Make sure this return to pool is cranked up a little bit higher than 0.5.
We don't want it to just disappear instantly.
That's how we had it for our explosions and stuff.
And oh, we also want to make sure that uh gravity scale is off.
And I'm even going to freeze rotation on this so that our rigid bodies here don't start spinning around.
we don't get some weird spikes.
It should either disappear when it hits something or kill something or go through things.
And before I press play, the last change I want to make is I'm going to turn this origin to 90 so that my spikes shoot up and don't start just spawning inside of the lava or shooting down into the lava.
So, let's see.
I'll press play.
Go back over to that scene view.
We should expect to see there we go.
Our spikes are firing up.
They are hitting the platform, but that's just because we haven't set them to a layer where they can't.
and they should be able to go up and now almost kill the player.
Let's finish that off so that they can kill the player.
We'll go back to our bullet spikes.
I'm going to adjust this by adding a script that kills player.
So, we'll put the damage player script right on there so that it'll hurt our player when it hits them.
And then we're going to change the layer of this.
So, I'm going to go to layers.
We'll add a new layer.
I'm going to call this spikes.
This would be my spike layer for all of the spike related things.
probably be like an enemy projectile layers would be like a better more generic name for it.
But if change that over to spikes, we'll apply the override here and then we'll go into our settings again.
Remember it's under project settings and then we got to go find our physics 2D and then there's the layer collision matrix.
We'll make sure that spikes only collide with players, not even with other spikes.
There we go.
Save our project off.
And now only our player should be hit by the spikes.
And we'll just go verify that that's the case.
So we should see our spikes go flying through.
Shooting the uh shooting right through.
Looking good.
And if I get my player over there.
Let's just just just see if I can make it.
Oh, almost made that jump.
Oh, let's go bounce in on some frogs.
See if we can get all the way over to the spikes and then let the spikes do some damage.
Ah, if that cat doesn't kill me first.
All right, I got a spike that's still sitting there on the ground.
Oh no.
Okay, let's just move our player over there and and just go verify it one more time.
Benefit of having editor access, we just go bam, drag our player right over here, press control P, and we should be able to see the spikes actually working and hitting our player.
Bam.
Okay, there we go.
Spikes hit me.
Took some damage.
And it's a bit of a challenge.
I do think the last thing I want to do to make this a little bit more manageable though for my actual player is just crank up the uh the follow size just a little bit.
So in our multiplayer camera setup, we've got our target group and I'm just going to crank up the radius here to let's maybe make it about five and unpause.
There we go.
Now I can see the world below me.
Ah, it's interesting watching the the ground move, but the spikes staying in the same place.
It makes it seem like the spikes are doing something weird, but it's really just the ground.
Ah, moving along.
All right, that's looking good.
I'm going to go into plastic and commit spikes damage player and launch at variable directions.