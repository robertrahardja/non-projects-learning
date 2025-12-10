 right here, there it is.
This is the grass that I'm worried about.
Oh, I've already moved it to my B encounter.
So, make sure that you move your grass mid underneath your B encounter here.
This looks like mine right now is named grass mid6.
Let's modify it real quick.
So this is the grass that's that blank platform.
Let's call this a flood ground platform.
And then let's go make our collider for this object turn off when our flood waters rise and turn back on when our flood waters go down.
To do that, we'll go back into our B encounter and we're just going to add a reference to that collider to the flood ground platform.
I think instead of typing out the reference, I'll just do it right here at the beginning or the end of toggle flood.
I'll say underscore flood ground platform.
Let's call it flood ground collider enabled equals enable flood.
And then we want it to actually not be enable flood.
We want it to be the opposite of enable flood.
So we'll add a not sign.
I'm going to add a reference for our ground collider.
Let's go duplicate water.
Put in the name floor ground collider and change this to collider 2D.
2D.
There we go.
Got no S, not 2Ds.
It's just 2D.
All right.
Now, I should be able to Oh, should be able to build once I put the D at the end of enabled.
All right.
Back in Unity, we'll assign that platform here.
So, we can turn the collider off.
Save.
And let's go try it out.
All right.
Here we are.
We'll jump over here to the platform.
We'll set the B to half health.
And now I am definitely floating around.
See that it's definitely it's going to get more difficult for me to move.
Ah, hitting my head on some lasers.
And I think uh things are looking pretty good.
Let's say that the bee died.
We'll set the be to kill.
And the water goes back down.
Um oh, we don't turn the collider back on, though.
Oh, actually, we do turn the collider back on.
But check this out.
Look at the platform real quick and tell me if you see anything obvious that stands out that could be the issue.
If you see right here, the platform got set to the dead layer.
So, our character can't collide with it.
Also, I can't jump anymore because it's not detecting that I'm in the water because I kind of fell in when it was dropping down.
So, we're going to make two quick changes.
The first one is a fix for the layer.
So, we don't want to be setting our layer to dead on all of the objects inside of our B encounter.
We only want that to happen on things that are inside of this Broot object.
Let's go back to our B encounter and see the part where we set that layer.
So, you see here in take damage when we die.
Let's add a little space there.
When we die, we loop through all of the children components that have colliders or all of the child colliders and we set them all to that dead layer.
But we don't want to do that for the B encounter.
We just want to do that for the actual B object.
So, if we add an underscoreb dot at the beginning there, that should fix the first issue.
The second issue is not any harder to fix.
When we're in our water and we're doing our raycast down, a lot of the time, our character's raycast is starting right down here and shooting into this object that has absolutely nothing.
Because of how tall our character is and where the buoyancy is, there's a good chance that it shoots down into here and hits this collider on our water bottom that didn't have a collider.
So, I've just added a collider to it.
Go add a box collider yourself and then make sure that you check the auto tiling so that it fills out the entire area.
Otherwise, you just end up with a little collider there in the middle and it's not going to help.
So, let's press play and try it out.
Here we are on the platform and we'll set the B to half health again and see that we're now floating around.
I can run, I can jump, I should be able to keep jumping multiple times.
It doesn't just reset.
And once I kill that bee, I'm in dead zone.
Let's kill him.
I should be able to still use colliders.
I can land on platforms and everything else.
All right, let's stop playing now and commit our changes.
First, we'll save our scene that we smoothed water rising and falling for B encounter and check it in.
To make the water part of our B fight actually difficult, we're going to make some changes to the way that our player handles water movement and water detection.
Specifically, we're going to make it so that when you're in the water, the water can push you around, but you can't move left and right.
You have to jump out of the water to be able to well move left and right.
So, how are we going to do that? Well, we're going to make a couple changes to our player script and a tiny modification to our water.
And then eventually, we're going to also update the sprites so that the water flows visually as well.
We're going to start by detecting when our player is in the water and caching that as another bool field here.
So, we'll duplicate the is on snow and change this to is in water.
And then let's scroll down to the part where we actually look for water.
Right now, currently in our check for ground, if I just search for water, there you go.
See how on line 249, we check to see if we hit a water trigger and then continue on so that we can try to mark ourselves as grounded.
Let's not do that anymore and add in a new little call down below so we don't have to have this get component call on every single collider when we're checking our ground.
This is probably the worst part of our code for grounding right now.
So, we're going to delete that out and we're going to add in a new set of lines right below.
In fact, let's delete out this extra debug line as well.
And what we're going to use is the physics 2D.
So, here, let's say var water equals physics 2D, if I can find the word physics 2D or spell it right, do overlap point.
And that's going to give us back a point or any colliders at a specific point that match our layer mask.
That's not this overload, but once we give it the correct overload, we'll see that happen.
So, we're going to give it our origin where we're checking for ground.
And then we're going to give it a layer mask.
Let's call this water layer mask.
Add a semicolon here.
And then we're going to generate our water layer mask.
Actually, I'm going to copy it.
Control leftclick on layer mask.
Go up here, duplicate, and paste.
I want those to be right next to each other.
All right, let's scroll back down or hit the back button.
There we go.
There's our water.
And if we get a water object, so if water is not equal to null, then we'll just say is in water is equal to true.
Now, if we're in water, I want that to allow us to jump as well.
So, let's start looking for our grounding code.
Let's go do a quick search for the checks for we see if we're grounded.
So, here you'll see see uh is it this one, right? Nope, that's jumps remaining.
Ah, okay.
So, here we get our jumps remaining and we do that with our grounded.
I also want to just set our jumps remaining to true if we're in water or if we're grounded.
So, let's make this an statement where we say if is grounded or is in water.
Whoops, that's not in water.
In water.
And then we're going to put that in the parenthesis so that this will get evaluated with the or.
If either one of them is true, it'll continue on and then evaluate to make sure that our rigid body's velocity is going down.
So, if we're in the water and we're headed downwards, we're going to set our jumps remaining up to two.
Now, I don't know why we're calling get component on our rigid body.
Let's cache that or use the cached version of it RB to optimize our performance there.
Now, we're also going to need to look for the other places we set is grounded to false, for example.
So, right up here, we'll say is in water is equal to false.
And let's just do a quick check to see if there's anywhere else that we need to address it.
So, we do shift F12.
You see that we set it we set an animator here to jump if we're not grounded.
That I actually don't want to happen when I'm sitting in the water.
So, that's actually perfect.
And uh the only other scenario is that yeah, we set it back to false and then we set it to true.
So, that should be good for allowing us to be grounded when we're in the water.
But that's not the key thing that I want to do.
What I really want to do is make it so that if we're in the water, we don't use our horizontal velocity at all.
And we just use whatever the existing velocity was.
So, we're going to add a line here right at right at what is this going to be? 211.
If is in water.
So, right at the end of our movement code, then we're not going to do this.
I'll duplicate the line though and add an else statement.
Instead of setting our velocity to the horizontal and the vertical, we're just going to set it to the underscore rb.vlocity.
velocity.x and the vertical.
So, we'll keep the velocity on the X exactly the same if we're in the water, but we can still jump out by using the vertical.
Let's hit control KR D to fix up that formatting.
Save and go try it out.
We're back in Unity now and need to set a layer mask for the water.
I'll make sure to save and override.
Let's do an apply overrides on it and save one more time just so we can make sure that our prefab has that water layer set.
And then we'll play and run over to the water.
So we go get in the water and I can still move left and right.
Let's check if my in water state is true.
So in is in water is not true.
If I check it obviously it gets set to false.
Now what's going on here? If we look at our scene view and go find our character and see that these are the origin points where we're doing our overlap check.
Let's take a look at the water there.
So I select this water object here.
You see this has a box collider not on the water layer.
This is actually that bottom part and it's not set to a trigger.
Let's look at the top water.
The top water oh is actually also not set to the water layer.
And uh it's other than that it looks like it's good to go though.
So let's make the changes real quick that we need.
So we'll stop playing and first thing we're going to do is set our water to a water layer.
Go to water right there.
And then the second thing we're going to do is go to our water bottom and we're going to change this to be a trigger.
And I'll show you why.
Let's um do it in play mode first.
Well, the one of the reasons is so that our code hits and lands and looks right, but also so that when we float, see how we're kind of standing up a little bit.
I hit is trigger, and now we're actually floating down into there.
And let's go check out our player.
Our player is now in the water.
So, I can't move left and right really.
I can jump and move around, but moving left and right doesn't work.
Now, how is this going to be interesting? Uh, you should be able to move a little bit, right? Well, what we're going to do instead is use the water and we'll use thatctor that we have, our buoyancy.
Go find it and expand out the flow and we can start giving it now a flow magnitude.
So, if I want it to push enemies toward or push the player towards the enemy, I can give it a value that's positive and it's going to push them over to the right.
So, let's stop playing and make both of those changes outside of play mode.
So, we'll go back to our water, choose that water bottom, and make sure autotiling is on, is trigger is on and everything.
And make sure that our object is set to the water layer.
I'm going to save my scene, and then let's open up the water script.
Let's add a new method in our water to set the speed of its buoyancy.
So, we'll do a public void set speed.
We'll take in a float named speed, and then we'll just get our oops, I got an extra parenthesis there.
We'll get our buoyancy.
Get component buoyancy.
B O U Y B U Y.
There we go.
Buoyancyector 2D.
And we'll set the flow magnitude equal to our speed.
So that we can turn this on and off or set the direction externally.
And we're going to do that from our B encounter.
So let's go back to that B encounter.
And inside of our B encounter, we've got a reference to our water.
and we set it and turn it kind of on and off here, moving it up and down.
But let's also just set that speed depending on what our enable or disable state is.
So we'll say underscore water set speed and I want this to go off to the right somewhat fast.
So we'll say enable flood.
Then it'll be a 5F.
Otherwise it'll be a zero.
So it's going to set it to either five or zero depending on whether or not we're enabling the flood.
Let's do a quick save.
do a build and jump inside and try it out.
All right, here we are.
We're in the water.
I can't really move around.
I just kind of float.
I can jump get over to where I wanted to be.
I think I'm going to get over here and just blast him a whole bunch.
Oh, he's invulnerable while he's shooting.
See if I can get a whole bunch of shots off on him real quick.
Kill him for real without having to cheat.
Look at that.
There's the water.
Okay, I can It's pushing me.
It's pushing me.
Oh crap, I died fast.
Okay, well that seems to be working.
I'm going to test it one more time, though, just to make sure that the behavior is right.
Uh, so it was kind of a quick test.
We'll go to the B encounter now that I've got my hotkeys here or my shortcuts.
We'll do half health.
Bam.
Should be getting pushed to the right.
I can jump out and I can move left and right when I'm in the air, but when I'm in the water, I'm just getting forced over to the right nice and slowly.
It could probably speed that up, crank it way up if we wanted to make it more difficult, but I'm good with that for now.
And I'm going to go into plastic and commit our changes.
So, we'll go back to plastic and make sure we save the scene and say that B water forces player B water moves player uh let's say player handles water properly and B water flows to the right when flood starts and we'll check our changes in now that our water is pushing the player.
Let's make the visualization on the water match up as well.
We're going to animate the sprite and have it slide off to the right so that we can have it look like the waves are actually waving.
Let's do this manually real quick and see what that would look like.
So, I've got my water selected here.
I'm going to collapse out a couple of these properties or these components and expand out our material here.
So, what I want to do is be able to adjust this offset right here.
Now, if I just go in and try to change it, you'll see that I can't actually modify this offset.
If I create a new material, I can modify this offset at runtime.
Let's do that real quick.
I'm going to do it, but you don't do it.
Just watch along.
I'm going to delete it and show you right afterwards.
So, we'll create a new material right here.
I'm going to call this water, and then we'll just assign it up here instead of using the default sprite.
So, go to the sprite renderer, and we'll assign that material.
We'll go pick the water.
Oh, looks like water already got picked.
And then we can now drag that offset.
And you can see that it will tile.
Although it does do a little bit weird, something a little bit weird, but it's sliding off to the left.
And it slides off to the right when I adjust this offset.
So, we're going to write code to adjust this offset.
But first, let's figure out why it's doing that weird thing.
So, if we pull this offset to the right, goes totally flat after one.
And if we pull it to the left, it goes totally flat after negative 1.
What's actually happening here is that our texture isn't set up for repeating or tiling.
So, if we click on our water top high, you'll see that the wrap mode is set to clamp.
If I switch that over to repeat and apply, I can now go over here and adjust this offset and watch as the water just kind of slides back and forth along.
Now, I don't need to create a new material for this.
So, I'm actually just going to delete it.
I'm going to go back here to my scripts, delete that water material, go back to my water here, and we'll just change the material from missing back to our default sprite.
Where was that? Ah, sprites default blind.
It was right there in front of me.
So, now that we've got that, let's go into our code and write the code to make that animation happen without having to do anything to our materials.
So, we're going to open up the water script, and I'm just going to start typing at the bottom of it.
I could add something into this water script to make it flow to the left.
But remember, I've only got the water script on the top level component, not on the water that's down below.
And I want this to animate for both of those water objects.
In fact, I want to animate for anything that could really animate a texture to the left or the right.
But for now, we're using it only for water.
So, I'm going to keep it named specifically a water flow animation.
So, I'll call this public class waterflow animation.
We'll make it inherit from a mono behavior so we can add it on as a component.
And then in the start method, let's add a start.
We'll just cache our sprite renderer.
So we say get component sprite sprite renderer equals get component sprite renderer.
We'll add a field for it.
And I'm going to add a require component attribute as well.
So say require component type of sprite renderer.
If I can spell sprite renderer right.
Okay.
RI T renderer.
There we go.
So that we have to have a sprite renderer if we're using this waterflow animation because it's definitely going to require it.
Now let's add an update method.
In the update method, we want to figure out what that new x value is going to be.
So we'll say float x equals.
And we just want this to be a value that changes over time pretty smoothly, but we want it to go from, you know, probably like a 0 to one or a one zero to negative one or or something like that.
So we'll say math f.re repeat and then we can use time time time and then give it our max value or the length that we want to repeat.
So we give it a one.
It's going to give us a value between zero and one over and over and over every single second.
Kind of like just getting the seconds.
We could of course multiply this and do some sort of a speed.
So we do times scroll speed and then generate a variable for that.
We could have that be a serialized field and then default it to one.
So, it's kind of the default, but then we'll be able to adjust it in the inspector and figure out a value that looks pretty good.
Once we've got that X value, we going to want to set that texture offset.
But the texture offset requires a vector 2.
It wants the X and the Y.
So, we're going to need to create a vector 2.
We'll call this offset.
And we'll assign it to a new vector 2.
and we'll give it the default or the value of x for its uh x parameter and then a zero for the y parameter because we don't want to offset the y at all.
And the final thing we need to do is call the sprite renderer and tell its material to set the texture offset to that offset value.
First, we have to give it the texture that we want to offset though.
And we're going to offset the main text, which is that main texture, and then we're going to give it our offset value and a semicolon.
We'll save that off, do a build, and then realize, oh yeah, we got to move this waterflow to its own file so that we can actually attach it.
So, we'll move it to a file.
Let's say move to waterflow animation.cs.
And then we'll jump into Unity and go attach it.
We've got our water here.
Let's go select the two water objects and add that water flow animation.
It should have a Let's go double check it.
It should have that one value.
So, I thought we had a uh Oh, I removed my serialized field.
Oops.
Let's go read that.
I copy pasteed and removed my serialized field for our scroll speed.
So, we can adjust that.
All right.
Here's our water flow animation.
By the way, on the water, I think I covered this, but just in case, if not, I did change out the polygon collider to a box collider because it just works a little bit better with these wavy shapes and end up with slightly better collision detection.
All right, so we've got our water flow animation.
Let's press play and play and see what happens.
We should expect to see our water now flowing off to the sides and then getting weird or not getting weird.
So, the water on the top is doing absolutely nothing.
Does it have the water flow animation? It does.
And the water on the bottom is animating, but it's animating incorrectly.
It's animating looping over that texture.
So, let's fix that first.
We'll go select our water and we're going to make it repeat instead of clamp.
So that water is looking good.
And then for that top one, it's probably actually working for you.
The issue is really simple.
I just grabbed the wrong sprite material.
So I need to find the sprites material that is the lit one.
There we go.
And now my water is flowing as well.
The speed is a little bit off though.
So let's stop playing and go fix those in edit mode.
So go sprites.
Okay, we'll just reset this sprite.
There we go.
Now it's got the correct material.
And I just need to adjust this tiling width so that it's right.
I'm thinking it's probably what, like 36ish, 35.
36.
There we go.
So there we go.
I've got my water stretched out properly and I've got the correct material.
And now if I press play, well, my Yeah, my water flow speed is as long as they match, they should flow nice and evenly.
There we go.
I've got water flowing off to the left.
And of course, I can also make it flow to the right.
So, let's change the scroll speed to negative one.
And we can see that it's going the correct direction.
So, I'm going to stop playing one more time, go back in and select both of these, set them to a -1 value for now.
And then we'll go to our water script and we're just going to tell our water to turn that component on and off.
So, inside of our water, when we set our speed, if the speed is greater than zero, we'll turn them all on.
And if it's less than zero, we'll turn them all off.
So, we're going to do another for each loop, and we'll say for each animator in well, let's let's call this uh let's call this WFA, waterflow animator, or I'm waterflow animator.
I don't really like shortening names.
In get components in children, waterflow animation.
Oh, yeah.
I guess that should be animation.
M match the name.
Oh, and we need our parentheses.
So for each of those, we're just going to set them enabled or disabled uh based on whether or not our speed is greater than zero.
So say water flow animation.
Oh, I need the var keyword.
And I'm missing all kinds of keywords and typos here.
Waterflow animation.enabled equals speed not equal to zero.
So we'll turn it on if the speed is greater than zero and off if it's less than zero.
That should allow our water to start animating automatically.
Um, but we do need to turn it off by default as well.
So, we should probably inside of our start for our water just tell all of these things to be disabled.
So, we'll add in a start method, loop through all of our water flow animators and set them to not flask false there so that they are not enabled.
And I'll delete out these extra braces because we just don't need them and they're making our file longer for no reason.
All right, we'll save and build.
Here we are back in game.
Oh no, I've messed up my layer on the on that front water.
Let's uh adjust that sorting layer real quick.
There we go.
Got my water layer right.
I should be able to run around and blast my bee.
Get that water flow going.
Now I've got a much harder fight where I can only jump in the ground or jump from the water.
And then I assume once I kill him that water is going to turn back off.
I don't know if this guy is still too easy or if I'm just really good.
There we go.
And the water has stopped flowing.
It's nice and chill now.
All right, let's stop playing.
Make sure that we've saved our scene and updated that player prefab.
I want to make sure there are no updates for it.
Looks good.
And then we'll make a commit.
So water for B boss fight is done.
And check it in.
Now we're going to work on persistence.
Our current game persistence setup works, but it's very basic, and we need to build something that's going to work for a large scale game.
something that'll allow us to persist all kinds of data and make it so that we don't have to write a bunch of code every time we want to add new stuff that's being persisted.
We'll make it so that we can persist things like the state of different collectible objects, the state of our different switches in the game and other things in the game, as well as our players position and location, maybe their velocity, so we can save when they're mid jump and reload and have them continue being in a jump.
and we're going to make it very easy to debug and test with some custom editors.
And that's actually where we're going to get started.
To begin, we're going to create an editor script for our game manager.
I've got my game running here.
I'm actually going to stop playing it.
Right click in the project view, hit create, and create a new editor folder.
It needs to be named editor, spelled exactly like that, edi.
I'm going to go in there, open it up, rightclick, hit create, choose C# script, and we're going to make a game manager editor.
So, capital G, capital M, capital E, and we'll open it up.
This is going to be a custom editor for the game manager.
So, when we select the game manager, okay, got to go back to that file.
There it is.
When we select the game manager, it's going to render the game manager in the inspector and add a little bit of extra stuff.
So, now to make that happen, we're going to need to replace the base class with editor instead of MonoBehavior.
I'll hit enter, and it automatically added the using Unity editor statement up there.
If yours doesn't, just go put it up there.
Next, we need an attribute to tell the editor what type we want this to be a custom editor for.
So, we put the break brackets here and then custom editor.
There we go.
And then we got to put type of inside parenthesis and open another parenthesis.
And here we want game manager.
Well, I got to close this out with two parenthesis and a square brace.
Now, the editor class has a couple methods that we can override.
Start and update are not them.
So, we're going to delete both of those and put override.
Oh, not onride.
Override.
And then we should see the one that we want is on inspector guey.
I'll hit enter and save.
That should now give me a custom editor that doesn't break anything and still shows the game manager in Unity.
Let's go make sure that that's the case and then we'll work on editing it.
So, go back into our game.
Go select the game manager.
I can see the game manager.
No errors here.
Even if I hit play just to force and make sure that it recompiles.
No errors here.
Looking good.
Now, if you run into some errors, just make sure that your game manager editor is in the correct folder and that you don't have like two of them if you search for game manager editor.
Make sure that you don't have a second game manager editor in another file or somewhere else like that.
Or just look at what the error message says.
All right, let's go back into the code.
Now in the custom editor, we automatically get a reference to the object that we're inspecting.
But that object is typed as a game object, not the thing that we need.
So what we can do is add a variable here and use that object by casting it.
So say var game manager.
Oh, look at that.
It's going to autocomplete.
Game manager equals and then we're going to get the target, but we're casting it as a game manager by using the parenthesis here.
Next, we just going to call game.
Oh, no.
We're not going to call anything.
We're going to add a button.
Next, we're going to add a button to save our game and another button to load our game.
So, say if.
And then we need what is it? It's guey layout.
I always forget which one it is.
And then we do open parenthesis and the name of our button.
So, this will be save.
I'll just let's call it save game.
And if that is pressed, then the code after it or the code inside the parenthesis will be called.
And I want this to be game manager.save save game.
Now, if I want to load a game, I want to be able to just press a button as well.
So, I'm going to hit duplicate and just select those lines there, hit duplicate, and I'm going to put reload game.
And here, we're going to call a method called reload game on our game manager.
Now, save game exists, I believe, but reload doesn't.
So, we're going to need to create that.
Let's hit alt enter and generate a method for reload.
And then, let's click on save game and just hit F12 to go to it.
You can see it exists, but it was read because it's private and not public.
So, it couldn't be accessed by another class.
We need to make this public so it can be called from our editor script.
And then down below our save game, we're just going to add a reload game method.
I'm going to put a public void.
Oh, wait.
We already generated a reload.
So, I should actually just go find that because that's going to be in here somewhere.
I think I generated it.
Okay, I didn't generate it.
So, I will type it in here.
For some reason, I thought I hit generate on it.
Okay, so we go to load game.
Right here, we're going to put public void reload game.
And this can just be an expression body method that calls load game and just passes in our game data.
Name.
There we go.
So, remember our game data.game name is the thing that's set and used for saving off our game.
So, we're just going to reload the game by calling load game and passing that name in.
Let's save and do a build real quick.
Make sure I haven't missed anything.
Go back into that game manager editor.
There we go.
We see I've got my two buttons available.
And then we'll go into Unity and see if they work.
All right, here we are in Unity.
We'll hit new game.
Run around.
Let's go take some damage.
Oh, I got hit a couple times or one time.
We'll save and then reload.
You can see I come back with my health at five.
Let's go grab some coins real quick.
Not coming back to my start, the correct position yet.
But I am coming back with the correct health.
Let's save and reload.
And I come back with 13 coins and my health's right.
But if we go back over here, of course, all of our coins have reset.
So, we do have a save and a reload option now available.
See, I reloaded and our coins went back down to the last time we saved.
But we've got a couple things to address.
For now, though, let's do a quick commit that we've added our added game manager editor.
We'll check that in and then we'll continue on.
Now, we're going to take a look at our player data.
We're going to add some data there and check out our entire workflow for it, as well as track down a bug.
So, here you can see I've got my player data visible underneath game data.
If you don't see yours, you can just expand it out.
I've got a couple saved games in here.
And if I save game and reload, my player data shows up.
Now, the reason I don't get my player data showing up automatically right now is cuz I didn't come in through the menu.
And I don't have this binding up to anything.
So, we're going to need to address that.
We're also going to want to store the position of our character so that we can reload that when our player comes back in so they can come back into the same spot in the world.
So, let's stop playing.
Well, first actually, let's shoot and let's take a look at the console because you see that we've got a couple errors down here as well.
I'm going to reload again.
And look, now we've got more errors.
It went up by four every time I clicked.
If I reload again, you'll see that it went up by six every time I clicked.
Click again, it's going to go up by eight every time I click.
So, something is happening every time I reload that's causing me to get two extra errors every single time I click.
Let's take a look at what those errors are.
We'll use that as our starting point and jumping into the code.
So here you can see I can click on these.
This one just tells me it's something in the the input system.
But the one below tells me is something in the blasters use method which is calling fire which is called from the use equipped item here on player inventory line 46.
And that's called by some delegates passed in from our input system.
So let's go take a look at line 46.
Here we can see here this is where it's trying to use our equipped item.
And the problem was that our item is destroyed or null.
At least that's what the error message said.
So let's take a look at the references for use equipped item and click here or hit shift F12.
Whoops, the wrong key there.
Shift F12, find all references and see that we register for the performed event right here in awake.
Let's check and see if we ever unregister for it.
An easy way to do that would just be to search for my fire string.
Just do a control F and hit enter.
And I can see that well we never unregister for that.
We also don't unregister for the equip next event.
So let's copy both of these lines on 19 and 20.
And then down here add an on destroy so that we can remove the registration.
I'll just paste it in and replace the pluses with a minus.
What's happening here is that our player inventory even though it's getting destroyed, it's still registered and bound into this player input event which is or this player input objects event or its actions here.
The input action asset technically.
And that's tied into the event system and that event registration doesn't go away automatically.
So whenever we press fire, it's still trying to call into this destroyed inventory of a past character and then use its blaster that no longer exists either and then eventually blows up.
Now it doesn't blow up in use equipped item because there's nothing here that references an object that's actually been destroyed.
The equipped item is still technically around.
It just hasn't been completely destroyed.
it's around because the C# part of it couldn't ever clean it up because there was still an event registered for it.
But Unity has destroyed the object.
So, we can't actually use it and we don't want to.
Now that that's fixed, let's go back into Unity and double check it.
All right, here we are.
We'll shoot, save, reload, shoot, reload, shoot, reload.
It's looking good.
Now, we're going to adjust our workflow for loading games.
Instead of having our player data be empty here because we didn't come from the main menu, we're going to make sure that whenever we restore a level, we make sure that we've got some player data here and that we have the recent data actually bound up to our players.
To do that, we're going to open up our game manager and in our handle scene loaded going to do two things.
First, I'm going to just comment out the save game because I don't want it to keep saving game constantly.
I want to just take tight control over that for a while and then we'll figure out where we want it to actually save after we've got all of the save systems up and working.
Instead, what I want to do is find all of our players.
So, I'll say var all players equals find objects of type.
And we're going to remove this in a while, so don't worry about optimizing it.
Find objects of type, not all.
There we go.
And we're going to find all the player objects.
We'll loop through each of the players.
Loop through each player in all players.
And then we're going to bind all of those players to their data.
So we'll say var data equals and we'll want to call get player data.
And here we need to give it the player index, but we don't have that yet.
So we're going to need to get our player input as well.
So say var player input equals player.get component.
We don't have it cached, do we? Nope.
So we'll do get component.
Got to double check.
And it's going to be that player input.
And then we'll pass in the player input dot player input.
There we go.
Player index.
And again, don't worry about optimizing this.
We're going to refactor this all the way into something more generic really soon.
Now that we've got our data, we just need to tell our player to bind to that data.
So now we're going to automatically bind up whenever we load into a scene.
Let's go try it.
All right, we're back in Unity.
We'll press play.
And we can now see our player data there.
Let's go take some damage and see what happens.
I take some damage.
My health is going down.
And if I go grab some coins over here, my coins go up.
I can save.
I can reload.
And I can see that data looking right.
Let's stop playing and we'll go make a quick commit that we've fixed event regist dregistration.
and and and default.
Oops, hit the wrong key there.
Okay, fixed event dre registration and default player data and check it in.
Now, we're going to start keeping track of our players position and velocity, as well as our saved game name.
when I save, I realize my game name is blank right now.
I can reload it, but I won't be able to come back in after I save and reload again because I'm saving off a blank name.
So, let's dive into the code and adjust both of those things.
I think we'll start by let's just go into the game manager and do the saving first.
So when I save my game right here at the beginning, if my game data name is empty.
So here we actually want to do a if string is null or white space.
So that way we can get blanks and spaces as well.
Then we just want to give it a new name.
We'll say game data.ame equals.
And here I'm just going to call it game.
And let's let's use like a game plus the number of games that we have.
So I think we have an all game names and we'll use dot count.
Should we do count plus one? So if we have one game, no, it should be exactly that.
So this be the game and a number there.
All right, let's go on to our player data now.
So our player in its update is going to just store off where it is so that we can keep track of it and then we'll be able to view that in our game manager.
That'll be stored off in the player data class though where we're storing our coins and health.
Let's go add these two things as fields.
We'll put a public vector 2.
And the first one, I want to make sure I get the Unity engine one, not the numeric.
Don't want to have a numeric using statement up there, or else we'll have an error later saying that the types don't match.
So, this first one's going to be position.
We'll give it a capital P.
I'm going to duplicate that and then make a velocity.
P E L O CI TY.
There we go.
Then we'll jump back into our player.
Now in our player in the update right at the end of it, let's just set our player data.
So we'll say player data.position equals and here we'll get the position from our rigid body which is a vector 2D.
And we'll duplicate that and do the same for our velocity.
Let's see.
Oh, I spelled velocity wrong.
Let's rename that V L O CI TY.
I had an extra C in there.
All right, we'll save and do a build and let's try that out in Unity.
All right, here we are.
You can see I've got a position and velocity and they're actually updating.
I can save my game now and it shows up as game three and I can reload my game, but it doesn't actually keep my position.
So, now that we're storing off or saving our position, I'm pretty sure we're saving it.
We're in that position.
We hit save, it should be serializing, right? We need to figure out how to restore it.
Let's take a look at our code again.
So, here's our update where we're setting the data and reading it from our rigid body, putting it into position and velocity on our player data.
But where would we restore it? And there are a couple things we could do here.
First, if we go down and find our bind method, we could theoretically do it in here.
The reason that I don't want to do it in here, though, well, there's twofold.
One is that bind generally just should be hooking up the data.
It shouldn't necessarily be moving objects around and doing more complicated things.
I I prefer if it just sets up the data and then maybe sets up the initial state, but we're going to keep a very generic binding system.
And we're going to extend this out to be even more generic.
And I don't want them to have very different implementations for each one.
So instead, we'll create another method.
And where we call bind, we're going to call this method to restore our position.
And one of the key reasons for this, by the way, is imagine that we are restoring the position in our bind method.
If we save off our position and then we load into level two and then we call bind again on the new player there, we're going to instantly bounce that player back to the position that they were at in level one.
So that could be maybe, you know, some random offscreen position or something else, but it's not the position that we wanted to teleport them into.
it's not the starting position for that level.
So, we want to be able to have some tighter control over that.
And we could maybe have a parameter in here for do a restore or something, but I think that having a separate method tends to be cleaner.
It makes things less complicated as well.
So, we're going to add a public void restore position and velocity.
And that's going to just tell our rigid body to move to its players player data position.
So, we'll say underscore RB.position position equals player data.position.
And then we'll do the same for velocity.
In fact, let's just duplicate that and replace position with velocity.
I cannot spell velocity.
All right.
So, that should put us back in position, but we're going to need to call it.
So, let's make sure that we call this from where we're calling our bind.
In fact, let's get rid of line 302 here.
We got an empty line.
Go to references, and we're going to find the one where we Let's find it.
where we bind in our game manager.
So not this one in handle player join.
Let's find the other call to player.bind.
That's when a player joins like our secondary player and comes in later midame.
So after scene load, there we go.
We'll say player.restore position and velocity.
Now we're not going to restore position and velocity on a second player that joins in the game afterwards.
And we'll deal with second players a little bit more later, but for now, we just want to restore the position of this player.
The first player when they come back in, or the first player that loads back in, second player will just appear near that person that's been saved off.
All right, we'll save and make sure that we save.
Let's go try this in Unity and see what happens.
So, here we are.
Let's run around.
I'm going to run right over here by the blue flag.
In fact, I'm going to start jumping upwards and hit save.
And then let's go over here to the right somewhere.
I've got game four saved.
You can see that's my game name.
And I'm going to hit reload.
And look at that.
I reappear over there popping up into the air.
Now, there is still one problem with this implementation.
If we land on this flag, look at that.
Look at where I reappeared.
I actually reappeared in the exact same spot as where the flag was.
We can see that a little bit better if I stop playing.
Let's go over here and just going to take this flag.
We'll move it up here.
We'll save.
Well, actually, I didn't save, but that's okay.
We'll press play, and I'll just run up there and jump on that flag and watch what happens.
So, come down here.
We'll go jump on the flag.
And now I appear up here.
So, I don't want that to happen.
I want that position to not restore.
Just like we talked about, I don't want it to happen every single time we bind.
So, we're going to go back into the part where we're calling this the restore position and velocity here.
And we're only going to do this if we're calling a load game.
So if the game is being loaded then we'll do this otherwise we'll skip it.
So we'll say if load actually yeah if load game or no game manager can't get my words out is loading.
There we go.
Then we'll call restore position and velocity.
We'll add a boolean property is loading to our game manager.
Oh look at that.
It automatically added a public static bool is loading with a private setter.
That's exactly what I wanted, just like my is cinematic playing.
Now, we're going to scroll down to where we do our load game.
And right at the beginning of it, we'll set is loading equal to true.
And then when we actually uh check it, so let's do another search for is loading is loading.
There we go.
Right afterwards, we'll set is loading to false.
Now, we're going to use this in one other place in our players update.
Let's go find our update method.
Where are we? There.
Oh, update grounding.
Right here at the top of our main update.
If we're in this loading state, we don't want to be moving our player around.
We don't want to be setting the position and velocity.
Right now, it's really fast.
It's almost instant.
But if we have a larger level and more stuff going on, we don't want to start kicking off actual movement and and controlling our player or doing anything like that.
We also don't want to be updating the position and velocity.
So say if game manager is loading, then we'll just return.
So it won't do any input or anything like that until we've finished.
Now let's go into Unity.
We'll go grab our our our game manager.
Let's go select it right here.
We can watch our data.
We can run around.
We can take some damage here.
Let's run over here.
Go grab a couple coins.
Save our game.
Jump over here.
Continue on to the next level.
And you can see I'm at the same the correct spot.
I can come over here, take some damage.
Let's see if we can find something.
Pretty sure I got some spikes over here that can hurt me.
There we go.
And then we'll reload.
And look at that.
I'm back here with five health.
Let's go into the other scene, though, and save our game here.
And reload.
Look at that.
We're not saving our scenes.
Let's take this as a quick opportunity for a challenge.
See if you can figure out how to get the scene to persist.
It should be very simple.
Just take a look at some of the existing code that we've been looking at recently and maybe one of the arguments and see if you can track it down.
Give you just a moment.
Go ahead and pause, of course, and let's continue on.
I'll show you the solution.
So, if we go back into that game manager right here, when we load a scene, we get arg.
can just cache that off in our game data so we know what level that we're we're currently in and then we can reload that level when we load our game.
So maybe let's say right down in here in any of the parts where we're not loading the actual menu scene, we'll say underscore and here we want our game data and we're going to use current level name equals arg0ame.
We'll generate a field for that.
It should just be a nice string.
Go a hit F12 and take a peek at it.
We'll go make that public as well.
And then we'll go back into our load.
So when we do a load game, there we go.
We'll figure out our level to load.
Instead of loading level one, we'll load a level based on the game data that we've got here.
So I'm going to cut level one right here.
And we're going to put it let's say var scene name equals and we'll say underscore game data current scene or current level name and we need it in actually a stringisnull or white space.
Oh yeah yeah then we'll return level one.
Otherwise we'll return game data current level name.
There we go.
Let's take a look at that logic since I kind of confused myself in my wording.
So, our scene name is going to be equal to if the current level name is set or not set, then it'll be level one.
Otherwise, if it is set, it'll be the current level name.
In fact, what we could probably just do here, I think it'd be a little bit cleaner to say if game data.curren level name is if string.isnull or if string.isnull or whites space current game data.current current level name.
Then game data.curren level name equals level one.
one.
one.
And then here we'll just pass in game data.current level name.
It's always good to look at the code, refactor it, and clean it up as you're writing it.
Make it a little bit easier to understand.
So now we should load the correct level.
Let's go try that out.
All right, here we are.
We're going to run across.
Actually, let's reload.
Make sure that we still end up in level one.
Yep.
And then we'll run over here, jump on this thing, run off to the right a little bit, save and reload.
And look at that.
We're back in level two.
I'm going to cross over to level one.
Reload.
And I go back to level two.
Things are looking good.
It's time to go make a commit that multi-level player position persistence works and check it in.
Currently, our data binding is working pretty well for our player, even across scenes.
But it doesn't work for anything inside of our levels, like these coins.
You can see again, I can pick up coins, of course, save and reload, and come back, and the coins are there and keep picking them up.
So, we're going to want to be able to persist things for each level.
And to do that, we're going to add in a new data structure.
Let's go into our game manager and then find our game data.
Let's go find game data.
We'll control leftclick on it.
And in here, we're going to add in a new structure that's going to handle all of the data for a single level.
We'll call this level data.
And then we'll fill it up with the different types of things that we have in the levels.
Remember, our player data is a little bit different because our player goes across levels.
And we're also going to have another type of thing that's a little bit different from our level data for items because they'll be able to move across levels.
But a lot of things stay in a single level and we should be able to handle those pretty easily with a level data.
So we're going to add a public list of level data named level datas.
And we'll initialize that to a new list of level datas.
Just like that.
We'll need to generate a class for level data.
So I'll hit alt enter.
And let's do it in this file.
I'm going to copy that serializable attribute and add it up here.
We're going to need a couple of properties.
First, a level name.
seems like an important one so that we can bind the level data specifically for a level.
We know what when we load level one, we know which level data to use.
So, we'll add that level name field.
And then I know I want to store the state of coins.
So, let's put in a public list of coin data named coin datas.
And again, we'll initialize that to a new list and then generate a type.
So, we'll hit generate type and we're going to do it in the same file.
Come down here one more level.
We'll copy that serializable attribute again, paste it in here.
And now for a coin, what do we really want to keep track of? I don't want them moving around.
I don't want them really changing anything other than their kind of is collected or is enabled state.
So, I'm just going to add in a bool, a public bool is collected, and then we'll save.
Now, inside of our coin, we're going to bind up to one of these coin datas from our game data.
And then we'll just toggle that field on whenever our object gets collected.
So, let's add in a bind method public void bind.
That'll allow us to bind to a coin data.
And we'll figure out where we're going to get that from in just a moment.
We'll name the parameter data.
And we'll just say underscore data equals Whoops, it autocompleted the wrong thing.
Equals data.
We'll generate a field for it.
And now we've got a coin data that we can use.
So delete that private keyword.
And down here when we add a point before we even add a point, let's just say data is collected is equal to true.
So now we've got something that we can set in here, but we don't have this bind method being called.
We need to figure out where that's going to happen.
And my recommendation where I would put it is right here after we've loaded our scene.
Once we load our scene, before we go through and restore our player position and all of that stuff, let's restore all of our coins or bind up all of our coin data.
I'm going to add in some new lines right here and just give myself a little space on line 52.
And I'm going to call a method.
Let's call this bind coins.
That seems good enough.
We'll generate a method for it.
And then in this bind coins method, we'll find all of our coins.
So say var all coins equals and we'll just do a find objects of type.
Make sure I do the of type.
I have to add in extra parameters and we'll find all of the coin objects.
Then we'll loop through each coin in all coins.
So for each var coin in all coins and then we're going to bind each coin to its data.
So we want to call coin.bind.
But we're going to need some data.
So let's get a data parameter up above.
Let's say var coin data or just call it data equals and we need to get something from our game datas level data.
So we're going to have to say underscore game data dot level datas and we're going to need to know which level we're currently in.
So here we're going to have to find the correct level data.
And since we're going to do that multiple times, why don't we do that one level up and pass it in here? So let's assume we have a level data and then we'll loop we'll get the data from our level datas level data coin datas and we'll do a first or default and we're going to match the coin data to our coins name.
So I'll say t dot and we want to use our name equals and then we're going to use this name or just name.
So, we're not not this.
Whoops.
What am I saying here? We got Oh, coin.name.
There we go.
Get our coin object.
Now, our coin data doesn't have a name property, and that's what we're going to use to match it up.
So, instead of having these all be indexed, which we could do, or having a unique key or a unique ID, one of the easiest things to do, one of kind of the cleanest things until you get to a very large scale is to just give them a unique name.
And we'll do some editor tooling to enforce this and link them back to prefabs later.
But for now, we're just going to generate a field.
We'll generate a field called name on our coin data.
Let's go take a look at it.
So, we've got a field here.
Let's make that public instead of internal.
And then we'll now that we've got our data, we'll bind it up.
Now, if we don't have a data for it, so if the data is null, so if data is equal to null, maybe we've added a new coin to the game or we've just never loaded before, then we're just going to instantiate it.
We'll say data equals new coin data.
And then we're going to give it our is collected is equal to false.
And our name is equal to the coin's name.
We'll save that off.
Hit control D to clean up our reference or our formatting.
And then finally, we need to call bind coins and pass in that level data.
We have our bind coins call, but we don't have the current level data.
So, let's get our current level data one level up here.
Say varle data equals, and we're going to get our game data level datas first or default.
Just like before, we're going to check the t.name or level name against our arg name.
So the level that we've loaded, remember scene zero or arg0 is the scene that we've loaded into.
So we're going to find the level data for the one that we've loaded into.
If that doesn't exist, just like before, we'll create it.
We'll say level data equals new level data.
And we actually need to make sure we add these to the list.
The level name is going to be equal to arg0.
And then we'll bind to that level data.
Now, we need to do two more things here.
We need to add these level datas that we're creating or this new one to that level datas array.
And we need to add the coin data that we've created to the coin datas, right? And I said array, but I mean list in both of these cases.
So let's add in some braces here.
Oh, not just an open close down below.
We'll say underscoreame data.le datas.
Uh it was going to autod do it for me.
Add There we go.
Level data.
And down here in our coin datas, we'll do the same.
When we create a new data object, we need to make sure that we add it to our list.
So say level data coin datas add data build and fix my typo here.
This should be equals null, not not equals null.
We don't want to create a new one if it exists.
Once that's good, we should be able to jump into Unity.
And then we when we hit play, we should expect to see a new level datas get created along with a coin data for all what do we have 16 coins.
So we've got a level datas object underneath there.
We've got all of the coins, all 16 of them.
And we can see that none of them are collected.
Let's go collect one and see if the state changes real quick.
So we'll run over here.
We'll go grab some coins.
Uh oh, looks like one of them changed.
There we go.
That other one changed.
Now they're all collected.
and we can save and reload, but the reloading doesn't do anything yet.
The state is still correct.
It's got that they're collected, but we're not restoring them to a collected state.
So, let's make that final change.
So, back in our coins bind method here, we've got a slightly different scenario than the player where we have to worry about our player updating and moving and doing other things during the loading system.
And and in there, we don't really want to adjust the player's position or move them.
At least I I don't.
But for our coin, we can restore its enabled state.
So when we bind, we've got the data in its correct state already.
And we just say if data is collected, then we'll just set our game object to inactive.
So say game object set active to false.
Now, if we go back into Unity and we reload our existing game, we should expect to see that the coins have disappeared.
So we'll press play.
Actually, I won't be able to reload the past game because our game level name won't match with our previous one.
But if I go into here and I just find our game name and put in game six and then hit reload, I got to tab out of that field.
Make sure that it saves my change over.
Hit reload.
Okay, that didn't work.
Let's just jump over, go into level one, grab those coins here.
We'll do a save and a load.
I'm not sure what the state of game six was.
I may have messed it up in between.
All right, so I go grab all my coins except for that one.
We'll do a save and a reload.
And we come back and there's just that one coin.
I go grab that last coin and reload.
Come back and the coin is still there cuz I didn't save.
And if I get it again and then do a save and a reload, of course, the data comes back correct.
And this is what we want to happen going forward.
Although we're going to want to make this a little bit more generic so that we can write even less code for all of the other things that we want to persist.
For now though, let's go into plastic and commit our level and coin data are persisting and coins properly restore and we'll check that in.
Now, we're going to extend our persistence to handle laser switches.
And we're going to do this in a relatively simple way again.
In fact, what I'd like to do is present this as a quick challenge.
See if you can figure out how to get the level data working with the switches.
So, you do the same kind of thing that you're doing with the coins, but do it with the switches so that you can toggle them on and off and persist their state.
When you're done with it though, follow along and watch my implementation and then get ready because we're going to do some advanced stuff in the next section where we're going to take both of our methods and do some combination stuff to make it so we can keep building extensible systems in the future.
I don't want to spoil it too much or talk too much about it.
So go ahead and see if you can figure out the level switch part, the the laser switch and the level data for your laser switch and then continue on if you get stuck or even when you're done just so you can see my solution and see how it compares and then be ready for the next part where we build out our bigger, more complex solution.
All right, I'll assume that you've either paused and gone through it or you just want to continue on.
So let's get started with the switch.
First, I've got a yellow laser switch.
Now, I already dragged this one out, but I'm just going to delete it again and go through that process again.
So, grab our laser switch, our yellow laser switch prefab, the one that we made before.
I'm going to pop it right over here.
I'm going to name this thing yellow laser switch 2 because I've saved some data on.
Actually, you know what? I'm going to just rename it back to yellow laser switch.
We'll press play.
And right now, if I load and save my game, I expect the state of this thing to not save at all, but my position to save.
Let's just go verify that we're in the correct state and that we understand where we are.
So, we come over here, we run across, we switch our switch on, doesn't do anything yet, but if I save the game, I don't have any level any switch data here or anything.
So, as soon as I reload, I expect it to Yeah.
flip back over.
So, how are we going to address this? Well, let's dive into our system right now for persistence.
We'll go into the game manager in just this window and then we're going to dive into our part where we're binding our coins.
So when we set up our coins right now, remember we find all of the coins in the scene and then we use this coin datas array or it's actually a list on our level data and then bind each coin up to one of those items and then we create new coin data items if they don't exist.
We're going to do the exact same thing for our laser switch.
So, we're going to need to create a laser switch data, give it a bind method, and then kind of copy this code right here.
So, what I'm going to do to start is just duplicate our bind coin.
So, just select it all, hit control D, left arrow, enter twice, and let's call this bind laser switches.
I need to make sure I use the word laser switches because if start using switch, it's actually a reserved word and it'll start causing some issues.
So, I just like to put laser switches in there and be super explicit.
Now I want to bind it to my level data still.
I don't want to get all coins.
So I'm going to rename this to all laser switches.
And then I don't want to use coin here.
I want to use a laser switch and continue on.
I don't want to use a name coin.
It's a laser switch.
So again I'll just rename again laser switch.
And then let's continue on to the next line.
So this is looking at coin datas.
I want to look at laser switch datas and I haven't created those yet, but we we'll figure it out.
We'll create them.
And I want to make sure that the name matches the laser switch name.
That looks right.
Data equals new coin data.
Doesn't sound right.
This should be a laser switch data.
And then is collected.
That doesn't make sense either.
I think for a laser switch, it' be is on, not is collected.
And then finally, we've got laser switch data.
So, let's just copy that and paste it in.
So now we've got a method to bind up laser switches to datas, but we don't have a laser switch data class or the list here.
So let's create both of those.
We'll copy laser switch data onto the clipboard.
Controllclick on coin data.
And I'll go down here and actually let's just select the entire class, duplicate it, hit that left arrow again, and enter and paste.
We'll replace is collected with is on.
And now I've got a laser switch data class.
Let's go back.
Next thing we need is laser switch datas.
If I just hit alt enter here and hit generate field.
Make sure not to hit rename.
I should end up with an object.
That's totally the wrong thing.
So I'm just going to replace this with list of laser switch data.
Now that said, it's I I really wish uh Visual Studio would get those right instead of uh making me have to correct the type.
But there we go.
We want this to be a list of laser switch datas so that they will get stored off.
All right, things are looking good so far.
We've got one issue left though, and that's that we don't have a bind method for our laser switch.
So, we're going to need to generate that as well.
I'll hit alt enter, generate a bind.
And inside of here, first, let's make this public.
We'll just set our underscore data equal to data.
And that autocompleted totally wrong thing.
So, I'll go back and retype it.
Hit alt enter and generate a field.
And then we want to use the is on state of this data object instead of the is on bool here.
So, I'm just going to delete this is on bool.
Delete that private keyword and then do a quick build because that's going to show me all of the parts where I referenced is on and then I can fix them.
So, just double click on it.
And here I want to use underscore data is on.
And in all of these other spots, I'm just going to copy and paste is on is on and is on.
Now, oops, got that twice and I just undid it.
Okay, let's see if I can get that correct in there.
Okay, there we go.
is on is true.
So the last thing that we need to do is deal with when we binding it.
When we bind it, we want to restore the state of our object.
If we just call turn on and turn off inside of our bind based on our data state, it's not actually going to work because the data state isn't changing.
If we call turn on with our data is on, well, it's already going to be on, so it won't do anything and it won't run this code in here.
So, we're going to extract out the code that switches on or deals with activating our switch or deactivating our switch and updating our say it's kind of our switch state.
So, to do that, we're just going to cut let's take lines 48 and 49 and actually let's do a refactor instead.
Hit alt enter and we'll extract a method and let's call this update switch state.
And then we only we don't this is only the stuff that we want to do if it's off.
So, I'm going to add in a check here for if data is um off.
Yeah.
So, if data is on, we'll do something else.
Otherwise, we'll do the off code.
There we go.
And then for the on code, we're just going to take this bit right here, 71 and 72, switching the sprite to the right mode, and calling the on method.
Finally, we need to call update switches from turn on so that we still run that code.
We just call the correct one.
And then in our bind method, right after we bind up the data, we'll call that update switch state as well.
Let's rearrange these real quick.
Get this update switch state.
I want to move this down.
Just cut it.
And I'll paste it down below.
All right.
And there we go.
That is our entire laser switch code.
Let's go check it out now.
So if I press play, I can see that I've got a laser switch datas, but I have no entries for it.
And the reason for that is simple.
I forgot to call our method.
So let's jump back into Unity and make sure that we actually call our new method from inside our game manager.
So we've got bind coins and see bind laser switches is light gray.
It's just because it didn't call it.
So duplicate bind coins, put in bind laser switches.
We go back in and now we should see our data bind up.
There we go.
You can see our laser switch is on or it's in here.
I can run across.
It turns on.
I can save my game and reload my game.
And it's back in the correct state.
If I switch it back off, I can save and reload and it stays in the correct state.
And go duplicate that switch.
Let's go make a yellow laser switch.
One and a two.
And we'll just drag these over into different spots.
There we go.
Save and play.
And we'll just go make sure that they all save independently.
And we can see multiple laser switches in here.
Let's just go double check that.
So, we'll run around.
We'll go select our game manager.
Go over here, flip some switches.
That's probably one of these.
There we go.
Flip another one.
Flip another one.
Let's flip that one back over.
Save and reload.
And things are in the exact same state again.
So, there we go.
We've got a nice simple setup for binding up our laser switches.
And hopefully you're starting to see how we can bind up any kind of data.
Although we are getting a little bit repetitive with the code.
So it's about to be time to start refactoring and making things a little bit more generic.
For now though, let's go into plastic and make sure that we commit our changes.
We bind laser switches to persistent data.
And we'll check that in.
Our current data binding system handles our player coins and laser switches, but it does the players in a slightly different way.
And if you take a look at our coin and laser switch code, they're almost essentially duplicates of each other.
They do about the same thing.
They find an object by name and then match up that data.
If the data exists, it m binds up to that data.
And if not, then it creates a new one.
And if we want to create new items that we want to bind to, for instance, items that we can pick up like our keys and blasters or anything else that we want to bind to, we have to copy and paste this code and make little modifications to it.
And I'd like to eliminate that and dive into a slightly more advanced topic of generics.
Now, you've used generics before.
You can use generics right here.
Find objects of type is searching for things using the generic syntax and finding all of the laser switches or the coins.
But we're going to use generics in a slightly different way.
Instead of just using a method that implements or takes advantage of generics like find objects of type, we're going to create our own bind method that takes some generics and allows us to generically bind up one object to its data.
no matter what type of object and data we have as long as they follow the same contract or interface.
And to start, we're going to create some interfaces and then we'll do our binding.
Let's start with the coin class.
Let's go take a look at our coin.
Our coin has a bind method and it binds to coin datas.
So, we're going to add an interface here that tells our system or our persistent system that our coins bind to a coin data.
We'll do that with an interface and let's call it ibind.
We're going to just add this at the end of coin and then we'll create the interface right afterwards.
So say ibind and we're going to give not ibindable.
Ibindable is part of the UI elements.
It autocompleted.
So we're going to do ibind and make our own.
It's part of the UI elements package.
So we're going to do our own one called ibind.
And we're going to bind to coin data.
We're going to give it the type of coin data.
And we don't have an interface called ibind yet.
So we're going to need to either generate it or go type it down below.
I'm going to create it right here in this file and then maybe move it over to our game data class later.
So, our game data file.
So, we've got an internal interface named bind.
Let's make this public real quick.
And it binds to a type of t.
Inside of that interface, we just want to have a single method called bind to the data.
So, now we've got this interface here.
Absolutely nothing has changed.
Though, let's go take a look at our game manager.
So in our game manager, now that we have our coin as an ibindable, perhaps we can implement a way to bind it up.
Let's go take a look at our bind coins method.
So here, remember, we loop through all of our coins, and then we find the coin data by name, matching it to our coin object, and then we bind it up or add it to our we add it to our coin data.
If it doesn't exist, then bind it to the actual object.
So let's add a method here that allows us to bind things slightly more generically that allows us to bind things that are ibindable to a type.
So we'll do void bind and we're going to take a type and then the data type and we're going to call this method bind and then whoops going to call I already called the method bind.
We're going to give it a parameter and the parameter is going to be a list of d and we'll call this datas.
So, this will be either all of our coin datas or all of our um item datas or laser switch datas or whatever other type that we want to pass in instead of passing in the level data cuz if we passed in the level data, we'd have to figure out which object to get.
So, we'll take our list or our bind method here and we're going to do the same thing that we do in bind coins.
First, we're going to find all of the objects that match the type.
So, I'll say var instances equals find objects of type.
Let's see, find objects of type.
There we go.
And then we're going to give it the type T.
It's going to find all of the objects of type T.
But now you see we've got an error here because it says the type T can't be used as a parameter in the generic find objects of type because there's no conversion from type T to object.
So let's go back to our or actually let's add a restriction here that says that T must be a game object or must be a MonoBehavior.
So we'll say where T colon mono behavior.
That'll get rid of the error here because now it knows that whatever type we specify here will be a MonoBehavior that has to be able to be getable with find objects of type.
So now that we've got all of the instances, let's loop through them.
So say for each instance and instances and then we'll find the data for that instance just like we're doing down here in bind coins.
We can pretty much follow along just rewriting the method a bit more generically.
We'll say var data equals datas because remember we're going to pass that in do first order default and here we're going to want to match on the name t do.tname is equal to our instance name.
Now we've got another error here because t.name does not exist.
Remember our coin data has a name on it.
So we're able to find it down below.
And our laser switch data has a name on it.
But our data object here this d does not have name on it.
So, we're going to need to be more specific and say that our data type must also have a name.
To do that, we're going to add in another statement here.
We'll say where don I named.
And we're going to need to generate an interface for I named that just has a name property on it so we can get that name and read it.
So, let's go generate an interface now.
We'll generate this down here at the bottom of our file.
And we'll add in a scroll down here a little bit.
string name and we'll add a getter and a setter because we're probably going to want to set that later.
All right, so we've got our I named interface and now our data line works.
We can now get the correct data from our list of datas.
If we don't get a data object back, just like on 94, we need to create a new one.
So we'll say if data equals null, then data equals new.
And here we're going to give it a new D which is our data type because it could be a coin data, it could be a level data or something else.
We'll add in our parenthesis there and then our let's put the braces so that we can assign the name.
We'll say name equals instance.name.
Now we're going to have an error here.
And again, this error is because we're not being specific about what type of data it is or what the data type has.
And here it says that we cannot create a new instance of variable D because it doesn't have a new constraint.
And what that means is that we haven't told this method that D is an object that can actually be nued up.
You know, some objects you can't do a new instance of.
Most of them you can, but in this case, we just need to be very specific and say, hey, this thing can be new by adding a new right at the end.
So, we add a comma after the I named and new, which just means that this part here, the data object, implements I named and can be instantiated.
So now that we've got a new data, we'll just say datas.add and we'll add in that data and then close out the braces and then finally call instance.bind and we're going to bind to that data.
Now we don't have a bind method on our instance.
So why is that? Well, it's because our t right here doesn't specify that it's also ibindable.
So we need to add that as well.
We've got our mono behavior.
We're going to do a comma ibind.
And I said ibindable, but I meant I bind.
and we're going to bind to D.
So now we've got this complicated looking method, but it's really just binding up types of T to data objects of D.
And we pass in a list of data objects of D.
D is our data type.
T is our object instance type.
So now that we've got that working, we've got that um completed, let's go hook it up instead of calling bind coins.
So we're going to go up to our part part where we call bind coins.
Let's see if we can find it.
Bind coins right here.
and we'll call bind and we're going to bind coin to coin data and then we'll pass in our level data coin datas.
Whoops.
Let's see if I spell it right.
Now I'm going to comment out the bind coins method and we're going to fix the last error here which says that the coin data cannot be used as a parameter D because the generic type because there's no implicit conversion from coin data to I named.
And that's because if we go over to our coin data, we added that I named interface, but we haven't actually implemented it.
So, we're going to add in an I named here.
And then that also means that we're going to need to make our public string here be a property instead of a field.
So, we're going to add a get and a set.
We'll save and do a build.
Now, if we just jump in and play and grab our coins, you'll see that there's actually an issue with the way that it persists.
I can go grab and collect all these coins.
But if I save and then reload, we're going to get multiple new elements and our coins aren't binding up properly.
And the reason for this is actually very simple.
If you look at these element names, notice something that's missing or these I I think I might have kind of hinted it there.
But if you look at these, notice that the name is here on our laser switches, not on our coin datas.
The reason for this is simple.
When we converted our property here, the name to be a property, it stopped getting serialized by Unity.
Since we're using Unity serialization system, we need it to be serialized by Unity for this stuff to work.
Otherwise, we're going to have to swap out our safe system, which is another viable option.
But an easy solution for this, so we can also see it in the inspector, is right at the beginning of our property here, and you can do this on any property that's got a getter and a setter, we're going to add a field colon serialize field.
I spelled that wrong, but if I can fix my typing.
There we go.
What this will actually do is take the backing field, the hidden backing field for our name property that's automatically created whenever you create a property.
It creates an like a a hidden name property that's going to be get and set.
When you call this getter and setter, it kind of autogenerates that code.
And this is saying, hey, for that field that you're autogenerating, serialize it.
That's all we need to do.
Let's go back into Unity now.
Press play.
And now when we look at that player data, notice that we've got all of the coin names.
Those are working.
I can run over here, collect things, save them all, reload.
I don't have duplicate data, and my state is correct.
Now, before we commit, let's do a quick diff on our files.
Just make sure we've got everything right.
So, our coin now just has that I bind interface in it.
We'll move that around later.
And then we've got our game manager which has the bind method and is no longer calling bind coins but calls the generic one.
And then we've also got our coin which has or our coin data which is now I named and we have that I named interface.
All right.
So with that I think we can commit that we've added generic data binding and check it in.
Now that we have a generic binding system, we're going to do a little challenge to make sure that it's clicking and that you're understanding how the binding system actually works.
So, what I'd like you to do is hook up the laser switches to use our generic binding system instead.
Remove the bind laser switches method or at least the call to it and use our bind method instead.
Go through the process of hooking up whatever it is you think needs to be hooked up.
See if you can figure it out and then follow along and I'll show you the steps.
So, go ahead and do that now and then we'll get going.
All right.
I'm going to assume that you've either paused and gone through it or again you just want to see the steps, but I would highly recommend that you've gone through it and at least tried it real quick because it's going to be very, very simple.
Let's dive into it now.
So, first thing we're going to do is go to our bind method.
Let's go find the part where we're calling our binds right here.
And I'm going to duplicate line 59 and comment out line 62.
We'll change coin to laser switch and copy that and replace coin data with laser switch datas.
And then finally pass in our laser switch datas.
Now, of course, we've got some errors here saying that laser switch and laser switch data don't match our generic types because they don't implement the two interfaces that we've created.
So, let's go to our laser switch data first and let's add the inamed interface.
And then finally, we'll just copy line 35 and paste it over 42 for speed.
So we can implement that interface without having to type a whole bunch.
Then we'll go back and just do control minus on my keyboard, by the way, or I have a a mouse key bound to it.
And then we've got to fix our laser switch itself, not the laser switch data.
So we'll go to the laser switch and we'll say that it has an ibind interface or implements the ibind interface and binds to laser switch data.
add in that closing one and don't let it add in a duplicate brace.
And since we already implement that method down here, we shouldn't have any errors.
It binds to laser switch data just like we would expect.
And then um that's it.
We're literally done.
Now our data binds up to laser switch data.
And hopefully you're starting to see the value here.
When we want to add in a new object type, we just have to implement those two interfaces and call this bind and our data should bind up.
Let's go test it out though just to make sure that it's actually working as expected.
So, we'll play.
We're going to run over there, smack some of those switches, and then save and load.
All right, we're almost in.
Get that game manager selected.
Scroll down here.
Do my save.
Let's go flip some of these switches over.
We'll just do those two.
We'll save and reload.
You can see that it switched state.
And now, let's just go flip that one over here.
and maybe these ones back.
We'll jump up.
Let's go over to level two.
Come back over here.
Jump back in.
Go into level one.
And my switches are still in the correct state.
So, my data is persisting and everything's working with our new generic system.
Hopefully, again, this is expanding your mind, giving you some ideas for how easy it's going to be to save any type of data that you want and for possibly ways that you can use generics in the future.
Whenever you got something that's super reusable like this where you've got the same pattern and you're finding yourself copying and pasting, generics might be a good option.
All right, let's go back in and commit our changes.
So, say that we've uh switched laser switches to use generics and we'll check that in.
All right, now it's time for items.
This is going to be a big section and hopefully very interesting.
We're going to get into refactoring a little bit, dive into editor tools and dig a lot deeper into data binding.
We're going to start with level one though and start by just putting out another item.
I'm going to take my yellow key here, drag it out.
So, I've got a yellow key one and um I think that I'll start with just that.
And then we're going to go save, pick it up, and just verify that nothing is persisting with our items.
I always want to do a quick verification, see what's happening, and that we're getting the same state.
So, I run over here, I grab that key, I go to my game manager, and I save and reload, and I come back in without a key.
Of course, if I went over here and saved and reloaded, then I would come with a key because I happen to reload right on the key.
But, of reload, and the key is over there because the key wasn't actually attached to me.
I just happen to save myself in that position.
Everything else is saving though.
My switches and my coins should still be saving.
Save and reload, but just not the items.
So, we're going to need to make a change and bind up our inventory to some sort of item data.
So, let's stop playing and go into our player inventory script.
Here's our player inventory.
We've got our items list.
We have our current item index.
And down at the bottom, we have that pickup method.
What we're going to want to do is save off any items that we've picked up and then be able to restore them.
And since we already use a game data system that stores off all of our data and binds through the game manager, we're of course going to follow that same pattern.
So, we're going to make our player inventory bind up to our player data.
To do that, we're going to need to add the comma here and the interface I bind again to player data.
Then we'll hit alt enter and generate the interface.
I'm going to leave this method blank for now.
Actually, let's just assign the data.
We'll say underscore data equals data and we'll add a semicolon.
That's because we don't have anything in our player data to bind up to.
We don't have any player data specific stuff or player inventory specific stuff in our player data.
Let's hit alt enter and generate this field real quick and we can go take a look at that player data.
So, hit control and click.
Go to our player data.
And right here, we don't have any inventory or item related data.
So, let's actually add some right now.
We'll add a public list.
Oops, that's not how you spell public.
public list of strings.
And we'll just call this items.
And make this a new list.
This will be the list of all of the item names that we've picked up.
And these will be unique item names.
Now we can go back into our player inventory and we could loop through all of those items and say for each see var item name in underscore data do items and let's just look in the scene.
We'll do a game OB let's say var item game object equals game object.find and we'll just try to find it by the item name.
This be our initial version.
If we find the object, then we'll just tell our player to pick it up.
So say if item game object is not equal to null and we'll get the um component that we need, the item component.
So we do item game object.
Try get component.
Give it the type of item.
And whoops, that's not it.
I item.
There we go.
I I hit the autocomplete incorrect there.
So we give it our I item interface and then outvar item.
So, if the game object is not null and we're able to get an item out of it, this will be true.
And then we'll have the item assigned to item.
And we'll just say pick up the item.
There we go.
Now, we're going to need to put some data into this data items list.
And we could probably do that right here in our pickup method.
So, just go right here at the end of it and say if data do items.contains contains and we'll give it our item.name and we we don't have access to that yet but we'll get it in a moment.
If it does not contain so we're going to add a not sign at the beginning or here let's just remove that and I'm just going to add a double equals false just make sure that it's very obvious and that there's no missing the not sign.
So if it doesn't contain it then we'll just add it.
We'll say underscore data do items add item.name.
Now I can remove these extra braces and we're going to need to get the name visible.
So right now our item is always on a MonoBehavior and MonoBehaviors always have a name property just like this this lowercase name.
But since it's not defined in our item interface, we can't access it.
So we're going to just go to the item interface and I'll just type it up here.
Public or not public just string name and we need a getter.
It has to be that lowercase one though to match the Unity naming setup they've got.
All right, now that should work.
We've got a bind method.
We've got a pickup method.
We've got some data.
The last thing we're going to need to do is go to our game manager and call this bind.
So, we'll add a bind to player inventory and we're going to bind it to a type of player data because that's what it binds to.
And we're going to give it our list of our player datas.
If I can find it.
Oh, not level data.
I've got the wrong thing there.
Game data.player datas.
Add that semicolon.
And then the Oh, last thing I need to do is go to our player data and make sure that it is also named because to bind we need to have the I named interface.
So, I'm going to just copy this right here, paste it right here, and then add our colon and I named so we can actually bind it.
Now, I should be able to do a build.
Looks like the build was successful.
I'm going to go back to the game manager, though, and just remove these two extra binding methods that are commented out, the bind coins and bind laser switches.
And I'm going to go down here and just remove these as well, just to make sure that we can clear up some of the clutter and keep our stuff easy to read and easy to manage.
All right, we should be able to test it out now.
All right, here we are.
We're back in Unity.
And while this is going to work, we do have an error message down below that we're going to need to take a look at.
First though, let's go grab the key.
Run back over here to the left, save, and reload.
And look at that.
We come back with our key and our switch is in the right spot.
If I go over to level two, well, my key is gone.
It doesn't exist anymore because remember, we're finding the key by doing a game object.find.
and that game object doesn't exist in the scene.
If I go back over to level one though, I've got my key.
So, let's take a look at this error and then we'll dive into how we're going to do that multi- scene persistence.
First, we get take a look at this log right here that says we've got an error in pickup.
There's a no reference exception.
It's in this pickup method on line 68 and it's being called by player inventory awake on line 24.
If we go click on line 24 here, you see that this is that part where we grab our blaster that's a child.
This is where we're automatically equipping our kind of default items or the ones that we've pre-attached to the player.
So, we're going to need to do something a little bit different here.
What's actually happening is if we go into our our pickup method, we're trying to um rebind to an item that's already got bound up that's already set up and hooked up to our player.
So, what we're going to do is add in an option to not add data for inventory items that are automatically added.
So, when we pick an item up, we'll just say whether or not we want it to persist.
If we don't persist, we won't add it to the items data.
So, here we're going to add an optional bool.
Bool persist.
And we're going to default it to be true for now.
That way, I can just pass in false on the one spot where I want to override it.
Now, this is an optional parameter.
You can always do this and just give it a optional default value.
I try to minimize these though, one or two at most.
Usually one is good though.
So here we'll go down to line 68 and we'll say if persist and the data doesn't contain that name already or the item list doesn't already contain that item.
Now we'll go back to the part where we're calling this pickup and we'll just pass in false so that we don't persist this item.
All right, let's go back into Unity.
And here we go.
You can see that the error is gone.
And I can run over and grab our key.
Let's just take a look.
Blast a little bit more.
Blast a little bit more.
Run over here and jump across.
And my items should still be gone, but I still have no errors coming into the scene.
I don't have that key until I go back into uh level one.
And now I've got my key.
And again, this error, if we go back to the code, I just want to show it one more time.
The root cause here is just that it's going through calling pickup and then down here in the part where it was trying to bind to our data items.
Items hadn't data hadn't actually been set up because the item hadn't been bound to yet.
So that's why it was throwing an error.
But we do need to not store this data off because if we stored it off anyway.
So say we like maybe did something to save that and then stored this off later, it would still be invalid because it would be data that we don't want to restore when we bind.
Otherwise, we would be calling pick up again when we picked up the item and restoring from the binding.
So we want to do one or the other and not both.
And removing or fixing the error here kind of it also has the side effect of fixing our binding order so that we don't end up rebinding the item.
So let's go back into Unity.
Make sure that everything was still looking good.
I can go back and forth.
I can save and I can reload.
And then let's stop playing and go commit our changes.
So go into plastic and say uh basic player inventory binding in same scene and we'll check that in.
Now we're going to let our player inventory restore items across scenes.
So, really we're going to let our game manager do that.
We'll let it keep track of our item prefabs and then spawn the correct object as needed.
Here in our game manager, if we're not able to find the item in the scene and just bind up to it, we'll just ask the game manager to create an instance of it and give us that.
So, we'll say else we add some braces.
And here I'm going to say item equals and we already have item declared up here.
So, we need to not redeclare it.
Just use item equals.
And here we'll say game manager.instance.get item and then give it our item name.
And then finally we'll pick up that item assuming that the item exists.
So let's first make sure that our item is not equal to null cuz it is possible that maybe we tried to persist and reload some item that no longer exists and we don't want to try calling pickup on that and then bugging stuff out even worse.
All right, let's call get item and generate a method.
And inside of our get item, we'll make sure to add some logging for that, too.
So, we want to be able to get any item in our get item method or any item that we have as a prefab.
And to do that, we're just going to start by creating a simple list of all of our item prefabs.
So, we can make something like a public list of I item and call this underscoreall items.
And then we could do something like bar or let's say string prefab name equals item name do substring.
And right now I'm using a naming convention.
Let's just go take a real quick look at it.
We're using one of the default naming patterns.
We're just doing an underscore after the prefab name and then a number for the instance.
So before we get into anything more complicated, I'll just use that as well.
we'll just kind of substring it and we'll take everything before the underscore and use that as the prefab name.
So say the prefab name is the substring from zero which is the start index.
So we'll start at the beginning of the item name and we're going to go all the way up to the index of the first underscore.
So to get that we do item name dot index of and then pass in our underscore.
So this is going to give us a string that's from the beginning to the first underscore and put that as our prefab name.
Then I'll say var prefab not var var var prefab equals all items and we'll just do a first or default which is just going to find the object or null if it doesn't exist.
And we create a lambda statement here where we'll check the name of the object against the prefab name.
Now, if we don't get back a prefab, this is probably where we want to do that error logging.
So, we'll say if prefab is equal to null.
Then we'll do a debug.log error that we were unable.
Let's put a dollar sign in here.
Unable to find item and then we'll give it the item name and our closing quotes and semicolon.
Then we'll just return null.
And at the bottom, assuming we got a prefab, we're going not to not want to return that prefab.
We want to instantiate a new instance of it.
So we'll say return instantiate.
Actually, let's create a new game object.
Say var ob new instance equals instantiate.
And we're going to instantiate the prefab.
And then I want to make sure that we've set that name.
So new instance.name equal to the prefab name.
There we go.
Um oh, we've got one other issue though.
Let's return our new instance and then figure out why is this a problem? Why is this giving us an error? But the problem is really lying with what we've got here.
We have an interface right now for an object that we're starting to use more like a mono behavior.
In fact, even if we comment out um let's say we commented out all of these lines and just returned null right here, we're also not going to be able to see our all items.
Let's go take a look at that real quick.
we'll fix it and then we'll come back to here and finish this up.
So, if we go back into our project and I go look at my game manager, you see we've got the game data, we've got our all game names, but this new public field that I've added isn't showing up even though it's public.
The reason again is because I item is an interface and interfaces don't get serialized.
They also can't be instantiated.
So, we're going to need to change this up a little bit.
And one of the easiest things that we can do is switch this interface away from being an interface into being an abstract class.
Since we know that they're all going to be MonoBehaviors for our items anyway, it makes it pretty easy to just create an abstract class that inherits from MonoBehavior.
Before I go in here and rename and change things though, I'm going to make the change inside of Unity first.
I'm going to go find the file, go find my I item, and rename it to be item.
So otherwise, if I don't do this, I'm going to end up with multiple files.
I might end up with an extra I items interface just sitting around inside the project if I try to rename and move things around with Visual Studio.
So I'll rename it, let it reload, and then reopen the script.
And now we'll rename this from I item to item cuz it's no longer going to be an interface.
Ah, my rename didn't work.
Well, let's change this to a class.
This happens sometimes where it just does not want to rename, by the way.
Um, let's try it again.
Crl R-r R-r R-r delete and it's not not going to do it.
So I I'll probably just manually do that.
For now though, let's delete out our three properties here.
We'll make our use method an abstract or a public abstract void method.
And we're going to make this actually an abstract class as well.
We'll make this inherit from MonoBehavior that it's already trying to autocomplete.
And I've already got my braces there.
I'm going to do a quick build again and then see if we can rename this item yet.
Rename to item.
There we go.
After doing a build and kind of completing it, the rename started working.
All right.
Now, let's do a build.
Find our errors.
We're going to have a couple of them here.
You'll see we've got cannot convert key to item.
That's because key is right now a MonoBehavior and an item.
We just need to delete the key part or the MonoBehavior part so that it's already it's an item which is already a MonoBehavior.
And then we need to change it up here.
We've got our use method.
We're getting an error here saying that our key does not implement the abstract member item.
That's just because we don't have the override keyword in here.
Since we didn't have the override keyword, it was trying to overwrite or uh replace and it's not exactly the same and cause some problems.
So well causes that error especially, but also would cause our inheritance and our polymorphism to not work exactly properly.
sort of deleting out those extra lines.
All right, let's do a build and find the next error.
We should have one for blaster as well cuz blaster inherits from item or had item as an interface or I item.
We'll delete the mono behavior there and then add the override here.
Save and build again.
I think we've got a successful build.
Now we can go into Unity and assign our couple of items.
Before we do that though, let's create an item folder to put our items in underneath our prefabs.
So, just right click on prefabs.
We'll hit create and create a new folder for items.
And then we'll just move over our couple items.
We don't have very many.
Really, just our yellow key right now.
We'll create a couple more in a moment.
So, we're going to want to have them in a folder nicely organized.
Let's go find our game manager and then drag our yellow key into our all items.
And then the last thing we're going to need to do in our game manager is uncomment out that code that we commented earlier.
Get our new instance spawning with the prefab name.
It should now compile now that we've changed that over to be a game object and not an interface.
And now if we hit play, I expect that we'll be able to persist our key across multiple levels because our game manager is staying around and just spawning that up.
Let's go try it out.
All right, here we go.
We'll run over, grab the key, switch between my two items.
Uh, let's see if I can make that jump.
And here we are back in here with my key.
Let's jump on this key or the flag again.
And I've got my items.
Let's go do a quick save and a reload.
And everything is looking pretty good except for we've got this one error here.
And if we take a look at this error, let's just go click on it and dig in.
Right here it's on player inventory.bind line 76 being called by game manager bind by handle scene load.
So we're loading into a scene binding up.
Our player inventory is getting an exception right here on line 75 because it's call the items is changing as we're iterating over it.
Now I want to present this as a small challenge.
See if you can figure out why this is giving us an exception and what the fix is.
The fix is pretty simple.
It really just requires a change to uh one line of code or I guess two lines of code and they're not in here.
So take a look and see if you can figure out what's going on and how to fix it and then we'll continue on afterwards and I'll show you the solution and kind of hopefully give you a good example and teach you how to track these down in the future.
All right, I'm going to assume that you've either figured it out or you're ready to continue on.
So what's actually happening here when we call bind? We're looping through our collection or our list of items and then we're calling pick up on the item.
So, we're either calling pick up on the existing item or a new instance of the item.
If we go to our pickup method, which is right above and see that we do some stuff, all kinds of other things.
Nothing except for nothing related to items though until we get down right here.
I've got items selected.
So, you can see it's kind of highlighting right there, which is a nice thing to do.
Another thing to do to kind of find some of these errors, just select the the loop or the collection that's causing the problem when you're getting these collection modified errors and hit shift F12.
You can also find them there.
So see that here there's a scenario where we add them, which is this line right here on line 69, which is the only place where it's modified.
So what's happening? We're looping through the items and then we're adding items to the list that already exist in there.
So realistically, we don't want this persist method to kind of default to true.
We probably want this to be false and only add items to this list if they're new items, not if they're things that are being rebound to.
So we're going to change this from a true to false.
And I'm going to rename this variable to is new instead of persist.
Now that said, there must be some scenario where we want this to be true, right? Or when we first pick up an item.
So let's go find that use case.
To do that, we'll hit shift F12 on pickup and then look for the spot where we call it from outside of our other code.
And that looks like right now it's in key.cs.
In our key method, we'll just pass in true as the other parameter so the item can be picked up.
Now, this does make me think though, hey, our on trigger enter for picking up an item is right here.
Shouldn't that probably be up one level in our item? Should that be in our key? It's only in our key right now because the key is the only item that we have.
So, it probably should move up a level.
Let's take this and cut it and click into item.
And then we'll paste it in.
Now, we've got a reason for an abstract class beyond just serializing.
We're also reusing our pickup logic, which probably makes a lot of sense.
Let's save and go back.
We'll go test this one more time.
All right.
And we've got no errors.
We've got a key that we've picked up.
Let's go over to the other level.
Our key is still there.
I come back and it's still here and we've got no problems or no errors down below.
Let's stop playing now and go into plastic and commit.
We can now pick up of items across scenes now works and we'll check that in.
In the last section, we introduced a new concept and now I want to take some time to talk a little bit more about it and that's the concept of abstract classes.
An abstract class is essentially a class that's incomplete and only partially there or one that kind of defines the way that things should work and usually does a tiny bit of work on its own.
It's a lot like an interface except it can actually do things like it can have an ont trigger enter 2D method where an interface can't.
It can also be serialized really easily by Unity where an interface also can't.
There is of course one weakness or downside and that's that you can only have one abstract class that you inherit from unlike interfaces where you can specify a whole bunch.
Now to use our abstract class, we have to inherit from it and create another thing that is actually using it or creating an instance of it.
And that's what we're doing with our key and our blaster class.
And when we inherit from an abstract class, if there are any abstract methods on it like that use method was there, then we must implement those methods as well.
Now, if we also inside of our key perhaps, let's go to the item.
Say we inside of our key also had this on trigger enter 2D.
Let's go back.
Then this method would get called instead of the item one.
It would actually use this one and never call the item one.
And in fact, that could be a problem if I hadn't changed that.
If I just left this right here and I had this other version of a pickup that didn't persist, then my keys would stop persisting.
So, I'm going to delete that real quick and then we'll take a look at one other thing to know about abstract classes.
So, here we are in the editor and I've got my key selected and I'm going to take my item script and drop it on.
And notice I get a nice little error here saying that we can't add the script behavior item because the script can't be abstract.
So, that's the other limitation of abstract classes.
You obviously can't assign them to a component or to be a component.
And that's of course because they're incomplete.
An abstract class needs to have something implementing it for it to be useful.
That's the entire idea of it.
If it's not in that scenario, if it shouldn't if it doesn't uh need something else, doesn't need some other implementation, then it probably shouldn't be abstract.
And maybe maybe it should be abstract and you should just move that implementation around.
It really depends on your scenario.
But when it comes to items, things like that, I prefer to have a nice base class, an abstract base class that I can use for all of my core item logic and to be able to reference them and serialize them all very easily in Unity.
So that's abstract classes for you.
I've done a few videos about this on YouTube.
We go deep and talk a lot about different scenarios with them, but that's really the core of it and what you need to know.
Abstract classes are partially done classes that have methods that can either be fully implemented or overridable.
And a lot of the time the core use is that you're serializing or using this object in multiple places and then overriding one or more methods inside of there.
A lot of time it's just a single method and that can be that can be fine.
That's what we've got here.
All right, let's uh continue on to the next section, I guess, cuz that's all I've got and there's nothing for us to commit.
With our current platformer components, we can build out a full game right now, but it's not very easy because building levels still takes a lot of time.
We've got to create prefabs, place them, stretch them out, and get them all exactly how we want them.
That's a lot of work.
So, in this section, we're going to dive into a way to simplify that process.
We're going to switch over to using the tile map system.
In fact, we're going to use the tile maps along with our existing stuff and kind of merge the two of them together and get the best of both worlds.
The tile map system will allow us to build out big giant maps by easily kind of painting and literally just painting onto the tiles just like you would expect.
It's a very easy to use system, but there are a couple of interesting things that you're going to want to make sure to pay attention to along the way.
Now, before we dive into implementing the tile map system, pulling it in, setting up the pallets and all of that, I want to start with a quick level design.
Let's create a level that would be somewhat difficult to build in our current system, and then see how easy we can put that together once we've got the tile map system set up.
Now, I'm going to draw out my level design, and I'd encourage you to draw out your own.
Maybe change it up a little bit.
Don't do exactly what I'm doing, but maybe steal a couple parts or pieces from it.
So here I've got just an empty paint document.
I try to keep it as simple and unopinionated as possible.
You can really draw in whatever.
I usually just go with paper, but paper is a lot harder to represent digitally and show you on screen.
So let's start with something simple.
I want to have at the beginning of my level, let's just start with my player right here.
Let's get my little player right there.
At the beginning of the level, I want to have the end piece kind of already visible.
So, I want to have the exit be right up here near the entrance.
And then I'm thinking I want to have like a little teleporter here, a door there that you have to get to to jump over to the flag and make it to the next level.
So, you'll see that kind of exit right from the beginning.
From there, I think I want to go over and let's introduce a couple little basic concepts like jumping.
We'll add a couple little jump platforms.
Maybe add some coins here they can pick up.
Get a couple little things right at the beginning.
And then let's do a pit.
So go from there.
They'll go down into thinking a big pit.
And I want to fill this up with little frogs.
Those are my terrible repres.
Let's write frogs.
That'll be my representation of frogs.
And then here, let's do a bunch of uh one-way platforms to kind of jump up.
And I'll make the exit up higher.
So kind of fall in.
If you fall down to the bottom, you might hit some frogs.
And then you got to jump back up and get over the ledge.
From here, I think I want to do a ramp.
That's something that's pretty difficult to do right now.
Let's do like a a sliding ramp down here.
They'll kind of they'll go down that way.
And then maybe into um let's do like a water.
We have water already, so let's add some a little flat area here.
And then some waves.
In fact, maybe I could even put I don't think I want to put a boss fight here.
It's a little too early, but I could put something here.
It's a little bit interesting.
Maybe.
Let's do um another lump here.
And then um think how do I want to do this? What do I want? Like the uh thinking I want you to do some swimming here.
See what that's like.
Um and then yeah, I'll just add some platforms.
I'll just add a couple platforms that you can jump up to get or do I want to add moving platforms? I'm trying to think of what I want to put here for this water.
So I'm thinking I want them to go down.
They get to some water and then they've got to get up over this edge by um jumping out of the water onto some little platform here and then jumping up over I think that that's probably fine for now.
I'll figure out if I want to make it more complicated later.
I'll go down here once I get up onto this.
Oh, you know what? Let's put a um an enemy here.
So, let's put we've got that cat.
Let's put the cat right here with his little tail throwing grenades.
Boom.
So, he's throwing grenades over there and then you're dodging them while trying to get up.
And if you end up Yeah, that seems okay.
That'll maybe work.
Maybe I'll change it up a little bit, but we'll see.
Then from here, let's add a little platform and um actually, you know what? Let's just go straight to like some lava.
Let's do like lava and moving platforms over the lava so you don't want to fall in.
Do like a left right platform.
Maybe another left right platform.
Um, and then we'll go over here to the end.
And at the end, I want to change things up a little bit.
I'm going to switch colors.
I'm going to go to gray.
And I want to put like a castle here.
We have some nice castle tiles.
Do like a castle entrance.
And then in here, I'm thinking like some sort of a a maze.
Oh, you know what? Let's do a Let's add a break here.
Thinking like let's let's do this.
This would be like one castle and then another castle with a bridge across and like a little kind of maybe like a little maze puzzle thing where you got to jump up and then get kind of up to the top and then run across, come down and then grab a little key.
Actually, let's add the key in yellow.
So key down here in this corner somewhere.
So, I'm not sure exactly on this part of the design, but I've got I think the the first part kind of figured out.
And uh Oh, yeah.
With this key, we'll probably want to have a door, too.
So, we'll add one of those.
Let's add another door to the beginning, too.
And go down here and just add a little door right there with a yellow lock.
So, this will be the uh the lock that we go get the key.
So, we'll see from the beginning that, hey, we need to go get a a lock to open up this door.
You know, maybe I'll um think about it more.
Maybe I'll move that up a little bit.
So, put it on a platform like right up there.
Oh, let's go into paintbrush mode.
Put on a platform up here.
Um with a key.
So, there's like Oh, whoops.
Yellow yellow door with a yellow key.
So, you could jump up to there.
Maybe we'll add another platform so you can make it up there, too, so that it's visible.
Or or maybe I'll drag it down here.
I'm not sure.
I want it somewhere though that you kind of jump up, you got a key, you can get to it.
Um, you got a key, it'll unlock and open the door, then you can go through that door or kind of enable that door.
So, that's that's the plan.
Um, I think I also probably want to add a little piranha or something here.
We've got the the fish character.
So, I'm thinking maybe we'll add a um Whoops, that's erase mode.
Add some fish or one or two um fish swimming back and forth shooting off some spikes as well to make the the lava a little bit more um a little bit more threatening.
And maybe we'll add a boss over here.
I don't know something there.
Probably some sort of a challenge there in addition to the puzzle.
But that's kind of the core design.
And again, I think you should build out your own design as well.
You know, kind of copy this, take some good parts, take some other ideas that you've got and put them all down on a page.
And then I'm going to show you how we're going to go about building that in the next section.
All right, we're back in Unity and it's time to set up our tile map.
The first thing that we're going to do is create a new level to build on.
So that way we don't end up overwriting our existing stuff.
We can go back and forth and take a peek at what we've done before and see what we might want to reuse from there and not overwrite those changes.
So we're going to start by just saving our level one as a level three.
So I'll go file and do save as.
Make sure that I'm inside of my scenes folder and I'm just going to name this level three or whatever your next level is.
So go ahead and pick if you have more levels, use whatever.
Next, I want to disable the environment.
So, we've got this entire environment object here that has most of our environment objects or most of our world objects, the ground pieces and everything else underneath it as children.
So, if I just disable that, should see that most of the world except for these more interactive parts just kind of disappears.
And we'll worry about these interactive parts later.
We'll probably just remove them from this level.
In fact, you can just go to the B encounter here.
Let's do that.
And just uh disable that as well to kind of clear this out.
So, we've got a little bit emptier, more of a blank level to start with.
All right.
Now, we're going to begin our tile map system.
There are a couple things that we need to do.
First, we're going to need to create a tile map.
And then, we're going to need to create a pallet.
To create a tile map, we're going to go to game object, 2D object, tile map, and choose rectangular.
That should give us a grid with a tile map underneath it.
I'm going to name it environment, and hit enter.
Now, if you don't see the tile map option there, make sure that you've got the tile map package imported.
You should have it in if you created the project the same way.
But if not, you can go to package manager and then inside of the Unity registry section, scroll down and you should find the 2D tile map editor section.
Grab that, import it, grab the latest version, pull it in, and then you'll be able to create your tile map.
Now that I've got my tile map created, you can see I've got grids here, but um they're all kind of blank and there's not an easy way or visible way to do anything about that except for this little button here, the open tile palette.
And that's what I want to do.
I want to click this and it's going to pop up a new window.
Mine popped up off screen and it's a little bit small, so I'm going to make it nice and big.
We want to make it big enough that we can see everything in here cuz we're going to be creating a palette in here, setting up all of our different kind of paintbrush pieces that we're going to use and then painting with it.
So, to begin, we've got an environment here, but no pallet.
So, we have this environment is showing us which tile map we're on.
That's this tile map right here that's selected.
And the pallet is what we can paint with.
We can create multiple pallets, and that's what we're going to do.
And we'll separate the pallets out based on their use.
We'll do some for environment, some for the background, and then we can do some for other things like props or whatever types of things that we want to separate out on.
Let's do a create new pallet, and then we're going to name this environment.
I'm going to hit the create button.
I'm matching the names, but the names don't have to match, by the way.
So, just because I matched my names doesn't mean that they all have to match.
Now, I'm in the art folder, and I think I'm just going to drop this tile map into my root art folder right now.
and then I'll probably move it into a tile maps uh or tile pallets folder afterwards, but I think I'm just going to leave it in the root for now.
Now that I've got my tile pallet created, you'll see I've got environment here for my pallet and I'm on that map or the tile map named environment as well.
I can go into my art folder, go to my ground subfolder, go to my grass folder, and I'm going to select all of these grass icons.
So, I hit control A.
Make sure that they're collapsed though because if I have one selected like that, and I hit control A, this isn't going to work.
So, I'll collapse them all, hit control A, and then drag them right into this tile map area.
You can do them one at a time, but I find it's a lot faster to do them all at once.
Now, for this folder, it's going to generate tiles into a folder or into whichever folder I've selected.
I'm going to make this match with the visual tiles where the PGs are or the Yeah, I guess these are PGs.
All of our grass sprites.
So, I select that same folder and now you can see I've got my grass tiles here.
I can zoom in and out with the mouse wheel.
So, if you don't see it, just make the window a little bit bigger or grab this bar and drag it up.
There's also an option over here to hide the bottom part.
I turned that on and off so you can see um just the visual change there.
You can drag around with the m middle mouse button to pan and again zoom in and out with the mouse wheel.
Now, it's time to do some well tile map editing.
First, before we draw onto the tile map, let me show you really quickly how we can modify our tile pallet.
So, let's zoom in.
In fact, let's make this much bigger.
And let's say I just wanted to rearrange this.
You don't have to rearrange this, by the way, but there are some nice benefits sometimes for rearranging it.
And it's important to know how to rearrange it.
The biggest benefit is that you can select areas of the tile map and paint with them.
But if I selected this as a brush and painted with it, it would look kind of weird.
I might however want to make like a little platform though that's got a center piece like this, a right piece and a left piece.
To do that, I can go into tile map edit mode and then I can go select the piece that I want and then just click over here and paint it down.
Now, that does give me two of the same tiles here.
So, if I wanted to remove that, I could I could just go in and hit the erase button there and clear that out.
But it doesn't hurt to have multiple of them in there.
Especially if I want to create different sections like this where I've got this little platform that I can then just go out and paint.
Now, speaking of painting, I think it's time that we give it a little try.
First, let's take the tile palette and we're going to dock it down here.
I'm going to grab it and dock it right here on Let's go with the lefth hand side of the project view for now.
Thinking the right hand side might be better, but I'll leave it there for now.
And I'm going to select this tile right here, the middle one with the grass.
And then we're going to go into paintbrush mode.
In paintbrush mode, wherever I click, a tile will appear.
So, I can just click and drag.
And you see the tile appears.
I can drag down here.
Oops, I get some extra tiles.
That's okay.
I just go over to the eraser and hit erase.
Now, if I want to draw a grid or a big chunk of ground underneath it, I probably don't want to go like this and start painting and dragging all around.
It's a little slow.
So, I just use the fill area or the paint a filled box, which is U for the hotkey.
Click, drag, and now I've got a nice big area.
again.
Mouse wheel to zoom in and out and left mouse to move around.
So now I've got the core of my intro part or the that base piece that I had.
Let's take a look at my map again.
All right, here we are.
So I've got my character is going to start right here.
Then I wanted to have a wall up there with a flag on it.
So let's add a wall next.
Let's find um well, let's see.
What do I want to add for a wall? I guess we could just use a big piece of dirt for now.
Do a big tall wall right here.
In fact, I probably drag this out a little bit so that it goes way past the edge of the screen.
And then we'll put a little ledge up there.
So, I want the ledge that looks like Where's the one that I want? I Is it this one? I'm thinking it's probably that one.
And we'll put one of those like right up there.
Let's see.
Zoom in.
Oh, that doesn't have a rounded corner.
Oh, that's the one I want.
Oh, here.
There.
We'll just add two.
And then I'm going to take my flag.
And the flag I'm not going to do as a tile map piece because these flags are interactable objects.
And while you can make tile map pieces interactable, it's not quite the same and it it's quite a bit more complicated and it'll add a lot of complexity that we won't really gain anything from.
So for our interactable object, we'll just place it right up here.
So now I've got the beginning of that level for real.
I've got kind of the the key piece up here that I want to show them, and I've got a bunch of extra junk.
But if I save and press play, I'm going to expect that my character is just going to fall right down through the ground.
Let's hit play and watch.
So, the reason for that is pretty simple.
When you're building out a tile map game, you probably don't want colliders automatically everywhere on the tiles, right? I mean, just like sprites, we don't want everything to have a collider on it.
So, we have to tell the system what should have a collider.
So, we're going to go to the grid and go to the environment object or the subobject there.
And we've got our tile map and the tile map renderer.
We're going to add a tile map collider 2D.
You add that tile map collider 2D.
We leave all of the settings default for now and press play.
And we should now find that our character can land on the tile map and land.
Let's see.
Can run around.
I can hit that wall just like I would expect to.
And I can even almost make it up to that flag.
You can see I can jump and get pretty close.
Things are looking quite a bit better.
So, let's save and take a real quick look at what we've done in plastic.
So, if we go to plastics, see the project settings is not important either.
Is that temp one? We've got our level three.
That's that's something we've actually added.
And then we've got all of these ground assets.
So, these are the tiles that we've created.
You can see over here to the right that it's got a couple of fields on there.
We've got the sprite showing which sprite the tile is for, obviously.
The color if we want to have some tinting, and then the collider type.
We can have none, grid, and sprite.
If you're curious what those do, the none option just makes it not have a collider.
Pretty obvious.
So, if you want to have a section with colliders and have a specific sprite that doesn't have a collider, you can just set that to none or that tile type to none.
If we use sprite, then it will use one based off of the sprite's outline.
So, imagine we've got our ramps.
We're definitely going to want those to match with sprite.
And then, of course, there is grid, which just matches with the cell shape.
So, matches with the actual grid.
So kind of just gives us a square in this case.
Other than that, the only file that we have changed is our environment tile pallet down here, which is this this prefab.
So let's say that we've added our first tile pallet and commit our changes.
Added first tile pallet and started level three.
And we'll check that in.
All right.
All right, now that we've got our tile map and our pallet, let's do some more level building.
Now, we're I'm going to go through the process of building out most of this entire level minus the boss fights and let you kind of follow along.
And again, I'd recommend that you follow along, but make your own modifications.
Add in some different tiles, add in some different, you know, designs and make it your own level as well.
Don't just copy me because that's not nearly as interesting and not nearly as much fun.
All right, so what we've got here is just this beginning part.
I've got my character.
I've got the flag there.
I want this other ledge up there with the door.
And then I want to add in these two ramps and the coins next.
So, let's start with um let's just add in a little platform up top.
First, I'll show you that part that I was talking about where we can select and paint big pieces.
I'm going to begin by just copying this platform and pasting it over to here.
I just got to make sure edit mode is on and it looks like it is right there.
So, I'm going to use the eyropper.
We'll take the right piece and then paste it over here.
And then I'm going to go remove that duplicate right piece and then use the eyropper again.
I'll click and drag to select these three pieces.
That's that kind of platform.
Notice that's now on my clipboard.
And I can paste it.
I'm thinking I'll put it like uh I'll put it over here.
I want it to be somewhere off to the right where you can see it, but you can't kind of make that jump.
Thinking maybe like about there.
I might have to move that up a little bit higher later, but luckily that's pretty easy.
All right.
So now I've got my platform there that they're going to jump across.
And that should match up.
Let's bring up my platform one more time.
That should match up with kind of this.
So, it would probably Yeah, it's going to be a little bit more to the right, but let's add these other uh platforms to go up and up.
I'm going to do that next.
So, we'll zoom out.
I'm going to go to the normal tool.
Let's go eyropper.
We're going to take the ground piece here.
And I'm thinking this will be up like two.
So, right around there.
Probably maybe like five wide.
And then we'll go up and over again.
Is that six? Did I go five or six? One, two, three, four, five.
Okay, cool.
Five and We'll do five and five.
Then I'm going to add some ground underneath.
Oh, it's not ground.
Where's the fill? Phil, fill.
Phil, where are you? Did I lose my ground mid somehow? Did I I must have painted over it.
Okay, not a problem.
Let's go find that tile.
So, if you lose a tile, I've got my grass mid right here.
Somehow that disappeared.
I Oh, no.
That's not the one I want.
I want the grass.
Where's the center one? Grass center.
If you lose a tile, you can just drag the actual tile right back out.
Grass center.
This is it.
Where's grass center tile? There we go.
Oh, the tile is wrong on that.
Oh, never mind.
It was just my clipboard was showing it wrong.
Got it.
So, there we go.
I've got my center piece again.
I don't know how I accidentally deleted that.
Got that selected.
Let's go select that.
And then we'll go to the paint mode and we'll just drag and fill.
So, we're going to drag and fill to there.
Let's try that again.
Drag and fill.
Zoom out a little bit.
It'll work better.
And then drag and fill.
Gonna get this whole uh whole ground area laid out.
So that gets me this and this.
I want to move that piece over and get my coins over there.
So let's go find all of my coins.
Next, I'm going to go grab my coins that I've got.
I've got a couple of them here.
I'm going to take uh let's take one, two, three, four, five coins.
I'm going to move them up here.
And I'm thinking I want to make them linear.
So go L 1 comma 5 and then a Y of zero.
There we go.
And then I'm going to click and drag them.
So the L one to five, by the way, just split them out one meter a piece.
So you do L is linear.
And then the distance, the start position and the end position.
So one and five are the X values that we would give it.
And then it will distribute them across.
So give them 1 2 3 4 and five.
And then that just put them 1 meter away from each other.
Now I've got a couple coins nicely placed.
Uh these other coins, I don't know what I'll do.
I'll move them around.
I'll use them later.
I'll just put them up here for now.
I I might use them later.
I might just delete them.
In fact, yeah, let's just delete them.
Clean things up.
No reason to leave coins here if I'm not actually using them yet.
All right.
So now we've got that done.
Let's move this platform next.
So I said I didn't like that position for it.
I'm just going to select it.
Let's do the do that.
And then we'll paint it.
Thinking like up here.
There we go.
And then erase the previous one.
All right.
Next up, we're going to do a pit.
So, we'll do the big pit with the frogs in the bottom.
So, to do a big pit, pretty simple.
Just go down here.
Oops.
Go select the eyropper again.
Grab my ground piece.
And we'll just do a pit that starts like down here.
And then we'll fill in that ground below it.
Ah, whoops.
I painted over my I should get out of tile edit mode.
Then I won't accidentally paint over my tiles.
It's a much better option.
All right, there we go.
Now we'll add that sidewall again that they've got to jump up.
See, it's going to be up like this or so.
Let's go take a look at that.
So, they come down and there's these little platforms going up and then there'll be a big ramp and then a drop off.
So, let's do the big lift up here.
Go up maybe even one or two more higher.
And then we're going to add some platforms in here.
We'll add oneway platforms in just a little bit.
Let's add the ramp going down next because I think that's a slightly more interesting and important part.
So, to do a ramp going down, first we're going to want to put some grass at the top.
So, go select my grass, go zoom in, and take a look.
Okay, grass looks good.
Next, we're going to add a corner piece.
So, take this corner, just drop it right there, and we're just going to go all the way down one at a time, filling in these ramp areas.
Now, there might be a way you could put together a nice, and there definitely is a way you could put together a nice tool to automate this, but um it's a lot more work than it's worth for just doing a couple ramps.
So, we're just going to put this in manually and just drop in paint in our couple quick ramps.
You can see how easy they are to paint in.
They go pretty quick when we've got a system like this.
And it's super flexible.
All right.
Next, we'll add in the grass center pieces.
So, that's going to be this.
And here, just go straight down a lot of time.
Just kind of going straight down from here until Oops, that's too high up until we kind of fill in the area.
The problem is you can't go below.
Um, you can't go to the right of the tile there at the top.
So, got to kind of just go down and slowly say slowly, but it's not really that slowly.
Some somewhat slowly fill them in.
All right, almost done.
Oops.
Got one little miss spot there.
And then finally, some more grass down here.
You can see how easy this was.
Oh, and then we've got a a spot for our little triangle right there.
Bam.
Now we've got a nice beautiful ledge that is just going to work and we didn't have to do a whole bunch of extra work to create it.
Looking good.
Now at the bottom of this I wanted to create some water and we're going to do water a little bit differently because our water's collider won't be the same as our regular tile map collider.
We're going to want to change that out and we're actually going to create a separate tile map for that.
So as a placeholder I'm just going to put in some grass here and then well actually let's uh let's add in a water.
Well, no.
I'll just add in grass.
We'll do some grass that's very obvious like this little platform here.
Um, that's going to be water.
And then we'll fill that all in in the next section when we add in the water tile map.
So, now I'm going to add in we'll put water right there.
Then we'll go up here with another ledge.
Just kind of matching what we've got here.
So, we'll go back up and kind of match with that ledge height.
And we're going to put a big old cat, an enemy cat right up at the top of that.
So, let's go up like that.
And then, oh, okay, we got to go down one more block.
And I think I want to expand this out like four wide or so.
We'll add some grass to the top.
And then we've got our cat.
Let's see if we can find my cat boss in my prefabs folder.
There we go.
And we'll just add him right up.
Oh, let's get out of uh out of tile mode.
W.
There we go.
And uh oops, I moved my cat around.
See? control shift F and zero on the Z.
That'll move it directly to the center.
By the way, on 2D projects, hit control shift F, move that Z position to the zero, and you got your uh your object right there in front of you.
So, here's our cat showing up.
I think he's looking good.
We just want to flip him around so that he can fire.
And let's just go double check my pool manager.
I know that I Yeah, I lost my cat bomb prefab earlier, so I'm just going to go reassign that in here.
And then apply overrides.
Okay, cool.
So now we've got our cat added.
The next piece will be a lava pool which probably also be a separate layer just like the water like I was talking about.
So let's add that out and then add in the castle piece and we'll start putting together those other layers.
So let's add in our lava area.
And I'm thinking again we'll just do a short little thing here.
So this will be the Oops.
Let's clear that out.
Didn't mean to paint like that.
I want to use the drawing tool so I can do a bigger line.
Thinking like maybe like that with lava and then a couple moving platforms here.
So I believe we have some moving platform prefabs already.
So we can just go take a moving platform and just drop it right up in here.
Got one.
Let's just duplicate it and add another one.
I'm thinking we'll have like yeah three platforms should be good.
And we can adjust the size and look at those in just a moment.
And then we'll go back to our tile.
And the final thing we have is the castle area.
So at the end of the lava, I want to go up onto some grass and then go into a castle.
So we'll say ground right here.
And again, this is all going to be lava in just a moment.
We'll add in a little piece of grass to the edge right here.
So we got this little uh Oh, no.
Let's just go with um a flat one.
the flat one without that icon there or the graphic the circle little cutout spot there.
And then we're going to go into castle area.
So for the castle, we're going to need more tiles.
We're going to need to have the actual castle tiles.
So go back into my ground section and I believe it's stone that shows all of the castle pieces.
Ctrl+ A again.
Select them all.
As long as it's all PGs and shows up as the texture settings up here, texture import settings.
Nothing else is in there.
I should be able to just drag them over and then put these into the stone folder.
And suddenly I've got a bunch more tile maps or a new bunch a bunch more tiles in my tile pallet.
All right, I'm going to take the castle piece and just draw out Oops, that's not it.
Draw out a big square for my castle.
I'm thinking it's going to be like I don't know around that big.
Looks like a decent size.
We'll put in a ground piece like the top that the player will walk along.
And then we're going to add in a couple more spots.
So, I want to have like a a left hand side of this, like a wall, I think.
Um, and have one of those big entrances and uh probably a couple platforms in the back.
But I think we're going to need some more castle graphics to really make this the way that I want.
Thinking about it, I think I'll go to the KennyL page and grab a couple more of those.
So, let's just plat let's uh kind of placeholder this out for now.
Get a rough idea of what we want.
So, I'm thinking we've got the big castle and then two like a split there and a bridge or something.
So, do like a big castle like this and then maybe another big castle like that.
And then this would be these will be like the background pieces and then the key is going to go over there.
So, the capsule part's not quite done, but we've got the rough layout, I think, of what I want to put together, and I'm ready to move on to adding in our new layers and setting up the rest of the tile map sprites.
So, let's save our scene, go into plastic, and say we've added initial level three design, and check that in.
It's time for us to dive into water and lava.
So, how are we going to deal with water and lava in a tile map situation? I mentioned before that we don't want to put them onto our basic tile map or our main environment one because well then they're going to collide just like they would normally with the player, right? So, our player would just walk on water.
That's not really the effect that we want.
And if we landed did the same with lava, well then obviously we'd have to do something special to make all of the lava tiles do damage as well, too.
So, let's actually start with the lava and then we'll dive into water because it's tiny tiny bit more complicated.
So, for lava, what we're going to do is take our three lava sprites right here.
And in fact, I think yeah, just the three lava sprites and then drag them right over to our tile palette for our environment.
I'm going to put these into the correct folder.
So, that's in art and tiles where the lava tiles are.
And now I've got my lava tiles in here.
So to paint my lava tiles out, I'm in my lava section.
I could just select this and start painting and dragging these out.
But then they're going to be on this environment and I'm going to have that problem where I can walk on them.
So what we can do instead is I'll just hit control-z.
I'm going to go to the grid.
I'm going to go to game object 2D object and I'm going to go to tile map and rectangular.
And look at that.
We've got an additional tile map.
I'm going to call this lava.
And then on that lava tile map, so I'll select lava right here.
We're going to draw out that lava.
So, select the lava, zoom, zoom, zoom, zoom, zoom.
Let's see if I can get over there.
Yep.
Mouse wheel and middle mouse button worked just fine.
Oh, but my painting didn't go down.
There we go.
So, now I've got my tiles.
And you can see that the grass is actually behind them.
It's actually painted onto that layer behind them on the other tile map.
So, I also want to go disable the lava temporarily, go back to the environment tile map, and make sure that I erase those because I don't want this grass piece just sitting back there and the player running along it.
So, we'll just delete all of those and then reenable the lava.
So, now I've got my lava.
I can see the lava showing up again.
I'm going to add in the pieces underneath the lava.
So, I'll just click and grab the box mode.
There we go.
Not paintbrush mode.
And drag it all the way down so that we've got lots and lots of lava.
Now I need to add in a collider.
So we're going to add our tile map collider 2D just like before.
So what's the difference? Well, we're also going to add the damage player script to it.
So if we add the damage player script to the lava, any tile that they hit that has the collider on, which is going to be by default all of them, is going to cause them to take damage.
So let's save our scene now and move our player out and just verify that I'm not crazy.
So, I'm going to select my player, control shift F, zero out that Z position again, and then save, and press play.
Got our player right there.
Expect he's going to fall down, hit the lava, take some damage, and go bouncing up.
Boing.
Look at that.
Taking damage.
Everything is working as expected.
And if I'm able to get over here to the ground, look, there's the cat.
There we go.
You can see everything is kind of mostly working.
and jump down here and fall into the pit where I'm going to put our water next.
So, let's stop playing and let's go do the water next.
So, for our water, we're going to add in another tile map.
Go grid, game object, 2D object, tile map, and rectangular.
We'll call this water.
And now, of course, we're going to create our water tiles.
So, select all three water tiles.
Drag those down as well.
Put these into the tiles folder.
And then with the water tile map selected, we'll go down to our section that's going to be water, which is right here.
And we'll just paint on our water.
So go select my water, paint it right over.
I'm thinking uh let's do it even on that entry tile.
So they slide right into the water.
But then, of course, that also means I need to remove those tiles from the environment.
So I'll disable water.
Go to eraser mode.
Bam.
Turn water back on.
And look at that.
I've got my nice, beautiful water.
I got the wrong water visual, though.
So, I'm going to switch it to the water top.
Oops.
Am I on the right wrong layer? Control-r Z undo.
Let's go to water layer here.
Drag and draw.
Perfect.
And then we want to Oh, I accidentally added an extra spot there.
I want to fill in the bottom part here with our our square water.
Like that.
There we go.
That's looking better.
So, now what do we do for the water? How do we make that work? Well, we're going to add our collider just like before.
See? Tile map collider.
But then we'll just add in a buoyancy there.
I cannot spell buoyancy.
So add in our buoyancy 2D.
And on our tile map collider, we'll just hit the used byector.
And then of course uh is trigger because it's a water.
So it has to be a trigger with theector in there.
And now I can press play and move.
Let's uh move our character over there though.
So control shift F or W.
Here we'll just move them right there.
play.
Watch him drop down and fall into the water.
All right, there we go.
And you can see that I'm sitting way on top of the water.
So, we'll just go to the water section here and start adjusting our surface level and our density.
So, I think I actually just want to turn the density down to whatever it was, like a 0.5 or 0.2.
I've forgotten my value now.
Yeah, 0.1 seems about good.
And then finally, of course, we've got to adjust the layers.
So, let's uh right, if I do it at runtime, it's going to not save.
So, if we change that to water, you see that's what it should look like.
So, we know that that needs to go to water, and that should go to a 0.1.
Let's stop playing.
Change this to a 0.1.
Change our sorting layer over to water and save.
So, now we've got water and lava both working.
I'm going to commit that into plastic.
Water and lava both working.
And we'll check that in.
Before we dive into our castle tile map, I want to fix up the beginning parts that we've already created.
Let's go take a look.
If we press play now, first thing that we're going to see is that our platforms are flying over to our face.
You can see the little indicators of them there.
Let's see.
See that? that starting platform.
Those are the moving platforms.
It's because we placed them, but we didn't set their positions.
And also, I feel like our jumping and our movement is probably a little bit too strong.
I can almost already jump up to this platform here, and it's going to be very difficult to limit and kind of set my player bounds if I can jump and move exactly as fast as I can.
So, I'm going to make a couple quick little changes.
First, I'm gonna find my player and I'm going to figure out a slightly lower jump value and maybe a slightly lower speed.
I'm thinking maybe like a 3.5 and a 3.5 for the velocity so that he still moves pretty fast but not too fast.
And when he jumps, it takes a double jump to get up like these ledges here.
I don't want a single jump to make it up, but double jump seems good.
Now, getting pushed by that thing is definitely a problem.
So, I'm going to stop playing and then go reset my player values.
3.5 and 3.5.
Of course, you can come up with whatever values you want, but I think this is a pretty good number based on the size and scale that I'm going with.
And then we're going to go adjust these moving platforms.
See, we've got the indicators for them, the gizmos over here to the left.
And that's because we haven't used the rightclick menus to set position one.
And then go over here and rightclick and do a set position two.
Remember, this is how we determined where it would move.
So, now it'll go from that spot to that spot.
Let's do the same for these other two.
I'm just going to do a let's say right now that's probably a good end position.
So I'll do set position two.
And then I'll drag it over here a bit and do a set position one.
one.
one.
Then I think I'll do the same thing for this middle one.
Let's go over here will be position two.
And then to the left a bit will be position one.
All right.
So now my platforms should move right.
And I should be able to jump about the right amount.
Let's press play and see.
So, run over here.
Go grab my key.
A double jump gets me up.
A double jump gets me up.
And now I can double jump onto this platform.
I can't quite Oh, I missed my jump, but I definitely could have made that.
And then I'm down here in the frog pit and I'm going to need a way to get out of here.
I wanted to fill this up with frogs.
The frogs happen to already be here kind of perfectly lined up.
Um, let's move myself up.
So, drag up.
Let's go to 30.
Oh, I'm not on myself.
That That's the the moving platform.
Grab my character.
There we go.
Move him up and uh to the right.
Just kind of cheat him up there.
There we go.
Run down a ramp into the water.
All right.
What's going on with the water? So, water layer is definitely wrong.
Go double check that as well.
That's under our grid and our water sorting layer is set to player.
That's the problem.
That should be on water.
Okay, cool.
So, now I've got my water layer and I can jump up here and Okay, I've got to get my exit.
So, let's stop playing.
We'll do those little changes.
We'll change that water layer to be on water.
And we're going to add in our one-way platforms.
Now, to get oneway platforms out of here, we've got a couple options.
I could just take our existing one-way platforms and just drag these out here.
This definitely work.
But since we have the tile maps, let's use the tile map system instead.
We're going to go to game object and create a new tile map.
Again, 2D tile map rectangular.
We're going to call this oneway platforms.
And then in here, we'll add another tile map collider and an aector.
So, we need a platformector 2D.
We'll go to the tile map collider and check the used byector option so that our player can now jump through any tiles that are placed on this one-way platforms uh grid.
So now I've got that tile map grid set up.
I'm going to go select it and then we'll go add in a couple platforms.
So I'm going to go select these areas, use that eyropper, go grab the three platforms, and then I'll paste them in.
Let's go one here, one here, uh one here, and then maybe like one more.
Oh, let's do it like right out here.
Straight there.
So, you can go straight jump right up into it.
Let's save and press play.
And now we should have a bunch of one-way platforms that our player can jump right through.
We'll run over here.
Run, jump, jump, jump, and jump.
And we've got our platforms.
You can see I definitely fall into them.
The frog hurts me.
And I can jump up onto these platforms.
and probably make it all the way across.
Let's see.
Looks like that worked.
Okay, looking good.
Now, we need to add a couple of those little one-way platforms to escape the water area.
I'm thinking here we'll do something slightly shorter.
Let's put um let's do this.
We're going to take two of these pieces, paste them together.
So, we'll do eyropper.
Oh, got to go to edit mode.
Eyeropper on the left.
Paste it right there.
Eyeropper on the right.
Paste it right there.
Eyeropper on both.
And now I've got a little 2 by 2 platform.
So, just go drop a couple of these out.
And these don't have to be oneway platforms, but since they're on the oneway thing, they they already are automatically.
All right, we'll save that.
Play again.
Just wanted to go double check that my platforms work.
So, we'll take our player and cheat.
Drag him right over, run over to our platforms, get into the water, make sure I can jump out of the water, and go across.
It looks like it's working.
Now, one thing that's worth noting is that my uh cat bombs are disappearing before they hit the ground.
You see that? They they end right there, and that's because of their lifetime.
So, let's go fix that.
Next, we'll go catbomb.
And if you remember, our cat bombs have a maximum lifetime amount.
So max lifetime amount.
Let's just crank that up to 10 instead of five.
Then these cat bombs when they the new ones at least that spawn would come over here and land.
The ones that we're getting right now aren't because they already exist and pulled.
So I got to go select them and just change those values to 10 as well because they're getting reenabled.
They're not getting reinstantiated.
So those values aren't changing.
There we go.
So now you're seeing ones that last longer.
That other one did it not get the uh uh I didn't change the value.
That's why my multi-edit failed.
All right.
Now they should all do that.
Well, assuming that all of them have the Yeah.
Cool.
Okay.
Looking good.
Let's zoom out a little bit.
And the last part we've got to deal with is our moving platforms and fish.
It looks like the moving platforms are already moving and kind of working pretty well.
Let's just double check that our player can get across it.
So, hit the player, go right here to the center, control shift F, and we'll zero that.
Oh, and then I killed myself.
Well, I'm pretty sure I can jump across.
So, I'm going to go into plastic and make another commit that we've added oneway platforms and fixed cat bombs and moving platform positions and check that in.
It's time to set up the castle now.
And to do that, I want to grab a little bit more art.
I'm going to grab the platformer medieval pack from KennyL.
Just go to KennyL and search for castle.
And you can grab this platformer pack right here that's full of a bunch of different tiles.
I'm going to use the side tiles and the doors and maybe the windows and a couple other pieces to build out a little castle that our player can kind of run along.
So, go ahead and download that.
Once you've got the pack downloaded, open up the PNG folder, select all of the files, and hit C to get them onto your clipboard.
We're going to go back into Unity in the art folder, rightclick, and create a new castle folder.
So, create a new folder, call it castle.
I'll open that by right-clicking and hitting show in explorer.
Hit enter to go in and paste to get all of my castle tiles into there.
Once that's done, I want to make sure that I fix my pixels per unit.
They're going to be wrong.
I think that some of these other things are uh let's see.
Yeah, these are 70 and it defaults to 100.
So, I'm going to select them all.
all.
all.
Make sure that there's no thumb file or anything selected so the popup shows correctly.
And we'll change that pixels per unit from 100 to 70.
Scroll down and hit apply.
It's just going to go nice and slow cuz I got so many objects selected.
And that should fix up my tile map or my my tiles to be the correct size.
Next, we're going to create a new pallet.
So, we'll go to the environment palette here and hit create new pallet.
And I'm going to call this castle background.
Maybe I'll just call this castle.
Actually, this is just going to be all the castle assets.
I'm going to put that into the art folder.
Remember, this is that tile map file.
So, I'm just going to put the tile map file, tile pallet file into the art folder.
And then I'm going to take all of these medieval tiles, select them all again, and drag them right in to create a new tile map.
There we go.
We'll do a select folder here, but we want this to be in the castles folder because this is where it's going to put all of the individual tile files, and I just want them to be side by side with the textures.
There we go.
Now, I've got a beautiful new tile map that I can start using to paint out my castle.
So, there are a couple things I want to do.
First, I'm going to just clear out what I've got here.
I've got my base, but I just kind of wanted to get my uh rough idea of where I want it to be there.
And now that I've got that, I'm going to just delete it.
Got my environment selected.
to go to selection tool and select.
There we go.
Get all these tiles and hit delete.
And oh, let's get these ones up above, too.
And oh, I missed my delete.
There we go.
Select and clear them out.
All right, cool.
Now, let's add in some wall pieces and a background.
So, I've got my environment layer here.
I want to add in a castle background layer, too, where I can kind of fill stuff in.
But, I think I'll do that after we add in the walls.
Let's add in the parts that matter and then we'll fill in the background so that it looks like a castle and not just a black area afterwards.
So, I'm going to add in a left side.
And I believe the left side graphic is right here.
It's this one with a little wood piece on that kind of left.
And I'll go to draw mode.
We'll go over here a couple pieces over and just draw up a big uh a big line there.
See, did I get the right one? It doesn't look like it.
Looks like I've got the wrong object there.
So, I'll select again and redraw it.
There we go.
Now, I've got my my left wall there, which is going to be the edge so that you can't kind of get out so that hey, this is the the edge of the castle.
There's no exiting it.
In fact, you know what? I think that now that I think about it, I might want to put that on the other side.
Do a right wall because this is going to be on kind of the inside here.
So maybe uh maybe it'll look cooler like that if I got a right wall there like that that you can't get past.
And then I'm going to add in a top piece.
So we'll do the top I think is just going to be like this castle looking thing.
I like that.
And then we'll do uh well let let's add in the the pieces that the player has to jump on next because I think that that's probably the most important.
First we'll clear out that little entrance right there.
And I'm going to add in a big door.
So, I want one of these big open doors.
I'm going to just select uh let's go eyropper.
This big open door right there.
That piece right there.
And then we'll drop it in right here.
And next, we need the center parts for it, which I think is this right here.
We'll drop that in.
And then the bottom.
Oh, I guess we just do that same thing again.
Bam.
Look at that.
And then we'll add in a top.
Make it nice and pretty.
Look at that.
Looks nice and fancy all of a sudden.
And then we're going to add in our platforms and our blockers for the player to move around.
Now, the plat platforms and all that stuff are in our environment tab.
So, I'm going to go back over to the environment tab.
And I'm also going to add in some boxes or crates.
Do I have those already? Let's see.
Got boxes.
Let's go find the box single and box double and box crate.
And I'm just going to drop all three of those in here as well.
Put those into the tiles folder.
I'm gonna use those to kind of build out this castle here.
So, I want to have a few things.
I want to I want the player to get like partway across and then do a jump across and then come Yeah.
So, like they're going to jump and then come across here and then get the key maybe over here.
So, I'm thinking like the the main key will be like right around that area somewhere.
So, they're going to come in and do this like little uh not super complicated challenge, but you know, we'll just build out like a little maze here.
So, there's going to be a wall here in the center or something that's blocking them.
So, they won't be able to get across here.
Um, and then I'm thinking a bridge across the top there.
So, let's go add in a platform here that they'll So, they'll run in, come maybe all the way to the end here.
Let's get rid of that piece there.
They'll come all the way over to the end.
Let's add in some brick walls here just as a uh end piece so they can't go past that.
Um, and then they're going to go up.
And maybe I could add in a boss or some enemies or other things in here as well, too.
But for now, I think we'll just go like this.
And um, let's go with a platform here and fill that in like that.
I'm thinking somewhere right around like this.
They'll jump up, go back and forth up until they get to the top of the castle.
Go back to that castle tile map one more time.
And again, I think you could probably come up with a a much cooler design than uh the specific little one that I'm doing here.
But I want to show you how to how to kind of put all of these things together and then let you build out whatever you think will be super cool.
All right, let's add in a wall piece here.
Whoops.
Not on the right tool.
Got to do the the line drawing tool.
So, go from the top down to the bottom and fill that in.
And we'll do the other wall here on the other side.
Top to bottom.
And filled in.
All right.
We are drawing on the environment layer here, though.
So, I'm going to need to add in a little hole to drop down.
And then we're going to go back to the main environment tab and add in a couple more platforms for our player to land on and kind of explore down.
So they land there, come down, and then I'll have two ways that you could go down.
There's one there, and maybe the uh the far one will be the correct one.
So the close one will go down like that, and maybe a dead end.
Or here, let's do a do an opening there.
And then a dead end, if I can draw it.
I find the right tile.
Nope, I had the wrong one.
They're like that.
And we do like some box crates right here to kind of fill this in so you can't get across.
Um, can't get across here.
And a couple more pieces.
So, we'll do another line there.
Yeah.
And then we'll put the key right down here at the bottom.
So, let's just go to key, select that key, uh, control shift F.
Zero out that Z again.
And I'm thinking like right around there.
Let's drop a couple crates in though so that our player can also jump back up and get out.
So add a couple of these.
Um Oh, got to go to paintbrush mode.
Right about here.
Thinking like one or two.
Oops.
Did I select the right one? Paint eyropper.
There we go.
Get our crates there and drop them right in.
So I got a a couple crates placed in here.
Um, I do want to clear out these other crates though because those aren't supposed to be there.
So, let's go to select mode and we'll just select and I'm actually going to get rid of the ground pieces right below it, too.
Let's select all of that and make sure that we're on the correct layer.
Got environment selected.
Go reselect those again and hit delete.
There we go.
Clear those out.
Then I'm going to go to lava and we're going to paint in some lava.
So let's just do Whoops, wrong button there.
I painted a lava over that.
Make sure that I'm not in tile edit mode.
Eyeropper.
Select my lava.
Drag that across.
And then we'll do eyropper again.
Select the internal lava.
And then oh whoops.
I thought I had fill.
Whatever.
We'll just paint that out.
Okay.
Let's get that last piece.
So we'll eyropper that one.
And then did I not do an eyropper? eyropper.
Click paint.
Oh, I'm on the wrong layer.
That's why.
So, these ones actually just need to get removed because I painted lava on top of the environment layer.
All right.
So, now I've got lava there.
I've got a way across almost.
I need to add the bridge.
So, we'll take the bridge tile.
Drop that right into here.
Put this into our tiles folder.
And now I've got a bridge.
We'll drag that across as well.
So now our player can get across, not fall into the lava.
But it looks a little bit menacing anyway, and then um hopefully get that key, make it all the way back out, and then uh pass the level.
I don't know that I'd necessarily love my level design, but I love the fact that I can now very easily modify and adjust this thing.
So let's hit play and just run through it real quick.
and make sure that everything is working kind of as I expect before we finish up the key functionality and the door to continue on to the next level.
So, we go.
We've got our key.
If I don't miss my jump, I can make it over to here.
Oops.
Come run down the ramp.
Got some cat bombs.
Ow.
Got hit in the face with cat bomb.
Jump up.
Jump up.
Jump up.
Oop.
Switch back weapons.
Hopefully my cat is killable now.
Oh, he's not.
I've got to fix his uh his death real quick.
But for now, I can jump into the lava.
Let's see.
Can I make that jump? Made that jump.
And then we get this jump.
We get inside.
Okay.
So, I can't get inside the castle.
That's a slight uh mistake there because I've got this on the wrong layer.
So, if I go to my castle here, my guess is that my environment layer right there, yep, includes the door and that needs to be moved to my castle background now.
So, I want to make sure that my castle doesn't collide and I've got this kind of thing filled in with a nice background.
Let's uh do that in the next section, though.
For now, we'll save save save that.
We've added most of the castle and check that in.
Now, we're going to dive into the interaction system that our players will use to teleport around the level.
We're going to create some doors that our players can interact with that you can extend to be any other type of interactable object as well.
And once we've unlocked the door, our player will be able to walk through that door or use and interact with the object to teleport over to the flag here.
So, we'll put a door up here, another door here, and then we'll have a way for the player to go between the two once the door is opened.
So, we're going to start with an empty game object.
We're going to create an empty game object called door.
And I'm just going to zero out the position for now.
We'll reset the position so that it's all at 00.
We're going to add in a closed door child.
So, I'll just drag that down here as a child.
And then underneath that closed door, I'm going to add the closed door top as well.
The closed door top, I'll set to a position of zero and one on the Y so that we get that nice uh full door.
We've got the top and the bottom there.
Let's go reselect those.
And then I'm going to move them up to the position that I want it to be in.
So, this door I want it to be right over here.
This is that exit that's going to get me to the flag.
I also want to have a door over here that I can get in.
So, this will be like the entrance door.
So, I'm going to select my door closed mid, duplicate it with control D, drag it over here with control, and just get it right up into the I think the position that I want, which is probably right about there.
Now, I'm going to add in some open doors.
I've got my closed doors.
I want to have open versions of them as well.
To do that, I'm going to take my open mid and I'll just drag it over here under door again and do the same with the top.
just to the top as a child there.
I'll set the position here to one and zero on the X again.
And then I'm going to move this thing to just be in the same position as this first door.
So, control drag it up.
Nice and easy.
If I'm holding control, then hit Ctrl + D, duplicate, and get an open door over here as well.
So, now I've got an open door and a closed door in both positions.
I'm going to rename these now.
Let's call this um closed one.
And we'll call this one closed two.
And we'll call this open two and open one.
I want to make sure that they're uh they're matching.
Oh, I didn't put the D there.
Let's put opened too.
I want to make sure that these match just on the the naming standard there.
So, opened and closed doors, one and two.
Now, we're going to need to set up a way to toggle between the two doors.
So, we're going to create a new script.
We're going to create a door script.
We'll do that in our scripts folder here.
Right click, create a new C# script.
We'll call this door.
And then we'll attach it to our door before we open it.
So, we'll grab the door, drag it right on.
on.
on.
Let's see.
Let's try that again.
See if it added.
We'll do a save door.
It just didn't recompile, so it didn't find the script.
Saving seems to have forced it to reload any second now.
We should be able to search for and find door or drag it on there.
There we go.
and we'll open that script up.
So, in this script, I said I wanted a way to open and close doors.
So, I'm going to add those first.
I'm going to delete out the start and update.
And we'll add a public void open.
And then, let's add a context menu item to be able to call this.
So, we'll say context menu name of open.
And then in our open method, we're going to turn both of our doors to the open mode.
So, say open one set active true.
And I'll duplicate that.
We'll do open two setactive true.
And then we're going to duplicate these both for the closed versions.
Say closed one and closed two.
And of course, we're going to set the active state of these to false when we open or when we open the door.
Now, I don't have either of these, so I'm going to go create them.
We'll go up to the top and just do game object, open one, duplicate.
We'll do an open two.
And we're going to duplicate again.
do a closed two and a closed one.
I need to make these serializable though.
So, I'll hold alt and drag and add a square brace.
Serialize field.
And now I've got my openable door.
I also probably want to have it closable though.
So, I'm going to take the open section, duplicate it, hit the left arrow and enter.
And let's call this close.
We'll change the context menu to be close as well.
And then down here, we'll just invert these.
So this will be false, false, true, and true.
Now I should be able to save and build and even execute those in edit mode.
So let's go back into the editor.
Should be able to rightclick, go to open mode, go to close mode.
Oh, I have to assign them first though.
So, let's assign closed one, closed two and opened two and opened one.
Then I'll rightclick and we hit open.
They switch to open mode.
Hit close and they switch to close mode.
Now, for my player, since they're not going to be in the editor, I'm just going to use our yellow lock.
So, we'll take that lock and we'll drop it right up here.
They're going to get the key for it in just a moment.
So, take this.
Let's just click and snap drag it.
Uh what? 17.5 and 7.5 it looks like is a good number.
And then for the unlock action, we're going to take our door.
Oh, got to hit plus there.
We'll take our door, drag it into here, and choose door and open.
So when we unlock this with our key, it'll open up the door.
Let's move our key really quick.
So I'll just take that key.
Um actually, you know what I'll do is duplicate it.
Control shift F it real quick.
zero out that position.
Oh, I had another yellow key right there at the beginning, too.
So, I guess it probably wouldn't have mattered either way.
But I'm gonna hit play now.
Oh, after I move my player back over.
And then we'll uh make sure that our key actually opens the door.
So, let's just grab the player.
Let's just move this guy way over here.
Perfect.
Run over.
Grab our key.
Go grab the second key that I don't actually need.
Go up here.
We'll use that.
The door becomes unlocked.
And now I could go through it theoretically.
The next part will be setting up our interaction system so we can actually go through the door now that it's unlocked.
For now though, let's stop playing, go into plastic, and make our commit that we've added the door and door script with lock to open it.
And I want to make sure that my door is in here.
Got a couple extra random jet marines files from Ryder in here.
And that my level file is in there.
We'll check that in.
So, for our doors, the plan is to have our player interact with them by pressing a hotkey.
I want to give them an interact hotkey that they can use to just use any object that's interactable.
To do that, we're going to need a new script for our player, a player interaction controller script or a player interactable script or something similar that's going to handle our interactable objects.
And then we're going to need a new UI element as well to let our player know that they can interact.
So let's start with the UI element.
We're going to go to our robot and underneath our robot, we're going to add in a new canvas.
So I'm going to rightclick, choose UI, and choose canvas.
We're going to change the render mode to world space and the scale to be 01 01 and 01.
Next, we'll reset the position to 0 0 on the X and Y.
It should already be zero on the Z.
and change the height and width to about 100.
Now you should be able to see that object if we drag it up here.
So if I set this up to like a one drag it up, you can kind of see that little canvas object.
So let's make Oh, I made it too small.
It's 10 x 10 instead of 100 by 100.
So make it 100x 100.
And now you can see that block right there.
This is going to be where we're going to put our text.
But that's obviously not quite wide enough.
So I think I'll triple this to about 300.
We'll right click on it now and add in a UI element.
That's going to be a text mesh pro text.
So, oops.
Got to go select text mesh pro text.
And then in here, I'm going to make this fill.
So, I'll hit the anchor, alt, and shift, and click on the fill option.
Then, we'll go down and we'll center it and center it again.
So, it's centered horizontally and vertically.
And then finally, put in some text like interact.
And then maybe give them a key.
Maybe it's E.
I don't remember if I already bound up E, but if not, we could use something like that.
Now, I can't see this on my view very well.
I think it looks kind of terrible.
So, I'm going to change the font.
We'll go over to a um I'm going to go with bangers and like a bright red just to make it really obvious with an outline or maybe a drop shadow.
So, now I've got this text that says interact over my head in bright red.
And I think that that'll probably look okay.
If I hit auto size and make it a little bit bigger, make it fill out that area.
And I I'll use this, I think, as my um interaction canvas.
So, I'm going to rename this to interact canvas.
And then we're going to go to our player and we're going to create that new script.
This player interaction controller.
So, hit add component, type in player interaction controller, and generate my script.
If that's not in the scripts folder, I'll move it over there in a moment.
It's probably going to be in my prefabs folder.
Let's see.
Go click on it.
It went into the root assets folder.
So, I'll click and drag it into scripts.
and then we're going to open it up.
So, our player interaction controller is going to need to do well really two things.
It needs to keep track of when we're inside or what objects we can interact with.
And then it needs to tell those objects to be interacted with.
So, I think the first thing we'll do is just get rid of uh start and update.
I'm not sure if I'm going to need start update.
I'm almost positive we won't need.
And then we're going to add in let's add an awake and cache our text mesh protext first.
So we'll say underscore text or let's call it interact text equals get component in children and we're just going to get our tmp text.
Now we could make a serialized field if we end up with multiple interactable or multiple text objects under the player but since we only have one for now it's easier and less maintenance to just have it cach it in our awake.
Next we're going to have some sort of way to interact.
So let's get our player input as well.
We'll say underscore player input equals get component.
And since this is going to be on our player, we should just be able to get it at that level.
Player input.
We'll generate a field for it.
And oh, we need to add the using statements for it as well.
So that added our Unity using Unity engine.inimpinput system.
And then finally, let's bind up for the interact action.
So we'll say player input.actions and we'll call this the interact one.
and we'll say performed.
That's the event that gets called back.
And we're going to call a method named uh let's call it interact.
So, we'll register for the performed event and call our interact method whenever that happens.
Oh, and I guess we should probably disable our interact text by default, too.
So, we'll say interact textame object set active to false.
We'll just turn that object off.
We'll turn it back on whenever we can interact with something.
All right.
So now we've got a base for being able to interact, but we don't have something to actually interact with.
We're going to need to go back to the door for that.
So in our door, when a player enters our trigger area that we're going to set up, I don't think we've set one up yet.
We're just going to tell our interaction controller that, hey, this thing can now be interacted with.
The player has come in.
So to do that, we'll add an ont trigger enter 2D.
And we'll say, well, first let's get the player.
say var player equals other.get component and we'll try to get the player.
If there's no player, then we'll just bail.
But if we do have a player, then what we want to do is tell our players interaction controller system to add this object.
So instead of getting the player, why don't we just get the player interaction controller.
We'll do that.
We'll do player interaction controller and then we'll say player, which is actually the player interaction controller.
So let's call this player interaction controller.r control R to rename.
and we'll say dot add and we'll just add in this object.
So we're gonna add a method for add which right now takes a door and you probably have a good idea of how to make that more generic for a more generic interactable.
I'm hoping you've got that concept down.
But since we only have one thing right now, we're just going to use doors.
And we'll say underscore doors add door.
We'll generate a field for that.
And that should be a list of door.
Makes sense.
Again, if we go to an interface or something more generic, it would be an a list of that type of thing.
And we'll initialize it to a new list of doors.
There we go.
I guess the the new shortened down would have been just fine.
Just out of habit, went around and uh and made it longer.
All right, so we've got our doors being added.
We also probably need to remove doors if our player leaves the trigger.
So, let's duplicate the trigger.
Enter, left arrow, enter, and change enter to exit.
and then change add to remove.
Generate a field a method again.
And here of course we're just going to say underscore doors remove and we'll remove that door.
So now we've got a door that we're we can go in or add a door.
We can remove a door.
And then finally we just need to be able to interact with doors.
So in our interact method we'll do a for each var door in underscore doors.
And really there should only be one door ever active.
But if we extend this to be more generic with more interactables, then you could theoretically have more than one interactable object in the area.
And we'll just say door dot and then how do we want to do this? Probably call like a interact.
And we'll pass in our object that's interacting with it because remember more than one player could be in the game.
So we need to make sure that our interactable object knows what thing is interacting with it.
We'll generate a method for our interact.
And then this is just going to well teleport the player from one door to the other, I think.
So, we'll just need to know which door we're at and then teleport to the other one.
Now, I think this is a a perfect place for a quick little challenge.
So, if you've got some ideas of how you want to accomplish that, go ahead and give them a try now.
Experiment a little bit and see what you can come up with.
The solution should be relatively simple, though.
when we're interacting with the door, we're going from one door to another.
We just need to figure out which door we're going to.
So, go ahead and track that down and then I'll show you my solution or go ahead and experiment and figure it out and I'll show you mine.
All right, let's go through my solution.
So, what I want to do is pick a destination based on whichever door is furthest away.
Whichever door is the furthest away one is the one that we want to teleport to cuz we're obviously closer to the other one.
So, we'll say var destination equals and here we're just going to look at the distance.
So we'll say vector 2.d distance and we're going to go from our player interaction controllers transform.position to the opened transform position open one transform position.
So we're going to say if this distance is greater than and let's just zoom that out a tiny bit and then we'll duplicate or copy this line and we're going to check if it's greater than the distance to number two.
Then we'll do a question mark.
destination is going to be open two no open one.transform.position position.
Otherwise, we do the colon.
It's going to be open one or open two.t transformed.
I said my words backwards, but hopefully you get the idea.
So, if this one is further away, if number one is further away, then we'll use number one as our destination.
If number two is further away, we'll use number two as our destination.
And that's just because the one that's closest to us is the one that we're already on.
So, we need to go to the one that's far away, not the one that we're already on.
And then finally, we'll just tell our player to move there.
So, we'll say player interaction controller.transform transform.position equals destination.
Now, let's get back into Unity and finish our interaction setup.
So, the first thing I want to do is let's move our player over here to like a 15.
I want him to kind of drop just by that door so that he's nice and easy to get to.
And then I want to add in our player input action.
We need an interact action.
So, let's go find the jump action.
Duplicate it with control D and rename it to interact.
All the hotkeys work here, by the way.
F2R D and all that.
And then I'm going to set the hotkey here to E because that's a pretty common hotkey for interaction.
We'll delete out the PlayStation control and save that change.
Next, we need to add in some colliders to our doors so that our triggers can actually fire off.
So, I've got open one and open two.
We'll hit add component and add a box collider 2D with the is trigger option set.
I'm going to save.
And right now, if I hit play, I don't expect Well, actually, let's go back into our interaction script real quick and just make sure that when we enter a trigger, um, let's do it right here after we add oursel.
Let's also turn on our text because I realize I don't think I've done that yet in our player.
So, when we add in a controller, let's go into add.
We'll say underscore interact set act or game object set active to true.
And then when we remove a door, we're just going to check if there are no doors.
So, we'll say if doors.count is equal to zero, then we're going to set it to false.
So, we'll turn that interact text off.
All right.
Now, let's save and play and watch and see if the interact text comes on.
I've got my doors in the open state right now.
So, I'm going to drop right into it without having to get the key and see if I can interact with them and teleport or not.
We're going to expect to see a big fat no.
But, let's watch and see if that's the case.
So, I drop in.
Oh, I actually can.
Okay, perfect.
That works perfect.
Oh, that's because I cheated and I already pre-added my composite collider.
Let's stop and remove that, though.
So, if I don't have my composite collider and my rigid body on the door that I accidentally pre-added and I press play, you'll see that I drop down and no trigger fires off.
And that's because the triggers or the colliders are on the child objects and the script is at this parent object.
So the cheat that I had used and let's pause and read it is to add a composite collider which automatically adds a rigid body and if I don't change this to static the rigid body will fall down and then press play and now what happens is it creates a single collider that consists of those two colliders.
So it's a builtup collider of the two.
So now I can use the script at that parent level and then uh have the colliders be children.
So let's jump up there and actually try using it.
So, jump up, jump up, come over here and hit E.
And you can see I can teleport over and now switch out to the the next level.
So, let's stop playing and just double check that I've got that composite collider readded to my door.
I don't.
So, I'm going to read it and set that back to static and save.
And then we're going to go check in our changes.
So, we'll go in here.
So, we've added the working interactable door and check it in.
In this lesson, we're going to add another enemy.
We're going to add the fish, and we're going to have him swimming through the lava and shooting spikes out at our player.
And we're also going to implement the splines library so that we can move our character along a nice smooth path and have them kind of swimming and jumping in and out of that lava.
If you've never seen splines before, they look essentially like a curved line.
You've got a line with points on it and curved data.
And they originate from back when people used to build ships, I guess, by putting these together.
I assume it's all digital now, but back in the day, they used to manually build these out to figure out their curves and put things together.
Nowadays, we just slap them into video games.
Now, in this lesson, we're not going to get too deep into the mathematics behind splines.
I've watched Freya's video on how splines work and all of the details there and I get lost constantly about 20 minutes in.
So, if you really want to dig into the details of everything mathematical behind the splines, I'd recommend go checking that out and check out a couple other resources on YouTube.
But if you want to just see how to use them right away in your game, well, that's what we're going to get into.
Before we add the fish or anything, we're going to start by bringing in the splines package.
We'll go to window package manager and then under Unity registry we should be able to scroll down until we find the splines package.
I'm going to install that.
And once it's done, we can click on the documentation right here to bring up all of the docs about splines.
I'm not going to go over these documents though.
We're just going to go right into Unity and use it.
But if you want to look into more info, you want to see the actual page, just remember that it's always there on just about every package manager page.
You can click on documentation and get more details.
With the package imported, we should be able to create a new spline under game object spline and then choose one of these existing spline types or just hit the draw splines tool.
If I hit draw splines, though, I'm going to get a spline that's located at 0 0.
I can double click on it to go to it.
and also has no points or no knots in it.
So, I'm going to need to add a couple knots.
I'll hit the plus button here.
Let's just hit it twice.
And then in spline edit mode, so I click on this little button right here to go to spline edit mode.
I can now grab and drag these points around.
Let's see.
I think I had one just a second ago.
Let's go grab it again.
There we go.
Now, I can move my point around for this knot.
And I can click on this other point and drag it around as well.
If I click on this little indicator here though, I'll go out of spline edit mode and then I can't select those.
Then instead, I'd be just selecting and moving my entire spline object if I could even click on it.
All right, let's move the spline now.
I'm going to take my spline and I'm going to move the base of it all the way over here.
Notice that those little points here, my two knots that are children of it, move along with it.
I'm going to move this right over to I think maybe like the start point of where I want my fish to swim.
I want my fish to swim up and over and kind of do a loop and maybe jump around like this and shoot off some spikes.
So, I'm thinking right about this point is good.
That means that my first knot I also want to be right at this origin point.
So, I'm going to set the value here on not zero of X and Y to be zero and make sure that Z is also zero.
Not one is at six and 2.8 an 8 and a three, which also means that if I click on 3D space, this knot is way over here off to the side, and we're working on a 2D game.
So, I want to change that.
I want to keep this flat.
I'm going to set this Z to three.
There we go.
And now I've got this nice curved line.
Let's see if I can get into a 2D view where it's trying to go up.
It's still going back a little bit though because of our orientation.
If we rotate the Y value by 90 degrees here and it's going to straighten that right out.
You see it's no longer sticking out.
We'll do the same on knot one as well.
And then just have that continue for our pre our next knots as we keep adding them.
So let's add another one.
I'm going to hit the plus button.
We'll go into move mode.
And I'm going to go into nice 2D view here.
Hit W and see if I can grab that knot and drag it back down.
So, I'm thinking I want this one back down here, but I also want this one up here kind of above the the water.
So, it kind of jumps up and then dips back down.
I want more knots.
So, I'm just going to keep hitting that plus button.
Add another one where I want him to go back up again.
Thinking right about there.
And then a plus again.
We'll drop him back down.
And a plus.
Get him up.
One more to go down.
We're almost to the end.
And then we'll do one more going up here.
And then at the end of it, I want him to kind of turn around.
So I'm going to drop him down a little bit sharper.
Then we'll add another point over here so he kind of swims back this way a bit.
And then have him kind of reverse that loop so that he goes up across those points.
So, we'll hit plus.
Go up to here.
Or, you know, maybe I'll Yeah, go right up to here.
We need to turn the rotation around, though.
So, we'll go to negative 90.
And we're going to start doing a negative 90 on the next one.
Let's see.
90.
And keep adding adding our points.
Think I may have There we go.
There's my point.
Almost lost it.
You can see I'm doing this crisscrossed wave here.
Now, we don't have to necessarily do a wave.
One of the benefits of this curve, I could skip this middle part completely.
It's not programmatic.
So, I'm not forced to have a point every set value or set space.
Hit plus one more time.
We'll get this down.
And then I think that's probably good.
We'll go up to the top and choose the closed option, which will turn this into a loop.
Now, it's going to do a little bit of weird rotation when he comes down here, but that's okay.
He's going to be off screen and not visible.
So, here's our spline.
We've got this nice long line and we're going to have to move our fish along there.
So before we do that, let's save everything off and let's do a quick commit that we've added the splines package and our first spline into level three.
And we'll check that in.
Now that we have our spline for our fish to follow, we're going to add our fish, make him animate, and make him follow that spline, which is going to be drastically easier than you might expect.
Let's take our fish and drag him into the scene first.
I'm going to move him over here to the right.
Let's see.
Just grab him and drag him so he's somewhere near the lava.
And let's go into a nice 2D mode.
There I can see my fish.
And I want my fish to follow along this spline.
Now to follow a spline, we usually call the evaluate method on it.
And then that'll give us a point that's between zero or and one or 0% and 100% along the spline.
We'd get a point here would be 0%.
And then here was probably like I don't know 5% or 05 right around there.
And then we loop around.
You get to like 98, 99, and 100 when we got back to the end of the loop or a one.
We don't have to do that though because moving along a spline is such a common thing that it's already built into the splines package.
So on our fish, we're going to add the spline animate method.
This takes a spline reference.
We'll just drag our spline over here, our fish path spline, and then we can press play.
We don't actually have to press play though because they've added a preview mode here.
So I can actually hit the play button right here and watch my fish completely disappear.
I can see a little bit of flickering going on, but the fish is not staying around.
Well, he kind of is.
He's just not really visible.
What's actually happening here? Well, first, our duration is way too fast.
We've got it one second for it to loop across the entire thing.
And you can kind of maybe loosely see that outline there.
If I turn this up to about a oh, let's go with like 15.
We can see that it's moving along.
And there we can see an outline of something, but it's not our fish.
And the reason for that is that our forward axis of our fish is incorrect.
If I go into 3D mode and go take a look at our fish, you can see that he is facing off to the side here.
But there's an option right here for forward axis.
I can change this from object Z plus to X plus.
There we go.
And now my fish is swimming in the correct direction.
Let's go into 2D view.
And when he turns around, he should also be swimming in the correct direction.
You see, he does that weird flip upside down under the water or under the lava.
It doesn't matter because he's not visible.
Um, there we go.
And then he flips back and looks good.
And he's going the correct direction.
So now I've got something that will move him along.
Again, this is running without me even pressing play.
I can pause, slide along.
It's a nice little editor.
And we're going to add our own editor that's somewhat similar to this for attacks in just a moment.
But for now, we've got a fish that moves around.
Let's make him animate.
We're going to go into our animation folder.
Go to fish and rightclick.
Create a new animator controller.
We don't want to use that override one that was in there.
We'll call this fish.
We'll open up that animator controller and I'm going to just move in my move fish animation right now, which is just the one that causes his tail to wag back and forth so it looks like he's swimming.
We'll go back into our scene view, go find our fish child object, the base one with the animator, and drag in our capital fish animator controller, not the override controller with the lowercase f.
Now, if I save and press play, I expect that my fish will start animating.
Let's check them out.
We'll go into the scene view real quick.
There we go.
We can see our fish animating and swimming around.
And the last thing I want to do with this fish right now is make it so that he actually shows up behind the lava when he's behind it and only shows up kind of when he jumps out of that lava.
It's kind of like his his fish water.
To do that, we're just going to need to add some new sprite layers.
So, we'll stop playing one more time.
Go back to our fish here.
Go select his child objects.
And we're going to need a new sorting layer.
that's behind whatever this is on.
And right now, I believe our lava is on the default.
So, I'm just going to add a new layer and call this um inwater fish or let's let's call it fish.
Actually, I'm just going to call it fish because that's what I'm going to put on there.
And I'm going to move that above the default but below the background.
So, it show behind everything except for the background there.
Now, we're going to open up that fish prefab here.
Go select all of the child objects by expanding this out and searching for sprite renderer.
I put a t equals at the beginning to make sure that it shows up.
That changes in every version.
It seems used to be a colon.
Now it's an equals.
It used to not require anything.
But now that I've got them all there, I'll select all with control a.
And we'll change this sorting layer from default to fish.
Press the back button.
Save.
And now we should have a fish that appears to jump out of the water.
Let's play one more time and check it out in scene view.
Go back over here to scene view.
My fish goes around.
It seems like he's kind of doing a little jump out of the water.
Perfect time for him to do an attack.
Turns around, swims back, does a jump, skips that middle part, does another jump, turns around, and shows back up.
All right, that is looking good.
Let's go into plastic and say that our fish now moves along the spline and animates if you haven't already seen it.
Our fish has a pretty cool attack animation and that's what we're going to hook up now.
You can see he does this roll and he's supposed to shoot off a bunch of spikes.
Those are the spikes on top of his head.
So, let's hook it up.
We're going to go to the fish's animator and we're going to drag out the attack roll fish animation onto the animator.
We need to add a parameter that'll be a trigger for when it should attack.
And we'll just call this attack.
And then we'll make an attack animation transition.
So we'll do make transition, go to attack roll, and do a make a transition back.
But on the transition from move to attack, we'll just add in the attack condition there.
So we have that condition of that trigger to go into attack.
And then we have has exit time on.
So it'll go back out as soon as the animation completes.
All right, that'll work.
But we need something to actually fire this off.
And we don't want to necessarily fire this off on some sort of a timer or something else.
We want it to fire off when it gets to specific points.
I mean, a timer could theoretically work, but seems a little bit complicated when really we want to be able to set the point somewhere along our spline where our fish will attack.
And that's what we're going to do.
We're going to add some fish attack points or just some attack points to our spline.
And you could think of these as any additional data that you could add.
You could always refactor this and change it to do whatever it is that you want at the different points in time.
Let's select the spline and create a new script.
We're going to call this spline attack points.
Generate a script for that and we'll open it up in our code editor.
In our spline attack points, we're going to need a reference to our spline container.
So we'll add a serialized field of type spline container and this is just going to be named underscore spline container.
Now we don't use a spline here because the spline will get serialized.
And if we actually go back to our spline object here, you'll see that this is actually a container that contains multiple splines.
It has the name spline here.
So it gets a little bit confusing.
You might grab the wrong type.
Just remember if you want to reference the scene object here or the component, use the spline container.
Now I can drag my spline container over and you see that that reference appears just fine.
I'm going to go back into code and what we want to do next is add in a list of points or points where our player will attack.
I'm going to add or not our player but our fish.
We'll add a serialized field.
It's going to be a list of floats which will be the percentages along the way.
And I'll call this attack points.
Now, I'm going to get rid of our start and update methods because we don't need these here.
And we'll add an ondraw gizmos instead.
And now we're going to loop through all of our attack points.
And for each attack point, we'll just draw a gizmo on our spline at the point where we want to attack.
That way we can see exactly visually right in the editor where our attacks are going to happen.
So, we're going to do a loop, do a for each loop of all of our spline, no not our spline container, our attack points.
There we go.
And we'll call these uh let's just call them point for each point in attack points.
For each one of them, we'll get the position along our spline.
And we'll do that using uh let's say vector 3 position equals and we need to use our spline container.
And we're going to use the evaluate position.
Let's see if I can get that right.
evaluate position method.
We'll give it our point value.
This will give us a position along the spline at whatever percent we've given it for this point here.
Now we've got our position.
We're going to do a gizmo.
So let's do gizmos.draw color or draw let's say not draw color equals.
And we'll do color red.
Make sure it's nice and visible.
And then I'll do a sphere like gizmos.draw sphere.
and we're going to draw it right at our position and give it a value a size of maybe like 0.2.
So this should give us all of our spline positions that we've added or our attack points visible on the on the object as gizmos or in our scene view as gizmos.
Let's go try it out.
By default, we should have none.
If I expand out attack points and hit plus, I get a point right here at the beginning.
If I hit plus again, I have a second point at the beginning.
But let's say I drag this value out.
You can see that little red dot is moving along.
And if I wanted my first one to be right around here, it looks like 0.1 is too high.
Probably go with a about a 07.
There we go.
Then I can duplicate that.
Add in another point and move it over here to wherever the next position I want to attack is.
It's probably going to be like a point five.
No, two.
There we go.
And so on.
I can keep adding these in.
Now, we could make some slightly better custom editors that allow us to slide and drag this, but realistically, most of the time, it's probably not worth it unless we end up with a bunch of designers building these or we need a lot of control over them.
We need to constantly change them.
But, as you can see here, with just uh a little bit of value typing, and I'm very quickly able to fill in all of these data points, and we can change these very easily, too.
We don't have to do very much work at all to modify this.
So, let's go with like a 61, a 62.
I want them all to kind of fire off right before we get to the peak.
So, I think we've got one more attack point here to add in, which is going to be the one where it comes up and then loops all the way over there.
So, what's that going to be like a 85 or 86.
There we go.
And now I've got all of my spline attack points ready to go.
Next, we'll set something up on our fish to actually use these.
But for now, we've got our gizmos set up and our spline attack point script working.
I think I want to check this in.
So, go into plastic, say we added spline attack points, and check that in.
Now, we're going to create a new script, a fish script that will tie all of our existing code together and make our fish work properly along the spline and shoot at our enemies.
We're going to start by taking the spline attack point script and I'm going to move this in my scripts folder.
It got generated into the root.
Then I'm going to go into the scripts folder.
Rightclick and we'll create a new C script and we'll call that fish with a capital F.
We're going to open that script up and we're going to add a couple references.
First, we're going to need a reference to our spline animator.
Let's get rid of this start method completely.
We'll add a serialize field that references our spline animator or spline animate.
And then we need a reference to our animator because we're going to want to turn that attack animation on and off with that trigger or really just turn it on with the trigger.
So we'll get a reference to our animator.
And then we're also going to need a reference to the attack data.
So we're going to need that spline attack.
There we go.
Attack points.
Now, to keep track of where we're going to attack next, we're going to use two different variables.
We'll create a float that has our next attack point.
So, let's do that now.
float next attack point.
This will be the time along our spline where we'll attack.
So, it'll probably be at I think right now we have one at zero that we'll probably remove.
But then we'll have our 2 and then 3 or whatever it was for our next attack and so on.
That's going to store that value right there.
So, we can do some very quick easy comparison.
We're also going to keep track of all of our next attack points or all of our available attack points.
And we're going to do that in a Q this time.
So we'll use a Q queue EU of type float.
And we'll call this attack points.
This will be all of ou