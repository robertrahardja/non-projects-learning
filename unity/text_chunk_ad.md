e not just pulling and updating every frame, and we can actually tell when our health changed, we can do some cool little things with that, like give the player some extra indication, not just audio, but maybe something visual in our panel.
I want to add a little flashing part to our panel that just kind of highlights that our health has changed and show you something else really cool along the way.
So, let's go find our player canvas and then our player panel.
And then I'm going to expand out and find the hearts object.
We have this image here that I didn't disable.
And if I turn it on, you might see that little outline that appeared.
But if I change the color to a nice bright like a red and then crank that alpha up like that so that the alpha is at 255 and it's not transparent at all, then it's very obvious.
If I click that on and off, you can see it becomes very, very clear that there's a big giant red flashing thing there.
And I definitely took some damage.
So, what I want to do now is make it so that when I take damage, this turns on for maybe half a second and then turns back off.
So, it's a little bit of a flash.
We could, of course, do something cooler and flashier and fancier, but I think that something simple like this with the code is going to give you a lot of opportunity to just do whatever it is that comes to mind.
So, let's take a look at our player panel and we're going to open up our player panel script and give ourselves a reference to that little hearts panel or this hearts image here.
So, let's go to the player panel.
We'll open the player panel script and right up at the top, let's duplicate line 11 and get rid of the array and let's rename this.
Instead of being hearts, let's call this flash panel something or let's call it flash image.
Make it a little bit more obvious what it is.
So, it's not an array.
Okay, there's only one image.
We could have multiple.
We just have to loop through all of them and turn them on and off.
But I've just got this one here.
So, I'm going to copy it.
Scroll down into our update health part.
And then on line 32, so after 31, we'll add a new line.
I'm going to kick off something called a co- routine.
And this is going to run code over multiple frames.
It's going to allow me to run something now and then do something else in half a second, which turn the sprite on and then turn it back off.
So we'll do that by calling the start co- routine method.
We need an open parenthesis.
Then we need to give it the name of our method.
I'm going to call this flash um image.
Well, let's call flash UI.
No, let's just call this flash.
I think that's good enough.
We'll add our open close parenthesis and a semicolon.
Alt enter and generate a method for it.
The return type of this doesn't want to be string.
It says string by default and it's going to generate that.
But we need to change this to an enumerator.
It's important that you don't get the enumerable which is another one that's easy to autocomplete.
You want I enumerator.
That's what a co- routine must return.
We'll remove the private keyword because we don't need it.
And then if I get rid of this throw, we'll suddenly get an error saying that flash does not return a value because it needs to return an IE numerator.
and it does it in a very weird way.
I'll show you the syntax.
We'll talk a lot more about co- routines as we go on, but you'll get familiar with it really quick.
The first thing that we want to do is update our health image.
So, flash image enabled equals true.
I said update, I meant enable our our flash image.
So, I pasted in my flash image that was already on my clipboard.
Did enabled equals true.
Now, we want to wait for half a second.
And to wait in a co- routine, we do a yield.
So we do y I e l d return and here we need a wait for seconds.
So we have to do a new wait for seconds and then open parenthesis and we want to give it the number of seconds or the amount of time.
If I do 0.5 that'll be half a second and I can add a semicolon, but it's going to give me an error because it only takes a float and 0.5 is a double.
It's a really weird kind of thing if you if you're not familiar with game math.
um and all this stuff.
It's essentially an optimization to make things much much faster.
Uses these floatingoint numbers to go faster and it gets a little bit confused on the type.
So if we put an F here, it'll know, hey, this is a floatingoint number.
It's fine.
Go ahead and use that and don't give me the error.
So that that'll fix the error.
The last thing we want to do is turn the flash image off.
So I'll copy line 27, paste it down here on 39, and put in a false.
Now, it's worth noting that you can save off and cache this wait for seconds object.
It's something that you can um reuse multiple times.
It's another optimization.
I'm not going to dive into that though because it's not something that we need to worry about yet.
And right now, we're focusing on the co- routines and the way they work.
So, we kick off the co- routine after we update health.
Our health UI updates, the correct number of health is there.
We start this co-ine flash, which on the first frame, right when we call it, is going to enable this image.
Then it's going to say, "Hey, now I'm supposed to wait half a second." The game is going to keep running and then half a second later, it'll resume on and run the next code and end it.
If we call this in between, so if we take damage and then we take damage again before this has happened, it's just going to restart and go back up to the top and we won't have to really worry about any problems.
So, let's minimize this.
Go assign our panel, our flash image.
So, I'll take the hearts here.
And actually, I think what I'll do is go into prefab edit mode.
We'll assign the hearts in prefab mode.
So that way it gets assigned on both of our objects.
We'll go back out of the player panel.
Hit save.
And now both of our player panels should have their own hearts object selected.
And then we'll press play.
Let's run over there.
Take some damage and see if we get a nice little flash.
Oh, I should have changed the color of that hearts panel on player two though.
I don't don't think I did that.
So run over here.
Boing.
Take damage.
And you can see got this nice flash appearing.
I can definitely tell that I took some some damage and I'm I'm probably dying.
So, let's stop playing, go into our plastic window, and say that we added a flash co- routine to the take damage interface.
Well, it's really to the take damage user interface.
It's I don't know if I like that commit message, but it's good enough that I understand what it means.
Oh, we need to save our scene.
Let's save the level.
We didn't really need to save our scene because it's prefab in there, but I want to save it anyway because it was starred.
And then we'll check in the changes.
All right.
So, hopefully you're starting to understand how to use these co- routines, by the way, and you can experiment with them a little bit on your own.
Maybe do some other flashing, some other things.
You could flash the the heart that's showing up there or whatever it is that you want.
Make a a slightly different interface for it.
But I think that hopefully you're starting to see some of the benefits of events so that you can get notified when something happens and do something when something happens.
And it doesn't have to be just UI stuff.
We're going to be using events for a lot of other things in the near future.
Now that we have some game data, not a whole lot, but some.
We're going to go through the process of building out our load and save game system.
We'll start with it just dealing with the player and then expand on it so that it can save and load all of the things in our scene later.
But first, we need to take a look at one thing in our workflow.
I'm going to hit play real quick, jump in from the menu, and I'm going to show you an error that you may have already seen, but if you haven't, it's important to see because it's going to be part of our workflow adjustment.
Here, we're going to go to the console tab with with it playing.
I'm going to go into level one.
I'm just going to run over here, jump a couple times, and let this thing kill me so that I can get back to my menu.
in a second.
Now, one more jump.
There we go.
And then I'm not really worried about these two errors right here.
These aren't something that we need to worry about yet.
There's something with the input system.
What I'm worried about is that I just clicked anywhere on the scene and we got an error here saying null reference object not set to an instance of object.
And here it's inside of our player.
So, the reason I care more about this one right now is because it's in our actual code.
These other ones are in the input system and we're going to be dealing with that along the way.
Now, if I click one of the level buttons, you'll see that the game still works even though that error is there.
So, you may be getting this error.
You may have not noticed it or it may just be there and seem like it doesn't matter, but there is something going on.
So, let's take a look at it real quick.
I'm going to open up the code by double clicking on the error and see that it's on line 49.
And here you see that it's trying to access our player canvas.
It's trying to find a player canvas and bind to the player canvas.
And the reason that that's failing is that if we're in our menu, let's die real quick and go back to the menu.
If we're in our menu, there is no player canvas.
So, there's nothing for it to bind to.
So, as soon as I Let's clear the log out.
Soon as I click and add a new player, the player gets created.
It's up here in the menu scene, and it's getting an error because it can't find that canvas.
So, I want to make a change.
I want to make it so that our player input manager doesn't join players in the menu.
And I also want to make it so that our player input manager and our game manager are available in the menu from the start so that we don't have to go into a level and load it because we're eventually going to need our game manager for loading and saving games.
In fact, that's the key reason that we're going to go through this process.
So, let's stop playing and we're going to go find our prefab for the player input and game manager right here and drag it into the menu scene.
I'll save and then we'll switch the join behavior here instead of it being join when a button is pressed to join manually.
I'll save one more time.
Press play.
And now, guess what's going to happen when I click the button and join in? Well, you'll see in a second.
If you if you guessed, cool.
If not, then uh watch.
So I click, nothing happens.
That's good.
Even though I've got the player input manager and game manager here, not getting an error.
But if I click level one and I get in um I've got my player here, that's all good, too.
Then finally, if I try to join in with a new player, though, I can't.
And now the reason that my player one is working and player two can't join in here is that if I look inside of level one, let's stop playing.
Go into our level one scene.
We have a player already placed here.
We have player one already placed in the scene.
So, he's able to spawn.
If I delete this player from my scene and save real quick, I'm going to undo that in a moment.
So, you don't need to do it.
Let's go press play.
And then if I jump in and hit join on level one, you'll see that I don't get a player here.
And the reason for that is that we now have to do our manual player joining.
And you can even see that my camera isn't updating since I don't have a camera.
I'm getting some things from the UI and that's it.
Everything is no longer updating.
I'm no longer getting updates after the the load completed and the old camera unloaded.
So, we need to make a change here.
We need to modify our code so that the player input manager can join players on demand.
And I want to undo that change to level one so that I have a player there placed where it's placed.
So, that's kind of my starting point when I want to just jump in and play on level one.
So, first thing I'm going to do is go to plastic SCM, find level one here that I just modified and changed, and right click on it, and hit undo changes.
That's going to undo the save that I did where I deleted the player.
So, if I go back to level one, I now have a player in it.
Then, I'm going to go back to my menu scene, find my player input in game manager, and what we want to do is modify our code so that join behavior switches to join on button press if we're not inside of the menu.
And we can do that using the game manager script.
So let's open up the game manager and inside of our awake right now we get the player input manager and we register for the onplayer joined event and then we essentially bind up our player whenever a player joins.
So we've got a player input manager here and we're going to need to reference it again to modify its join behavior.
So instead of calling get component a bunch of times or multiple times, what we'll do is cache and save our player input manager.
So, I'm going to add in a new line here right after the right before the dot in the parenthesis.
Add some space here.
And I'm going to say underscore player input manager equals get component player input manager.
So, that's line 20.
I'll hit alt enter and generate a field for it.
Now, we should have a field for our player input manager.
It looks like it went down here.
I'm going to move both of these up to the top because I don't like having my fields down at the bottom right below my static instance.
And let's add one line of space in between them.
And then finally on line 27, or I'll copy line 25, paste it right here in front of 27.
So now we get the player input manager and save it off into a variable that's private.
I'll get rid of that private keyword since it's redundant though.
And then we register for the onplayer joined event.
The final thing that we need to do, let's clean that up, is register to our scene manager to get notified when we load a new level.
Whenever we load a new level, if the level is the menu, we'll set it to manual join mode.
If the level is not the menu, then we'll set it to click join mode or press button press join mode.
So to do that, we need to go down or add an extra line here and reference the scene manager static method or static event which is scene manager.
And notice that it's not autocompleting.
What I can do is hit alt enter and get the using Unity engine scene management statement up at the top.
So I'll hit that.
Go up to the top and you can see that it added using Unity engine.
Management.
You can always just type this out if it doesn't auto add.
This is going to give us access to all of the scene management methods and classes.
And the one that we care about is the static event on here which is the on or no I think it's scene loaded.
That's it.
Not on scene loaded.
It's just called scene loaded.
So, I'll hit enter, let it autocomplete the text or the the casing there.
It's got a weird casing, not the casing I would typically use.
Um, but that's the that's what it's got and we can't change it.
So, it's got scene loaded with a lowercase s and we want to do plus equals because just like on player joined.
This is an event that we're registering for.
Remember, we just did our own event just a moment ago.
Same kind of thing.
We want to register so that something gets called every time a scene gets loaded.
Let's call this handle scene loaded.
We'll hit alt enter and generate a method for it.
It's going to give me a private void method that has an argument arg named arg0 which is the scene that got loaded and then another argument for the load scene mode which will tell us whether the scene was loaded additively or if it was loaded to replace the current scene.
You can do it two different ways.
We haven't talked about additive yet so you can pretty much ignore that for now until we get into it.
Let's delete the private keyword because we don't need it.
And on line 35, what we want to do is check the name of arg0, which is our level name.
So I'll say if argname and here, let's say arg0 dot and you can see all of the different things, the fields or properties that are on the scene object.
So arg0 is a scene.
They just name it arg0 because that's the default when it's autogenerating.
So, we've got the is subscene option, the handle for it, the root count, um, couple other things.
Let's scroll down.
We've got the path, the name, there's a build index somewhere, right there, build index, which is that index in the in the build settings.
You see it starts at a zero.
We want the name though, so we're going to check if the name is equal to, and we want menu with capital M.
It needs to match the scene name.
If it is the menu, then we want to tell the player input manager that it's load or join behavior.
Where's that at? Join behavior is equal to.
And here we want it to be the manual one.
I accidentally did this backwards the first time I did it.
Now, if it's not the menu, we want to do an else, which is going to run if this is not true.
So, if this is true, we'll get line 36.
Otherwise, we'll get whatever's after line 37.
And on line 38, we'll say player input manager jojoin behavior is equal to.
And here we're going to use the button pressed, which is what we had before.
I'll save that off.
Do control shiftb to get a build.
It looks like it succeeded.
And then we'll jump back into Unity and let's see if we're able to go through the entire flow of joining a game, getting through it without that error popping up anymore.
So we press play.
We've got our player input in game manager.
I click a level.
Join.
Looks good.
I can run over here.
Let myself die.
Let's see if it all works.
Notice that that other error message is gone, too, because that was in the player input manager trying to join.
There we go.
I'm in the menu again.
I can click all around.
I can click on my controller here.
Everything looks good.
I can go Let's go into level two.
And we have no more errors.
I can join with the second player once I'm in the level.
And things seem to be working good.
So let's stop playing and go commit our changes into plastic.
So go over here.
We don't have a lot.
Just our game manager and our menu that we fixed player input manager to support running on the menu scene and we'll check in the changes.
Now that we have the game manager in our main menu, we're going to go through the process of setting up a new game button and the ability to load existing games.
First though, let's create the new game button so that we have a UI element that we can hook up to this game manager to kick off a new game.
And then we'll dive into how we're going to structure that data.
So to start, I'm in my menu scene.
I'm going to take my canvas and rename this to level select canvas because that's what it's covering right now is a background and some level select stuff.
I'm going to rename the image to background and then I'm going to select the level select canvas.
So just click on it and duplicate it with control D.
I'm going to select the initial one, the first one that I had and just disable it.
So now I've got this new one here that's just an exact copy of the previous one.
I'm going to rename this to new game canvas.
And then we'll expand it out.
I want to move this level one button or just recreate it and make it into a new game button.
And I'm going to delete the level two button.
So I'm going to go to level two, delete that.
Rename this level one button to new game button.
And then I want to center it kind of let's just do it right in the middle of the screen for now.
And let's make it twice as tall because I want it to be pretty big.
And then let's change the text to say new game.
Now, we could of course just go in and recreate this manually, but I find it a lot easier to just duplicate and go through the process and speed this thing up.
Or well, just not go through and manually recreate all of the buttons every time.
Let's adjust the max size here.
I'm going to put this down to about 150 so that it fits in there pretty good.
I've got my new game button and I think I want to just drag this up just a little bit.
Actually, let's let's dock this to the top here.
Alt.
Oh, sorry.
Got the wrong object selected.
We'll go grab the button.
And I'll just grab the position Y.
Let's just drag it up here.
I'm gonna put it right above that little guy's head.
You can put it wherever you want on your screen.
I just didn't want it covering up this guy's head.
So, we've got our new game button here, and it has a load level button script.
I'm going to remove that component, and we're going to add a new script.
That'll be a new game button.
So, we'll right click in our scripts folder.
Here, I've got the scripts folder selected.
Rightclick, create a new C script.
Let's call this new game button.
Again, no spaces.
Capital NG and B because we're using our Pascal case for class.
We'll open up that new game button.
That didn't open it.
Oh, there it goes.
It opened up.
And in our new game button, what we're going to do is first delete the update method.
And then we're going to register for our button click.
And on a button click, we'll tell our game manager to fire off a new um a new game essentially.
And there are two ways that we can do this.
The first way is let's create a public void method named um start or let's call this uh create new game.
I I like that better.
I don't want to have the word start in there.
And then in here we can call game manager.instance new game.
Now the instance exists but new game does not exist on our game manager.
So we'll click on it, hit alt enter and generate it.
We don't need it to do anything yet.
We just needed this to be our hookup for it.
Know that hey somewhere in that game manager in this new game method will create the new game.
We'll we'll deal with how we do that later.
For now, let's deal with hooking it up.
So I'm going to save.
We'll save our game manager script as well.
In fact, let's go down to that new game method here and write out a log.
We'll say debug.log new game called just so that we know that hey new game was called.
I'm going to make this public as well just because I don't like the internal keyword.
And I'm going to get rid of this private keyword too because I just realized it was there and I don't need it.
And the private keyword is the default.
So it's kind of redundant to have it there.
Let's go back to the new game button.
So we've got this create new game method here.
And we need to hook this up in the editor.
Let me show you two different ways that we can do this though because I think that it's important that you understand that there's one way to do it and then there's a completely different way to do it that you're going to see many many times that might also sometimes be better.
So let's go into Unity.
We'll go find our new game button.
We'll add the new game button component to it.
That was already searched for.
And then in my button script here, if I expand that out, that's the one that was created automatically when I made a button.
We have this on click.
And right now it's got an actual value in here that's missing.
If I hit minus that'll go away and it'll say the list is empty.
The reason that that was missing is because it's referencing an object that's not there anymore.
So what we'll do is hit plus and then I can take my new game button and drag that right in here.
Technically it doesn't actually matter.
I could drag in this button or anything else.
It's really just referencing the game object.
It's referencing this specific thing when you drag that in.
any component will do that cuz then when you hit the no function button, you'll get the popup of all of the components.
So there's the game object, the wctck transform, which is the thing up way up the top, the canvas renderer, the image, and the button, and this new game button.
All of them have things that we can access.
Like I could turn off the game object.
I could game object and say set active and set it to false.
Then when I clicked, it would just turn this game button off.
Let's let's do that real quick.
Let's just hit play, disable this button, and watch that happen any second now.
There we go.
The button turns off.
Not what I want to do, though.
But I can register again anything.
What I want to register instead is new game button and choose the create new game, which was just off screen, of course.
So, let's go try that one more time.
So, new game button and create new game.
Now, this will call the create new game method.
Let's try it out.
Any Any Any second.
Load it up.
Load it up.
We should see it in our console log.
When I click it, new game called.
That worked.
Great.
So, now I want to show you the other way that you can register this so that you don't have to go into the UI and hook these things up kind of more manually, the way that you can do it from code.
So, I'm going to remove this registration.
We're going to go into the new game button script.
And inside of the start, we're going to say get component.
and we're going to get oops I spelled that wrong.
We'll get the button component.
And if that doesn't auto add the using Unity Engineui up at the top, you'll need to go up there and add that or hit alt enter on it.
It just kind of auto added it as soon as I typed it.
You might have noticed that.
And then we want on this button to add a listener to the onclick event.
So it has an on click here.
We type O N with a lowercase O and then do a dot and we can do add listener.
What this will do is allow us to pass in a method that we want to be called whenever they click, just like if we did it in the inspector.
So here I just put in the name of my method, create new game, and add the semicolon.
Oh, I've got to put a W in new.
There we go.
Put a semicolon in.
Save.
Control shiftB.
Do another build.
And now if I jump into Unity, I'm going to get the exact same behavior, but now I don't have to write in these on clicks.
I find that this is really handy if you have a script that's specific for like a button or something else that needs to use a button and is going to register for this so that you don't have to go through that extra process of hooking it up and you don't have to worry about going in and checking it later if that registration gets somehow removed by a designer that's doing something else.
Plus, it's important to note that they can still add in extra clicks here.
So, I can click and get that new game called, but I can also have my designers go add something in here, like maybe they um let's say that when they click it, I'll do something stupid like change the text color.
They select the text and let's find our color.
Where's that at here? There's There's so many things here.
We'll just find the Let's find the alpha.
There we go.
And we'll set the alpha to well, maybe 100.
So we click let's go to there we go.
It's it's zero to one.
So we got a 0.5 or a 0.1.
There we go.
The text alpha went down to 0.1.
I can set it up to a 31 which is just going to be a one.
So you kind of get the idea.
We can add in extra things here without having to worry about them breaking the functionality of that new game button.
All right.
So now that we've got our new game button in, let's save our scene.
Go into plastic and say that we've added that.
and we'll get ready to modify our data structure next.
So, added new game button to main menu and hooked up in code.
We'll check that in.
Now, we're going to dive into our data for our saved game so that we can start saving them.
In our game manager, we've got the new game method that just right now logs out new game called.
We'll leave that in for a moment, but let's think about what needs to happen when we create a new game.
The only data that we have right now for our game is our player datas.
If I hit F12 on it, remember that's a list of player data objects.
And the player data objects right now store the coins and health.
We'll of course store more information with these later.
But these are the two things that we care about right now that we've actually saved off.
So we need to save our player datas into some sort of structure or some sort of format that we can reload later.
And then we need to be able to create a new set of player datas when our player chooses new game.
And what we want to do here is bundle these player datas and all of the future stuff into an object that'll store all of the data for our game.
And we'll call that a game data object.
Let's go to the player data class.
I'm going to control-click on it.
And right below player data, I'm just going to add in a new public class called game data.
We'll add on a list of player datas.
a public list of player data and we'll call this player datas and initialize it to a new list by default.
With that, we'll add the serializable attribute so that we can see it all in the inspector and so that we can serialize it in just a moment.
And then we'll go back over to our game manager.
Our game manager has this list of player datas.
And I want to get rid of this now and replace it with a single game data.
So, we'll get rid of the list of player datas here and just put a game data_ame data.
That's going to give us some errors.
And I find that one of the best ways to figure out what code needs to be changed is to do a control shiftb and do a build and get all of my errors down below.
It'll tell me the spots where the code no longer works because I've deleted something.
It says here the name player datas does not exist and does not exist and does not exist here.
See, it's on line 52, 55, and 57.
But I don't need to care about that.
I can just double click on them to go to them.
So, we don't have our player datas anymore, but we do have a game data that has player datas on it.
So, instead of calling player datas, we'll call underscoreame data data data dot player datas.
So, you see that now we're referencing the player datas on our game data object instead of a list in our game manager.
We'll copy this game data.player player datas, put it on my clipboard with control or command C, and then paste it over these two remaining player datas.
I'll hit control shiftb.
My build is successful, and my data should still work exactly the same as it did before, but now I've got it wrapped into this game data object.
Let's just go verify that real quick.
Make sure that I've built, go into Unity, we'll press play, and we'll hit the new game button.
Oh, the new game button right now doesn't load us into a new game.
So, let's just play.
make sure that we don't have any errors at the very least.
Looks good.
And then let's go hook it up so that our new game button throws us into level one.
We'll go into the new game button.
Go to the new game method with F12.
And right after we call the new game called log message, let's say scene manager.load scene.
And we're going to load level one.
Now, if your scene manager doesn't show up, of course, make sure that you go up here and you got your using Unity Engine.cene management statement there.
This got automatically added.
So, you want to make sure that if it doesn't auto add, you go add it up there at the top so that it turns blue and you don't have an error.
All right.
Now that I've got my load scene, let's just go in and play one more time.
Make sure that our data looks good.
And I get a player that has six points of health and no coins when I start a new game.
Let's check that out.
That's what I expect to see.
So, I load up.
I've got six health.
I can take some damage.
Let's go get a coin real quick.
Got four coins.
Let's go into level two.
Got five health and four coins.
We'll go back into level one.
Five health and four coins.
I should be able to die now.
Let's let ourselves die.
And he says now four.
Boom.
I'm dead.
And now if I hit new game, we come back in.
And well, I've got four health and I've got well actually I've got no health, sorry.
And four coins.
So my new game isn't clearing out or resetting our player data.
And that's our next step.
So let's go into our new game called method.
And right here before we call our load scene, let's say underscore game data equals whoops equals new game data.
So, we're going to be creating a new game data object whenever we call new game, which makes sense, right? We're creating a new game.
We should be creating a new object for that data.
So, let's minimize our editor again.
Try it one more time.
And now, we should expect to see that when we hit new game, we get a fresh character.
But when we kind of bounce between levels, we have our same character data.
So, we hit new game.
We'll go uh grab a coin.
Switch levels.
I'm at six there.
Let's go switch levels again.
We'll go take some damage.
Let's see.
Three.
I'm just going to go into level two again.
We're just going to make sure everything is good.
Looks right.
I've got my three health and my six coins.
And if I go over here and die, we should get right back to the menu.
And then new game gives me a fresh character with no coins and full health.
I can bounce around and I've got the same thing happening.
That's a seven, guys.
A seven looks a lot like a one.
All right, so now we can see that things are working and the new game system is starting to come together.
Next up, we're going to have to figure out how to save and load.
So, let's go into the project or the plastic SCM window.
So, we've set up a new game system.
Um, well, game data and new game system.
Added game data and the new game system is hooked up.
And we'll hit check in changes.
With our game data in place, it's time to dive into saving and talk about how we're going to save data, how we format that data and how we can store it off locally, what we can do with it.
So, let's start by taking a look at our game manager script.
I'm going to go into the game manager and what we're going to do is add a save method.
We'll talk about how this works.
We'll implement it and then we'll dive into the actual data.
Let's go into the scene handle scene loaded and right below our else statement.
Well, two lines below so that it's not included in the else statement.
Let's say save game with an open close parenthesis.
We're going to call a method named save game that we're going to generate right now.
Let's hit alt enter on save game.
Create a new method.
I should get a private void method right here.
I'll delete that private keyword.
Again, it's just redundant.
And then delete that throw exception because we don't want an error.
we want to actually save our game.
So, the first thing that we need to do when we save our game is determine how we're going to serialize the data.
And serializing data is essentially taking data that's in our game or in memory and converting it into some sort of savable format, some sort of text format or a binary format that essentially looks like text.
It's characters that you're just not going to be able to understand.
We're going to start with the JSON format though because it's one of the most popular ones.
It's one that a lot of people are familiar with.
It's extremely easy to understand and debug and it just gets the job done for most things.
So to do that, we're going to use the JSON utility method or the JSON utility class and its convert method.
We'll do this right here on line 45.
And I'm going to say string text, which is going to be our JSON text, equals JSON utility.
You can see it auto completing capital J and a capital U dot to JSON.
And we want to pass in our game data.
Not game manager, but our game data.
Because our game data object is marked as serializable.
If we go to the game data here, it's got that serializable attribute and our player data has a serializable attribute.
The JSON utility should be able to convert this over to a bit of text that's formatted that we can understand and that the computer can understand to reload it later.
Now, let's go down one more line and say debug.log and we'll log out that text.
Let's save.
Go into Unity and see what this does and then take a look at that data in another tool real quick.
So, I'm going to minimize.
We'll press play.
And then as soon as my game starts, we should get our new game called.
And right down here, you can see my log that looks a little bit weird.
It's got some brackets says player datas coins zero health six.
If I select this line, and I just copy this first part right before the debug log, the second line, I don't want that second line.
Just copy this line.
And I'm going to go over and find myself a nice JSON formatter.
Got a whole bunch of JSON formatter options.
I'll go select the first one and I'm going to paste in my JSON data.
JSON, by the way, stands for JavaScript object notation.
It's something that's used a lot in JavaScript code, obviously, but also just in networking, um, sending data across and for storing and saving and serializing data.
So, here's the formatted version of my JSON.
You see that we've got the braces here and this is kind of the outer game data object.
Then underneath it, it has player datas and I can collapse or expand that.
And it's got one player data object.
This right here is the brace for the single player data that I've got that has zero coins and six health.
Let's go in and make some changes to find some more things.
Go maybe get another player in here.
Run over here, get a couple coins, and then I'll even take some damage.
And then we'll load another level.
Let's do that.
So, we'll take some damage or here, let's I'll let myself die.
We'll get to the main menu.
I'm going to clear out my log.
So, I got nothing in here except for my new entry.
There we go.
I've got my player data entry.
I'm going to copy this top line.
We'll go back into Chrome.
Go back to our JSON formatter.
We'll go back and paste this JSON in.
And now you see that I've got my player datas, but I've got two objects underneath it.
my first player and my second player.
And each one has their data.
The first player has eight coins and no health.
The second player has zero coins and six health because this player got himself killed.
This player never picked up any coins.
All right, let's minimize.
And now that we've got our data in the right format, let's talk about how we can save that data out.
So, we're going to go back into our code.
And right here on line 47, we're going to use the player pref system.
We're going to do this as an initial one.
Then we'll talk later about some other ways that you can save data.
But the easiest way, the way that works across just about everything is to use the player prefs set string.
And then we need to give it a name for our game or a name for our data that we're saving off.
So I'm going to call this game one with no spaces right now.
And then we'll add a comma and our parameter that we want to save off, which is our text, which is our just our JSON saved text data.
So, this is going to save all of our game data off onto our system locally.
Let's save.
And it's going to save it all into this game one.
So, every time we save, we're going to be resing over the existing save game.
Let's press play, see what that does and where that data is, and then we'll talk about loading and all of the other things that we need to do for this.
So, let's play.
We get in, we press the button, we've got some saved data, and it still wrote out the same log.
But where did our actual data go? Let's take a look on Windows.
First, let's go to our project settings.
We'll go to edit and we'll find the project settings here and select the player settings.
And we need to make sure that you know your product name.
This should also be what's up at the top, but you've got your company name here and product name.
Don't change them now because we just saved data.
Just copy out your product name and let's open up the registry editor.
If you search for reg, you should find it.
If you're on a Mac, there's slightly different instructions and I'll put the link down there for the instructions, but you can essentially find this data in a folder on a Mac just the same.
So, here I've actually already found it in my registry, but let's just go back here and do a quick search.
So, say you've just opened up your registry.
What you can do is hit find and then put in the name of your project.
Hit find next and you should have your project appear pretty soon.
Now you might see first a couple things about um most recently used applications or something like that.
So let's let it search find our data and then we'll view that data, take a look at it and make sure that you're able to find yours as well.
Again, if you're not on Windows, it's going to be in a different location and that location is going to vary from device to device.
So let's actually let's pull that up while our search is running.
So here we've got there it is the player prefs data.
So you can see on MacOSS it's stored in the library preferences folder in a file named unity company name which is going to be that default company unless you changed it.NameP list and then on Windows it's in our registry.
On Linux it's in this uh folder Windows Store apps and Windows Phone apps.
They're all in totally different places as you can see, but that data is available on the page and we'll link that below.
So here we've got our first thing.
Oh, the most recently used app.
So it's just showing us that we've run Unity with that.
It's it's got that stored off.
So I'm going to hit the button again, search a little bit more.
Now, you can also just browse directly to the location, but I find it's usually just easier to search for it um than to expand it out, especially when I'm explaining it to people.
Having to explain the difference between current user and current machine and all that stuff um and then the weird structures that are relatively arbitrary in the registry seems confusing.
So, we'll let it keep searching and any second now, it should find our project with the um the save game data.
So, any second now, come on.
searching, searching, searching.
And here it is.
So, it found my alien blaster under default company under Unity editor under Unity under What is this? Let's just go.
We'll go collapse it all down real quick.
I just want to make sure that we find it.
We can see it.
So, oh man, this is Oh, here's here's where we can find it.
Let's go select it.
Alien Blaster.
So, you can see the full path to it is actually right up here.
That's the easier way to see it than trying to expand and collapse.
So, what do we have in here? Well, we've got our game.
Oh, where I accidentally renamed it.
I put a space in mine and then resaved it.
So, it has game one.
And if I double click on it, you can see it's got our data here.
Here's the binary version of it or the hex code version of it.
And here's the text.
It's got that player datas, the coin, and the heel stuff.
So, that's where it's saving our stuff.
And now, what we're going to do is save out multiple games and start reloading them.
Let's go back into Unity, though.
I don't need reg edit open anymore.
I don't need to see that.
Just wanted to show where it was.
And then let's figure out how we're going to do our loading next.
Back in the game manager, let's add a load game method now.
So, we're going to go to right below our save game, add a void load game, and we're not going to take any parameters yet.
Instead, what we'll do is call player press.get string.
And we're going to pass in game one.
I fixed my game one so that it no longer has a space.
And we're going to assign that to a string.
So we'll say string text equals player prefs.get string and passing game one.
That's going to give us back this JSON that we just saved out.
Now to convert that JSON into a game data object again, we'll say underscore game data equals JSON utility.
And instead of using two JSON, we'll use from JSON.
We give it the type.
There we go.
it's going to autocomplete and just work.
So, first thing we're giving it here is the type of object that is in the text, which is a game data.
If we put the wrong thing in, it's going to give an error and not be not know what to do.
And we do have to specify it because this method doesn't know from the text what that object type is.
Then, we give it the parameter of the text and it's going to convert that into a game data object.
Now, we need to hook this load game method up.
So, let's make it public.
Save it off.
And then we'll go add a load game button.
So, I've got my new game button.
Let's go open that new game button script.
I'm going to delete out this comment with shift delete.
I don't need that extra comment in there.
And then let's turn these into expression body methods.
And then create a load game button as well.
So, I'm going to go to line nine, hit alt enter, hit to expression body method.
Because it's a oneline method, it just shortens it down.
Doesn't need these braces.
That's all it's doing is saying, "Hey, this method only has one line.
Don't add the braces." Just put it onto one line.
Make it nice and simple.
Do the same for the create game.
And again, you put it right before the right after that first brace, and it'll give you that popup option.
Or you can just manually type out that statement.
So, I've got my new game button, and I want to make a load game.
Let's copy the new game button.
Select it all.
Ctrl + C.
Go down below, paste, and replace the word new with load.
Now, when we load a game button, I don't want to call create new game.
I want to call load game.
So I'm going to rename this method.
To do that I'll hit CT controllr and call this load game.
You can also type on it, hit F2 usually brings up the rename.
Oh, F2 is not my rename button.
You can go up here though and find your rename option in the uh is it in edit now? I don't know where it's moved around.
Just rightclick and hit rename there.
Control-r.
It's different depending on what options you choose when you set up, but that should be the default.
So, we've got our load game button, and I want this to load a game, not call new game.
So, we'll replace the new game part with load game.
And then, finally, we need to move this class to its own file because we can't add it to a game object if it's part of if it's not the first class in the file if it's part of another classes file.
So, we'll hit alt enter, choose move type to load game.cs, which is going to create a new file.
Put that in there.
We'll save it off.
We should have a load game button appear here.
any second.
It should appear as a script down below.
There it is.
And then the final thing we want to do, oh, let's minimize that.
Just popped up on its own, is go to our new game canvas and let's make a new button.
I'll go to the scene view, duplicate the new game button.
Let's move it down a bit.
So, expand out the rec transform.
Just grab this Y value.
I'm just going to keep dragging it until it's somewhere down below that guy's head.
I'll rename it to load game button.
I'll remove the new game button script and then add the load game button script.
Remember, that's going to automatically register for the uh See if I can drag it in here somewhere.
Let's get it to pop on.
There we go.
Right at the bottom.
That's going to automatically register for the on click and call load game.
And then the final thing I want to do here is just change this text.
I don't want it to say new game.
It's not a new game button.
It's load load game one.
Let's just say it like that.
And then maybe shrink the max size of the text down to oh 140.
So it fits in there pretty good.
We'll save.
Let's press play and see if I can save or create a new game.
Make some little data changes and then reload my game.
So here's my new game.
I'll go grab a couple coins.
I'll go take a little damage.
I'll go to five.
Let's go to five.
Four health.
Go.
Five coins.
Four health.
We'll go into another level so that our game saves because remember we save when we load a level or load a scene.
Now let's hit play again and let's watch the logs because there's something important in that last statement that I think you should note.
Oh, let's do it one more time.
So we press play with the logs clear and notice that we also save as soon as we load into the level.
So as soon as I start it up in my game, we're actually rewriting it.
Let's go take a look at that again.
That's this line right here in our handle scene loaded is calling save game even if we load our menu.
So now we're just going to move this save game call so that it only gets called if we're not in the menu.
We can do that by adding some braces for the else.
So add a brace before and after the player input join behaviors changed.
And then move that save game call with Ctrl X and paste it right up here onto line 40.
So now if we load into the menu scene, we won't save.
Let's go back into Unity.
And actually, let's make one more change in the load game.
Let's make sure that we actually go into level one once we've loaded up our data so we can see it.
So, just like we do in new game, we're going to call load scene level one.
I'll copy that line 82.
And we'll paste it right here as 57.
We'll save.
Let's go in, press play.
We should no longer see a load on the initial startup.
And we should be able to save and load our game data.
Let's clear.
We'll press play.
Now, our first game data, if I just load, is going to be a default new value.
So, it's not really going to be useful, but um let's let's just do new game instead.
I feel like that makes it a little bit more clear.
We'll go get a coin.
We'll go take a damage.
And then we'll load a new scene.
We'll go into scene two so that we save our game.
Stop playing.
We'll play again.
And then we'll load our game and watch that data.
So, here's our saved data.
We see we had one coin and five health.
I hit load game.
We've got one coin and five health.
One coin and five health.
Everything is working pretty good.
I'll go up to another level.
I got five coins.
Now we'll press play one more time.
Hit load game.
I expect to see five coins.
There we go.
And if I stop again and I do a new game, I expect to completely wipe that out and have new values.
Let's just go verify that we're not crazy.
Yep, looks good.
No coins and full health.
All right, let's stop playing.
go to plastic is that we added support for a single saved game.
Saved game and we'll check that in and then we'll work on adding support for multiple save games.
To save multiple games, all we really need to do is give our games unique names and then save off the list of unique names that we have for our game so that we can recreate a UI and allow our players to pick which one they want to load.
So, let's start by going into our game manager script.
And when we create a new game, let's give it a new name.
Right here, you'll see in the game data, we create a new game data object.
And here, let's assign a name to it right afterwards.
So, on line 83, we'll add a new new line.
We'll say game data.
Let's see if I can spell that right.
Data.game equals.
And here, I want to use a timestamp.
I'm going to use the current time formatted neatly so that it just shows the date and then the minute and the hour and the seconds.
So to do that we can say date time let's see date time dot now which is a C method to string and then this allows us to pass in some formatting.
If you just do that you're going to get a kind of long string but we can pass in some formatting and choose which type we want.
So there's the general long date.
There's a general short one that kind of cuts out the seconds.
There's a full long date that shows like all of the text.
I'm going to go with the general long date format though because I think that that probably works well for what I want and it's going to look good in my UI.
So, I'm going to add a semicolon there.
Just put that capital G there so it knows how to format.
And then we need to generate our game name property.
So, I'm going to hit alt enter and hit well let's hit generate field.
I don't want it to be a property.
We'll hit F12.
And then we'll go rename re change let's not rename it change this to be public instead of internal.
So now our game data has a game name on it.
Let's go back to the game manager and when we save our game let's save it based on the current game data's name instead of the game one that I've got here.
So instead of saving to game one we'll replace this with our underscoreame data name.
Now, we can't just load_game data.gamename because this object doesn't exist when we're trying to load.
So, we're we're creating it from this.
So, we need to find some other place to save off all of these game names.
And in the save game method seems like a pretty good spot to do it.
So, we'll create a list of all of the game names that we have.
Let's do that up at the top.
Actually, let's create a new list.
I'm going to make this a public list.
So, I think I'll put it right after my public static instance.
public list of string and I'm going to call this all game names and then we'll initialize it to a new list of strings.
Okay, we've got our all game names.
Let's go down into the save game and here let's add our game name to this list of all games.
So say all game names dot add and we'll add our game data.gamen name.
Now, we don't want to add that name if it already is in the list, though, because we could end up adding it multiple times.
So, we're going to add another line here right above it.
I added a couple spaces just to clean things up.
And we'll say if all game namescontains, and then we do an open parenthesis, and we'll put in our game data.game name is equal to false.
And then we'll run this line of code.
That way, if we resave our level multiple times, we don't end up with that game name in the list multiple times.
So, we've got our all game names here.
We need to now save that off into our player preps.
So, I'll add another line here.
Actually, let's just duplicate line 54 with control D.
I'll put in all game names for the key here, this first value with a quotation mark.
So, this be all game names.
And then we'll paste in our all game names.
But if I just do this, it's going to give me an error because set string takes a string, not a list of strings.
So now we need to combine all of these names into one big string or one big piece of text.
And we'll do that with some comma separation.
We could use whatever character we want, but commas are a really common way to separate things.
So we'll use a commaepparated list.
I'm going to go down here and add two new lines.
And I'm gonna say string, commaepparated game names equals string.join.
And this is going to join a bunch of strings and add in a delimiter.
And if I hit tab, you'll see that it's actually knows exactly what I want to do.
Quotation marks around the string or around the comma here.
And then another comma outside the quotation marks and all game names.
This will give me a commaepparated list of my names.
And I'll put that in there for my player preps.
Save that off.
And now every time I create a new game, it's going to add that name into my all game names list.
Now I can't see that.
So I want to add in one more log entry so we can see it every time we maybe restart our game.
Maybe right at the end of awake.
Let's load in our all game name.
So say all game names equals player prefs.get string.
And we'll put in our all game names.
And if I just do it like this, we're going to get that same error.
So remember what the error was and how that happened.
Here's a quick challenge.
See if you can figure out how to convert this string back into a list of strings.
If you're not sure how to do it, do a quick Google search.
Say, how do I separate a comma or convert a commaepparated list of strings back into an actual list of strings or list object of strings in Unity or in C.
If you can't figure it out, don't worry.
I'll show you in just one second.
But I feel like that's a fun and interesting challenge for you to give a try.
So go ahead and try it and let's continue on and go through the answer.
So we've got our strings here and we can't assign it to all game names cuz that's the list.
We want the comma sep.
We want to assign it to a temporary value.
That's the all game names instead or all game names commaepparated.
So I'll say string comm, list is equal to that.
And then all game names will be equal to commaepparated list dot split and we'll split it on that quotation mark.
And then we finally need a dot to list.
What's going to happen is the split will return back an array of game names.
So it'll give us back all of the game names in an array format which is very much like a list but doesn't support adding and removing things.
So then we just call the two list on the array that it gave us and it converts it to a list and assigns it to all game names.
I can save that off.
And the last thing I want to do actually is just log out our commaepparated list.
So let's say debug.log and we'll log out that commaepparated list with semicolon right here.
So we can see all of our game names.
We can't log out a list of strings, but we can log out that nice separated one.
So let's go back into Unity, press play, and I'm going to make a couple new games.
I want to get a couple new games in there.
So, I've got a little bit of data data data and then we'll take a look at what that data looks like and then figure out how we can add our buttons to do the loading.
So, we've got our console here.
I hit new game and I've got a new game created.
Let's hit play.
Stop playing and play again.
And this log entry should no longer be blank.
The first one right here was blank because I had no game saved.
So, there's my first game 217 2023.
And you can see the time stamp.
And if I hit new game again, stop playing, play again, you'll see that.
Oh, what did I I didn't stop playing.
Let's stop playing and play again.
And I should get another one.
That's a couple seconds later.
See that? The one 15 seconds later.
And every new game that I do is going to create a new entry into there.
So, I'm going to have one new game created.
It'll save off my actual game data into the game object and it's going to save off into the game list.
Let's go take a quick look at that registry one more time.
So you can just see what that data looked like.
Got my registry editor here.
And here you can see I've got my all game names.
If I double click on it, I can see the text there.
It's again gets that weird format, but you can see I've got my first one, then my second one starts after that, comma, and the third one starts there.
And the game names are actually right here as well.
So you can see the games are saved off just as a timestamp for their key.
And that's where I can see I can open up any one of these and see the data for that game.
So my games are saving, the data is saving.
My final step now is to build a UI so that I can pick which game I want to load.
Before I do that though, let's go into plastic and commit that we are now saving all game name spot game right game names list to player press and we'll check that in.
Oh, popped up an error.
Let's do it one more time.
It was refreshing that asset.
Hit check in again.
And there it goes.
You see it updated right after there.
We're good though.
So, we'll continue on.
Now, let's build our load level panel.
We're going to go into our new game canvas.
And I think what we'll do is just duplicate it and let's create a load game canvas.
We'll disable that new game canvas temporarily and then expand out the load game canvas.
We can do these as panels, by the way, instead of canvases, but I like separating them out.
It makes it a lot easier to understand what's going on and to figure things out.
and it's easy to adjust back and forth.
And we can get some nice performance benefits from keeping them separate like this.
So, let's take a look at our load game canvas.
We have two buttons on it.
I don't want either one of these buttons really.
I kind of want the load game button.
So, let's delete the new game button.
And let's create a new panel in here.
We'll right click, choose UI, and choose panel.
I'm going to center this so that it's not so um big.
So, it's kind of in the middle.
Let's do a center right here and make it oh 600 wide.
So, I've got this nice centered panel here where I can put all of my buttons.
I'm going to take the load game button and drag it on to be a child of that panel.
I'm going to rename this panel to games list panel.
It's got all of my games, or at least it will.
And then let's go modify our load game button.
So, our load game button here is a little bit taller than I want.
I'm going to shrink it to about 100 high.
And then, let's see.
We've got our load button script.
Let's go turn this into a prefab next.
So, go to the prefabs folder with our load button kind of shrunk down a little bit.
We'll drag our load game button in and make it into a prefab.
Now, we're going to go to this games list panel.
We're going to create a new script for it that's going to use that prefab and instantiate one for every saved game that we have.
To do that, we'll create a new script for our games list panel.
Go to the scripts folder, rightclick, create a new C script, and call this games list panel.
We'll assign that to our games list panel by selecting it, and then just dragging it on.
Ah, my code editor popped up for me.
Nice, but not what I wanted right now.
So, as soon as it finishes, we will collapse that shader down and drag the games list panel right here onto the games list panel in the inspector.
Now, let's open up that script and add a place for our load game button prefab.
I'm going to delete out my start.
Well, let's delete out u let's just start up here.
We'll delete those in a moment.
Maybe we'll start by adding a serialized field.
And this is going to be of a load game button.
And we'll call this button prefab.
Let's call this load game button.
No, let's just call it button prefab.
Keep it nice and short.
There's only one button type that I've got on here.
Now, when we load this object up, maybe when it enables instead of it starts, I want to go through and set up all of the buttons.
So, I will delete the start and update.
We'll select all the way 9 through 19 and delete and add an on enable so that when this thing turns on, that's when we do the loading.
So, that way every time we turn it on, we can get new sets of buttons if we've got new levels loaded.
We don't want to just do it once when we start the game up or when we lo Well, actually, technically, we could probably just do it once when we load the menu up.
So, let's change this to start.
We'll change it back to start instead of on enable.
It'll simplify things.
We won't have to clear up the buttons.
So, we're not going to get any new buttons, new menus or new games until we go back into the menu anyway.
So, we've got our start method here.
And what we want to do is loop through all of the games that we have saved.
So, we want to say for each var game name in game manager.instance doall game names.
Now, this should already be filled out because this is loaded in our awake of the game manager.
If this was in the start of our game manager, this would be a problem because it may or may not be ready.
Since it's in awake and this is in start, not in on enable or awake, we know that all game names will have been filled out before this ever gets called.
That's because awake and on enable get called before start.
So, we're going to loop through each game name and we want some braces here because we're going to do more than one thing.
The first thing we're going to do is instantiate a button for each game.
So say v button equals instantiate which is the method to create an object at runtime.
And we're going to pass in our button prefab.
So this is going to spawn our button prefab on the UI.
But first before we do that, we need to give it one more parameter which is the parent that it's going to have.
And we want the parent to be this game list panel.
So we'll just say transform to pass in our transform.
It really wants not a component object but a transform to be the parent.
So we pass in our own transforms.
Now we've got a button here.
Next thing I want to do is assign the game name to the button.
So we'll say button dot set.
Let's just say game name.
Let's let's make a method.
Set game name.
And we'll pass in our game name.
No, we'll just assign the game name.
Let's do it like that.
Game name equals.
And we'll just assign it as the game name.
Now, we could do both ways.
This will make it so that we're setting the property instead of calling a method.
It's a little bit simpler and there's really not a good benefit in using a method right now.
So, we're going to go with the simpler way.
We'll hit alt enter and we'll generate a property for it.
So, I hit alt or enter right there.
And now, if I hit F12, I should have a public string game name.
So, this is the game name for this button.
Now, oh, you know what? I lied.
I do want to call this set game make a set game name method.
So, let's change this.
We'll call set game name and we'll pass in our game name parameter.
Then we'll hit alt enter and we'll generate a method for that.
I'm going to get rid of that extra spacing there.
Hit F12 and let's go take a look.
So, the reason that I want to do that is because if I just set this game name here, it's not going to update the text.
But if I set the game name as a private thing and then update the text in my set game name method, I'll get a nice UI update.
So, let's delete out line seven here.
And on line 15, let's say underscore game equals game name.
We'll generate a private field for that.
So, now we've got just a private string that can't be read by other things.
And then let's update our text mesh pro.
So, we'll say get component in children tmp_ext.
That's going to be the text object that's a child of this button.
And then we need our open close parenthesis to get the object and dot to reference a property on it or a method.
We want to reference the set text method and pass in our game name.
So now we're saving off the game name in this method, which is why we used a method instead of a field or a property.
And then setting the text here.
Well, that's really why we're using the method instead.
I'm going to change this to be public just so that it matches and get rid of this private keyword that I don't need so that we're consistent.
We'll save.
And now if I go into Unity, I should be able to see my buttons appear.
But there's one thing I want to modify first before we do that.
First, let's uh save this.
Save our games list panel.
And then go back into Unity.
And we're going to add a component to make our buttons stack up.
So, if we go to the games list panel, we can add a layout group.
We can either do a vertical layout group, a grid layout group, or a horizontal layout group.
I'm just going to go with a Let's go with a grid layout group for now.
And we'll set the cell size to 600 grid layout group.
Kind of auto controls the size of all of the buttons and everything.
Makes it really easy to work with.
We'll save.
And then we can delete this load game button that's a child of our games list panel.
Go make sure that our games list panel has the button prefab assigned, which doesn't.
So I've got my games list panel selected.
I'll hit the search button.
See if I can find my asset.
And look at that.
It found it.
If yours can't find it though, you can just go down to the fold.
Oh, it actually found the wrong thing.
So, we're not going to use that.
Don't use the search box cuz I didn't realize it searched in the scene and it found the wrong thing.
So, instead, we want to look at assets and you'll see that it has none.
Let's go down to the prefabs folder, though, and just take the load game button and drag it on.
We don't want to be spawning this disabled one here.
That's not the right object.
We want to be spawning and referencing the one down here in the prefab.
So, select your games list panel, click on the button prefab.
Whoops.
Let's see.
Click on the button prefab, not the script.
and make sure that it's selecting this one right here.
Now, if I save and press play with this canvas up, I expect to see all of my saved games pop up here.
And there they are.
I can click on one of my saved games and load right in.
Let's go over here, maybe take a little bit of damage on the saved game.
What is this? Game two.
The second one there.
I lost track of the time.
We'll force it to save.
Let's stop playing.
Go back in and make sure that we're loading the correct data.
I should see my health be at two when I click on this game right here.
Oh, and I don't.
And the reason for this is pretty simple.
So, I want to leave it as a little challenge at first.
See if you can figure out, taking a look at the load game button, why we're not loading the proper game.
Go ahead and view it.
See if you can figure out what's going on.
And then I'll run you through the solution.
You can build the solution if you want, but if not, don't worry.
I'm going to show you in just a second.
Just go ahead and pause and take a look at it.
it.
it.
Okay.
So hopefully you noticed that what happens is we call load game and we go into our game manager load game method and then we load game one.
Every time we load, we're not actually using the game name of that method or of that button.
So we need to make our load game method take the game name as a parameter.
So first thing I'm going to do is copy our game name and add that as a parameter to my call to load game.
That's going to give me an error saying that no overload for load game takes one argument.
So I'll hit F12 and we'll change that.
We'll add a parameter to load game.
Say string game name.
And then instead of calling get string on game one, we'll call get string on game name.
We'll save that off.
Go into Unity.
And now we should load the proper game.
Oh, we have an error here.
Let's make sure that I've not typed anything.
Do a quick build.
Oh, I didn't build.
That's why my file wasn't saved.
So, it wasn't calling the proper method.
Now that my build is done, it should work.
Let's hit play and then try loading that game again and see if we have our modified health.
So, here we go.
Let's go.
We'll go grab a couple coins.
Make sure that we're save because we weren't actually saving to the correct game.
We were saving to a blank game.
We'll go take some damage.
One, two.
I've got seven coins and two damage.
We'll leave the level.
Load the level.
Press play.
And then reload our game.
And here we go.
We've got our saved data and everything's working right.
So, let's go into plastic and say that we added support for multiple saved games and checkin.
Our saving and loading system should be working pretty well now, but the menu system is a bit of a mess.
So, what we're going to work on now is an update to the menu system so that we can navigate between canvases and even delete our saved games so that we don't end up with a whole bunch of them that we can't manage.
Seems like an important thing to allow our players to do.
So, I'm going to stop playing and we're going to take a look at our canvases.
We've got the new game canvas, which is not on right now.
I'll enable it.
And then we have the load game canvas, which we can't see anymore.
If I want to bring this load game canvas in front of my new game canvas, I can adjust the sort order on the canvas.
Just turning it up to a higher number like one.
But now I can't see my new game canvas anymore.
So what I'm going to do is disable the load game canvas with the sort order set to one.
Then we'll change this load game button so that it enables the load game canvas.
It's pretty simple way to set it up.
We'll expand out the new game canvas and go to the load game button.
And then we'll scroll down and remove the load game button script.
Hit the plus on the on click so that we have a new listener whenever we click this button.
And the target for the thing that we want to run code on when we click the button is the load game canvas object.
So I'm going to drag it right in and then choose from the function list.
We'll choose game object and set active.
What this is going to do is call the set active method on that object which will turn it to either active or deactive.
Right now, it's set to deactive because the checkbox is off.
If I set the checkbox to true here, then when we click this button, this active checkbox right here will turn on and the UI will pop up.
Let's go and test that out.
So, I'll play.
Turn that load game canvas off.
And as soon as I click the load game one here, it should pop up my menu.
There we go.
I see the load game canvas appearing.
I'm going to stop playing now.
and let's add a back button so that we can go back out of load game mode.
To do that, we're going to turn on the load game canvas.
I'm going to go to my load game button here and duplicate it with control or command D.
And then I'm going to drag it down on top of the load game canvas.
Now it appears because it's on this canvas and not the new game canvas.
New game canvas still has its own button.
If I turn off my load game canvas, you can see there's still the button there, but the load game canvas has one as well.
I'm going to select this load game button, and I'm going to put it right up here in the corner by clicking on the recct transform tool, holding alt and shift, and clicking the top left corner.
Now, I also want to shrink this down a little bit cuz it's going to be a back button.
I want it to be a little bit smaller.
Make it maybe a height of 100.
And then rename it to back button right up here.
Just rename and hit enter.
Now, the next thing I want to do is change the text because it says load game one.
So, I'm going to expand out the text here, the child of the back button.
Go select it.
And as long as the text mesh protext is expanded, I should be able to write right in here or type right in here.
And I'm going to put the word back with a capital B.
It's still all in uppercase mode, so it doesn't matter how I case it here.
But I like to case it correctly so that if I decide to change the font, it'll still look right.
Now that I've got my back button, I'm going to go to the back button object again, scroll down, and find the onclick listener.
All I have to do is uncheck this checkbox.
Save my scene and press play and watch what we've got.
Right now, the load game canvas is going to be up by default because I turned it on by default.
But I can go back and turn it off.
And I can go back into the load game menu just by hitting the load game button.
Now, as a last thing to make this a little bit fancier, we could add a little icon here.
Maybe something that shows that we're going back, a back indicator or an arrow.
And to do that, we can just right click on the back button, go to UI, and choose image.
We'll get a new image that's sitting right on top of my sprite.
If I go to the scene view, you can see it right here.
I could drag it over or move it, but I like to use the recct transform tool instead.
So, click the recct transform tool, hold um actually, yeah, alt and shift, and then click the left side.
That's going to move it right over here to the left.
And I just need to pick a sprite for it.
Now, there is a pretty good sprite that we can use already in our pack.
If you just search for sprites and search for the word left, you should see a sign left.
And look at that.
It I think it fits pretty good.
I want to shrink it down just a little bit though.
So, let's adjust the height to be maybe 80 by 80 instead of 100 by 100.
So, it's not going over the edges.
I think that looks pretty good.
So, now I'll just disable the load game canvas.
press play and make sure that we've got the flow that I expect except for I've got the number one after my load game text here.
That's the only thing that I think is an issue.
Let's see.
Go back and forth.
Back buttons looking good.
And I can load into a level.
I'm going to stop playing.
Make sure that I've saved my scene and type in a commit message that we added.
Menu navigation to load game canvas and check it in.
Now, we're going to give the player the ability to delete their saved games.
We're going to go into our load game canvas and enable it and then go find our prefab for our games.
So, we've got our load game button right here.
Just double click on it and open that prefab.
What I want to do is add a little button to the right of our load game button that is like an X or delete game or something like that that the player can click on.
Maybe we'll give them a confirmation later and then they can delete that game so that it doesn't show up anymore and we don't have a giant list of saved games.
Should be pretty easy to accomplish.
What we need to do first is rightclick on our button and choose UI and then choose button again.
We want this text mesh pro button right here.
And it's going to add a new button right on top of our existing one that looks kind of ugly.
I'm going to call this delete.
Let's see if I can spell that right.
Delete button.
and then I'll move it over to the right.
If you didn't name it over here, you can always rename it right here.
Let's go to the rect transform tool.
I'll hold alt and shift and click to the right.
I'm going to adjust the size to be 100x 100 so that it matches with my button.
Then move the position X over 100 more, the exact size of my width so that it lines up perfectly and I've got this button just off to the right.
Now, I want to change the color of this to be red since it's my delete button.
And then change the text as well.
I'm going to scroll down.
Oh, actually no.
I need to go over to the delete button, select the text, and then change our font asset right here.
So, here we're going to choose, we could go with uh the bangers one or something else.
I think I'm going to go with Robbo this time, though.
I'll choose the surf.
Let's go with the drop shadow and a white.
I'm going to change the text to be a big capital X and then click the auto size.
So now I've got this big X right here that I can click to delete a game.
Next thing I need to do is hook up the delete game button though so that it actually does something.
To do that, we'll go up to the load game button.
And on our load game button script, we're going to add in a new method.
One that'll allow us to delete a game.
That way our delete button can just reference this and we don't have to write a whole bunch of extra code, add a bunch of extra scripts or anything like that.
So keep it nice and simple and accomplish the task.
So, we'll open up our load game button and right below our load game method, let's add a public void delete game.
This will call into our game manager.
So, we use the game manager.instance just like we do with load game.
And let's call delete game.
Pass in our game name.
And we don't need a true or any other parameter like it tried to give me.
So, this should be good.
We've got a delete game method that'll call into our game manager, our current one, the instance of it, and tell it to delete the game.
Now, delete game doesn't exist, so it's got a red underline.
I'll hit alt enter and just generate a method for it.
And I'll completely ignore that method for now.
I'm going to hit control shiftb so that all of my files build.
If you don't do that and you just save this, your game manager file might not save and you may still have a build error as soon as you jump over there.
So, make sure that you saved your game manager and your load game button at the very least or you do a build with control shiftB or whatever your hotkey is.
Now, I'll jump back into Unity and we'll go to the delete button.
Scroll down.
It has nothing in its onclick listener.
I'll hit the plus button.
We'll drag our load game button, the parent into the target.
So, this none object right here.
And then for our function, we'll choose load game button.
And we're going to choose the delete game right down here on the bottom.
Now, if I go back, save my changes, I should now expect to see that my buttons appear with a little red X next to them.
And when I click them, it deletes the but the game.
Let's press play and see if that's the case.
So, we play.
I've got my buttons here.
Let's go back real quick.
Go back to load game.
Yep, still got my buttons here.
I'm going to hit X and get rid of this uh 115616 one.
I click it and well, look at what I get.
method or operation is not implemented game manager delete game.
So if I double click on this see that oh yeah we haven't actually implemented the delete game method and that's what this does the throw not implemented exception it just gives you that error saying hey this method hasn't been implemented which just means that you need to go do it and it's really just kind of a warning or notice to the developer hey you um haven't done this yet you autogenerated it and you forgot to get to it.
So instead of doing nothing, it gives you some warning to let you know there's some development probably needed here.
So we need to delete our game.
To delete our game, we just need to call player prefs.delete key and pass in our game name.
And then we also need to delete our game name from our all games list and save that.
So we'll say all game names do remove.
This is how we remove something from a list.
And we'll pass in our game name.
And then finally, we'll save our all game names list.
So to do that, let's go up, scroll up to the part where we save game names, which is right here.
So on 59, 61, and 63, we're saving the game names.
62, we're actually saving the game data.
So let's move this up a little bit.
I'll select line 62, hit control X or command X, and I'm going to move it right up here.
Um, right, let's do it right above line 56.
So we'll add a new 56 that saves the game.
Then all of this code below will be for dealing with the game names list.
And these three lines here, 61, 63, and 65 are what I need to save all of the game names.
So I'm going to delete out 62 and 63 now just to clear it up.
Get rid of some extra spacing.
Copy these lines 61 through 63 that save the game names.
Creates the commaepparated list from that list and then saves off that list.
We'll scroll down and paste it into delete game.
Save my file.
And now if I go into Unity and I delete a game from here, you're going to see that the game will get deleted, but my UI isn't actually going to update.
So, let's try it out.
Let's see what what that's like.
So, I go in, I hit the X button, and I think the game is gone.
It didn't show an error here.
And if I stop playing, or let's see, if I go back and back, nothing happens.
But if I stop playing and play again, I should see that that game has disappeared.
And the reason that it's still in the UI is that we haven't done anything to remove it from the UI.
So, we need to have a way to make our UI update with our games.
And that's what we'll do in the next section.
For now, though, we're going to go into plastic and commit our load game deletion.
So, say added a delete option to the load game button.
And first, I want to make sure that I've saved my scene here as well.
get all my changes in and check in.
in.
in.
This lesson is going to be a little challenge.
What I want you to do is finish up the functionality of this button.
Make it so that when I click the X, our game gets deleted and the UI element is gone.
If I go back and I go load game, you see that it's still gone.
I come back in, press play, I expect that element to still be gone or that saved game to still be gone.
So, what I want you to do is just recreate that so that you can delete them.
And if you end up with a situation where you delete all of them and have nothing left, but then you press play and you get a blank entry, don't worry about that.
We'll talk about that in a moment.
First, just worry about getting the X to work so that it actually removes it.
And what I want you to think about when you're doing this challenge is simplicity.
There are a lot of ways to do this.
There are many, many different options for ways that you could set this up.
And you can get extremely complicated or extremely simple.
I generally recommend that you air on the side of extremely simple until complicated stuff is needed.
So go ahead and give it a try.
Pause the video and then in a moment when you're ready, unpause.
And I'll show you the solution that's I think the simplest and what you should go for in this scenario at least.
All right, let's stop playing and well, we don't even need to stop playing.
Let's go take a look at how we've actually solved this.
It's very, very simple, like I said.
And if you looked down below, you may have cheated and already seen the answer.
But all we really need to do is call the destroy method on our game object.
Right after we delete our game in the delete game method of our load game button, remember this is on that button that's placed that we want to remove.
We call destroy.
It'll remove itself.
The layout group is going to automatically adjust.
Now, there are lots of other ways that you could do this.
Again, I recommend staying with the simplest until you need something else.
So calling destroy, not having a whole big system for managing and updating those makes a lot of sense.
They only get added when we hit the or when when we load in and we've got some saved games already and then they'll get removed later.
The next thing I want to do is give our players the safety of a quick confirmation so that when they click the delete, their game doesn't instantly get deleted, but they have to click one more time, maybe in a slightly different spot to make sure that they don't accidentally go, "Hey, I'm trying to load my game and ah whoops.
I clicked and deleted it.
So, let's do that by going into our button.
We'll find our load game button prefab.
Open it up in prefab edit mode by double clicking the prefab.
And then let's find this delete button.
We've got delete.
And what I want to have is a delete that pops up a confirm and a cancel.
And then have this button do like the actual or this functionality here be the actual delete functionality on the final button.
So, I'm going to duplicate this delete button.
I'm going to call this confirm delete.
And I'm going to move it over to the right 100 pixels.
So let's go to 200 on the position X.
And then we'll expand out the text and change the text from saying just an X to confirm delete.
I think that looks good.
It's very obvious what we're doing here.
Now I'll go back to my delete button and I'm going to remove this on click thing.
Instead of it updating or calling delete game on our load game button, we're going to call enable on our confirm delete button.
So, I'm going to take the confirm delete button, drag it over the load game button, find the game object, and choose set active.
We'll set that to true so that we can enable this button whenever we click the X.
Now, I also need a way to go back like a cancel or a um disable or deconfirm.
I guess it would be just cancel, I think, would be it.
Let's let's duplicate our delete button again.
We'll call this cancel button.
And then we'll change the text.
Well, first let's change the color.
Let's make it like a gray.
And then let's change the text to say cancel.
And then the final thing we need to do is go to this cancel button and then make it set the confirm delete.
Uh well, actually, what do I want it to do? If I cancel, it should set confirm delete to not enabled and it should set itself to not enabled so that it hides both of these buttons.
I guess we also need to go back into the delete button and make it show the cancel button.
So, we'll go to the delete button, hit plus, and we'll drag the cancel button into the target for the second one.
Choose game object and set active and set it to true.
Now, the last thing I need to do is go find these two buttons, confirm and cancel.
I'll hit control and select them both and uncheck them.
That should disable them both.
If I go back out of prefab edit mode and let it save, I should now have the functionality that I expect.
Let's go test it out and debug and make sure that didn't mess anything up or miss a reference or anything.
Still got to get rid of this blank game when there's no game.
But for now, let's go create a new game.
I'll just run over here and let it kill me to I really need to add a quick die shortcut so that we can do this faster next time.
Let's let it kill us though.
And we've got our new game.
I'm going to hit the X.
And there's a cancel and a confirm.
I'll hit cancel.
It doesn't go away.
So now if I accidentally click this, I'm pretty safe.
I've got to click this and then go over here and hit confirm delete to get rid of the game.
There we go.
I've got my confirmation.
So I'll stop playing.
go into plastic and say that we added delete confirmation to saved games and check them in.
Now, if you're wondering how to get rid of this blank game that keeps showing up when you don't have any saved games, then you're in luck because in this section, we're going to dive into debugging it, seeing what's causing that, and going through the process of actually tracking down the cause and solving it.
So here you can see that blank game that only appears if by the way if I have no other saved games.
So let's stop playing play again with it deleted.
Make sure that it's gone and that I'm correct in that assumption in my observation.
And if I delete this one, come back in and press play again.
I expect that that bad game is going to show up again.
Let's check it out.
See if that's the truth.
Yep, there it is.
And then let's talk about how we can track this down.
If I look at my games list panel, see I've got that one load game button right here.
It obviously has no game name because I don't have a saved game there.
If I stop playing, that should disappear.
It's not a placed prefab that's already there or anything.
And all we really have to look at is our games list panel cuz that's the thing that's on here that's dealing with our load game button.
So, let's take a look at that script and then see how we can use some debugging to track down the cause.
I'm going to open up the games list panel.
And right here, we've got our only method.
In the start of this method, we loop through all of our game names.
We instantiate a button for each game.
And that's it.
So, what's happening here? Well, what we can do, we could guess and try to figure it out.
I already know the answer, so guessing probably isn't that helpful.
And if you don't know the answer, guessing is usually wrong.
So, what we can do is guess or test and verify.
So to test and verify in our code editor, I'm using Visual Studio right now.
You can do this in Writer or just about any code editor, you'll click over here to the left and add a breakpoint.
Right here on this bar is the break points area.
And on any line of code that's an actual executable line of code, or even on some of these where it's a brace at the end of the brace, I can add a breakpoint where my code editor will stop execution and show me a bunch of information about what's going on.
To make that happen though, I need to attach.
And let's shrink this window down just a little bit.
You can see what happens at the top.
To attach, I just hit the F5 key, which I actually have a uh a little Star Wars speeder on just to make it nice and easy for me to hit all the time cuz I hit that key all the time.
And then once it's done attaching, it should look like this.
I have a pause button and a red stop button.
I'll go back into Unity.
And now I press play.
And what should happen, assuming everything works right, is it will kick me back over to the code editor as soon as this buttons or as soon as this panel's start method calls.
There it goes.
It worked.
Now, sometimes things break and it'll just sit there and hang forever.
If that happens, you need to come back into Visual Studio, hit stop, and probably restart Unity and restart your code editor.
Occasionally, it gets bugged out, freezes, and just stops working.
Um, this happens with just about every code editor.
happens with every ed engine I've used as well.
So, just be aware of that.
If it doesn't kind of pop back over quickly or you can't hit play, make sure that you hit that stop button.
Maybe even close the debugger.
Sometimes debugging just causes issues.
But this time it worked perfectly.
So, let's take a look.
You can see here that I'm looping through my game names and it definitely found one because it stopped on line 13.
It's showing me right here.
The yellow is the next line of code that it's ready to execute.
It stopped right before it executed it because I put the break point there.
And it wants to instantiate a button.
And then it wants to on the next line, if I put my mouse over the game name, I can see it's got a game name of blank.
So, it would set it to a blank game name.
That leads me to believe, yep, this game name right here is blank.
And I'm guessing if I mouse over the all game names thing, here you go.
You can see it says there's a count of one.
There's one game in here.
And if I expand it out, the entry in zero.
So the first entry in our index or the first entry in our list or array.
I think it's a list here that we have at index zero is completely blank.
So we have a blank game name in there.
So now I got to think like well well how do I have a blank game name? That's I mean that's good to know but that doesn't help me solve the problem.
I need to figure out why my game name is blank.
So the next thing I'll do is just um remove this break point and hit F5 so that it continues on execution.
and it'll just let the game finish loading.
And then I'm going to stop playing cuz that was interesting, but it wasn't helpful enough.
I want to find out what's filling out all game names and what's breaking that.
So, I'll go to my all game names in my game list panel, and I'm going to hit shift F12 or rightclick and choose the find all references right here.
My hotkey for shift F12.
Yours could theoretically be something different.
I'm going to drag it up here.
And you can see down in the bottom right, I've got all of the references to my all game names.
Most of them are in game manager except for this one in the games list panel.
So, where's the part where we set or add things? Well, we've got one where we add right here um and double click on it in the save game.
But that's probably not where things are breaking is my guess.
We can add a breakpoint here though if we want.
So, just go over here, add a breakpoint so we'll be ready to check it.
There's also a spot right here where we assign it all game names equals something.
So, let's add a breakpoint there as well.
I'm still in debug mode.
So, I'll go back into Unity and we'll press play and I expect to get a break point or have it stop at that break point.
Pop open the code editor and let me track down the problem.
So, here we go.
Now, we're in the let's see, let's minimize these bottom windows real quick.
We are in the awake method.
We've got our commaepparated list from player press get all names.
And you can see that oh, our commaepparated list is blank.
So, we've got nothing.
We log that out and then we get all game names by calling split on this.
Let's hit F10.
F10 will step us ahead one one line.
So, it's essentially going to run this line and go to the next line.
I hit and here we are.
I can look at my all game names.
Now, if I put my mouse over it, I can expand it out and see that oh yeah, it gave me a blank one.
And it's giving me a blank one.
It looks like because the split or the list that I'm splitting is blank.
So, because I'm giving it an empty string, it's giving me an empty game name.
So, I've got a couple options here.
First thing I want to do, though, is stop debugging.
So, I'm going to hit this little red square so that I can start adding code.
It can't really change the code while I'm debugging.
So, I'll stop that.
And I'm going to remove my break point there because I don't want it to stop there anymore.
Now, there are a lot of ways that we can fix this, but I think that the easiest way is to just remove any blank game.
So, we can just say all game names.
remove and we'll just remove any blank entry.
Now, if there are multiple blank entries, that's not going to catch it.
But we don't have a scenario where we get multiple blank entries.
And I don't expect that to be the case.
We're only getting the blank entry because the commaepparated list could be empty or null.
So, we've got to deal with it here.
But, we shouldn't have to deal with multiple in there.
And we probably don't need to make the code any more complicated than that.
We should be able to save, go back into Unity, and see that we no longer get a blank game if we have no games.
Let's check that out.
So, I press play.
We're no longer attached.
Make sure that you've hit that little red stop button so you're not getting broken or paused.
And look at that.
No blank game entry.
If I hit new game, come back in.
I expect my game to be there.
But I'll not get that blank um null entry anymore.
Just double check that.
Yep, looks good.
Confirm my delete.
Press play.
Play one more time.
I should expect to see no bad new entries there.
Look at that.
And there we go.
So again, one of the key things here is just to make sure that you attach.
You hit F5, add your break points at the spots where you want to break.
Here I actually need to remove this extra break point.
And if things break, just hit the stop button.
Consider um restarting the code editor, Visual Studio or Writer, whatever you're using.
Or restarting Unity.
Sometimes things break, they bug out, and it just gets frozen.
Remember, your game will stop execution.
And you can use F10 to step over things.
And you can also use F11 to step into methods.
We haven't talked about that yet, but we might dive into that later.
All right, for now I'm going to go back into Unity, go to my plastic window, and we'll update our game manager or say that we've updated our game manager to fix the empty games.
So, fixed empty game showing up in the game list.
Before we dive back into gameplay, I want to finish cleaning up our menu system just a little bit.
We've got our load game canvas here.
And right now it's on by default.
I want to turn that off by default.
But before I do that, I want to make a change to the background so that we can tell pretty obviously that we're on a different scene or a different canvas and just kind of add some different visual feel.
And there are a couple different options that we've got here.
The first is that you could just grab another background like the one that I've got down below.
You should be able to grab that background, pull it in, and import it and have it look just like this.
Let's go select that background and assign it.
So, I've got my background under the load game canvas and I should just be able to drag in this background object.
This background, well, it's a sprite or texture.
Let's go select the texture.
So, you can see the default settings that I've got here.
It's as a sprite and it's just set to all of the the normal standard defaults.
Now, if I go back and forth between my scenes, I should see a pretty good visual notification or distinction.
It's going to be pretty obvious that I'm on a totally separate menu.
New game is different.
Load game.
Okay.
Yeah, totally very, very different.
Now, this works good.
It looks great, I think.
I mean, I kind of like the art here, but there are some things to remember and think about if you're building out a bigger game and you want to target a mobile platform or something, you do need to start kind of being a little bit conscious about the size of the the textures and files that you're using here.
Here, these ones aren't too huge.
They're about 1 megabyte, but depending on your game, you could end up pulling in some 4K textures here that are a lot bigger or something else that's even even crazier.
Um, and you're going to want to think about that in terms of memory size.
When you start building out a game for different platforms, the more memory that you use, the more likely you are to run into problems.
Now, if you're on not on mobile, you're just targeting desktops and you're just targeting um well, really, if you're just targeting desktop, you're probably totally fine.
Don't need to worry about it at all.
But if you're targeting mobile devices or you're targeting consoles, you do have to pay some attention to this stuff.
You don't have to worry about it too much when it comes to your menu things cuz it's pretty easy to change them out later.
So, my general recommendation is go with something pretty and nice.
And then when you get to the point where you're like, "Oh, I need to start saving some memory or some space for textures and I need to start deleting out some of these bigger images because I want to put in some characters and this kind of is a trade-off for my budget." Then you can do something like this.
Go to your background and instead of using this big image, we could go find something like a brick.
Change it over to tiled mode.
And now I've got like this brick wall background might work just fine as well.
So I'm gonna leave mine as a brick wall background for now.
I'm going to disable the load game canvas and then I'm going to go to my new game canvas and fix that text there that says load game one because that has been driving me a little bit crazy.
Um so I've got new game or load game.
Let's say h should I just say new and load? Uh we'll just leave the word game in there for now I think.
Let's see.
Is there anything else that I wanted to change on my canvases? I don't think so, but I'm going to double check.
Nope.
I think it looks good.
So, we'll save.
We'll go back into plastic and say that we cleaned up the canvas.
I don't know why this uh this material keeps trying to check out.
I'm just going to let it change.
I don't know what the change actually was.
So, let's do a diff real quick.
We'll right click, hit diff.
I'm going to guess.
Yeah, there are uh find differences.
Interesting.
something changed on it and I'm not sure what.
So, I'm just going to let it commit.
We've got a updated main menu.
So, now it should have a perfect normal flow and we can get back into gameplay development.
Now, we want to add a lot more functionality to our game, and I want to make sure that we can do that without really messing with your levels so that you can start doing some level design and building things when you're getting some spare time and having fun, but still experiment with and have a place to build out our new things.
This is exactly what we do in a normal AAA environment.
We have some sort of development environment set up where our designers and code teams can go play around with things and make their own stuff.
In just about every game I've ever worked on, there are special levels set up for the designers to do exactly that.
Sometimes each designer will have their own level, and some MMOs, some designers have their own zones where they just build out all their own stuff.
And sometimes it's just a shared one.
In this case, we're just going to build a sandbox where we can experiment, build things, put things together, and try out our stuff without modifying levels and without having to put things into our existing levels.
So, we're going to start by just taking level one and duplicating it or saving it off as a sandbox level and then building upon that.
So, we'll go into level one.
I've just doubleclicked and opened it up.
We'll go file, save as, and I want to make sure that I'm in my scenes folder.
And I'm going to call this sandbox with a capital S and a lowercase B, just all one word.
Now, I want to clear this out a little bit.
There's a lot of stuff in here that I don't want to have just by default.
I want to start it off with just platforms because that's what I'm going to work on.
So, I'm going to find the flag, the spikes, delete all of those.
I do want to keep my player input manager.
I don't need these coins, so I'm going to delete them.
And the same with the springs.
I don't need those either.
I'm going to go down to my environment.
I do want to keep most of the environment, primarily the platforms, though.
That's the part that I care about.
So, I'm going to make a new subfolder here or a new folder in my root, which is just an empty game object.
And I'm going to call this platforms.
I'll right click on the transform and reset it so that it's all zeroed out.
And I'm just going to take the platforms, one of each.
So I've got a two, a four, a six, and a five.
And I'm going to drag them onto my platforms object.
I'm going to rightclick or actually let's go over to the transform.
We'll right click and reset their positions and transforms and all that.
So right click and reset their transform essentially.
And then we're going to go to the position Y.
And I'm going to use a special function.
So with all of these selected, I'm going to put L and then an open parenthesis.
And I'm going to put a let's start with zero and then a comma and a 10.
What this is going to do is linearly split them out or space them so that they're from 0 to 10 m up.
Now, if I look at the position here, I see that that's actually giving me some kind of odd numbers.
getting like 33 um 66 and 0 and 10, which is what I should expect, but that's not really what I want cuz I want these to be more rounded numbers.
So, instead, I'm going to do it again, but this time I'll pick a number that's divisible by 4.
So, I'll go maybe 0 to 12.
So, do L 0, 12.
And now I should get nice whole numbers.
So, I've got a 12, a 4, an 8, and a zero.
And now that's nicely lined up, and I should be able to jump up those.
But let's make it so that they're split off to the right as well.
So, select them all and for the X position, we'll do an L.
And we'll just go zero, comma, and let's do maybe 12 again.
There we go.
Now, I've got some split out little platforms that I should be able to jump up.
Let's save our sandbox scene.
I want to press play.
Just make sure that everything is working before we add any new functionality.
Make sure that we don't have any errors.
Nothing's popping up in the console.
Just this serializ thing.
We can ignore that.
But no regular errors.
I can jump up and I can make it up onto my platforms and kind of test these all out.
So now I've got a spot where I can test out all of my different platforms.
Let's stop playing and create the new platform that I want to make.
Actually, let's commit our sandbox level first and then we'll do it in the next section.
So go into plastic and say that we added a new sandbox level for experimenting and testing and we'll check that in.
Now, we're going to create a new platform.
I want to start with a one-way platform.
It's an easy one to use and something that's really popular in platformer games.
So, to create a one-way platform, we'll just take one of our existing platforms.
I think I want the four wide.
Let's find that grass four wide.
And I'm going to duplicate it.
Sorl D.
I've got a second one.
And I'm just going to move it right down here kind of next to my player.
So, it looks like it's at a about a - 7 and a zero.
I'm going to rename this to one way grass platform 4.
It's going to be four wide and one way.
And then we're going to add in a newer.
So I'll collapse my sprite renderer and box collider temporarily.
We'll hit add component and we want to find this platformector.
If you search forector, you should see there are quite a few different types.
We've already added a buoyancy and now we're going with the platform one.
So add the platformector and you can expand it out and see that it's got a couple options.
It's got a one-way option, which is what we want.
And it has a rotational offset for having different tilts and different ways that you can get in through the platform.
But for now, we're going to leave it at the defaults.
And then zoom in a little bit.
If I look right now and press play, I should not be able to jump through this platform.
It's not going to work by default.
And you can see right here why there's a little warning saying theector will not function until there is at least one enabled 2D collider with used byector enabled.
So, I'm going to find the box collider and we'll hit used byector.
Now, if I jump up in through the middle, I can land on the platform and it looks pretty cool.
But, there are still some issues.
If I jump on the sides, my head hits on either side.
And I don't like that it looks the same as the other platforms.
So, we're going to make two more changes.
Let's stop playing because if I change anything else while we're running, it's not going to save.
Notice that used byector option is no longer there.
So, I'm going to stop playing.
Check the used byector.
And now look at that.
We can see the arc.
And then let's deal with the corners.
Why can't we jump up through the corners? That's because the other corners are done with separate colliders.
We have a polygon collider for the right and the left.
And while this is nice and gives us the little bit of rounding that we have there.
We don't need it for these one-way platforms.
There's absolutely no benefit.
There's just a downside.
There are two ways that we can fix this.
One thing we could do is add a composite collider.
When we do that, we'll have to add a rigid body, set it to static, and then it gets quite a bit more complicated.
Or we could alternatively uncheck autotiling, set the size here to be four.
So now that it lines up exactly.
If I set this to like a five, you can see how it goes over the edges.
Get the little It's very difficult to see with the green on.
Let's go into platform edit mode.
Actually, let's turn this into a prefab first.
We'll set it to four and then we'll turn it into a prefab so we can view this in prefab edit mode and then see it I think a little bit better.
So I'm going to go to the prefabs folder.
We'll take our oneway grass platform and I'm going to drag this in so that we have the the bigger icon mode.
It makes it easier to find a white space to drop onto.
Then I'll drag my oneway grass platform down here and I'll hit original prefab.
And now I've got my oneway grass as a prefab.
I'll double click on it to open up in prefab edit mode.
Double click again.
And now if I go and modify that collider.
So I take the size here, this X, and drag it up.
You should be able to see.
Okay.
Yeah, it's covering the edges at four.
It's actually right at the edge.
So I'll put it at four.
And then we just need to go down and make sure that we've removed the colliders from the two children.
Don't need those on here anymore.
The two polygon colliders from the left and the right because now this parent one is doing it.
We're not using autotiling, but that's totally fine because this platform is the size that it is and it's not going to change.
We'll go back, save, press play.
And now I should be able to jump through on both of the sides.
Let's verify that.
And then let's shrink this thing down so that it looks visibly different.
So run over here, jump up, and look at that.
I've got a nice one-way platform that I can go through on the sides and anywhere else.
I have to jump all the way up to the top of it, though, to make it through.
So let's stop playing and do the final part, which is the visual change.
I'll go back into prefab edit mode.
We'll hit that little arrow there.
And then let's shrink this down.
Instead of using the fullsized grass sprite, let's use the half one.
So I click on it.
It should show me the sprites down here.
And then I'll find the grass half mid and drag it in.
We'll go find the two children.
So we got grass half left.
Oh, this is right.
I've got the wrong one selected.
Let's go drag in half right.
And then for our left, we'll drag in half left.
Now there's one issue left, which is that my collider no longer matches up.
My collider is now bigger than my sprites.
I'm not using autotiling.
So, I need to modify the size of this.
First thing we'll do is set the size to half what it was.
So, instead of one, we'll go to 0.5.
And then we need to move it up.
Now, the amount we want to move it up, we could kind of figure it out by dragging it up and down.
But if you just think through the math, it's probably about half of five or.25.
There we go.
That looks pretty good.
I've got my collider right.
Remember, it doesn't matter exactly where that bottom is cuz I'm jumping up through it.
So, I think this will work.
Let's go back, save, and then let's find this platform.
And I want to just duplicate it one, two, three times.
Go select it.
But I need to make sure that this is collapsed.
So, when I do this selection, if I select it like this, and I put in my values that I want, L um 0, 12.
It's going to split out those children, too.
So, the children will get messed up.
And you can see those children right here are not in the correct place.
In fact, they're way up here, way, way, way above.
So, I need to make sure that when I do that, let's hit control-z and undo.
I collapse this one here.
Select just the parents.
And then I'm going to put in L 0, 12, and got to put my closing parenthesis.
And there we go.
Now, I've got four platforms stacked up neatly, and I should be able to just keep jumping up through them.
Let's press play, run over there, and do my jumps and see if I get all the way up to the top.
Whoops, I missed that one.
Didn't Didn't hold my jump long enough.
And it seems to be working.
So, I've got oneway platforms in and working.
I'll save my sandboxing.
Oh, got to stop playing.
Save my sandboxing.
Go to plastic and say that we added oneway grass platforms.
We can, of course, add more one-way platforms.
We just have to modify this prefab for our different sizes and different textures.
Let's hit check in, though.
Our next platform type is going to be a moving platform.
Something that the player can land on and move along with.
To get started, I want to use maybe these planet platforms.
I think that these look different enough and will be an indicator that this platform is going to move.
You could use whatever you want, but I think that this one kind of fits well with what I'm thinking.
So, I'm going to start by dragging a planet mid right out onto platforms and creating a new platform from scratch.
I'll name this moving platform six.
I'm going to make it six units wide.
I'm going to move it over here to the right holding control so that I get that quarter by quarter snapping.
And move it over to oh, let's just type in maybe an 11.
There we go.
And then I'll scale it up.
So to do that, I'm going to change the draw mode again from simple to tiled just like we did before.
And since I want this to be six wide and I want to have end pieces on it, I'm going to set a width of four.
Now, it does say that the tiling might not be right because it's not set to full wreck.
So, I'm just going to go set it to full wrecked on all three of the ones that I'm using.
I know it's not an issue, but I'm going to set it anyway.
Let's go find it right here instead of tight full wreck.
Just got to find the right drop down.
And then that should get rid of that little warning.
And I can add in my right and left.
So, I'll take the right drag it on to be a child of the moving platform.
Did it drop on? Nope.
Let's try that one more time.
I drag.
Let's try drag it and drop it.
There we go.
Got it in the right spot.
Now, notice that it's right here in the middle though.
It's at 0 0.
It says -1, but that's because it's offset from this thing's positive 11.
I'm just going to take this planet right, hold control, and drag it over so that it gets right into place.
It looks like at about 2.5.
I do the same thing with the planet left, drop it onto the moving platform.
Got to mix.
Get that drop right.
There we go.
And then hold control and snap it over.
into place.
Now I'll go to my moving platform.
I want to modify or actually I need to add a collider.
So add a box collider 2D.
Expand it out.
And then let's set the size to be right.
You can see right here the green is pretty small.
We're at one unit by one unit.
This is supposed to be a six wide one.
So a value of six seems about right.
Look like that just hit the edges.
And you can see if I grab and drag it up, it's going just past the edges and just inside.
So we want to set this to six.
Now I've got my platform.
It should just work as a normal platform.
There's nothing special about it.
Basically recreated the six platform.
Let's just go double check that though.
Make sure that I'm not crazy before we start making it move.
So we'll run over here any second now.
Soon as it finishes completing the domain.
There we go.
And run over.
It was completing a domain reload.
I just finished in the middle sentence.
There we go.
It can land on the platform.
Looks good.
So now I want this platform to move.
We're going to need a new script for that.
We're going to create a moving platform script.
And to do that, we'll go into the scripts folder, rightclick, choose create, and choose C# script.
Call this moving platform with a capital M and a capital P.
Again, no spaces in our script names, and we'll hit enter.
That should open up the code editor.
Probably won't go to the right thing, but it does look like it got my moving platform file opened here.
Now, if it doesn't happen for you, you of course just go back into the editor, double click the file again, and it'll probably find it.
Or you can go over to the right into the solution explorer, and then find it down here.
You might have to expand out your assets and scripts, but it should be there.
All right, now that we've got our update and our start method here, it's time to start writing code for our moving platform.
Well, first thing I want to do actually is delete my start method because I don't want to do anything at the beginning of the life cycle of this moving platform yet.
What I want to do instead is keep track of two positions, a starting and an ending position, and then move this platform between them.
I'll call those positions, I could call them like left and right, but then if I make a platform that goes up and down, it might not make sense.
So, I'll call them positions one and position two.
We'll make them serialized fields.
So, I'll start with a serialized field of a vector 3, and we'll call this underscore position one.
I'll duplicate it with control or command D.
and now have a position two in the update method.
What I want to do now is move my character between the left and the right or position one and position two some percent of the way.
So let's start by just making it so that we can control this in the editor.
And we'll say transform.position equals and we're going to get a position in between position one and two.
And to do that, we'll use the vector 3.lurp method, which does a linear interpolation, which is going to give us a value from position one to position two based on a percentage across.
So we'll put in position one as the first value, position two as the second value, and then our third value right there is a float or a parameter for the percent of the way that it's gone across.
I'm going to add an underscore PCT which will be percent or let's spell it P E R C N T say percent across.
I'm going to make it a big long variable name.
We'll add a semicolon and then we'll generate a field for that percent across.
So hit generate field and then I'll take the serialized field attribute and replace the private keyword with that cuz don't need the private keyword and that will make it show up in the inspector.
Now I'm going to add a range attribute range.
And we'll go from 0 F to 1 F.
And that's going to turn this percent across into a slider.
Let's save.
Go into Unity and attach this moving platform script to the platform.
So as soon as it finishes reloading everything, I should be able to select it, go add my moving platform.
I'll minimize the box collider.
Notice we've got this percent across me or percent across that we can fill in here.
But my positions right now are set to zero and zero and zero zero zero.
All zeros all the way along.
So if I just press play right now, it's not really going to do anything except for pop over to 0 0.
Let's just press play and verify that I'm not crazy.
And that that's the case.
Should go right to the center and just kind of pop into here and stay there.
And now no matter what I do with this slider, it's not going to change anything.
Nothing's going to happen.
Let's stop playing though and put in some values here.
Let's say that position one is our current position.
So 11 on the X and zero everywhere else.
And then position two, let's just move it five units to the right.
So we'll go a value of 16.
Now I'll press play.
And now it should start off in its initial position because that's position one.
And then let's go to the scene view so we can see it better.
As I drag the percent across, you'll see that it's going to go across to the right to position two.
Watch that value interpolate from 1116 all the way over.
And when we get to a full value here, now one thing that's kind of interesting is I could also adjust the y position.
Like maybe make the second y position be three units up or 3 meters up.
Now as I drag this, it's going to go up and to the right.
Pretty cool, right? And if I did like a negative three, it would go obviously down and to the right.
I could adjust this to be like a maybe let's not go with a negative, but maybe like a four.
And then suddenly it's going to go down and to the left.
You can kind of get the idea of how this is going to move based on the value that we put in here.
So, we're going to put in a value between zero and one and have it go initially just back and forth.
So, it'll go from the left to the right basically by moving this percent across value up and down.
All right, let's stop playing though and let's go into plastic and do a commit because we've got a moving platform that we can manually control.
We're almost to the point where it's automatic and I think that this is a good check-in point.
So, we'll say added a manually controlled moving platform and we'll commit.
Oh, we've got one error that popped up.
If that happens, just hit check in again and it should save.
There we go.
Before we make this platform move on its own, we're going to add some gizmos so that we can easily control where it's moving, the starting and the end position, and make it easy for ourselves and I guess game designers, if we have any on our team, to set these up without it being some big tedious process of trying to find exact positions and type those in.
So, we're going to start by opening up the moving platform script.
And down at the bottom of our script, let's see if I can get over to the left.
There we go.
We're going to add an ondraw gizmos.
This is going to allow us to see exactly where our platform will start and where it'll end and even see the current position of it along the slider.
So, if we move that slider, we see where it would be.
So, we're going to start with setting the gizmo color to red.
We'll do that with gizmos.color equals color.
It's a lowercase R and a lowercase C, but other uppercase G and C there.
A little bit confusing and a little bit unconventional, but that's the casing for it.
Next, we need to get our box collider and figure out how big it is so that we can draw a box that matches the size of our box collider.
So, we'll say var collider equals get component.
And we don't want to just get a collider.
We want to get a box collider 2D, which is what all of our moving platforms will have.
Next, we'll draw a gizmo.
So, we'll say gizmos.drawbox.
Or is it draw cube? I always get that mixed up.
It's not a box, it's a cube.
And we need to give it the position.
So our first position will be position one.
And then a size.
For the size, we'll use the collider.bounds size.
Now we'll duplicate that and do a another one for position two.
And save.
This should give me two boxes that show up as gizmos in the inspector.
Let's go see.
Well, in the scene view, not so much the inspector.
And they should show at the positions of my um my thing.
So there we I got one box to the left and one to the right.
And that reminds me that I want a wire box, not a regular cube.
So, we want a draw wire cube.
There we go.
Wire cube.
That's what I was looking for.
Let's save.
We'll go back in.
We should see them no longer be these big blocks that make it really hard to see what's going on, but instead be some normal cubes.
There we go.
I can see that's the start position and that's the end position.
If I move the start position over to maybe like six, oops, not 63, six, I can see that the block is perfectly aligned right there.
Now, I'm not seeing the current position based on a percent across.
I do kind of want to have that as a gizmo.
But I also wanted to show that if I move these positions up, like I put this up at like a two, you can see that it's going up and above and have this platform going across.
Let's go back into the platform and add another wire cube that shows the current position based on that percent across.
So to do that, we're going to copy line 15 or at least the right half of line 15 and we're going to use that as the position.
So we'll say var current position equals and then paste.
So we'll get the position based on the percent across.
Then we'll just draw another wire cube at that position.
So I'll copy line 23, paste it down to 26, and use current position instead of position 2.
The final thing I want to do is change the color so that we have some indication that this is the one based on the percent across.
And to do that, I'll copy line 20, paste it here as the new 25, and change the color to yellow.
Everything after the color change, we'll draw in that color.
So we just have to modify it right before we change it.
So now I should get a box that's going to show right here since percent crosses at zero in yellow.
And as I draw drag it across, I can see it moving over to the other line or the other the other square, the other edge.
Now I've got my box, I think, pretty much working.
If I press play, I can drag that percent across and it should move across just exactly to those two positions.
Let's just double check that.
So, I drag it and yep, it looks like it's going back and forth between those two positions.
But I want to do one more thing because I don't like having to go in and type these positions in.
Let's say that I want my second position to be, I don't know, up here or something, right? Right in this spot, and I want to get this position.
I could, of course, I go in and copy this and paste it in 11.75 and then paste in an eight.
And that'll kind of work.
But I'd like to add a shortcut so that I can do that a little bit quicker.
And to do that, we're going to go back into the moving platform.
And I think I'll do this right down below on draw gizmos.
We're going to add a method to set position one and set position two.
So make a public void set position one and it's going to be an expression body method because it's only going to do one thing.
So we're going to use the lambda statement which is the equals and the greater than.
And what we'll do is say underscore position one equals transform.position.
Now I'm going to go to the beginning of the line here with the home key and we're going to add some braces and add an attribute.
We're going to add a context menu attribute so that we can rightclick and pop this up by just right clicking on the inspector.
So, right or add that left brace.
There we go.
And we're going to add in the keyword context menu.
And then we need to open parenthesis.
And we'll put name of set position one and then close close parenthesis and a closing square brace.
So now I've got this here.
This could be on a separate line.
I could also do this one line above.
Whoops.
Let's see if I can if I can move that properly.
Cut.
Paste.
There we go.
So, I can do it one line above like this or I can do them as a oneliner so that it just kind of fits.
And I prefer to just do it as the single oneliner.
Then I'm going to duplicate it with control D and do the same for position two.
So, I'll just change these ones to twos.
And let's save.
Now, if I go back into Unity, I should be able to just move this thing to where I want it to be for that position.
right click and then set that position to kind of lock it in.
So, I'm going to drag it over and say I actually just want it to be across the water.
So, it starts on one side.
Maybe it even goes from that platform and then docks over to this platform.
Now, I'll right click on my moving platform and choose set position two.
And now my second position is going to be over there.
And I can see that it's going to move back and forth between these two spots.
With that done, I'm going to save my scene and then go into the project view and turn this into a prefab.
So, in my prefabs folder, I'll take the moving platform 6, drag it down, let it become a prefab, and now I should need to save my scene one more time to get rid of that star.
We'll go back into plastic and we'll commit our moving platform with gizmos or manually moving platform with gizmos.
Next step is to automate its movement.
So, we'll say manually moving platform with gizmos and we'll check that in.
Now, we're going to make this thing go back and forth on its own so we can see how our player works with it.
and then make our player work perfectly with it.
So, first thing we're going to need to do is open up the moving platform script.
And when we use the percent across, what we want to do now instead of just uh having it be manually modified by our serialized field or by the inspector, we're going to need to modify it over time or we're going to need to pass in a value based on time.
And to do that, we can use time dot time.
But time dot time is a value that goes from zero up to however many seconds that we have.
And what we really want is a value that goes from zero to one and then back to zero every second.
And luckily there's a method in Unity, well a method in the math library that does exactly this.
And that's the math f.
Pingpong method.
So what we can do is add a new line here on 15 and assign our percent across using that pingpong method.
So say percent across is equal to math f.pingpong and we'll use our time which is that zero to however long we've been playing value.
And then we need to give it the length to pingpong across.
So since we want a value from 0 to one, we put in a one.
Now this will give me a moving platform that moves all the way across um relatively fast.
If I want to get some speed control over that, I can multiply times a speed value and then generate a field for it so that I can modify this and figure out how fast I want it to go per platform.
So I'll take my serialized field, replace the private, and then set a default value of one.
So we know what that default is.
Then we can speed it up or slow it down, and we can have independent control per platform.
So let's go try that out.
All right, here we can see the platform moving back and forth.
Let's go to the scene view and check it out.
I can modify the speed.
Set it down to a nice 0.1 and it's going to go really slow.
I could turn this up to a one or there's an 11 or a one or a two.
And you can see I've got total control over how fast this thing's moving.
Let's go jump on it though.
Let's see if I can get up there.
Jump.
Jump.
I will make it.
I think.
See, did I make Oh, I missed the platform.
Okay, I'm going to make it onto it this time.
So, we jump onto the platform and look at what happens.
The platform moves and we can kind of follow along with it, but we're not moving with the platform.
We're moving up with it because it's kind of pushing us up and we'll move down and kind of fall down with it, but we don't get that left to right movement that we kind of probably want on a moving platform.
So, let's stop playing and fix that because that's the final thing that we need for a moving platform.
To do that, we're going to go into our moving platform script and we're going to add in two more methods.
First, I think I'm going to move these set position context menus up to the top.
Let's get them right up here so they're kind of out of the way.
I'm going to get rid of that update comment because I don't need it.
And I'm going to get rid of the private keyword.
Minimize on draw gizmos.
And then I'm going to add an on collision enter 2D.
What we want to do in this method is check to see if a player hit us.
And if so, make that player our child.
So we'll say var player equals collision.getcomponent or I know I need to get the game object.
So game object.getcomponent or we could also use the collider.getcomponent.
This would be the same either way.
We're going to get the player component.
And then we'll say if player is not equal to null then we want to set the players transform parent.
Wait.
Player.t transansform set parent equal to our own transform.
Now we'll do the same on the on collision exit.
So I'm going to get rid of that private keyword.
I'm going to copy this method.
Just control D and duplicate it.
And then I'll change enter to exit exit.
We get the same exact There we go.
We get the same exact structure, but instead of setting the parent to our transform, we're just going to set it to null or clear out the parent so that we're no longer parented to this this platform.
Let's stop or stop editing our code, start playing, jump on that thing, and see what happens.
Although, first, I think I want to move this.
Well, let's leave it up there.
I was thinking I want to move it down.
I think I'm just going to move my player up so that it's easier for me to run onto that platform.
Or maybe I'll just move this platform here over to the left.
I don't know.
Maybe I'll just hit play and run and jump on it.
I guess we'll see.
One editor update later and now I've got my platform working.
I've set it to 0.1 and I stick to it as long as I'm touching it.
I can walk right off of it or walk onto it and it just kind of works.
Let's see.
Get to the edge.
I can walk off.
Kind of little jump to make it back on.
But you can see my platform is working.
So go ahead and check this into plastic.
I just accidentally committed without recording.
So you're not going to see me do it on this one.
But just go through your change set, commit it.
I called this working moving platform with player sticking.
Now, we're going to add a new type of platform, one that our players can destroy.
And we'll start by going to our tiles folder and finding one of the bricks.
What we're going to do is create a standard brick like you would see in Mario that our player can jump up, hit, and destroy.
And then we'll add some other ways to destroy bricks as well.
So, we're going to start by just taking a brick.
And I'm going to drag it right out here.
Maybe next to this platform.
I'll fix the position to be a flat -3.5 and a zero so that it's perfectly aligned here.
And then we're going to go modify it a little bit.
First thing I want to do is rename it to brick.
I might name it brick brown, too, just so that it matches cuz we have a gray one, but I think I'll leave it as brick for now until I decide that I want to have a gray brick as well.
And then we'll add a box collider 2D to it.
Next, we're going to need to add a script for this thing so that we can make it destroy or make it get destroyed when we hit it.
Specifically, when we hit it from below, though.
So, we're going to create a new script in our scripts folder, and we'll call that the brick script.
So, rightclick, create a new C# script, and name it brick.
I generally like to name things after what they're going on until they get to a point where they become more abstract and they're used for multiple things.
Then, I might go about renaming it.
But since this is just a brick, I'm going to add it as a brick script for now.
It didn't open up my brick script, so I'm just going to double click and force it to open.
So, I've got my brick script here.
And what I want to do is deal with collisions from the bottom only.
So, I'm going to get rid of start and update cuz I don't think that I'm going to need those.
And we'll add an on collision enter 2D method.
On collision, enter 2D will fire off whenever we hit this brick with our player or anything else.
So the first thing we probably want to do is check to make sure that the thing hitting it is a player.
So we'll say var player equals collision.game object.get component and we'll get the player component.
This should give me back a player if we have one and if not we just want to return.
So I'll say if player is equal to null.
So if we don't have any player then return and do nothing.
So if we do have a player we'll continue on.
Otherwise, we'll do what's called an early exit where we'll just check to see if we have a player.
If we do, we'll save them off.
Otherwise, we bail out and don't run any code.
Return is just going to make it exit this method without running any of the code after it.
I'm going to get rid of that private keyword.
And then we'll add in the next bit of logic.
So, the next thing that we need to do is check to see if the player hit the brick from below or if they hit it from above or the side.
Really, we just care if they hit it from below.
And to check that, we can use the dot product.
First though, we need to get the normal of our collision.
So we'll say var or let's say vector 2 and be a little bit more explicit here.
Vector 2 and this will be our normal is equal to collision dot contact zero normal.
You can see it's going to autocomplete.
So this is the angle that we collided at.
And what we can do with it is use that vector 2 dotproduct.
Let's take a look at it right here.
And it takes in two different vectors.
So give it a left vector and a right vector or the first one and the second one.
And what it's going to do is return a one if they point in the exact same direction, a negative one if they point in the opposite direction and some value in between if it's close.
So if I give it a right hand side of up and a left hand side of a vector that's down because our our normal was down, then it's going to give me a negative one.
If I give it a right hand side of up and our normal was up, it's going to give it directly straight up and down, it's going to give us a one.
If it's at some angle, it's going to give us some value greater than zero and probably some value greater than 0.5 depending on where what the exact angle is.
So let's take a look at this in practice.
So I've got my normal here and then I'm going to get the dotproduct and I'm going to say float dot equals vector 2 dotnormal no sorry dot dot not normal and then we'll pass in our normal and vector 2.up as our second one.
So this is going to give us that dotproduct.
Then we're going to log it.
So we'll say debug.log and just write out that dotproduct just so we can see what it is.
And then finally, we'll say if the dotproduct is greater than let's say 0.5, then we want to destroy our game object.
So we'll say destroy game object.
And that's going to destroy our brick.
Let's try that out real quick.
See what it looks like and then see if this code and logic is correct or if we might need to invert or switch this.
So we'll jump over to Unity.
We'll press play.
And I'm going to run over.
We'll go to the console tab.
Oh, that platform is moving a little fast.
Jump and take a look.
Well, I didn't add the brick script.
So, we didn't get anything.
So, I'll add the brick script to our brick.
And then we'll jump again.
And we can see that we got a one and the brick was destroyed.
Let's stop playing.
Go add the brick script in not play mode.
And then let's go land on top of that brick and see what it does.
make sure that we can jump on top of the brick and it doesn't break.
Or we can hit the brick maybe from the side and it also doesn't break.
So if I hit it from the side, you can see that the normal was a zero.
And if I go up to the top, we see that that normal is a negative one.
Here you can see I got a negative.5 or whatever when close to that when I was jumping sideways.
And if I come at it at an angle, you see that we still looks like we still got about a one on that normal because we hit perfectly flat up and down.
So, that looks good for destroying our first brick.
Let's turn it into a prefab, though.
So, we'll go into the project view.
Go into our prefabs folder.
That's starting to get a little bit full, but we'll split this out soon.
And we'll take our brick and drag it in.
Now, it's a prefab.
And we'll save off our sandboxing.
I'm going to go to plastic and say that we created a brick that gets destroyed from hit with hits from below.
So added brick that destroys when hit from below and check in.
Now we're going to add some visual indication when our brick is destroyed.
Beyond just the brick disappearing, let's add some particles of little bricks flying away.
And to do that, we're going to need to create a new particle system.
We'll go to game object and choose effects and particle system.
I'm going to name this brick break particles.
And then we need to first create a material so that we can assign our texture here and get this showing up.
If you look down at our particle system underneath the renderer section, you'll see that the default material is here.
It's the sprite lit default.
And that's not really helpful.
We need an actual material that shows some sort of a block.
And if we look at the particles folder here, you see that we actually have a broken little brick brown object or texture that we can use.
So I'm going to create a new material that uses that brick brown.
We'll rightclick and choose create.
And we're going to choose material.
Now, we need to give this a name.
I'll call it brick particle.
And then we need to choose the material shader type.
So, there are a couple options here for particles.
First thing we need to make sure that we do is go to the universal render pipeline because that's what we're set up to use.
And then go into the particle section.
Here we can choose lit, simple lit, or unlit.
I would often choose lit, but what we need to do actually doesn't work right with the lit particles because I want my bricks to eventually fade away.
And right now, that only works with the unlit shader.
So, I'm going to choose the unlit shader, which will work totally fine for what I want to do.
And change the surface type from opaque to transparent because I want to be able to fade away the alpha and make these things just kind of smoothly disappear.
Next, we'll assign the texture.
So, I'll take this brick brown and drag it right into that base map.
And then it hasn't updated here yet because we haven't assigned that material to our brick particles.
So I'll go select the brick particles.
We'll expand out that mesh renderer again.
Just click again on the big bar here, not the check box.
You don't want to turn it off.
And then drag the material over to the material section.
Now you see a bunch of bricks going flying up in the air.
There are a couple things that I'd like to change though.
First, I'd like these to fly off in just kind of a burst instead of all at once or instead of consistently.
So, I want them kind of like blast off all at once, not in a in a consistent stream of them.
So, we'll go to the emission section and change rate over time to zero and hit plus to add a burst.
Here, we can control the number of things in the burst by adjusting that count.
But before we do that, let's change the shape that they're bursting out at.
Instead of them going up and out, let's make them go all directions.
We'll expand out shape and change the shape from cone over to sphere.
In fact, let's go to the scene view real quick before we do it.
So, you can see the cone right here that it's using.
If we change this over to a sphere, you'll see that now they go off in all directions.
Now, I also want to shrink these things down.
I don't like the size of them at all.
They're way too big.
So, I'm going to go find the start size up here at the top and change this to about a 0.5.
I'm going to change the start lifetime to about 75 so that they go pretty quick and they can disappear over time.
Then we're going to go do that disappearing over time part.
So that's underneath color over lifetime.
If I expand out color over lifetime, I get a popup here.
And well, first I've got to turn it on.
I'll get a popup when I click on this.
And if I go to the top right bar here, I can adjust the alpha at the end of the life cycle.
So I drag this all the way down to zero.
And then my brick particles should start pretty good and then disappear halfway along.
Now, I don't want them to disappear right away.
So, I'm going to add another point right up here where the alpha is all the way at 255.
So, they don't start blending away until about halfway through their life cycle.
To do that, I just clicked up at the top.
And I think I'll drag this over even more to probably around like 80%.
In fact, I I might even just type in an 80 there.
So, at the last 20%, they'll just fade away.
So, there's my bricks.
They're looking okay.
Let's change that.
I'm going to pick put that to 60.
I want to change this a little bit more, though.
I want to make these things rotate and kind of spin randomly and maybe even shrink over time, too.
So, to do that, we can find the rotation over lifetime.
Expand that out.
And if I leave it at just a default of 45, you see that they'll all spin the same.
I want them to be somewhat randomized, though.
So, I'm going to choose the random between two constants from the drop down there.
And put a negative 180 and a positive 180.
So, that way they'll all spin totally randomly.
And it'll be a little bit, you know, varied, I guess.
So, let's watch it in here.
See, they all kind of spin.
Looks good.
The last thing I want to add in here is a size over a lifetime.
So, I'll expand that out, check the box, and do exactly the same.
I'm going to hit the drop down, choose random between two constants, and put a let's go with a 0.1 or 0.5 and a 0.1.
So, we can go anywhere from our initial size to all the way down to 0.1 depending on uh what we randomly pick for that particle.
So, now I've got some particles that I think look okay.
They look pretty good for when I destroy a brick.
The next thing I need to do is assign them to my brick.
So, we'll go to the brick.
We'll go open up that brick script and we're going to add a serialized field at the top for a particle system.
So, I add a serialized field.
Call this particle system.
And I'll call this brick particles.
Now, when we hit our brick, we want to spawn some brick particles so that our player can see them um as well as destroying our object.
So, I'm going to copy the brick particles.
And right here on line 19, we'll add some braces because we only want to do this if we're actually going to destroy the object.
We don't want to call this code if we're, you know, landing on top or something else.
So, if that product is good and we should be destroying our game object.
Before we do that, we will instantiate a particle system.
So, I'll paste in my particles at our transform position and we'll use the quatian identity for the rotation.
And again, that's just the default rotation value.
It's like passing in um nothing or just face the normal default direction.
So, we're just going to give it that.
Save.
Jump into Unity.
And let's go see if we get a particle system that appears and shows up when we break a break a brick.
So, hit play.
Oh, I've got to assign the brick particles.
Here's what I'll do.
While we're playing, I'm going to drag this brick particle in here and assign it.
run over here, jump and hit it and see if it actually works.
Okay, so that worked.
We got the brick there, but we still need to make this into a prefab and uh probably make it so that it doesn't keep looping.
I don't know if you saw that appearing there.
So, next steps are just go into our prefab folder, take our particles and drag them in.
Then go find our brick and assign the brick particles to them.
Then we should probably apply the overrides to our brick script.
And then finally, let's go adjust that brick particle one more time.
So, I'm going to delete the placed one here.
Go double check that our brick doesn't have the reference to the placed one.
It's actually referencing the prefab.
Then, we'll go open up that prefab.
And I want to uncheck the looping option because I don't want this thing to loop.
I want it to kind of destroy itself or clean itself up.
I'm also going to change the duration from a five to a one because the lifetime is 0 75.
So, this thing should end at about a one.
And then I can probably figure out a way to clean that up.
So, let's go back, save, press play, go one more time, break a brick, make sure that it works, and that I only get one particle, and then we'll do a commit.
So, run over here.
Let's go land on top of it first.
Seems good.
Hit it from the side.
Seems good.
Hit it from below.
The brick breaks and disappears.
So, it's looking good.
Let's go into the plastic setup and commit our changes.
First, I'm going to save my sandbox scene, though.
Make sure that it shows up in here.
So, we added brick break particles and we'll check that in.
Right now, when our player jumps and breaks a brick, you'll get a particle system that appears and shows the particles, but then it never actually clears itself out or goes away.
So, this is fine if I've got a single brick, but if I added hundreds of bricks and destroy them all, my hierarchy is eventually going to get filled up with a bunch of different particle systems that are no longer running.
And that doesn't seem like a good idea.
It seems like something that we should definitely clean up.
We want to keep the hierarchy clear and cleaned up of all these objects so that we don't have to traverse through them.
It'll speed up the game just a little bit, but also make it a lot easier for us to manage things.
So, what we're going to do now is a small challenge.
What I'd like you to do is write a single script, a simple script for your brick particles that will destroy them when they're done playing their particles.
Now, there are multiple ways that you can go about this.
I'll show you my simplest solution right after we go through the what the actual challenge is, but I'd like you to come up with a solution that cleans up the bricks and just destroys them for now.
We'll talk about pooling them and putting them back into a pool later.
So, don't dive that far ahead.
Instead, just get rid of the bricks after they're done so that we can put as many as we want in here.
We'll spawn bricks and then they'll despawn.
And later we'll talk about some of the benefits or optimizations that we can do to make that even better.
So go ahead and take this challenge on create your brick particle script and then see if you can figure out how to clean it up.
All right, I'll assume that you've either gone through it now or decided not to and just want to see the solution.
So we're going to rightclick create a new C script and I'm going to call this brick particles.
Let's fix my caps lock there.
brick particles and then I'm going to assign it to my actual brick particles.
So I'll go find my brick particles, which is my prefab right in here, my brick break particle, and then we'll assign it.
So I've got my brick particles script, and it's now attached to my brick particles.
I'll open up that script, and what we want to do is destroy this object after some amount of time.
So, we'll in the start method, I'll just say destroy.
We'll pass in our game object, and then we'll give it a parameter for the amount of time to delay.
And the amount of time that we want to delay is just going to be whatever that particle systems lifetime is.
So, I'm going to add a line up above to get our particle system.
I'll say var particle system equals get component particle system.
There we go.
And then for our second parameter, I'll paste in that particle system variable.
And here we have a duration, but that's not what we want to use.
If I put that in, you'll see that we get a little deprecated message saying the duration of particle system in seconds read only.
But right below it, it says particle system.duration is obsolete.
The duration property is deprecated.
Use main.duration instead.
So what that's saying is this used to be the way to do it, but they've changed it and now you want to actually access it through particle system.
That'll get rid of the error.
fix the problems and make everything work.
I'll get rid of this update method and that extra line at the end.
I'm even going to get rid of these two using statements that I don't need.
All I need is that using Unity engine.
That's why they were light gray.
So, the light gray ones, I can just delete those out.
I'm going to save, do a build, and now I should have particles that clean themselves up after whatever the duration of that particle system is has expired.
So, let's go check that out and see if that's the case.
I should now be able to Well, let's duplicate my brick.
So, let's put two bricks here side by side.
Go break them both and make sure that I end up with no particle systems in my scene after the 75 or 1 second or whatever it was that I I set my thing to.
There we go.
Looks good.
My particle systems are self-destroying.
So, let's go back into plastic.
Make sure that I've saved my scene.
I've got my second brick here.
So, we made particles or brick particles self-destruct.
Now, you might be wondering, should we make this more generic for other particles? We'll do that later.
Once we have some more particles, we can probably rename this to self-destroy particles or something else.
But for now, we only have brick particles, so we'll name it for the thing that it is, and it's easier to find that way, easier to manage, and then less abstract until we actually start to use the abstraction.
So, check that in.
Another brick issue that I want to address is the way that our player deals with hitting multiple bricks going up.
So, I'm going to duplicate our first brick, hold control, and move this up one meter or one unit.
So, it's at a one on the Y.
I'm going to press play, run over, and I'm going to do a big jump where I just hold and jump up into the bricks.
Let's see what happens.
Come over here, and I hold space.
Oops, I messed that up.
Let's try it again.
Let's go back over to the right and try it one more time.
I hit the uh the grass there.
So, it messed up my demonstration.
Let's go destroy this other brick off to the side.
There we go.
And then do a big jump.
So, you can see here when I jump up and I hit things, I just kind of go right through them and I continue on.
And what I like to happen instead is if I jump up and hit one of those blocks, I want it to kind of knock me back down just like it does like in a Mario game.
You break a brick and you get pushed back down just like you hit your head on anything else.
So, let's make that change.
Now, what we can do to change that is simply go into our brick and when we hit with a player, what we'll do is tell our player to stop their jump.
So, right here, when we've actually taken a hit from a player, we'll say player.stop jump.
Now, how we're going to implement that stop jump, we can figure that out later.
We just know that when we hit this collision, we definitely want to cause it to stop jumping.
So, we'll hit alt enter, generate a method that's right now going to throw an exception, and then we'll hit F12 to actually go look at that method and figure out what it might want to do.
So, to stop a jump, let's go look at our code.
How do we currently stop a jump when we release the the jump button? So, if I let go of my jump, then our jump stops.
And how does that happen? Let's go find it.
Let's see.
Where's our code? um right here.
So, we're checking to see if they're still pressing the value and the jump end time is greater than our current time.
So, here we're just checking to see are they still holding it down and do they still have some jump time left.
Now, it'd be hard to override whether or not they're still holding it down.
And we probably don't want to lie to ourselves about that.
We don't want to go in and change this input action and say, "Oh, yeah, they're not holding it down." But instead, what we could do is just set our jump end time to the current time so that uh their jump has to end right away.
So, we'll just go down into our stop jump, modify this to say jump end time equals time.
We'll make this public instead of internal just because I like the consistency of the the wording there.
And then we'll go into Unity and let's try it out.
What I expect now is that my jump should end the second that I hit my head.
Now, I have not stopped myself from double jumping.
If I wanted to do that, I could also just set my jumps remaining back down to zero, but I think that I kind of want to leave double jumping alone right now.
So, I'm going to jump and oh, I still didn't get knocked down.
Let's go make sure that I've actually saved my code.
So, go back into Unity.
Oh, and I didn't save it on the brick.
There we go.
Save the brick so that it actually calls stop jump.
That's why that little star was there.
So I'll press play one more time.
So again, an important reason that I usually hit control shiftb and do a build when I'm in the code editor.
So that way catches all of the code files that I've changed, not just whatever the one that I have open is.
So here, let's do a jump.
I'm going to hold it again and got knocked back down.
Perfect.
That's the behavior that I expect to see.
So save my scene.
I've got that new brick in here.
go back into plastic and say that the player gets or player jump stops when breaking a brick.
And we'll check that one in.
Now, we're going to add lasers to our game.
Before we put lasers in our player's hand, I want to put them on the floor with some switches that we can use to toggle on and off.
To do that, we're going to need to grab the KennyL pack that has all of the requests.
This is the platformer art requests pack.
I'll link this down below, but you can grab it and then open it up and you should find inside there's a tiles and a vector folder.
I'm going to go into the tiles folder.
What we're going to do is just copy this entire entire folder.
In fact, what I'll do is actually go up one level.
I'll copy this tiles folder.
I don't need the preview or the vector ones.
And then I'm going to go into my project folder.
So, find my project folder, go right into the art subfolder, and I don't want to put it into the tiles folder.
Instead, I'm going to create a new subfolder called um let's call this lasers.
It's requests, but I want to call it lasers because that's what it actually has and it is my lasers.
I'll hit show in explorer in that folder.
We'll go into the folder and paste in the tiles subfolder.
So now I should get that other folder of tiles right in here.
There we go.
And then finally, I'm going to go into this folder.
I think actually what I want to do is select everything.
So, I'll go in the folder, Ctrl+ A, and I'm going to hit Ctrl X, go up one level into the lasers folder, and paste all of my files into here.
Now, I can get rid of this extra tiles folder and just have a lasers folder with all of my files in it.
There we go.
The paste just finished.
My tiles subfolder should be empty.
I could have also just selected all of those files from the zip and pasted them in as well, but I did it slightly different, and I just wanted to show show that process.
So, here I should get my lasers all importing.
So, it's going to be lasers and beams and other things.
I need to make sure that I set the pixels per unit here.
You can take a look at these and see that these are actually set to 70 by 70 on all of these textures.
So, what I want to do is select the first one, go down to the last one, hold shift, and hit select.
And I can see that, oh, one sprite is selected.
So, I need to go find the one entry that's not correct.
And if I can't tell what it is, the easiest way to do it is to just drag this list down.
And I should be able to see the one entry that looks slightly different.
Let's see if I can find it.
I have not found it yet.
But I can also just scroll through here until I see it change.
Why am I not see Okay, maybe.
Let's go start to end.
I am not finding the one that's bad.
Do I have one expanded? I'll just hit the down arrow until I find the one that shows no.
Oh, here it is.
It's this one right here.
Ah, laser blue vertical was expanded.
That was causing the problem.
So, with it collapsed, I'll hit home, shift, end.
That should select them all.
Perfect.
And then I'm going to set that pixels per unit to 70 so that it matches with these sprites that I've just pulled in.
That should make it so that each sprite is still 1 meter by 1 meter.
Let's go check that out.
I've got my sprites set and I'm going to take um let's see what's a good one to grab.
Let's do this blue laser.
No, let's take the yellow laser switch.
I'm going to take it, drag it right out here.
Yeah, I can see that looks like it's about one cube by one cube.
In fact, it should be exactly one cube by 1 cube.
So, drop it out.
I'll fix up the position to be a four and a negative 3.5, which is just where my ground is.
And then I'm going to rename this to laser switch.
It's defaulting to the off position.
That's the one that I grabbed the off.
So, it's off to the left.
And I expect that when I push it to the right, I want to make it change to that.
And then turn some laser on.
The next thing I'm going to need to do is create a script for this.
I'm going to need some sort of a laser switch script or a toggle script or something like that.
I'll go into the scripts folder, right click, rightclick, and choose create car script.
We'll call this laser switch since that's what we're putting it on.
And then once that script is created, as soon as it finishes, there we go.
I'll go minimize the code editor and I'm going to assign it to my laser switch.
Let's go select it and assign.
Now, there are a couple things that I want to do with this switch.
I want to change the graphic and then I want to make it toggle or do something.
And I want to have it interact when I walk through it.
So, if I walk forward through it, it'll turn on.
If I walk backwards through it, it'll turn off.
I could also bind this up to a hotkey or something.
So, I could toggle it on and off.
But, I'm thinking right now it's just like walk through it, walk to the right, it turns on.
Walk to the left, it turns off.
So I can accomplish that by opening up my laser script.
And first I'm going to add some references for the two images that I want to have the on and the off images or the left and the right sprite.
So I add some serialized fields here up at the top.
I'll do serialized field and this will be a sprite.
I'll call this underscore left and then I'll duplicate it and make an underscore right.
So I've got two sprites there.
I'm going to delete this comment about the start method.
In fact, I'm going to rename start to awake because I want to just cache and save a variable, which will be our sprite renderer.
And I tend to cache and save variables in awake so that they're ready for anything else that might need them later.
So, I'm going to put it underscore sprite renderer equals get component and we'll give it a sprite renderer type.
There we go.
That last one.
one.
one.
Now, hit home, alt enter, and generate a field for it.
So, we've got that sprite renderer.
I'm just going to go to the private keyword and hit enter so I can get a new line and get rid of it all at once.
And then we're going to look for an on collision or an ont trigger stay.
So we're going to delete the update method and we're going to add an ont trigger stay 2D.
What this will do is fire off or get called every frame we have something inside of our trigger area.
Now we're going to add a trigger area in a moment.
It's very simple.
It's just like adding a collider.
But we can do some extra in or get some extra info with this because we can stay inside of it.
We can now look at the player and see what direction the player is moving and then turn ourselves on and off based on what direction that player is moving.
First thing we need to do though is make sure that we're actually colliding with a player.
So we'll say var player equals collision.get component and we'll get a player.
Now, this is able to get me the component from the collision because it's named collision, but this is actually a collider 2D.
The the name of this variable by default, I think, is terrible.
It should probably be collider, but it's named wrong or named oddly, so you can still get that component.
If this was a collision 2D, you would have to get the game object or the collider object first.
But since it's a collider 2D, you can get it right away.
Now, if we don't have a player, we want to return and do nothing.
So, we'll say if player is equal to null, then return.
We're going to do another one of those early exits because there's no player here, nothing to read.
Next, we want to determine what direction the player is moving.
And to do that, we're just going to read or access the rigid body.
So, we'll say var rigid body.
Let's see if I can spell it right.
RID body equals.
And here we'll do player.get component.
And we'll get the rigid body 2D.
Once we have that, we should be able to tell what direction the player is moving.
So, we can say if rigidbody velocity.x is greater than zero.
So, if they're moving to the right, then let's uh turn it to the right mode or turn it on.
So, we'll say turn on.
I'll hit alt enter and generate a method for it.
And then if they're going to the left, which would make their velocity dox less than zero.
So zero means they're not moving at all.
Positive X means they're going to the right and negative X means they're going to the left.
So if they're going to the left, we'll just turn it off.
And to do that, I'm going to duplicate lines 25 and 26.
I'll select them both.
Ctrl D, click right here, and hit enter.
And then add the word else.
So else if the rigid body velocity is less than zero, so switch that greater than to a less than.
Then we'll call turn off.
We'll generate a method for turn off as well.
Make sure that you don't rename turn on to turn off.
But we just want to generate a new method.
And now we've got a turn on and a turn off method.
The final thing that we'll do in this section here is update our sprite so that our sprite renderer shows either the left or the right sprite depending on if we've turned on or off.
So in the off mode, we'll set our sprite renderer sprite to the left one underscore left.
And I'll copy that line down for turn on and we'll set it to the right sprite.
So now we should get the toggle happening when we run through it and having it switch our sprite back and forth.
But before that happens, we're going to need to add our trigger and assign our two sprites.
So first, let's assign the sprites.
We'll go to the lasers folder.
We've got the off sprite for left and the on sprite for right.
Then we'll go add a component and we're going to add a box collider 2D.
And the important part here is that we need to make sure that we check the is trigger box.
That'll make it so that our player won't actually collide with it, but it'll instead just call back into our on trigger methods.
On trigger enter, on trigger stay, and on trigger exit.
Right now, we're just using on trigger stay.
And it should switch our sprite back and forth.
Let's hit play.
Run over here and check it out.
So, I run to the right, it switches on.
Run left, it switches off.
So far so good.
I can toggle this thing back and forth pretty easily.
Now, I just need to make it actually do something.
Before we do that though, let's stop playing.
make sure that we've saved our scene with our laser switch and go in create a prefab out of it.
I'll go to my prefabs folder and I'm going to take this laser switch.
I'm going to name this yellow laser switch cuz I might want to add multiple lasers with different colors and I'm thinking I probably will.
I'll drag that into the prefabs.
Save our scene.
Go to plastic.
So, we added the yellow laser switch and check it in.
Now, we're going to make our switch functional.
We're going to do that by turning on a laser blaster.
So, we're going to go into our lasers folder again and take this laser left.
And I want to drag it right up here to about a one and a one in my positions.
This will line up perfectly with what I want to do.
I want to make a laser that can blast this block when I turn this light or turn this switch on.
Now, I've got my laser.
I'm going to name it laser and get rid of that lowercase laser left part.
And we're going to add a new component, one that we haven't used before, and that's the line renderer.
So, hit add component and search for line, and you'll find a line renderer.
This is a nice component for drawing lines of an arbitrary size or beams or other things where the size is going to change.
We could alternatively add in a sprite and kind of manually adjust it and tweak things, but align renderer allows us to do a lot of really cool things and does it really well very easily.
One thing that you're going to notice though is that by default you're just not seeing anything.
And that's because if we expand out the positions in our line renderer, by default it starts at 0 0 to 0 01.
which means that if I go into 3D mode in my scene view, I can actually see a line that's peeking down from the center and going back one meter into our game.
That's not the view that we want, though.
We're not in 3D.
So, we need to change this around and first zero out that Z position.
So, now I should see absolutely nothing.
If I change the starting index to match my position and make this a one and a one, you start to see that there's a line at least showing up.
If I go into the game view, I can see that it goes from 1 one to 0 0.
0 0 is 0 and 1 one's right there.
Let's make it go over to the left.
So, I'm going to add the Y of one so that it stays the same.
And then I'm going to put in a3 here for the X.
So, I've got a purple beam going from here all the way over to the -3, 1 line.
We're going to write code to do this dynamically later, but we're going to start by doing it manually.
Next, we need to turn this purple line into something that looks more like a laser blast.
So, we're going to create a new material for our laser.
I'm going to right click on the laser yellow, choose create, and choose material.
That's not going to assign the texture, but it should at least give me the correct uh the correct render or the correct shader up here.
And then I'm going to go scroll up in here.
Let's see if I can scroll up.
Oh, I've lo Oh, I've got my Where did my material go? I didn't name my material.
Let's go find it.
It's named new material.
Where did it go? LM new material.
We'll call this yellow laser blast.
And what we're going to do is assign that yellow laser to it.
So, I'll take the yellow laser, the horizontal one, and drag that into the diffuse.
Next, we'll go back to the laser, and we need to assign that material to the laser.
So, we'll scroll down to the materials section, expand it out.
You should see something that looks like that.
none assigned.
And we'll drag in our material.
And look at that.
We've got our laser showing.
It is showing on top of our laser blaster, though.
And that's just because of the sprite layers that we've got set up.
Yours may or may not be showing that way.
If we go take a look at our sorting layer right now, it's on default.
I'm going to change this to be on props.
And I'm also going to change the sprite renderer up here to be on props.
I need to go find my where's that at on my sprite render under additional settings.
We go find props and then I'm just going to pull this forward one value.
So I'll put the order and layer here to one so that my laser shows up or my laser emitter, the blaster thing shows up on top of the laser and it looks a little bit better like that laser is coming straight out of there.
Now I need to go into my laser switch and make it so that my laser switch can turn this thing on and off.
To do that, I'm going to go into the laser switch code, and we're going to add in what's called a Unity event.
This is going to allow us to assign things just like we did in buttons, but to our own code.
So, right up at the top, we'll add two more serialized fields.
A serialized field that's going to be a Unity event.
And I'm going to Whoops.
Let's call it Unity event.
There we go.
And I'll name this underscore on.
Now, I'm going to add in a using statement here.
So there's a using Unity engine.events.
If I hit enter on that, it should appear right up at the top.
And now Unity event shows up.
So if you're not seeing Unity event, it wasn't looking right.
Just make sure that you've got the using statement up there.
It should automatically add it.
But if it doesn't, you can hit that alt enter and make sure that it gets added there and that you've got the correct one.
Now I'm going to duplicate this line with control D and add an off event.
And then down in our turn off method, we'll say underscore off.invoke.
And in our on method, we'll say underscore on.invoke.
So this should turn on every time that we move right and turn off every time that we move left.
Now, right now, we're actually doing this constantly.
We're doing this many, many times as we move across.
We'll deal with that later, though.
Let's first go in and make sure that it works.
So, we've got our on event here showing up and our off event.
In the on event, I'm going to hit plus.
I'm gonna drag in my laser here.
I'm going to go find the line renderer and I'm gonna check the enabled box.
I'll check that box there.
So, I selected enabled and then checked the box.
Now, I hit plus on the off and we're going to do the same except I'm not going to check the box.
So, drag the laser in.
I'll go find that line renderer, take the enabled flag and leave it off.
Right now, all this is going to do is toggle the visual effect.
It's not going to make it actually functional yet.
We'll swap that out and we'll change these references soon.
But first, let's make sure that we can actually turn it on and off.
So, I hit play, make sure that I've saved my scene, and I should be able to now walk back and forth and turn that laser image on.
It's already on by default, and off.
Oh, it didn't turn off.
The way that we have our switch set up right now is a little bit rudimentary, and it's definitely not what I would recommend longer term.
Right now, we're accessing the line renderer and turning that on.
And we really want our laser to deal with all of that.
The laser should turn its visuals on and off, deal with damaging things and all of that stuff.
So, what we're going to do is move some of the functionality from our laser switch over to the laser, make that thing a lot more intelligent, and add a little bit of extra intelligence to our laser switch.
Let's start by going to the laser and adding a new script.
We're going to go to our scripts folder, rightclick, and choose create and car script.
and then give this a name of laser with a capital L.
I'll go assign that to our laser as soon as the code editor does its whole thing.
Pops up and then I minimize it.
And then what we're going to do is make this laser script deal with turning that on and off.
And then of course blowing things up.
And like I said, we're going to modify what we call from the laser switch.
So let's open up our laser script.
And let's first get a reference to our line renderer.
We'll do that in an awake.
And I'm going to delete the start and update methods cuz I'm not sure if we're going to use them yet.
Well, I know if we're going to use them, but I don't want to spoil it yet.
So, we're going to start with an awake.
And in awake, we'll say sprite renderer or line renderer, not sprite renderer equals get component line renderer.
That should get us our line renderer.
We'll hit alt enter on the field on the the name up here and generate a field for it.
And I'm going to go delete both of these private keywords.
I'll just go to the beginning and hit shift, not shift delete, control delete and controldelete to delete out those private keywords.
Now I've got my line renderer here and I want to add a method to my laser to toggle it on and off that will just for now start by disabling and enabling the line renderer.
So let's add a public void toggle that takes in a bool which will be the on or off state and I'm going to call this state.
Now, if the state is true, we're going to set the line renderer to enabled.
And if the state is false, we're going to set the line renderer to disabled.
And to do that, we'll just say line renderer.d equals state.
I don't have to add an else or an if else or any of that.
I can just set it to true or false based on what I pass in here.
I'm going to save this off.
And then we're going to go into our Unity editor and then go modify those references in our laser switch.
So on the laser switch, instead of calling line renderer.enabled, we're going to call laser.toggle, which is right here off at the bottom of the screen.
So you might not have seen it.
Let's collapse these two.
And we'll select it down here for the second one.
Laser and toggle.
So it'll toggle on and toggle off.
I'm going to save, press play, and then I should expect to be able to run over there and get exactly the same functionality.
Let's go see if that's the case.
So, I run over, turns on, turns off, turns on, turns off.
Now, I should probably have my laser turn off by default.
So, I'm going to go back into the laser script.
And inside of our awake method, we'll just say toggle false to just turn our laser off.
Now, you might wonder why we just turn the line renderer off.
It's cuz in toggle, we're going to end up doing quite a bit more, or at least a little bit more to determine whether or not we should be updating and drawing a line renderer.
So let's start by adding it in a state or a permanent state.
So instead of just keeping this state here and using it and then go having it go away when we leave our method, let's turn this into a member variable or a field inside of our laser.
So I'm going to say underscore is on equals state.
We'll generate a field for that named is on.
And I like this name for it because it makes it very obvious.
If it's is on is true, then the thing is on.
If it's off, then it's false.
So, it's very very clear.
I'm going to delete out that private keyword that we don't need and then save this out.
Let's go back into our laser switch now because I want to take a look at a little performance issue and a little minor optimization that we can do that kind of matches what we've just done here with our is on.
So, in our laser, our turn off and turn on methods are actually getting called quite often.
If I add a log, we can see just how often that's happening.
Let's do that.
Let's say debug.log.
And here I'm just going to put in the word turn off and a semicolon.
And then I'm going to select this line, copy it, paste it down here to turn on, and put in the word turn on.
So now I can see how often these things are called.
Let's go into Unity.
We'll press play.
We're going to run over there, turn this switch on, and turn it off again.
I should expect my laser to be off by default because we added that code to the laser.
There we So, it's off.
And if I run over here, let's go to the console first.
Clear out our log completely.
Run over.
And you'll see that oh, I had 17 entries.
If I unclap, you'll see that it called turn on 17 times.
If I go over here to the left, turn off got called a whole bunch of times as well.
If I collapse, it looks like it was 27.
The reason for that is every frame that we're in this trigger, we're running this code.
The code right here on trigger stay.
So, we're checking the velocity and then calling turn on and turn off.
This part is okay.
Running this code to check to see if we're hitting something or we're in something is all right.
The get component calls are slightly less than optimal, but it's not bad at all.
The part that we probably should optimize is inside of our turn on and turn off methods.
What we could do is instead of invoking this off and toggling the sprite or changing the sprite multiple times when it's staying exactly the same, we can just say, hey, if we're already off, don't do anything.
If we're already on, don't do anything.
So, let's do that by writing some code in our turn off first.
First, I think I'll get rid of the private keyword here and that private keyword there.
We'll get rid of all these extra privates.
And then inside of turn off, we'll say if underscore is on and then I'm going to let it autocomplete and add my braces.
I'll put the closing brace at the end of my big long statement.
So if it is on then we want to call the off invoke turn the sprite to left or off and then turn or write off our debug log.
But we also want to say is on equals false.
Now I need to generate a field for is on.
It looks like it automatically generated it.
But if it didn't generate for you, you can just generate a field.
Alt enter and you should get a private bool right up here.
Or you can scroll up and just go type it.
Put it right below your sprite render and remove that keyword that private keyword again.
Now in the turn on method, we'll do the exact opposite.
So I'll just copy lines 38 and 39.
Paste them right here and then add in a closing brace and we'll say if is on is equal to false double equals false to make sure that it's not true.
So if it's not on then we'll turn it on.
So on the next line we'll say is on is equal to true.
We'll toggle it on and off.
Now if we go into Unity we should see that this method is on and is off only gets called once.
it won't toggle back and forth or it won't retole the same thing multiple times, spam out that log and then be trying to do things to our laser.
So, let's go check that out.
So, go over it turns on.
Go over, it turns off.
And now I'm getting a single entry and I can see that laser showing up and toggling its visibility there.
So, I'm going to stop playing.
We're going to go into plastic and we're going to save our changes or commit our changes to the laser.
So, laser script created to hold laser functionality and switch optimized.
And we'll check that in.
Now, we're going to modify our laser so that it can shoot an arbitrary distance until it hits a target that it can start dealing damage to.
To do that, we're going to open up our laser script and we're going to add in two new fields.
We're going to start with a direction.
So, I'll add a serialized field here.
For direction, it'll be a vector 2.
And I'll name this underscore direction.
And I think by default, I want to just aim this off to the left.
So I'll name it ve put in vector 2.
So that it automatically just goes the direction that I'm thinking.
But if I want to do a laser that goes up or to the right or anything else, I want to be able to control that.
Next, we'll add a field for the distance that I want this to be able to shoot or a maximum distance.
And that'll be a float because it's going to be a number with a decimal point.
And I'll call this distance.
And I think I'll give this a value of 10 by default.
So put in a 10 there.
So I can go about 10 m.
And we can adjust this per laser or maybe come up with a standardized distance for them or maybe make it infinite so they shoot off forever.
But for now, I'm going to go with a distance of 10.
And then we're going to add in our update method.
And in the update method, we're going to figure out how far to shoot this laser and then adjust that line.
renderer.
So, let's add a void update.
Let it autocomplete.
I'll get rid of that private keyword.
And the first thing I want to do is figure out an end point that is whatever distance away in the direction that we have.
So, I'll say var end point.
This is going to be the end of our line renderer is equal to our transform.position.
So, our starting position plus some offset, which is going to be our direction.
We're going to put this in parenthesis.
We're going to multiply direction times distance.
Now, this is going to give me an error saying that it can't add a vector 2 to a vector 3.
And the reason for that is that our transform position is a vector 3, which means it has that Z position in it.
While while our direction is a vector 2, so it doesn't have a Z.
And when we multiply the vector 2 times distance, we still get back a vector 2.
And it has a hard time adding a vector 2 to a vector 3.
doesn't know what we want to do and it thinks, hey, maybe you've made a mistake here.
But really, what we care about is not the Z position of our transform, just the X and the Y.
So, we can actually cast our transform position as a vector 2.
It's by putting vector 2 in parentheses right before it.
And what it's going to do is it will treat this transform at this position as a vector 2.
This only works if the types are convertible.
Since a vector 2 is just the same as a vector 3 without the Z, it's able to convert that, get rid of the Z, and we just get a 2D X and a Y.
So, we've got that initial position plus our direction times distance to give us our end point.
Now, we'll set the second point of our line renderer or position one.
You'll look at the indexes in a second to that end point.
So, we'll say underscore line renderer set position.
And there's a set position and set positions.
Set positions allows you to pass in an array of them.
Set position is to modify a specific position.
We want to modify the second one, which is index one.
Index zero is the first one.
And we want to set the value or the position to our end point.
I'm going to save that off.
We'll go into Unity.
And we should be able to now modify our line renderer just by adjusting the direction and the distance of that laser.
Let's play and make sure that that's the case.
We'll go select our laser as soon as it starts.
And I'm probably going to have to run over there.
Let's go turn the laser on.
There we go.
Turn the laser on.
You can see that it's blasting out a beam pretty far to the left.
If I drag in this distance, should see that the distance kind of comes in.
If I put it at three, was it three? No, it's four.
Four meters away to that block there.
Should work.
And if I change the direction to maybe a positive one, it's going to go out to the right.
I can drag this out as far as I want.
I could even go up and go at some angle or go like a zero and a one here and have a a laser that goes straight up and down.
So far so good.
We're getting our laser and it's customizable, but we probably want to make sure that it goes out to a specific target.
So to do that, we're going to add in a raycast.
We'll open up our laser and right before we set our position, after we've calculated our default endpoint, let's add a new line.
Actually, let's add one more.
And then we're going to do a raycast.
We'll ray cast out in that same direction and see if we can find another target.
Find that brick or whatever thing is off to the left or whatever direction we end up going.
So to do that, we'll assign a raycast hit.
So say var and we'll call this um let's call this first thing.
This is the first thing that that I've hit.
And it's going to be equal to physics 2D.
There we go.
Raycast.
And we want to give it our origin which is our transform.position.
Then we need to give it a direction which is going to be the underscore direction.
And then finally a distance which will be our underscore distance.
This should return back the first collider that our raycast hits.
And then if we find something we'll say if first thing collider is not equal to null.
So if first thing collider will just be true if we've actually hit something.
it'll be false or null if we've not hit anything.
So if that is not null or if we've actually hit something, that's what this is checking.
Then what we want to do is set our end point to be equal to our first thing which is it's not actually the first thing which is a little bit confusing.
It's the first things raycast hit 2D.
So it's got a little bit of info.
It's got the collider, but it also has the point where the raycast hit.
So, if I set the end point to the first thing that I have hit point and save this off, I should now see my laser blast over to the edge or over to this thing and then stop.
And then maybe if I turn it the other direction, it should go up until it hits the platform that's moving and then stop.
Let's try that out.
So, I press play play play and I'll go turn on my laser so I can see it.
And look at that.
No matter what I set the distance to, as long as it's greater than four, um, it's going to hit that object.
And if I change the direction to one, watch what happens.
And let's let's set that distance out there.
Notice that the the beam kind of goes and matches with that moving platform.
It's hitting that platform.
I'm going to put this back to a negative one, though, because now I think that we're just about lined up.
It's shooting that laser.
It's getting it at the right target, and it's ending at the right target.
We're finding the thing that we're hitting.
Let's stop playing though because there's one other problem that we've got here that we haven't addressed yet.
We're doing all of this code even if our laser isn't on.
Right now, we're running this code to do the updates and we don't necessarily need to.
We don't need to be doing that raycast and we definitely don't want to be damaging things when it's off.
And that's what we're going to do next is write some code to damage things.
So, let's make sure that we only run this code if our laser is on.
And I don't want to turn this script off because that causes some other problems.
Instead, we'll just check the is on bool here.
So, in our update, we'll say if is on is equal to false, then just early exit and return.
That's all we need to do.
We can quickly bail out and not add some braces and add extra um indentation or anything like that.
We'll just bail out if our thing isn't on.
We'll save.
Do a quick build.
Just make sure that all of our files are saved.
And then go back into plastic.
And now we have a dynamic laser that hits targets.
put dynamic laser that hits and ends at its target.
And we'll check that in.
Now, we're going to make our brick take damage from the laser.
To do that, we'll open up our laser script.
And in the part where we find the first thing that we've hit, we're going to figure out if that thing can take damage, and if so, we'll just tell it to take some laser damage.
Now, right now, the only thing that we have that will be able to take damage is a brick.
So we're going to start by just seeing if the thing that we hit is a brick and then we'll make it more generic as we have more things to damage.
So say var brick equals and here we need to get the brick component from the collider.
So we'll say first thing let's see if I can spell it right.
Collider get component and we want to get a brick.
If the brick is not equal to null.
So if brick, then we'll tell the brick to take laser damage.
Now I don't have a method for take laser damage yet.
So we'll just generate one and we'll figure out how that should work.
So taking laser damage on a brick should be relatively straightforward.
We have two real options.
We can either keep track of some amount of health or we could just keep track of the amount of time that this thing has taken laser damage.
And that's what I want to do.
We're going to add in a new field here for damage or let's call this laser damage time and we'll plus equals time dodelta time.
So we're going to add the amount of time since the last frame to our laser damage time.
I'll hit alt enter and generate a field for it.
I'll remove that private keyword and make this one internal.
Change it to public.
Now I want to add a serialized field for the amount of time that we can take.
So I'll add a new serialized float.
it's the um let's say laser destruction time and I'm going to set that to 1 second.
Now in our take laser damage method, we'll check to see if our laser damage time is greater than our laser destruction time.
In fact, I'm going to rename this.
Let's call this taken damage time underscore taken damage time.
Make that a little bit more explicit.
If that's greater than our laser destruction time or equal to, let's add the equals right after the greater.
Then we want to destroy our game object.
But when we destroy our game object, right now we instantiate a particle and then do the destroy.
So let's take that bit of code, line 34 and line 35, hit alt enter, extract it, and make a new method called explode.
This will do our explosion and kind of destroy our object cleanly and give us that particle at the same time.
I'll remove that private keyword.
Copy the explode method.
Scroll up and we'll paste it right here.
I don't need the braces for 16 and 18, though, so I'm actually going to paste it over them.
I'll select it and paste so that we just have that oneliner.
Now, we'll save and do a quick build just to make sure everything's saved, and then go back into Unity, and we should expect to see our brick blow up after 1 second.
Let's see if that's the case.
I'll press play, run over, turn that switch on, and watch our laser blast through that thing, get some particles.
Let's see them in action.
So, I run through.
Oh, there we go.
And it blew up.
Looking pretty cool.
Let's stop playing though and I want to go add a couple more bricks.
I'm going to take this brick right here and let's add a rigid body 2D component to it.
So, I'm going to add a rigid body to this one because I want to make a brick that can now fall.
I'm not going to add this to the prefab.
I just want to play with it for a moment and experiment and maybe we could make a falling brick later.
Maybe that could be the gray brick as the falling one and the brown brick doesn't fall.
Let's duplicate it though.
I've got my brick with the rigid body.
I'm going to duplicate it.
Drag it up.
Duplicate it.
Drag it up.
duplicate it, drag it up, and press play.
And just watch as all those bricks get destroyed and fall down.
Let's see.
Remember, the one on the bottom does not have a rigid body, so they don't all just start falling down.
There we go.
It's blasting through them.
It stops the second I turn it off.
It won't keep blasting, and then it'll turn back on and start blowing these bricks up.
That is looking pretty cool, I think.
Now I want to go into plastic and commit our changes so that we've made bricks break with lasers or lasers can now destroy bricks.
I'm going to save my scene even with those weird bricks that I've got here and check in my changes.
Now I want to add a visual indicator to our brick for when it's taking damage and introduce you to another new code concept.
Let's open up our brick script.
And inside of our brick, let's add an awake method so that we can cache the sprite renderer.
We'll add the awake.
Just type it out and say underscore sprite renderer equals get component sprite renderer.
I'll add a field for that.
Hitting alt enter just generate a field and delete out my two private keywords.
Now, when we take laser damage, what I want to do is just change that sprite renderer's color to something else and then make it flip back when we're not taking damage.
So, when we start taking laser damage, I'll say underscore sprite renderer color equals and I'm going to go with red color.
Next, I'm going to add in a field for how long I want to show that afterwards.
So, I want to be able to show that it's red for maybe like a tenth of a second after it's taken damage, but that's about it.
So, that it's like red and then it kind of just dissipates down.
So, to do that, I'm going to add a new field.
And that field is going to be my reset color time.
I'll say underscore reset color time equals time plus 0.1f.
So, that's going to give me a time that's 10 or a tenth of a second in in the future or 100 milliseconds ahead.
So, a very very short duration from now.
I'm going to generate a field for it, which should give me a float right up here.
Got my reset color time float.
Delete that private keyword.
And then we're going to add an update method.
I think that we'll do this.
Let's do it right after take laser damage so that it makes the most sense and the code's right next to each other.
We'll add an update.
Hit tab.
Delete out that private keyword again.
And in our update method, we'll check to see if that current time, so if time is greater than or equal to that reset color time.
If so, then we'll reset our color back down to white.
So say sprite renderer color equals color doh.
And this should work, but I want to test it out and then make a little optimization to it.
So let's go try it out real quick.
Let Unity reload.
And I expect these things to turn red when they're taking damage and then turn back to their normal color shortly after.
If I toggle the laser off.
So, let's go do that.
We'll run over here, turn the laser on and off, on and off like that.
It updates properly.
But there's still one issue that we need to address, and that's that our boxes right now, our bricks, are turning themselves white every single frame.
Let's go take a look at that and see what I'm talking about.
If we go into our brick script right now in our update, if the time is greater than that reset color time, which is going to be zero by default, it's going to set this color to white.
Let's add a log here.
Say debug.log set brick to white.
And let's see how often this is actually getting called.
I'm going to minimize my code editor, jump back into Unity, press play, and expect to see a giant spam of that message because every frame for every block, we're calling that code and just updating the sprite color for no reason.
It hasn't changed.
It doesn't necessarily need to change.
So, we could probably optimize it.
Let's take a look, though.
Look at that.
You can see, oh yeah, we're getting basically a couple calls per frame.
Every single frame, we get one call for every brick there.
So, let's modify this code a little bit so that it doesn't have to do that.
So that we don't do this code if the reset color time is reset if it's either at zero or if it's null.
And I want to show you there are two ways that we can accomplish this.
One thing we could do is say if the reset color time is zero, then just bail out of the update.
And we could set the reset color time to zero right here after after our code.
Let's let's do that.
We'll say underscore reset color time equals zero.
And here right before our code, we'll say if reset color time is greater than zero and time is greater than reset color time.
So we'll save.
We'll go back and press play.
And I was thinking about showing a different way to do this, but I think in all honesty, the simplest solution is that one.
And it makes a little bit more sense than my previously thought out solution, which tends to happen.
And I was thinking about using nullables and then I realized I don't really need a nullable here.
I can just put it at zero.
Zero will work just fine, too.
So now if I run over here, you'll see that I shouldn't be getting those log entries every frame.
Only when the brick actually turns back to white, I get one.
So here we go.
Just occasionally get a log entry when when a brick goes back to white.
But I don't end up getting these every single frame.
And I've fixed my problem.
Let's go back into the code.
delete out that extra log entry that we don't need on 35.
Save and then go into Unity and commit our changes where we've got a brick showing visual dam incoming damage.
So, we'll go to plastic soon as that's done so that bricks show damage visually.
And I'm going to make sure I save my scene just in case.
I don't think I modified anything, but I want to check just in case.
And we'll check that in.
Now, we're going to add another enemy to our game.
We're going to add one that's a little bit more intelligent and can start dealing with the laser too and interacting with that.
We're going to use the ladybug.
Although you're welcome to use the spider or mouse or something else if you prefer the visual, but I think that the ladybug is going to work pretty good for what I want to do.
So, I'm going to put a ladybug right up here on this platform away from the laser so that I can start setting it up.
I'll grab my ladybug and drag it right out here.
I'm going to fix up that position.
Looks like -6 and about a one should get it right into place.
Next, I'm going to create an animation for my ladybug so that it can just play a little walk animation while it's running around.
To do that, I'll open up my animation window.
Remember, window and animation.
Animation or it looks like control 6 is the hotkey for it.
With the ladybug selected, I'll hit the create button.
And then we're going to go up into our art folder.
And let's go find our animation folder up in the assets route.
And I'm gonna call this snail walk.
No, not snail.
Ladybug walk.
Thinking of snails.
I just saw the snails a second ago.
So, we've got our ladybug walk animation created.
And now we need to add in our key frames.
To do that, I'm going to take the animation window and just drag it right up here so that it's docked below the scene view instead of docked with my project view.
And I'll take the ladybug sprite, hold control, and take the ladybug move sprite, drag them both up onto the animator, and I should get two frames.
If I hit play now, it's going to be like this weird flashy jittery thing.
Not what I want.
I want it instead to take a little bit longer.
So, I'm going to drag it out to about the 030 or the essentially the half a second mark.
And now I've got, if I hit play, an animation that goes from one to another, but it instantly bounces back.
it doesn't kind of give me that delay before it goes back to the first animation.
So, I'll stop playing and we'll copy this starting key frame just by dragging and selecting it and hitting Ctrl + C.
Then, I'm going to go over to the 1 second mark and paste it in.
Now, if I play, I should get a nice slow animation like I expect.
And if I select all of the frames, I can grab the little bar here and drag it in to speed this up or slow it back down.
But, I think that I like the 1 second mode.
That seems about the speed that I want this guy to move at.
Next, I'm going to add in some more components to our ladybug.
First, let's add a collider.
Let's go to the components.
So, let's get rid of this animation window.
I'll drag it down.
And then we'll go add a new component.
So, I want to add in a collider first.
We'll add a capsule collider 2D.
And to make that a little bit easier for us to see, let's turn this ladybug into a prefab so we can view it in prefab edit mode.
So, here's our prefabs folder.
I'm going to just drag it down so I can see the icons and again have some empty space and take my ladybug and drop it in.
Then I'll double click on the ladybug.
And now I can see that collider much better.
So the first thing I want to do with my collider is change the direction from vertical to horizontal.
Right now that doesn't look like it did anything.
But if I change my Y value now to a 0.5, you see that I now have a nice horizontal character or capsule collider.
If I switch this back to vertical, you see that it looks the same height or the same like a circle because I it doesn't work that way.
If I want it to be a flat thing, I'm going to switch it to horizontal so it's a horizontal capsule.
Now I've got my size about right, but the offset is way off.
It's way up above where I want it to be.
So I'll change this Y offset to a negative and it's going to be half of.5.
So 0.25.
Move it right down into place.
Now I've got a nice ladybug with a capsule on it.
I want to add in a ladybug script.
So, we'll go to the scripts folder, rightclick, create a new ladybug script with just a capital L, no capital B.
It's a single wor