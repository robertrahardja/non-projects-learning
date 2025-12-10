indows on a super high-end system doesn't make any difference.
You're not even going to be able to tell on here.
Soon as I go to a mobile device though, you're going to notice a huge, huge spike.
So, we'll talk about that in a moment.
For now though, we're going to go into plastic and commit our initial changes that the blaster shots selfdestruct and clean up.
And we'll check that in.
Now, we're going to dive into the solution to our despawning or spawning and despawning objects problem.
the problem with memory where we end up with either too much memory allocated or we end up with memory fragmentation and our garbage collector has to reallocate and clear up and move objects around again.
On a high-end desktop system, you're going to have a hard time seeing that until you hit a really hard or high limit.
And on a mobile device, you're going to see it almost instantly.
You're going to see the freezes and hitches when the garbage collector is trying to fix up and reallocate or rearrange objects in memory so that it can create new objects.
Now, this is a very common problem in game development and the very common solution to this is to create a pool or a reusable group of objects.
In this case, it'll be a reusable group of blaster shots.
So, we'll create blaster shots, have them pulled together, and then we'll request one of these blaster shots from the pool, launch it off, and then whenever it hits the end target, we'll just disable it and send it back to the pool to be reused for the next time that we need a shot.
We'll end up with quite a few objects in our pool, but that's okay.
We can have it all be totally dynamic.
And to create a pool, we don't need to do very much because since it's such a common problem, Unity's built a pooling system right into the editor.
You'll probably find a lot of videos on how to create pools, how to do all of this on your own, but if you just use the latest versions of Unity, you can use the object pool that's built right in.
And that's what we're going to use.
If you look at the Unity documentation, you can see the object pool is a way to optimize projects to it says lower the burden of CPU and when you have to rapidly create and destroy new objects.
And it says it's a good practice and design pattern.
Again, such a common problem that Unity released a solution for it.
And here you can see some examples that they have.
This is a script for a particle system that will make it automatically return itself to a pool.
This is I'm not sure which one this is.
This is getting a pulled item and showing quite a few of the different methods.
Now, we're going to go through writing this code ourself and setting up a pool for our blaster so that it can shoot out objects and then reuse those objects.
And then we'll figure out how to do them across players as well.
To make our blasters use pooling, we're going to start by opening up the blaster script.
So, select the player and open up the blaster script.
And up at the top in our awake, we're going to initialize and create a new object pool of type blaster shot.
So we're going to say underscore blaster or pool, not blaster pool equals new object pool of type.
So we do the open braces right there or the less than symbol.
And we're going to put in blaster shot.
Do an open close parenthesis.
And that will give us an error saying, "Hey, you need to pass in some parameters.
Specifically, you need to pass in a method that'll get called when our object is created or a method that will create and return back a new object." So, I'm going to create a new method here that we'll just type in the method name of.
And I'll call this um let's say add new blaster shot to pool.
A nice long name.
I'll hit alt enter and generate a method for it.
That should give me a method that returns back a blaster shot and just throws an exception.
Now, to spawn a new blaster shot, we're just going to instantiate one.
So, I'll just put that right here on line 25.
Instantiate a blaster shot prefab.
And I could just return that right here.
So, now I've got the definition or the correct call to create an object pool.
And I need to actually create the field for it.
So, I'll select the pool, hit alt enter, and generate a field right up here.
I'm going to double click the private keyword and hit enter just to get rid of it, and add a little bit of spacing.
So, now I have a pool that I can get blaster shots from.
And when it needs to create a new blaster shot, whenever it runs out of blaster shots, it's going to call this add new blaster shot to pool method, which will just return it a new blaster shot that it can add to the pool.
So, what do I need next? Well, I need to use this pool.
So we'll copy the pool and find the spots where we instantiated before.
So on line 31 when we called instantiate, I'm going to instead call pool.get.
I'll add a semicolon and I'm just going to comment out the rest of that line for now.
We're going to take another look at it in just a moment.
We're going to do the same thing here on line 40 where we're doing our super fast rapid fire.
In fact, I'll just select over here with shift and click, copy, and then paste right down here.
So in both cases, we'll now get the blaster shot from the pool instead of instantiating it.
And you might notice that this also means that we're no longer putting this blaster shot at the correct position because now when we instantiate it, we don't spawn it at a firepoint position and we're not spawning it multiple times.
So we can't pass in that firepoint position when we want to spawn it again.
So instead, let's give it the initial position to launch from in the launch method.
To do that, I'm going to copy firepoint.position_firepoint.position right onto my clipboard with C.
And in the launch call, I'm going to add a comma after direction and paste with alt enter or shift controlv, not alt enter.
And now I'm going to hit alt enter though and get my popup that's going to allow me to add a parameter to the launch method.
You can see here it wants to change it from being a method that takes a vector 2 named direction to one that takes a direction and a position.
If I hit enter, it's automatically generated it.
And now my launch method should look right.
I can't see it yet though.
Let's hit control and click on launch.
It'll take me right into the method.
Oh, it didn't actually do my change.
Let's go back and do that again.
Alt enter and we'll generate that method.
Oh, that's strange.
It was supposed to have refactored my method and changed it.
Let's go back and redo that real quick.
I want to go back into my blaster shot and we'll go back over to the parameter here.
Alt enter.
And we want to Oh, yeah.
It's not allowing me to generate my method this time.
That's fine.
I or it's not allowing me to refactor and automatically update my method.
That's okay, though.
I'll just go to the launch method.
We'll click on it.
Control-click.
And we'll type it in right here.
So I'll say comma vector 2 and we'll call this uh position.
Then we'll set our transform.position equal to position.
And it's important that when you're doing these autogenerates and you're going through and you know trying to hit the hotkeys to make things happen.
Sometimes it just doesn't happen and you've got to go in and do it manually.
You can't get stuck and hung up on the fact that something's not working in an autocomplete or something like that.
It'll really slow you down and giant waste of time.
Most of the time the tools just work, but every now and then something doesn't happen right and you've just got to work right past it.
Just go in and do it manually.
So here we need to get this other parameter into our second call into launch for the rapid fire.
So I'm going to copy what we've got selected right there on 32 and paste it in.
Now, if we just run with this, we will get shots launching, but they're not going to be reused because we're not actually sending anything back into the pool.
So, we need to make sure that instead of destroying our objects, we actually return them to the pool as well.
Let's go into our blaster shot script.
I'm going to hold control and leftclick on the blaster shot.
We destroy our blaster shot with this destroy call right here in awake and the destroy call on line 43 and on collision enter.
Instead of doing that, let's tell our object to self-destruct.
And when it self-destructs, it's just going to disable itself and return itself to the pool.
So right here in our awake method, I'm going to call an invoke and we'll call in method named self-destruct.
So I'll put name of selfdestruct.
That's going to make it so I don't have to use a string for the name.
And when I can now I can now generate the method name right here and change the return type to be void.
Now I need to give it a delay.
I'm going to give it a delay of our max lifetime and add a semicolon.
So it'll self-destruct at whatever our max lifetime is.
At the max lifetime, I want it to disable itself.
So just say game object setactive to false and then return itself to its pool.
Now, it doesn't have a reference to the pool, so it doesn't know how to get back to the pool.
I'm just going to assume that I can figure that out, though, and say underscorepool.release, and we want to release this.
Now, release is the method that you call on an object pool to send an object back to it or say, hey, this object is now ready to be reused.
Go ahead and put me back in your pool and do whatever you're going to do.
Now, we're going to need to get a reference to this pool though.
And I can do that from our launcher.
So, if I go to the blaster right here, when we are creating our blaster shot, instead of just instantiating it and returning it, let's instantiate it, tell it what pool it came from, and then return it.
So, I'll replace this word return with varshot equals.
Then I'll say shot setpool, and we'll pass in our underscore pool, which we do have here.
Remember this is the blaster.
It has a pool already defined.
And then we'll generate a method for that with alt enter by clicking on set pool and hitting alt enter.
And then finally return the shot.
Now I'm going to go into set pool by hitting control and clicking on it.
And then in the set pool method, we'll just say underscore pool equals pool.
I'm going to replace internal with public just because that's what I like to do.
And then generate the field for our pool.
This should give us a field up at the top that's a private object pool of type blaster shot named pool that gets defined or assigned right down here.
I'm going to go up to the top or remove that private keyword here.
And then the final thing I need to do is call self-destruct when our object gets destroyed.
So I'm going to copy this self-destruct right here.
Go down to the part where on line now it's 51 where we destroy our object.
I'm going to replace that and the set active call with self-destruct.
And we're going to um I guess that's it.
We don't really have to do anything else.
Just call self-destruct.
The final thing that you're going to notice now though is that when we spawn objects, they're going to be initialized or enabled by default.
They'll launch off.
They'll fire off.
They'll get returned to the pool and disabled and not turned back on.
Let's go see that real quick and then fix that last issue.
So, we'll jump in.
We'll press play.
And we should expect to see a bunch of blaster shots fire off and then some weird intermittent behavior where we have blaster shots not actually visible anymore and then eventually get to the point where we may have no more shots ever showing.
Let's hit play.
So, here we go.
There go the shots and you can start to see that intermittent set of blasting.
And what's actually happening is that we're just getting these blaster shots back from the pool that are already used.
So these objects, they're never getting reenabled.
So let's go back into our pool.
Oh, we can actually see we're even getting another error here.
Let's go back into our blaster script and make one more change.
Now when we define our pool and instantiate it, we only passed in the add new blaster shot to pool method.
But this method or this in constructor actually takes multiple parameters.
Now let's go take a look at the object pool parameters.
So here's the documentation and you can see that it takes quite a few parameters.
There's a create function which is the first one which is used to create a new object.
So that's the one that's instantiating something for us.
Then there's the one the next method action on get.
This is a method that gets called whenever an object is taken from the pool.
So whenever we call get this will get called automatically and this is a great place to enable our object.
There's also one for onre to call when our object gets released and this could be a great place to disable the object.
In fact it even says that right here.
There's one for destroy.
There's some a couple others that we're not going to dive into like a max size and a default capacity is actually kind of interesting.
If you need to spawn a large number of objects and you know that you're going to need at least 100, you could maybe set this to 100 and not have the objects spawn over time.
This is useful for things where you have a good idea of the size of the pool off the start of the game.
Now, we're going to dive in and just take advantage of the action on get and the action on release.
We go back to the code and minimize that window and we're gonna add in two new parameters.
So I'm going to put a comma there and a new line.
And for the next next uh input parameter, the thing that we're going to call, I'm going to use a lambda statement instead of creating a method.
So I'll put a t here and then a lambda.
So t is going to be the the object that gets released or the object that gets um gotten actually because the first one is the action on get.
So when we get an object, we'll get back a blaster shot and that'll be assigned to t here and I'll say t.gameobject game object dot set active to true.
Now I'm going to add a comma and go to the next parameter which is our action on release.
And we'll do the same T and a lambda statement.
t.game object set active to false.
Add in my closing brace right there or closing parenthesis right there.
Let's add another line.
Save.
And then I'm going to go into that blaster shot real quick and remove those two calls or that call in the self-destruct that sets us to not active because we'll already be inactive.
We don't need that anymore.
Now we're back in Unity.
Let's shoot and see what happens.
So you can see my shots firing off and it doesn't look like there's any missing or stuttering.
All of my projectiles are actually reappearing.
But we are seeing an error down here in the console.
If you have your console window open, you might be noticing this.
And the problem is that our object is self-destructing even after it's already been returned to the pool.
So imagine we hit something.
Our object hits right there.
Let's just clear the log real quick.
We hit it.
Our object has been returned to the pool, but the timer already fired off or on awake to make it return itself to the pool again.
And we need to fix that.
We need to actually not use the timer in awake and instead use something else.
we need to move it so that our object doesn't get destroyed only once and only once after it's been launched out.
So, let's go back into our blaster shot script and make our final change to the blaster shot.
Instead of calling our invoke in on awake, we're going to just delete this completely.
We're going to instead just give ourselves a self-destruct time in our launch.
We'll say underscore selfdestruct time equals time plus our max lifetime.
We'll generate a field for our self-destruct time.
I'm going to hit F12 and just go remove that private keyword from it.
And then we'll copy that self-destruct time onto our clipboard.
And inside of the update, I'm going to say if time is greater than or equal to our self-destruct time, then we will self-destruct.
Otherwise, we're not going to self-destruct.
And if we hit this object, we hit and release ourselves or call self-destruct.
Oops, that looks like I accidentally deleted that.
If we call self-destruct down here, we're going to disable our object and update's not going to get called again.
So, we won't be self-destructing more than once.
Let's save.
Do a build real quick.
Make sure that the build succeeded, which it looks like it did right down there.
And then we'll get back into Unity and start shooting and watch as our blaster shots fire off.
And I should expect that we've got now no errors.
And if I pull in my second player, let's get this controller on.
We should be able to start blasting.
And the same thing.
We've got shots firing off in both directions.
And no problems at all.
If I go to my profiler window, I can pull this up and watch the memory usage.
Let's see if I can drag this up properly for once.
Watch my memory usage.
And it should just be relatively stable, not starting to skyrocket and fly off.
It is going to go up a little bit though because we haven't completely fixed the problem.
If I don't if I look over here, you see that now it's not going to go up at all.
The problem is that our explosions are still not pulled.
So those things are still spawning an object and still creating some memory allocations.
We have one other issue, too, and that's that both of our players have their own pools.
So if one player starts shooting a whole bunch, let's let's just reproduce it real quick.
If one player starts shooting a whole bunch and then the other player starts shooting a whole bunch, the second player is going to need to create all of its own objects because the first player has its totally separate pool and they're not sharing those blaster shots.
So that's something that we want to think about and something we want to optimize.
And the of course the other shots are the other problem.
So here we go.
This is that player this the second player running around and see all of my shots here and the size of the the pool right here.
As soon as I start shooting on my other player, we're gonna get all new shots coming in because this player has its own pool.
So, let's stop playing, jump into plastic, make sure that we've committed everything, and then we'll talk about how we can optimize this even more.
So, we've added basic pooling to the blaster.
And let's check that in.
I mentioned in the last section that each one of our players has their own pool.
And I want to show what that looks like just a little bit more before we solve the problem there.
Let's go into the blaster script.
And I'm on line 27 where we add a new blaster shot to the pool.
And right after we do that, right on line uh 31, let's just log the count of all objects on the pool.
We're going to do debug log_pool.ount all.
This will show how many entries we have in that pool.
I'm also going to remove this private keyword so that it matches with the rest of my naming and conventions.
Now, I'm going to go into Unity and we're just going to start shooting a little bit with one of our blasters.
So, we'll use one of the players.
I'll shoot and see what the log entries look like and then we'll press play and or join in on the other player and see what the log entries look like as well.
All right, here we are.
And if I got my log open, I start shooting, you'll see that we got zero items.
Shoot a bit, we're starting to build up the items.
And the number is now up to like 70, 85 items, whatever.
If I clear out the log, it's never going to be a smaller number.
We're just going to get more as the pool grows.
So, I've got 99 items in this pool.
Now, I don't know if I'll if I shoot more yet, I can get up to 120.
So, it's as many as I need to have.
But as soon as I add in my second player and I run over, you see that they start shooting.
Now they've got 20 items in the pool.
30 65 totally separate pool of objects.
So the total number of objects I have is now not 188.
It's 188 plus however many this other character has.
So I want to remove that and get it down to a single pool for all of the like objects.
This will make a lot more sense for if we have poolled objects for our enemies.
We don't want to have a separate pool for each single enemy that shoots projectiles.
We want them to all reuse this these objects.
So, we may as well do the same with our player.
To just get started, we're going to create a new script.
And this new script is going to go right along with our game manager and player input manager.
And this will be a pool manager that'll be responsible for pooling anything that we pull.
And it'll be a good place for us to assign objects and grab them back.
So, we're going to go into the project folder and rightclick in the scripts folder.
Create a new C script.
And I'm going to call this pool manager.
No spaces with a capital P and a capital M.
We'll open that script up.
And we're going to start by just making it return back a blaster shot.
We'll make it blaster shot specific.
And then we'll extend it out from there.
So, I'm going to get rid of the start and update methods and instead we'll add an awake.
And in the awake method, we want to initialize that blaster shot pool.
Let's just go steal that code away from the blaster.
I'll go into my blaster and we'll find the part in awake where we initialize the pool and I'm going to select it all line 18 through 20.
Crl X and cut it and get it right out of there.
We'll paste it into our pool manager and get rid of the private keyword.
Now, we don't have the add blaster shot to pool.
So, we'll go into the blaster method and we'll take that as well.
I'll select it.
So lines 24 to 31.
Crl + X.
Go over to the pool manager and we'll paste it in.
We don't have a pool yet.
So we should go steal that declaration too.
We'll go over to the blaster one more time.
Take line 11, select it.
Ctrl X and then go over to the pool manager and we'll paste it in.
Oops, I accidentally added a plus.
We'll get rid of that and paste it in.
Now we do have an error here saying that it doesn't know what the object pool is.
If I hit alt enter, we should get a using option for using Unity engine.pool.
Click that.
And now our pools are back in.
That got automatically added to the blaster when we typed it in, or at least when I typed it in last time.
Now we need the blaster shot prefab.
We'll steal that from the blaster as well.
Each one of these things that we steal out of the blaster is making the blaster script simpler and moving the responsibility of spawning these objects into the pool manager.
So, we'll paste it into the pool manager.
We've got a blaster shot prefab.
We've got a pool.
We've got an awake method and a method to create our blaster shots.
Now, let's go back into the blaster and clean things up.
So, line 8 is blank.
We can clear that.
We've got an extra space here.
We can clear that.
And again, shift shift delete or control X will remove these lines here.
XR X get rid of those lines.
And now in our trifire and our update methods, we no longer have a pool to get from.
So, we need to replace this pool.get get with something that gets it from our pool manager.
So, I'm just going to put pool manager.instance because I know I could just turn this into a singleton if I just put the instance right there and then call get.
I'm going to copy pool manager.instance, paste it over the underscore pool.
I'm also going to get rid of these comments at the end of the lines just to make it a little bit less confusing so I have less to look at.
So, now I've got pool manager.instance.get get that will return back a blaster shot.
So, I don't think that that's a good method name though for getting a blaster shot.
I should probably call this get blaster shot.
I'll replace get down here with get blaster shot.
And then I finally need to create an instance here and then generate the get blaster shot method.
So, let's start by generating a property for the instance.
Now, I'll hit F12 to go check that property out.
to give me a public static object of in instance or named instance.
We're going to replace that with pool manager.
So instead of object, it'll be a pool manager.
Instead of an internal get, it'll be or set it'll be a private set.
Inside of awake, we'll set instance equal to this.
So now we've got an object that we can get the instance of that we can then call the get blaster shot on.
We finally need to generate a get blaster shot method.
So go back to the blaster, hit alt enter on the get blaster shot and generate a method.
And then all this needs to do is return pool.get.
Now right now our pool is only a blaster shot pool, but we could probably rename that to blaster shot pool in in a few minutes when we have another pool type.
For now though, let's make this public.
Save.
Do a build.
And we should have a working pool manager.
And now a single pool for both of our blaster shots.
Let's go double check.
Oh, we've got yep, our log entry right there.
Just want to make sure it was still there.
We'll go back into Unity.
We're going to add the pool manager to our game manager prefab so that it's available in all of our scenes.
And then we'll assign that blaster shot to it and we should be good to go.
Let's go check that out.
Here's that game manager.
We'll add our pool manager script to it.
I'm going to collapse some of these down.
And then we'll go assign the blaster shot prefab to it.
See if we can find that in my assets folder.
The search didn't show it, but I know where it is.
Just in my prefabs folder.
Take that player blaster shot and drop it right in.
Now I want to apply my changes to the prefab by going to the overrides and hitting apply all.
Oh, here I've pressed play.
And let's go check it out.
So I've got my log open.
If I shoot a couple shots, I can see I'm up to 11 there.
I've got my second player here.
Let's bring him in.
Start shooting.
And this guy's got 17.
Let's shoot up to Okay, 124.
Let's clear the log and keep clicking and see that.
Look at that.
I'm not getting any more.
Next one's going to be over 100 at least.
I might even have to shoot two of the 125.
There we go.
Start shooting from both players to start building up more and more.
So now I've got a single pool for all of my blaster shots and they're being reused.
I don't have to create new ones and I can use the same system for all of my other pulled objects.
Let's stop playing.
Make sure that I've saved my scene.
I think my prefab is updated.
Let's go into the plastic window.
And actually the first before we commit, let's go back to the blaster and remove that log entry because we don't really want to be spamming out that we are um or I guess it's in our pool manager.
We don't want to be spamming out the log entry of how many things are in the pool.
So, I'm going to delete that out.
We'll save.
Go back into Unity, go to plastic, and we'll commit our change that we've now created a pool manager to handle pulled objects.
Created pool manager to handle pulled objects and check in.
Because our impact particles, those explosions, aren't pulled yet, we're still not completely saving ourselves from the issues that we'll have with performance.
So, let's set up a more generic pooling setup that'll work for our impact particles and any other impact or explosion type things that we might want to show.
We're going to start by going into our blaster shot script right to the spot where we spawn our explosion.
And instead of spawning our explosion and telling it to destroy, let's just tell our pool manager to spawn one at this specific point.
We'll say pool manager.instance instance dot and here we have a get blaster shot.
Let's say get blaster explosion.
And then we'll pass in the point or position where we want to spawn this thing at, which is our second parameter right here, the collision contact point.
So I'm going to copy that and paste it as a parameter.
I accidentally got the comma, so I'll hit backspace, go over and add my semicolon.
Now I know that I want this to last a little less than a second.
The rotation doesn't seem to matter.
And the impact explosion is a prefab that I have defined up above.
So I'm going to delete lines 51 and 52.
Just hit shift delete.
Shift delete.
And then I'm going to go up to the part where I have my impact explosion.
And I'm going to double click that line or just click and hit home and hit controlX to get that onto my clipboard.
Now I'll generate a method for get blaster explosion.
Alt enter to generate the method and F12 to go to it.
So inside of my get blaster explosion, I just want to return back an object from a blaster explosion pool and set it well but also set its point or position to this point.
So we'll say var explosion equals and then we'll say underscore let's call this uh explosion pool.get.
We don't have an explosion pool yet, but we'll get one in a moment.
Then we'll say explosion.transform position equals point and then finally return explosion.
I'm going to change the return type here to be a game object.
So we'll just return back any old type of object and the type or the public.
We're going to replace internal here with public.
There we go.
Now we're going to need an explosion pool to get our objects from and to put things into.
So, let's go up to our pool manager up at the top and take a look at where we have our blaster shot pool.
Right here on line 11, we have an object pool of type blaster shot named pool.
I'm going to rename this to blaster shot pool.
Capitalize the S and the P so that we keep that nice camelc case.
So, I've got a blaster shot pool and I also want to have a pool for our blaster explosion.
I have the blaster explosion line already on my clipboard.
So, I'm just going to paste it in.
Or it's the impact explosion.
So, maybe I should just call this I'm going to call it blaster impact explosion.
Let's rename it.
So, I've got my blaster impact explosion.
I have my blaster shot pool.
I need a blaster impact explosion pool.
So, I'm going to duplicate line 12.
And I'm going to copy, what is this? Line 10, blaster impact explosion all the way up to the word pool and paste it.
We'll change the type here from blaster shot to game object so that it doesn't need to be a blaster shot and it can be any old type of object.
And then we'll instantiate the pool in our awake.
To instantiate the pool, we'll just add in a new set of lines.
Let's type it out this time instead of copy and pasting.
I'll say blaster impact explosion pool equals new and then let it autocomplete.
Now we'll give it our three methods.
The first thing that we need to do is give it a way to add or create an impact explosion, which is just going to be instantiating an object, setting its pool, and then returning it.
So, right now, let's just return an object instead of instantiating one or let's instantiate one instead of doing one where we have a pool to set because we don't have anything to set a pool on yet.
So, we're going to use a lambda statement.
I'll do an open close parenthesis and then equals greater than instantiate.
Got to spell it right.
Instantiate.
Let's see if I can spell it.
There we go.
And then open parenthesis.
And we'll do our blaster impact explosion.
And I'm going to rename this to add the word prefab at the end.
So that I know very obviously that this is the prefab.
So that's line one or the first parameter.
Then I'll add a comma.
And then our second is the set active and set inactive stuff.
So we've got to just basically copy lines 21 and 22.
So say T and do our lambda T T.Aame object or actually we're already on a game object.
So we'll just do T dot set active to true.
And then for the third parameter we do T and another lambda.
T dot set active to false.
Add in the closing parenthesis and the semicolon.
And now we have a pool that will give us back an object.
And um oh that's pretty much it.
It would just give us back an object.
Now, we need to replace the word explosion pool here with what I named it, which was blaster impact explosion pool.
And save.
If we just use this, it's going to get us our objects.
But you may have noticed that we're still missing something.
We're not actually returning our objects to the pool.
And that's part of the issue with the game objects.
If we want to return them to the pool, we're going to have to do something else.
We're going to have to give them some script or some way to know how long they need to be alive for or when they should return.
Now, there are easy ways to do this and hard ways to do this.
And my recommendation is almost always go with the easy way until it doesn't work and until you actually need to go with something harder.
So, what we're going to do is create a new script that's more generic that we can add to any object that will just return it to its own pool after some amount of time that we can define on the prefab.
Let's start by typing down at the bottom of our pool manager.
We're going to make a public class called return to pool.
We'll inherit from MonoBehavior.
So we have the colon mono behavior.
And then we're going to add in here an on enable.
So in on enable when we've enabled ourselves, we're going to invoke a method.
And I'm going to call this release.
Well, actually we need the word name of here.
Name of the keyword right around the release name.
and get rid of that capital S there.
And then we're going to delay that by some amount of time.
Let's call that um delay underscore delay.
We'll generate a field for the delay, which is going to be a float.
And then we'll make this a serialized field instead of private.
And I'm going to give it a default value of maybe like a half a second.
We can modify this per object.
So it'll be totally customizable.
Next, we'll generate a method for the release.
So I hit alt enter and generate release method.
make it return back void or nothing.
So it has no return.
Get rid of the private keyword.
Let's get rid of this private keyword up here as well.
And then in the release, we're just going to tell it to return itself to its pool.
So say pool or underscorepool.release this.
Now we don't have a reference to a pool.
So that's the last thing we're going to need.
We're going to make a public method public void set pool that takes in a pool of type return to pool.
So it be an object pool of type return to pool pool.
Now I'm going to use a lambda statement and just say underscore pool equals pool.
I can also turn the release method into an expression body and then hit alt enter and generate the field for it.
So now we have an object pool.
Oh, it didn't give me the object pool type.
That's a little bit obnoxious, but I'll just copy it right here.
Object pool return to pool.
We'll paste that right in and save.
We'll do a quick build.
And now that we have one more issue that we need to remove remove this script from this file.
It needs to be in its own file.
It's a mono behavior.
And for it to work and be a valid component, it has to be the first class in the file.
So we're going to move it to its own file, return to pool.cs.
Then we'll go back into the pool manager.
And the final thing we need to do is just replace these instances of game object with return to pool for our blaster impact explosion.
I'm going to actually also here by the way if you're not sure how to do that the thing I just did there.
Just click hold alt click and drag and then you can type on multiple lines at once and go back on multiple lines as well.
Last Oh, where else are we missing it? It looks like the explosion prefab needs the correct type as well.
And then finally, we need to make sure that we're setting the pool because in our initialization right here, we just instantiate the object.
We don't set the pool.
We have a couple options.
We could make another method like we have for our add blaster shot to pool.
Or I could just add in a little lambda statement or a little inside of our lambda statement, some parentheses and a couple more lines.
If we just have one thing after the lambda, we don't need a semicolon.
But if we have more than one thing and we have them in these parenthesis, we need a semicolon for each line.
So I have a line to instantiate it and we need to assign that to something.
So I'll call this barsh shot equals instantiate.
Then we say shot setpool.
We'll pass in our blaster impact explosion pool.
And then finally return shot.
This is exactly the same as creating a method down here just with a little bit less code.
Kind of keeping it all compact so that it's in one spot.
Let's save.
Do another build.
That build popped up.
One more error that I missed, which is right here that our get blaster explosion isn't returning the right type.
It's got game object instead of a return to pool.
Let's try one more build.
See if that works.
Do we get it? Did all the errors go away? I think so.
Let's go back into Unity and tab in.
I'm still seeing an error down there, but I think it just hasn't caught my new file change because the return to pool file moved to its own file and it hasn't updated in the editor yet.
Once I tab over, it should reload everything and then reappear and the error should just disappear.
Oh, there it goes.
It popped back up my code editor.
Yep.
And now my build succeeds before I can even see it in here.
So, let's press play and see if everything is properly pooling now.
Oh, you know what? It's definitely not cuz I haven't added the prefab to my game manager or my pool manager and I haven't added the script to the prefab.
So, let's go do that first and then we'll press play and make sure that it all works.
So, here's my pool manager.
Let's go find that blaster shot impact or the explosion right here and drag it on.
But I can't drag it on because it doesn't have the component that it needs, the return to pool.
So, I'll add the return to pool component to the prefab.
go find my pool manager again.
Drag my blaster impact explosion on and apply changes to my override.
Then we'll go into play mode and start blasting.
Let's watch these explosions all start to go into the pool.
There we go.
I can see my explosions coming out of the pool and going back in.
They're getting readded, redabled, or enabled and redabled.
And I end up with a nice steady amount of blaster shots and everything is I think working pretty well.
Let's get one more player in here just for the fun of it.
Make sure that we're still seeing um all of our shots properly.
Yep, looks good.
They can shoot right through each other.
And my blaster shots are, I think, looking pretty nice.
So, I'm going to stop playing, save everything off, make sure that I've got my scene saved, and again, my prefab overrides in there.
And then we'll go into plastic and say that we've added a return to pool a generic let's say added generic return to pool script for the explosions on pool manager and we'll check that in.
It's time to take a deeper look at our players animator.
If we watch right now you can see that our player idles but also constantly shoots.
And that happens even if I'm running around or jumping.
And I also can't duck.
There's no way to do our duck animation.
So, let's go find our robot.
Let's find his animator controller and open up the actual controller for it and then take a peek.
So, we've got a couple things going on here on our animator.
First, we have this mobility layer.
And we're going to talk about layers in just a moment.
On the mobility layer, we've got a couple things happening.
We have our idle animation that's playing right now.
And if I run around, remember we've hooked up our movement animation.
And that's happening with the move option or the move checkbox.
When move is checked, when we're actually moving, it's getting set to false by our code.
But when we're actually moving, it plays the run animation, but our fire still keeps happening.
And the reason for that is our layer setup here.
So an animator controller can have one layer, and a lot of them do have a single layer, but you can also add more layers by hitting the plus button.
And you can use multiple layers to blend and combine animations.
Here we've got our idle playing on the mobility layer.
And on this action layer, we have a shoot animation playing.
Now, we also have a hidded animation layer, which I don't like the name of at all.
And it's also not showing anything.
You can see that it's playing through.
It says it's going none, hurt, and dead, but you can't actually see anything animating there.
The reason for that is on this gear, there's a weight option.
And if we slide this from 0% all the way up to 100%, you can see that it starts to play that death animation loop.
Of course, it's fighting with the mobility one.
So, I can't actually tell what's going on or I can't see the death happening very well.
Now, I can't crank down the weight of my base layer.
I have to do something differently.
And I don't really like this setup personally for death animations.
I feel like the death stuff should probably be on this mobility layer.
So, I'm going to turn the weight down and we'll move that stuff over later.
For now, I want to take a look at our shooting.
Our shooting animation is constantly happening, not just when I actually shoot.
And what I'd like it to do is instead fire off whenever I click the button.
So, as soon as I click or as soon as I start a shot, it'll just fire off that animation.
So, we're going to add a new parameter.
We're going to go to the parameters tab.
I'm going to stop playing because I found that if I add parameters when I'm playing, half the time Unity just crashes.
And then I'll hit the plus button and we're going to choose trigger.
I'm going to name this trigger fire so that it matches with my input.
And then we'll add a transition right here from none into shoot.
Well, we've got the transition there.
We'll add a condition to that transition that we have the fire trigger happening.
We'll uncheck has exit time so that it happens immediately.
And now whenever I set fire, it should do this shooting animation and not um when I'm not when I don't set this trigger.
So, by default, it's not going to sit there and keep playing my fire animation, and it should instead just play it every time I click this box.
So, I click it, and it fires off.
You might notice, though, that if I click it, and I click it again.
Oh, yeah, it's firing pretty good.
That looks good enough.
So, I think that what we'll do is go now into our code and hook up our fire animation or our fire trigger.
So, to fire this off, we're going to need to know on our blaster when we're trying to shoot.
And when we try to shoot, we'll just tell our animator to set this fire trigger.
So we'll open up the blaster script.
And in the method where we fire, well, right now we have two spots where we fire.
We have this try fire and then we have our rapid fire section.
Let's take the lines of code 23 and 24.
Select them both here.
Hit alt enter and move this into a method named fire.
Inside of that fire method, we'll also set the animators trigger.
So say undersc_an animator a tour that's a n i m a t o r dot oops let's control z to undo and fix that autocomplete and we'll do set trigger and we're going to set the fire trigger.
We don't have an animator yet.
So I'm going to copy animator.
Go up to the top of my awake and we'll put animator equals get component.
And we want get component in children animator because remember our animator is a child of this object.
So, we're going to hit alt enter on the animator field.
Hit home, then alt enter, and generate an animator field.
And then I'll get rid of this private keyword here and add a little bit of spacing between my serialized field and my non- serialized fields.
We're going to reenable the performed event so that we now try fire whenever the fire method is performed.
So, only when I leftclick.
And we're going to add some checks in here to see if we can fire in a moment.
But for now, we'll just call straight into the fire method.
So, we got an empty method here that's calling into our other fire method.
And then we're going to replace lines 39 through 42 with the fire call as well, so that we can rapid fire by holding the button down.
And finally, I think I'm going to comment that out, but with control C.
So, I've got rapid fire set up there if I want to enable it, but I'm going to have it disabled by default.
So, I'll save, do a build, make sure that we can compile, and then we'll jump into Unity and see if our animator starts playing correctly.
So, we press play and let's click, click, and shoot.
Click and shoot.
And you can see that every time I click, it pulls up and it shoots.
So, there's one change I want to make so that it's a little bit more responsive.
So, that if it's still playing the downward animation, it'll fire off and go up again.
Let's take a look at that real quick.
Let's go to the animator and let's take a look at our shoot layer.
Here we are.
And you can see that when I shoot, there are lots of times when it's still playing in the shoot and it doesn't restart the shoot animation.
So, what we can do is add a transition from any state.
I'm going to stop playing because I don't want it to crash.
Make a transition into shoot.
And then on that transition, add the fire condition.
So now, even if it's in shoot, it will go into this shoot state.
I'm going to remove the transition from none over to shoot because that's just a duplicate transition.
We already have one from any state into there.
So, we don't need that other transition just to make it extra confusing.
Now, if I click, you see that every time I click the weapon goes up.
It's looking a little bit more responsive and I think kind of the way that I want it to.
So, I'm going to stop playing.
We'll go into plastic.
Make sure that we've saved our scene and project.
So, I'm going to go save project.
That'll make sure that my animator controller is updated.
and I say that we um made our blaster only animate when it's actually shooting.
Animates when shooting and check in the change.
Now, we're going to take a deeper look at our robots animator.
We're going to hook up the duck, make sure that it works properly, and figure out how to make that work with our character's collider movement and everything else.
So, let's take a look at our animator here.
Here I've got my robot selected and I've got the base object underneath it with the robot controller on it.
And here I've got my robot controller opened up.
So double click on the controller and double click on the actual character controller right there.
Pops open this controller on the bottom.
I'm going to go select the base.
I'm going to press play real quick and just watch it in debug mode for a moment.
See that I can go between my states again.
So I've got my idle state here and I go into the run state when I start running.
If I jump, I go into that jump state.
My blocks start to fall down.
And if I want to duck, right now, I don't have any way to do that other than going to parameters and choosing the duck option.
Remember, I can hit fire, and that should work when I'm ducking or when I'm standing.
It's not shooting off a projectile because I'm just clicking the button on the animator.
And if I stand up and click it, you'll see that it does that same animation.
Now, let's go take a look at the layers again.
Remember, we've got a mobility layer.
That's what we're seeing right here.
This is the default layer.
It's just what it's named.
It's called mobility because it's handling the movement.
It could also be called locomotion movement or just about anything else.
A lot of times it's just called layer.
We've got this layer though that handles our moving, jumping, and ducking.
And then we've got the other layer here for our shooting.
And then finally, we have this hit layer that we're not going to hook up yet, but eventually we're going to cut it and move it over to our mobility layer.
So, what I'd like to do now is make our duck work.
And then I'd like to make it so that we can do a couple other transitions that don't exist yet.
So right now our duck works by transitioning from idle into duck when the duck condition is true.
That's our parameter right here.
When this gets set to true, goes into duck.
And then when it's set to false, it goes out of duck.
If I'm running, it also gets set to true.
Let's see.
If I run and I stop, you see that it went in from duck or from run into duck.
And if I try to get out, it should well, it's not going to go straight into running because I'm not holding down the controller and clicking at the same time because it knocks me out of focus in the window.
So, let's now hook up our duck.
To do that, we're going to need to set this duck parameter in our code.
To do that, we'll open up our player.
I'll go to my player and find the player script.
We'll open that up.
And inside of our update, we're going to start reading our vertical input as well as our horizontal input.
On line 80, we read the horizontal input by reading the action move and getting its vector to which is our X and Y or our horizontal and vertical.
And I want to get the vertical part from it as well.
So I'm going to duplicate line 80 and change this X to a Y.
Now, personally, oh, first I'll change this to vertical.
And then I'm going to say that personally I don't really like doing it exactly this way because now we're reading that action twice just to get the x and y value.
And I'd rather just take this line right here or this bit of code on line 80 the part where we get the vector 2 cut it with an x and call this u let's just call this input with a lowercase i.
I'll say var input up above equals and then paste.
And then on line 82, I'll put input.y.
So now I've got a horizontal input and a vertical input.
I'm going to copy my vertical input.
And I'm going to go down to the part.
Oh, I think um right around here where I set the horizontal and I had it commented.
So right after my acceleration, I'll add two lines.
And I'm going to say underscorean animator set bool.
And we're going to set that duck bool.
So say duck and we're going to or is it duck or ducking? Let's go double check that I've I've typed the same name.
It is named duck.
Just want to double triple check to make sure that I get it right.
So we're going to call it duck and then we're going to pass in true if the horizontal value is not a negative one or the vertical value is not negative.
So if we're not pressing down, we'll put pass in true and we'll pass in false if we are put pressing downward or trying to get a negative value.
So I'll say underscore vertical or no there's no underscore just vertical input.
There we go.
Less than oh vertical input.
Got to get these.
There we go.
Got my auto correct right.
Less than zero.
So if our vertical input is less than zero then we will set the duck parameter on our animator which should cause our player to duck.
Let's save.
Go into Unity and press play and see if our player now ducks when we push down.
All right, here we are.
And I push down and you can see he goes into duck mode.
Let go and he goes back into up or standing.
And if I run and duck, he goes into duck mode and kind of slides around and then goes back into run as soon as I let go.
All right, that's kind of good.
But I don't want my character sliding around like that when he's ducking.
I want him to kind of stop moving as soon as I start actually ducking down.
So let's go into our player script again and let's add another line of code here so that we don't move if our vertical input is less than zero or so that our desired horizontal becomes zero if we're pressing down so that we kind of stop moving left and right.
So to do that I'm just going to add a new line and we'll say if vertical input is less than zero then desired horizontal is equal to zero.
So, this should stop us from moving sideways or stop us from having an input sideways if we're pressing downwards.
Let's go try that out.
We should be able to get in here and run around back and forth.
Yep.
And then I hit down.
And now I'm instantly stopped.
Run over here, hit down, and I'm instantly stopped.
Now, there is one issue with this.
We're going to address this in a moment, but try jumping and then pushing down.
Look at that.
Our jump stops in the middle.
We don't keep getting that arc.
We're not actually finishing our jump.
We just start dropping down instantly.
And that might be a setup that you want.
Maybe you want it that you push down and you instantly stomp down like a Kirby or something.
But that's not the effect that I want.
So, we're going to need to address that.
But before we do, we should check in our changes cuz we've got quite a bit here.
And then we'll continue on and fix it in the next section.
So, say we've added duck input to the player there.
Get rid of that extra space and checking our changes.
Now, the way our duck code works right now, it stops us from moving if we're running side to side and we press down by just checking to see what our input is.
And while that works great if we're just running and we want to stop like that and just push down, it doesn't work so great if we're in the air like I showed you a moment ago.
If we're jumping and we press down, our animation's still in that jump animation.
You can see on the animator, but our character stops going instantly because we're pressing duck and we're trying to duck, even though we haven't actually started ducking, it's stopping us from moving.
So, we're going to make a modification to this code.
We're going to change it so that instead of ducking when our prayer player presses duck, we'll read from the animator when our player is actually started ducking.
And in that case, we'll go into the stop moving mode.
So to do that, we're going to add in another parameter.
We're going to add a parameter that we're going to read instead of writing.
And when I add a read parameter, I usually like to prefix them with the word with the word is just so that I know that this is the one that I'm reading and not the one that I'm setting.
We're going to add a new parameter and it's going to be a bool type.
And I'm going to call this is ducking.
Now, we're going to set this is ducking script or this is ducking parameter, sorry, from a script that we'll set on this duck animator or this animator node.
So, on this animation node, we're going to add a new behavior.
And we're going to do this by clicking the add behavior, hitting new script, and we're going to call this duck behavior.
I'll hit enter, and we'll now get a new animator behavior.
Let's go find this duck behavior.
There we go.
I hit control, comma to search for it.
Now, when we create a duck behavior, what we actually get is a scriptable object that's attached to this animator node that has a bunch of callbacks on it.
So, just like on a MonoBehavior, when we start, we get a start method and then when we update, we get an update method that gets called automatically.
We can also automatically call some things on these animation nodes and then tie into our code.
You can see here there are quite a few commented out methods.
There's an onstate enter that gets fired off whenever we enter this state.
An onstate update that obviously gets called every frame.
And there's a comment here gets called every frame.
And then there's one when we exit the state.
And then we've also got some for when we move and when we do inverse kinematics.
We're going to deal with the onstate enter and onstate exit.
So to do that, we're going to uncomment these lines.
What is this? Line 8 through 11.
I'm going to hold alt and just drag over them.
Click and drag and get rid of the comments there.
And in the on state enter, we're going to get an animator passed in.
When we enter this duck behavior or this duck state, what we're going to do is tell it to set the boolean parameter is ducking to true.
So say animator set bool is ducking to true.
Now I'm going to copy that line and I'm going to do the same thing here on lines 20 through 23 in the on state exit.
So alt click drag remove the comments paste and then we're going to set is ducking to false.
Let's go back into Unity and see what that does and then we'll see how we can use that in our code to make this feel a little bit smoother and actually work exactly how I want it to work.
So we've got our duck behavior right there.
We've got this duck animation node and the duck behavior is on it.
If I press play and watch our robot animate, I may need to go select the base object here.
See the animation playing.
Oh no, it looks like we've got it.
So I run around and as soon as I duck, look at that is ducking.
Notice that is ducking isn't exactly the same as duck.
When I press down, it doesn't instantly pop on.
It's pretty close, but it's not instant.
When I release, you can definitely see the little bit of a delay as it transitions between states.
So now, let's see what happens if I jump and try to duck.
Well, I jump and duck and I still fall.
But that's because we're reading this duck variable.
Let's go change the code and see what happens if we change it to the is ducking variable instead.
So to do that, we'll open up our player and we'll find the line where we read duck.
Oh, where we set the duck bool.
And then right below it where we're doing the if vertical input is less than zero instead of that we're going to say if animator.getbool is ducking and we'll get rid of the less than zero and add a parenthesis.
So this is going to return true if is ducking is checked or true and false if it's not true.
Now, if I go back into Unity, we should see that when we're in that jump state, we're no longer going to get the ducking behavior until we actually land and drop down to the ground.
And um we'll also see that tiny bit of a delay.
Let's see.
So, I run maybe I can definitely see the delay when I'm standing up.
So, I don't actually start running until I stand up.
And if I jump and duck like that, the ducking doesn't happen until after I land.
That is the behavior that I was looking for and a very cool use of animator behaviors.
So, if you haven't used these state machine behaviors on the animator, this is a great way to use them.
There are also lots of other things that we're going to use them for.
But before we continue on, the last thing I want to do is make sure that we have a transition from ducking to jumping because look what happens if we jump from our ducking state.
Let's go into a duck state real quick and jump.
And I get this weird behavior where not only can I not move left and right, but I stay in this weird ducking animation.
And also notice that my my head hits way too early.
That's because my collider isn't correct.
We're going to address that soon.
First though, let's stop playing and add transitions from duck to jump.
I'm going to right click on duck, hit make transition, and go into jump.
And we want to make this transition.
I'll hit the button on under the condition that jump is true.
So to say jump is true, we'll go from duck into jump.
Now I'm going to make a transition from jump into duck.
And in this one, we want to make sure that jump is false and that duck is true.
So we'll go into the ducking state from a jump if we're pressing down.
We're trying to duck and oh, I got that backwards.
Duck is true.
And we're not jumping anymore.
So let's save.
Let's press play again.
And now we should see that nice smooth transition from a jump and back.
Actually, it's not going to be that smooth because I didn't uncheck has exit time.
So, I'm going to select both of those nodes.
Uncheck has exit time.
Uh, and I crashed my editor.
That happens.
I'll restart it real quick.
And now I'll remove those has exit times while I'm not playing.
Exactly why I don't do it while I'm playing.
It crashes relatively consistently if I modify this animator controller in play mode.
Now, press play.
And we should expect to see the correct duck to jump transition.
There we go.
Duck to jump.
And it goes right back in.
And I can move when I'm jumping.
Obviously, if I hit my head on stuff, it makes it a little bit harder, but you can see my transitions are now working pretty good.
I can't move when I'm when I'm ducking, but I can jump from that duck state and kind of continue on.
All right, let's stop playing.
Make sure that I've saved my project now because I've been modifying my animator controller.
go into plastic and say that we added the duck behavior.
And I I added the U here.
I did not put the U in the name there.
So spell it whichever way you prefer.
I don't think it really matters.
Added duck behavior and made player able to transition from duck to jump and back.
And we'll check in our change.
Now we're going to move down our laser beam.
And we're going to do this so that we can duck underneath it and set up some interesting challenges.
To start, let's grab our laser object.
We'll take the laser and I'm going to move it right down to about here, about one unit up.
So, two and a 2.5.
I'm going to take my laser switch and drag it over here to the left a little bit so I can play with it.
And then I'm going to take one of these blocks that don't move.
One of the ones with no rigid body on it or anything else, duplicate it, and move it right down here underneath my laser just so that it looks nice and I can't walk right through it.
All right, so now I've got my laser here.
But if I press play, we're going to see some strange behavior.
Let's check it out.
In fact, we can probably already see a little bit of strange behavior.
My laser beam is uh off in a weird spot.
Let's go turn this laser on.
And look at that.
I now have a laser beam firing over to my player from down here.
So, what's going on here? Think about this for a moment and try to figure out in your head what's happening.
Why do I have a laser beam going from up in the sky and smacking my player? I can turn it off.
I can turn it back on.
But if I keep running over, you see that I still keep getting a laser on my head.
Now, I can get away from it by going over here or something.
But the laser is back on my head.
So, I want you to just for a moment think about what's going on.
Think about why this might happen.
And then we're going to talk through the cause and I'll show you how to solve it.
So, I'll assume you've thought through.
If not, you can pause and think more.
If not, or you're ready to continue on.
Let's take a look at what's going on here.
So, we have our laser object, right? This laser is placed right here.
I'm going to go to the scene view.
Our laser is placed right here in the world at 2.5 and -2.5.
Our laser has a laser burst object on it that's placed right in the correct position.
If our laser was shooting from here over to our player's head, that would be about where it would hit.
And we also have a line renderer.
And the line renderer has two points on it.
It has a position zero that's at one one.
And then a position one, which is well variable.
Let's watch as I move my character around what happens to that position one.
Position one changes.
Position zero does not.
If I modify position zero here, let's say I put this down to a zero.
You can see that it actually does change it.
So position zero is the start of my line renderer.
And since the start of my line renderer doesn't match up with the position of my object, well, it's going to look very strange and be offset.
If I copy the position of my object into position zero, then you can see my laser shows up properly.
All right, so it's ready for me to duck almost, except first, I'd like to fix it so that we don't have to manually adjust the position every single time.
So, we're going to stop playing and go make a change to our laser script.
We're going to open up the laser script and in our laser, we're going to add an on validate method.
On validate will get called every time it validates our object.
essentially every time we click on it, save or do a build.
And in the onvalidate method, where I'm going to remove the private keyword, we're going to do a couple things.
First, we're going to cache our line renderer.
So, I'm going to take line 16, cut it, and paste it into 22.
That also means that I need to make this into a serialized field cuz otherwise it will not save.
So, if I don't serialize this field, it'll get it in on validate.
It'll work fine on validate, but then when I go to play mode, well, it won't have a value cuz on validate doesn't run when you start play mode.
I'm going to get rid of line 10.
Add a line after there for 11.
So we've got a blank space.
And then let's continue on to our onvalidate.
So in our onv validate, the first thing we want to do is just set our starting point to our transform point.
So we'll say underscore line renderer set position and we'll give it index of zero, that first position, and we're just going to set it to our transform.position.
Now, our end point or the left hand point should probably do the same thing that we do for our update.
It should just figure out where the object is to the left of it that would hit and then draw the laser out to there.
So then we can see what it's going to hit and have a good idea of that in edit mode, not have to go into play mode to test it out.
So we'll take the end point code line 40 and 42 and 43 the part where we get the end point the default one out in our direction and then where we raycast in the direction to find a collider.
Copy all of those up to line 30 and paste.
And then we'll say if first thing collider end point equals and here we actually probably could have just copied this line right here.
First thing point.
So, we'll get that point or for our end.
And then the final thing we'll do is set the line renderer set position.
Oh, whoops.
I put this into the wrong method.
I put this into toggle.
So, we're going to cut this, put it into onvalidate.
There we go.
And we'll line renderer set position one to our end point.
Now, I'm going to get rid of that extra line that I added in my toggle method.
Take another look at our onvalidate.
And then, let's go look at it in Unity.
We should now see our end point properly assigned and our lines showing up in the right spot right against our player.
Now, the one thing that's wrong is that our little laser beam is in the wrong position.
So, let's go open up the laser script one more time.
What did I call that thing? The laser burst.
So, we need to make sure that the laser burst position is getting set as well.
And I believe that is right here, line 53.
So, we'll copy line 53 as well.
and we'll paste that over to uh well, let's see.
I guess we could probably just do it right here at the end.
So, we have the laser beam, the point either at the far end or at the thing that it hits.
So, then we'll know exactly how far it's going to go.
Let's check it out.
There we go.
Now, I've got my laser beam there.
If I grab my player and I move him around, I should be able to see it update once I go reselect my my object or maybe save or press play and eventually it's going to build and then validate that.
All right, let's go turn it on and we run over here.
Looks good.
I still can't duck under it.
And I stopped playing and yeah, my laser is looking good.
All right.
So, I'm gonna stop playing.
Well, I guess I already stopped playing.
Go into plastic and make sure that I commit my laser change.
So, laser are now movable.
And we'll check that in.
in.
in.
Now that our laser is in position and we can duck underneath it, let's take a look at why it's still hitting our player and see what we can do to fix it.
I'm going to grab my game view, drag it down below, and then take a look at my scene view.
I'll select my player character and take a close look at him.
So, here you can see I've got my character with this collider and it's hitting me kind of right on the face.
If I duck down now, you can see my character with that same exact collider and it's hitting right at the top of my head.
So, I'd like to change this.
I'd like to shrink down my collider so that it doesn't hit my player when I'm ducking.
Now, if I look at my capsule collider, you can see that I've got it set to a size of two here.
If I drop this down to about a one, I can see that now I fit underneath it, but that offset is way off.
So, let's set the offset to a 0.5 or I guess it's a negative.5.
And now I can see that it would go under or go right through me.
But I don't know if that looks right with the duck.
So, I'm going to duck and say that is probably a little bit too small.
If we look at the collider again, you can see it's this green capsule right here.
I think it should be a little bit bigger.
So, one is too small.
I'm going to change this to a 1.2.
And then I'm going to stop playing.
Get my default values back.
And let's just add a second collider.
What I think what I'd like to do is get my second collider in cuz I want to make sure that the bottom of it aligns perfectly with this one.
So we're going to take our capsule collider now and we're going to hit copy component.
Then I'll rightclick again and hit paste component as new.
That'll give me another capsule collider down below that I'll drag up here to be side by side with my full-size collider.
Now, I'm going to change the size of this one.
I'm going to shrink it down to a 1.
Oh, let's go to like a 1 2.
That might be good.
And then grab the Y and drag it down until it lines up.
Figure out what that value is.
What is it about a point4? There we go.
And then let's see how that collider lines up and looks.
I'm going to first turn off the other collider.
Just uncheck it for a moment.
Press play.
And then I'm gonna look, duck, see what my character looks like.
See how that lines up.
And make sure that the laser also goes over the head.
That looks about right.
So, it does kind of go right through the antenna, but that's kind of the the feeling that I was looking for, that the antenna wouldn't necessarily count as a hit.
Um, yeah, I think that that's pretty close.
I could, of course, increase it a little bit more, but I want to give my player a little bit of wiggle room.
So, I think that that is a pretty good value.
Now that I've got my two colliders here, I need to actually make sure that they switch back and forth or so that we can actually have the tall collider on when we're tall and the short collider on when we're short.
To do that, we're going to just open up our player script.
And we already have code where we check to see if we're ducking.
And if we are ducking, we're going to just enable one collider.
And if we're not ducking, we'll enable the other collider.
So, first things first, let's cache the is ducking variable into a bool.
I'm going to cut it.
Add a new line and say var is ducking equals and then paste our animator.getbool.
I'll copy that is ducking and say if is ducking desired horizontal is zero.
And then we're going to say underscore duck collider.enabled is equal to is ducking.
I put two equals one equal.
And then we want an underscore standing collider.
Actually, let's name this ducking collider and standing collider.
And we'll call it say enabled not equals is ducking or no, sorry, equals not is ducking and put my words all backwards.
So the exclamation mark will make it be the inverse or the opposite of what is ducking is.
Now we're going to need these two colliders to exist.
The standing and the ducking collider.
I'll hit alt enter.
generate a field for both of them.
Click on the first one, generate a field.
Click on the second one, generate a field.
Hit F12.
And they're both going to be the wrong type, but it's easy enough.
I can just altclick and drag and change these two collider 2D.
We'll change private to serialize field.
So, I hit home.
I'm still in block edit mode.
So, I've got both of the lines selected.
I'm going to hold control and shift and hit the right arrow and then put square braces.
Serialize field and closing brace space.
There we go.
I've got my two colliders.
I want to move these up though over by my other serialized field.
So I'll cut and paste them right up here.
Save and do a build.
Now I did get an error here.
Oh, I got an error cuz I didn't put the D on enabled.
I put enabled instead of enabled.
Fix that error and go back into Unity.
This is again why I like to do builds all the time.
Instead of save, do control shiftB.
If I have a typo or something, I'm going to get a notification, a warning right away.
Now my player should have a ducking collider and a standing collider.
The standing collider is the tall one.
The ducking collider is the short one.
Now that those are assigned, I'm going to go to overrides, apply all of my prefab overrides, press play, and see if my character can duck underneath this laser beam properly.
Run over here, turn the laser on.
I'm getting hit in the face.
And duck.
Look at that.
I can duck under it.
Now I can set up whatever I want on the other side for my laser beam to hit.
And also, I can now duck underneath enemy shots, which I think is probably the much more important thing and the thing that you're going to be doing even more often.
But a laser beam is just as important to duck under.
Well, maybe not just as important, but still important.
All right, let's stop playing.
Go into plastic.
Let's save our sandbox scene that has our new player updated.
And our player can duck under things with the proper collider now.
And checking our changes.
It's time to give our player some inventory.
Right now, he has a blaster that's permanently equipped.
And I'd like to be able to give my player multiple different items.
Maybe swap out weapons or give them items that they can pick up in a level and use throughout that level.
And I want to start with two different item types.
one that we can have across multiple levels that kind of persists with us and one that's just for a specific level like a key to a specific lock on the level that we have to grab and find to go open something or trigger some other action.
Let's start by creating a key so we have two different items and then we'll figure out how we can build this into an inventory system for our player so they can pick up multiple things and then switch between them.
We're going to begin by going into the items folder of art and grabbing one of the keys.
I'm going to take the yellow key and drag it out here so that it's just off to the side of the player so that I can pick it up.
I think I'll zero out the X position.
Just go to a flat zero and do a -3.5 on my Y so that it's just evenly aligned with my cubes.
Now, I'm going to add a collider to it.
I'll go with a circle collider 2D.
And this is going to be so that I can pick the key up.
When I touch the collider, I want to pick up my key.
I'm gonna shrink the collider size down because you can see it's a little bit bigger than the key.
Maybe to about half of the 0.5 and about a 0.25.
Think that's close enough.
Maybe a.3 would be a little bit better, actually.
There we go.
That covers the edge of the key.
Should be able to pick it up pretty easily.
So now I've got a key with a collider on it.
And I need a script to be able to pick this thing up.
So I'm going to go into my scripts folder.
Actually, first I'm going to grab my duck behavior and drag that into my scripts folder since it's a script and it kind of belongs in there.
Then we'll go into the folder and I'll rightclick and choose create and we'll pick C script and we're going to call this key with a capital K.
So keY and then we'll open that script up in Visual Studio.
Get our code editor up here.
Now in our key script, I want to keep it pretty simple.
I want our key to just be able to lock and unlock things.
But I also want my key to be able to be picked up by the player.
So I'm going to start with a simple ont trigger enter 2D.
We'll delete out the start and update and just do an ont trigger enter 2D.
Let it autocomplete.
And first thing I'll do is check to see if it was a player that touched us.
So just check against the tag for now.
We'll say if collision compare tag and we'll check against that player tag that we have assigned to our player.
If we have a player that we've touched, then all we're going to do is say that our transform.parent or set parent to set our parent because we want our parent to be this other object or the player that we touched.
So there we go.
We can let it autocomplete and have it give us the collision.t transansform.
I'm going to save.
We'll go back into Unity.
We'll make sure that this object actually has our collider set as a trigger and that we have the script on there.
And then we're going to go pick the key up and see what it does.
So we go over here.
Oh, is trigger is not checked.
So, we'll make sure that gets checked.
And then let's go add the key script.
Now, we'll press play, and I should be able to walk over there, pick up a key, and have it just kind of be bound to my my object.
Not really bound, but parented to my object.
So, I run over.
There we go.
Now, I've got a key that kind of follows along and gets drugged behind me.
That's neat and all.
Not exactly what I want.
I kind of want the key to be in my player's hand instead, though.
So, let's start by making a little change.
so that we can drag or drop the key right up to where this player's hand is.
And in fact, let's take a look at it while we're playing.
I'm going to go through and click click and find the object that I've got here.
So, it looks like there's a front object.
We've got the gun right here, which is probably where I want this thing.
So, while we're playing, I'm actually just going to take my key.
Let's see if I can find it.
And drag it to be a child of the gun for now.
I'll reset the position.
0 0.
And yeah, that looks like it probably about right.
Let's change the sprite renderer and adjust the sorting layer to be on props so that shows in front of our player.
And yeah, that's about what I'm thinking right there.
That key sitting right in front of the player.
So, what we're going to do is add a new point now so that we can drop this key onto where the gun is without it being directly on the gun.
So, we'll stop playing, go to the gun, rightclick, and we're going to choose create empty.
It's going to give us another game object that's a child of the gun.
I'm going to call this item point.
Oh, let's move the mouse off of there and then drag it out so that it's not a child of the gun anymore.
Now, I'll go to my player and apply my overrides.
So, I just hit apply all to add that item point to my prefab.
Next, I need to find a way to assign this item point.
And to do that, well, we'll just add a field in our player like we have for our blaster and our fire point.
So, we'll go to the player and we're going to add a new field here.
I'm going to make this one public for now.
make a public transform and we're going to call this item point.
We're going to leave it just as a public field because in just a moment we're going to move it out of here and completely change it.
So for now we're going to leave it as a public field that we can assign or use and read from in our key method.
So instead of assigning it to or setting the parent to our collisions transform, we're going to get the player object and then assign it to the item point instead.
So instead of checking the tag now, we're going to look for a player.
So we'll say var player equals collision dot get component type player.
Then we'll say if the player is not equal to null then we'll transform set parent and we'll set it to the players item point.
We'll add the semicolon there.
Delete outlines 14 and 15.
We no longer need that code.
And then we'll jump back into Unity and we should see the key getting dropped onto the hand and in the correct point, which is also going to give us the nice side effect of when we turn around and face the opposite direction, it's now rotated and snapped over to the correct side.
Let's see if that's the case, though.
So, we come over here, we grab the key.
Oh, I can't grab my key.
Oh, and that's because my point isn't assigned.
That's because the item point on my player is not assigned.
So, if I take the item point here, drag it over.
Now I'll run over and grab it again.
And you can see that my key is assigning itself to the correct child or the correct parent.
It's now underneath the item point.
But my position is not getting zeroed out.
So I've still got an offset here.
If I zero this position out, you'll see that it goes to the correct place.
So I need to make two more little changes.
Let's stop playing and make those changes.
Now first change is we got to go to the player and reassign that item point while we're not in play mode.
apply our changes to our prefab so that that gets saved and works in all of our levels.
Next, we're going to go into the key and in the part where we set the parent, right after we set the parent, let's also set our local position to zero.
So, we'll do it to vector 3.0 and we'll save.
Now, that should reset our key so that our key is kind of snapped directly to our hand.
And we before we finish, let's make the third change that I I forgot to mention, which is that we need to make sure that our key is on the correct sprite layer.
So, we're going to go to the sorting layer, and we're going to change this to be props instead of default, so that it shows up in front of our player.
Now, I'll save my scene, press play, and let's run over, grab our key, see if it snaps to our hand, and we can move it back and forth, and maybe start using it to open some locks.
There we go.
I've got a key in my hand, and it's looking pretty good.
I can still shoot.
Weapon still works.
There's nothing stopping that right now.
But I've got a key and I can uh maybe start bouncing this around and and using it on something.
So, let's stop playing.
Go into plastic.
Make sure that we've saved everything.
Save the project as well.
And then say that we added the key script and check in.
We have a key now.
So, let's add a lock and make our key work and then see if we can figure out where some inventory refactoring might tie in.
We're going to start by going to the tiles folder and grab the yellow lock.
I'm going to take lock yellow and just drag it out here somewhere off to the left.
I think I'll go with what is that like a -9 and again a -3.5, which is what my ground is set to.
So, I've got my lock over here to the left, and I want to make it so that my key can unlock this lock, and so that when I unlock the lock, something happens.
I'd like to be able to just kind of toggle this to turn something on and off, kind of like I do with the switch.
So, let's add a new script.
We're going to add a toggle lock script that can toggle the state of this lock on and off and fire off some events.
We'll go to the scripts folder, rightclick, create a new car script, and I'm going to call this toggle lock.
I don't want to use just the word lock because it's a reserved word and if I do a lowercase lock then I'm going to have an a conflict with that specific word.
It's one of the few special case words kind of like var or string or int.
Lock is another one of those.
So now that I've got my toggle lock script, I'm going to add it to my lock yellow object.
And I'm going to rename both of these objects.
I'm going to name this yellow lock and I'm going to name this yellow key.
key.
key.
These are going to be my prefabs.
Next, I'm going to go to the yellow lock and we'll add a collider to it.
So, let's add a box collider 2D so that I can't walk through it anymore and then figure out how we're going to write some code so that our toggle lock can do some toggling and switching of the state of this thing.
So, let's start by going into the toggle lock script and add just a toggle method, one that toggles the state of this to from locked to unlocked.
We'll delete out the start and update.
And I'm just gonna make a public void toggle.
And then all this is going to do is switch the state of a bool and change the look of our sprite renderer to start.
So we'll say toggled equals underscore or not toggled.
There we go.
Hit alt enter and generate a field for it.
And we should get a private boolean.
So this is going to be the bool for whether or not it's toggled.
In fact, let's rename this to unlocked underscore unlocked.
It's controllr to do that or F2 to open up the rename dialogue.
So, I've got an unlocked boolean that'll toggle on and off when we call the toggle method.
Next, I want to change the look of the sprite renderer.
So, let's cache the sprite renderer and an awake method.
So, add an awake here and we'll say underscore sprite renderer equals and then let it automatically type out the rest of the code for us to get the component of the sprite renderer.
We'll generate a field by hitting home and alt enter.
And then I'm going to get rid of all of these extra private keywords that I don't need.
And in our toggle method, I'm going to set the sprite renderer's color to either white or gray depending on whether it's locked or unlocked.
So we'll say sprite renderer dot color equals.
And here we'll do an unlocked.
So if it's unlocked, we'll get the value after the question mark here.
If it's not unlocked, then we'd get the value after the colon that's going to be there.
So, we're going to start with color.white so that we get the nice bright fully colored version.
And the if it's locked, so if unlocked is not equal to true, then we get that second value here.
And that's going to be colorg gray.
There we go.
With an a gr a y.
So, this should allow me to toggle the lock on and off visually.
And then I can probably fire off some events from there.
Let's now add a context menu to this so that I can make sure that it works.
And we'll use name of toggle.
There we go.
Save and do a build.
And we should be able to now toggle this on and off in the inspector.
And then figure out how we can call this toggle method from our code from the key or somewhere else.
All right.
So, we're back in Unity.
I'm going to press play and then I'm going to right click on my toggle script and see if I can toggle it on and off.
off.
off.
So, press play.
It's actually my toggle lock script.
There we go.
And it's up.
So, I right click and I toggle it.
And now it's going to probably the on state.
I right click again and toggle it and it goes to the off state.
Right click again and toggle it goes to the on state again.
So the next thing I want to do is make it so that we default into the off state so that it kind of starts off by default.
It's not on.
To do that, we can just add some code in our awake unlocked equals false.
And then let's set the sprite renderer color again.
So I'm going to copy line 20.
And for now, we'll just paste it up here as line 14.
Realistically, it's always going to be gray, though, so I may as well simplify it and get rid of the turnary check there.
And just make sure that we set the sprite renderer color to gray.
Now that we'll go back into Unity, we should see that it's disabled by default.
And you can ignore that little error there on my plastic connection.
And then we'll run over here.
It's just trying to connect with my internet connection reset.
And we run over and look at that.
My lock is off.
If I right click on the lock, I can toggle it.
And I can toggle it back off.
So far so good.
Next step though is we need to make our key handle the toggling.
So before we do that, let's just check our toggle lock into plastic or first let's create prefabs out of these and then turn them and then commit them into plastic.
So we'll take the toggle lock, the yellow lock here, drag it into the prefabs folder.
I'm going to put this into the list view or not the non-list view, the icon view so I can see some empty space.
We'll take the toggle lock, drop it over and the yellow key.
Sorry, it's the yellow lock and the yellow key.
Make those into prefabs.
Go into plastic.
Now I've got my three files.
So that we added yellow lock and check in.
Now we're going to add a way for our player to use the key.
We're going to specifically add a less than optimal way in my opinion and then figure out how we can refactor that and talk about why it's less than optimal.
We're going to start by adding the code onto our key script.
So let's stop playing.
We're going to open up the key script.
And when we pick up the key, instead of just setting the position, let's also bind up to the player input so that we can re remember or get notified whenever the player presses the fire button.
So I said remember, but I really mean get notified or or get told about.
So we're going to say var player input equals player.get component player input.
Then we'll say player input dotactions just like before.
And we're going to get the fire action by name.
See if I can get rid of that popup there.
And then we'll register for the performed event.
I'll say plus equals.
And I'm going to name this method use.
Let's call it use key.
Make it a little bit more explicit.
I'm going to generate a method for that.
And we'll get a use key method that passes in that callback context for our input action.
I don't care about that context, though.
All I want to do is find all of the locks that are within a specific range that I can customize or adjust and then tell them to toggle.
Now, to get all of the locks in a range, I can use the physics 2D overlap circle method, which is what I'll do first.
I'll type in var hits equals so that I have something that I can assign all of the hits to.
And it's going to be physics 2D physics 2D.
There we go.
Circle.
But I want to make sure that I get the circle that gets all of them.
So it's overlap circle all.
There's also overlap circle nonalloque which is slightly better.
We'll talk about that later though.
Let's for now just use overlap circle all because we're only going to be activating this or firing this off when we use the key anyway.
So it's not going to be a big allocation issue.
Now we need to give it two parameters.
The starting point or the initial position which is just going to be our transform.position position and then a radius which is going to be like our use range.
So I'm going to name this underscore use range and then hit alt enter and generate a field for it.
I'll hit f12 and then let's go give this a default of like 1 meter and make it a serialized field.
So there we go.
We've got a use range of one.
I'm going to add the semicolon to the end of the line.
And now we've got back a list or really it's a a collection or an array of these hit objects.
Now my my mouse over is not giving me the uh the proper tool tip there.
So I'll just continue on.
So we've got our overlap circle hits and what I want to do is l loop through each of these hits.
So I'll say for each var hit in hits.
We want to check against this object and see if it has a key lock or a toggle lock on it.
So we'll say var toggle lock equals hit.get component and we'll try to get a toggle lock component.
If the toggle lock exists.
So if it's there then we'll let's add some braces.
Say toggle lock toggle.
And then let's just break or return out of this loop so that if we have multiple toggle locks in range, we only hit one of them.
There should never be a scenario where we hit multiple.
But we don't want to loop over all of the other colliders in there if we've already found a lock.
I'm going to remove this private keyword now.
Save and do a build.
And let's go try out our key.
We should be able to run over and use our key on that lock and watch it turn on and off.
All right, we'll play and then run over and grab our key.
Come over to the lock.
Click.
And look at that.
It turns on.
Click.
It turns off.
Click.
It turns on.
Click.
It turns off.
If I don't have the key, well, then that's not going to happen.
So, let's just go double check that and make sure that can run over there with no key on and click cuz every now and then you'll write code and not realize that you shortcuted something.
So, let's see.
Yep.
Doesn't work without a key.
Exactly as expected.
And if I pick up a key and run back over, it works fine.
All right.
So now we've got our key kind of working, but there's definitely an issue here.
One of the biggest issues is that our key if it disappears is going to start causing us to get some errors.
It's going to start causing us to throw exceptions.
Let's let's take a look at that.
Go find our body upper arm right arm lower hand and that item point.
So let's say I just um deleted my key and now I press fire.
Now I'm going to start getting null reference exceptions because the performed event is trying to fire off into something that no longer exists.
It's trying to make a call back into something there.
We also have this is also getting called I believe by our our input system as well.
So the input system bindings are still there even though our key has disappeared.
Also, if we have that key there and then we have our blaster and we pick up some other items, our if our key is listening for the inputs and registering for that, then our our objects are I in my opinion doing a way too much.
They're thinking too much.
They're having a little bit too much control.
These items instead should probably be controlled by the player or by some player inventory and have that script tell them when to be used and when not to be used.
Then we can hook up our bindings once, have it so that our player input just binds to whatever system it is that uses the items, and then have that system tell the items, whichever item is currently equipped to be used.
So that's where we're going to take this next.
But for now, we're going to stop playing.
We're going to go into plastic, and we're going to say that we added a well, let's save our scene, too.
Added a bad key use system.
So added ba let's see added basic key use setup not optimal so that we remember it's not the optimal setup that we want um but it's our first version of it which is again the way that I always like to write stuff make sure that we've got our code we've got it working we kind of got it figured out and then we figure out the actual system that it's going to fit into try to let these systems kind of develop and build around what it is that we're creating instead of trying to guess and predetermine what what they need to look like.
So, let's check that in.
Now, we've got a key and a lock.
But let's say I wanted to add another item.
Let's just start with something simple like another key.
Maybe I wanted a blue key and I wanted to duplicate my yellow key.
Rename it to blue key.
Hit W in scene view mode and maybe move it over here a little bit to the right.
Change that graphic over to the blue key instead.
And then I save.
and I press play and I go pick up some keys.
Well, what do you think's going to happen? And think about it for a minute while we go into play mode.
And then let's go try it out.
And we should see that we end up with just two keys kind of stacked on top of each other.
You can see I've got my yellow key there.
If I turn off the sprite renderer for the blue key is right behind it.
And if I run over here and try to use it, you'll see that it doesn't actually seem to turn my lock on and off.
And the reason for that is actually because I've got two keys here.
So, I'm toggling it on, and then my other key is toggling it off.
And I can't switch between these two keys.
I can't really control what I'm doing here, and I don't like having to have both of my items stacked.
So, what we're going to do now is add our player inventory script that's going to deal with keeping track of our items, letting us switch between active items, and controlling when we use items.
So, let's start by going to our player and actually into the scripts folder, and then rightclick, create a new player inventory script, and then we'll add it onto the player.
So, I've got my script created.
I'll go to the player, and I'm going to add this new player inventory script onto there.
Now, I could add all of this code into my player script, but I want to take a look at my player script real quick.
It's actually growing to be relatively large.
Let's see.
We've got down here at the bottom 225 lines of code.
If I add in all of the inventory code to this, well, we're probably going to hit around 300 or 350 lines of code.
My player is going to start to get bigger and bigger and bigger, and it doesn't necessarily need to.
I generally prefer to keep my classes around 200ish lines or less so that it's relatively manageable and maintainable for me that I don't end up with a giant class with hundreds of thousands or tens I've seen the most I've seen is like 50,000 I think in a class and I've seen quite a few that were like 10,000 lines.
It's terrible and it's nightmare.
You want to end up with smaller classes in general that are responsible for doing one specific thing.
And that's what our player inventory script is going to do.
one thing.
It's going to deal with playing placing our items in the correct spot and showing the correct items so that we can switch between them and using those items.
So, it's one responsibility, although it does, I guess, technically do more than one thing.
It's one responsibility of keeping track of our inventory.
So, let's take line 23 here, this item point that we had put on player, and let's first move that over to the player inventory.
So, I'm going to cut line 23, get rid of those empty spaces.
I'll open up our player inventory script.
Control, comma, brings up the drop down and start searching.
Player inv.
There we go.
Player inventory.
And I'm going to paste our item point up here.
Next, I'm going to go to the key.
And in the key where we tell it to get a player, instead of getting a player, I'm going to get a player input.
And then we're going to tell the player input to just pick this item up and do whatever it needs to do to pick this item up.
So, let's replace player here with player, not player input, player inventory.
I think I might have said input there.
And let's replace the word player here with player inventory.
Control-r or F2 to rename.
And now that I've got my player inventory, and I know it's not null, I'll say player inventory.
This.
Now, I'm going to take all of the code after that and just cut it.
I'll generate a method.
Alt enter.
I've got that on my clipboard, by the way.
Crl + X or shift delete to put that onto my clipboard.
Now I'll generate the pickup method.
Hit F12 to go into it.
And inside of that pickup method, I will paste.
But now the code that I have is actually kind of inverted.
I don't want to set the transform of my player inventory.
I want to set the keys transform parent.
So I'm going to take key put it before the transform.
Say key.transform setparent.
And then I just want to set it to my item point.
I don't need the player inventory anymore.
I can get rid of that.
And then I let's see, let's double check that we've got everything.
Yep.
Need to set the keys transform local position to zero as well.
So put a key right there.
And then we can delete outline 15.
And then let's take a look at our new line 15.
We have this player input actions fire.performed.
Remember when we pick up a key now, we're just binding to that performed action so that we get a call back and we could call it tell it to use.
Instead of doing that when we pick up, let's do that inside of our player inventory awake so that we can use it all the time no matter what item we have picked up.
And then we'll figure out what our active item is and kind of pass that message along.
So we're going to cut line 15x again.
And I'm going to add an awake method right up here.
In the awake, I'll paste, but we need to get a reference to the player input.
So I'm going to make this be underscore player input.
I'll go up a line and say underscore player input equals get component player input.
Remember this player inventory is at the same level on our player game object as the player input.
So let's go take a look at it real quick.
Got player inventory here and player input right there.
So it's got a direct reference just by calling get component.
Now that we've got our player input getting grabbed, we need to actually generate the field for it.
So we'll select it, hit alt enter, and hit generate field.
Should give us a private field up there.
I'll delete that private keyword.
And then we're going to come down here and implement the use key method.
Now, I don't want this to be use key because this is going to use whatever item I currently have equipped.
So, I'm instead going to rename this to use equipped item and then hit alt enter and generate a method for it.
Now, I want to use whatever item I have picked up most recently by calling it use method.
And right now, the only method or the only items that I'm picking up are keys.
So, I'm just gonna save this off into a variable for mo my most recently picked up key.
We'll change this in a moment, but let's start with something simple.
So, say underscore um equipped key.
Let's think there's two P's in there.
Equipped key equals key.
It'll be whatever key we picked up last.
We'll generate a field for it.
So, now we have a private key field up here named equipped key.
And then in the used equipped item method, we'll say equipped key key key dot use.
Now use is not showing up because I don't think it's marked as public.
So we're going to hold down control and click on it.
See if we can go to it.
Oh, let's just hit F12.
Okay, it's not even taking us in there.
We'll just hold control and click on the key.
Oh, it's cuz I named it use key.
That's right.
So we're going to go down here.
We're going to change the use key method.
Let's replace the word key with blank.
So it's just use.
We're going to get rid of the callback context because I don't need to pass in any input data here.
And then we're going to make this public instead of private.
I'm going to remove this private keyword here on the ont trigger enter too since I'm already in the file.
Now let's go back into our player inventory.
And our player inventory now should be able to use the equipped key whenever we press fire.
Now we don't want this to fire off and give us an exception if we haven't picked up a key yet.
So let's add one more line here before line 22.
I'll copy equipped key and we'll just say if equipped key and then oops, there we go.
All right, let's remove these two private keywords here.
Do a build.
Make sure that it compiles properly.
It looks like my build succeeded.
So, jump back over to Unity and let's go try picking up a key with our new player inventory.
We can't switch between them, but it should allow us to just use the whatever the most recently picked up key is.
Let's see if the use method works.
That's the main thing I want to make sure is functional and working.
So, I go grab a key and you can see that it's not in the correct position.
And I come over here and I obviously can't use it.
So, let's go take a look at the player inventory.
Ah, the item point's not assigned.
Let's go take the item point and assign it on the player inventory and then apply our overrides.
So, overrides, apply all.
So, our prefab is updated.
We'll save the scene so that we've got the updated prefab in there.
Press play one more time.
And now I expect that my key should go to the right place.
Yeah, that looks good.
And I can come over here and use it.
And if I go over here and grab the blue key, I've got one key still active.
So I should still be able to use this.
And now I've got multiple keys and I've got a way to start using things.
And I can start to make this a little bit more generic.
And I've got one hookup point for it.
Also, if I go in here and I just delete out my keys, go delete those two keys and start clicking, I'm not going to get errors because we're checking to see if that key exists and it's doesn't exist anymore.
So, we don't throw an error.
We do have it looks like one object returning to a pool that's probably just placed in the scene.
Not an issue to worry about.
So, I think we'll stop playing and go into plastic and let's check in our changes.
So, here we'll say that we've added initial player inventory and check in.
Now, we're going to give our player the ability to switch between items.
We'll start with keys and then again expand out to more item types in the near future.
Let's go to our player and let's open up the player's input action map.
So, we'll double click on the actions and we're going to need to add a new action.
This will be our equip next action so that we can cycle through our different items.
I'm going to hit plus and just name this equip next.
And then I'm going to give it a binding.
So, I'll click down here in the bindings, and I'm just going to bind this to, I think, three on my keyboard.
So, I can just reach up, tap three, and then go on to the next thing.
You can bind it to whatever it is that you feel is the best next item button that you want, or you can even bind it to a mouse thing.
But I think that three is just kind of like where I rest my hand all the time.
I can reach up there and tap it nice and easily.
I'm going to save my asset, and then we're going to go into the player inventory script and bind up to this equip next.
So, let's go find our player inventory.
And right here where we're binding to our fire performed, let's duplicate the line and replace fire with equip next.
And then let's change the method instead of use equipped item to equip next.
Then we'll hit alt enter and generate a method for it.
it.
it.
And then get rid of that private keyword there.
So our equip next method is going to deal with changing what item we have equipped or what key we have equipped.
and then eventually what item we have equipped.
So to do that, to use that, we're going to need all of our equipped items in some sort of a collection so that we know what they are and we can go through them all and just activate the correct item.
So inside of our pickup method, instead of just adding a key and equipping it, let's add a key to a list.
So right now we we set the parent to it or we set the parent for the key.
We reset the position and we set the equip key.
Let's just add it to a items list.
So we'll say underscore items add and we'll add our key.
I'm going to generate a field for it and it's going to give me a totally wrong type of field I'm sure.
But I'll hit F12, go up to it.
Yeah, we got a private object.
Let's make it a list of keys for now.
We'll initialize it to a new list of keys and then hit home shift or control delete and get rid of that private keyword.
So now we've got all of our items that we pick up going into this list.
When we want to equip the next item, all we need to do is keep track of which item should be equipped next or which item is the next in our list, set that item to active and deactivate all of the other items and then also set our equipped key to that um specific one as well.
So to do that, we're going to keep track of the currently equipped item by index and then increment that.
So in our equip next we'll say underscorecurren item index++ then we'll say if our current item index is greater than or equal to our items.count we'll set the current item index to zero.
You can see that it's trying to autocomplete for me.
Current item index equals zero.
I'm going to hit home alt enter and generate a field for it which should just be an integer field.
they'll delete that private keyword and it's going to default to zero because there's no value set.
So we've got our current item index will increment when we try to equip the next item.
And then if it gets to be more than the number of items that we have or equal to the number of items that we have.
So say we have two items and our index gets up to two then we'll reset back to zero because zero will be the first item and index one will be the second item just like you see in our arrays in the inspector.
Same kind of thing here.
So, we've got our current item index incrementing and our items or our our resetting back to zero or looping back to zero.
Next, we want to just loop through each of our items.
So, I'll say four and then hit tab a couple times to have it generate a loop for me.
And I'm going to loop through the items.length or I guess it's going to be count because we're using a list and not an array.
So, we've got our loop through all of our items.
And what we want to do is set the item to be either active or inactive based on whether or not its ID or its index matches the current item index.
So we'll say underscore items or items at i.
We need the braces and the indexer.
So this is going to get us the first one zero at the first loop run through the loop and then it'll get us item one and then item two and so on until we run out of items.
So the first thing will be item zero and we're going to tell it to set its game object to set active and we want to set it to either true or false.
It'll be true if I is equal to our current item index and false for everything else.
So to do that we just say I double equals current item index.
So it'll go true for the one that we've selected and false for all of the others.
Now, this will toggle the object's active state, but it's not going to set our equipped key.
And we need to have that active or correct as well.
So, let's make a change to our equipped key, but instead of setting our equipped key inside of this equipped next method, let's turn this into a property instead.
So, I'm going to go to equipped key.
We're going to rename it.
Hit control-R.
I'm going to remove the underscore and the lowercase E and make it capital.
And then we're going to make it into a property.
And to do that, we're going to add a getter or just an expression body property, which is a lambda statement.
So do an equals and a greater than.
And what we're going to make it return is underscore items at our current index.
So now we'll get back the item at our current index.
Now, if we don't have any items at all, we need to make sure that we don't return back an an exception.
So if items has no entries and we try to get item zero, it's going to blow up and give us an exception.
So we also need to make sure that we've checked to see that items has at least the number of entries that we need.
So we'll say underscore items.count greater than or equal to our current item index.
Then we'll return back items at that index.
Otherwise, we'll just return back null and have no equipped key.
Now we've got an equipped key method or equipped key property that we can read from.
We no longer need to set it.
I'm going to remove that on line 45 and we'll save and then do a build.
Now, let's go try this out and see what it does.
You're going to notice that it almost works, but there's still one little issue here.
If we go pick up our our two keys, let's go grab them real quick.
And don't forget to remember what key you bound your next equip item to.
So, I'm going to run over here, grab that key.
Looks good.
I can hit three.
Doesn't seem to do anything.
Okay, looks cool.
Let's go grab this blue key.
You can see I got the blue key, but I don't see the blue key on me any right now.
If I hit three now, I can toggle between them.
But look at what that state was when I initially picked up the blue key.
It didn't turn on the blue key, and it didn't turn off the yellow key.
Well, I mean, the blue key was already on, so it just kind of left it there, but it didn't turn off that yellow key and hide the key away.
So, we never got the new equipped item.
When we picked up an item, it didn't automatically become equipped.
And that's what I'd like to change real quick.
Going to make it so that our item becomes automatically equipped.
Now, I think this seems like a perfect opportunity for a small challenge.
So, if you're up for it, go ahead and see if you can figure out how to equip the item as soon as you pick it up.
Do a little bit of refactoring, maybe extract out a single method, and then continue on, and I'll show you my solution for it.
All right, I assume that you've gone through it.
If not, then not a problem.
We're going to run through it right now.
The solution is actually pretty simple.
when we pick up an item, we just want to equip the most recent key or the most recent thing that we've grabbed.
So, first let's get rid of the start and update.
I don't know how those got in there.
I thought I had deleted them.
And then let's add a little bit of code here.
So, when we pick up, we're going to add an item.
And then let's just set our current index to be our last index.
We'll say it's equal to items.ount minus one.
So, this will give us our last index in the array.
Next, let's take our code that updates or toggles our active item and just extract it into a method.
So, we'll take lines 29 through 32, control shift or let's hit alt enter.
There we go.
And hit choose extract method.
And I'm going to call this um toggle equipped 2ps item.
There we go.
So, I've got a toggle equipped item that's just going to set the state of our item correctly based on whichever one's the current one.
And I'll copy that call to toggle equipped item and paste it down here in the bottom of pickup.
Get rid of that extra line there.
Let's jump back into Unity.
Got a little plastic error.
Not a problem.
We'll press play.
And now I expect that when I pick up the yellow key, it gets equipped.
And then when I run over and pick up the blue key, the blue key gets equipped.
Let's see.
So yellow key is equipped.
I can see the yellow key right there.
I go grab the blue key.
The yellow key is off and the blue key is on.
And if I hit three, I can switch between them.
So far so good.
Let's stop playing.
Go into plastic.
Make sure that we've saved our scene.
And I just want to make sure that I've saved my project.
I don't think there's anything different in there.
It looks good.
And say we added player inventory item switching and checkin.
Our current inventory system works pretty good for keys.
We can pick up multiple keys and toggle between them, but it doesn't do a very good job of dealing with our blaster.
We can switch between keys, but our blaster stays on.
And if I stop playing and start playing and just try to shoot, oh, we're going to run into an error saying that it can't find any keys to try to use and it's not trying to use our blaster instead.
In fact, our blaster fires off constantly, but we still get this error message.
If I go grab a key, the error is gone because it's able to use my key.
It's able to find something, but it's still firing off.
And this is definitely not the behavior that I want.
So, I want to make my blaster into an item.
I want to make it into a first class kind of item.
That's an object that can be used by our player just like the keys are.
But I want to do this slightly differently.
I don't want to take my blaster and pull it off of my player and then make it so that my player has to go pick it up.
I want it to be just kind of their default item that they start with or maybe an item that they can unlock and keep across multiple levels.
For now though, since I only have one weapon, I'm going to make it the default that they've got and they just kind of start with it.
So to do that, we're going to need to make a couple of changes to our player and to our blaster specifically.
Let's find the player object here in our sandbox and expand it out until we get to the blaster, which should be under the body upper and then the right arm and all the way down to the right below this item point, we've got the gun object.
If we go look at it in the scene view, let's go to the scene view.
We can see that this is our object for the blaster.
And I can turn it on and off by toggling the game object.
I'm going to rename this from gun to blaster.
And then we're going to take the blaster script from our player and we're going to click and drag it and drop it onto the blaster here.
That should move the script down to our blaster object and it's got a plus there and it should be removed from our player.
You can see it's got the minus right there.
And then we can go into our blaster and make sure that our settings are correct.
So, first thing we need to do is make sure we have a firepoint assigned.
And here you can see I'm in debug mode.
In normal mode, we see only the firepoint.
But if I go to debug mode, I can see all of the other fields that are going to need to be assigned as well.
We've got that animator, the player, and here it has a player input.
We're going to adjust this a little bit, though.
Let's go open up our blaster script, and let's make a few changes.
First off, I don't want my blaster causing animations to happen.
I want that to happen from my inventory system.
So, I'm going to delete the animator here.
And I also don't want my blaster reading input.
I want my inventory system doing that.
So I'm going to delete the player input as well.
I'm going to take line 14 and what is it? 16 and 17 and delete them all as well.
So we've just got our awake down to getting a player right now, which also is probably going to be an issue.
But for now, let's get the player.
But we need to get a player in parent.
So we'll do get component in parent because we're no longer at the same level as our player.
Remember our blaster is a child object way down here.
And our parent way up here has the player script on it.
There's our player script.
Let's go back into our blaster code though.
Open that blaster script and let's make the other changes that we're going to need.
So our fire method should no longer call the set trigger to fire.
We're going to do that inside of our player inventory.
So I'll delete that as well.
And I guess I'll delete out my rapid fire method.
The update.
I'm going to shrink this all down.
So now I've got a very small blaster script and I want this blaster script to be usable by my inventory.
So let's open up our inventory.
Let's save the blaster script and open up our inventory.
Inside of our inventory, the first thing I want to do is add our new blaster to our set of items and equip it.
I want to essentially call pickup and equip a blaster.
But you can see here that the pickup method takes a key.
And if I go look at our items list, well, we've defined this to take a key as well.
So, let's make something a little bit more generic.
Instead of having a key or a blaster there, let's have this be some sort of shared thing.
And I've got two options.
I can go with an abstract class, a base class that they both share and inherit from, or an interface where they both just have the same or similar methods.
And I feel like in this case, as with most cases, an interface is the best default implementation.
If we find that we're reusing a whole bunch of stuff and reusing a bunch of functionality, we could switch it to an abstract class.
But for now, let's start with an interface.
And to do that, we're going to create a new interface that our key and our blaster will both inherit or implement.
And let's call that I item.
So, we're going to go into our key.
And right at the end of our key, I'm just going to start typing a comma and I item.
I t.
So, it's an interface for an item.
That's why I'm using I item.
I'll hit alt enter and hit generate public interface or generate I item in new file.
It's the one that I want.
This should give me a new interface which is in a new file and it's going to say public interface.
Oh, where'd it go? Public interface I item or it says internal.
I'm going to make that be public.
Now, our interface is going to need to have at least one method on it that allows us to use the item.
It's going to need a couple other things, but the primary thing we need is a use method.
So, we're going to add a void use with a semicolon there and no parameters.
Let's go back into the player inventory.
And now, in all of the places where we're using a key, let's replace key with I item.
So, I'll take key and put in I item.
I'll copy that onto my clipboard and just start pasting it over all of my key entries.
So, my equipped key will now be essentially my equipped item.
We'll have to rename that in a moment.
The list will take I items.
And if I scroll down below, you can see that I start to have a couple errors.
The first error is that I item doesn't have a game object property.
So, it says I item doesn't contain a definition for game object.
So, we need to add one.
We can do that by hitting alt enter and creating a readonly property.
So, I hit enter and F12 to go to it.
And we should get an interface property here, but it's going to be the wrong type.
It'll be object instead of game object.
So, I need to go in here and put in game object.
Then save.
Oh, we got to hit alt enter and add the using Unity engine statement up to the top.
Then save.
We go back into our player inventory.
And now that error should be gone.
We can now call game object setactive on an I item.
It just has to be a mono behavior that has a game object that has a set active on it.
But as long as our interface is attached to a MonoBehavior, which in our case of a key, it is.
It's just on an object that inherits from MonoBehavior, it's going to automatically have that game object and be able to call set active.
Now, the other issue that we have is down here in use equipped item.
The equipped key check is giving an error because we're now comparing an interface to null instead of a class object to null.
And the shortcut of just checking it without the double equals null doesn't work when we're doing it with an interface.
So, we need to replace it with a not equals null to make sure that our equipped key or really our equipped item exists.
In fact, let's rename this to equipped item and then save.
Do a build and jump over to Unity.
And let's just make sure that our key still works.
We should still be able to pick up a key and use it, but probably not use our blaster.
So, here we are.
I can click and I get an error if I try to use my blaster as I expect.
I'm going to go grab both keys.
I can switch between them with my hotkey 3.
And the keys still work.
They still activate or toggle the lock, but my weapon doesn't shoot.
All right.
So, let's go back into the code and add our blaster as an item that we can use.
To do that, we're going to need to pick up our item probably in awake.
So, we're going to add a little loop in our awake method to find all of our children that implement the I item interface.
That way I can put multiple items on the player character from the start, have them kind of initialize with those or have those be on the prefab and then have them automatically be assigned.
I can toggle them on and off.
And I want to use these for items that I'm going to use across different levels.
For items that I want to use in a single level, I'll just pick them up normally.
So for the items that are children, like our blaster, we're going to find them with a get components and children.
And we'll use a loop.
So I'll do a for each var.
And let's call this item in get components in children.
I want the plural version to get the type I item.
So we want to get everything that implements that I item interface.
Then we want to pick up everything that's one of these items.
Now pickup doesn't take an I item.
So we're going to need to change the signature of it.
I'll control-click on it and we'll change key to be item.
And then I'm going to rename the key parameter here to be item.
Actually, I need to make this I item.
I've almost missed my I for the interface.
So there we go.
I've now got a pickup that takes items and adds them.
But you can see I've got another error because the item interface, the I item doesn't have a transform property.
So just like we did for the game object, we'll hit alt enter and generate a readonly property.
Hit F12 and go to it and change the type from object to transform.
It always just defaults to that base object which is kind of the uh the base level type for all of the objects in C.
And here I can see that I can shoot.
My blaster is working.
I can go pick up a key and it goes to key mode.
I can hit three to switch back to blaster.
Switch to my key and toggle these things on and off.
If I'm on my blaster, I shoot shots.
If I'm on my key, I toggle items.
So far so good.
I think it's time for me to commit.
So, I'll make sure I've saved my scene.
Go to plastic and say that we've added the blaster as an item.
It's got my duck behavior readded there.
I moved it around.
Just ignore that.
We're just going to check in these other files.
Now, let's take a look at player two.
We've got player one running around, ducking, picking up items, and doing things.
But what happens if we bring in a second player? I've got my controller here, and I'm going to try to join in as soon as I can get my mouse over the right spot.
There we go.
And I've got my character here that can run around and seems to duck quite a bit.
So, let's run over here.
See if I can pick up items.
Oh, I can get past the dog.
Okay, I'm going to go this way.
The dog is beating me up.
So, we'll run over here.
We'll go I see.
I'm ducking constantly.
And I'm going to run over here and pick up a key.
And well, okay, first things first.
My character poofed and disappeared.
And why did that happen? Well, let's take a look.
Let's see if there's a difference between our two players.
We've got our new player, our first player here, and our player's all set up with the inventory.
It's got the player input.
You can pick up items and this stuff seems to work.
And if I look at my other player, oh, you can instantly see that things changed, right? First off, the blaster script is on the player still.
And uh well, I wasn't able to pick up keys.
You saw what happened.
So, there's definitely a difference here.
And the first thing that we're going to notice before I give you any challenges is that our player hasn't had its prefab updated.
So, we need to hit apply all for our prefab.
We'll save the scene.
And now if I press play, I expect that our second player, while it will duck constantly, should be able to pick up an item.
Let's jump in.
There we go.
I got an item.
And I was able to pick up both of those items.
I can't switch items because I don't have a binding for my controller.
So, I'm kind of stuck on this key.
I should, however, be able to use the key.
But you might have noticed what happened there.
My key went kind of wonky and weird as soon as another player touched it because players just pick up and steal items from each other.
So, what we're going to do now is fix this issue and the ducking issue.
Now, we're going to take a look at item stealing.
Right now, our players can both pick up items and they can definitely steal from each other.
You can see that this player runs over, grabs the key, and runs off.
He could also run over and drop that key off if I'm slick enough with it.
Maybe I just got to take this guy over.
There we go.
Run over and steal the key.
They can pick up these keys and they can use them.
And they also get some kind of slightly strange behavior around them.
Look at this.
My character's toggling a lock with no key visible at all because the key actually was stolen by the other guy that's also kind of bugged out now.
So, how do we fix this issue? How do we stop an item from being picked up if it's already been picked up before? Assuming that we don't want to allow items to be picked up and passed around.
We could always add that later, but let's just assume that we want our items to stay with the player that owns them or has picked them up.
How can we go about that process? And what changes do we need to make to do that? It should be again, as usual, a pretty simple and straightforward change.
So, the challenge here is to go find the in my case, it's three lines of code that are all together that will make it so that your items only get picked up once.
So, I'm going to give you a chance to go ahead and see if you can figure that out, track it down, and if you need help, I'll give you a clue in just a moment, and then I'll finally give you the answer afterwards.
So, go ahead and give it a try.
And if you're getting stuck, let's just take a really quick look at the player inventory script.
Let's go through that.
We've got our player inventory script.
And right here, when we pick up an item, remember this happens.
Let's go find the line of code where it's called from inside of our player inventory.
It's called for picking up an item there.
And then if I hit shift F12, it's also called by our key.
So whenever we enter the collider of our key, we pick up the item as well.
So let's see how could we prevent this pickup from getting called again by another item.
Well, when we pick up our item, what we could do, if you haven't figured out the solution, if you've already figured out the solution, awesome.
If not, then what we can do is just disable the collider on the item that we have when we pick this item up so that it can't be picked up again.
It'll also prevent us from having an extra collider in there that's being calculated for no reason.
So, we can do that with a simple call to the items game object.
We'll say item.gameobject.get component.
And we want to get the collider 2D.
We'll save this off into a variable.
So, say var collider equals that.
and I'll say if collider is not equal to null.
So if we've got a collider then we'll set the collider enabled to false.
Now we need to check to make sure that we actually have a collider because our blaster doesn't need one.
We don't have to add a collider to our blaster to pick it up.
It's automatically there and picked up by the awake code.
So this code right here will disable it for the other objects that we've already picked up and or that we were going to pick up that have colliders and it will work fine for our blaster as well.
Let's press play and see if we can now run back and forth and get things working.
By the way, it looked kind of like we had our blaster stolen before.
It's not actually what happened.
What actually happened was that our item inventory index got messed up and we weren't able to switch back because an item got stolen away.
So, I've got my key here and if I let's see run over here, run past the player, you can see that he does not steal it.
I can take this player over here and he doesn't steal it.
I can use the key on the lock right there.
And my other player can run over here and grab a key as well.
I can switch between items on that player.
Run over here and even activate it by click.
I would be able to activate it by clicking, but I hit play.
But the one thing that I can't do still is switch inputs or switch items on my second player.
So, here we go.
Yep, that key works.
I join in, though, and I want a blast.
That works.
I get a key.
Cool.
But I can't change my attack or my weapon or my current item on that second player.
So, let's stop playing and let's do one more challenge in the same section.
Challenge is pretty simple.
Go ahead and figure out how to make it so that your item can be swapped on a controller as well as the keyboard.
If you don't have a controller, it's fine.
You can skip that part.
But if you do have a controller, which hopefully you've got something like this laying around, then go ahead and add in the input part for that as well.
And when you're done, again, continue on and I'll show you the solution.
All right, I'll assume that you're done or you're ready for the solution.
So, we're going to go to the player input and open up the action map.
Find equip next and expand it out.
We hit the plus and add a binding.
And then we'll just bind it up to oh, what is this? The the triangle.
That's it.
Tri angle on a PlayStation controller.
I'll save.
press play.
Now we should be able to go into Unity and press triangle to switch items and uh my right trigger to shoot.
Let's see if that's the case.
So I jump in.
I hit triangle and I can go back and forth between items and I can shoot with my shoot button.
I can go pick up another item.
Triangle goes through all three of them and my blaster still works.
So I think this is looking good.
I'm going to stop playing.
Go into plastic.
Make sure that my action map and my player inventory are both there.
And it'll say that we fixed item stealing and swapping with player two.
And check it in.
Now, we're going to add in another enemy.
This is the cat.
And the cat is going to reuse some of the concepts that we've already kind of started with and build upon them.
and it's also going to introduce some new concepts that we can apply back to our previous code.
So, let's start by moving the dog out of the way.
So, I've got my dog here.
I'm just going to put him up onto a platform over here.
Let's put that at what is this about five and uh I'm going to go with 4.5 there.
Have him sitting up there so I have plenty of room for my cat.
I'm going to go find that cat art object in the prefabs folder.
So, we have the cat right here.
here.
And if I double click on them, I can take a look at it.
You can see here it's a neat little robotic cat with a grenade on its tail that it's going to launch at the enemies.
So, the first thing I want to do is go find all of my sprite renderers.
So, we'll dig in.
Let's go just select everything and then, well, actually, let's go find the object that's not a sprite renderer.
I'm go select select.
I'm just going to click through and keep selecting until I accidentally select anything that's not a sprite renderer, like that foot.
As soon as notice that as soon as I click on an object that's not the sprite renderer, it says that this matching components list can't be edited.
So, I'm going to keep holding control.
That's how I select all these objects.
Just hold control and click.
I I realize that the foot objects are probably what I want to not click on.
So, I'm just not going to click those.
Select everything else.
Oh, effect doesn't look like one of them.
And then, now that I've got all my sprite renderers, I'm going to go to the sorting layer and we're going to Oh, I don't have my enemies layer here.
Let's um add a sorting layer and let's hit plus and let's call this enemies.
Thought I'd added one.
Apparently not.
So I'm going to go reselect them all and then do that again.
So let's just go I'm going to select all the way to the end.
So shift and end.
And then I'll just controllclick on the foot each each one of the feet and that one effect.
Now oh I'm missing something.
Is it the body? No.
One of these objects here.
We'll find Oh, it's the head right there.
So once I've unselected those parent objects, got my sprite renderer available again.
Go to the sorting layer and choose enemies.
Now if I look at my cat, I can see on the base it's got an animator, but it's missing the animator controller.
So I'm going to need to create an animator controller for my cat.
So let's go to the cat folder under animations.
Rightclick, choose create, and create an animator controller.
We'll call this cat.
And you can see that our cat has quite a few animations.
We're going to start with just an idle and a shoot, though.
I don't really need this guy walking yet.
If I decide I want him to walk, though, I can add that in.
Let's start by opening up our cat animator controller.
And here's my animator controller that popped up over to the side.
I'm just going to dock it up here.
I think I'll go side by side with my actual cat.
Then I'll take my idle animation and I'm going to drag it right into my animator controller.
I want to be able to go from an idle to a shoot.
So, I'll take my shoot animation and drag that into the animator controller as well.
And then we'll make transitions.
We're going to go from idle to shoot.
So, I'll right click, go from idle to shoot, and make a transition from shoot back into idle.
So, now we should be able to watch our cat character do his idle animations.
If I go select my character, let's see, let's go out of prefab edit mode.
Let's go drag a cat into our scene.
So, go from our cat.
Where's our prefabs? Take our cat and drag him right into the scene.
He's a little bit large right now.
Let's go make sure that the animator controller is actually assigned.
Oh, I didn't assign that animator controller.
So, let's go assign the animator controller.
Go back up to the prefab, hit overrides, and choose apply all.
Now, if I go to my animation window and I select the character right here, I can see some of my animations.
The two that are on my animator controller.
I got my idle and my shoot.
If I press play, I can see that it plays that idle.
And if I go to the shoot animation, I can press play and watch it do the shoot.
Let's hit play and watch it in game.
It should just go back and forth between the idle and the shoot animation.
See? So, it goes plays idle, then it plays a shoot, then it plays an idle, then it plays a shoot.
All right, looking good so far.
Obviously, this cat's a little bit big, though.
I've scaled everything else down to 0.5, so I think I'm going to scale this one down.
You're welcome to leave your cat huge if you want to have a giant cat.
Now to scale it down, we're going to take the base object, not the cat up here.
We're going to take the actual visual part right below it and scale it to 0.5 and.5.
Again, that Z doesn't really matter, but I like to just kind of keep it consistent there.
So, we're going to save that and then flip this cat around.
I'm going to go to the cat base object and do a 180 on the Z so that my cat is facing the correct direction.
So, now I've got my cat here.
He should be animating properly and let's see, swinging his tail off to the right, looking like he's going to shoot the grenade, but he is not actually ready to shoot that grenade.
In fact, if we take a look at the grenade here, let's go expand out the character.
See, it's under the body and then tail.
Tail.
There's a bomb here.
It looks like that's the object.
You can see that it's just a sprite object underneath this tail.
So, we're going to need to replace that.
We're going to need to replace it with an actual bomb that can launch, fire off, and hit our enemy or well, hit the cat's enemy, which is us, the player.
So, let's stop playing.
Go to the cat.
I want to make sure that I Oh, I do have one override change.
That's just for flipping the transform.
I don't need to apply that.
So, I'm going to go into plastic and say that we've set up our cat with the controller before we start putting together our projectile.
the setup cat and animator controller and we'll commit that.
Oh, and make sure that we've saved our scene as well.
This is our cat bomb.
It's just a spinning sprite that is going to explode when it touches our player or whatever other things we want it to explode on.
You can see I've got the animation playing here, but it's really just spinning along on the uh rotation.
So, it's taking this rotation value and it's spinning it.
And then there's a trail renderer that's adjusting its param its time.
So, that's for the trail that you'll see in a moment.
So, we've got it spinning around.
Again, this is just the cat bomb that we're going to set up.
Let's go to our project view.
Let's go find our cat.
And then, let's go take a look at our existing bomb.
If I look at here at my object and expand out my tail and look at the bomb, you see that this one's just a sprite renderer kind of holding the place of where our bomb is supposed to go.
So, I want to replace this now with our actual cat bomb object, the one that can spin around from our prefabs folder.
So, I'm going to take the cat bomb.
I'm going to drag it right on top of the bomb.
And then I'm going to drag it off of the bomb under up onto the tail.
I wanted to put it onto the bomb so its position would exactly line up.
Now I'm going to go select that bomb object underneath and I'm just going to delete it.
I don't want that object on there anymore.
Now I'm going to right click on my cat bomb and hit create empty parent.
And I'm going to call this bomb.
Let's call it cat bomb transform or catbomb firepoint.
There we go.
And then I've now I've got an object or a transform right here.
Let's hit W on it.
Oh, that's way off position.
So, for some reason, it did not create it at the position that I want it at.
So, what I'm going to do is rightclick and hit create empty.
And I'll name this cat bomb firepoint.
And I think that the reason that this went into the wrong position is it gave me a position in between the parent and the child.
And it really wanted a position at the exact spot of the child.
So, I'm going to take the second cat pom firepoint.
I'll take cat bomb, drag it onto the tail, delete the original cat bomb firepoint, the one that's bad.
Take the second one that I've created, drag it out underneath the tail, and I can just leave it there.
What I want now is to be able to spawn bombs at this fire point.
So, I can just keep spawning objects right here, and then eventually we'll figure out how to launch them away.
So, now that I've got my firepoint figured out, I think I'll actually just uh delete this cat bomb back out.
I'm going to go to my cat and go to overrides and apply my prefabs.
You see that I removed the bomb and added the firepoint.
Now I need to figure out and by the way, another easier way to do that would have been to just replace the bomb object and change it to be a the firepoint, but it was linked up with an animation.
And I don't know if that's going to cause other problems and figured we should show it both ways.
So here we've got our cat bomb firepoint.
We've got our cat.
Our cat now needs some sort of a script to deal with launching objects and deal with its cat behavior.
Remember on our dog, we have a dog script, but that's down here on the animator layer so that it can deal with animations.
And I mentioned that I'm not really a big fan of that.
I don't like having scripts anywhere below the top layer unless they absolutely need to be.
And there are ways around having our dog script at that level.
So, let's take a look at our cat script.
We'll put it at the base level and then see what we can do to maybe figure out how we can tie into animations that are one level below.
So, we're going to go to the scripts folder.
We're going to create a new C script and we'll call it cat.
We'll attach that to our cat here.
And then we're going to open that script up.
up.
up.
And the first thing we're going to want to do is get a prefab reference for our bomb that we want to spawn so that we can spawn a bomb whenever we kind of get to the point where we should reload.
And maybe if to start we can just do that every second or so.
So let's add a serialized field of type game object to start.
And we'll call this cat bomb prefab.
Inside of our start method, let's just invoke repeating that will spawn some bombs there.
So do an invoke repeating.
We'll give it the name of a method.
So saying name of and then we'll call this method let's say we'll call it let's say spawn grenade or let's say spawn cat bomb.
We want to keep it exactly matching the names.
And then we'll do it every 03 seconds.
I'll add a semicolon there and then we'll generate the spawn catbomb method.
See if it gives me the right type.
Oh no, it gave me it wants to return back an object.
We want it to return void instead.
And all we want to do in this is instantiate our prefab, which is going to be that catbomb prefab.
And we want to instantiate it at our catbomb firepoint.
So let's call this a fire point.
We'll generate a field for the firepoint that's going to be a transform.
So let's see, generate variable and field.
We'll scroll up here and we want this to be a transform, not a vector 3.
And we'll make it a serialized field as well.
So now we can assign a serialized field to our firepoint.
And every 3 seconds, oh, we're missing the second parameter here.
We need we need an initial delay and then a repeating delay.
So this will do it after 3 seconds and then every 3 seconds going forward.
So now we'll spawn a cat bomb prefab at our firepoint every 3 seconds.
Let's save, make sure that that works, and then we can figure out the actual logic for when we want to spawn one and when we want to launch it and how we want to do the launching.
Let's just press play though and see if we start to get some bombs.
Oh, we're definitely not going to because we haven't assigned the cat bomb prefab or the firepoint.
If I go look at the errors, you can see got lots of errors here.
An animation event and a prefab that's missing.
So, let's stop playing.
Go back in.
We'll assign the transform for the firepoint right here.
And then we'll go to the prefabs folder and find our cat bomb and drop that onto the cat bomb prefab.
Now, I'll press play one more time.
We should start to see our objects spawning.
They're just going to spawn, spawn, and spawn and stack up on each other.
At least that's what I expect them to do.
So, here we go.
You can see that we've got a cat bomb there.
You got a bomb kind of spinning around, twirling.
Now, there's three of them.
four of them and they're start now there's four they're starting to add up.
You can see more and more of these cat bombs are appearing on the tail.
So the spawning code is working.
The object is appearing in the right place.
And you can see that it moves and animates with it perfectly and it just now needs to kind of fire away and launch off.
Before we do that though, let's get our cat with our launcher checked in.
So, we've got a cat that launches or spawns and reloads cat bombs.
We'll check it in.
Now, our cat spawns bombs, but he can't launch them, and we need to make them launchable.
To do that, we're going to start with our cat bomb object.
Right now, it's just a visual prefab that shows that model that spins.
Just remember it's got an animator on it and it can spin around in circles.
I can hit play and watch it spin and then it does a a line renderer as well.
So it looks nice and pretty, but it doesn't actually hit things.
So let's start by modifying our cat bomb prefab and adding a couple components to it.
First, I've got my cat bomb selected.
I'm not in prefab edit mode and I'm not using one in the hierarchy.
I'm down here in the scene view.
So my changes for the prefab edit will apply.
So, let's hit add.
And I'm going to choose a rigid body 2D component.
This is going to make it so that my cat bomb can fall down.
Now, I also want to add a collider to it.
But if I just add a collider right now, I'm not going to be able to see it.
So, I'll double click, go into prefab edit mode.
See, my rigid body is already here.
And then I'm going to hit add component.
And we'll add a circle collider.
So, let's type CIR.
And a circle collider appears.
I'm going to expand this out and shrink down the radius just by grabbing it and dragging.
It looks like what was that about a 0 2.
That fits pretty perfectly.
So now I've got a cat bomb that should just spawn and drop down to the ground.
If I go back out of prefab edit mode, save and press play.
My cat now should spawn bombs, but those bombs shouldn't just stay on the tail.
They should kind of act a little bit weird.
Let's watch.
You can see it kind of drop down, but it still wiggles around because they're still attached to the parent object here.
They're still attached to the tail, but they are doing physics.
So, they'll fall and do their own rolling and stuff, but they still snap back around when this object moves, which gives it some very strange behavior.
So, I want my cat bomb to be a little bit more intelligent.
So, we're going to add a catbomb script now that can deal with launching it and also impacting players and whatever other stuff we want to impact.
Let's go into the scripts folder.
We'll rightclick, choose create car script, and let's call this catbomb.
Now that I've got my catbomb script, I'll go apply it to my prefab once it allows me to.
I'll select my prefabs folder, go find my catbomb, and hit add component.
Let's go add component.
Catbomb.
So my catbomb script.
This is going to first, I think, just have a method to kind of launch itself so it can detach from the tail right here.
So let's open up the catbomb script.
And then we'll delete the start and update methods.
We don't need those in there right now.
and then add a public void launch.
We don't need any parameters yet, though we might add some.
And the first thing we want to do is just set our transform parent to be nothing.
So say transform set parent and we're going to set it to null.
So we want to be able to launch a cat bomb and and eventually we're going to want to kind of shoot it off in the correct direction or maybe add a target, but for now we'll just set the parent to null so it stops doing that weird thing.
Now I'm not spawning cat bomb.
So, let's go into our cat and let's take a look at the cat script.
Right now, we're spawning game objects.
We need to change this to spawn cat bombs so that we can call that launch method.
We could of course just inside of our instantiate or somewhere in here maybe do a get component and try to get the cat bomb prefab, but I think it's generally or the cat bomb component I should say, not prefab, but it's generally better to reference the type that we want and reference the component that we want here.
So, I'm going to change the cat bomb prefab to be of type catbomb.
Now, we'll instantiate the correct object.
So, right now, we spawn a cat bomb every 3 seconds.
And let's say that we want to launch it.
Let's say var catbomb equals our instantiate method.
So, we'll get a reference to it.
And then we'll say catbomb.launch.
So, this should spawn our catbomb init right away.
and then drop it to the ground.
Or not right away, but every 3 seconds.
And as soon as it spawns it, it will drop it right to the ground.
Let's go try that out.
First though, we're of course going to need to reassign our cat bomb.
Oh, we don't actually need to reassign it.
I'm surprised it caught that prefab change.
So, normally those get dropped.
If you don't see your cat bomb prefab there, make sure that you go assign it.
It's probably because I've added all of the components without tabbing back in at all and it and just kind of lined up and worked.
But a lot of the time that reference will get dropped because we've changed the type.
Okay, so I've got my cat bomb spawner there.
You can see the bombs are spawning and they're no longer attached.
If I look here, I can see that this is the fire point and the bombs are down here.
So the bombs are spawning.
They're not launching in the correct direction, though.
So let's now make them launch forward and to the left.
So to do that, we're going to go back into our Oh, let's open up our cat script.
See if I can get that open.
Oh, there we go.
And then inside of our cat script, when we call launch, let's tell it just which direction to launch our cat bomb in.
I want to go off to the left and up.
So, I'm going to pass in vector 2.up plus vector 2.
Now, I'm just hard coding this guy to shoot to the left for now, but we can of course use our direction later.
Let's add in the parameter to our launch code.
So, I'm going to hit F12, and we're going to add a new parameter to the launch method, which is a vector 2, and we'll call this direction.
Now, we need to add some force to our rigid body in that direction.
Since we're going to be using this catbomb multiple times, and we're eventually going to pull it and reuse it.
Let's cache our rigid body.
And we'll do that in an awake method.
We'll add an awake and say underscore RB equals get component.
And we don't want a rigid body.
We want the rigid body 2D.
Make sure you get that one.
We'll add a field for the rigid body with alt enter.
Get rid of these extra private keywords here.
And then in the launch method, let's say underscore rb add force, which will add force in a specific direction.
And we'll give it the direction.
And we'll multiply that times some force amount.
We're going to give that another or we're going to turn that into another field.
So hit alt enter, generate a field for it.
We'll make this a float so that we can easily adjust it and give it a default of about 300.
We'll change the private to a serialize field.
And now we've got an adjustable amount of force that we can apply on our cat bomb and launch it in the whatever direction we want.
Let's go back into Unity.
Oh, let's make sure that we've saved our cat file.
So, we need to be passing in that launch parameter.
Do a build.
Make sure the build succeeds, which it looks like it did.
And then we'll go back into Unity.
Make sure that we don't have any errors.
Press play.
And let's see if our cat bomb now launches off and to the left.
So, we've got a cat bomb spawner guy here.
There we go.
So, he does spawn them.
He does launch them off to the left, but as you can tell, it's completely unhooked from our animation.
So, let's stop playing and then let's apply our overrides to the prefab for the cat.
Save our scene.
And I want to go into plastic and say that we've added catbomb script and launching.
And next, we're going to tie that into our actual animation so that it fires at the correct time.
Let's hit check in.
Let's take a look at the animations for our cat again.
If I go back to my cat object and I look at my animations, I've got my idol here, which I can see playing on the cat.
looks kind of cool.
He just wiggles around and then I've got my shoot and I play that and you can see that there's a very specific point where it seems like he should be launching the object.
That's kind of how I expect to get my art from an artist.
Let's take a look at it in slow motion.
If I drag it here, you can see that when I get right about here, yep, that's when the thing's about to launch.
And you can see that up at the top there's an animation event assigned.
So, the animator actually kind of specifically thought that this was the perfect time for this object to launch and added an animation event.
We don't have a script assigned to it, though.
That's up to us to do.
And this is going to be the case anytime that we get something with an animation event or we need to tie into an animation.
It's going to be pretty much always up to the programmer.
Sometimes a designer is going to do a little bit of it, but programmer is going to have to set it all up.
So, we need to tie into this animation event.
And if I hit the drop down here, you see that it says no function selected.
And the reason for that is because if I look where the animator is, there's no script.
So I've got some options.
I could take my cat script and drag it down to this child.
And then if I went over to my shoot and found my animation event and hit my dropdown, I can see, oh, spawn cat bomb is now available.
But I mentioned earlier that I don't really like having scripts down at lower levels.
So, I'm going to take the cat off that base object and move it back up to the cat.
And the reason that I don't like that there is um well, here let's hit apply overrides and just make sure that we've got a single cat script there is that it often hides a lot of logic.
If you open up a project that has a lot of prefabs in it and there's not much at the base level, it's very easy to misunderstand what those objects are, how they work, or have a hard time digging into what it is that they're doing.
If there are lots of scripts that are littered all the way down the hierarchy here, it gets much much more complicated to deal with.
Having all of the scripts at the root level of the object usually makes the most sense and is usually the easiest to deal with.
So, how are we going to get messages though or animation events from this animator to the cat? Well, in that case, what I do is add in a special script.
So, we'll add another script that's sole responsibility is to pass messages up from the animator to our cat or to our other parent objects because notice on our dog, we have the same issue.
Our dog is down here.
Just so that it can receive back an animation event, which I believe was the shoot one.
Yeah, is this animation event right there.
So, let's go add in a setup so that we can do that without having to move our cat script down.
We're going to start by going into our scripts folder.
And I want to create a new script.
And I think I want to call this a um maybe like a fire animation wrapper or shoot animation wrapper.
Let's call it shoot animation wrapper.
Um so that way it's very obvious that it has nothing to do with actual fire.
It's it's about the weapon shooting.
Shoot animation wrapper.
We'll attach that shoot animation wrapper script to our base object here.
Oh, got a nice reload here.
We'll go select the cat though, select the base, and drag the shoot animation wrapper script onto it.
I'm going to open that shoot animation wrapper script.
And as usual, I'm going to delete the start and update methods.
And I'm going to add in two things.
First, an event that's an action.
So, I'll add a public event action.
And I'm going to call this onshoot.
Then I'm going to add a public void shoot.
The shoot method is going to call onshoot.
So I'm going to use onshoot question mark.invoke.
Hit tab and tab again.
So we've got an expression body method.
Since it's a oneliner, we'll use the expression body instead of the parenthesis.
And it's going to invoke the onshoot method if it's registered for.
That's what the question mark's doing there.
avoiding a null reference exception if nothing has registered for on shoot.
I'm going to delete out lines two and lines three and line nine.
And look at how nice and short that got.
So now we need to call into our shoot animation wrapper.
To do that, we'll go back into our cat script and inside of our start, instead of doing an invoke repeating, let's get our shoot animation wrapper.
So I'll say var shoot animation wrapper equals get component.
And I don't want to get a component.
I want to get a component in children of type shoot animation wrapper.
I'll hit tab and make sure that I get that semicolon over there at the end.
Let's zoom out just a tiny bit.
And then on our shoot animation wrapper, we're going to register for our onshoot event.
So I'll do shoot animation wrapper.onshoot plus equals spawn catbomb.
Whoops.
Get the B in there.
remove the semicolon and delete out that invoke repeating.
So now whenever our shoot animation wrapper says it's time to shoot, our spawn catbomb will fire off.
Let's go back into our script or our our project, not our script.
And then let's go hook up that animation event now.
So we'll go to the animation window.
We've got the cat selected.
We'll go to the shoot animation and go find that animation event.
We now have a option here for shoot because that's part of our shoot animation wrapper.
And our cat should now be registering for that and listening so that it can launch off a bomb as soon as it uh as soon as it's ready.
As soon as it gets to that shoot point.
Let's go watch.
Boom.
Look at that.
It's now launching my bombs exactly when I want it to.
Looking pretty good so far, I think.
Let's stop playing.
And now before we go any further, let's have a little challenge.
What I want you to do is take advantage of what we've just written here and see if you can refactor the dog so that our dog script is no longer at the base level and is up at the parent here.
And I say the base level, I mean this base level, not this actual kind of base parent level.
So I want you to make the change so that our dog script can go up to the top.
Go ahead and get that done or continue on in just a second and I'll show you the solution.
All right, I assume that this was pretty easy, but what we're going to do is add that shoot animation wrapper to our dog base object here.
Move the dog script up one level to the dog and then we'll open up our dog script in our code editor.
So, let's see where's our dog script.
There it is.
Inside of our dog script, we'll add in a start method.
And then in the start method, we'll get that fire animation event wrapper.
So we'll say get component in children fire animation.
No, a shoot animation event wrapper.
Shoot animation wrapper.
And then we're going to do an onshoot plus equals shoot.
I'm not even going to cache this component because I'm not going to listen for any other events on here.
Now I can make this shoot method not be public.
So I can remove the public there and remove the public here.
Turn this into an expression body method.
Oh, I guess it's not going to let me.
And then realize that when I'm shooting, I don't even really Oh, that's why I had a little extra character there.
I don't even really need to call this code because it doesn't do anything yet.
But let's leave it in here for now.
Let's save.
go back into our game and make sure that our our dog still at least logs out that he's shooting even though he doesn't do anything when he is doing his his shoot yet.
Oh, and first let's apply our overrides to our prefab.
I'm going to press play, go to the console log, and we'll just watch to make sure that our dog is still calling his shoot stuff as well.
So, go to the scene view.
Yep.
You can see he he logged out shooting.
And every time he goes up and down, that shooting counter is going up and down or up again.
Now that that's working, I want to make sure I've applied my prefabs on my cat and my dog.
Save our scene.
And let's go to plastic and say we added the shoot animation wrapper, which we're going to update in the next section.
Now, we're going to do another challenge.
The challenge here is pretty simple.
What I want you to do is try to reproduce or recreate the behavior that you're seeing right here with the cat.
So, watch when his tail goes back, a new grenade appears or a new bomb appears.
And when his tail gets to the end point, it launches.
So, it's not spawning when it's launching.
Instead, it's spawning when it's resetting and getting ready, just kind of sitting there waiting to launch.
And then when it's ready, it launches off.
And then eventually, a new one spawns out.
Let's watch it in slow motion real quick.
I'm going to zoom in here.
And we're going to go frame by frame.
So, you can watch as it gets down to the bottom, a new one appears.
And if I keep clicking fast enough, you can watch it go forward slowly, slowly, slowly.
Oh, it's still doing a whole idle.
Let's just watch.
There we go.
It got to the end.
Ah, I was too slow.
But you can watch that.
It's empty until it gets down to that point and then reloads.
So, that's the mission.
See if you can figure that out.
If you get stuck, don't worry.
There's quite a bit to it, but it's just reusing a lot of the concepts and things that we've already done.
There's nothing new that you need to do.
Just redo a lot of the stuff that we've done.
See if you can figure that out and then continue on if you get stuck or even if you don't so that you can see my solution and we'll see how how well they align and match up.
Now, to accomplish this task, we're going to do something simple.
We're going to extend out this shoot animation wrapper.
Right now, it does onshoot.
Let's add an on reload, so that we can have an animation event fire off when we want to reload, and then have our cat do the reloading at that time.
So, I'm going to select both of these lines, six and seven, hit control D, hit the left arrow, and enter.
I'm going to rename the second one to on reload.
Rename this method to reload and then copy and paste on reload into there.
So now I've got an onre reload and a reload.
I'm actually going to move my events up and then my methods down so that they're kind of aligned in a way that I think looks a little bit better.
I'm going to double check that on reload calls reload and shoot calls on shoot or reload calls on reload.
Shoot calls on shoot.
Let's go back into our cat now and where we call our registering for the onshoot that spawns a cat bomb.
Let's duplicate and add an on reload.
Now, to me, on reload sounds more like something that should spawn a cat bomb, and onshoot should probably shoot the cat bomb.
So, let's rename this one to shoot catbomb.
Hit alt enter, and generate a method for it.
Got to go down and choose generate method.
Now that I've got a shoot method, I can take this catbomb launching part.
In fact, maybe I should rename this.
Oh, no, let's leave it as shoot.
Um, I'm yeah, I'm going to leave it as that name.
I'm going to take line 27, cut it, and paste it over 21.
But you notice that we don't have a cat bomb here.
This isn't a field variable.
This is just a parameter or a local method variable that was around.
So, let's promote this thing up by removing the var keyword and adding an underscore instead.
We'll hit alt enter and generate a field for it.
And we should end up with a private cat bomb right up here.
I'll hit enter on that private to just clean that up.
I'm actually going to hit shift delete on the start method too to get rid of that extra comment.
Not the start method, but the comment right above it.
Now, in our shoot cat bomb, we'll add the underscore so that our cat bomb can launch.
I'm going to remove this update method down here as well and kind of clear out all this clutter and shrink our file down to the size it actually needs to be.
So, this looks like it should work.
It should spawn our bomb at the right time and then launch our bomb at the right time.
For it to work though, we're going to need to hook up our animation event.
So, let's go back in, find our cat's base object, the one with the animator on it, and find the animation window.
Or just go to window and animation.
Animation right there.
Should pop it right back up.
And then I want to find the shoot animation.
Here you can see we've got our shoot animation event right there at the top.
And I want the reload to happen probably right here at the end.
Either that or right at the beginning.
I'm thinking um right at the end so that he has the grenade on his back like at the end of the shot while he's idling.
It's just kind of sitting there ready.
So to add a new animation event, all we need to do is rightclick on this top part wherever we want the animation event and choose animation event or add animation event.
I'll choose the function that I want, which is reload from our script right there.
And then we'll press play.
I expect to see a couple things.
The grenade should appear there.
It might act a little bit wonky and weird for a second.
Let's see.
And then I also expect to see a little error in my in my logs, but the grenade does launch out.
So, couple things to address here.
First, when our grenades or cat bombs spawn, they fall to the ground.
I don't want that to happen.
And they're spinning already by default.
I don't want that to happen.
And if we look at the console, we have an error here, right when we start because our first time that we call the animation event for our launch or our shoot, which is right here, is before we call the first time for our reload.
So, we end up calling shoot when we don't actually have a a bomb loaded up.
So, let's stop playing and address all of those issues.
We'll start in the cat bomb.
When we first spawn our cat bomb, let's make it so that it's not simulated and that the rigid body doesn't move until it's launched.
To do that in our awake, we can just say underscore RB is simulate or no, it's simulated, not is simulated equals false.
I'll copy that and put it down into my launch method right before the ad force and change the false to true.
That should stop it from dropping instantly.
I also don't want it spinning and doing that animation.
And so I'm going to cache the animator in awake with underscorean animator equals.
Whoops.
Let's hit control-z.
It got the wrong thing.
Equals.
And I don't want to get component.
I want to do a get component in children of type animator.
I'm going to hit home alt enter and generate a field for it.
And then on the next line, we'll say underscorean animator.enabled equals false.
We'll copy line 16.
Paste it down here after 22 onto 23 and enable the animator once we've launched it.
Now, this should work at least once.
We're going to have to do some addressing things when we start pooling this object, though.
But for now, let's remove the private keyword on the animator.
I'm going to move the serialized field up a little bit, rearrange things so that it's nice and clean.
Get rid of these two extra using statements and the extra line at the bottom.
Take a look at our script.
And I think this looks pretty good.
We should now be able to launch and have our object look right.
But we still have that issue of we're spawning or we're firing off a bomb before we've actually spawned one.
We've got a couple options here.
We could either in our shoot cat bomb check to make sure that we have a cat bomb, that it's not null.
But I think that it's better that we just start by in our start method spawning a cat bomb so that we already have one ready to go and load it up and we don't have to worry about it.
Um, shoot catbomb should probably set our cat bomb to be null once it's shot.
And then in our spawn cat bomb, we can just check to make sure that we only spawn a cat bomb if shoot cat bomb or if our cat bomb is null if we don't already have one.
So I'm going to zoom in here and we'll say if underscore catbomb is equal to null.
That way if we accidentally spawn a cat bomb some other way, we're not going to end up with two of the bombs stacked on top of each other.
We'll always have one until we launch it and then we'll get our next one.
We won't keep respawning multiple.
Not that I expect that to happen, but I just like to write it a little bit safer to make sure that in the future we don't have to worry about that.
Let's remove lines one, two, and three here with shift, delete, shift, delete, shift, delete.
And I think we are good.
Oh, let's get rid of these extra private keywords as well.
Shrink this up a little bit.
Save.
And then let's go try it out.
This should be the complete solution that solves all of those problems.
All right, we'll press play.
And there's our first bomb.
You can see it starts spinning and launches out.
Second one starts spinning, launches out, and watch when it reloads.
It reloads when it gets right back to the end.
Exactly as I expected.
All right, I'm going to stop playing.
Make sure that we don't have any changes to our prefab to override.
Go into plastic and say that we fixed catbomb reloading.
and check it in.
Oh, got the error there.
It's okay.
We'll just hit check in one more time.
Oh, I wanted to update our animation.
It's good.
I almost missed the animation file.
Now, we're going to start building out some cinematics.
We're going to do this in preparation for a boss fight and create cinematics that both kick off at the beginning of our level and when something interesting happens.
To start, I'm going to go into level one.
You can use whichever level you want.
If you've already got stuff built in level one that you want to keep, you're welcome to just copy your level and make a new one.
But I'm going to take level one here and expand it out just a little bit.
So I'm going to take this grass here on the right hand side that I've got, duplicate it with controll D.
Controll drag it over and just give myself a little bit more grass.
And then I'm going to add a little area I think on top of this platform.
It's going to be an exit that's keyed off.
I'm going to do that by going into my stone section of the ground.
Grabbing one of these stone center tiles, dropping it right on, putting this at, let's go with a 41 and a three.
Switching the draw mode over to tiled so that I can drag it up or make it taller.
And here I'm just going to hit T, hold control, and drag it up so that it's too tall.
I want to watch that height so it gets just to the correct height.
Duplicate that stone center.
And I'm going to hit W.
Move this one up here.
right to about there so that it's at what is this 41 and 5.5.
Then I'll hit T, drag it down so that it's only one tall and then drag it over to the left and again holding control so it's about oh let's go to five wide.
I want to get it kind of wide here.
Next I want to grab some of those locks or the toggle locks that I've got.
I believe those are in my prefabs folder.
Let's go find my yellow lock.
There it is.
I'll drag it and drop it right out here.
I'm going to put it in a kind of snapped position of looks like about 37 for me and three.
And then I'm going to make this one tiled as well so that I can make it fill up the entire wall.
So as soon as I touch any part of it with a yellow key, I can have it open up.
So let's hit tiled and I'll hit T over here.
Oh, switch over here.
Hit T, control drag and get it right up to the top.
Now I can see my collider here is not the full size.
It's that little green box there.
That's because I haven't checked autotiling yet.
So, I'll hit that.
And now I've got a fullsize collider.
So, I've got my lock here.
I want to add in a key that we can show the player.
I think I'll put the key maybe way over here to the right.
So, I'll take our yellow key and drag it over here.
And now I've got some things to show them.
Well, let's add one more thing.
Let's add an exit as well.
I'm going to go to I believe it's under tiles.
I've got an exit sign.
And I'm going to drop that right in here.
And I might even add a door.
Let's do that.
Let's go find a door.
I'll take a door closed mid.
Drop it right here.
And then I'll take a top piece and make that a child of that door.
I'll zero out the position and set it to zero and a one so that it kind of snaps onto the top.
Get that door nicely positioned at what is this going to be? 40 and three.
And then I'm going to do the same with that exit sign.
Just kind of snap it over to I guess I'll go to 38.5 and three.
So, it's right there.
You can see that it's an exit.
Actually, I think I want to move this door over just a little bit.
I'm gonna hit W, hold control.
There we go.
Think that looks a little bit better.
So, now I've got a scene where I can show my player an exit and a key that's passed there that they're going to have to get.
I do still have this flag here, though.
So, we should probably get rid of that since it's not going to be the actual exit anymore.
Or, you know what? Let's undo that.
I'm going to just move that over here to the left.
So, I've got a cheat way into level two.
And then I'll go add that same load level script and a collider onto the door.
So we can use that as our normal exit.
So we got this load level script.
I'm just going to rightclick and copy it.
I'll click over here to the door.
And then I'm going to choose the little buttons here.
And there's right off to the side.
Let's just drag it over so it's visible.
Go right off to the side.
I'll choose the paste component as new option.
Gives me that load level.
But I do need my collider.
So let's add a box collider 2D as well.
I'll drag this back out.
And now I've got a valid exit, a key, and some stuff to show.
Now I'll just clean up the hierarchy a little bit.
I'm going to take my exit signs, my stone pieces, move them into the environment folder.
I think I've got my yellow keys and locks, and my door.
Want to move these as well along with the springs and the spikes.
So, I'm going to drag all of these into environment.
They're just kind of props that I'm not too worried about.
I want to get them out of the way and kind of invisible.
Take my lock and my key and the door as well.
Drop them all into that environment folder.
Kind of shrink this down.
I don't have a whole lot here.
We'll save.
And then I'm going to go into plastic and say that we've set up our initial level for our cinematic or setup.
I'm going to say set up level one for the cinematic.
intro and we'll check it in.
Now that our level's set up, we're going to do our cinematics.
And the first thing I want to do is show the player the exit.
To do that, we're going to start by creating a virtual camera that's aimed right at the exit.
We'll go to game object, cinem machine, and virtual camera.
I'm going to name this virtual camera exit.
And then I'm going to move it by going into transform move mode.
So, click on it over here, hit W, zoom out, and aim it so that it's right over the exit.
If I pull up my game view down below, I can actually see what it looks like.
If you're not seeing it there, you can hit the solo button to force it.
You may have it as a lower priority.
And if it's a lower priority, and it's not in solo mode, like it is right here, you see that it doesn't show up.
But as soon as I put it into solo mode, it shows up or it forces it to.
Now, I want to adjust the zoom of this.
I want it to be zoomed way in on the exit.
So to do that, I'm going to adjust the ortho size.
So just drag this way down here so that it's zoomed in a whole ton and then drag it up so that I've kind of got this just nice view of just my exit.
It looks like about a 2.5 and I'm going to level off these numbers just because I like to, but you don't necessarily have to.
So I've got my camera lined up right here for the exit shot.
After showing them the exit, I also want to show them the key though.
So I'm going to duplicate the camera, this virtual camera.
Let's rename this one to key instead of exit.
I'll move it over here to be over our camera.
Let's get that game view back up.
And then I'm going to adjust the ortho size.
I want this to be zoomed out a little bit more.
Maybe like a 5.5.
And I drag it up here.
Now, I don't really like that there's a blank spot here.
So, I think I'm just going to grab some more water, duplicate it, and controll drag it over to kind of fill in that area.
And I might add some more grass there.
actually think I'm just going to move this camera over a little bit to the left here.
So, there we go.
I've got a view of that key and I've got my exit set up as a separate camera.
Now, I need to make it so that we can show these things and we're going to use the timeline system to do that.
The first thing that we're going to do is create a new timeline, but we're going to create it in a new folder called cinematics.
I'm going to go to my assets folder, rightclick, choose create, choose folder, and call this cinematics.
I'm going to put all of my timelines in here for showing intros to levels, showing bosses, and anything else I want to show.
I'm going to go into that folder, rightclick, choose create, and about near the bottom, about 2/ird of the way down, there's a timeline option right above signal that we'll talk about later.
I'm going to add a timeline, and I'm going to call this level one intro with spaces in there and capitalization.
Hit enter.
And now it should have created my level one intro timeline.
I'm going to collapse some of this stuff down in my hierarchy real quick and then just drag this level one intro right in.
What that's going to do is create a new game object with a playable director and my playable timeline asset assigned.
Now that I have my timeline, I can start to set up the actions that I want to happen.
I need to make sure that I've got my timeline object or my playable director selected.
And then I'm going to create a new track.
Down here in the bottom left, you can see I've got a add new tracks option.
and I can click it and get a popup.
And I'm going to choose a Cinem Machine track.
I want this to work on my main Cinem Machine camera brain.
So, I'm going to hit search.
And it's this Cinem Machine brain one.
I can click on it and find it.
It's the one under my multiplayer camera setup.
That's the one that I'm using right now.
I think the other one was buried underneath my player object.
Now, now that I've got my Cinem Machine track or my Cinem Machine control, I can take a virtual camera exit or my virtual camera exit and just drop it right out here.
This is going to make it show this virtual camera when the timeline gets to that specific point.
Let's grab the game view and I'm going to drag it up here to be kind of side by side with the scene view.
And then I'm going to just scrub through here.
And notice that as soon as I get it over to this point, right where it hits the line, the camera on the game view completely switches.
When I get past the end, it switches right back.
Now, if I just hit play, you should see that.
Well, let's watch.
Here it goes.
And my camera is kind of stuck on this exit one.
I'm not actually seeing a switch back and forth.
And the reason for that is pretty simple.
Just the priority on these two cameras is higher.
It's set to 13 and the priority on our main camera is set to 10.
So, I'm just going to take these two and we'll just set the priority down to a nice low one.
And now, let's go back to that playable one more time.
Press play and let's watch the camera do the transition.
And we should actually see it automatically switch from one camera to the other when it gets to that point.
And then go right back.
There we go.
That's kind of cool, but it's a little bit fast and I don't really like that it instantly pops.
I want to show them where that camera is and have them get a little bit of a quick view to it.
So, to fix that, I can go select this virtual camera exit line.
And then go to my clip timing.
And there's an easein duration.
I'm going to set that to two, give me two seconds to ease into it.
And then let's scrub over and look at what that does.
You can see that that does a nice quick or nice kind of quick but smooth transition over to there.
I realized I'm in play mode.
So, I'm going to stop playing and then I'm going to add in my other camera target, my virtual camera for the key.
To do that, I'll take the virtual camera key, just drag it right here to the right and then drag it over so that they overlap.
And you can see that if I get it to about this 5 seconds mark, it's going to go for 2 seconds to warm up.
It's going to wait from the 3 second mark to the 5-second mark.
So, another two seconds there where it just kind of hangs out for a minute at that exit.
Then for another second, it's going to transition over to the virtual camera for the key.
I think I want that transition to be a little bit longer, though.
Let's make it like 2 seconds long.
So, drag that line out here.
And then I'm going to give my virtual camera key an ease out duration of oh, 2 seconds as well.
So, that way we show the key and then we show the exit.
I think I want to drag this out to maybe about 11.
There we go.
Give myself a little bit of time there.
Now, let's uh save.
And actually, I'm just going to press play down here in the timeline view.
This will allow me to watch the entire thing without having to go into game view without having to play.
So, I can see what it's going to do.
It's going to show that camera, show that camera, and then go back to the player.
Now, the reason that it's automatically playing and playing instantly is because the play on awake option is checked on our playable director.
So, if I press play right now, I should expect to see that we get the full intro.
There we go.
The exit sign shows, the key shows, and then we're back to our player who can run around and do whatever.
All right, it's looking good so far.
I think it's time to commit and then take a look at what we need to modify, especially around that player.
So, let's go in here and say we've added initial cinematics and check it in.
Now, we're going to look at a problem.
Let's press play and let the cinematic play.
But watch what happens when I'm in my game view and I start trying to run around.
So, my cinematic is playing and you can probably see what's going on with my robot on the left hand side.
Just going along and doing all kinds of stuff, bouncing over here and dying, not staying where I want them to, which is generally what you want to happen during a cinematic.
You don't want the rest of the game kind of going on and things happening.
So, we're going to add a way for our game to semi-pause when a cinematic is playing.
Specifically, we're just going to lock down the player's movement, but we could stop anything that we want.
If we want to control and stop other things, it's very easy to add that on.
Let's go to the level one intro and figure out how we're going to do this.
Right now, we only have access to our virtual camera, but we can access pretty much anything in our scene.
If we try to use our players though and do something directly to the player, we're going to find that we have a problem because we can't access things that aren't in our scene yet.
And our players are instantiated at runtime.
They can die.
They could be recreated.
Things could happen to them.
We can't guarantee that we're going to have a reference to them in in our timeline.
So instead, what we want to do is reference our game manager and tell our game manager that a cinematic is playing or that a cinematic has stopped playing.
And the easiest way to do that is to go down into our timeline.
So, I've got the intro selected, go rightclick, and choose a new signal track.
A signal track is going to allow us to create an object that we can kind of link up on our game manager or any other objects and listen for an event and then fire off some code that we want to run.
I'm I've got my signal receiver field right here.
So, I'm going to take the game manager and just drag it down and then choose create signal receiver on player input and game manager.
It's going to create a new component on there.
If I go over to this object, you'll see that I now have a signal receiver.
I could also just remove this though and just hit add component and just type in signal receiver.
Does exactly the same thing.
It just needs to have one on there.
If I go back to the timeline, you'll see that it removed it because I removed that signal receiver temporarily.
So, it's no longer a valid OB object.
So, I just go red drag it and reassign it.
Now, I want to add a couple of signals.
The first signal is going to be when a cinematic is starting.
I want to make sure that I can stop the player from moving.
So, I'm going to do it first by just right-clicking here and choosing add signal emitter from signal asset.
We don't have a signal asset, so I'm going to choose add signal emitter instead.
That's what I meant to choose.
And then we're going to go over to the right hand side and we're going to hit the create signal option.
That's going to allow us to create a new signal that we can use and listen to for listen for in our game manager.
I'm going to create this in the cinematics folder.
And I'm going to call this cinematic started.
So now we've got a cinematic started emitter that's going to fire off or a cinematic started signal that's going to fire off right about here.
If I go over to my game input manager, you'll see that now I have a signal receiver or reaction listening for the cinematic started event or signal to fire off.
I'm going to add another one.
This time though, I'm going to do it on the opposite side on the game manager side because it does exactly the same thing and I just want to show that you can do it from either side and it doesn't make any difference.
We're going to hit add reaction here.
We're going to choose from the dropdown and instead of choosing none, we'll hit create signal.
This is kind of the way that I prefer to do it.
Anyway, I'm going to go into cinematics and we're going to rename this to cinematic ended.
That should create a new one.
And we've got now an empty list here with nothing firing off.
So now what's going to happen when we run through our timeline? Let's go select our timeline intro.
Right now we're going to fire off a cinematic started and never fire off a cinematic ended.
So let's let's go add that real quick.
Right.
Right about here near the end.
We'll right click, hit add signal emitter from signal asset, and I'm going to choose cinematic ended.
And then we're going to go back over to this game manager.
And in here, what we're going to do is just set a boolean to true or false based on whether or not a cinematic is playing.
And we'll just do that in our game manager.
So, we'll open up our game manager.
We're going to create a new boolean and a new method to set that boolean.
Let's make a public void.
Let's call this um toggle cinematic.
And then we'll put have it give it a boolean parameter.
So cinematic playing.
And then we're going to make this an expression body.
So just do the lambda statement and set a public variable named cinematic playing.
Did I spell it right? Cinematic playing equals the lower score cinematic playing.
I'm going to go over to cinematic play and just leftclick on it, hit alt enter, and generate a property for it.
That should give me a public property that's got a private setter.
And I want to make this static so that I don't have to reference the instance.
I know that there's only ever one of my game manager around.
I don't need to get into that.
So, I'm going to jump back over to our player script now and make sure that when our cinematic is playing, we just don't move our player.
To do that, I'll take all of our code inside of our move our update that's for movement.
So, I guess everything after line 82 and we'll wrap it in an if statement.
We'll say if game manager cinematic playing is equal to false, then we'll run all of this code, which looks like a great spot to extract.
So, we need everything down up to the update animation.
If we are playing a cinematic, we still want to update our animation and the direction.
I think that's probably fine.
I think the final step here is to just take this big chunk of code from line 85 down to 129.
Hit alt enter and extract method and call this update movement.
That's handling all of our movement.
And I think that makes our update method a whole lot more readable and manageable.
And it looks a lot better.
Let's do a build with control shiftB.
It looks like it works.
We'll jump back over to Unity.
Now, our signals are going to need to be set up really quick.
In our signal receiver, we just need to choose for cinematic started.
We're going to use game manager.
And let's see if I can get this onto the screen.
We'll just drag it over here.
We'll go to game manager.
And we want to do toggle cinematic, which is also offscreen.
So, we're going to drag that up as well.
Let's see.
We'll do it just like this.
So, go game manager and toggle cinematic.
And when it starts, we're going to say true.
So, we check that box.
And then when it's ending, we're going to do the same.
Game manager, toggle cinematic, but then leave that unchecked so that it sets it to false.
We'll save.
I'm going to go select that level one intro, hit play, and then let's watch what happens as I now try to run around.
And as my cinematic starts and ends.
So here I try to run.
I'm hitting the arrows going left and right.
Nothing's happening.
And I'm just going to hold this right arrow down until the cinematic ends.
And as soon as it did, you can see my player started running.
You might have noticed one other thing, though.
Let's stop playing and play one more time.
And watch what happens if I just click.
I can still shoot.
So this could also be an issue.
And I'm going to leave this as a quick little challenge.
Go ahead and make the little oneliner code change so that our blaster stops shooting when a cinematic is playing.
I'll leave you to that and then you can continue on.
We'll wrap it up and commit.
All right, I'll assume that you've done it, but if not, the fix for this is going to be relatively simple.
We don't need to over complicate it.
We can just go directly into our blaster, which is still a pretty simple script, and just fires off an object with no reload or no refresh times yet.
And inside of our use, we'll just check to see if our cinematic's playing and just not fire off if if our cinematic is playing.
So, we'll say if game manager cinematic playing is equal to false, then I'll tab in that fire statement and do the fire.
So, we'll only fire if we're not playing a cinematic.
We should probably add a reload time and countdowns and all that stuff, but for now, this should fix our problem.
We jump back in.
We'll do a real quick test before we save and commit.
So, play and then start clicking.
No shots.
No shots.
I'm clicking away.
You may not be able to hear it, but I'm clicking as loud and fast as I possibly can.
And there go the shots firing off right afterwards.
All right, let's stop playing and we'll go back into plastic and it's time to commit here.
I'll say that we added cinematic mode to the game manager using signals and we'll check it in.
Now, we're going to take a look at a couple more things that we can add to a timeline.
Let's go down to the timeline that we have and choose the plus button.
You should see a couple more options.
We've got activation tracks, animation tracks.
We're going to look at those later.
Audio control, playable, and signal tracks.
We've already done a signal track and a cinem machine track.
Now, let's add an activation track.
Let's make it so that our key appears after a moment.
So, we'll show the area and then show our key appear.
And then we'll add some sound effects as well, so we can get kind of a nice little pop when that happens.
I'm going to choose activation track and I'm going to go find my key.
I'm going to go to the environment folder.
I think I'll just take the yellow key, drag it out.
Oops, didn't mean to make it a child of the player.
Let's put it right above the player or right below.
Go back to my timeline, take that yellow key, and drop it on as the game object.
I'm going to go over to the part of the timeline where my key actually shows up.
So, that's Let's just drag the timeline over here.
So, I'm thinking right about here, about halfway after we've gotten there, I'll make the activation appear.
So, I'll grab the beginning of it and just drag it right over to there.
And now my key will appear.
And then at the end, it's actually going to watch if I drag this a little bit shorter.
It's going to disappear.
I don't want my key to disappear, though.
I want it to appear and just stay permanently.
So, I'm going to go over to the left hand side on the track itself.
I'll select it.
Let's just rightclick.
There we go.
And then allows me to get the activation settings up here in the inspector.
Really have to get this thing selected.
but it's just kind of hard to select.
Right clicking usually makes it easier for me.
But once I've got it selected up here, I can go choose the post playback state.
And I want this to stay active.
I'm just going to set it to active right there.
And now once I play past there, it'll actually turn it back on or it'll leave it as active when I actually do the playing.
Now, I also want to add a sound effect to this thing.
So, let's go to the sound effects folder or my projects and my audio folder is not really sound effects.
And I don't think any of these are going to work.
Well, I'm going to take this one from Open Game Art, this epic amulet item.
So, I'm going to download this and pull it into the project.
We'll just choose download right here.
Save it off.
And then I'll take that file and drag it in.
Now that it's imported, I'm going to rename this to key reveal so I know what this sound effect is actually for.
Go back to my timeline and go choose the timeline object itself and then choose the plus and we'll add an audio track.
We need to give it an audio source.
We'll just create one on our level intro object.
So choose create audio source right there.
And then we're going to give it the track.
To do that, we'll right click on the spot where we want it and choose add from audio clip.
This will show us all of our audio clips.
And I'm going to go find my key reveal clip.
And I want this to appear or play a little bit before the thing appears.
So you get a little sound effect.
And then it pops up right after.
So I'm just going to drag this over to the left about maybe about there.
I can figure out the exact position.
And then I want to trim this way down.
I don't need this playing sound the whole time.
Um, once we can start playing or moving around, that seems like a good point to end the audio and cut it off.
I'm going to save now.
Let's press play and see what it does.
And make sure my audio is on in game view.
We get the exit there.
I can see the timeline playing.
There we go.
And the key appeared, but the key Oh, the key disappeared.
and then reappeared afterwards.
The reason for that is that I didn't grab the the active.
I need to drag that out to the end of the timeline so that it stays active the entire time and then goes back to staying active at the end.
So here, let's uh may as well drag that sound effect out as well.
And we'll press play one more time and we're going to watch that happen.
Make sure that our key shows and stays active and and doesn't actually ever become inactive.
So here we go.
There's the view.
You can see the key right here should appear and stays there the whole time.
And we can now run around and get over to the key.
Let's go do that.
Run, run, run, run, run.
And we've got our key.
All right, that looks good.
Let's save everything off.
Make sure our timeline is saved.
go into plastic and say that we added sound effects to the level one intro.
And I also want to check in my other file because I just upgraded my Unity version.
And we'll check that in as well.
Now that we have our key and the lock there blocking the exit before we start adding some real challenges to the way to kind of block us, let's make it so that the key actually works.
Let's go select our key object.
Let's go into play mode here.
Let's see.
Go find my timeline.
Let it play.
And we'll go find that key.
And I'm going to move the key over just by hitting zero here on the X so that my player picks it up.
And I'll just run over here over to the door.
Let's go grab it or go run over to the door.
Again, moving the position of the key to zero.
Just put the door or the key right on top of me is exactly where I wanted it.
So, if I jump up here, come over to the door, I can click on it, and I can turn this thing on and off, but that doesn't let me get through.
So, I want to make it so that I can actually walk through this object.
To do that, we're going to add in something new to the toggle locks.
And I think that this is also another good opportunity for a challenge.
If you're up for it, go ahead and try to figure out an easy way that's reusable that you can fire off some code or do some action whenever the keys are unlocked or whenever the toggle locks are unlocked.
Don't worry about when they're locked.
Just worry about the unlocked state for now.
If you can figure that out and make the keys just dis or not the keys, the locks, that little wall there just disappear, you're good to go.
If not, don't worry.
We're going to go through the solution in just a moment.
All right.
I'll assume that you've gone through it or that you're just ready to do it.
So, what we're going to do is find our toggle lock.
Let's go find the actual object here, this yellow lock, and I'm going to open up my toggle lock script.
We're going to add in a Unity event so that we can do whatever it is we want whenever one of these toggle locks is modified and we don't have to add new code every single time.
So, right up at the top, we're going to add a Unity event.
We'll make it a serialized field of a Unity event and we'll call this on unlocked.
We're going to add in a using statement for that Unity event.
So I'll click on it, hit alt enter, and it's going to add using Unity.events.
Make sure it didn't add a different using statement up above.
And then down below here, we're going to add in a call to this on unlocked whenever we toggle and turn it off.
So, right after we change the sprite renderer, let's just say if unlocked, then we want to call on ununlocked question mark invoke.
That's going to fire off or invoke all of the things that are registered for the onunlocked event in the inspector.
And it the question mark again is going to make sure that it won't give us an error if there's nothing registered.
Without that, if there's nothing there, we could theoretically get an error from the invoke call when there's nothing actually registered for it and listening.
Now, let's go add something so that we don't have to worry about that either way.
We'll go back into Unity and on our toggle lock, we now have the on unlocked field here.
And we can hit plus, just grab our own object.
It doesn't matter which one of these components I drag in.
Just drop any component on.
go over here and choose game object and set active and leave it set to unchecked.
That's going to turn this yellow lock off the second I try to use it.
Let's hit play.
And then again, I'm going to just cheat and move my key over.
It's always important that you uh do lots of cheating in your own game development so that you're not sitting around waiting for stuff.
So, find our yellow key.
There it goes.
It appeared.
We'll hit zero.
Move it over to us.
Run over here.
Jump up.
Trying to avoid those spikes in that frog.
Come over here.
Jump over.
Come over.
Click.
And there we go.
The door is open.
And I can walk through and continue on to level two.
So, let's go into plastic.
Make sure that we've saved our scene so that toggle locks now fire unity events and level one can be passed.
Two S's there.
And check in.
Now, we're going to make a boss.
We're going to use this little bee here, and we're going to hook up a couple of his attacks, set up a whole environment, and make a bit of a challenge for our player.
We're also going to use some cinematics to introduce him.
The first thing we're going to want to do is make sure that you've committed to source control because if you didn't, and you have any kind of mistake here, you're going to end up breaking your player's character controller and really wish that you had source control so that you could go back to it.
So, we're going to take the bee and fish package.
You should be able to download that and drag it into our project.
You see here that it's got a bunch of animations for our bee.
And it also has a bunch for the fish.
It's got some prefabs for some of the special effects, the lightning, the explosion, and some bullet spikes that can fly off of the fish.
But there's also right up here, if I look and find the correct spot, there are all of the character animations.
I want to remove those.
Uncheck those.
And then there's an animator controller that I'm trying to find.
Ah, there it is.
The robot character controller.
If you don't uncheck those, you're going to need to go back and undo your changes.
is you're going to want to go back and revert that so that you don't break and lose your character controller setup.
Let's hit import now.
And now I should see all of my things.
Now again, if you messed up, you made a mistake, you can go to your plastic window, go to change sets, and then scroll to the wind the last change set.
So it' be this toggle locks one.
Right click and hit switch workspace to this change set or revert to change set.
And it'll undo your changes.
Revert will actually undo your pending changes.
Switch to will require you to actually locally undo your pending changes.
So, you probably want to hit revert to and it'll take you back to that past version.
If that gives you any problems, you can always go over here, hit the little gear, and hit launch plastic SCM and then do the same thing in there.
It tends to work when it occasionally fails in here, although most of the time it just works in here as well.
All right, so now we've got our B imported.
Let's go find them.
If we go to the prefabs folder, you should see that there's already a B prefab object set up and made.
I can grab it and drag it right into my scene and put it right around near the key.
And by the way, when I said this was set up and made, this is the way it came from the artist.
It's already set up.
It's just with the animations on it.
We're going to flip the rotation now so that it's facing the correct direction.
I want it to face towards my player.
So, just go find the rotation and set that to 180.
And I'm going to rename this object to B root because I'm going to need to be able to move this piece around and reference a whole bunch of different parts of this B object.
Now, I don't want my B to be there initially.
I want my B to appear when my player gets close.
So, I'm thinking my player comes over here, they think it's all clear.
It's nice and easy.
Run to the key.
They get right here and all of a sudden a B pop