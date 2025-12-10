s up and appears and kind of blocks their path.
So, what we're going to need to do is add in some sort of a trigger to kind of activate and start this whole sequence off.
Before we do that, though, I want to set this up as a full encounter.
It's going to be a bunch of different pieces that are all tied together, and I want to group them together so that it's easy to tell that they're related and to work with them in the future.
So, to do that, I'm going to rightclick and just create an empty game object.
We'll call this B encounter.
and we'll reset the transform so that we've got it all zeroed out.
I'm going to take my Broo root object and just make it a child of that B encounter.
And then I'm going to rightclick and hit create empty.
And let's create a B trigger.
I'm going to add a box collider 2D to it and check the is trigger box.
Now what I want to happen is when I enter this trigger, my cinematics will kick off and the whole B encounter thing starts and the fight kind of begins.
This is like a the boss battle begins.
Camera maybe changes.
Maybe my controls change.
I don't know.
Whatever things I want to fire off, they're going to fire off from this B trigger happening.
So, when we enter this trigger, we're going to want to do one or more things.
And I don't really know what those things are going to necessarily be.
So, I'll create a more generic script that uses Unity events that we can hook up to whatever different things we decide we need.
So, we'll go into the scripts folder.
And let's just minimize this down.
And I'm going to create an event trigger script.
So let's create a right click create a new C script.
Call this event trigger or let's call this um do you want to call it event trigger or trigger event? H I'm going to call it event trigger.
That makes more sense.
It's the trigger for my events.
I'm going to go add this to the B trigger object soon as it allows me to select it.
There we go.
We'll take our event trigger, drag it on there, and I'll open up that script.
Now, we're going to want to listen to an on trigger enter 2D because we want to find out when the player comes in.
These event triggers are only going to listen for the player.
So, add on trigger enter 2D.
And we'll first check to see if the thing that's touching us is a player.
So, we'll just check the tag.
We'll say if not collision.compare tag and then we'll check against player.
then we'll return.
Otherwise, we'll fire off our untriggered event.
So, let's let's actually go up to the top and add a serialized field.
There we go.
A serialized field.
The autocomplete and everything popped up right over me.
And the serialized field is going to be of type Unity event.
And I'll hit escape, alt enter, and add that using statement for Unity engine.vents.
Let's call this onevent triggered.
Now I'm gonna call that down below.
So I'll just double click, copy it and controlV to paste and question mark invoke it below.
So now whenever we enter the trigger with a player, we'll invoke this onevent triggered.
Now that's good, but I only want this to happen once.
So let's add in a check to see whether or not it's already been triggered.
I'll add that down below.
say if triggered then return as well and then we'll say otherwise we'll say triggered equals true.
So that way it'll only get called once we don't have a triggered variable.
So I'll hit home alt enter and generate a field for it.
I'm going to double click that private, hit enter there and add in a little bit of spacing.
I want to remove these two extra using statements at the top and that extra little line at the bottom.
Save it off.
And I think this looks pretty good.
We could combine these statements, but I think that leaving them separate is a little bit easier to read in the file small enough that it's not going to make a difference.
So, now we've got our event trigger.
Let's go back into Unity now and use it to toggle some things.
Let's start by just turning on a camera that shows our bee in the player fight.
First, I've got my B.
I've made sure to move him up here.
If you didn't move your B already, just get him out of the way.
But, I'm going to rightclick and create a new Cinem Machine virtual camera.
I'm going to call this virtual camera B and make it a child of the B encounter.
I'll make sure that I'm in move mode and drag it around.
I want to drag this ortho size down to something like a seven though, so that I can see this whole area, but not too much more.
I think um right about to there is probably pretty good.
Now I'm going to go to my B trigger and in our new onevent trigger that we have available, I will hit the plus option and drag our virtual camera B in.
Choose game object and set active and just set it to true.
That means that by default I'm probably going to want to have this B camera off.
But I do want to make sure that the priority is higher than my normal camera.
So I'm going to crank it up to 100 and then turn it off.
Now I'm going to go back to this B trigger and let's take a look at it.
I'm going to hit F and go zoom in.
And look, we've got this little tiny box here.
You can kind of see the green there.
That's not the collider that I want.
I want to have a collider over here that my players touch.
And as soon as they touch it, the encounter kind of starts.
So, I'm going to drag it over here.
I kind of see it there underneath the ground.
And then I'm going to adjust the collider size.
I'm going to take the X, I'll just make it like a 20.
And I'll make the Y about a 20 as well.
Put this over this entire area.
So, if the player gets anywhere over here, it's going to trigger it instantly.
Now, I've got that set up, I think, correctly.
So, I'm going to save and I'm going to press play.
We'll run over there and I'm going to see if the camera switches once I get into that position.
Again, I turned my level one intro off so we don't have to watch that pop up or watch watch the entire intro every time.
Here we go.
Run over.
See if I can dodge the frog.
There we go.
Once I get into this area, yep, the camera has switched and we're ready for the bee to fly in.
So, let's save.
And I think we've gone quite a few changes in.
Let's go save off what we've got.
So, we've added the B to the level and an event trigger to start the encounter.
And we'll check that in.
Now that we've got our bee showing up in the camera appearing, let's trigger some cinematics so that our bee can do a cool flyin.
Let's add a bee cinematics underneath the bee encounter.
I'm going to rightclick, choose create empty, and call this B cinematic.
I'm going to add a playable director.
And then we're going to need a playable asset.
So I'll go into my cinematics folder, rightclick, choose create, and we're going to create another timeline.
We'll call this B intro.
And then we'll drag it onto that B cinematic.
There we go.
Now, we're going to double click and open it up.
And what I want to do first is make our bee fly in.
Let's double click on the bee.
I want to make him fly in from up here and do a little loop and kind of present himself all while he's doing his animations.
So, I'm going to go to the B cinematic that's got my playable director and I'm going to create a new track.
We're going to use an animation track and we're going to take this B root object and use that as the thing that we're animating.
If we look at the B root, you see that it doesn't have an animator on it, but the child down here, the base object is the one that has the animator that's doing all of the animation stuff.
And we're going to dive deeper into that in a moment.
But for now, we're going to go back and go to our B cinematic and we're going to take the B-root and drag it onto that animator track.
And it's going to want to add a new animator to the Broot.
So, we're going to hit create animator on Broot and then hit record.
Now, we can select this B-root object.
Notice that it now has an animator.
We can hit W to go into move mode and start adding some key frames.
So, right now at zero, it's going to be way up here.
I'm going to go to the 2C mark and drag it down to here so that it's going to fly way down there.
And then at the 2 point or maybe the 3 second mark, I'll have it go down a little bit more and forward.
Then at 4 seconds, I'll have it kind of come up.
And at five, let's make it go up a little bit more and backwards.
And six, we'll go back that way.
Seven, I'm going to come back down here.
And you can see what I'm doing.
Just kind of dragging it into a circle.
Go forward a second and kind of loop it around.
And I think that's kind of a good circle.
I'll stop recording now.
And if I press play, I can watch my bee do his animation and see him kind of go through that that entire thing.
But I just realized I don't have a key frame at the beginning where he's off screen.
So I'm going to hit record again.
We'll go select that B route one more time.
Actually, it was already selected.
And I'll just drag him up here.
So now let's stop recording and play one more time.
And we should see him do kind of that full fly in loop around kind of loop loop loop and then drop down and pop back up into that position.
So it seems like a decent enough animation.
You're welcome to adjust yours as much as you want.
Just remember the wings are going to be flapping in just a moment.
Right now they're not.
So we'll go now to our B trigger and we're going to add another event or another event registration on the event trigger happening.
So I hit plus and it added a copy of the existing one.
Instead I'm going to take the B cinematic, drag that in as the target, find its playable director and choose play.
Now I need to also go to my B cinematic and make sure that play on Awake is not checked so that that doesn't play automatically and we'll save.
And now just to save some time and speed things up, I'll go to my player, hit F.
Let's zoom in and let's zoom out a little bit.
Now I'm going to hit W and move him over so he's right near the water.
and then save so that I can just jump right over the water, make sure the cinematic works, and not have to run quite as far.
So, we're going to be testing this quite a bit.
So, we run over here.
View changes.
The bee flies in.
He does a taunting little scary loop and ends in his correct position.
I can still shoot through them.
We haven't really set them all up, but his cinematic is happening and it's doing what I expect it to do.
Now, I think the last thing I want to do is find some sound effect of some bees and have that kick off and start playing.
Open game art.
Looks like it's got a couple of options.
I'll take this single B sound and I'm going to download it.
We'll open that zip up.
And then we've got this one B.wave.
Let's just drag it into the project.
So, you can go find whatever B sound you want.
I'm going to take this one and drop it right into my audio folder.
Copy.
We'll right click, hit show in explorer.
And then now that we're in the explorer folder, paste.
And now it'll appear.
There we go.
Got the B file.
The reason for that was that it was inside of a zip.
So I think let's see.
How do I want to add our B sound effect? Let's do it inside of our cinematic.
Let's just play the B sound when the cinematic kicks off.
So to do that, we'll go into the timeline.
We'll go add a new audio track.
And here again, we're going to need an audio source.
So I'll add the B encounter itself as the source.
And then that's going to add an audio source to the B encounter.
And then right here, we'll add a new clip.
And it's going to be our B clip.
I think I'll just let it play.
Let's just let it play here and loop.
So, to make it loop, we'll just check the loop box and then drag it out.
You can see that it'll loop all the way to the end.
And I'm going to save and press play.
Now we should be able to run over there, see our bee do his animation, and hear a little bit of a a taunting B sound for a second.
All right, I'm going to stop playing.
I don't want him buzzing anymore.
We'll go back into plastic and make sure that we've saved everything.
So, we've added the B intro and we'll check that in.
Now, let's take our bee and make him actually fight.
Let's turn this into a real encounter.
So, there are a couple of things that I want to do.
I want to have some platforms that the player can jump on to try to shoot at the bee and blast, but I want also have the bee shoot lightning back at them.
I also want to have the bee do a straightforward bolt shot that just kind of fires off and hits the player if they happen to be standing in front of them.
We have a couple different visual effects and I want to try to use them all.
So, let's start by adding some platforms so we can get a feel for it.
And then we'll add some powerful lightning effects that can kill the player to those as well.
We'll first take this.
Let's go with the um I've got a grass platform 2 here.
I'm just going to duplicate that and drag it over here to I think right about the same height.
So, I'm going to go with a 50 and a two here.
I'm going to take this and make it underneath my B encounter since it's going to be part of this B encounter.
And I'm going to call this a B platform instead of a grass platform.
Now, I want to modify this platform.
But first, I want to get a couple of them in position and figure out how I want them to be placed.
So, I'm going to duplicate this.
Drag it over here like that, I think.
Then, duplicate.
Drag over a bit more.
I want to go with kind of even numbers.
What was that? 60.
And what was the other one at? 50.
Let's go with 55.
So, we'll go over by five each time.
And um I think three is probably good.
I want to then duplicate those and then drag them down a bit and kind of off center.
So, they're like maybe like that or like that.
I'm thinking maybe more like that.
I'm not sure on the exact positions.
I might want to raise or lower them a little bit, but I think that that's pretty close to where I'd like them to be.
So, we've got some platforms that our player can now jump on and bounce around.
Let's just hit play.
Make sure that those are in a good position.
So, I come over here.
I can go up on these platforms.
Yep.
I can kind of like shoot, blast, go up and around.
Hopefully that bee doesn't touch me.
Go.
Hey, get back, Mr.
Bee.
Um, I'm thinking maybe the bee might even need to end up a little bit further to the right here.
So yeah, let's let's make a couple minor adjustments here.
To do that, we'll just take our B cinematic here.
I'm going to go to the timeline and we'll go find our let's go select that B cinematic.
We'll go find the B animation right here.
Hit the record button and right here at the end, go to that end part, I'm going to just move him so that he's over to the right a little bit.
So we'll go W.
We're going to have him end kind of over there.
Just going to go right around here.
do a loop and then go flying right back.
Let's zoom that in just a little bit.
Broo root W.
There we go.
I I had my my key frame out just a little too far.
I think we're good there.
Let's see.
Just going to go down and then back up.
Okay, cool.
That's in a slightly better ending position.
And I've got these platforms kind of where I want them.
So now I want Oh, let's stop recording.
I want these things to be deadly.
I want them to have a little lightning bolt that can pop up and kill the player.
We've got a lightning bolt visual effect inside of the prefabs folder that came with the B.
So I'm going to go find that.
Go find our lightning.
And I'm going to drag it down to be a child of this B platform.
Look that I've got this big giant lightning here.
If I go to my game view, well, I can't see it in there, but if I go down here, I could play it.
We'll play it in a moment.
Actually, let's first though make sure that it appears on top of our platform.
I don't like how it's showing right behind our platform.
So, we're going to expand it out.
Go find the two sprite renderers that are children of this lightning.
The one and the shadow.
See, these are two sprite renderers we've got.
And we're going to change their sorting layer.
I'm going to hit sorting layer and hit add sorting layer.
We'll hit plus.
And we're going to add effects.
We're going to have effects show up on top of everything else.
So they're kind of like right there in your face.
I think that's the way that they should be.
We go select one and shadow.
Change that sorting layer over to effects.
And there we go.
It's now on top.
I'm also going to move this lightning object up.
I'm going to select it, hold control, and drag it up to right about there.
Now, I'm not sure if I want to keep that size or shrink it down.
I think for now though, I'm going to leave it nice and big.
And then we'll press play.
Let's just run over there and watch it and see it in action for a second.
It's always cool to go check out your actual particle effects.
You can see it's got this lightning.
Okay, my position is actually off.
I do need to lower it back down.
So, let's put that back down to a zero.
No, that's too high.
Let's go to a 0.5.
I think that might be just about right.
There we go.
Looks like it's kind of landing at the right spot.
Let's go with maybe a point 4.
Yeah, that's even better.
So, I'm going to adjust it to a point 4.
I need to stop playing though and then go back in not in play mode and change it to the point 4.
Now I've got this B platform and I don't want to modify the prefab here because if I do I'm going to change all of the platforms including this one over here that's not supposed to be a BP specific one.
So instead we're going to create a new prefab variant.
I'm going to hit select and then that's going to give me my prefabs folder.
And I've got quite a few prefabs in here.
So, I think it's probably time to create a folder for platforms.
I'll create a subfolder and call this platforms.
And I'm just going to take all of the platform objects that we have and I'll move them into there real quick.
And then we'll create our prefab variant after that once we've got these just kind of moved out of the way and a little bit cleaned up.
It's always good to start creating folders once you get too many things.
And I feel like this is probably just about too many.
So, we've got our moving platform.
Moving platform.
Yep.
There we go.
Take all of those and I'm going to drag them up into platforms.
All right.
So, now we've got our platforms folder.
I'm going to take this B platform, drag it down, and make it be a prefab variant.
I've got a B platform variant.
Um, I don't know if I like the name variant in there, so I'm just going to select it and remove the word variant.
I'm going to select all of my other B platforms now.
One through five here.
Right click and find that prefab option.
Choose replace.
And then now I can find my B platform.
And I've got a bunch of B platforms.
I can save, play, and I should see the lightning just appearing at all of them.
And we're just about ready to start taking control of them.
Let's go over here.
Here we go.
Lightning is appearing everywhere.
I'm sure you can imagine that's pretty dangerous and deadly.
That be sorting is terrible, but that looks pretty scary.
So, let's find finish up by fixing the B sorting layer and then we'll start writing code in a moment.
Let's go to the B, find the B route, expand them out, and actually, let's just open up the prefab for it.
I'm going to hit the arrow there and we'll find all of the sprite renderers.
So, up here, we're going to do T equals sprite renderer.
And then that should just select only sprite renderers.
I'll find all of the objects.
We're going to do that equals.
It used to be a colon, but they changed it to an equals.
And now that we've got all the sprite renderers selected, we're going to change the sorting layer.
Instead of it being on default, we'll change it to enemies.
Go back, hit save, and now I want to play one more time.
Just watch that cinematic.
And then we'll save and and commit our changes.
Let's just jump over here though, and make sure that the bee looks good, the effects look good, be showing up in front of stuff.
We can see the transparency in his wings.
I think he's going to look pretty awesome once he's animating and controlling these attacks.
All right, we'll stop playing.
We'll go into plastic and we'll say that we've added B platforms with lightning visuals and check in.
To make this B fight into an interesting encounter, I want to give him a couple of different abilities.
The first is going to be this lightning shock that fires these little sparks.
And you can see it's on our platforms that we've already created and also on the ground.
Now, the way that it works is through a script that allows me to completely adjust and modify this.
If you take a look at my being counter script, you see I've got all kinds of lightning elements here and a bunch of different settings that allow me to change the way that this works.
I can adjust the number of simultaneous strikes.
I can adjust the delay between the strikes.
And I can adjust how long before the player takes damage.
And of course, I could move these lightning areas all around if I wanted to.
So, here is what we're aiming for, and now we're going to go through the process of creating it.
So, here's where we left off.
We've got our platforms with the lightning auto playing, and our bee has gone back to his home position.
We need to set up the script now that's going to control these lightning blasts, make the player take damage, and maybe add a couple more lightning strikes down on the ground.
So, to start, we're going to create a new script.
We're going to go into the scripts folder.
I'm going to shrink this down with control and the mouse wheel.
Right click, hit create, choose C# script, and we're going to call this B encounter.
Again, no spaces, but a capital B and a capital E.
We're going to select our B encounter object.
This is the parent again, not the one that actually has the B on it.
So, if I go to my B encounter, remember it's at 0 0.
And then underneath it, there's a child of a B visual that um the B root object right here that I can turn on and off.
I'm going to go to the B encounter that parent.
I'm going to minimize the audio.
source and I'm going to add a B encounter script to it.
Then we're going to open that script up and talk about the code.
Here's our B encounter script.
And before we get started, I want to mention that when it comes to creating a scripted encounter, there are definitely a couple of different options.
We can write out some code.
We can build some datadriven solution or we can do some sort of visual scripting option as well.
They're all somewhat valid options, but typically in most games, what I recommend to start with is a simple scripted setup.
You don't really want to start abstracting and building up state machines and script stuff until you have a good idea of what it is you're going to be building, how much of it you're going to be building, and who's going to be building it.
When you get to the point where you've got other people that are game designers that have no programming skills working on stuff, you want to start to look at some other options.
And as things grow and get bigger, you do.
But when you're just trying to build out a nice tight, good encounter, it's drastically faster, easier, and a lot easier to just get done quickly.
Well, not just quickly, but quickly and the exact way that you want if you write it in code.
So, that's how we're going to do this.
And we're going to start by just removing the start and update methods completely and adding an on enable.
That way, we can toggle this object on and off.
And inside of this on enable, we'll kick off a co- routine that runs our encounter.
So here we're going to add a start co- routine.
And we're going to call this co- routine start encounter.
I'll add my parenthesis, generate a method with it.
Alt enter.
And then we'll change the return type to not be string, but an enumerator, which is the one thing that Visual Studio constantly gets wrong.
It always wants to put a string there, but it should be an I enumerator.
I'm going to remove my private keywords and then let's talk about what our start encounter method should do.
The first thing I want it to do really is disable all of the lightning.
I want to turn all of that lightning off and then randomly pick some lightning and just turn one of them on.
And I think I'll start with that and then expand from there because the next thing I wanted to do is pick multiple and have them all turn on, you know, in an order and do more of the actions like we described.
So let's start by just turning off all the lightnings.
To do that, we'll say underscore lightning or let's add a for loop instead.
Delete that for each var lightning in underscore lightnings.
And then we'll say lightning not underscore lightning lightning.
Oobject set active to false.
Now, we don't have a lightning array here, but I'm thinking that for our lightnings, we're either going to want to reference the transform, the animator, or the game object.
I'm not sure which one yet.
So, let's just start with the transform.
I'm going to copy lightnings.
Actually, let's just hit alt enter and generate a field for it.
And we're going to change this.
Instead of being an I innumerable of object, we'll make it a list of transforms.
Transform.
We got to get rid of that s.
We'll make it a serialized field so it shows up in the inspector.
And then we'll have to do something after our start encounter.
So this right now should loop through all of our lightnings, set them to inactive.
And then let's do a yield return null and save.
We'll go into Unity.
Let's assign our lightnings real quick.
Make sure that this turns them off when we enable it.
it.
it.
And then we'll finish up the code after that.
So we'll go expand out our lightning objects.
And I don't want to grab my B platforms because I don't want these things turning off.
I want the lightning objects underneath it.
So, I'm going to go back to my B encounter.
I'm going to lock the inspector so that it stays on the B encounter.
Then, I'll go expand out all of these B platforms.
I'm going to go to the bottom one, hit right arrow up, right arrow up, right arrow up, right arrow up, and then go find all of the lightning objects.
I'm going to hold control and click on all of them.
There should be six of them so far.
And with all of them selected, I'll drag them right into lightnings.
Now, if you missed one, you messed one up, um, you can always just say it's that one right there.
If I remove that one from the list.
Did I remove it? There we go.
Hit the minus key.
Then I can always just click that single one that I missed and drag it in or clear it out.
Just make sure that you've got all of your lightning objects there.
I'm going to press play.
And when this enables, it should just turn those off.
If that's good, then we're good.
So, there we go.
It looks like it turned off all of the lightning objects.
Let's stop playing and jump back into code.
Now to turn a random lightning object on, we're just going to at first choose one at random and flip it on.
Now to choose one at random, we just pick a random number between zero and the number of lightning objects inside of our lightning list.
So to do that, I'll say var or let's just call it out as an int.
int is the same length as var.
And I'll call this int index equals and we'll use random.range.
And here it's not going to autocomplete because it's finding system.random, random, not Unity Engine.Random.
And that's because I have a using system statement up there, which is because something in here is using Oh, I think it's the serialized field attribute.
Let's see.
Let's remove the using system statement.
And you can see that now, oh, now we're good.
I guess I wasn't using the system statement.
So, we can do random.range from zero up to lightning's.
Now, if we do need to have the using system statement up there, by the way, we can also just add Unity engine right to the front of random.
So we can use the Unity random generator, not the Microsoft.NET system random generator, which is a slightly different random generator that requires you to instantiate it and deal with the seed.
It's a little bit more work than the Unity engine one.
So I I prefer to use that.
So now we've got a random index.
We'll turn on the object at that index.
So I'll say underscore lightnings at index.
There we go.
Oobject set true.
It already knew exactly what I wanted to do.
And then if we want this to just repeat, we'll just wait.
So we'll say yield return new wait for seconds.
And here we'll add in our delay between lightnings.
Let's make that a variable.
And then finally, we'll just turn this into a loop.
Let's actually first before we do the final part, generate a field for the delay.
Turn it into a serialized field and then give it a default value of I'm going to go with one.
So now we've got our code.
We just need to make this into a loop.
So I'll say for each or not for each while true and we'll add braces around it so that all of the code inside of the braces will run permanently or indefinitely.
It's going to run forever as long as this co- routine is running.
And it's just going to loop over, loop over, keep despawning them all and then spawning the next one.
It's going to actually despawn it a little bit early though.
It's going to spawn, despawn it before the lightning finishes striking.
Let's go check that out.
Make sure that it's doing what we expect.
There we go.
Go over to the lightning.
We can watch it.
You can see the lightnings appearing and then quickly disappearing.
The reason for that is that the delay between lightnings is two or is one right now, but the animation takes 2.5 seconds.
So, I change this up to about a 2.5.
I'll pretty much get a consistent non-stop lightning strike applying at one of these positions.
So, we're partway there.
We've got a somewhat interesting setup.
I think the last thing I want to do is change this to a 2.5 and save my scene.
And then I'm going to commit this and we'll talk about how we can make it a little bit more complicated.
Say added basic lightning control to the B encounter.
And let's check that in.
Our lightning visuals are working.
We've got one strike appearing, but now I want to make sure that it damages our player before we start to add a bunch of other strikes.
Let's make sure that it's fully functional.
So, inside of our start encounter method, we've got a loop that essentially spawns one piece of lightning or spawns a lightning strike and then it waits until whatever time we've got here.
And you saw that our timer kind of has to match our animation time for this to all work.
If we take a look at our animation, I can go into Unity, go find our lightning object, and go expand it out.
There's that base subobject.
I need to make sure I unlock my inspector.
Go take a look at my lightning strike.
Or even better yet, if I go to the base and go to the animation window, not animator, I can look at my lightning strike animation and I can see it actually play out.
I can drag the timeline across and see that it actually is supposed to strike or do damage right here at 1 and a half minutes.
That's what the 130 is.
30 is half of a minute.
So that's the halfway mark.
So it's supposed to stop, go to 1:30, and then it's basically all the way gone before the 2C mark.
It looks like there's some key frame out here at the end at 2:30.
I don't know why it's quite so long, but it looks like it actually ends at just about less than 2 seconds.
So I'm going to modify our code just a little bit to take advantage of that.
And we've got a couple options when we do this.
By the way, there's already an animation event that our animator has put into here.
I'm actually going to delete that out because I don't want to have to tie in an animation event and have my designers have to come in here and modify and move the animation event when I know it's at 150.
And if I want to change it later, I'd rather just have a slider in there for all of my B encounter settings that I can modify this setting on.
Now, using animation event can be good if you have lots of animations, you want to tie them all in and your animators and designers are good at using it that way, but I find that for this situation, putting it in my B encounter is going to make more sense.
So, I'm going to open up my B encounter script, and we're going to add in a couple new fields.
We've got a delay between lightning, which is right now kind of doing its job, but not really.
I want to add an animation length and a delay to damage.
So, I'm going to just duplicate the line twice with control D like I just did.
And I'll put delay before damage.
And then a um let's call this lightning animation time.
So, the full time of the animation, that's going to be two.
And the delay before damage is going to be 1.5.
I already know the values.
I want to be able to modify them, but since I know them, makes sense to put in an actual accurate value.
Now, inside of my loop here, inside of this while loop, instead of waiting for the delay between lightning, we'll wait for the delay before damage.
And then we'll damage players in range.
And we want to do players in range of our selected lightning object.
So to get that, I'll just copy part of line 28 up to the end of the index and paste it.
And that's going to give us a reference to the transform at that index in the list and pass in that transform.
So I add the semicolon home and alt enter to generate a method which should give me a private method that takes in a transform because that's what we're passing in.
I get rid of that private keyword.
Then after we damage players and range, which we'll write the code for in a moment, we want to wait a little bit longer.
We want to wait until the animation is done.
So let's copy line 30 and paste it down here on line 32.
And we don't want to wait for the entire animation time.
Right? If we go up here, if I just did it for this lightning animation time, then we would wait for 1.5 seconds damage players, then wait for another 2.5 seconds.
Now, I could change this to be maybe a.5 so that it's um the delay after damage, but I feel like having it just be the full lightning animation time is easier to understand.
So, I'm going to copy that and we'll just do a little bit of math.
We'll paste in lightning animation time minus delay before damage.
As long as these values are correct, so that this number is always greater than this number, we should be pretty good.
We shouldn't run into any problems.
Now, we can make sure that that's the case by adding an onvalidate.
So, we'll go up to the top and add one quick on validate and just say if the lightning animation time, so I'm going to copy that, is less than or equal to the delay before damage, then the lightning animation time is equal to the delay before damage.
so that our lightning animation time will always get just kind of cranked up if we accidentally mess with this delay before damage.
In fact, probably should adjust this.
Let's do that.
Let's change it so that our delay before damage has to always be less than our animation time.
So, here we'll just say that our delay before damage is equal to the lightning animation time.
I'll just adjust swap the order of those so that we keep the lightning animation time the same.
I think that makes more sense.
All right.
So, now we've got a loop here.
We just need our final wait.
So, we're waiting for that amount of time.
The last thing is to wait for our delay between lightning.
So, I'll copy delay between lightning.
Duplicate line 38 and paste it right in here.
So, we'll wait till the end of the shot and then play again when the next one is ready or play again once our delay is done.
Now, the last thing we need to do is damage our players.
So, here we've got our damage players in range method.
And the easiest way or I think one of the best ways to find all of the things in range of a specific place is to use the overlap circle method.
So we're going to say var hits or let's call this out again int hits equals physics 2d physics 2D dot and then there's an overlap circle.
Find this overlap circle method.
You can see that this will actually return back a number or the first object that overlaps.
That's not what we want.
There's a overlap circle all that will return back all of the objects that are within a circle radius of a specific position.
That's close to what we want.
But there's actually one method that a lot of people don't use.
And I generally recommend you use instead of overlap circle all.
If you're using any of the overlap alls, you should consider or at least look at using the overlap circle nonalloque or the nonalloque versions of any of them.
In fact, I would say you should consider you should almost always use them, especially if you're using it in something that's commonly called.
And that's because it won't create a new array of things to save off the hits into.
Instead, it will you'll use a a preset array or preset collection and you'll just be filling those up.
It saves you on garbage collection and saves you essentially saves you from allocating memory and causing performance issues.
So, we're going to use overlap circle nonalloc and we're going to give it the first parameter which is the point which is that transform right there.
And I'm going to rename this transform to be lightning because I want to make sure that it's not confused with my own local mono behavior transform.
So, I've got this lightning object.
I'm going to paste in lightning.position as the first parameter.
That was our position.
Next, we need a radius.
For that I want a ver a parameter variable and I'll call it lightning lightning radius.
This is that damage radius for it.
And then we need a set of results or an array of colliders.
You can see right here it's showing my collider 2D.
So here I'm just going to use underscore player hit results.
This doesn't exist just like our lightning radius doesn't exist.
And then finally, I'm going to add in a layer mask so that we only look at players and we don't look at anything else.
So I'll call this underscore player layer.
I'll add in a semicolon at the end.
And then I think I'll split these parameters out into new lines just so that it's easier to read.
So you can see I've got my hits call.
We pass in the position.
We pass in the radius, the hit results, and the player layer.
Let's create the radius first with alt enter.
We'll generate a field for it.
Hit F12 and change this to be a serializ field and give it a default of about one.
1 meter away is probably good, but we can always adjust this.
Now we'll go down.
We'll add the player hit results.
I'll hit alt enter.
Generate a field for that.
F12.
And you see we got a private array of collider 2Ds named player hit results.
I'm going to remove the private keyword and add a little bit of spacing here so that it just looks a little bit cleaner.
We got a little separation between our serialized fields and our regular private fields.
The last thing I want to do is add our player layer.
I'll hit alt enter.
Generate a field for that.
F12.
And this one I do want to be a serialized field for now.
So I'm actually going to cut it.
Move it up here.
Add a new line.
Copy the serialized field.
Paste it over the private.
And then we're going to change this from an int to a layer mask, which actually inherits from int.
So it's able to work just fine.
So we can use our layer mask.
Let's go click on it real quick.
Doesn't does not inherit from int.
I lied.
But it has a value from int and and it will work in here.
So, let's go down and um take a look at our code.
We should have no more errors.
Last thing we need to do is damage all of the players that we found.
So, we'll do a for loop and we're going to loop through the number of hits that we got because overlap circle nonalloc is returning back the number of things that it put into this player hit results.
Once we loop through it, we'll just access the player hit result at that index, which is right now is actually going to be null.
Let's take a look at this in a moment.
It's going to give us an error, but we'll access that.
We'll get its player component.
So, we'll say get component player.
Let's capitalize that G.
And then we'll tell it to take damage.
And for now, we're just not going to give it a vector.
I'm going to pass in vector 2 or 3.0 so that we don't pass in any damage vector so that it doesn't go flying off in any direction.
Now, the last thing that we need to fix with this is actually going to be an error.
But before we fix the error, I want to show you the error so you can see what it looks like because you're going to run into this many, many times.
I've seen it, I don't know how many times, and I think it's important to note.
So, we've got our B encounter.
We've got our player layer.
I'm going to switch it over to the player.
I'm going to save our scene.
We're going to press play and let's watch the error appear.
Go to the console and look at that.
Argument null exception value cannot be null.
And it says the parameter name is result.
So think for a second.
Don't click on it.
Think about what this might be.
If you can think about what the possible problem is, what could be null right now before you even click on it.
Think through the code that we've written.
Go take a quick look at it and think about it.
And then come over here and click on it.
Let's take another look.
So here you'll see that it says the value cannot be null and the parameter name is results and it's in the overlap circle internal.
And if I scroll down a little bit more, you can see the actual call stack.
So it was called by uh line 42 and then line which called line 50 which is in our damage players and range.
If I click on it, you see that it's the overlap circle all and it's this results parameter.
The reason it said results is if I hit comma here and go over, you see that the name right there is results.
Ah, if I can get over there far enough, it's that name of the parameter right here.
So the problem is that this player hit results is never initialized.
So we need to initialize it to a new collider 2D array and give it a default size.
Um usually we don't need a number probably as big as 100.
I probably go with like 10 since we're doing this on a player layer, but you can pick a size.
Usually I go with 100 as a default so that we can have up to a 100 things in that hit array.
Um again, it's players.
I'm only going to have one, two, maybe four at most.
So, that's probably fine.
Now, before I jump back into Unity, there's one other thing that I just forgot about, and you may have noticed as well, that I've not turning the lightning back off after the animation's over.
So, I'm going to copy line 40 here and paste it right after 43.
We'll set change this to be a false so that we turn the lightning object back off after the time has run out.
Let's go back into Unity and we'll press play.
And then I should expect to see my damage happening and some decent control here.
Although we can only have one lightning at a time, I can control how often those lightnings appear and uh what their damage radius is as well.
Let's see if I can take some damage.
There we go.
Look at that.
Worked perfectly fine.
And I expect it to work fine no matter what spot I'm on.
Let's crank up the radius though, just so we can see that it actually does impact things.
Like that I took damage there.
And if I want to turn down the delay between lightnings, I can put it at a zero and we'll just constantly get lightnings firing off over and over and over with a huge radius.
Let's turn that back down to one so that doesn't insta kill me.
But now you can see that I've got some control and it's very very easy to modify.
Let's stop playing now.
Go into plastic.
Say we've added player damage and some lightning control.
And then wait for them all to finish.
That way we can give ourselves a little bit of a delay without having to write very complicated code.
To start, let's grab our lightning and start extracting and refactoring some of this code.
Our start and counter method is already what is this almost 20 lines long.
I think it's about time to start shrinking it down and turning it into some things that are easier to digest.
The first thing I want to do is grab our lightning object after line 39.
So on line 40 say var lightning equals and here we're just going to get that lightnings at index.
Then we're going to replace the lightnings at index down below with the word lightning just so that we can get rid of and stop accessing it from the array.
We just kind of pull that reference to the object off.
add in a space and then do this awesome trick of selecting the entire thing, hitting alt enter or let's see, control shiftr.
Let's see if it's going to let me do it.
Rightclick and find the extract methods, quick actions and refactorings.
It's not going to let me refactor and extract.
That's fine.
Sometimes it works, sometimes it doesn't.
Depends on the code editor.
So instead what I'll do is select all that code hit controll X and then I'm going to write the code or the line start co- routine and here I'm going to call show lightning li ht n i n and I'll pass in the word lightning or our lightning object and add a semicolon.
We'll generate this method and get ready.
I've got my stuff on the clipboard.
I'm just going to paste it right in.
I do need to replace this string with iie numerator.
But now I've got code that's going to kick off a co- routine to show a lightning object and then wait for it.
So what if I wanted to show two lightning objects? Well, I could just duplicate this.
Well, actually, if I did that, it's going to just show that same lightning object, but I could duplicate the part that picks a lightning and then shows it um and then show it right afterwards.
So, I could take this bit of code right here.
Let's just copy it all and paste it.
Just got to get rid of the declarations here because they're already declared.
And then this would show another lightning.
Although theoretically it could pick the same random index and show that same lightning object.
Let's just do this for a moment.
Let's add a yield return new wait for seconds.
And we'll wait for a delay between strikes.
And then we'll add an alt enter, generate a field for it.
Hit F12.
We'll cut that.
I'm going to move it up here.
Um, we have delay between lightning and delay between strikes.
Um, I kind of feel like these are somewhat redundant, but they're not actually.
So, this is the lightning.
This is a between each individual attack, and then this is between each individual strike.
I'm going to put this delay at maybe like a 0.25.
And we'll do a build.
control shiftb jump into unity and let's just see that in action.
Make sure that we're getting two lightning strikes that our two co- routines are working and that everything is somewhat okay or see if everything just goes completely wild and haywire which is kind of what I expect.
Let's watch it.
So, here we go.
We're in the scene view and well, let's see.
If I go to the console tab, you see that stuff isn't really showing up, but I can see some lightning's kind of appearing and then disappearing instantly.
And what's happening here, let's take a look here.
If we go back to our code, is that we're in this while loop.
And in this while loop, we're doing a little bit of a wait.
We wait between strikes and we um is that it? Yeah.
And we do one yield for a frame.
But right after we kick off these two co- routines, we go right back to the loop and we turn these objects back to false or not active.
So, we're just disabling all of the objects again right at the end of it.
Now, if we waited, if we moved this outside of the while loop, it would get a little bit better.
Our first lightning might actually show partially, and our second one would still end up getting overwritten or disappearing or doing something weird.
Let's actually see that.
Let's cut this.
We'll move it up here to the beginning.
And we can actually delete out the while yield or the yield return null statement that was there.
And let's change it to be just like this.
and go take one more peek at Unity and see what that looks like.
See the behavior and then we'll talk about how we can wait for these co- routines to finish instead of having it kind of run them and keep kicking them off in a loop.
So let's see what happens if it's insta kicking them off in a loop without turning them off.
We're going to see lots and lots of lightning.
Get ready.
I'm going to go.
Let's just run over here.
There we go.
Tons of lightning appearing constantly.
some of them are getting interrupted halfway through because a new one starts it up and then eventually or really quickly my player dies.
So what we need to do is wait for these two co- routines to finish and we can do that with a simple statement which is a yield return wait until.
So do yield return wait until which waits until the condition inside of the lambda statement afterwards or the condition that's passed in is true or met.
So, we're going to create a lambda statement.
And the lambda statement is going to be that our active lightning objects are all um not active.
Now, to get access to know what our active lightning objects are, we're probably going to need to store them off somewhere.
So, let's create a list of active lightnings.
Let's create a list right up here.
list active lightnings or no list of transforms sorry named active lightnings and we'll just assign that to a new list and then we'll add in our new lightning objects to it.
So when we kick off a co- routine we'll say active lightnings.add and we'll add our lightning.
I'll do that down here for the second one as well.
And then we're just going to wait until all of the active lightnings game objects.
So, we'll do doall all of its game objects.
And here, I'm just going to do another lambda inside of this.
And we'll say t um no, not t.active self or game object.active self.
There we go.
And close that off.
So, we're going to wait until all of our active lightnings have their game object inactive.
So, that means that they are no longer active.
And then we'll clear out our active lightnings.
So say active lightnings.clear.
And I've got a typo right here where I missed my new keyword.
It's a new wait until.
Whenever we do the yield return, it's always yield return new wait until or it could be anything that we've cached off so that we're not creating a new one every frame or every time, which is even better, but beyond the scope of this for now.
So I've got my build, I think, working.
I should be able to jump back into Unity now and then control the number of active lightnings and the delay between them and the pause between them.
Let's go see if that's the case.
See if it's all up and working as we expect.
So you can see lightning lightning got two shots firing off.
Two more shots firing off.
Now I've only got one shot firing, two shots firing, two shots firing.
Let's turn up the number of shots.
Oh, I didn't.
And make it variable yet.
So, we won't turn up the number of shots, but we turn down that delay and they should fire at the exact same time.
Turn it up to like a 1 second and I can see that they fire about a second behind.
But let's watch one more time and see if we get the case where it doesn't fire off two.
If I change the delay between strikes to zero, eventually we should see a scenario where only one fires off.
And the reason that that's going to happen as soon as it does happen is that it's picking the same lightning object twice.
So, let's see if it happens.
Come on now.
It's never going to happen.
There we go.
It happened.
So, that happened again because we picked the lightning object and then we don't check to make sure that it wasn't the same lightning object that was picked before.
So, instead of adding our lightning and then um just picking it again, let's make sure that when we pick a lightning object, it's not already in our list.
So to do that, we could just do a check right here and say, say, say, let's see, how do we want to do this? Let's actually first let's take this bit of code here, line 49 through 53, and just delete it.
I'm going to get rid of that for a moment.
And I want to take the code here from lines 41 through 47.
And we're going to turn this into a method called spawn new lightning.
Let's do that.
Can we hit alt enter and extract a method? Maybe or Visual Studio let us.
If not, we'll just cut Crl X and say spawn yield return spawn new lightning.
Now we generate a method for that spawn new lightning with alt enter.
Make sure that it returns an IE numerator and then paste in our code here.
So this will spawn a new lightning object.
Oh, but we do need a reference to our active lightnings.
So, we've got to now decide, do we want Active Lightnings to be a field variable or a member that's just passed in? And this is a good time to promote this up to be a field.
To do that, we'll just change the name here.
Control-r, add an underscore to it.
Go home.
Control delete.
Control delete three more times.
Hit alt enter and generate a field.
Then I can just add that underscore right here.
And my code is fixed.
If I hit control-click on this, you can see that it just added that public list or private list, sorry, up at the top.
Let's delete out that private keyword.
So now we've got a spawn new lightning method that will spawn a new lightning.
Um, no.
And that's essentially all it's going to do.
We can duplicate that method or we can make it spawn any number of times.
But before we spawn a lightning, let's make sure that the one that we've picked isn't in our active lightnings list.
So in our spawn new lightning method, we'll say while active lightnings.contains contains lightning.
Then we're just going to pick a new index and create or select a new lightning.
So I'll copy lines 50 through 51 all the way up to the index part cuz I'm going to have to delete that int.
We'll add a brace here, paste it in, and delete out the var keyword.
And now we've got a loop here that's going to keep picking a random one until we pick one that's not in our list.
There is a theoretical and a very easy to cause giant crash bug here.
So before you start running this code, make sure you save your scene, save everything, and make sure that I would even say that you commit because you will crash the editor if you start playing with these values and start moving things around cuz you can get this while loop stuck and break the whole thing.
We'll talk about that in the next section though.
For now, I want to make sure that we can spawn any number of lightnings.
So we'll add a loop here.
We'll say four tab and we'll change length to number of lightnings.
And then we'll move line 45 inside of that loop.
We'll generate a field for number of lightnings.
Hit F12.
Change that to be a serialized field.
And I'm going to default it to one.
We'll cut it and move it right up here.
Oh, I did not cut that correctly.
So, cut it with Ctrl X and paste it up here.
So, now we've got a number of lightnings to show.
We've got the delay and we've got all of our other settings.
I think that we are ready to now go play with it, cause everything to blow up and have some fun adjusting some settings.
So, let's save.
Make sure that the whole scene is saved.
We'll go into plastic.
So, we've added a variable lightning count and check it in because again, we're going to be able to crash things.
May as well get us get our stuff in a perfect safe state before that happens.
We'll press play and let's just watch everything in action.
I'm just going to go to the scene view.
See the one lightning appear.
If I turn this up to two lightnings.
The next time we should get two appearing.
And there's a little bit of a delay between.
If I turn it up to three, we should get three appearing.
And notice that we're going to get three every time.
We're not going to get situations where we get one or two.
If I turn it up to four, we're going to get four appearing.
I can turn the delay down to zero and I'll get four appearing all at once.
I can turn it up to five and I get five appearing.
Turn it up to six.
I I'm guessing you know where this is going.
Let's turn up to six.
I get six appearing.
I turn it up to seven.
And my editor has completely crashed.
The game has blown up and I can't work anymore.
So hopefully I committed.
Hopefully you've committed too.
In the next section we're going to talk about what's going on and how to fix that.
Let's take a look at the code that blew up and see why it happened and what we can do to fix it.
But I also want to take this chance to introduce some more AI stuff because I think that when you run into some scenarios like this, if you can't figure out the problem on your own and you're having a hard time finding somebody else to help walk you through it, this is another great way to figure out what's going on.
So, instead of explaining the actual problem and solution to you, I'm going to copy the code that we've got right here, paste it into chat GPT and see if it can tell me why this is causing a hang.
And if so, then we'll continue on and we'll um we'll make it better.
So, I've got my chat GPT window open here, and I'll say, can you explain why this code is causing my Unity editor to freeze when I have more and let's go look at the actual name of my variable here.
More um light no uh let's see what is the actual variable number or variable name.
a number of lightnings higher than um the num than available lightnings when I have more number of lightning than the available lightnings.
And then I'll paste in my code down below.
Hit enter and let's see what it's doing.
It's saying that it gets stuck in an infinite loop when all the lightnings are already active.
See, it already is explaining and telling us exactly why we're trying to get one from the list that isn't active, but the number is higher than the actual available number.
And to fix this issue, again, why I wanted to show this, you can add a check to prevent an infinite loop to make sure that active lightnings never exceeds the total number of available lightnings.
Look at that.
Place that condition at the beginning of spawn new lightning and it will just bail out and say, "Hey, too many lightnings.
We're good to So I can copy that little bit of code, go paste it right at the beginning of spawn new lightning, save, do a build, and notice this yield break statement.
What that's going to do is actually return from here and not continue on execution.
So it's going to log out an error continue or break this code or not break but break the execution of the code so it stops executing it and then allow the code to continue back at one level up.
So, that should fix our issue.
Let's press play.
Not only should that fix our issue, but that should show you that AI is starting to make things um drastically different.
And the way that you solve these problems, like not knowing the pro the actual issue here is, I think, a lot easier to to solve.
Now, you start searching, start putting in your code and finding the solutions for this stuff.
So here we've got a very simple, very easy solution that works, solves the problem.
Our error is gone, and now hopefully you're kind of inspired to start looking at chat GPT for some other ideas and other types of code and things that you might want to do.
Done a lot of it lately.
I highly, highly, highly, highly recommend it.
All right, let's stop playing and go check in our change that we've fixed the being counter or the infinite while loop.
and check that in.
Now that our bee is shooting lightning, you might be tempted to make it start moving around and maybe blasting off laser beams and doing a bunch of other cool stuff.
And while that is what we're going to do, there's something else that we need to do first, and that's make our player character movement a bit smoother.
If you look at our character right now, you can see that it's pretty easy to jump and get stuck on a platform.
Kind of jump up and bounce around.
You can I can even get stuck in between these platforms.
Sometimes you can get stuck in the water and not be able to jump out.
And there's a scenario here.
Watch what happens if I just keep jumping.
First, I'm not getting a jump animation.
And second, notice that my jumps are infinite.
So, there are a couple things going on with our player character that we're going to adjust.
We're going to make it so that our player feels a bit smoother, more like a natural platformer.
And then we'll add in the extra functionality for our bee.
Cuz right now, I could fight our bee.
I can make him really good at fighting, but our player doesn't handle well.
So, we can't really test that and get a good feel for it.
So, let's work on the player first and then we'll dive into the bee.
The first thing that I want to take a look at with our player is our jumping.
Let's take a look at our jump right in here.
You can see that I've got unlimited infinite jumps and we're not playing any animation.
And there's a very good reason for that.
Let's go take a look at our code.
We'll start by opening up the player script and let's look at the part where we see where we're grounded.
In our update grounding, we check against a center point.
We're doing array cast downwards.
If we hit something, we mark as grounded to true.
Then we check the left and do the same.
And then the right.
If any of those hit, if we have a ray that goes down from our character and touches any collider, then we say that we are grounded.
So, why is that happening when we're in the air? Let's go take a look at our character again.
And now, let's go look into at him in scene view, though, instead of in the game view.
So, go to the scene view, and we'll double click on our player, zoom out, and see that there don't appear to be any colliders here.
And if I select my player and go to the rigid body and expand out the info section where I can see the actual things he's contacting or touching, I can see that when he's on the ground, he's just touching the grass mid object there.
And when he's jumping, he's not touching anything at all.
So there's no collider that's following him or anything like that.
So I'm going to add in a line in my code to log out what's happening and tell me a little bit more about it.
I've got a couple options.
like I could log out a line or add a breakpoint.
We'll do both.
Let's go in here and when we find something in our update grounding that we've hit, we're just going to log what that object is.
So if is grounded is set to true, then we'll just log out the object and a reference to it.
And then we'll add in a breakpoint too just to debug and attach and show both ways to do it.
So here we'll say debug.log touching and then here we're going to give it the object that we're touching.
So, we'll use a braces and I'll put hit.c collider.
This is going to add the closing braces.
And it didn't automatically add the dollar sign at the beginning like Ryder usually does.
So, I'll go up there, type it, and add a semicolon at the end.
So, now this is going to tell us what object we're hitting.
I also want to be able to just click on the object.
So, I'll add in the second parameter to our debug.log, which is the context object or the object that you'll select when you click on it.
And we'll use the hit.colid.game object.
I'm going to copy this line 153 and paste it down here under 162.
So it's 163 and it looks like 173.
We'll save S.
Do a quick build with my control shiftB.
And then we're going to jump back into Unity and see what object is touching our ground or what object is being found to make us think that we're grounded.
If you already know what it is, don't worry.
You're you're ahead of the game.
If not though, we're going to show you exactly what it is by popping up this error log or debug log.
It's not actually an error log.
All right, here we are.
If we go over to our console now playing, you can see I've already got lots of log entries.
Touching B trigger, touching B trigger, and touching B trigger.
And if I select it, see that B trigger object appears.
I can jump and then eventually I get a touching ground, but I'm always getting a hit on this B trigger.
Let's go look at the B trigger.
I'm going to pause.
We'll go into scene view and we'll look at that trigger one more time.
Remember, this is the activation area for our B.
So, what's happening is our raycast is hitting that trigger and then thinking that it's the ground.
So, we're going to need to refactor our raycast a little bit and make it a little bit more intelligent so that it's not checking against triggers and other objects that we don't necessarily want it to.
We should also probably not have all of this copy and paste here.
We've got check center, check left, and check right.
They're all doing the same thing with just a very minor change, and it's very difficult to see what that change is.
You can see it's actually right here, the plus foot offset and or minus foot offset and plus foot offset.
So, get ready.
We're going to refactor this, clean it up, and make it a lot easier to understand and fix bugs along the way.
To fix our player controller and make it a lot more versatile, we're going to start by refactoring our update grounding method.
Instead of copying and pasting a check center, check left, and check right, we're going to call in a single check ground method and then just pass in the different positions that we want to check against.
That way, we can check the center, the far right, the far left, or any number of other points along the way, or just use totally arbitrary points.
To do that, we're going to start by taking the lines from 148 to the end of 154 and just extracting this into a method.
The reason that we're selecting this is because if you look at all of our lines below, the only thing that changes is the origin.
So, we're going to select everything after the origin.
So, the origin will be passed in as a parameter to the method that we're extracting.
If I select the origin here, in fact, let's do it real quick.
Select the origin, hit enter, alt enter, and extract.
You see that I get a method with no parameters named new method.
And I could call this check grounding.
But I wouldn't have a way to duplicate or reuse this with a different origin.
I'd have to go in and change it.
So I'm going to z.
We'll select again all the way up to the beginning of the hit, but not including the origin.
Alt enter.
And then extract the method.
And we'll call this check grounding.
And now we're passing in an origin.
inside of that check grounding method.
You see that we do our raycast just like before and we check to see if we hit a collider and do absolutely nothing different.
So nothing has changed in our check grounding.
We're just now extracted that into a separate method.
I can also delete line 148 here because I'm not going to need it.
If I delete it though, I'm going to get some errors.
Let's watch it.
So I delete it and you'll see that here on check left and check right, I was trying to use that hit variable or my code was and it's not there.
So, it's giving an error.
I don't want to do that, though.
I just want to call check grounding in each of these positions.
So, I'm going to copy check grounding, select lines, everything after the origin essentially down to the beginning of the check right and paste over it.
Do the same here on the check right side.
Replace hit all the way down to the end of the brace with a check again.
And now we're checking against the center, the left, and the right.
If I save now and do a build, I should have zero functional changes.
So, let's just go make sure that it works and that no nothing has actually changed functionally yet.
All right, we're back in and I can jump and double jump.
That seems good.
Jumping resets when I land on the ground and it should still bug out over here and I should still stay in like an infinite jumping state.
Okay, so no functional changes yet.
Just wanted to verify that.
Now that we've moved our check grounding code into a single method instead of copy and paste it or our raycast part here, we can modify this code to check and see if we're in a trigger so that we can ignore that trigger.
So let's do that now.
We'll go right above line 164 and let's add a check.
We'll check to see if we are in a trigger and if so, we're just going to return back out and not set that we're grounded.
So we'll say if hit.c collider and hit.c collider is trigger.
So if I'm if I hit a collider and I'm in a trigger in that case let's just uh return.
We won't say that we're inside of a or we're grounded at all and check grounding will not return if we hit a trigger as our thing that we're we're hitting with our raycast.
Now if I go back into Unity, you'll see that this somewhat fixes the issue.
Look, my character just got a little bit bugged out.
I can double jump now and I'm not getting the extra unlimited jumps here.
But my character will still occasionally bug out.
Look at that.
It still thinks that I'm in jumping mode right now.
And the reason for this, if I clear out my log, let's go back to the console and clear out the log and do a jump and see if we can see it.
Is that we land, we're touching the grass, and we're touching the grass and we're touching the grass, but then we stop touching the grass and we're not we're no longer grounded.
So, it thinks that my character is not grounded.
If I go to the player and go select them and then let's go check the is on is grounded and see that he doesn't look like he's grounded.
He actually doesn't think he's grounded.
And the reason for that is that our raycast notice that it's not hitting this showing this touching grass mid.
It's actually hitting the the the background here and never getting to the part.
So, not the background, the trigger area.
It's hitting the trigger area here on line 166 and never getting down to the next line.
Let's go into debug mode now.
like I mentioned before and see that in action.
So, if I put my breakpoint there, just click to the left and add a breakpoint and then press F5 or attach to Unity.
F5 is the default and the hotkey that I'm using.
It should now run our check grounding method multiple times per frame.
Let's see.
We should get a pause and a break any second now.
There we go.
And we'll see that we're hitting a collider.
That's the B trigger.
And then if I hit F10, it just wants to return.
And it's never going to get down here to line 169 to say that we're grounded.
So we need to change this.
The reason that this is happening, and it may not happen for you, it's going to be very dependent on your system and the scene setup.
Exactly.
The reason that it happens is the physics 2D raycast method only returns back the first thing that it hits or the first thing that it finds in the list.
And I believe it's doing them by the internal um object ID, but I'm not completely sure.
What we can do, however, is find all of the objects and then just loop through them.
So, we're going to change this check grounding method.
Instead of doing a raycast, we're going to do a raycast all.
I'm going to stop debugging.
We're going to change this from raycast to raycast all.
And then we're going to change from raycast hit 2D to arraycast hit 2D array by adding the two braces.
and rename this from hit to hits.
Then we'll add a for loop.
So we'll say for each var hit in hits and we'll add a opening brace.
I'll delete out that closing brace.
Go way down to the end of our if statement here.
Add a new line and another closing brace.
So now we've taken what we were doing against one raycast.
Hit these lines right here that I've selected 168 through 176.
And now we're running them against everything that we hit in our check in our raycast instead of just the first object.
Now, this is going to cause a little bit of a problem though because on line 169, we don't continue on and check all of the things.
We return back out if we hit a trigger.
That's not what we want to do.
We want to just continue on and check the next object so that our loop actually works and we've solved the problem.
Let's save now and go check it out.
see if we can now see our character working properly in that area or in our trigger area.
All right, here we are in the trigger area.
If I jump, I jump again.
Got my double jump, one jump, two jumps, and I'm good.
And it looks like my jumping is working.
I'm no longer bugging out.
I can land on the ground.
And things are getting a little bit better.
Let's go into the water, though.
So, I go into the water and I jump.
Land, jump, land, jump.
Oh, I can't jump anymore.
So, we need to make one more change to our check to make sure that if we're in the water, that also counts as being on the ground.
So, to do that, we'll stop playing, go back into our player script, and now we have that one single place to check.
We can check it right here on line 168.
So, if we hit a trigger and that trigger is not water, then we'll continue on.
If we hit a trigger and the trigger is water, then we're going to just mark it as grounded.
We'll say that yes, we are grounded because um the the object um well it's water so it's it counts as the ground.
So we'll say if the collider is trigger is true and hit.c collider.getcomponent water is equal to null.
So we did not get a water.
Now I'm going to add these out as separate lines because I think it makes it a lot easier to read.
And then let's evaluate it one more time.
make sure that it's all easy to understand.
We can probably refactor and change things around even a little bit more.
In fact, let's we I can see that we've got this hit collider check twice.
Let's move that up to the top and do an early exit so we can simplify this down a little bit.
So, I'm going to take line 173, cut it, move it up here to 168, and we'll say if hit.colider, and let's add a knot.
So, if it hit there's no collider, then we'll continue.
That way, I can get rid of the hit.
Check in the other spots.
So now on 171 I can get rid of that and simplify this statement down a little bit.
And then I can get rid of the braces on 176 and one now 179.
Kr D to fix my formatting.
And I think it's getting a little bit easier to read.
Let's do a shift delete on 175.
And now let's evaluate it one more time.
So we're looping through all of our hits.
If we didn't have a collider, somehow we've got something in here that doesn't have a collider.
Shouldn't happen.
But if that does happen, we'll continue on and just keep going.
If we hit a trigger and the trigger um does not have a water on it, then we'll continue on because water triggers, we want to count as ground, but everything else we don't.
Otherwise, we've hit something that's not a trigger and is is or is water.
So, we mark grounded to true and then we check to see if we should be marked on the snow.
Now, there is an issue here.
is on snow um could be set to true in one frame and false on another frame or another part of the frame.
So we could call in check grounding the left foot could be on snow and then we get is on snow to set to true and then we check the right foot right after that and if the right foot was not on snow then we could be setting it to false.
So if we want to make sure that if any piece is on snow that it gets set to true.
We can also make one quick modification to line 176.
And instead of doing an equals, we can do an or equals.
We do the it's shift in the key right above enter or shift in the the pipe that's right next to backsplash or backspace, not backsplash, backspace, and that will make it be set to true if it was false, but not set to false if it was true.
So it'll turn it on, but not turn it back off.
Now is on snow is already getting set to false at the beginning of the frame.
So it'll only get set to true.
It'll never get improperly set back to false.
All right, I think that's all we need.
We're going to save our code, do one more build, and then go test it out.
And here we are.
I should be able to jump normally on the regular ground.
Looks good.
In the water, I can jump unlimited, I assume.
I'm always marked as grounded.
Look at that.
Yep, jumping is good there.
And then if I go into my trigger area, jump.
Jump.
Looks good.
I can run around.
I still get stuck on things.
We haven't touched that yet, but I can still run and jump and properly get into the correct jumping and landed and grounded states.
Things are looking good.
So, I'm going to stop playing, go into plastic, and before we commit, let's do a quick diff and just take a look at our changes.
So, we'll open up the player diff.
And we can see that we've just added in well here's a little bit of extra spacing there.
But down below the part that matters, we've added in a check grounding method and we've refactored our update grounding to call that.
You can see that there's still a little bit of room to clean this up, I think, but it's getting quite a bit better.
And now we've got one spot that now works properly in triggers and in water.
So, let's close that out and say that we've fixed jumping in triggers and water and refactored the grounding method and we'll check that in.
Now that we've got our raycast refactored, we're going to pause and take a quick look at performance.
There's actually a good opportunity for some simple optimization and a good explanation of some of the things that are changing with the 2D physics system.
So, let's take a look at our character here.
I can run around and jump, and I can see that it's working fine.
I've got my double jump and all, but I want to look at how it's actually performing.
So, I'm going to open up the profiler.
I've got the tab here, but if you want to open it, you go to window and then go to analysis and profiler.
That'll bring up the profiler window.
I do have deep profile turned on.
You're going to want to stop playing.
Make sure that you go to the profile mode and turn on deep profile.
It turns on.
it gets that little uh you know the Unity visualization it's off and now it's turning back on.
With deep profiling on I can get performance characteristics of every single line of my code, not just at the top level.
If I don't have deep profiling on, I won't get full info about what's going on.
I'm going to press play now.
And when I say full info, I'll get things like the update for player took how much time, but it won't tell me how much each sub method that got called from inside of there.
If you enable deep profiling, it's going to give you the entire stack trace all the way down.
So, I'm going to go into profiler.
I've got my game running right here.
Go to the profiler tab right here.
And I'm just going to click on any old random frame.
I know that I call my grounding code and all the raycasting stuff every frame, so I don't really need to care which frame I'm on.
But if I scroll through here and I just look at the overview down here at the bottom.
Let's drag this up here to the top.
So I've got CPU usage and rendering showing.
I don't really care about rendering yet.
So I'm just going to drag this all the way up.
So just CPU usage is showing.
Here's a a scroll bar on the right hand side that allows me to go through all of the different things that are being profiled.
Again, I'm going to go up to the top and just select CPU usage and grab a frame here down in the hierarchy.
If you don't see the hierarchy and you see it as a timeline or maybe as a raw hierarchy or something, just make sure that you go select hierarchy.
And then if you don't see the thread correctly, I mean, it should be on main thread unless you went and selected something else.
Then scroll up to the top and we're going to sort by time.
So just click time ms right here.
So that the arrow is pointing down and the thing with the highest time is at the top.
We can see right up here at the top we have our update script run behavior update.
This is our code being run.
This is our own scripts being run.
And underneath it, we've got the behavior update, which is the update method for all of our scripts being called.
If I expand that out, you'll see that it's calling players up, player update, debug updater, event system, blaster shot, and some Cinem Machine update.
So, all of these things have an update in them.
The only one that's taking a good amount of time and doing this GC allocation, which is our garbage collector allocation, is the player update.
If I expand that out again, you'll see that it's actually all inside of the update grounding method.
And I can expand that out again.
I just use the right arrow and down arrows, by the way.
And I can see that check grounding is doing it.
I can keep expanding out and see that the biggest impactor right here is the debug.log.
That's usually the case.
If you have a debug log, it's going to destroy performance.
So, I'm going to remove that.
And then let's take a look at what else we can remove, though, or what else we can change.
If I go down a little bit further, you can see that much much smaller but still there as an issue is the physics 2D raycast all method.
If I expand that out, you see it's calling raycast all internal.
It's allocating some memory.
The GC alloc means that it's creating objects that are going to have to be cleaned up later and it's taking a little bit of time.
Now the time amount here I'm not too worried about.
It's 002 milliseconds.
It's not horrible, but the allocations I don't want happening.
So, we're going to fix that as well.
Let's stop playing and go look at the code now.
Now, in our code, the first fix, and the biggest one, is to just get rid of this line 177.
I'm just going to comment it out with my two forward slashes.
The next thing that we want to do, though, is change this raycast all.
Instead of using the array cast all method, we want to use one that doesn't allocate memory.
One that just reuses or restores off an array of things that it's hit and then fills that.
The reason for that is again so that we don't have to have objects that are being created and destroyed every single frame because that causes memory fragmentation, eventually causes garbage collection, and then that causes a freeze or a pause or a hitch on your game depending on the system that you're on.
But if you're not on a high-end system with fast memory access, you can expect that to happen.
So you want to minimize these allocations.
Now to do that, we've got a couple options.
We can use the raycast all nonalloc that appears as an option.
But what we actually want to do is switch back to raycast.
And that's because the way that the physics system is being updated, the raycast method is getting a bunch of overloads.
and the raycast all and raycast nonalloque.
In fact, all of the nonalloque overloads or methods are being removed or deprecated.
And we can see that easily by let's just go put the raycast nonalloc here and hitting F12.
If I hit F12, it's going to show me the decompiled code in my code editor.
And this is shows me that it's marked as exclude from docs.
And if I actually go look up this up in the documentation, you'll see that it does say that it's going to be deprecated soon.
So, what can we do? Well, what we can actually do is use one of these raycast overloads.
If I look right above it, you see there's a raycast that takes an origin, a direction, a contact filter, and has a list of results.
Or there's one up here with an array of results.
So, I can use one of these two methods as my um as my thing or my my call and then pass in the list or array of results.
So, let's go back and rewrite this.
We're going to just add a new line and I'm going to say int hits equals physics 2D raycast and we'll do the open parenthesis and I want I believe it's overload four.
So I'm just going to hit the down arrow until I get to the fourth one and I can see it.
Oh, is it four? No, it's number five.
So I know that the first parameter is my origin.
I'll pass that in.
Then our direction, which is vector 2 down.
Then we've got our Let's see if I can find my overload again.
overload 5, our contact filter.
So, we'll put let's just do a new contact filter for now.
And in that contact filter, we'll set the layer mask equal to underscore layer mask.
And then our next parameter for the array cast is going to be the results.
So, do underscore and oh, is it actually let's make sure that it's results.
Go down to number five.
Yes, results.
So, raycast hit array.
Let's call this underscore results.
And then finally, we need our distance, which we've used a 0.1, so we'll use a 0.1 for this as well.
I'll put the semicolon at the end.
And then I'm going to get rid of line 165, and we'll generate the results field.
We'll hit alt enter and generate a variable for it.
Hit F12.
We should have a private raycast array right here by our player data.
I'll get rid of the private keyword.
And then we're going to initialize the array to be a new raycast hit 2D array.
and give it a size of 100.
That's way larger than we'll need.
We're never going to have 100 colliders that we hit.
So, if we have more, we'll just overallocate it by quite a bit.
It's still a tiny amount of memory, but way more than we need.
All right, let's go back to our code.
I'll just hit the back button a couple times.
And I'm going to split this raycast into a few lines because feel like it's a little bit harder to read now because we've got our contact filter in there.
So, let's just split this all into new lines.
And then instead of looping through each hit, we need to do a for loop because hits is now an integer and not a collection.
And now we have an an array here of results.
But if we loop through all of these results, we'd be looping through a bunch of empty entries every time because it's got an 100 entries there.
And it may or may not be filled.
The array cast method is going to tell us how many things were put into the results array.
So we can just loop through that many times.
So we'll replace our for each with a for loop by typing four.
I'll hit tab a couple times and replace length with hits.
Then I'll delete out the brace here on 173, the for each loop, and that brace again on 173.
And then we'll add a new line here and just say var hit equals underscore results at index i.
So we give it the braces.
And now we're looping through all of our results and assigning their first result to hit, checking it, and then assigning the next result to hit and checking it.
And so on.
So, we're looping through them all without creating a new array.
We're now should be running this without allocating any extra memory.
Let's save, go into Unity, and try it out and see if our change worked and if our performance has improved.
All right, we're back in Unity with the profiler running.
I'm going to go over here.
We'll just find a random frame.
And we can look here at check grounding and see that it is now allocating zero and taking 002 milliseconds.
The raycast has shrunk down just a little bit and we've got zero allocations.
Things are looking good.
This is again a nice easy optimization and something that we should do on anything that we're doing a raycast for that's continuous.
If we're doing a raycast every frame, it should almost always be nonallocating.
In fact, there's very there's almost no excuse not to use one that doesn't allocate.
The overloads are there and they're kind of the default.
So, go with that on anything where you need to raycast continuously or where you're just going to do it often enough that the allocations are going to matter.
So, now that we've got that change in, I think I want to go into plastic and commit our changes.
We've also got um some extra junk here.
Just cleaning up and version updating.
But let's say that we've Let's see.
Let's do a diff real quick.
We'll pull up the player.
We'll diff.
And I guess the only note here will be that we've uh switched to ray casting a non-allocating version of raycasting.
So switched ground check to nonallocating raycast.
Now, we're going to dive into our character's wall sticking issue where you can run against walls and just keep kind of running and sticking in them or jumping up on them and you can see it kind of floating in through there or sticking on little ledges like this.
We're going to make it so that when you're pushing off to a direction and you're up against a wall, we know that you're touching a wall and we stop trying to run against it like a weirdo.
So, to do that, we're gonna make a couple of quick changes to our character.
But first, I'm going to stop playing and we're just going to grab a little wall and move it down here just so that we've got something to kind of block ourselves when we're not running.
I think I'll just take this grass platform, duplicate it, and move it right down here so that it's off to my left.
So, now I should be able to run against it.
And I want to be able to have just something that I can test to make sure that I don't have to jump every time.
Okay.
So, there we go.
I've got a little platform there, and I want to be able to stop running when I'm touching it.
So, let's stop playing and think about how we're going to go about doing this.
We've got a couple of options.
One thing that we could do is just make our character have zero friction so that they could slide down and it would fix the issue of them jumping up against the walls here.
So, they would kind of slip down, but it wouldn't fix the problem of me just running at a wall constantly.
I want to know a little bit more about what's going on with my character and be able to have a little bit tighter control over that.
So, just like we do a raycast downward for the ground to see if we're grounded, we can do some ray casts off to the sides to see if we are touching something that should stop us.
And then we can even specify what types of things should stop us and what things shouldn't.
So, if we want to have things that we can run up against and push, we can specify that those things are pushable.
And if we want to have things that just stop us, that can be the kind of default behavior.
So, to do that, we're going to need to modify our player script.
And we're gonna set it up so that we do raycasts out each side of our collider.
Now, we've got two different colliders.
Remember, we've got our standing collider and our ducking collider.
There's our standing collider and the ducking one.
And we want to do a raycast probably from the center of each collider out.
And then maybe one from near the top and one from near the bottom.
We could do any arbitrary number, but I'd say at least three like we have for the feet.
So, let's start by visualizing that inside of our player.
We'll add some gizmos in there that show the positions that we're talking about so we can make sure that we're actually raycasting from the right spots.
And then we'll hook it up to actually use those and fill in some fields.
Let's open up the player script.
And then let's find our ondraw gizmos.
And after we draw the right foot, let's go down and draw some gizmos for our left and right sides.
Let's make a method called draw gizmos for side.
And here I'm going to put in vector 2.
And we'll give it a number of points.
Let's say we're going to draw three gizmos for that side.
Then I'm going to duplicate that and do one for vector 2.
Now generate a method for this that's going to draw gizmos on each side.
And then we'll generate the method.
We're going to rename the first parameter from right to direction.
That's the one that we're facing.
And then the int here to be the number of points.
Now, we're going to need to figure out where to draw these.
It's going to be somewhere from our center and then um off in that direction, I think.
So, I think we'll start by just using the center point plus the offset to the right.
So, I'll say var origin equals transform.position plus direction.
And then um we'll just use that as our initial one.
Then we'll add in a oh this wants to be cast as a vector 3.
There we go.
So that it can combine them.
That's because the transform position is a vector 3 and vector the direction was a vector 2.
So now we've got a vector 3 for our origin.
And right now we're just going to draw a gizmo at that origin.
So we'll say gizmosdraw.
Let's do a wire sphere at that origin.
And we'll give it a default value.
I don't like a value of uh three.
I think that maybe like a 0.05 is good.
Give us a nice little wire sphere.
So that should give us a wire sphere right at the center there.
And then we'll set it up to do the number of points right afterwards.
Let's go back into Unity.
see if we have a wire sphere showing up somewhere off to the center and one meter over to the right and left.
There we go.
We've got one right and one to the left.
And if I go into prefab edit mode right there by clicking the arrow, see it becomes a little bit easier to see.
So, I've got my two points there.
Now, let's make it do points all the way up and down.
To do that, we'll change our code to use a loop.
So, instead of doing one at the origin, we'll do a loop.
We'll say four tab.
and we'll go through the number of points and then we'll move our code inside of that loop.
Now, we're doing them all at the exact same point.
And what we want to do instead is evenly distribute them from the top or the bottom.
So, we're going to need to figure out how tall this thing is and then divide that height by the number of points.
So, we'll create a collider height.
Let's call it float collider height.
And let's just start by using the height of our standing collider.
So say standing collider dotbounds do size.y.
And then we're going to use a like segment size.
Let's call that segment size.
So float segment size equals our collider height divided by our number of points.
It should give us a nice amount to go up by from the beginning.
Now take that segment size and we're going to go up segment size times number of points from the bottom of our character.
So let's spell that out kind of step by step.
Let's start at the bottom of our character.
So that's going to be our transform position minus half our collider height.
So that' be transform position minus a new vector 3 of 0 comma collider height divided by two and a zero.
So that's going to give us a base or the feet.
Now we want to go up however much our segment size is.
So say origin plus equals our segment size or actually it needs to be a new vector 3 first.
new vector 3 of 0 comma our segment size time I.
So we'll start at zero.
We're not going up at all.
Then we'll go up by whatever it is 33 or whatever the third is or 2 if we do five and then we'll go up to 04 and 6 and so on.
You kind of get the idea.
This assuming I did five had to three here.
So it' be 33 66 and one.
And then for our final parameter we'll put a zero for the Z.
So that should give us our origin going up from the center.
Again, we're using the standing collider only.
And right now, we're completely ignoring the direction.
So, we also need to offset it by the direction some amount.
To do that, we can just add another line here and move the origin over in that direction times some multiplier that we put in.
And so we'll say origin plus equals direction times and let's call this wall detection detect ci.
And then we'll generate a field for our wall detection distance.
Hit F12 and then go turn it into a float because of course it wants it to be a vector 2.
We'll make it a serialized field and then I'm going to cut it and move it up by the rest of our serialized fields.
and then give it a default value of I think about a 05.
I think that's that should be good based on our current character, but we can modify it now and adjust it.
Let's go back here and take a quick look.
So, our direction times wall detection distance is going to give us a vector 2 and origin really, really, really wants to be a vector 3.
Let's just um cast our direction as a vector 3 for now.
There we go.
and we'll do a quick build.
Now, we should be able to see our gizmos off to the side and specify how many of them there are.
And then we'll be ready to use those positions for our ray casting.
Again, I think it's always a lot easier if I do the gizmos first.
I can see where things are going to happen.
There we go.
I've got one point there and one point there.
And let's see.
Let's go find our values.
So, we've got our wall detection distance.
I can drag that in and out.
Oh, our number of points is not variable yet.
Let's go check that out.
So, let's replace this three with a variable.
Let's call it a point count.
public int point count.
And we'll move this in a second.
I'm going to set this to five.
We'll copy and replace these two threes here with this point count variable.
Let's do a quick build.
We'll jump back into Unity.
And then let's watch our points go up and down.
Then we'll move that and figure out a good name for it.
I'm thinking like a wall point count or wall check count.
Uh something like that.
We got to come up with a good variable name.
So I've got my point count here.
And if I adjust this up and down, I get absolutely no change.
And the reason for that is that we're using the standing collider.
And if I turn the collider on, you see that suddenly all of my points are working.
And that's just because our code was looking at a collider that wasn't on.
And we actually need to look at the correct collider.
So instead of using standing collider.bounds bounds size.
Let's pick the correct collider.
We'll say var active collider equals.
And then here we want to check if we're ducking.
We'll say is ducking question mark.
We'll use the ducking collider.
And then if we're not ducking, we'll use the standing collider.
I don't think we have an is ducking variable yet.
So, we're going to need to go add that.
We'll copy is ducking.
And I believe in our is ducking code, we actually have a lowercase version of this variable.
Let's go find it.
Is ducking.
There we go.
Right here on line 140.
I'm just going to replace the var here and the is ducking with the c capital is ducking and then we'll replace it right there.
Replace it right here and replace it right there.
And then we'll generate a field for it.
I hit F12.
We'll move this field up by our other ones like is uh let's see is on snow and is grounded.
And then we'll make it public so we can sit there and watch it evaluate our is ducking and see what's going on in the inspector as well.
All right.
Now, let's go back to the code where we were using that right here.
Oh, I was already right at it.
And just make sure that we use the correct collider.
So, instead of using the standing collider, we use the correct active collider, the one that we're actually showing.
Let's go back into Unity one more time and look at our little wires or our little uh wire meshes up here.
We've got two, one, and two.
Change this up to three.
Now, I've got three there.
And I can change this up to like a let's go to five and see I get lots and lots of points.
And I can scale it up and kind of adjust the number of points that I'm going to get.
So this is mostly working, but I'd also like to add in a little bit of an offset as a final thing so that we're not checking against the bottom position right here.
And we kind of move this up so that it's off of the center instead of off of the ground.
We'll do that in the next section though.
So, for now, let's go in and commit our change to the player that we've added gizmos for wall detection.
And actually, before we check that in, let's make sure that we've moved that one variable that we had to move.
In fact, let's go back in and do a quick diff.
Rightclick, do a diff.
It's always good to do a quick diff before you commit.
Make sure that you've got things finished and in the right place.
And remember our point count.
That's the variable that I want to move up.
So, I'm going to cut that.
I'm going to move it up here.
And I can actually do this inside of the diff tool.
I don't generally recommend that you do it, but you can.
As long as we don't mess up and make any typos, we should be good.
I've got a serialized field for my point count.
Now, I'll save that, close it, and then commit our changes soon as it finishes completing domain.
Terrible name for a thing, but anyway, there we go.
Check in and done.
Currently, our rays or our gizmos for our rays aren't distributed evenly from the center.
And that's kind of intentionally.
So, we can use a cool trick to figure out how to make them be evenly distributed.
If we adjust the points and see if I go to like one point, it's down at the feet instead of in the center.
If I do two points, I have one at the feet and one in the center.
Three, I kind of get one split up here, but I never get one all the way to the top.
I get them kind of at the edges, but not where I really want them.
I want them to be centered.
If I have three points here, I want them to be centered from here and have one above the middle, one below the middle, and then have some offset there.
And I could figure out the code for it and explain the math and probably get confused.
But in a real scenario, if you get stuck and you want to do these kinds of things, the tool that I've been using and highly recommend everybody get into is the generative code AI stuff.
I like chat GPT, but any of the code options will do.
Let me show you why.
Let's take a look at our draw gizmos for side method.
And I'm going to copy it.
We're going to go back over to chat GPT and we're going to tell it that we like this method, but we'd like it to evenly distribute the points along the side from the center instead of from the bottom.
So, I'd like the following method.
Let's see if I can spell following to distribute points along the side of the collider from the center.
Let's say too evenly instead of from the bottom.
I'd also like to be able to specify a buffer for from the top and bottom for the points that's shared.
and let's paste in the code and let's see what it does.
My expectation is it's going to give us a buffer parameter or a buffer field and then it's going to modify the code and give us essentially a working version.
So here we go.
We've got a draw gizmos for side.
It's taking a look at the collider height and using the buffer.
Now it's figuring out the segment size which is the number of points.
Oh, minus one.
probably part of the problem with our our code.
And then it'll loop through the number of points.
Let's see.
It's almost done.
Start from the bottom instead of the center.
I don't know why it's starting from the bottom.
Well, I guess it's explaining what it's doing.
It makes sense that it would start from the bottom though because the way the math works.
And then it's going to loop up and give us our code.
So, let's let's copy the code.
We'll paste it into the editor and see if it just works.
So, we paste.
We save.
We go back into Unity and as soon as it recompiles, oh, it doesn't look like it recompiled.
I haven't passed in that last parameter.
So, once we've saved, we know now have this buffer parameter that we need to pass in.
Let's just call this uh underscorebuffer.
And we'll generate a field for it.
Copy that in and paste it into both of these calls.
Should probably just make this like a global field.
And we'll give this a value of 0.1.
I'm going to make this a serialized field.
I spelled serialized totally wrong, but I'm going to cut it, move it up here, and then just copy and paste.
All right.
Now, if once I get my F on the end there, we should be able to jump into Unity and see if the AI was able to give us working code, which nine out of 10 times it just does.
Look at that.
We've got some nice evenly distributed points here.
We can adjust this barrier kind of up and down.
Oh, the buffer isn't working correct.
It doesn't give us one from the bottom, but we can adjust the point count and see that that's working.
So, let's set this buffer back to a zero here and adjust the point count up and down and watch the values.
You can see that it's filling in pretty good, but our buffer doesn't work.
So, let's fix the buffer part.
To do that, we'll go back into chat GPT and say the buffer only works from the bottom.
I'd like it to work from the bottom and top simultaneously.
I think I spelled that close enough.
And it's going to apologize, I'm sure, and then give us a corrected version of it where the buffer works on the top and the bottom.
So, we get our updated gizmos code.
And then once I'm done with it, if I'm curious on what the difference was, I can just ask it, hey, what was the difference? And why does this one work? Why did the other one not work? A lot of the time though, when it comes to simple stuff like this, this is the code that I'm gonna write once and then forget all about because I once it works, it works.
I don't need to think too much about it and I don't want to spend a ton of time just uh locking it into my head.
So, I'm going to copy this code again.
We'll go back into Unity.
We'll go find our method one more time.
Draw gizmos for side.
We'll paste over it, assuming that everything is okay.
One thing I did notice is that the word detection is wrong here.
So, let's replace this.
Wall detection.
I think I typoed that before and uh put that into the bot and the bot got confused.
All right.
So, now we've got our code.
We jump back in.
We should have a working buffer is my guess.
I haven't even checked it.
I'm just guessing that it's probably going to get a buffer that works.
Oh, nope.
Now we got a buffer that works only from the top or only from the bottom.
So, let's try it again.
That buffer only works from the bottom.
I'd like one that works from the top.
Bottom and top at the same time.
There we go.
Now it's explaining the problem.
The buffer should be added to the base of the collider.
Yep.
when computing the origin.
Okay, so version three or the third time should should solve the problem.
This happens again a lot when you're going through AI stuff.
Um you're going to get code that just doesn't quite work.
And if you correct it, you'll get the fixed version most of the time and doesn't always work and it's getting drastically better, but by the time you watch this, it could be 10 times better than this even.
So don't just avoid it because it gets things wrong the first time.
just continue the conversation with it until it starts to understand what it is you're trying to do.
Unless, of course, it's just taking you way longer than doing it yourself.
Don't obviously don't do it for things where you already know the the solution.
So, let's fix this detection distance again.
I just pasted over the code one last time in hopes that the system has finally figured out the problem.
Let's go see.
So, I've got some points.
They look pretty evenly distributed.
I changed that buffer to a 0.1.
That looks good.
Change this to maybe three points.
All right, I am liking what I'm seeing.
My buffers are good.
My points are good.
And I'm ready to do the raycasts.
Before we do that though, let's go check in our code that we've uh added buffer and proper spacing to wall detection points.
And we'll check that in.
Now that our player can jump around and dodge the bee's attacks, let's give him more attacks and give our player the ability to kill the bee.
And that's where we're going to start.
We're going to add some colliders to our bee and make it take some damage.
This should be a pretty simple process.
We're going to start by going down to our Broot object underneath the B encounter.
Remember, our B encounter holds the bee and the platforms and all of the other things related to this boss fight.
The Broot is the actual character that has an animator that we haven't set up yet and then has underneath it all of the different body parts.
The first thing that we're going to want to do is add some colliders to the parts of the body that we want our player to be able to shoot.
Now, that might not be the entire body.
A lot of the time we want it to be specific parts or sometimes it's even just specific parts that are only activated when they're in the middle of some certain animation.
This character has a couple pieces that we could use like that, but we're going to start with just adding colliders to the body and the head and leaving it off of the wings and the little tentacle things going up.
Make it a little bit harder to hit the guy, but not too difficult.
To do that, we're going to select the body parts that we need.
Looks like the head on is one of them.
We'll add a polygon collider to it.
And then I'm going to select down.
Let's click again until I don't want the effect parts.
No, we'll click right here.
This is the body front.
So, we'll add a polygon collider to that as well.
And then I want this big base part of the body, too.
So, I'm going to click and select it.
It looks like that's body back number one.
And I'll hit add a polygon collider there as well.
Now, again, I mentioned that these change.
So, we've got a part two.
If I turn this on, you see this is a slightly different one.
Um, you can't really tell the difference, though.
I think let's see.
Switch it.
You You probably can't tell unless Oh, yeah.
There you can see it.
So you can see that's the one for when he's animating and trying to shoot out.
But it does some rotation and stuff.
So it's a little bit more difficult to see it.
For now though, we're going to turn that back off and just make it so that you can only shoot the bee when he's kind of in these normal modes.
Although I believe you can hit his head anytime that he's not dead.
All right.
So we've got some colliders on him.
And if we shoot him right now, nothing's going to happen because he's not set up to take any damage.
Now to make him take damage, we've got a couple options.
We could go add a script where we've got these colliders here for our polygon colliders and implement the I take damage method and then figure out how to pass that along to our B.
But a simpler and less involved solution that I think works a little bit better, requires a lot less setup and is less likely to break is to open up our blaster shot script and have our blaster shot look for parent objects that take damage if it doesn't find one on the collider that it hit.
So to do that, we'll just add in a line here after 49 and say if damageable, let's see, I spell it right.
Equals null.
Then we're going to just assign it.
So I'll copy line 49 except for the var.
And we'll use get component in children.
So if we don't get an object, we'll find a child or not in children.
I said the wrong word, in parent.
So we'll find an object in the parent or up the hierarchy that has the I take damage interface.
If we find that, then we'll tell that thing to take damage.
So, let's go back and look at our character one more time for our B.
So, our B has these different parts here that are all children of the B root object.
We could put our damage part on the B route, but really the B-root is just the animator and the piece that's moving around kind of moving those colliders and stuff.
The part that's got all our logic is the B encounter.
So, we're going to add the I take damage to our B encounter.
We'll go right up to the top, implement the interface or declare that we're going to implement it.
Then hit alt enter and generate the method.
Whoops, I hit F12.
I want to go down to the bottom.
We'll go to our take damage method.
And in here, we're going to make our character just take some damage.
So, we'll decrement the health that doesn't exist yet.
Underscore health minus minus.
And we'll check to see if the health is less than or equal to zero.
If our underscore health is less than or equal to zero, then we probably want to die.
And to die for now, let's just disable our B's object.
So, we'll say B set active to false.
So, we don't want to turn the whole encounter off, just that B object there.
Now, we going to need to implement or create these fields.
We're going to need a health field.
So, we'll generate that.
And then we're going to need a B field.
So, I'm going to generate that.
And we're going to make that into a serialized field.
Let's hit F12, go up there, and grab our fields.
So, the B first I'm going to move up right below our number of lightnings.
We'll make it a serialized field and we'll make it a game object cuz I want to be able to just turn that object on and off.
That's the moving bee.
Then we've got our health.
Let's make that default to about five so I can kill the bee pretty quickly.
And I'm going to make it public.
I want to be able to see and view this number temporarily, but I don't want to get it confused and make it a serialized field until it becomes a max health or something that's not changing at runtime.
For now though, we'll jump back into Unity.
Let it compile and then we should be able to now run over there and shoot our bee.
Have the messages go up to the bee encounter and kill our bee as the first step of being able to fight this actual battle.
Let's see if it works.
So, we'll get in, run around, run and jump, jump, jump, go blast our bee.
We should see the shots landing on him.
If I can land a shot.
Oh man, I'm terrible at this.
See if I can land a shot here.
I'm just going to go over next to him and shoot him.
There we go.
Shot him.
and he disappeared and died.
Looks like it's working so far.
So, I'm going to go into plastic now and just commit that our bee can take damage with his colliders and check in.
Oh, and save our scene, of course.
Now, we're going to work on the process of making our bee encounter much more challenging.
actually making it kind of fight back instead of just shooting some random lightning.
We're going to start by allowing our bee to move.
We'll give him some destination positions and move them along there and then talk about how we can use AI to make that even cooler.
Let's dive in though with our B encounter.
What we want is for the B object here, the B routt, let's hit W and go into move mode to move around during the fight, stop at different locations, and eventually let off that big laser blast that he's got.
So, we're going to start by creating some positions that he can move to.
We'll predefine four or five of them.
And then we'll dive into the B encounter script and see how we can hook those up and make him move among those points.
We'll start by right-clicking on the B encounter, choosing create empty, and making an empty object.
And that's going to be way off at 00 0, like way over there.
So, I'm just going to zoom in where I want it kind of loosely, and hit control shift F, and then zero out the Z position so that it's right there along the line.
This looks pretty good.
But I think like somewhere right around here in the middle is good cuz it's going to do like a laser blast down there.
So I'll take uh this point and then I'll duplicate it.
Actually, let's rename these real quick.
Let's name this destination_1.
I'm going to name it B destination_1.
Delete that duplicate.
And then I'll duplicate this one and get my second one with the underscore.
I'm going to put this one kind of up and maybe a little bit closer to the uh the top.
And then I'll duplicate again.
Maybe do one that's down low here somewhere.
and then one that's kind of uh I don't know maybe maybe in the middle something like that.
All right, I've got four destinations now and I want to hook those up to my B encounter and have him move around those points.
Let's go into our B encounter script.
And first the thing that I like to do is just give myself a reference to those points so that I've got something to use in my code.
So we'll add a serialized field and this is going to be a transform array because we have multiple transforms.
It could also be a list of transforms.
Let's just use a transform array.
And we're going to call this B destinations.
We'll go back into Unity and assign those real quick.
First, I'll do a quick build.
Control shiftB.
Jump back into Unity.
We'll assign those and then we'll hook up the code for it.
I know if I don't assign them now, there's a good chance that I'll forget to assign them later.
That's why usually when I make a serialized field, if possible, I just go assign it.
So, it's locked.
I've got the window locked on the BN counter.
We'll drag the destinations onto the destination section and we get all four of them.
And then I'll unlock this so I don't get confused later.
Go recheck my B encounter and open up the B encounter script.
So in our on enable, we kick off a co- routine that starts the encounter.
I want to change this up a little bit.
Let's make multiple co- routines.
Have our start encounter be something like a start lightning and then have a start movement method that we call as well.
So, we're going to rename start encounter to start lightning.
And then I'm going to duplicate line 33 and change lightning here to movement.
We'll create a new co- routine with alt enter just generate a method.
It's going to of course have string there.
So, I'll replace it with i numerator and then we're going to add in our code.
So, first thing we want to do in this code is create a while loop.
We want just a loop that's going to run indefinitely.
Um, just like we have here on line 50.
We don't have any real setup to do.
So, we'll say while true.
So, for the rest of this thing, as long as this object's around, we want to get the next destination.
Figure out what that is.
And then we want to move towards that destination.
So we'll say var destination equals_b destinations at and then let's create a variable for this which should be our destination index and then we'll generate a property or a field for this.
I think I want to do this as a field so that I can see it in the inspector just kind of debug it although it could just be a local variable declared right here above line 39.
I'm going to generate it as a field though.
And then I'll just add the uh well, let's make it I'm going to make it a serialized field for now.
I could make No, I'm going to make it public because I don't want to accidentally get confused that it is a serialized field that I want to be serializing, but I do want to debug and view it and be able to change it and play around with it for a little while before I make it private.
So, I'll probably in the end make it private and have a show in inspector or something.
But for now, we want to be able to also just slide this and adjust the value and and try out different things.
All right.
So, in our start movement method, we're getting our destination.
Next, we need to get the direction to that destination.
To do that, we say var direction equals.
And here, we just use our local position transform.position minus the destination.position.
And this is actually wrong.
This is broken.
And it's a problem.
And it's a problem that's very easy to fall into when you start moving around child objects.
Let's think about this for just a second.
The transform here is the B encounter transform.
It is not the transform for our B's object, the B root here.
This animator that that we have.
We need to use that object and move that around instead.
So we need to move the underscoreb transform, not the B encounter transform.
To do that, we'll just change this code right here to say underscoreb.transform.
transform.position.
So now we've got the direction to the destination.
Next we need to normalize it because when we subtract those two vectors we don't actually get the direction.
We get the entire distance in xy coordinates how far away it is and in the direction essentially we get the direction ma with the magnitude.
We want the direction normalized though which is just setting it down so that the vector max or the vector's magnitude is one.
And so if it's straight up and down, it'd be like a one on the y and a zero on the x.
And if it's at a 45 degree angle, it's whatever it is, like 7.77 on both of them because it I think it's 707.
It it normalizes them out so that the total magnitude, the total distance from the center is still one unit.
That's what normalizing is.
It makes it so that the distance from the center point in the direction is one unit, which in unity is typically 1 meter.
So we're normalizing our direction.
And now we need to move in the direction of that normalized direction.
So to do that we're going to create another while loop.
We'll say while vector 2.d distance and here we want to check the B transform position and our own destination.osition.
So while that is greater than and here we want some sort of movement threshold.
Let's just start with a 0.1.
So a tenth of a meter.
While it's more than a tenth of a meter away.
Oh, missing an closing parenthesis there.
Um, what we want to do is move towards that position.
So, we'll say underscoreb.t transform.position equals vector 2 dot whoop.
See if I can get that right.
Vector 2 dot move towards and we'll give it our current actually really we don't even need the direction here.
We'll give it our current position b.transform.position and our destination.position.
position.
Now, now that I'm realizing that we don't need that, oh, we'll need the third parameter, though.
So, we'll need our speed or our movement amount, which for now, we'll start with time.
Delta time, which is going to move it 1 meter per second because over a time of 1 second, it'll move one meter distance.
That's what that third parameter is.
Let's fix the formatting here and talk a little bit more about this code.
So, our distance check is I added an extra parenthesy.
Our distance check is good.
And now our B movement is I think solid.
But again, we don't need the direction part now because we're using the move towards method instead of actually adding direction.
So I'm going to delete outlines 42 and 43.
I did want to leave them in there though because that's kind of the default thing that I start to do when I start writing code.
I end up writing things to get the direction and then half the time realize, oh yeah, I don't need the direction.
I'm using move towards.
So we use move towards to move towards our destination.
And there we go.
clean up our formatting.
And then finally, we want to yield return null.
Once we've reached our destination, we just want to increment our destination index.
So, we'll say destination index plus+.
And then we need to check to make sure that our index didn't go past the number of B destinations that we have.
If we got four B destinations, we get an index of four.
We're going to get an out of range exception.
So, we'll say if underscore destination index, did I get it right? There it is.
is greater than or equal to our B destinations.length, then we simply want to set the destination index back down to zero.
So, we're just going to loop it back down over to zero.
So, right now, we're looping through all of these points and our character or our B should move between them when the start movement method kicks off.
Let's go into Unity now and see if it works.
We should have our B destinations assigned.
Just got to go double check that.
Yep.
And our B is in there.
And our destination index right now is at zero.
So we'll press play and run on over here.
Let the encounter start.
He's going to go do that animation playing back.
And then he's going to go snap over, jump over to that first position, and then he's going to move to his second position and his third position and his fourth position.
and then back down to the fifth position or the fourth pos the first position.
Sorry, getting my words mixed up.
Oh, no, actually he's going to three.
Now he's going to the first one.
And you can tell that by looking at the destination index and see he's going to one.
Now he's going to two.
And the reason I wanted to leave this open if I just change this to a zero.
Then I can force it to go to the the next one.
I I think I'll probably just make this read only though, so that it's just visible in the inspector because I'm not seeing a lot of value in being able to change it.
But I do see a lot of value in in being able to debug it and see what it is.
So now we've got our character moving around.
We're going to go into plastic and commit that before we make the changes to make him choose something at random instead of picking the same point.
And we're going to do that with a new class and something really cool and exciting, I think.
So for now, let's say the B moves between basic points, and we'll check that in.
Now, our bee moves, but he picks the same destinations every single time.
And I'd like him to randomize or choose a different set or different order so that our player doesn't know exactly where the bee is going to go.
It could go to one of the spots, but not necessarily always in the same order.
Got to add a little bit of variation here.
And there are a lot of ways that we could go about this, just like anything with coding.
And what I wanted to do for this section is actually dive back into AI and asking AI a couple questions for ideas because I think that it's important that you remember that when you're building out code systems, there are multiple different ways to go about doing things and there are different um algorithms and solutions available.
So, let's go into chat GPT and I'm just going to tell it that I have a character in a Unity game that needs to choose random destinations from a list of transforms and just asking it what options do I have for randomly picking the points.
And I assume we're going to get back a probably a very basic answer at first.
So, it says that we could use system.random or Unity engine.random and then pick one at random with a range.
So, here we get the code.
We can see it's giving us a choose random destination method.
which just uses random.range from zero to the number of destinations and then picks one and gives it back to us.
Um, that'll work.
That right there will give us a random position and move our B towards it.
Uh, we may end up with situations where we choose the same destination twice.
But in that case, we would still um we would still probably just we would continue moving on because RB would be at that point and we pick another destination.
Although that might be kind of problematic if we wanted to do that and we wanted to do it with a stop and a pause.
So if we pick if we move to a destination, stop, pause, shoot, and then pick another destination.
If that same destination is picked, then that could be an issue.
So let's ask it if there's a way to do it without choosing the same destination twice.
Is there a way we can not choose the same destination twice in a row? I didn't even put a question mark, but it knows that I want an answer.
It says yes, you can check to ensure the same destination isn't picked.
And now it's going to give us another method for doing it.
So here it's got a interesting a do loop.
Not a fan of do dowhile loops.
So I'm sure we'll ask it to refactor this again.
So it says in this code we have a last index that stores the last index of the chosen thing and then uh okay and then checks to see if it was the val invalid one.
So actually let's just use this code.
I was thinking you know let's just change it and pick something else.
But it's important to be able to understand and read what this does even if I don't necessarily like Actually I'm going to tell it to refactor it.
But let's take a look at the do code right here.
So a dowhile loop actually runs kind of a lot like a for loop except it always runs the code in this do part first.
So it's going to run that and then it's going to continue looping it while this statement is true.
It's kind of like a while loop but it always does it the first time.
So let's copy this code and see if we can get it to work.
I'll hit copy code.
We'll jump back into Visual Studio.
And right below my start movement method, I'm just going to paste in this choose random destination.
And I'm gonna make it do a couple things.
First, I don't want it to return void.
I want it to return back the actual destination.
So, right now, I get back a destination.
That's a transform.
Let's just return back that same type.
So, we'll get a transform from our choose random destination.
And we remember have this list of B destination or this array of B destinations.
So, instead of using or just destinations, we use B destination.
So, I'm going to copy that and paste and paste and paste.
But now we've got a couple errors on count and that's because B destinations is not a list like destinations was.
It's an array and arrays have the length property, not the count.
So we'll just copy length over the counts.
Uh for this random message, it's thinking that we want to use system.random because we have a using system statement up at the top and we can't remove that.
So we'll just go back down to the error and put that it's a Unity engine.random.
There it is.
So go find it right here and say Unity engine.random.
random.range.
And then finally, oh, we've got one more instance of B destinations.
The last thing we want to do though is remove these kind of last two lines of code.
We don't need to cache the destination and we don't want to move our character to it.
So, let's delete.
Let's see what do we got here? Line 73, 74, 73.
Just keep deleting.
And then we're going to return back out that B destination at the index.
So, just do a return.
And I think uh oh, at the bottom, we'll need to return null.
If we have no destinations, we're going to get back null.
So, we should probably just be ready to deal with that.
Although, realistically, our code doesn't deal with that anywhere else.
So, we could probably um h we should probably just leave it there.
Let's leave it.
We'll do a build.
We should probably deal with it in the part where we choose a random destination.
So, let's put in choosing a random destination.
We'll copy choose random destination and paste it over line 41 here where we're setting it to the destination index.
And then we'll just say hey um if destination is equal to null let's do an error unable to choose a random destination for the B stopping movement and then we'll just return.
So we're going to exit out if we somehow can't get a point and we can't actually do a return.
What we have to do instead is a yield break.
I I always almost put yield return break, but it's a yield break, which is going to just exit out and return and stop our co- routine.
So, if we get to the point where somehow we can't pick a random destination, it means that our data is wrong, something's bad, we should stop, log out an error, and be ready to fix it.
The next thing we need to do is just delete out lines 53 through 55 because we don't need this destination index anymore.
So, just hit delete.
Delete.
And then let's go find that variable and make sure that we delete it as well.
We had that destination index right here.
This is line 23.
Shift delete.
We'll get rid of it.
We'll do a build.
And now we should expect to see that our B can move around randomly between positions and doesn't choose the same position twice.
Let's see if that's the case.
So run over here.
We'll watch our B.
We've kind of lost that destination index.
So we're just going to have to watch him move around.
There we go.
He gets to spot one, spot two, the next spot, and where is he going next? Down.
Back.
Oh, that back down to that bottom one.
Then back up and then back down.
I'm not liking the movement pattern that I'm seeing at all.
He's just going back and forth.
Oh, and now he went to a different one.
So, I don't particularly like this.
I I think that perhaps he should randomly choose all of the positions or from all of the positions at the beginning and then um loop through them once and then reset.
So let's ask chat GPT if it can give us a version that does that instead.
I'm going to start by copying my code.
So I've got my choose random destination method.
I don't want to continue the previous conversation because I've already modified this code and I want to be able to keep that code that I've modified.
So I'll take that.
I'll go into chat gpt and then before I paste in my code I'll just ask it can you rewrite this method so it chooses all the available positions before resetting or or res re returning to a position it's already been at make this reset once it's passed all of the positions and then I'll paste in my modified code and let's see what we get back.
So it says the current method is choosing a random index from array and making sure the chosen one isn't the same.
But my requirement is now changed and I want to make sure that they've all been visited.
So it says that we can do this by creating a list of indices from zero to length and every time we just pick a random destination we'll move the index on that list.
So here we can see what is it writing here if b destination's length is greater than zero.
If indices is null and indices count is equal to zero then indices is equal to the range.
Oh okay.
So the number of val in integers between the point or between the zero and the length and then it randomizes them.
Oh no.
It picks a random one from the indices and then okay gets it and then removes it from the the list.
This is a little bit confusing.
I'm going to ask it if it can write a less confusing one so it's less confusing.
I mean, I can follow what it's doing, but describing the um the steps is, I think, a little bit confusing.
I think that the having the extra indices is extra and probably not necessary.
So, let's see what happens here.
It's going to choose a random destination.
If we have no destinations, we return.
If they've all been visited, then we reset the indices.
Okay? It's going to select a random one and then it's going to set the destination index to that random one.
Okay.
So, this isn't is this making them go in uh yes, it is into the a random position of them.
So, this does kind of work and it's describing it a little bit more.
Let's ask if it can do it without the indices.
because I feel like that's the extra confusing part.
It doesn't need to be there and um could probably be refactored out.
There we go.
So now it's going to create a copy of B destinations array and shuffle it and then iterate through that shuffled array.
And I think that this is probably the solution that I would end up on unless we end up creating a separate class that does the randomization too, which is another option.
So maybe we'll let's see what this does and then we'll ask it if it can turn this into a class that can transform or shuffle transforms.
So here's a method that shuffles the transforms.
I don't think that we need something that that that necessarily written out.
we can probably use a link statement.
And then it's got a choose random destination method that's uh using that array.
So this this part I like.
The part I don't like still is that the shuffle is uh not not using um a simp it's it's a little bit more complicated than I think it needs to be.
So say can you convert this to a class that randomizes transforms like a grab bag or something? Sure, I can convert it.
It's going to be named transform grab bag.
And a grab bag is just a thing where you sh throw a bunch of stuff in and randomly pick out items and tell it's empty.
So that's just one of the many types of uh or terms for randomization system.
So here we go.
We've got a transform grab bag that takes a array of transforms that shuffles them and then allows us to grab one item.
And let's ask it real quick.
Can you write the shuffle or can you replace the shuffle method with a simple link statement? So here you'll see that it's going to rewrite it again.
But I also wanted to while it's doing that look at this code.
So here it's you create a grab bag and then just get a destination out of it.
I like this a lot more than I like having all of that extra code inside of our B encounter.
Since this code is going to be responsible just for randomly picking transforms, we can now use this anywhere.
We can use it for anything that needs to pick a random transform or a shuffled transform that needs to follow this the same rule.
And we don't have to clutter up our our B and encounter code again.
So, let's copy this code, the transform grab bag, and we're going to jump over to Unity.
We'll just paste it down here at the bottom.
and then I'll move it to its own class.
So click select the class name right here.
Alt enter and move to transform grabbag.cs.
We'll go back and we're going to delete out the using statements here.
Those extra ones that got pasted over.
And then we'll go to our transform grabbag.
Make sure that this looks good and built and check the code.
I don't see any errors here.
Sometimes the copy paste stuff from chatg could have code error typo or some weird formatting.
So I just got to double check it.
And now we'll go back into our B encounter and actually use this.
So if we look at the example from chat GPT.
Let's see if we can pull that one up.
It was recommending that we call the method like this.
We create a grab bag and then we get a destination from it.
So I'll copy that.
We'll jump over to our code and inside of our choose destination or get ran choose random destination.
We'll delete that or where we call it right up here.
We'll paste our new code.
So we got transform grabb bag that takes the destinations and then we'll take a destination from the bag.
So here I'm going to cut line 39 and paste it over 43.
Let's get rid of the all this duplicate stuff.
We got destination equals grabbag.grab.
And here we've got that grab bag being initialized.
Now the one thing we want to do is reinitialize this grab bag.
Um if it gets empty, right? Does it do that automatically? grab.
If it's greater than the length, then it shuffles.
Yep.
So, it does.
It'll automatically reset it.
We don't have to do anything else.
It's looking good.
Let's do a build now and see if it works.
And if you're thinking, hey, couldn't we make that more generic? The answer is yes.
We'll do that next.
So, let's hit play though and watch our B move around.
We should see him come in and then choose some random positions, but never going back to the same.
He shouldn't do that back and forth.
So, go up.
Okay, it's going to that position, that one, then he's going to go down.
Okay, we should just never see him kind of going back and forth through those same points.
We should see you'll go through all of the points and then reset and pick a new a new set of points.
So, he's going all the way up to that top one and then back down.
I think things are looking pretty good.
The last thing that I want to make sure of though is that if he does a reset in that loop, so with the grab bag, I want to make sure that it also checks to see that we haven't um we don't go back to the new the first last destination when we reset the grab bag.
So, when we shuffle our transforms, I want to make sure that we never pick the one that we ended on at the beginning of the last one.
So, let's copy this transform grab bag code one more time.
And I'm just going to again ask I could write the code for it, but I'm going to tell chat GPT to do it because I want to see if it can.
And we'll just go down here and say, can you change the method below so that when the the the when when when shuffle transforms is called because it ran out of options, it doesn't choose the last position as the first new position for shuffle.
Oh, and then I need to actually paste the code in.
All right, so we can modify shuffle transforms to ensure the next position is not chosen.
So here we go.
We should get the last one and it's just going to memorize or remember the either the index or the transform of the last one and then make sure that that's not the first one.
That's all it really needs to do.
Let's see.
We should see the change inside of the shuffle.
So shuffle is looking at okay knows what the last transform is and it's is it rewriting the link statement? Ah yep.
So it rewrites the link statement.
Oh and then it adds the last one.
Huh.
So, this is going to work, but it won't work properly because it's going to take the um the last transform and shove that in as the last one.
I just want it to not be the first.
I just want the last transform to be first, not always last every time.
Can you fix that? Again, sometimes it gets a little bit slower writing code with uh chat GPT, but I think that if you're not sure how to write these things, you're not sure how to solve the problem, having these conversations with it.
And writing the code back and forth is going to make a huge difference and make it makes so you can actually get things done that you weren't able to do or kind of got stuck on before.
So, here's our shuffle transforms that's now caching the last transform.
And here it's saying, hey, if it got shoved into number one, um, move it into numbers, or if it got shoved into index zero, the first spot, then move it up one.
So, this should do it.
We'll copy that code.
Go back into here and take our shuffle transforms.
And we're going to paste in that new shuffle transforms method.
Let's zoom it in just a little bit.
You can see the entire thing.
Add in a space here.
And we'll just reevaluate it one more time.
So, it's going to order all of the transforms randomly using a link statement.
It's not the best for allocations, but it doesn't matter because it's once per loop on our encounter.
It's not something we're going to need to worry about performance-wise.
We could always optimize it if it becomes an issue.
And then we're going to look to see if the last transform was put at the beginning.
If so, then we just move it down to the next spot so that it doesn't become the the same spot.
We're go back to the same spot.
Let's save.
We'll go back into Unity one last time, test it out, and then assuming I'm not crazy, we'll make our commit, assuming chat GPT didn't break my code, too.
Let's see.
So, we press play, run over here, jump, jump, try to dodge that lightning.
There we go.
And let's watch the B.
It's going to one position and another position.
And another one.
And another one.
I just want to make sure that it's working as expected.
I think it's looking good.
He's looping through.
And I'm not seeing any issues.
So, we'll go into plastic and commit our changes.
First, I'm going to stop playing.
Make sure I've saved my scene and say that we added the transform grab bag and randomized B movement.
and we'll check that in.
Now, we're going to take a quick detour because we have a perfect example here of something that could be using generics.
And if you're not very familiar with generics, don't worry.
They're very simple and you've actually been using them quite a bit.
Often people don't realize that they're using them because they've never created a new one and don't really know how it works.
It's actually super simple.
So, we're going to do that right now.
Let's dive back into our code and take a look at the grab bag example.
So, go find that code window right here.
There we go.
And we've got our grab bag right now that takes a set of transforms, an array of them, and then shuffles them up and gives us back a transform.
What if we wanted to do this with game objects, though, or sprites or items or weapons or any other type of object in our game? Well, we could copy and paste this and just replace transform with game object or with whatever thing it is that we wanted to grab from grab.
But there's an easier solution and that's the generics that I was just mentioning.
So to use generics, all we need to do is tell it that we want to use generics.
Really, we give it a less than and then a type declaration or a type name.
I'm going to put T here because that's the most common.
And we're just about done.
Now, this isn't going to allow me to pass in any type of object because transform grabbag still takes an array of transforms as a parameter.
So, I'd want to change that.
Instead of taking an array of transforms, I'm going to want to take in an array of t or whatever the type is that's specified by the thing that's using the scrap bag.
So, let's put a t here.
And notice that we don't have an error.
And if I put my mouse over it that you are seeing that these are referencing the same thing.
Let's zoom it in a little bit.
You can see these T's are the same type.
So whatever type I declare for my grab bag will be the type of object that I have to pass into here.
Now that obviously causes an issue here on line 12 because the transforms that I'm passing in are of some type.
We don't know what it is.
Just type T.
And the transforms that we're assigning to are an array of actual transform.
So the first thing I want to do before we change this type is rename some of these variables.
Instead of calling these transforms, let's call them underscore things because there could be any number of things.
they different types of things and they're not going to be transforms.
And if I have the word transform everywhere, it's going to get confusing.
For shuffled transforms, let's call it shuffled things.
And then for the parameter here, I'll just call this things as well.
And I think I'll rename the method here to be shuffle things.
I want to get rid of transform as much as possible except for in the types because we still have to do some actual code changes for the types.
Oh, the last thing we have here is last transform.
Let's rename this to last thing.
Whatever that thing is.
Now, we'll scroll up here and we're going to fix the error.
So, on line 12, we're assigning an array of t or whatever it is to an array of transforms.
That won't work.
So, we're going to need to change this transform here to be t as well.
Very simple, right? All we're doing is replacing transform with t or whatever the type is.
Remember, it doesn't have to be coming from a transform.
This could have been something that worked on game objects, on uh sprite renderers, or any other thing that we want to randomly pick from.
Okay, so we've got T there, we've got T here, we've got T there.
It's looking good so far.
If we scroll down to our grab method, though, we've got an error on 26 that it's trying to return back a transform, but shuffled things is an array of T's.
So, we're going to replace transform with T.
And remember again, T is not a specific class.
It's not a thing that exists yet.
It's just the placeholder that we've declared right here.
T is the placeholder for whatever class we decide to use this with or whatever class the consumer of this class decides to use it with.
All right, let's go down to shuffle things.
In shuffle things, we actually have an error that we're going to have to do something a little bit more complicated with, but it really ties in perfectly with generics.
On line 38, we check to see if we're past the number of things and if the thing at index zero is equal to our last thing.
And this doesn't work.
And the reason for it is that we can't apply well here it says you can't apply operands of type T and transform.
So we can change this transform here to be T.
That will get rid of one error down below.
But this still doesn't get rid of the error because now it says can't be applied for operands of type T and T.
Really helpful, right? Well, the problem here is that it doesn't know what T is.
And T could be some type of object that can't be compared.
That can't just be compared with a double equals.
So, we need to go up to the top and tell it that T is always going to be a class because it it it is always going to be a class in our situation.
So, to do that, we just put where T colon and you can see it's autocompleting class.
Now, this doesn't have to just be class.
It could be where T is a mono behavior.
We could put like mono behavior or if we had some inheritance chain where we had like NPCs that inherited we had dragons that inherit from NPCs or something we could have where it's an NPC and it only randomizes things that are NPCs or derived from there.
For now though, we just want any type of class cuz this is randomization.
We really probably could just randomize just about anything.
Randomly order just about anything.
So there we go.
We've got our shuffle things method.
It should be working as a generic with the last thing I want to do to it is rename it.
Instead of being transform grabbag, let's just do control-R and rename it to be a grab bag.
Now it's just a generic grab bag.
That should rename our file as well.
Let's go check the file.
Yep, we got it renamed.
It's now moved to be grabb.
And the old one is now marked as moved.
And then the last thing we've got to do is actually hook it up.
So we're going to use this grab bag.
If I try to do a build, I should see an error because it's trying to reference it without the type.
Right here on line 38, we have a grab bag that has a it's being assigned a new transform grab bag.
So, first thing we got to do is delete the word transform there and create a new grab bag, but we also have to specify the type.
And here, remember, we're using transforms.
So, we'll just use transform.
And then we'll do the same right here.
And we're good.
So we should be able to build and save.
Now one optimization we could make here is we could um maybe not pass in the transforms or not do transforms and do a grab bag of vector 3es that just returns back those vector 3es.
But I generally prefer to um stick with transforms a lot of time especially when I'm earlier in development.
I want to be able to move things around at runtime and play with stuff.
So just an idea there, but I wanted to make sure that you you know it's there.
So think about generics when you're writing code.
when you write something that you want to reuse and you find that you're like copying and pasting and just changing a couple things in a class, that's a perfect opportunity for generics.
So, keep an eye out for for options where where they make sense and uh just just remember that they're there.
All right, let's jump back into Unity.
Oh, and also remember that you use them all the time.
Get component in children, get component and parent, uh find objects of type, all of those use generics and a lot of other built-in Unity methods do as well.
So, say we added generic grab bag and we'll check that in.
Now that our bee can pick random locations, let's make him do something interesting at those locations, like stop and blast us with a giant laser.
The first step to make this happen is pretty simple.
We'll add a little bit of a delay once we've reached a destination and just wait there.
First though, let's actually delete line 57 because it's unused.
You can tell it's unused because it's light gray there, just kind of sitting there underlined, letting us know that we don't need it.
So, we'll delete it with control X.
Now, inside of our while loop for our start movement method, let's add in a delay.
And we'll have a delay that's randomized between some minimum and maximum amount of time.
So, to do that, we'll add a yield return new wait 4 seconds.
And then we're going to give it a time that's random.
So, we'll use the Unity engine.random.range between some minimum and maximum idle time.
Let's put a min idle time and a underscore max idle time.
We'll let that auto oops.
Let's let that autocomplete there and add the semicolon.
And then we'll go generate two fields for this minimum and maximum idle time.
So, I've got min and we've generated a max.
Hit F12 to go to them.
And let's add the serialized field attribute.
Hold alt and drag over the private keyword.
Add those square braces and the serialize field.
I'm going to move these up so that they're up by our other serialized fields.
We'll cut and paste them and then give them some default values of maybe one and two.
So, we'll wait between 1 and 2 seconds.
That should be enough for our delay to happen.
Let's go test it out.
Here's our bee.
He's moving around and he should stop in just a moment and wait for 1 to two seconds.
There we go.
And then move again and wait again for 1 to two seconds and so on.
Looking cool, but I really want to see this guy animating before we do an attack.
So, let's add in some animations to our code and then hook up the animator controller.
Let's go into the B encounter script and when we start moving, so right here before our while loop, let's tell our animator that we're moving.
To do that, we're going to say underscoreban animator set bool.
And we'll just set a boolean named move to true.
We don't have a B animator yet.
So, let's go create one.
I'll copy B animator.
I'm going to go up to the top.
Control and home to cut right up to the top.
And then we'll add a serialized field.
I think right below line 17 below my B object.
So I'm going to duplicate, put in B animator by pasting and change this to animator.
It's probably not going to be at the same level as the B.
So I don't want to replace that B game object.
I've got my B animator.
Now I'm going to go back down to my code and we set move to true while we're moving.
And then while we're doing this idle, I want to set move back to false.
So I'm going to copy this line, paste it right here on line 60, and set move to false.
So, we'll set move to true.
Move, keep moving, keep moving, keep moving, and then set move to false.
And then wait.
Okay, let's go back into Unity now and hook that up.
The first thing we're going to need to do is assign our B animator.
Let's expand out the B encounter and the B route and take a look.
So, if you see here, I've actually got an animator on this base object and an animator up at the B route.
And I know that the one on the B route is wrong, but I want to show you how to be able to tell that it's the wrong one, too.
What we can do is go into this B controller here.
And if we just give this any clip, let's go give it maybe our B idle.
We're actually going to delete this in just a moment.
And then go back up to this base B object.
Go to the animation window.
Instead, I've got this idle B and it looks good and it plays.
If I select the B route, you'll see that that same idle B does not play and everything says it's missing.
That's because this is at the wrong level in the hierarchy and just needs to be removed.
So, I'm going to remove that animator component.
Go back down to this base.
And like I said, I don't like this B animator override controller that we've got.
So, we're going to delete it and create a new animator.
Our B doesn't need to act the same way as our robot or anything else.
So, let's delete it and create a new controller.
We'll rightclick and choose create and choose an animator controller.
There it is.
And I'm going to name this B with a capital B so that way I know it's the one that I created.
I'll go to this base object underneath my B and take the B animator controller, drop it on there.
We'll double click it to open it and then take the idle animation to make that our default.
Now I want to be able to go from idle to moving.
So I'm going to take the move animation and drag that out as well.
We're going to need a transition from idle to move.
And I want that to be either when we're moving true or when we're not moving false.
and nothing more complicated.
The up and down animations here don't really work great for just ba basic movement.
They're more for attacks.
So instead of using them, I'm just going to add a boolean here and call this move.
We'll then add a transition from idle to move and add a condition here.
If we scroll down the preview window, I can see my conditions.
We'll hit plus and we'll make it to be conditional on movement being true or move being equal to true.
We'll add a transition back from move to idle.
And this one will of course be on move equals false.
All right.
Now that we've got our transitions going, one thing I want to change is this idle to move transition.
I want to get rid of the exit time because I want it to be really fast and immediate once I start moving that I see that transition happen or that I see the animation start playing.
Let's save.
Now, I want to go make sure that I've assigned my B correctly.
I think I talked about it, but I didn't actually assign it.
So, I've got the B encounter here.
take the B animator.
We'll drop that down.
We'll save.
We'll press play and then go watch our B animate.
So, here he is.
He's flying down.
Flying.
Flying.
Flying.
And then I expect he's going to go into his idle.
Yep.
And then flying.
And then once he reaches his next destination, he'll go back to an idle and then fly.
And then idle again.
Now that our bee can pause, let's give him an attack.
We'll open up our B animator controller to start.
And let's take the attack B blast animation and drag it right above idle here.
I'm going to line it up nice and cleanly and then add a new trigger.
This trigger will be named fire just like our other triggers.
And we'll rightclick, make a transition from any state into that attack animation.
I'm going to click on the transition and add a condition to be the fire condition.
So that when we fire trigger or when we trigger fire, our animation will play.
After our animation plays, we want to make a transition into idle and we should be good.
Now we can call fire and call the trigger this animation to play any time.
Let's save and jump back into the code.
Now to do our fire, we're going to need to set a trigger.
Let's just duplicate line 60 with control D.
Change this to set trigger and then make it be the fire trigger.
We don't need a parameter there, so we'll remove it.
So, we're going to stop moving and set the fire trigger.
Actually, I think I want to do this right after we wait for our delay, though.
So, let's move that down one line.
And then, let's add in a weight.
So, we want to wait until our animation has blasted or fired off.
And let's take a look at that to see what I'm talking about.
If we look at the bee's attack B blast animation, let's just go click on it and then press play and watch it play.
and it fires off.
He kind of does this charge and then finally does a launch or a blast part right there.
And if we double click on it, you can see that there's actually an animation event that the animator already added for us right at the point where he should be doing that firing off or that launching.
Let's see if we can select the B right up there and drag and kind of watch it.
Let's go select the correct animation, the attack one, and I drag it up.
You can see it's right about here where it wants to do the shot and then it would kind of end over here.
So, what I want to do is fire or wait until it gets to right about here and then enable the big blast object.
So, how are we going to do that? Well, we're going to do two things.
First, we're going to wait for a call back from this animation event.
And to do that, we can just go to our animator object and just use our shoot animation wrapper.
The same thing that we've used before that has an onshoot and an onreload.
Once we've added that, we can click on our animation event and just go choose shoot.
So now we've got a call back that we can register for when we get to this point and enable our object.
Let's go back into the code and make that change.
Here we are.
Let's just add a new yield statement.
We're not going to yield return null though.
We'll yield return new.
Wait until we're just going to wait and we're going to add a lambda statement here.
So we'll wait until shot started is true.
And then we'll generate the shot started boolean value.
And let's go find it real quick.
I'll hit F12.
It should be up here at the top.
I'm going to remove that private keyword because we don't need it.
And then in our on enable, let's just register for the onshoot event in that animation wrapper.
And then when that happens, we'll call shot or we'll set shot started to true.
So we'll say get component and children shoot animation wrapper and then we're going to register for the onshoot and when we register or when we get the onshoot we'll run this lambda statement that simply sets shot started equal to true.
So now whenever onshoot is fired from that animation event shot started will be true and we'll be able to continue past line 66.
Once we've got the shot started, we'll just enable our blaster shot or our B shot.
Um, what do I want to call this? Let's call this the be laser.
We'll say be laser set active to true.
We're going to need to create a be laser game object reference up here.
So, we'll copy that and go add a serialized field of game object named be laser.
Let's jump back into Unity and grab that be laser now.
Here we are.
Our B laser should be inside of that prefabs folder.
This blue laser lightning is the lightning or blast object for our B.
And we're just going to drop it right on the effect shoot.
So, I'm going to take it and just drop it right onto effect shoot.
It should be all zeroed out for its position and the scale and everything should be at one.
Now, if I press play, I'm going to see this thing just constantly blasting.
Let's just go check it out, though.
Make sure that it's moving around with our B and just constantly shooting.
Yeah, that's exactly what I expect.
And now let's go back into the code and turn it off by default.
Here we are.
We'll copy B laser onto the clipboard.
And inside the beginning of start movement, I'm just going to set active to false.
So our B laser is not playing.
Now our B laser is getting turned on down below, but it's not turning back off.
And we're going to need to make sure that it turns off as well.
And since we already have a shot reload, why don't we use that? We can register for the reload event on that animation wrapper.
And then when it's the shot is finished, we can just use that as the reload.
And then turn our be laser active to false.
So to do that, first I'll just copy lines 68 and 69.
I'll just hit select them both and hit control D.
Click right here, hit enter two times, get a little bit of space.
And let's say we'll replace shot started with shot finished.
And then we'll set active on the be laser to false.
And then we'll go up to where we register for shot started right here on line 39.
And we don't necessarily want to get this component twice.
So we'll take the get component part and we'll just turn that into its own line.
So let's call this wrapper equals get component in children shoot animation wrapper.
Then we'll say wrapper.shoot plus equals.
And you get it right here.
The shot started equals two.
Oh, I called this wrapped instead of wrapper.
And then we'll duplicate it and have an on reload.
And that's going to say shot finished equals true.
That is what I named my variable.
Oh, I haven't generated the variable for shot finished.
So we'll copy that.
I'm going to go up to shot started, duplicate, and paste.
So now we have a shot finished that gets set on reload and a shot or shot started that gets set on shoot.
The one last thing that we're going to need to do though is deal with this looping because shot started is getting set and shot finished is getting set, but they never get set back to false.
So after we've done the weight, we also need to just set these variables or these booleans back to false so that they'll be ready for our next use or the next time we loop through here.
So say underscore shot started equals false and underscore shot finished.
And it's already autocompleting.
Let's hit control Krl D to fix up the formatting.
Save, do a build, and go test it out.
We'll have to make sure we assign the be laser before pressing play.
But once it's done, we should see something like this.
Here comes our B.
Going to fly on in.
Stop.
Load up.
Blast.
And stop.
And look at our blast is firing again.
Ah, that's because we never set up the reload animation event.
So, let's do that.
Now, the final thing we're going to need to do is go to our B.
I'm going to select the B part with the animator.
Go to our animation window and let's go find that attack B blast.
We have the animation event right here for shoot, but I forgot to tell us to add the animation event for reload.
So, right near the end, not all the way at the end, about one or two frames before, we're going to hit the plus on animation event and add a new animation.
You can see that little tiny blue sliver there on the animation event.
We'll choose reload.
We'll save.
Press play.
And now everything should work.
And here we go.
The bee is flying down.
Let's let him shoot.
And it's looking good so far.
There we go.
And it goes away.
We still got two little things to adjust on this, but we'll do those in the next section.
For now, let's stop playing, go into plastic, and add our commit notes that the B moves and blasts properly.
I guess it just blasts properly, but we'll put that in there.
All right, let's have another challenge.
It's time to add damage to our B.
And I want to see if you can do this without adding any code at all.
Let's watch our B.
Bam.
blast my player and try to jump.
You can see that every time that I get hit with one of his laser shots, I'm going to take some damage and go flying.
So, go ahead and pause.
See if you can figure out how to do this yourself.
And if not, go ahead and continue on.
Or either way, continue on and I'll show you the solution.
Bam.
I'm dead.
All right, let's go take a look at the solution.
So, what I've done here to make this happen is actually very simple.
So, if you go expand out your bullet laser lightning and go look at the different objects underneath it, you'll see there are a couple different sprites here that represent different sizes of those glows.
I just want the damage to be on this inside glow and I want it to just kind of match with that.
I don't need it to be on the outside glow or anywhere in between.
So, all I've done is add a polygon collider and then our damage player script.
With that alone, we should be able to now, well, we actually not just should be able to, but you can see that we're able to damage our players and cause them to go flying back.
Now, if you wanted to do something special with our damage so that they don't go just launching up in the air, maybe you want to do some other type of check, then you could just replace the damage player script with something that behaves slightly different.
Perhaps one that damages and stuns a player or even add an option to stun a player instead of moving them so that maybe they stand still can't take damage for a while or something like that.
For now though, let's just stop playing.
Well, I've already stopped playing.
Go in and commit our laser prefab.
So, say updated B laser prefab to deal damage.
And we'll check that in.
We're going to give our bee one more special attack.
But before we do that, we're going to fix up the death and hit animation so that our bee can be hit multiple times, only in certain states, take damage, and then play an actual death animation.
And then we'll crank up the health and add in that extra attack.
Let's go to the bee's animator controller, double click it, and open it up.
And the first thing I'm going to do is remove my transition from any state to be blast.
Let's make a transition from idle into the be blast and on that transition have it have our condition of fire.
And the reason for that is that we're going to add another transition from any state into dead.
And we don't want to go into be blast if we're already dead.
So we've got a transition into our beast there.
Let's add in our hurt animation next.
So we'll take our hurt animation and just drag it down below idle and move.
I'm gonna make a transition into hurt from idle and from move and then make a transition out of hurt back into idle.
We're gonna need to make a trigger here.
So, we'll add a plus or hit plus and add a trigger.
And let's just call this hit.
This will be the trigger that will fire off in our code whenever our B is hit.
We'll have that trigger be the condition for the transition from idle to hurt.
So, hit plus and go find our hit.
And then the same from move to hurt.
So go find it and hit plus and choose hit.
Now if we go into our code, we can hook up our hit trigger and watch the hit animation play.
Let's make sure that works before we add in our death.
So we'll go into our B encounter.
And right down in our take damage method, we'll tell it to play our hit animation.
And so I'll say else B animator sett trigger hit.
Oops.
Let's get the semicolon in there.
Do a quick build and test it out.
We're back in Unity.
And before we hit play, I'm going to crank up the health from 5 to 50 so I can shoot this guy a whole bunch of times.
Let's press play and try it.
All right, here we are.
I've selected the bee and moved the animator window down below so you can see what's going on.
Let's watch him do some animation.
Goes idle and then does his attack.
Oh, I just got hit by some lightning and lightning again.
Now he's going to move.
I'm going to shoot him a couple times and he does a transition.
Well, look like he's trying to do a transition.
Let's see.
He's going to do another shoot.
Let's jump up and blast him a couple more times.
So, we shoot him and he does do the transition, but look what's happening with the animations.
So now he's got that hit trigger.
He's going to go into idle, go into move, and then play hurt.
So he's actually waiting quite a while to make those transitions.
Now I don't want him to go from be blast into hurt because I don't want to be able to interrupt his blast and have it go into a hurt animation, but I do want the transition from idle and move to be instantaneous.
So let's select both of those transitions and uncheck the has exit time so that the transition will happen immediately.
Again, it still won't happen if we're in the attack state, but it'll happen immediately.
Other than that, we're now getting an error, and that console error that we saw a moment ago is the cause of this.
We've got an animation event that is not running anything.
And this happens a lot when you grab animations from other people.
So, it's important to know how to fix this.
All we need to do is go to our animator or our animation window.
I'm going to select this B.
Go find that new animation that we just hooked up because that's most likely the culprit.
It's the hurt animation.
And look right here, there's an animation event that has no function on it.
We don't need to hook this up to anything.
If I drag it over, you'll see that it's for this point when the B is kind of uh halfway through the hit.
I don't know what I would use that for necessarily.
So, I'm just going to delete it.
Go back into the console.
Let's stop playing and play one more time.
And now I should be able to run over there and have our animations look proper.
There we go.
would run, jump, blast this bee in a moment once he starts gets on screen.
There we go.
Shoot him a couple times.
See, he's taking hits.
Taking hit.
Taking hit.
Taking hit.
Taking hit.
Taking hit.
Keeps taking hits.
And there we go.
He's dead without ever actually hitting me.
Now, how is this happening? Let's take a look at our animator one more time.
If we scroll down and look at the transitions here, our idle to attack animation requires the fire condition.
Our idle to hurt animation requires the hit condition.
So let's see what happens when both of those conditions are set to true.
So I've checked them both and we'll just skip through one frame.
Here you see I've clicked and the hit trigger is off and we've started a transition into hurt B.
So why is that happening? Why is this transition happening? instead of this one.
There actually two causes to that.
The first is very simple that our has exit time is checked here.
So our transition into attack can't happen until after our idle has finished.
Which means that our hit that doesn't have a has exit time can happen immediately and we'll get priority.
So first we can just uncheck has exit time.
Let's check both of these again though because that may not fix our problem.
Let's hit play and click them both.
If I can click them both fast enough.
wait for after the attack and see what happens if he attacks again.
Oh, he went into an attack again.
Now, there is a scenario where he may not attack again.
Let's take a look at the animations again.
If we select the idle state, you can see here we've got a bunch of transitions and this shows which transitions take priority.
If I move the hurt B up above the attack blast and then check both of these, watch what happens.
Now, it goes into hurt B first instead of going into fire.
and we get that big long weight.
So, we also need to make sure that our transitions are ordered properly.
We'll select the idle estate again and just make sure that hurt is probably um well, actually, I think we want attack all the way up at the top and then hurt and then move.
That looks like a good set of transitions.
All right, now that we've got that set up, let's go back and try it one more time.
We'll press play.
Remember, we've moved that has exit time from the transition out of attack and we've rearranged these transitions a little bit.
We'll go shoot this bee.
Let's go blast him.
Can't hit him when he's blasting, which is exactly what I expect.
Let's blast him again while he's moving.
Oh, did I get him? I am terrible at hitting this bee.
There we go.
Got a couple hits in.
And now the shots start to go through him once the animation begins.
And he's firing back.
All right, that's looking good.
Before we go any further, let's save our scene and commit our changes.
Here we've added the be hurt animation and well, I just added be hurt animation and check in.
Now that our bee can take hits and show those animations properly, let's finish up as death and create an actual death sequence.
We've got our animator tab right here, and we need to add in the death animation.
First, let's go to the project view and take the dead bee animation and drag it right up here to the top right corner.
I want to be able to transition into death from any one of these three states.
Either attack, idle, or move.
If we're in hurt, we'll go back into idle and then straight into to dead as well.
So, let's do transitions by right-clicking and hitting make transition and dragging one from each of these three points up to dead.
Next, we're going to add a parameter.
And we're going to add a dead boolean here.
You can see I've already added it.
I'm going to delete it and read it again.
You can just name it dead.
And the reason that I want this to be a boolean is pretty simple.
instead of a trigger.
And that's I want to be able to transition back from dead into idle and bring my be back to life if I want to do some testing or I want to reuse this character.
So to do that, I'm going to rightclick and make another transition back into our idol from dead.
But first, I need to well actually after I need to go in and add in all of my conditions.
Let's start with the exit out of dead.
We'll go select it and choose the condition that dead is false.
For the transitions into dead, we'll select them and choose the condition that dead is true.
But we're also going to uncheck has exit time because I don't want the full idle animation to play or the move or the attack to finish.
I want dead to play automatically if we die.
Let's go to the next transition from move to dead.
Add in our condition of dead equals true and uncheck has exit time.
And the same from our attack.
We'll go choose dead equals true and uncheck has exit time.
So now we should be able to set the dead state on our B and have him switch into that animation.
To hook that up, we'll go back to our take damage method and let's just replace the set active with a B animator.
Let's just replace that B animator set bool.
And we're going to set the dead boolean to true.
We'll save.
And then let's jump back into Unity and go try it out.
I'm going to make sure the bee's health is down at five.
so that he's nice and easy to kill.
Go blast him a few times and then let's see what happens.
Go shoot him.
Here we go.
All the way down here.
And he's dead.
He plays his death.
And uh it looks like it it actually worked.
So, he died, but he's not doing exactly what I want him to do.
I also want him to fall down to the ground.
And I want all of this lightning to turn off.
I want to make sure that he's not moving around.
He's not moving because of his rigid body, but I want to make sure that the lightning and everything, all of my scripts are turned off and that he drops down.
So, let's go into our B.
First things first, I want to give him a rigid body so that he could drop down.
So, we're going to go to the base part, the part that has our animator.
We're going to give him a rigid body 2D.
I'm going to set the body type to kinematic so that he doesn't fall automatically on his own.
And I'm going to freeze the rotation and position so that he can just drop down.
Oh, let's just freeze the rotation.
Actually, I don't think I want to freeze my position.
I'm just going to freeze the Z rotation so he doesn't spin around when he drops.
He's not going to drop yet, though.
Let's save and go into our B encounter and hook that up.
So, we'll go to our B encounter script and we're going to expand out this bit of code here.
We're going to add in some braces and instead of just setting our character to dead, we're going to stop our co- routines.
So, we'll do stop all co- routines.
That's going to stop the two co- routines that are running on our B encounter.
If we go up here in our on enable, right now we're turning them on.
We get to move these to the end of our intro, but for now we've still got them in on enable.
And this will turn off both of these.
So our movement code will stop.
Stop moving our character around and blasting lasers.
We definitely don't want that happening.
And our lightning will stop as well.
That's kind of the behavior I want.
The other thing I want to do though is stop our rigid body.
So we're going to say underscoreb rigid body.
I say stop.
I really activate our rigid body.
And we're going to want to set its body type.
We don't have a reference to it though.
So let's copy this.
Go to the B animator by Ctrl + left clicking.
Duplicate it with Ctrl + D.
Ctrl +V to double click.
Crl + V to paste and get our B rigid body.
And then make this a rigid body 2D.
We'll go back down to our code on take damage.
This is line 157 for me right now.
And we'll set the body type equal to and we want this to be dynamic so that it will fall on its own.
Now we can save.
Let's jump back into Unity and try it out.
Before I press play, I've got to make sure that I assign my rigid body or we're gonna end up with a bunch of errors.
And I'm going to turn this health down to five again before I play.
So that way I don't have to keep remembering to do it.
Let's now jump in there.
I should be able to blast this guy and watch him hopefully fall right down into the water.
Let's see.
There we go.
He falls down and now he's just bouncing in the water.
That is exactly what I wanted.
There's an issue though.
Take a look at this.
I can stand on him and I can't really walk through him.
What if he is in the way? What if he lands somewhere important? Let's take a look at our B real quick.
Let's just drag his position over here.
What if he lands like over there? Well, then I'm kind of stuck and I can land on him and bounce around him, but I can't move.
So, I can't walk because he's not counting as grounded and I'm slipping off of him.
And really, I think I'd like to be able to walk through him.
And I think we'll deal with that in the next section cuz that's going to be a slightly more complex thing.
Let's go into plastic for now.
Make sure that we've saved and say that our bee falls to his death and check that in.
Now, let's take a look at our dead bee and the collisions and see what we need to address.
Still, if I run over here, you'll see that I still can't go through the bee.
I can land on it and I can't really walk because I don't think I'm getting counted as grounded.
If we go check our character, let's go find the player, we should see that I'm guessing is touching right wall is true, but oh, is grounded is true.
Good.
So, I can keep jumping it at the very least.
But I can't move left and right because it thinks I'm on a wall.
I can't walk through it either because it thinks I'm on a wall.
And I can even blast it and knock it over to the side because it's not locked in position.
So, what I want to do now is make it so that my bee doesn't get interacted with by the player or the player's bullets, but I still want it to be able to fall to the ground and do all of the the typical physics stuff so that it's there, but it's not interacting with the players just with the world geometry and I can walk through it.
And to do that, we're going to need to add a new layer.
What we'll do is set all of our B here to be on a layer that's maybe for our dead objects that doesn't interact with our player.
Let's start by adding a new layer.
We're going to go to the layer dropdown and hit add layer.
It doesn't matter what object you select because that just opens up the tags and layers inspector.
Doesn't actually change the layer of the object we're on.
We're going to add a dead layer here.
And then we're going to go into our code and set the layer to be dead whenever our character dies.
Before we do that though, let's make it actually do something useful, having it on a separate layer.
And to do that, we're going to go to window or edit, not window, and then project settings.
and we're going to find our 2D physics collision matrix.
If you haven't found it yet, it's find physics 2D, not regular physics.
Go off of general settings over to layer collision matrix.
And we want to uncheck dead and player.
Ah, looks like I've already unchecked it.
Just make sure that it is unchecked so that dead things don't interact with players, just like player bullets don't interact with players.
Remember, the player bullets are on that player layer.
Now, let's set our character colliders to be on that dead layer.
To do that, we'll go into our take damage method and we're going to just find all of the colliders.
So, we'll say for each var collider in get components in children.
Let's find the plural one.
And we're going to do collider 2D.
We don't care which type of collider it is.
And really, we're not worried about the performance characteristics of this because it's only happening once when the thing dies.
It's not going to be enough of a hit to make any difference at all.
So once we've got each collider, we'll just tell the collider to have its game objects layer be set to layer mask dot and we want to use name to layer, which is going to take a name and then give us back a layer mask.
So it's not actually the layer number, but it's the mask or the bit mask for that specific position.
And we're going to give it the layer name dead.
We'll save that off and let's go back into Unity and see what this does.
You might be a little bit surprised.
All right, we're back in.
We'll run over here.
Let's blast this bee.
Make him fall to his death.
And check it out.
So, here I still can't run through him.
But watch what happens if I jump.
I don't land on him either.
And now I'm stuck inside him and can't move left or right.
Let's get back on there one more time and see why that is.
So, if you look, when I'm standing inside, it still thinks that I'm touching walls on the left and right.
So, even though the collider is not colliding with my player, the code that's checking for wall touches is detecting a collision.
Let's go take a look at that code one more time.
So, we're going to find the part where we're touching and that's checking for wall right here.
If we go up the call stack a little bit, let's just go find it again.
I was already there, but is touching right wall.
If we look for that, it's called or set by calling check for wall, which then goes through and does our raycast.
And it does a raycast against a layer.
And our layer is probably set, right? If we go back in here and we look at our layer mask, see that? Yeah, it shouldn't be interacting with player or dead.
So, what's the problem? Well, take a look at this code right here.
The issue is actually on line 117 or 117 to 121.
And what I want to do is present a small challenge.
See if you can figure out why this isn't working.
It's a relatively small problem.
It's a small solution and it's right here in the code.
It's just something that needs to be modified or added.
So, go ahead and track it down.
see if you can figure it out and then continue on and I'll show you the solution.
All right, I'll assume that you've either found the solution or just want to continue on.
The problem is that we're using a layer mask, but when we use a contact filter 2D, it has all of these use options that are boolean toggles like use layer mask, which is defaulted to false.
There's use triggers, use angles, and um use depth as well.
We're going to just enable use layer mask though.
Now, that also means that the other place where we're using a contact filter 2D, if it's using a layer mask, which it is, should probably also have use layer mask set as well.
So, we'll say use layer mask in both of those.
Do a save and a build.
And that was for our check grounding.
So, it's technically allowing us to ground on things that weren't in our layer mask.
Now, if we come back into Unity and kill this bee, let's give him a couple more shots.
I should be able to walk through him, jump through him, and everything else.
and even shoot blaster shots right through them.
That's exactly the behavior that I want.
Now I'm just ready for them to start floating in the water.
Let's go to plastic and commit our changes first.
Make sure I've saved my scene and so that the oh cuz there we go.
We got our B our tag manager and our physics settings and make sure that those are pulled in.
If you don't see those, go to file and do save project as well to make sure you force those.
and say B death now doesn't or let's say B switches to dead layer when dying.
I'll understand what that is and check it in.
Now, we're going to add the last piece of our boss battle.
We're going to set it up so that when the bee gets to about 50%, the entire ground floods and the player can no longer land on the water or land in the ground.
they land in the water and get kind of pushed around.
Let's start by just adjusting the environment.
The first thing that I want to do is take my ground that's right here and just kind of lower it.
Actually, let's lower the water first.
Let's select the water object here.
I'm going to move it down about 1 meter.
So, hold control and drag it down.
I'm going to take this one that's right at the beginning.
I think I'll go down about one so it's at 5.5.
And then I'm going to hit T and make it wider.
So, hold control and drag all the way over so that it's the same width all the way to the edge of this.
What we're going to do is have this one water object come up and kind of take over the ground.
Now, we need to expand out the child as well.
So, I'll just click on it and select it, holding control, drag it over, and get it into position.
It's a lot easier to do it this way than typing in the numbers there.
And then I'm going to make my water a child of the B encounter.
So, I'll drag it down here.
Since it's part of this encounter, I'm going to make it a child of that encounter.
Next thing I want to do is drag my ground down.
I've got this piece of ground here, and I want to kind of give the player a little bit of an indicator that something's going to happen here.
So, we're going to move this piece down.
Oh, let's hit W and just drag it down until maybe about just the top is there.
So, is this about a negative 5.25? So, I think we went down about 75.
I think that that's probably a good height except now the grass in the background doesn't line up anymore.
So, let's just grab it.
And we've got a couple options.
I could put in a sprite here that kind of fills and matches that color.
But, I think I might just grab this background and move it down one on the Y instead.
So, just do like a negative one on the Y and get it down there so that it's below.
And then if I have other things at this kind of level, they'll be fine as well.
Let's now remove that second water.
So, I've got a water that was over here to the right.
I don't need that anymore because the water now extends to it.
And I can see here that I actually need to move this background down just about maybe 0.25 more.
So let's go to one negative 1.25.
It's just right below that waterline.
Once I've got this lined up and had a solid position for it though, I probably wouldn't drag it down and we just add some green sprites.
But for now, I think that it's fine.
It doesn't really lose anything there.
We're still getting a good background view and everything looks right.
The top here, however, I don't like.
Right now, we have this big blue, this uh I for it was a corn something blue.
Whatever it is, it's a blue that doesn't match our sky.
So, let's go fix that real quick before we continue on.
We're going to go find the player, not the player, the camera system.
Go find our multiplayer camera setup and go find the actual camera here.
And then underneath the camera, we can find the environment section.
Remember, we've got a URP camera, so it's slightly different than the built-in one.
And we got to find environment and change the background type from skybox to solid color.
Use the color picker and just go pick that color.
And tada.
Now we've got our nice, beautiful sky.
All right, let's get back to our water.
So here's our new water leveling game.
It's a nice drop down from the cliff.
And then we've got this little ledge that we can walk along.
And now the goal here is going to be that when the bee gets to 50% health, this water rises up and starts flowing and pushing the player in one direction or the other.
or you could even make it alternate directions.
Since I want this to start when the bee gets to 50% health, let's begin in the take damage method.
We'll do a check after we've taken some damage to see if our health is at exactly the 50% mark.
So we'll say if underscorehealth is equal to and now we need to figure out half of our max health.
And right now we don't have a max health.
If we look at our health, that's our only field.
So this is the one that gets serialized and it's the one that we use as our temporary variable.
This is a temporary thing so we could see it and adjust it.
Let's make a change now so that we have a maximum health and a current health instead.
So the first thing we'll do is rename health to be current health.
Find that it's a lot easier to understand which one it is if you put the word current there instead of just having a health and a max health.
Then we'll delete that public keyword.
I'm going to copy this line.
Just copy and then paste it right up here.
We'll add a serialized field attribute and then replace this with max instead of current.
So it's a max health and I'm going to set it to 50.
Now we don't want to necessarily set the current health right here.
I want to make sure that's being set somewhere else.
So I'm going to just remove that initialization and then do it down here in on enable when our character starts.
So say current health is equal to our max health.
Now we can go back to our take damage and we can finish that check.
So if current health is equal to and here we'll do our max health divided by two.
So if we're at half health then we want to start this flooding.
To start the flooding let's do a co- routine.
We'll do start co- routine and we are going to call this maybe start flood but then we're going to need to stop a flood too.
So let's maybe call this toggle flood and then pass in a true.
So we're going to turn the flood on and then we'll be able to turn the flood off as well.
Let's generate a method for toggle flood.
Hit F12 to go to it.
And then change that return type to be an ie numerator.
We're going to need a flag here that's better than in v.
Let's say um enable flood instead of v for our variable name.
For our initial implementation, let's just move the object or the water up or down one meter depending on if we've enabled it.
If we enable it, we'll move it up a meter.
If we've disabled, we'll move it down.
And that'll be our our starting version of this.
So we'll say um target let's say var target water y equals and if we're enabling the flood we want to do our current y + one or plus vector 2.up.
And then if we were doing it down we'd want to do minus one.
So we'll say it's equal to our if we're enabling flood it's going to be our transform.position.y y y y + one.
Otherwise, it'll be a transform.position.y minus one.
There we go.
And then we'll just move our transform position to that.
So, we'll say our oh, we need not our transform though.
We need our waters transform.
So, let's get a water reference.
We'll add a public water_water.
And then we'll replace transform with water.transform.position.
There we go.
So this is going to give us our target y position for this new water.
Then we'll set the water's position to that.
So say water.transform.position equals a new vector 3.
And we'll just give it our current position.
So water dot or no, we need to give it our yeah water.transform.position.x the wrong words there.
And then our target Y.
That's what we want.
And then our water transform position Z.
All right.
So that should instantly move our object up, but we're in a co- routine and we're not waiting for anything.
Eventually, we're going to want this to go over time so that it floods up kind of slowly.
So let's just add a quick yield return null.
Go assign our water.
Make sure that works.
And then we'll continue on.
All right, we're back in Unity.
So we'll assign that water transform to the water.
It's actually a water object.
And then save.
And if I press play, I'm going to have to go blast this guy 25 times to get his health down.
So, let's add a little shortcut down here at the bottom of our B encounter.
Let's add a method that sets our character or our be to half health.
I'm going to call this method half health.
We'll call void half health.
And then in this, we'll set our character's health.
So, we'll say underscore current health equals max health divided by two.
And then we'll just add one.
So, current health plus+.
I could also say it equals max health divided by two plus one, but this is a little bit easier for me to read.
We'll add one and then we'll tell it to take damage, tack damage, take damage, so that it'll actually call the take damage method and go down to that exact amount of health.
Now, I want a context menu to be able to call this.
So, I'll say context menu and put in name of and put our half health right here.
Now, I also kind of want to be able to um kill this thing.
So, let's just copy this method and add a method for killing them as well.
So, say kill and we'll change the method name here to be kill as well.
And we'll set the current health to one and then tell it to take damage.
And then finally, let's just do like a full health restore.
So, let's say uh full health and I'll paste that in.
And here we'll just set the current health to max health and do absolutely nothing.
All right.
Now, we'll go back into Unity.
All right.
And here's our water.
We're in it.
Let's move it up by moving that B.
We'll say half health.
And you see the water pops up and gives us this this nice risen water that's over the ground.
All right, that's close to what I want.
Let's make sure that we can now drop it down.
So, we'll say kill.
And see that the bee dies, but it didn't actually kill.
Um, it didn't it didn't get rid of the water and it's still acting up a little bit.
So, let's go adjust that now.
Let's go back into our B encounter and then when we take damage here, if our current health is less than zero, let's call the co- routine to turn the flood off.
So, we'll say start co-outine toggle flood false.
Now, I don't want to do this right here because if I do this on line 161, look what's going to happen.
line 162 is going to stop that co- routine.
So, what I actually want to do is cut this, move it down one line here, and then remove that.
So, we're going to stop all of the existing co- routines.
Those are the ones for moving and shooting.
And then we're going to kick off the flood disabling co-outine when our bee dies.
Let's save, go back in, and test it out.
All right, here's our bee.
Let's put it to half health.
We see the water goes up.
Be should still be kind of flying around over here.
And if I right click and kill the bee, he should fall to his death and the water drops back down.
All right, this is looking good.
I'm going to go into plastic now.
Make sure that I've saved my scene and commit real quick.
Added be water that instantly raises and lowers.
And check that in.
Now that our water works, it's time to smooth it out.
We're going to make it so that our toggle flood method will slowly rise or lower the water depending on if the flood is being enabled or disabled.
We already have a co- routine here.
So, we're just going to need to add in a while loop and smooth out this movement.
So, instead of just snapping to the new position, we'll move over time.
This should be a relatively easy problem to solve, but since we're going to go in two directions, it's going to get slightly more complicated.
The first thing that I want to do is just cache this initial position here.
the position that we're getting for the Y because I want to be able to lurp from that position to my target position.
And if I don't cache it and I keep moving my Y position, then that value is going to change and I won't be able to do my lurp properly.
So, I'm going to cut this and call this initial water Y.
I'll add a variable up above, a float initial water Y.
Well, not W equals transform.position.y.
I'm going to copy that and replace the other instance where I'm grabbing that y position.
And then I'm going to change this to be a float instead of a var so that the names and the parameter lengths match up.
Actually, I don't need an underscore here.
I don't know why I added one.
So, I'm going to remove that.
It's just out of habit.
I automatically started typing an underscore.
So, now I've got my initial Y and my target Y.
And what I want to do is loop over them or loop for a certain amount of time and move from that initial Y to the target.
So, we're going to add a couple of fields.
First, we'll add a float for our duration for how long we want it to take to loop.
I'm going to make that 1 second.
So, just do a 1 f.
And then, we'll add a float for our elapsed time.
So, call this elapsed elap sed.
There we go.
Time.
And we'll set that to zero.
We'll add a while loop.
Look at that.
It's going to automatically autocomplete that for me.
And while elapse time is less than the duration, we want to well of course increment the elapsed time.
And then we want to move our object towards that new y position.
So let's take this vector 3 part of line 186.
I'm going to hit shift and end to go to the end of the line.
C to copy it.
And up here on line 84, I'm going to say var destination equals and paste.
So this is going to give us our destination for where we want to go.
Now, I don't want to necessarily go directly to that target Y.
So, I need to figure out my Y value for this current frame.
We're going to start it off at the initial Y and then move towards that target Y.
So, let's create another float.
We'll say float Y equals.
And here we're going to use the lurp method.
So, we use math f.lurp, which is going to interpolate between our start value and our ending value.
We'll give it the starting Y, our initial water Y, and then we'll give it our target water Y.
So this is the initial y value and the target or the ending y-value.
So imagine this is going to be if we jump into unity.
We've got this y at 5.5.
So it's going to go it's going to go from that to like a negative uh 4.5.
So it's going to raise up.
So let's go back into the code.
And then here we need to give it our elapsed.
But I don't want to use elapsed time.
So, if I use just that elapse time like it recommended, then what we're going to end up with is we won't be able to do durations greater than one because it's going to always do it at one and it's going to ignore our duration completely.
So, what we need to do instead is figure out a progress.
So, we'll add another variable up above float progress and it's going to be equal to our elapse time divided by our duration.
And then we'll put in our progress right here.
Finally, we'll set our destination's Y value to that Y.
Well, actually, we'll add a semicolon first.
Then, we'll set our destination's Y value to that new Y that we've calculated and then move our object to that destination.
So, we'll say water.transform.position.
Let's just copy that.
Paste equals destination.
Now, of course, you could shorten this down into less lines, but I feel like having it split out makes it a little bit easier to see what's going on.
The last thing I'm going to do here is just delete line 189.
and it snaps it to the target position.
I don't necessarily need that, so I'm just going to take it out.
Although, you could leave it in if you want to make sure that um it ends up at that position at the end, but it's going to end up at that position at the end either way.
So, I don't necessarily need it.
I'll just delete it because it's extra code that's not really going to make a difference.
All right.
We also want to move this water because our water is a public field that's down here at the bottom, not a serialized field.
So, I'm going to cut it.
Delete that extra space.
Go up to the top and let's add in a serialized field for our water.
So, add water.
We'll add the serialized field attribute.
Save.
And do a quick build.
Oh, before I can build, I've got to add a semicolon to the end of that line.
Let's do one more build.
And that should be a successful one.
Build succeeded.
And we'll go back to Unity.
So, now we'll play and watch what happens when we set it to half health.
Well, it instantly popped back up.
If I set it to kill, it instantly pops back down.
So, let's take a look at the code one more time and see if we can figure out what's going on.
What I want you to do now is just evaluate this code.
Look at the toggle flood and see if you can figure out where the issue is.
Why is it not smoothly moving up? Why is it snapping into position? Go ahead and evaluate this code for a minute or two or however long it takes and then continue along and we'll dive into the solution.
All right, hopefully you found the problem already.
It's actually a really simple one.
We're in this while loop and we're running through elaps modifying our elapsed code or elapse time, incrementing it by timed delta time, continuing on the progress, moving our y up, figuring out the destination, and then moving and then we continue on and do the same thing again and again and again.
And once we're done, we wait for a frame.
See the problem now? Well, the problem is pretty simple.
We just need to wait for a frame after each movement.
We're doing all of this movement in one frame in one go and then it's just snapping our object up.
We've got to move that yield return null right here so that we can let a frame complete and pass before we just run through this loop.
This happens all the time in co- routines with while loops.
You forget that yield and usually you'll end up with a crash or something else if it goes on indefinitely.
But luckily this one has a time limit of 1 second so it kind of ends quickly and can't crash it for us.
All right.
Now, with that in, we should be able to jump back into Unity and see our water move smoothly.
All right, here's our water.
Let's go jump in it.
In fact, let's go stand on the platform here and set our character to half health or our B to half health.
And okay, now I'm floating and see that the ground is still a little bit high here.
I'm still kind of able to touch it.
And I don't really want to move it.
Instead, I think that the best solution here in this case, let's go look at it in the scene view here.
We've got this ground piece that's just kind of right down here below.
It's not that one.
Let's see if I can find it.
We'll go select the ground piece real quick and then show the solution.
So, we got to go find it in the environment here.
Let's just turn off the water.
Easy way to do this.
Go select that object.
And