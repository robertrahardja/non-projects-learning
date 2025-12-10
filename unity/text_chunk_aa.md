Hello and welcome to the course.
I'm really excited to have you here and hopefully you're excited to be here.
In this course, we're going to cover a lot and you're going to learn a lot about game development.
We're going to start with the fundamentals of programming and Unity, learning our way around the Unity editor and how to read and write code, and then we're going to get into some really advanced topics.
We're going to be using professional workflows and the things that you would use in an actual game development job.
We'll set up source control.
We'll set up build automation and we'll do some refactoring, learning, debugging, optimizing, profiling, and a whole lot more.
Don't worry though, I'm going to make sure that it's completely approachable and that you can understand it and won't get lost.
So, I hope you're excited.
It should be a lot of fun.
We're going to build some games, have some fun sharing them with friends and seeing what kind of cool stuff you can come up with while you're learning this whole process.
All right, let's get started.
Before we start building, I want to have a quick discussion about game engines.
Because in this course, we're going to be using a specific game engine.
I want to briefly explain why we're using that game engine and what the alternatives are and just give a little terminology so everybody understands where we're starting from the beginning.
So, the game engine that we are going to use for this course is Unity or sometimes called Unity 3D.
The actual name of the engine though is Unity.
Their web page is unity3d.com.
There are a couple of game engine options out there though.
Unreal is one of the most popular ones.
I'm sure you've heard of it.
Fortnite's built on that along with a lot of AAA games and Unity is the other big one or the other big player in the game engine space.
There are some other ones that used to be big.
They've all kind of shrunk off and then there are lots of little company or not little companies but lots of big companies that have their own custom engines.
But for the most part, the two leading engines in the industry are Unreal and Unity.
While there are a couple big differences between the two engines, you really can do just about anything with either of the engines.
Unity is generally seen as more of an indie friendly and mobile friendly engine that's kind of approachable by a single person or a smaller team.
And Unreal has, at least historically, been something that was more used in AAA games.
So, you'll find that a lot of AAA developers already have a lot of Unreal experience.
It's what I used to use before I used Unity.
And because of that, they're bringing that in there.
They also have some really cool features in Unreal, like the new Lumen and Nanite systems.
Unity also has lots of cool new features, though, and lots of stuff that's constantly coming.
In fact, one of the things that made Unity so big was that they were the first ones to the mobile market by, I think, over a year.
So, if you wanted to build out for an iPhone, Unity was the way to go.
And you'll find that's the case for most new platforms.
Unity tends to be ahead on that stuff.
And Unreal tends to be slightly ahead on rendering quality for AAA level graphics.
So, that's kind of the loose difference.
You can really use either, but for this course, we're very specifically going to use Unity, and we're going to use a specific version of Unity.
So, I want to talk a little bit about different Unity versions.
Unity is released in three or four different branches.
First off, there's an alpha branch of Unity.
This is where you'll see all of the latest and greatest newest features.
I'll talk about how you can get that and see that later, but just understand that it's not really that um reliable.
It's something that you should expect to crash.
You should expect to be somewhat unstable because it's testing out the new features.
They haven't been fully vetted.
They haven't found all of the bugs and fixed them.
The beta build or the beta branch you'll find is quite a bit better.
It's a lot more stable.
You'll find that a lot of the new features are there.
They get there quickly after they go out of alpha.
They'll go into beta and they're usually mostly stable there.
But it still does crash.
It's not super stable and you probably don't want to do your final builds off of that either.
There are two other versions though.
There's the LTS and the techream.
The LTS, which is the long-term support version, is the Unity version that's going to be supported for at least, I believe it's two or three years.
You can look on their page and see the exact details for each LTS.
But the one that I have up here is the Unity 2021 LTS, and you can see that they're going to support that all the way through 2023 and beyond.
And the Unity 2020 LTS version will start to reach its end of life cycle around 2023.
What does this all mean? not a whole lot for you except for if you're going to build a final version of a game, like you're getting ready to release your game, you want to use one of these LTS versions.
Usually, it just means that this version of Unity is going to continue to be supported.
If they find some weird bug like, oh, um, a Chrome update makes it so that this game now crashes, WebGL builds on this Unity version, they'll go back and fix that.
they'll find, you know, fixed things that they found in that issue or in Unity in that version in that LTS.
The Techstream, which is what we'll be using, is a little bit newer.
The Techstream is the latest version that's considered stable, but it's not like a locked down version that's going to have support.
It's going to have some new things.
It's not going to be completely stable.
It's not the 100% stable, but I consider it 99 98% stable.
So, that's what we're going to be using.
Again, it's called the text stream version, but you can always use an LTS.
And eventually, this text stream that we're using will be turned into an LTS.
Now, for your Unity version, I recommend that you either use the one that we're using or a newer LTS or newer um textream version.
Don't use an alpha, don't use a beta.
Just make sure you go with a Techstream or an LTS version.
And to get specific, in the next section, we'll actually go through the installation process.
You'll see the exact version that we're using.
So, just make sure you're using at least that version or newer.
In this lesson, we're going to cover installation of Unity.
If you already have Unity installed and you already have the latest tech stream, then you're probably good to go.
But I would recommend that you watch this through maybe on 2x speed.
So, the first thing that you're going to want to do if you don't have Unity installed is go to the unity.com page and then look for their download link.
I have it at unity.com/d download right here.
And you can see there's a button to download for Windows or download for other versions.
If I scroll down here, this is what that download for other versions option looks like.
There's a Windows one, a Mac one, and Linux.
We're going to completely ignore Linux, but if you're on Windows or Mac, just click on whichever one is your current operating system.
Hit the download button.
It should download your installer.
And once it's finished, just hit the open button or download and open your installer, however you do it on your system.
Once the installer starts, you'll see the license agreement.
Just hit agree.
Choose an installation folder.
I'll use the default.
This is for the hub, not for the actual Unity installs.
So, it's going to be a relatively small download.
I wouldn't worry too much about where you're putting it.
Probably just leave it in the default location.
If you want to worry about where you're installing the bigger versions of the editor, which is what we're going to be getting into, or the full actual editor versions, you can do that when we go to the editor installation part.
So, now that the hub has finished the installation, we'll just hit the finish button and allow it to run the hub.
I'll allow firewall access.
And then the hub should look like this.
If you don't already have a Unity account, you're going to need to create one.
If you have one, you're good to go.
just sign in with it.
Let's go through the creation process real quick.
I need to give it my email address, a password, which has some pretty strict requirements, a username, my name, and then agree to the terms of service, and prove that I'm not a robot by clicking on some it looks like bicycles.
There we go.
That's not a bicycle.
And fire hydrants.
Guess that's kind of a fire hydrant in there.
All right.
Now I'll create my Unity ID which is going to be just this Jason Wyman 2023.
And I should get an email that I'll go confirm.
Yep, I got it right here.
Let's hit confirm and then continue.
Oh, I've got to prove I'm not a robot on the phone first.
Now we continue and I have my account.
It didn't automatically sign me in though, so I'm going to need to go over back to Unity and sign in.
So, minimize this tab, hit the sign in button, and then allow it to use the authentication through the web browser, and there we go.
Look at that.
I didn't even have to put in my password.
Now, it's going to ask me where I'd like to install Unity and allow me to select a version of Unity to install.
Right now, by default, it wants to install 2021.3.16F1.
This is the LTS.
This is not the version of Unity that I want to use, though.
So, we're going to change this.
We're actually going to hit skip installation.
Hit agree and use the personal license.
And then we'll choose I don't want to switch to light mode.
So, hit maybe later on that.
And then on the installs section here, if you don't see this section right here, just go to installs if you're on projects or learn or somewhere else.
Go to installs.
Choose the install editor option.
We're going to find an official release that's not the LTS because I want to use 2022.2.
If there's a 2022.3, which I don't think there's going to be, or if 2023 something is here, then go ahead and use that.
But I want to use something slightly newer than 2021.
because there are just some new updates coming.
It's going to be an LTS for 2022 very soon.
And I feel like there's a couple cool features in the newer version that you should be aware of and be using.
So, let's install 2022.2 and hit uh install.
Then we get this popup here.
Now, here we have a couple of options that we can choose.
We can use the default code editor, which I'm going to leave installed by right now, but we're going to talk about code editors later and talk about installing another code editor later.
We also can choose if we want Android support, iOS support, support for Linux, Mac, or Windows.
What I do want is WebGL support.
So, choose whatever ones you want.
Don't overchoose and select a whole bunch.
If you're thinking, "Yes, I definitely want to build out to my Android device," you can choose the Mac or the the Android option.
You can always go back and reinstall or read these later, though.
So, don't feel like you have to, but if you're looking at options, just make sure that you get this WebGL build support because we are going to do WebGL build so that you can set up an automated build that's going to deploy this out and allow you to just play every time you do a commit.
It's going to be very cool.
You want to make sure that you have that.
So, I'll choose WebGL and leave the default code editor.
Hit continue.
Agree with the terms of service and hit install.
Then we'll let this install.
It's going to take a little while.
So, I'll be back when it finishes.
Once the install finishes, it should look like this.
You should see 2022.
Whichever version you've installed along with the platforms that you've installed support for.
If you don't see it, maybe you're in the pre-releases or official releases section.
You should be in official releases.
It really shouldn't show up in pre-releases.
That's where your alpha and betas are, but you should see everything in all.
This can end up having a lot of installs of Unity.
I generally recommend keeping maybe up to two or three of them around.
They get relatively big, so as new Unity versions come out.
I try to keep an LTS version around and a Techream or two Techstream versions around and occasionally I'll have an alpha or beta.
th those versions I want to make sure to clean up and just delete later because they do take up quite a bit of space.
Now we're done with the install though and it's time to create a project.
It's time to create a new project.
To do that, we'll go to the projects tab.
I'll click on projects and then we'll hit new project.
This should give us a popup of a couple different options of different project types that we can create.
There's also a drop down up at the top that's important to remember.
So, when you install new Unity versions, it'll let you select which Unity version to create your new project for.
By default, it's just going to be on the one that we've installed.
If you have multiple installed, though, just make sure that you've selected the correct editor version here and don't have an old one there.
Now, we have quite a few template options.
There's a 2D core, a 3D core, a 2D URP core, a 3D mobile core, 2D mobile core.
There's all of these different options down here.
They all kind of do slightly different things.
I'll talk really briefly about what those are and then we'll make our selection.
The 2D core option allows us to create a 2D platformer using Unity's older built-in render pipeline.
This is something that well was the only way to create 2D games in Unity up until relatively recently.
I would say it's now near being deprecated and probably not something that you should choose.
In fact, I don't think it should really be the top option here.
3D core is kind of the same way.
This is for creating a 3D game using the built-in render pipeline, which is the old non-customizable render pipeline.
Now, these are the two old ones.
The new ones are the 2D URP core, which is a 2D project using the universal render pipeline, which is a rendering system built for, well, rendering on just about every device.
That's why it's called universal mobile devices, uh, consoles, PC, web, just about everywhere.
It doesn't have the maximum like highest end graphics, but it has very, very good graphics, just not the super photorealistic stuff.
For that, you would go down to something like 3D HDRP.
In fact, there isn't even a 2D HDRP option because it's two-dimensional game.
2D games don't really have that realistic lifelike stuff.
3D HDRP is for a 3D realistic game or 3D URP for a 3D game that is well something that you're building without a giant art team that's giving you these great realistic 3D models.
So, your general options are usually going to be 3D URP or 2D URP.
Those are the two that I recommend for most projects that you're going to end up building.
For this project, though, we're going to choose 2D URP.
So, make sure that you've selected 2D URP.
And then scroll down and give your project a name.
I'm going to name mine Alien Blasters.
And then we'll give it a location.
So, choose where you want to save your project off to.
I generally like to have a folder right off of the root of my drive where I store all of my projects.
So, let's go create one.
Now, I'm going to create a new projects folder and then create or created into that folder.
So, we'll have an alien blasters folder that gets created in my projects folder.
I'll hit create and our project should get created.
Unity will launch up and in a minute or so we'll have our new project ready to go.
go.
go.
Now that it's finished opening, which took a little bit longer because I've got a bad internet connection here.
We can see the Unity editor and we can see my project.
The editor might look a little bit confusing right now.
There's a lot of stuff here, a lot going on.
And we're going to talk about that all in the next section.
And I'll go over each of the different areas and describe and explain what's going on there and what all of these things mean.
For now though, you can just go to window and choose the layouts option and choose default to get a nice default layout.
You don't need to go set up the project or do the linking or anything like that.
We'll do that afterwards.
Once you've got your view looking just about like this, click over to the game view.
Make sure that it looks blue.
Go back to the scene view and then come to the next section where we'll go over all of the different editor parts.
Now that we have our project created, let's take a look around at the editor.
If your editor doesn't look like mine, it's okay.
Just go to window, choose layouts, and choose default.
This should give you this default layout where you've got an hierarchy area or a hierarchy area on the left, a scene view in the middle with a little game tab up there, an inspector to the right, and on the bottom, a project and a console window.
Now, let's talk through what all of these different sections are and go into just some depth so that you feel a little bit more comfortable.
If you're already totally comfortable with the editor, feel free to skip this part.
But if you're new to the editor at all or you just haven't seen this version, recommend you just hang on for a moment and let me show you a couple of quick things.
First off, we've got the scene view.
The scene view shows us everything that's in our current level.
The hierarchy here also shows that, although by default, the Unity editor, when you open up a new project, for some reason collapses everything in there underneath the name of the scene.
Right now, we've got our sample scene open.
If you don't have that open, we'll talk about how to open it in a moment, but let's hit the arrow to expand it.
You'll see that there are two objects in our scene.
We have a main camera.
I can select it and a bunch of things just changed.
And I have a global light selected, and it looks a little bit different.
If you don't see this sample scene, that's okay.
We'll come back to this in a moment.
Let me show you how to open it.
Down here on the bottom, we have the project window.
There's a project and a console tab.
If it looks like this, just click over to the project window.
underneath the project window, you should see assets and packages.
There's also a favorites section up there.
Go to the assets section and then click on it and then choose scenes.
Double click on it and you should see your sample scene in here.
Just double click on it and it should open up the scene.
It might ask you if you want to save the empty scene that you're in.
You could just hit no.
So once we have this sample scene open, let's look at it again and talk through some of these objects here.
On the left, we've got our main camera in the hierarchy and our global light.
If I select the camera, you see that the inspector here on the right shows a whole bunch of somewhat interesting things.
It shows a transform, which may or may not be confusing to you, with some positional information.
It's got a position with an X, a Y, and a Z.
We're going to talk a lot about that later, a rotation, and a scale.
We don't really need to talk too much about the transform, though, so I'm going to collapse it by clicking the arrow.
Then, I'm going to talk about the camera here.
This is the next component on our main camera game object.
We'll talk a lot about game objects throughout this course.
This camera here has a couple of settings on it.
First, you'll see that it's set to orthographic here under the projection section.
This is because we're building a 2D game.
The other option for this is perspective.
So, if you're wondering how to get things into a 3D view, perspective mode is usually the way that we're going to want to go.
We'll talk a lot more about camera modes later, though I don't want to go too deep into it.
Just want to show some of the option stuff here.
The other option that I want to show is under the environment section.
Our background type right now is set to solid color and our background color is set to blue.
Right here, you can see a preview of our main camera is showing blue.
And if I go over to the game view here, you see that all we see is a nice big blue screen.
Now, if I change the background color by clicking on the color and then choosing a new tone or new color and go all the way to white, all the way to blue, go over to like a green or something else.
I can totally change what my background is looking like.
We can also add in images and we're going to do all that.
But background color is an important thing to understand and know about while we're learning about the inspector.
Now, let's undo this change.
I don't want to have a green background in my game.
It's kind of blinding me right now.
So to undo it, I'm going to hold control or command if you're on a Mac and hit Z.
That's the universal undo button.
And control or command Y is the redo button.
I don't want to do that though, so I'll control- Z again and remove that color change.
Now that we've got all of the different parts of the Unity editor talked about, let's kind of dive back into the hierarchy for just a moment.
In the hierarchy, we've got multiple objects and I can select between them.
And remember that the inspector is changing which object is or showing which object is selected, showing the selected one.
If I hold shift and I hit the up arrow here, I can actually select both of them or I can click on one and hold control and select multiple.
And you'll see that over here on the right, it looks a little bit different.
It has a transform section.
But here it says components that are only on some of the selected objects cannot be multi-edited.
So that means that because both of these objects have a transform component up at the top, that part can be edited together.
I can multi select them and edit it.
I could modify the scale or the rotation or something.
But because they don't both have a camera, I can't multi select and modify the camera or multi select and modify the light because only one of them has a light.
So that's pretty much the core of the editor or the core of the areas that you need to know about.
There's one other section that I want to show you though that you might get stuck with and might run into a problem with in the future and I think it's important to call out right away.
Well, two of them actually.
First, there's a lock button up here.
Say I've selected my global light and I accidentally clicked this lock and I go over to work on my main camera.
Notice that the lock button has kept it from changing.
It's actually changed or selected and locked onto this global light.
This window can't change to my newly selected object.
If I hit the lock again, it'll unlock and then I can now select objects and have them show up in the inspector.
This is very useful sometimes, but it's easy to get it mixed up and accidentally leave it on that mode.
Another issue that I see people run into often is right here on the triple dots.
See if we can drag this over just a little bit.
There's a debug option.
So, if you choose this debug option, things suddenly look really weird.
There's lots of extra text here and you're seeing things strange.
This comes in handy later.
We'll talk about how and when you can use this later, but if you ever see yourself kind of stuck in that mode, remember you can just go back here and choose normal.
Choose the three dots, go back to normal, and you're good.
And then the last thing is just remember that you can always go to window layouts and default to get back to a normal default layout and kind of match what you're seeing with my setup.
It's time to start building our game.
And to do that, we're going to need some art.
I usually like to start with a little bit of an environment and a player first because I feel like it lets me get right into the game, start to understand what I'm doing, and it makes it a lot more fun and interesting of a process.
So, to get started, the first thing we're going to need to do is download some art.
We don't want to be creating our own art.
You might be an artist and want to create your own art afterwards, but for this, we don't want to be creating our own art.
We want to be focusing on the game creation, coding process, and all of the other things that matter.
So, the art that we're going to use for this course is actually, well, two sets.
First, we're going to start off with some free online art that I really love from Kenny.
You can check out the Kenny NL page to find all kinds of awesome art that you can download for free.
and he's got some really great packs for $10 and $20 that I'd recommend you go check those out later.
You don't need them to get started, but as you start to build your game up, you might see some cool stuff and want to go grab it or just grab some more of the free packs.
But the pack that I'm going to use to start is this platformer pack redo, which has the latest version of the platformer assets that he's created in a slightly higher resolution than the old ones that were available before.
So, if you've downloaded these before or seen these before, they're just slightly upgraded ones that look a little bit nicer.
I'll hit download and grab this file.
And once the download finishes, I'll open it up with Explorer, or you can use your zip program if you prefer to use something that you have that deals with zips or Finder if you're on a Mac.
Now, inside of this zip, you'll see that we've got a couple subfolders.
There's a sprite sheets folder, a vector folder, there's a ken folder which has some info on how to use things, and there's a PNG folder.
The PNG folder has backgrounds, enemies, ground, HUD, items, particles, players.
This is what we want.
This is where all of the art assets that we actually want to use are.
And go down into here and see the details and see all of the different files in here.
So, how do we get these out of the zip and into our game? Well, first thing we're going to need to do is we'll put a folder down into our project that we can put them into.
But what I like to do first is just select all of these file or folders under the PNG folder.
Rightclick and choose copy or hit control or command C to copy onto your clipboard.
That's going to copy all of these folders onto the clipboard so we can paste them into our Unity project.
Now, I can't just rightclick and paste them into here, but I can rightclick, hit create, and choose folder and make an art folder.
So, we'll create a new art folder that we'll drop our files into.
Again, that was just right click in this project view in the open empty space.
Hit create and choose folder and then give it a name.
I named one art.
I'll make another one named art 2.
And then I'm going to delete my art too because I already have that art folder.
Once you have your art folder though, just double click on it and then rightclick and choose show in explorer or showin finder.
This should open up a window for you that you're used to.
just go right into the art subfolder.
It's going to actually open you at the assets folder with that art folder selected.
So, just double click or hit enter.
And then we're going to hit controlV or commandV to paste.
Or you can you might be able to rightclick and paste, but I noticed in Windows 11 for some reason the paste option is missing, which is a little strange.
Probably something with the zip.
Now that I've got all of these subfolders inside of my art folder, I should be able to use them.
But notice that back here in Unity, I don't see it.
It looks empty.
As soon as I click over to the Unity editor, it's going to import all of these folders and all of the files underneath.
Let's watch it happen.
So, I click and there it goes.
It's starting to pull in all of the different files that are in that zip file.
It's going to have all of my subfolders right down here.
And you can see it.
Now, I can go into perhaps the ground folder.
And let's go take a look at grass.
And I can see all of the different grass pieces that I can use to build out my game.
and go look at the planet folder, the sand, snow, and all that and see all of the different art assets that we've now got available to use.
There are some other asset packs that we can grab from Kenny that we'll talk about a little bit later, but for now, we're just going to stick with the the smaller pack and use this until we need something else.
We'll go through the process again of pulling in new things.
So, let's take a look at these art assets, though, because there's something that we're going to need to adjust for just about all of them.
And I find that it's a lot easier to just do them all at once than to do them later.
Let's go select this dirt center or whichever one you've got.
You could be on ground, grass, whichever.
Go grab one of the center icons here and look down here at the bottom right.
You'll see that it shows a preview of the graphic and it says 128x128 RGB compressed, a bunch of other weird stuff that may or may not make any sense to you.
What this is is telling us the resolution of this image.
So, it's telling us that it's 128 pixels wide and 128 pixels tall.
So, each dot there's 128 dots across, 128 down.
Now, that's really useful information if you know how to use it.
So, let me show you how to use it.
What we need to do with that info is put it into this pixels per unit field.
If we don't do this, things are going to be all weird throughout our entire process.
So, we want to do it right when we start to pull in our 2D art.
We want to set this to be 128 and then choose the apply button.
Now, you can't tell anything happened and this didn't update it for all of our sprites.
So, we're going to need to do this modification for every single sprite and then start to build our game up after we've modified them.
So, how are we going to do it for every sprite? Well, down here in the project view, there are a couple cool little tools.
And this one right here allows you to search for all of the sprites or all of things by a specific type.
So I'm going to choose sprite, but I also need to make sure that I go up to the art folder first.
So select the art folder, go up to the root art folder, and then search for sprites.
Otherwise, I'll only find the ones that are children of that folder or maybe some subset.
But if I go back to up to art and hit sprite, I should find everything.
Should be able to scroll through, see all of my players and boxes and everything else.
I think that looks good.
I want to go now select everything except for these backgrounds.
Actually, technically I could just select the backgrounds, too.
So, let's select the first one.
Grab all the way down to the last.
Hold shift and click.
Or you can just click in here and hit control A.
That'll select all of them.
Then go to the pixels per unit field here.
Change this to be 128 and hit apply.
Once that's done, it should finish importing and updating our assets.
We'll be ready to go and ready to start putting things into our level.
and start building out a level.
Now that we have art and we have a project, let's start building a game.
The first thing that I want to do is learn how to build a little bit of an environment and add a player.
So, we're going to expand out our sample scene so that we can see the main camera and our global light.
Again, if you don't have this scene open, just go to your assets folder, go to scenes, and double click on sample scene.
That should open it right up.
Once we've done that though, let's go over to the ground folder of our art folder and choose grass.
And then find the grass mid.
Let's see, where is it? Right here.
Grass mid.
We're going to take the grass mid and I'm just going to grab it and drag it right into the hierarchy here.
Not over here, but over here into the hierarchy.
It's going to center it and drop it right in the middle of our game world.
I can use the mouse wheel to zoom in and out.
And remember that middle mouse button to pan around.
Now, I don't like the position of that.
If I go to my game view, you'll see that it's got grass right here in the center of our world.
I want that to be down kind of near the bottom of our world.
So, let's make a change to do that.
But if we do it right here and I just grab, for instance, this Y position, click and drag and pull it down, it will move it down.
I could get it into a pretty good place, but it's going to be inconsistent because I haven't done a very important thing yet.
First, let's set this back to a zero.
And then let's go up to this game view window area and take a look where it says free aspect.
What this means is that our game will just kind of adjust and scale based on the the view of or the size of the window.
So the aspect ratio will adjust based on how much space we have.
If we have more wide space, it'll go widescreen.
If we have less, it'll go nice tall and portrait.
We don't really want that.
We want instead to be in a fixed aspect ratio when we're building a game.
That way we know what things are going to look like and have it'll be consistent.
Otherwise, we're going to have things looking all kinds of weird once we switch to an actual device that's playing full screen at 1080p or 4K or whatever the resolution you end up building at is.
So, what resolution do we want to choose? Well, by default, we go with full HD 1920x 1080.
It's what I would usually recommend.
Don't try any of the others yet until you have a need for them.
So, let's switch over to that.
Notice we've got some bars here now on the side.
And as I drag it, we keep that aspect ratio.
That's what we want.
Now, if I reset my layout, I go back to window layouts and default.
It is going to reset that back to free aspect.
So, I need to make sure to change it back to 1080 or 1920x 1080.
I could call it 1080p a lot from the old school TV times.
So, what's a value that I could put this grass at to have it be down here at the bottom? How can I move it around or how can I lower it? I showed you that I can click on this Y and just drag the mouse down to move it.
Look at that.
And you can see the number there changing.
Let's see what that's actually doing, though.
If we go over to the scene view, you can see that I've got an object here with with my grass.
And I can kind of click on it.
If I click the right spot, I get the mouse.
I can drag it around.
If I hit the W key, I'll get these arrows.
And then I can just drag it.
Oh, look.
Up and down or left and right, depending on which arrow I grab.
Right goes left, right, and the green goes up and down.
If I hit the E key, I can rotate it and spin it around.
I don't want to do that.
So, I'll hit control Z and undo my change.
And if I hit the E or R key, sorry, I can actually scale it up and make it nice and big or scale it down.
I also don't want to do that.
So, I'll hit control-z.
I also don't want this weird position.
So, I'm going to change that back to a zero.
And then we're going to move it downward.
So, to move it downward, I'm going to hit W, go into the move mode, but I'm not going to just drag it down like this.
Instead, let's control- Z.
I'm going to hold my control key, which is going to enable snapping.
Now, watch this value here, this position Y value.
As I drag it down, holding control, it's going to go down by increments of 0.25.
So, it's going to go down by one quarter of a meter is what that is.
And if you're not familiar with a meter, it's about a little less than three feet.
So, got to get used to that.
You're gonna have to get used to meter conversions.
But as I drag it down, it snaps down by a quarter meters.
And I can get it all the way down to what is this about -4.5 where it's right on the bottom touching this white line.
You're wondering what's this white line? That's actually the camera.
That's showing us where the camera bounds are.
If I go back to the scene view, this is showing us kind of the edge of the camera and the game view is showing us the the actual game rendered.
We can, by the way, drag these around.
Watch this.
If I drag this and see it, I can now see them side by side.
I could drag this around and see it on both of the views.
Again, control- Z to undo that.
I can grab my game view and just drag it back over here to dock them side by side.
Can always go to layouts default.
If you mess that up, just remember to change back to full HD.
All right, so now we've got some ground here.
What can we do with it? What if we want a whole bunch of ground? We want ground to go all the way across the bottom.
What should we do? Should we just go back in, find that ground object? Let's go find it.
and then drag another grass mid out here and try to lay it out and line it up.
I mean, technically, we could do that.
It would be a terrible way to do things.
That would be super inefficient and it would probably be really, really painful and take a long time.
So, let's undo that.
Let's go select this grass.
And I'm going to hit delete that second grass.
Not the first one, just the second one, the one that said grass mid with a one after it.
Then, let's go select the grass here that we've got.
And let's do a little bit of a modification to it.
Down here on the inspector, you see that we've got our transform that we've kind of looked at and moved things around with and looked at a couple times.
And then we've got the sprite renderer.
This is the component on our object that's making this sprite appear.
We've got three objects in our level, a camera, a light, and one object that has a sprite on it.
And it's named grass mid because that's the name of the sprite when we drag it out.
So, what does this sprite renderer do? It shows our sprite.
It gives us a couple different options of the way that we can show our sprite.
Right now, the draw mode is set to simple.
If I click on it, I can actually change that to tiled.
And a tiled sprite will allow us to repeat a texture and have kind of like a tiled background or a tiled floor or anything else that you'd seen tiled in a video game.
Now, to increase the tiling size, we can just modify the width.
Crank that up.
Make it 1 2 3 4 5 6 or whatever.
10.
I'm going to change this to be about let's go with a 20.
and then go over to the scene view and see what it looks like.
It's going just past our camera view.
We've got this nice long piece of grass.
Let's go back to the game view, though.
And then let's look at the sprite renderer and see what this little warning is because we notice we've got this big exclamation mark.
It's yellow.
And it might be a little concerning.
It says sprite tiling may not appear correctly because the sprite used is not generated with full wctck or sprite mode set to polygon mode.
To fix this, change the mesh type and the sprites import settings to full wctck and sprite mode to either single or multiple.
Now, for our use case, it actually works totally fine because the way these sprites are done, it's not really an issue, but it is something that I hate having there.
So, we'll just go get rid of the error by doing exactly what it said.
So, it says to change the sprite mode.
Let's Where does this to fix it? Change the mesh type, sorry, in the sprites import settings to full wreck.
So, we go find our sprite.
To do that, we'll select the sprite down here.
That's the actual sprite in our project view, not the one on the renderer.
And then we'll go to the mesh type right here, which is set to type by default.
And change it to full wrecked.
Hit apply.
And now our error will be gone once we get rid of the grass.
All that's really doing is making it pull in the entire sprite and not trim out edges if there were transparent empty corners or edges.
But these sprites don't have any empty corners or edges, so it doesn't make any actual difference.
That's why it's not actually changing anything.
So, now we've got our ground down below.
And I think it's time for us to add our player.
To add a player, we're going to go to the players folder.
We're going to select the 128x 256 folder.
This is the one where every sprite is the same height.
The other folder has the sprites at different heights.
We'll talk about that a little bit later when we get into ducking and jumping and all that stuff.
But for now, let's just go into the I'm going to go with blue folder and I'm going to find the blue alien that's idle.
Now, I can't see the names here.
So, I'm going to drag the little slider here so I can see them in list view.
And I'm going to take the one that says um what's his name? Uh alien blue front and I'll drag it right out into the scene view.
Now, I've got an alien sitting here right in the middle of our game.
And I should be able to press play and now have an amazing alien game with some grass underneath.
Let's see it.
So, there we go.
We've got our game and it works, but it doesn't actually do anything.
So, let's stop playing.
To stop playing, we click the play button again or use control or command P.
It's another hotkey I highly recommend you get used to.
Control P, command P to start and stop playing.
It toggles it on and off.
So, nothing happened yet because we haven't set up anything for our game.
We've got no code, no physics, no interactions, just kind of a static scene that we've drawn with some sprites.
Not so much a game yet.
So, in the next section, we're going to start hooking things up.
But before we do that, we want to make sure that we save our level.
To save our level, we're going to go to file and hit save.
That should get rid of that little star there.
And our sample scene name should just say sample scene without a sample scene star.
I don't particularly like that, though.
I don't like us working in a scene named sample scene or that we don't have a level of our own yet.
So, let's save one more time.
But to do that, let's go to file and choose save as.
We're going to go into the scenes folder and we're going to name our level level one.
So, right here in the file name section, we'll choose or type in the word level one with a space and hit enter.
We now have our scene showing up as level one here.
And go check this out.
If we go to the assets folder, go to the scenes folder, we now have a level one.
We also have a sample scene.
I can double click on it and see.
Yeah, it looks exactly the same.
Go back to level one.
Looks exactly the same.
So, not not anything too exciting.
I want to make sure that I don't accidentally work in this sample scene, though.
So, now that I have my level one, it's working and it's loaded.
I'll go down, select the sample scene in my project, and hit delete and delete it again.
Make sure that you're in level one before you do that and that you've saved it and it's all working.
Don't want to go delete that, otherwise you have to go recreate it afterwards.
Now that we've got that saved, we're good to go.
In the next section, we'll start to hook up our physics.
Now that we have our level created, let's talk a little bit about gameplay and physics.
One of the first things that we're going to need to do is set up physics for our player and our environment.
And to do that, we're going to need to add a couple interesting components.
The physics system in Unity is pretty powerful and robust, so you shouldn't have to do a whole lot of complex math or anything else to deal with collisions and combat and all of the normal stuff that you would want to do.
All we're really going to need to do is control the way that the player moves by sending it a little bit of data here and there and reading some inputs.
Sounds a lot more complicated than it is.
Let's take a look at how we can start moving our player around.
How we can start making it interact with the physics system.
To do that, we're going to go select the alien blue.
I'm going to go to this scene view again.
Remember, if you don't see it like this flat, just click that 2D button.
And we should see our alien here right above the ground with some stuff kind of covering his face.
If you want to get rid of the stuff covering a space, by the way, you can click this button to hide all gizmos.
Just make sure that you remember you can bring it back up so you can see that camera view and other things that it will show you later on.
So, I'm going to hide it for now.
And then we'll take a look at this character a little bit more in the inspector.
In the inspector, we've got the sprite render and we've got the transform and perhaps I could write some code that makes this thing move down or I could drag this thing down to make him fall with gravity.
But again, there's a physics system.
We don't want to do that.
but we want to use the built-in stuff.
So, how do we do that? Well, we need to add a component.
We need to add a physics component specifically.
We'll do that by clicking the add component button.
We'll clear out the search box that I've got there and then find physics 2D.
It's about what halfway down here and then click on it.
And you'll see there are a lot of different options.
Don't worry, we're going to cover most of these and they're a lot less complicated than they seem once you've gotten used to them.
So, now that I've got this popup though, I want to find rigid body 2D.
Select that and add it as the component to my alien.
So, now I've got a sprite renderer and a rigid body 2D component.
If I save by hitting Ctrl S or file, save and hit the play button, I should now see my alien start to fall down.
It's going to fall fall and kind of drop back either behind or in front of that ground piece and then keep falling.
If I look at my position here on this alien, I still have him selected.
So, he's showing up in the inspector.
So, he's just falling and falling.
The the value is going down lower and lower and lower.
A lower value on the Y just means it's lower down.
Up on the Y, positive on the Y is up.
Negative on the Y is down.
So, now he's falling very, very far.
So, now I want to make it so that he doesn't just keep falling.
I want to change it up so that my alien um when he falls down and touches the ground, he'll actually stop and land on the ground.
To do that, I'm going to need to add a couple more components.
I'm going to need to first add a collider.
So, to do that, we'll collapse the sprite renderer and I'm going to collapse this rigid body.
Notice you can click on these to collapse and expand them.
You don't have to find that little arrow exactly.
I'll collapse both of those and I'm going to hit the add component button again.
go to physics 2D and I'm going to find the polygon collider 2D.
I'll click on it and it should be added.
And if I zoom in a little bit, I might just be able to see it.
Oh, I've turned my gizmos off.
If I click the gizmos button, I can now see this green outline showing my collider.
It's a little bit hard to see because there's a lot of stuff in front of it.
But if I uncheck this sprite renderer, so my sprite stops showing up.
I can see this green outline showing me my collider.
And the collider is the thing that the game engine is going to use to determine how it actually interacts with the world.
So if it falls down, it'll land on this object.
It won't use the actual sprites.
The reason for that is you don't want every sprite to have collision on it.
Imagine I've got a fence sitting in front of me that I'm walking in front of or past or something that I'm trying to like run behind.
Um that object I don't want to collide with me.
So we have totally separate control over the collisions versus the rendering.
And this is kind of seeing that in action.
All right, let's zoom out with the mouse wheel, middle mouse to pan around and press play.
I'll let let my character fall down and see if he stops on the ground.
So, you can see that he didn't stop on the ground.
He falls all the way through.
And the reason for that is we need a collider on the grass as well.
Colliders only interact with other colliders and need something to actually hit and land on.
So, to add a collider to the grass, we'll go select our grass and we'll choose the add component button again.
go to physics 2D and this time we're not going to choose a polygon collider.
We're not going to choose the polygon collider 2D because we have a relatively square or rectangular shape.
So we can actually choose a box collider 2D.
And the reason that we want to go with a box collider over a polygon collider is primarily performance.
Calculating collisions for squares and boxes for the computer is very easy.
Calculating them for sprites is a lot more complicated.
Even when the sprite is technically just a box, there's no real reason to use a sprite renderer when we have a box.
So, we'll go with a box collider or sorry, a box a polygon collider, not a sprite renderer.
Said the wrong word there.
All right.
So, we've got our box collider.
And if I press play, I should now see that my character lands on top of the box collider.
So, I play and he lands right there.
Looking good so far.
There is an issue though.
If I uncheck the sprite renderer on my grass so that I can only see the collider.
Look at this little green box here.
That's where my collider is.
My collider isn't tiling out and using the same width like my sprite renderer was.
That's actually an option though.
Right here we've got the autotiling check box.
If I check that, the green box went all the way out and now it's covering the entire thing.
I'll recheck my sprite renderer.
Press play.
And it's going to work exactly the same because I was landing over there.
But let's see what would happen if I hadn't done that.
So let's say that I haven't checked autotiling and I move my player over here a little bit to the right.
Like I make his position be oh let's say two on the X.
Now look at the grass.
So the colliders there, my character is there.
If I actually select both of them, I can see the colliders for both.
And press play and see that he'll fall right past falls right past.
Yep.
And then if I go again, check that auto tiling.
So the collider covers the whole thing.
He'll land on top of that ground.
Oh, he did not land on top of my ground.
Why did he not land on top of my ground? Oh, I checked autotiling on the wrong collider.
If we go to the grass mid and check autotiling, then he'll land on the ground.
You got to make sure that you actually selected on the correct object.
There we go.
Looking good.
So, I think that's good.
I'm going to save my level and then we'll move on to moving our player around and setting up some source control.
Before we start writing code or doing anything complicated, we really need to talk about something that's somewhat of an industry standard.
Something that I think is very important that everybody understand, know about, and use.
Whether you're a beginner, a professional, or anywhere else, if you're doing software development or game development, you need to know about this.
And that thing is, you probably saw the title, source control.
We're going to be using source control throughout our project and throughout the entire course for a couple of reasons.
But before I dive into what those reasons are, let's talk about what source control is for those who may not know.
Source control is a system where every revision or every change that you make to your code can be tracked and modified or gone back to or shared with somebody else.
So, when we make changes to our game, we'll do what's called a commit where we'll just check that piece in, save it off, and it's not going to anyone else.
It's just going to be for you, but you'll be able to share it if you decide to later.
But you'll be checking this thing in to a remote system that will then save that version of your project off.
Then you can work on your project some more, and when you're ready, you can check that version in and save off your your latest changes every time.
Now, the benefits of this are enormous.
It might not seem that great.
It might seem like, oh, I could just copy and paste the folder of my project or something like that, which is what people used to do in the olden days is a terrible terrible idea nowadays because there's so much better options.
But let's dive into what what the real benefits are.
The first benefit of using source control is that if something goes terribly wrong with your system, you know, your computer gets stolen, catches fire, your hard drive dies, or whatever else, you're able to recover your work.
Now, when it's a small project, a side project that you don't care too much about, it's not a big deal.
But if it's something you've been working on for a couple months, or it's a school project, or your company work, it becomes a very, very big deal.
And even when it's a small project, it's kind of annoying that you've lost it for no reason.
Um, the other thing that it really helps with is giving you access to your project from other places.
So, if I'm working on a project and I'm using source control, when I commit my changes, they go up to a remote system.
That remote system can be accessed by me.
I can log into it from another computer and download my project, work on it from there, and then upload my changes by committing them again and resume my work on my other system later.
It allows you to go back and forth between computers relatively easily.
In fact, probably the easiest way to do it.
And it's one of the things that I do constantly.
I work on my desktop and I go back and forth to my laptop by committing into source control and committing regularly.
The other thing, and this is probably the most valuable thing that it does for you, is allow you to experiment and kind of play around and learn and try things out without worrying about losing or destroying your project or losing work or anything.
So, if you want, if you got an idea, you want to just, hey, go play around, try something out, you can go experiment all you want and delete things, change stuff up completely, and then you can just rightclick and undo your changes.
You can get go right back to the previous version that you were on or you can even do what's called a branch and have a totally separate version that you can then combine back in or ignore and just abandon later if it ends up not working out.
We'll talk a bit about those more advanced topics later.
Though I first just wanted to really dive in and kind of explain that source control is extremely important.
It's something that you're going to need to know how to use.
It's something that if you're a professional developer, you should already be using.
And it's uh I I think one of the most important things to make sure is also on your resume.
Now, before I show you how to get started with source control, I do want to mention that you can use other source control systems.
The one that I'm going to show you is actually owned by Unity.
They acquired it a few years ago and it's integrated really well into the engine and has pretty good support.
But if you're already familiar with Git or Perforce or something else and you really like using that, feel free to use that instead.
This is mostly for people who aren't already using source control, don't already have a workflow set up for that.
So, let's take a look at the workflow for setting up Unity source control system, which is called plastic SCM.
To get to plastic SCM, you'll need to find the window menu.
Let's go find window right here, and then choose plastic SCM.
This should give us a window down by the console and project windows that has an option to log in or sign up for a Plastic account.
Let's click on that button and we should get this popup.
If you don't get this popup, try just clicking on the button again.
I've had it in the past pop up an error message or just show nothing at all, show something in the console, and then going back and hitting the button again just made it work.
So, now that I'm at the point where I can sign in, I've got two options.
I can sign in with my Unity ID or with an email.
I'm going to use the Unity ID option since we've already set up a Unity account.
And now I should be signed in with my new Unity account that I've created.
Now, I don't know why it gave me an error saying there was an invalid token, but I'm guessing I can just jump back over.
Yep, went back over to Unity.
And now it tells me that it's time to create a new cloud organization.
This is something that we'll be using along the way through the project to do more than just committing files.
We'll also use it for our build automation stuff.
But for now, we just need to hit the create button and come up with a interesting or cool or unique name.
It doesn't have to be something amazing.
I'm going to call this Jason or I put game Jason courses.
There we go.
I recommend obviously don't use my name.
Use something else.
Use whatever it is that makes sense for your organization.
You probably only want to have one of these.
You probably don't need multiple.
So come up with something that you'll want to stick with longterm or don't worry about it and just change it later.
Then choose the correct region for yourself.
I'm going to choose uh US East since I'm in the US.
And then hit the create button.
This should create the organization and create our repository.
So this is doing a little bit more than normal source control but not a whole lot.
It's creating well the repository part is normal.
the extra stuff.
The cloud services stuff is a little bit extra.
All right, so we've got the organization created.
We hit the continue button and then it's going to pop up the documentation.
You're welcome to go through this.
In fact, I recommend that you do.
There is a standalone plastic SCM tool.
We're going to take a look at that later on down the road, but if you want to dive in more into source control stuff, if you're just kind of curious about it, you can definitely check out this documentation.
But for now, we're going to go back into Unity and we should have a little popup like this that says we've joined Plastic SCM or joined our organization or we have a button to join it.
If you don't have this, just click that login button again.
It's possible that the token thing didn't work.
Just hit that button and it should pop you get get you back to this window.
I'll hit the join button and now it popped me back up to the documentation again.
We'll go back into Unity and we'll hit the create workspace button.
Now that I'm logged in, I should be able to create a workspace.
And it's going to come up with a default name.
It's going to say Alien Blaster at JSON coursescloud.
That's exactly what I want it to say.
If you don't see that, if you see, well, you shouldn't see JSON courses, but you should see your own version.
If you don't see that, click this little dropown and make sure that this isn't selected onto local.
I've seen that happen multiple times and it just won't work.
It'll give you a little error, a timeout, or something else.
If that says local, just switch it over to the cloud one, whatever your cloud one is, and then it should work.
The last thing we need to look at before we hit create is this little option for which way we prefer to work.
If we want branching, merging, and the ability to push and pull using a plastic workspace or if we want the older simplified version.
We're going to stick with the default.
We want branching, merging, and all of that.
And then we'll hit create workspace.
This should create our repository and then change our UI to show us all of the files that we've added to our project.
It's got 455 files and I can scroll through them and view them all.
Kind of get a quick list view of them.
See the icons, but I don't need to see them all.
It's all of the files in my project.
So, I'm just going to check this little box here at the top on added and private.
It's going to select all 455 of the 455 items.
And then we're going to type in a message.
I'm going to just say this is a we've added our initial art and level one and then I'll press the check-in changes button.
This is going to commit our changes to the repository, upload them to the remote server, and then show us that we have no new changes.
If you get an error when you click that, probably just click okay and then click the check-in button again.
I've seen that happen multiple times.
An error pops up, you hit check in again and it just kind of works.
All right.
Now that that's done, we should be able to go over to our change sets window and we should be able to see our actual commits.
So right here we've got our added our initial art and level one.
But notice that that's number two.
There's actually a commit number one that was created when we initially created the repository and another one that was created I guess the first one.
So zero was created when we created our repository.
Then it automatically uploaded some of our project settings files.
These are files that you don't need to worry about.
They're managed by the editor and they're changed when we go into edit and then find our project settings.
All of these little sections here have their own little settings file.
That's what was committed in the first one.
And then commit number two is ours with all of the art.
So now we've got all of our art in there.
I've accidentally unloaded my level.
Let's go back into level one and we'll continue on.
All right, it's time for the fun part.
It's time to start writing some code.
To do that though, we're going to need to create a folder for our code to go in and get our code editor set up and running.
Let's start by going into the assets folder.
I'm on my project window.
Go to the assets folder.
We'll right click in anywhere the empty space or anywhere in the empty space.
Choose create and then choose folder.
We'll name this folder scripts.
S C R I pts with a capital S there so that it matches the casing of the rest of our project and hit enter.
I'll hit enter one more time to go into that folder or just doubleclick on it.
Now we have a scripts folder and this is where we're going to keep all of our code.
We can move our code pretty much anywhere in the project, but in general you're going to find that Unity projects tend to keep their code in a scripts folder or something similar.
Scripts is kind of the default that's um recommended and in a lot of examples.
So that's what we stick with.
It's what I generally stick with.
I used to use some custom ones, bounced all around, and now I just go with the scripts folder.
I like that and it works really well.
Let's rightclick now in our scripts folder and create a new script.
So, we'll choose create and right up here, right below folder, there's a C script option.
I'm going to click on it and be very careful not to hit anything else.
I'll get a new script down there that's named new behavior.
And it's right now in renaming mode.
I don't want to hit anything until I've renamed this script.
I'm going to rename it to player with a capital P.
So, hold shift P and then lowercase L A Y R.
And now I've got a player script.
I'll hit enter and it's going to actually generate that script.
Now, the reason that I wanted to be very careful about that is because if you look over here at this script in the inspector, which is not where we'll normally look at scripts, but gives you a nice little preview.
It has this part right here where it says public class player.
And if I had hit the enter button before and then went back and tried to rename this or something, this would be named whatever the file was when it first went in.
So it would have been that uh new behavior or I forget what it was called.
I think it was new behavior instead of player.
And I want this to be player.
So now I've got my script here and it's time to work with it and start writing some code.
To do that, we're going to need to open up our code editor.
And the code editor that's installed by default with Unity and Windows is Visual Studio Community.
And you get Visual Studio Code on uh Mac.
Now, I prefer Jet Brains Writer.
We'll talk about that code editor a little bit later.
I don't want to confuse things though.
So, for now, we're just going to go to assets and go to open C project.
This should open up Visual Studio.
And you'll probably get a window that looks something like this.
If you've never opened up Visual Studio before, first time in, you're going to get this what's new window.
I'm going to close that.
Expand out this assembly part.
Expand out assets and scripts until I can see my player script.
I click on it and double click it and it should pop right up here and show me my player class.
Let's zoom in by holding control and using the mouse wheel.
So, I hold control and mouse wheel to zoom in or uh there's a drop down somewhere around here that you can use.
Ah, bottom left corner.
It moves around.
It's at 214% right now.
So, now that I'm zoomed in, I can see my script nice and large.
And there's a lot of stuff going on here.
If you've never written code before, if this is first time seeing code, first time writing code, it can be a little bit overwhelming, but don't worry, it's going to get all very simple and make a lot of sense relatively soon.
So, the first thing that I want to call out is this class name.
Right here on line five, we have the word public class player.
This is the name of our script.
This is the thing that we've named it when we created the script and it's the thing that's going to show up as our component name when we add it to our actual player game object or that alien that we've created.
So, this is important that it matches exactly with the file name.
If we change the file name or we change this little bit of code here, I add in a K here in the middle of it, we're going to get errors.
Everything is going to break.
It has to match.
It's kind of a weird Unity thing and it's not something that most coding systems require, but with Unity, it's very important that our components that we're going to add or our scripts that we create by hitting that rightclick and create new script that the file name matches the class name.
So, the next part that we have is a colon and the word mono behavior.
Now, this actually means that our player script or our player class is going to what we call inherit from the mono behavior class.
That means that it's going to get some abilities and some stuff that it can do because of that.
It's essentially going to get some of all of the abilities that a mono behavior class has and make them available to our player class.
You don't need to know what all of those are, but we will talk about what some of them are.
It essentially makes it so that our player class does a lot of things for us automatically and we don't have to write code to do all of the things that a game engine would do for us.
Kind of gives us ways to tie into all of the different things that we would care about like when we've hit something, when the player has pressed a button or when every frame has happened.
In fact, that's what this is right here on line 13.
You'll see what we have is a comment.
You can tell it's a comment because it has two forward slashes and it's colored green.
And a comment is just code that doesn't actually run.
It's not really code.
It's like notes in the code just for humans.
This comment says that update is called once per frame.
Which means that this method here on line 14, which says void update, it means that void means that it doesn't return anything.
We'll talk about that in a bit.
For now, just know that that's kind of the default thing you're going to see in front of a method.
And then we have the name of the method, update.
So this update method gets called once per frame.
So, if we have something that we want to happen every single frame of our game, we can just write that right into this update method.
So, let's do something here.
Let's write a little message that uh will log something out to our console every single frame.
To do that, I'll go to line 16.
So, right here in between 15 and 17, click.
And I'll type debug with a capital D.log with a capital L.
And I'll do an open parenthesis.
That's shift and number nine.
And then quotation marks.
and we'll say updated at and then I'm going to put a space and watch this.
We're going to do something a little bit complicated after the quotation mark.
So I moved over to the right of the quotes with the arrow key.
We'll add a space and a plus.
So shift and equals for me at least.
And then we're going to do time do time and then I'll go to the end and add a semicolon.
So take a look at this line.
There's a little bit there going on.
You want to make sure that it's copied exactly as I have it.
debug.log open parenthesis then open quotation marks.
It's a double quotes updated at and then we have a closing quotation marks and then plus and then time with a capital T dot time with a lower case t.
Very important that they all match.
Next, we're going to press Ctrl S and save to get rid of that little star.
So, there are changes to our file have happened.
You're going to find that throughout the process of building games, you constantly forget to save your file and then wonder why things don't work.
Just make sure that you go back in here and hit Ctrl S.
Now I'll minimize the window for our code editor.
Go back into Unity.
And if I press play right now, what do you expect's going to happen? Think about it for a second.
Let's click on the console window.
Press play and think what's going to happen.
See what happens.
We can see in the console window, nothing seems to be happening.
There's nothing appearing down here.
We're not getting a log message like we just written out.
So, how do we get that message to appear? Let's stop playing, go back to the project view, and let's go select our alien blue front, which is actually our player character that we have.
What we need to do is add our player script to the character or to this game object.
Until it's added to the game object, it doesn't exist in the world and it won't do anything.
So, we can write a script.
If the script isn't actually used or referenced in our game, it won't do anything at least until we use it or reference it in our game.
So to do that, we can do well a couple different things.
We can hit the add component button and then we can go down to scripts and then find player.
That works perfectly fine.
That'll add it right on.
I can rightclick and remove it though because I want to show you one other way to do it.
I can take this player script, click and drag it on and also assign it that way.
Now if you just single click, it'll select it and that won't work.
You actually have to go back over here, click on your alien, click and drag and hold it and drop it onto there.
But look, now I've added two players.
That's a problem, too.
I don't want two of them.
So, I'll right click and remove the second one.
Now, I'll save my scene.
So, we get rid of that star, press the play button, and we should see our console start to log out our message that we've written.
Let's see.
Go to console, updated at, and look at these numbers here.
The numbers are actually the amount of time that's passed since the game started.
So, updated at 10 seconds in, 11 seconds in, 12 seconds in, and so on.
Let's stop playing now.
Now, let's go to Plastic SCM and commit our changes.
So, we've got our new player script and our level updated.
We'll say that we've added the player script and attached it in level one.
And we'll check in our changes.
Hit save to make sure that my level is saved.
Oh, and if we get that error, can just hit that check-in button again.
There we go.
Now, we're going to write some code to make our player move or allow our player to control the character's movement with some input.
We'll allow them to move around with a controller or the keyboard that they have.
So, to do that, we're going to need to reopen up our player script and add in a couple more lines of code.
It's actually relatively simple.
You'll be pretty impressed with how easy it is, I think.
Let's open up our player script and then go down here to our update method.
So in our update method right now we have this message that we're updating at some time.
We're going to delete that message.
We don't need to log something every frame.
This is just so that we could see the code and see something happening without doing anything complicated.
So I'll select that line of code and hit the delete key.
That should clear it all out.
Now what I want to do next is move my rigid body component or move my object around using that rigid body component.
So I'm going to need to do two different things.
I'm going to need to read the input from our player and then apply that input to our rigid body.
So let's start by reading the input seeing what that looks like and then see how we can apply it to the rigid body component.
So what we want to do is read in the horizontal and vertical inputs for our keyboard controller and our basically our entire system.
So to do that we can say var horizontal.
I'm going to spell this correctly.
It doesn't have to be correctly, but the next part does have to be equals, and we're going to use the word input with a capital I, I pu t dot get axis, which is a capital G and a capital A.
Then open parenthesis, which is that shifted nine, and a quotation marks, the double quotes.
And here we need the word horizontal.
It needs to be spelled exactly right.
And it needs to be cased correctly, too, with a capital H.
So I'll add a semicolon to the end of it.
So it looks just like this.
Now we've got a variable that will be assigned to whatever the horizontal value is on our system.
We're going to talk about what that means in a moment.
First, let's log this value out.
So on the next line, we'll hit enter at the end.
We'll type debug.log.
And you can see it's actually trying to autocomplete for me.
I can hit tab and tab and it'll just autocomplete and fill that in.
or you if it doesn't autocomplete, you can add the parenthesis and put the word horizontal with no quotation marks.
I'm going to save S.
That got rid of the star there.
And we'll jump back over to Unity and see what this did and how this works.
And now that we're in Unity, it's not going to do anything until we've pressed play.
And of course, it won't do anything if our alien doesn't have the player script.
So, make sure that you select your alien, make sure that it still has your player script that you haven't accidentally forgotten it, removed it, or did something weird, and then press the play button.
Once we do that, we should see our game mode.
We got our character right there.
And if we go to the console window, we should see a bunch of zeros writing out here.
That's because our horizontal input right now is at nothing.
It's zero input.
We're not pushing to the left.
We're not pushing to the right.
But if I click in my game window and I hit the A key or the D key, I'll see this value start to change.
The D should turn it all the way up to a one and the A all the way down to a negative one.
And you'll see it kind of go in between there as well.
What it's actually doing is trying to replicate the behavior of an analog stick.
So if I push to the left, I should get a negative one.
And if I push to the right, I should get a positive one.
You can kind of see that happening.
And the reason that I get the partial values is if I'm like partway over here.
So, if you tap on a keyboard, it'll actually kind of pretend that you slid a a stick over instead of going immediately and snapping all the way over.
So, now we're reading our inputs, and you can see that value showing up there.
Now, we just have to apply that to our player's rigid body to move them around.
First, we'll stop playing.
And then, let's take a quick look at the game object that we have here in the inspector.
We have a player script here.
And if you look to above above this polygon collider, we have a rigid body 2D component.
And what we want to do is tell this play have this player component tell the rigid body how to move or what to do for its movement based off of that input.
So let's open up our player script again to make that change.
To do that, we can actually get to our player script a couple different ways.
We can go back in the way that we went before, or I can just double click on this player script right here, and it'll pop it open.
So now that I've got my horizontal value, I want to apply that to my rigid body.
I'm going to add another line here.
And I'm going to say var RB, which is just short for rigid body equals get component.
And I'm not going to hit tab to autocomplete this because it's actually wrong.
It wants to get a rigid body, but I want a rigid body 2D.
There we go.
I can actually hit the down arrow and select the correct one.
Now I'll hit tab and let it autocomplete.
So, this is going to get a 2D rigid body component.
If I just did rigid body without the 2D, it's going to fail to find that component because I don't have a non- 2D one.
That's for the 3D one.
That was the original name.
It's not called rigid body 3D because there was no 2D long before 3D existed long before 2D ever came around.
So, it was called rigid body.
So, I'll undo that with control Z.
Have my rigid body 2D.
And then we'll go to the next line.
Let's talk actually really quickly about what this git component does.
Git component will actually search the game object that you're calling this component this this code from this player script is attached to.
So it'll search this game object that this alien has with this player script and look for that type of component.
It'll look for a rigid body 2D component and if it exists, it will assign it to this variable.
And in fact, I can change this from being var to be a rigid body 2D and make it slightly more explicit.
Now, on our next line, we're going to use this RB variable and we're going to use it by setting the velocity.
To do that, we say RB, which just gets us our reference.
And look, it actually knows we want to modify the velocity.
Just know what we want to do with it.
We'll say dot velocity equals and we want to make this a new vector 2 or vector three.
I think new vector 2.
A new vector 2.
And a vector 2 is a variable with an x and a y value.
So imagine you've got a grid with an x going along the horizontal and a y going along your vertical up and down.
The vector 2 just has the two values that you have, the x value and then the y-value in that order.
So the first value that we want to give it is the x or the value along the horizontal axis which is going to be our horizontal value.
And then we give it our vertical value.
So how what we're doing up and down.
For that I'm just going to give it a zero and we'll put a semicolon at the end.
We'll save this off and then minimize our window.
Go back into Unity and we should be able to see our player moving around.
Now we just have to hit play play play and then let's use the arrow keys or A and D and we should be able to move left.
Look at that.
I can move to the left or to the right.
Notice that I fall slightly strangely though.
That's because right now I'm actually setting that hor or the vertical velocity.
We're setting it to zero every frame.
So I don't fall smoothly and my falling speed doesn't kind of stay consistent.
So let's stop playing and we'll make one last change to that little bit of code.
We'll go back to our player script and instead of putting in a zero for the y value, let's use our current y velocity.
And we can actually access that by saying rb.ve velocity.y.
So now what we're going to do is modify the velocity, but we're only modifying the horizontal part, not the vertical part.
Now you might wonder why we can't just do rb.ve velocity.y y or x, sorry, equals horizontal.
And that's because we can't assign one of the variables of a vector 2.
You can't modify the x or the y of a vector 2.
You can only create a new vector 2.
So, we have to not do that and assign that new vector 2 where we pass in the horizontal and the velocity.
Let's go see what this looks like in game.
We'll jump back in and press play.
We should be able to move and then see our character kind of falling slightly more naturally.
They're going to get that regular gravity fall.
There we go.
Yep.
Gravity fell and everything was a little bit normal.
So, we'll stop playing.
We'll go back to plastic SCM and commit our changes.
Say that we've added horizontal movement to our player and check in the changes.
Now, we're going to give our player the ability to jump.
To do that, we're going to open up our player script and we're going to make a couple little modifications.
Instead of just setting the velocity or the vertical velocity to its current vertical velocity, we're going to want to set it to a jump velocity when the player presses jump or leave it at that if the player hasn't pressed jump.
So, how can we do that? Well, let's add a line right between line 18 and 19.
So, I'll go to the end of line 18, click here, and hit the enter key.
And we're going to create a new variable.
We'll say var horizontal equals no not horizontal vertical var vertical equals and we're going to set it to equal to our rb.v velocity.y.
Now we're going to hit enter and I'm going to hit escape.
The autocompletes popping up.
Those are all that gray stuff there was just autocompletes.
So just hit escape and it disappears.
Now, what I want to do in my velocity setting is instead of setting it to a new vector that's the horizontal and the current velocity, we're going to set it to the horizontal and the vertical.
And right now, this actually hasn't changed anything at all.
It's going to do exactly the same thing.
All we've done is added another variable here.
Instead of setting it directly to this y values var value y variables value, we assign it to a vertical variable.
And then we're just using that.
So we need one more bit of code.
We need to check to see if the player has pressed the jump key.
So we're going to add in a if statement or an if statement.
We'll say if and then we're going to do open parenthesis.
Notice that it's purple because it's a different type of keyword.
It's a new one.
What this is going to do is check to see if something is true.
And if it's true, it's going to run some extra code.
So we say if input get button down capital B, capital D, and a capital G there.
and we use our open parenthesis and quotes and we're going to check for fire one which is our leftclick button and I think it's also our space button.
So if we have pressed that button then we're going to run the code on the next line which is going to say vertical is equal to and we're going to assign it to let's just say five.
So we're going to give it a big value of five upwards and then we'll hit enter and add in a new line.
So we'll save with control s get rid of that star and we should have no errors.
If I hit control shiftB, it should actually do a build and show a build succeeded message down there.
If you don't see that, if your hotkeys are different, go to build and look for the build solution one.
Control shiftB is the default.
That's what I use.
Make sure there are no errors.
So now I've got my update method with the check to see if we pressed fire one.
That should modify the vertical velocity whenever we press fire one.
So let's minimize this window.
We'll go back into Unity.
We'll press play and then we'll see if it works and then talk about where these buttons are coming from.
So, we hit play.
I can click and look at that.
My character jumps up, bounces up.
I can move left.
I can move right.
Kind of spin around and jump.
I can spam jump as fast as I want.
It just seems to work.
So, all right.
So far, things are looking pretty good, I think.
But you might be wondering where are these inputs coming from? What is this all? Where's this magic? What are these strings? Let's go take a look at our edit and then project settings.
You go to edit project settings.
You should get a window like this and then look for the input manager section.
In the input manager section, there's an axis section or an axis drop down tree, I guess, you can expand.
And underneath it, you'll see that we've got horizontal.
Look at that.
It shows the keys that it's bound to.
We've got vertical.
We've got fire one, fire two, and so on.
Yeah, it was left control and mouse zero.
So, you can see what these buttons are.
Um, fire two is the right click and I think fire three is your middle click.
These are all part of the old input system.
This is the system that's been built into Unity forever.
It's very simple, very easy to use.
It works great for the most part, but it does have some downsides when you start to get into doing multiplayer development and other things.
Relatively soon, we're going to switch away from the old input system to the new input system.
But I wanted to make sure that you understand that this exists, understand how it works and that it's slightly different from the one that we're going to be using throughout most of the course.
But you will see projects that are using the old input system constantly and tutorials and everything else.
So, it's very important that you understand it, know it exists, and even if you don't regularly use it, you should know that know how to use it.
So, there we go.
Let's go back into our plastic SCM window and let's commit our changes.
So, right now we've added a jump.
So, we'll say added a basic jump and check in our changes.
Cool.
Now, we're going to make some modifications to our jump.
Our current jump makes our player bounce up every time we click.
I can keep clicking as much as I want, but I can't hold and jump.
I don't have a whole lot of control over it.
So, what we're going to do is modify our jump code, add in a member variable, and take a look at some timing.
Let's stop playing and open up our script.
To do that, I'm just going to double click on one of my log entries down here just to show you another way that we can open up scripts.
Double click a log entry and it'll actually take you to the script at the specific line where that log was being written.
Notice that my cursor is right here at the end of that debug.log line.
If it doesn't work the first time, sometimes you just got to double click on it again.
Sometimes it's opening up the project for the first time or something.
So, let's continue on by looking at our code.
The code that does the jumping is here on line 21 and 22.
We check to see if the player has pressed the fire one button, which remember a moment ago we looked at was bound to the left click on your mouse or I believe it was left control.
And if they have pressed that in this frame, then we'll set their vertical up to five.
Otherwise, we set their vertical to the current velocity.
So, it just continues to fall down.
So, what is this doing? Well, it's only checking when we press the button.
Let's change it real quick and get rid of the word down here.
There's actually a get button method, a get button up, and a get button down.
Let's just change it to be get button though.
And I'll hit Ctrl S and save.
Make sure that that star goes away.
Make sure it's spelled exactly right.
Jump over to Unity and guess what's going to happen if I hold my button down now.
Well, I'll let you guess.
I'll let you try it out and then see if you guessed right.
So, we start to play and we fall and I hold the button down.
And look at that.
I continue to go up for as long as I hold the button down.
And that's because the get button method is checking to see if I'm still holding the button down or if the button is down this frame where get button down is checking to see if the button was pressed down this frame.
It's a little bit confusing.
Again, you don't need to worry too much about these because we're going to move on to the new input system shortly after this.
But for now, let's just remember that get button down is for pushing it down or the event when it fires or when it's pushed down, the frame when it's pushed down.
Get button up is for the frame when it's released.
So if you release the button, you can have it do a jump on release or get button is the one for checking to see if it's currently down this frame.
It'll be true for every single frame.
All right, let's go back into the code.
So we now know how to check to see if the fire button is being held down.
Now, how do we make it so that we can only hold the fire button down for a certain amount of time? Because I want the player to be able to jump and hold the jump, but maybe only for 1 second or something.
I don't want them to be able to hold it indefinitely.
Well, to do that, we're going to need to keep track of when the player started jumping.
And we know how to track when the player started jumping, or we should have a good idea because we just talked about it a moment ago.
We can use the get button down method to see when they've started jumping, keep track of that time, and then use that time in our calculations to see if they can continue jumping or not.
So, let's add in a new line here above line 21.
So, right after 20, I'm just going to add in a line.
So I have a little bit of space.
And here, let's check to see if the player has pressed the fire button this frame.
So that means that they've started the jump.
If they have, then we'll keep track of when they can release the jump or when the jump has to end, I guess, is really the way that I want to say that.
So say if input.get button down.
Remember, this is the one that fires off whenever the button is clicked for the the first time for the frame or the first frame that it's pressed down.
So we'll put in fire one.
So if the fire one button is pressed, we want to run the line of code right after it.
And that line of code is going to say that our let's see jump end time is equal to time dot time plus and let's just add a one here.
So we're going to add 1 second to the current time.
So our jump's going to end 1 second from now.
That's the longest we can hold it.
I'm going to add in an extra line by hitting enter.
And then notice that our jump end time doesn't exist.
So we need to create this variable for our jump end time.
And we're going to create this variable as a member variable.
So instead of it being something inside of our update loop where we have here this update method where we have for instance our var horizontal and our var vertical we can't do a var jump time or jump end time equals zero here because if or we'd have to put an f because it's going to be a floating point v value.
We'll talk about that in a moment.
We can't do this here because this jump end time would get reset every single frame.
So every frame the code would run through jump end time would get created set to zero and then the time would get checked to or maybe get set here.
And this would not work at all.
We need to keep track of jump end time across update loops.
So we're going to delete this line 21 here that I've added there.
And I'll hold shift and delete to delete out those extra lines.
Shift delete will actually delete whatever line you're on.
Just make sure you're on the correct line.
Remember you can always control Z to undo.
Shift delete to delete those lines.
So, we need to make jump end time into a member variable.
And there's something special that I do when I create member variables.
And that's I go to the beginning of them and I usually add an underscore with shift and the key.
It's next to zero.
Adds a little underscore there.
And this just is an indicator for me that this variable is something that's going to be used across multiple methods.
It's not just a method or a variable that's for this method only.
So to create this member variable, there are a couple things that I could do, a couple different options.
One, I could copy the name of it, and then go up kind of to the top of my script here, paste it in with with writing the code.
I'll show you how to do that later, cuz the other way that you can do it is just hit alt enter, and then hit generate field.
This looks a little bit different in every editor, but it's pretty much the same.
It's always available.
There's always a generate field option.
and we'll just hit generate field.
And you'll see that I now have a private float, which is a floating point number.
It's essentially a number that has decimal points.
There's a little bit more to it, but just think of it as a number with decimals versus an int, which is a number without decimals.
We've got our variable name jump end time.
And notice that this is inside of this player class squiggly brace here.
So, there's an opening squiggly brace at the end of our player class definition or declaration.
And there's the variable here inside of it.
We also have our start method in here.
We haven't really talked about that one yet, but it's up here.
We can kind of ignore it for now.
Let's look at the update.
The update method that we've been using is also inside of this squiggly brace.
The main thing to note here is that this variable is inside the class.
It's part of the class, but it's not part of the method.
You see how look inside update? It's not part of the method.
So, it's going to be stored and kept along or persisted indefinitely as long as this object is around, not not updated and recreated every single frame.
So, now that we have that time, we need to actually use it.
And to use it, we're going to modify the if statement on line 26.
Remember, this statement checks to see if the player still holding down the fire button.
And if so, it runs the code on the next line 27 that sets our vertical to five so that we go upward.
What we want to do though is check to see if they're holding the button and if it's not past the jump end time.
So if the current time is not greater than or past or beyond the jump end time and we can do that in an if statement by adding a double amperand after the first condition.
So our first condition is this input.get get button fire one all the way up to the ending parenthesy right there that middle right in between them.
So we'll just add a space between the two parenthesis and add two amperands shift 7 shift 7 and we'll check to see if jump end time is greater than time dot time.
So, if jump end time is sometime in the future, any time up to 1 second from when we initially set it, then we'll allow our player to continue jumping.
If that's not the case, so say jump end time is at 1 and our current game time is at two, then well, we can't jump because we've already started falling.
We should have landed.
Let's take a look at that in practice and see how this actually works.
So, we'll save S to get rid of that star.
Minimize our window.
go back into Unity and then press play.
We should expect to see that we can jump up and then start to fall down automatically.
We can still click and spam click all the way up if we want.
We haven't stopped that, but my maximum jump should now be about 1 second.
There we go.
I click and hold and I fall after about a second.
Now that that looks good, let's go modify it a little bit and make that jump half as high.
So, I'm going to go back to our code.
And when we modify our jump end time or set our jump end time here on line 24, we're adding one to the current time so that we can jump for up to 1 second into the future.
Let's make this half a second.
To do half a second, we just need to put a value that's half of one or 0.5.
Whoops.
Got to get it on the right spot on my keyboard.
0.5.
Get my semicolon there.
And notice that we've got a little error here.
What it's actually telling us is that this 0.5 is a different data type.
It's a double and not a float and jump end time wants a float.
It's nothing that you really need to worry too much about.
U we'll talk more about data types and numbers later.
You just need to know that when you see this, you need to add an F just so that it knows that you want this to be a 0.5 that's a float, not the 0.5 that's not a float, so that it can actually work.
So if you see that error again, remember, just try adding that F to your zero.
We'll save, get rid of the star, minimize, and let's go see if our jump is now cut in half.
That's what you should expect to see.
So, hit play and we hold the button.
And look at that.
Now, I'm jumping.
I would say about a reasonable height.
So, let's stop playing, go back into plastic SCM, and commit our change.
say that we added a maximum jump time to the player and we'll check in our changes.
Now, it's time for us to learn a little bit more about variables.
What we're going to do is modify our player so that we don't have to go into the code and change things when we want to modify how long the player can jump or even how fast the player moves.
We're going to make some variables that are these fields that we talked about, but we're going to make them available to us at runtime in the inspector.
It might sound like a lot.
It might sound simple.
Don't worry, it is simple.
Let's start by opening up our player script.
This time, I'll double click on our player.
Actually, I'm going to stop playing first.
Actually, I'm not in play mode.
Double click on our player.
And I'm going to find our jump code.
So right here where we do the jump, we set our jump velocity to five or we set our vertical velocity to five, which is our how high we are f how fast we want to jump.
And by the way, if you're wondering what that five is, that five actually represents meters/s.
So we're jumping up at 5 m/s.
Imagine that the game is scaled to one meter um units.
So each block that we move over is 1 meter and we're going to jump up five of those per second.
That's what that is.
So we need to make this variable so that we can adjust this without having to come into the code and change it over and over.
Same with this maximum jump time.
We had to go in and change this by putting a 0.5 instead of a one.
Let's say I want that to be variable as well.
Well, to do that, we're going to create a new field to I'm going to delete my five here.
So, I've got my cursor right at the beginning of the five.
I'll hit delete.
We're going to create a new field, and I'm going to call this jump velocity.
Since it's going to be a member field that's going to be stored up at the top like this, I'm going to put my underscore there.
Again, this is more of a syntax that I just prefer.
It's not required.
You don't have to have an underscore there.
Sometimes you'll see an underscore.
Sometimes you'll see an M with an underscore on some really old stuff.
And sometimes you'll see absolutely nothing indicating it.
I just like to have something there indicating it that it's not part of this me member or this method here.
It's not a variable like this horizontal.
It's something that's stored at the class level.
I'm going to give this the name underscore jump velocity.
There we go.
V E L O CI TY.
And then I'll hit alt enter.
And I'm going to generate a field for it just like I did before.
Now, one cool trick that I can use is hitting F12 on my keyboard to go right up to that definition.
F12 is the go to definition hotkey and it'll take you right to wherever the thing is defined.
So here I have my jump velocity, but it's not set to anything.
It's not set to that five.
And right now if I save, it's not modifiable in the editor in the inspector.
What I need to do is take this private keyword.
I'm just going to double click on it.
Or actually, let's go to the front of it.
We'll just leftclick it right at the front.
And we'll add a square brace.
This is the key right next to P on my keyboard.
and we're going to add the word serialize field and then a closing brace the key right next to that other one.
Now, make sure that you spelled it right.
There's no D.
It's not serialized.
It's serialize field.
And then there should be the braces around it.
It should light up.
You can hit save with control S.
Go back into Unity.
And now you should see a jump velocity on your player.
If you don't see that, make sure that you've selected the alien.
Don't be on the grass or the light or something.
Go to the alien.
Go find your player script.
If it's collapsed like this, expand it out and then find the jump velocity.
Also, if you have too many things expanded, it could be way down at the bottom.
Just collapse the other stuff.
So, we've got a jump velocity right now that is a zero.
So, the default value right now is zero.
And I don't like that.
So, let's go back to our player script and give it a better default.
We had a value of five before.
So, right at the end of jump velocity before the semicolon, we'll add an equals and we'll put in a five here.
By the way, the semicolon is always the indicator for the end of a line or a command.
We don't have it when we have braces.
So, you're not going to see semicolon at the end of a brace, but you do see it at the end of every variable definition and at the end of every line that's executed.
Not at the end of a method with the braces, but at the end of everything else pretty much.
Let's save.
And often if you see an error like this, say I delete that, this little expected semicolon.
Look, if I put my mouse over it, you'll see it says CS 1002 semicolon expected.
Ignore the part above it, the readonly strruct part.
You don't need that.
That part's a little confusing, but it's telling you right there it needs a semicolon.
So, let's go add a semicolon.
Save again.
And it should work.
We should now have a default value of five showing up here, unless we've modified that value already.
Let's see.
Did it show up? Oh, no.
It didn't actually show up.
That's okay.
So, if it doesn't show our default, we can rightclick and we can choose reset.
That'll reset to the default.
Now, you don't want to do that later on once you've set up a whole bunch of stuff because it's going to reset everything to defaults, but right now there's really nothing on there except for our jump velocity.
So, let's play and see how this works.
I'll hit the play button.
I haven't saved, but that's okay.
I probably should have, but it'll be fine as long as I don't crash.
I should be able to jump.
There we go.
And I jump to about halfway up my screen.
Let's change this jump velocity to 10.
So, I jump 10 meters per second instead.
And then I'll jump.
And look at that.
I now jump way above my screen.
Let's change it down to one.
And you can see that I have a very slow, very small jump.
Now, I like the value of five for now.
So, I think I'm going to go back to five and just leave it at that.
But we now have the ability to modify it completely.
Let's continue on and make it so that we can modify the jump duration as well.
We'll go back to the player script.
And just like we did the jump velocity, we're gonna do the same kind thing for our jump duration.
We have this 0.5 and we're going to need to figure out a way to make a variable that controls how long this player can jump.
In fact, what I'd like to do now is present that to you as a mini challenge.
Don't worry if you get lost.
I'll show you how to do it in a moment.
But my goal for you is that you go through this process and create a jump duration variable.
see if you can create it yourself and then continue on and I'll show you the process to do it in case you got lost or had any problems or questions.
So, go ahead and give that a try now.
All right, it's solution time.
Let's change this 0.5 and put in a variable.
Hopefully, you've found a way to do this by just putting underscore jump duration or something similar and then hitting alt enter and generating a field.
Then I hit F12 to go to that field.
Hit home to go to the beginning of the row there.
And then put in my square brace and do serialize field.
There we go.
I'll save with S.
Oh, and let's give it a default time.
Right now I have it at 0.5 seconds.
So I'm going to add in a 0.5F right there.
We'll save one more time.
Minimize the code editor and jump back into Unity.
And I should now see a 0.5 value and my jump velocity.
There we I've got a jump duration and a jump velocity.
Let's try jumping and see if it actually works.
So, we jump and I go about half the way up.
Let's change that jump duration to 0.25.
Try jumping.
And yep, I jump quite a bit shorter.
And if I change it up to one, I can jump for a very long time.
All right, I now have two variables that I can modify and see how I like things and get them to the levels that I want them at.
There are a lot of different ways that you can use these and we'll be talking about them and using them in different ways in the future.
But just remember that if you want to make a field modifiable, you want to have a variable that you can modify in the inspector.
The key thing you need to use is this serialized field attribute.
There is one other way to do it.
There is an alternative way to do it, which is to make this public instead of private.
We'll talk about what that means later, but it's not the way that I would recommend doing it.
You can replace this right here with the word public.
Save and it's going to work exactly the same.
Everything will work.
You'll have no problems except that this jump velocity could get messed up later.
And I'll talk about how that happens in a later lesson because it's a slightly more advanced topic.
For now, I'm going to hit control-z, save, and then go back into plastic and commit my changes.
So, we've added two variables, a jump velocity and a jump duration variable.
also say added jump velocity and duration variables to the player and commit or check in.
The next change we're going to make is going to require us to take a deeper look into the Unity physics system.
Right now, we can jump unlimited numbers of times while we're flying around in the air.
There's nothing really stopping us from just flying indefinitely.
Now, I want to change that.
That's more like a swimming mechanic.
I want it to be so that we can only jump when we're on the ground or when we've decided that we want to let the player jump.
Maybe it's off of a wall.
Maybe there's a double jump.
But for now, only when they're landed on the ground, not this weird state where I can just keep jumping indefinitely.
To do that, we're going to need to figure out when the player is on the ground.
Let's stop playing and let's go to the scene view real quick.
So, here I am at my scene view and I've got my alien selected.
I'm going to double click on him and then zoom out just enough so that I can see the ground.
Now, when I play my game and I let my character fall down, let let's see what happens.
I'm going to take the game view.
I'll drag it down here to the bottom so it's kind of out of the way.
Press play and watch as the player falls down.
So, he falls down and he kind of lands there.
And I've got, you know, him right above the the actual ground.
I need to determine how how to tell if he's kind of on the ground or I need to find a way to tell if he's on the ground.
And there are a few different options for this.
The way that works the best though, the thing that I found to be the most useful is to do what we call ray casting, which means that we'll do a little check.
We'll add essentially a little laser right down here at the bottom of this character and shoot it down and see if there's ground underneath him or if there's not ground underneath him.
And if there is ground underneath him, if he's like very close to the ground, then we'll allow him to jump.
If there isn't, then we won't allow him to jump.
Now, to see this or to get this working, I like to visualize it first.
So, I like to open up my Let's stop playing, open up my player script, and add in some code to draw some cool gizmos so that I can see what I'm doing and kind of understand it quite a bit better.
To do that, we're going to find our start method.
And I'm actually just going to delete this first.
We'll take lines 11 through 15 and just hit delete because we haven't needed our start method and it's just kind of sitting there taking up five lines and getting in the way.
So, I'm going to delete them.
My code should now look like this.
I've just got my fields up top, my floats, my three floats, and then I've got my update method and then my closing braces.
Make sure that everything matches before you start.
And then right here on line 11, let's add an ondraw gizmos.
Now, notice that I didn't capitalize it.
That's because I know it's going to autocomplete and I'm just going to hit enter and it's going to capitalize for me.
So, it automatically created an ondraw gizmos.
It's got the private void part right at the beginning and the parenthesis.
I don't actually need this private keyword.
So, I'm just going to double click on it and hit delete twice just to get rid of it.
The void method doesn't have it.
Um, ondraw gizmos doesn't have it.
It doesn't need to have it either.
The reason for that is that private is the default.
It's like uh adding a special decoration to say that it's already the thing that it is.
So, we don't need the private keyword there.
It's already private by default.
The alternative is public and we don't need this to be public.
We'll talk a lot more about public and private later once we get into some scenarios where it actually makes sense.
In our ondraw gizmos method, we have the ability to draw gizmos on the screen or in the scene view.
Now, if you're forgetting what those are, don't worry.
We'll come back into Unity and take a look.
Remember this little world that toggles all the gizmos on and off? That's that these little icons, the colliders, and other things.
This is going to be our own custom one.
So, let's go back to the player.
Let's draw a simple line.
First, we'll say gizmos.draw line, and we're going to draw it from vector 3.0 to vector 3.1.
And we'll add the semicolon to the end.
Let's go back into Unity and see what that does.
We should expect to see a line right around the center of our world.
There we go.
Going from 0 0 to one one.
So, this is now actually in 3D, too.
If I go into the 3D view, you'll see that it's actually moving kind of over there backwards a little bit.
If we go back to 2D, though, it looks pretty flat.
So, this draws a line from one point to another point.
What I want to do is draw a line from the feet of my character just downward a little bit.
so I can see where I'm checking for the ground.
To do that, we'll go back to our player.
And we need to figure out where the feet of our player are.
To get the feet of our player, we're actually going to use the sprite renderer component.
Remember, that's the component right here that's drawing our sprite.
This thing knows where the bottom of the sprite is.
So, we can use that value or use the sprite renderer to get that value and then pass it into our gizmo system.
So, let's go back into the code.
And the first thing I want to do is calculate where the bottom of our character is.
And to do that, we're going to need to use the sprite renderer component.
Remember how we got a component before on line 21 using the get component method.
We're going to do the same thing here on line 13.
We're going to add in a new line for our line 13.
And we're going to say sprite renderer.
And let's call this sprite renderer with a lowercase s.
Notice the casing here.
We've got an uppercase sprite renderer and a lowercase sprite renderer.
The uppercase one is telling us that this is the definition or the type, the class definition, the sprite renderer type.
We're going to say that whatever comes after this is going to be a sprite renderer.
And then we're going to name it the exact same thing, but it can't have the the same casing.
We want to have a lowercase casing or what we call Pascal case.
So it starts with a lowercase S and then we add in the capital R there so that it's easier to read.
I mean if we did it like this sprite renderer it would just be harder to read.
That's why we use Pascal case or camelc case not Pascal case and it's much easier to read.
This is C Pascal case with capital S.
This is camelc case with the lowercase S.
That's the difference between the two of them.
All right.
So sprite renderer sprite renderer equals.
And then look at that.
It already knows what I want.
I'm just going to hit tab and let it fill it in.
Get component sprite renderer.
So that's going to get our renderer.
And the renderer has a couple of unique or interesting fields on it.
The one that we care about right now is the bounds.
So we can get the bounds of the sprite renderer to tell us where the top, the bottom, the left, and the right are.
So let's go back into our code and we'll do that by saying let's let's actually keep this off as a y value.
So say float bottom bottom y equals and we'll use the sprite rendererbounds.extense.y.
Now let's use this bottom and this position in our draw line.
To do that, let's actually create a vector 2.
We'll say vector 2 origin and we'll make it equal to a new vector 2.
And we're going to use our characters position.
So we'll say transform.position.x.
And then for the y, we'll use transform.position.y.
But we're going to subtract out that w that bottom y or the extents.
So we'll say minus bottom y.
Then we'll add a semicolon here.
And then on our draw get draw line code, we'll change it from going to zero or starting at zero to starting at origin.
And for our second value here after the comma, I'm just moving around using the arrows.
By the way, if you use control in the arrows, you can actually bounce around word by word.
Hold down shift and you can bounce over here and select the word.
So I'm going to select that vector 3.1 and replace it with origin plus.
And now what I want to do is do a line that goes downward just a little bit.
So I'm going to use a vector 2 down times 0.1f which is going to give me a downward vector that's one/10enth of a meter.
Remember vector 2 down would be down one unit or 1 meter time 01 is 110th.
So it's going to take us down one/10enth of a meter.
So, I should get a line going from the bottom of my character down one/10enth of a meter.
Now, one last thing I want to do is make this line red.
Let's do it right before we draw it.
Let's go up ahead up one line.
Add a line on 16 and say gizmoscolor equals color with a capital C dot red with a lowercase R.
We'll save.
Get rid of that little star.
Jump back over to Unity.
And let's see if we have a little red line pop out of our character once it finishes reloading.
Here it goes.
And look at that.
We've got a little red line down there.
So, we haven't used this to do anything except for draw a red line.
But watch when I move my character around.
Oh, accidentally added a child object there.
Let's move this guy around.
And look, we've got a red line following him around.
So, that's perfect.
That's kind of what I wanted to see.
So now what we want to do is make it so that when our character's red line is overlapping with the ground, we can jump.
If it's not overlapping with the ground, we can't.
By the way, I'm just clicking and dragging him, moving him around.
Remember that's W on the keyboard to get into move mode.
Or you can click the move tool right here.
You could be on a different tool like the panning tool or the rotating tool or something else.
Just go to the move tool with W and move him around.
So so far so good.
We've got our character drawing the line to show us where he's checking to see if he's on the ground.
And I think that's good for this lesson.
So, let's save.
Go into plastic SCM and say that we added a grounding gizmo.
We'll talk about what grounding means in just a moment.
Added grounding gizmo and check in our changes.
Now that we've visualized where we want to do our physics checking, it's time to do the actual code for physics checking.
And again, this might seem complicated.
It's going to seem simple by the end of this course.
Let's open up our player script one more time.
And we're going to go down to our update method.
In our update method, we want to check to see if the player is touching the ground or if they're not touching the ground.
And we want to do that by using this little laser that we've drawn in the gizmos.
But unfortunately, the gizmos are just a debugging visualization.
They don't actually give us any information back and the gizmo code can't check to see if we're touching the ground or anything.
It just gives us an idea of what we're looking at.
And as long as it matches up with our physics code, then it'll tell us kind of what's going on with our physics code.
So, what we're going to do is use the physics 2D ray casting system.
And if you want to take a look at the documentation for it, the Unity page has pretty big documentation that goes over a lot of the different parameters that are available and has some example stuff, but I feel like the examples a little bit more complicated than what we need right now.
Let's go back to our code now.
And before we make the physics code, let's do one little change to our gizmos code.
Right here on line 15, we calculate our origin by using our position and then this bottom y variable.
The bottom y variable is assigned right above on line 14, which is actually just the extents.y.
Let's replace bottom y here with just extense.y.
So we can get rid of this variable.
And I'll explain why we're doing this in just a moment.
But first, we'll copy.
So I'll select this whole sprite renderer.bounds.extense.y.
control or command C or rightclick and hit copy.
And then go to bottom Y over here.
Just double click on it and controlV or commandV to paste over it.
I'll zoom out with the mouse wheel here.
So it's control and the mouse wheel.
Remember this little slider down here.
So I guess it's like a drop down.
Go to 100% or whatever.
Zoom back in a little bit.
But now we've got this origin calculated without this extra line here on 14.
I'm going to go to line 14 anywhere on it.
Hold shift and hit delete.
And then I'll explain why we did that.
We're actually going to reuse this origin right here down below in our update.
And if we have two lines of code that we have to copy, then we have two lines of code that we need to update and double the chance of making mistakes.
If we cut it down to a single line here that does everything we need, and we don't need that extra variable, which really wasn't very useful for us, then this will just kind of work.
So now we're going to take line 14 and we're going to copy it.
We're going to hit Ctrl + C and then we'll go down to line 21.
Hit enter.
Enter.
I'm going to go up.
I just wanted a little bit of space there.
And then hit Ctrl +V.
We're going to get an error here.
Take a look at it and see if you can spot the error.
You should be able to tell by the little underlined squiggly that there's a problem here.
It's saying, "Hey, this sprite renderer does not exist in the current context." And why is that? Well, if we look at it up here on line 13, we're finding the sprite renderer, but that's inside of our ondraw gizmos method.
Down here on line 22, we're inside of the update method.
Since this variable is defined inside of a method, it's not a member variable.
It's not available to everything in the class, only to this method.
So, our update method can't see the sprite renderer.
Now, our jump duration and jump velocity, jump end time, these variables are all defined outside of the scope of a method.
So, they're all accessible outside of there.
So, what we could do is make it so that our sprite renderer is available outside of the scope.
There are a couple issues with that, specifically with how on draw gizmos works, or we could alternatively just get the sprite renderer down and update.
And that's where we're going to start.
and we'll talk about caching and some performance benefits of other ways we can do it a little bit later on.
So let's take line 13, select the entire line, copy it with control or command C.
Go up above line 22 right here on 21 after the brace.
Enter.
Get a new line and controlV to paste.
The error should go away.
And now we have an origin.
We haven't done anything with it yet, but we've got the origin in our update method.
Let's add a new line.
And so I'll click at the end of line 23, add one more line.
And in here, let's do our raycast.
We're going to say var hit equals.
And this is where we're going to tie into the physics system.
Physics physics 2D.
Got to get that 2D part in there.
Dot raycast.
Then we'll do an open parenthesis.
And the first variable that we need to give it is the origin.
So that's where we're going to start.
And notice that I name my variables to kind of match.
That's just out of habit and out of experience.
I know that origin is what it kind of expects and that's the start of a ray or the origin of the array.
So I name my variables to match.
It's not something magic.
It doesn't have to match but it does because of habit habit mostly.
So our first variable is the origin.
The next variable I hit comma and space is the direction.
And the direction that we want to go in is downward.
To get down, we'll do vector 2 down.
Next, we need another parameter.
So, right now, it would allow me to add a semicolon and be done.
But that's not what I want.
That would give me a ray that goes from my origin down infinitely forever.
I want to add another comma here after the down.
I want to add a maximum distance.
And I want to go that 0.1 m or that tenth of a meter.
The same variable that I've got right here.
So, 0.1f or the same value.
It's not really a variable.
It's more of a a constant.
And the last thing that I want to do is check for the ground.
And to do that, it's a little bit more complicated.
So, we'll wait until the next um the next section.
We'll get into the the layers, but there actually is another layer mask here that we'll use shortly after.
For now, though, we're just going to go with these three parameters.
And then we'll go to the next line and we'll say if and then open parenthesis hit.c collider and then closing parenthesis.
So what this is going to tell us is if we hit an object and that object or we hit something and there's an object there.
If that's true then hit collider will just basically return back true.
It's actually going to give us back the collider the instance of it.
But this variable check, this if check is going to be true.
If that thing exists and if there was no collider, if we didn't hit anything with our laser beam, then it's going to return back false.
So if we did hit the something with it, then we want to set a variable to true.
And we're going to set a member variable, something that we can see in the inspector and that we can use later on.
Let's call that is grounded with a capital I.
Okay, so we'll say is grounded equals true and a semicolon.
Now we're going to hit enter.
Don't worry about that error.
We're going to address it in just a moment.
Next, we're going to write the word else.
E L S E, which is also going to be purple.
And then we'll hit enter one more time.
We'll say is grounded equals false.
Now, if your editor added some braces around things like this, don't worry.
You can just delete those.
You can leave them in there, but if they're the wrong way, then you don't want to have them there.
So, you can just hit shift delete.
And shift delete get rid of those braces.
Now, what are we going to do about this is grounded? And what does this else statement mean? Well, the else statement means that if it collider is true, well, we'll set is grounded to true, but if collider is not true, so otherwise or if else, not if else, but else, then is grounded will be set to false.
So, we're essentially setting grounded to true if we've touched something with our laser and setting it to false if we haven't.
But is grounded doesn't exist.
So, we need to create it.
And to create it, I'll select it, hit alt enter, and we can generate a field, a property, a local, or a parameter.
The one that I want to choose is a field.
We're going to generate a field right up at the top.
And it's going to give us a private bool named is grounded.
And I'm going to change this private and make it public.
We'll save.
and then look for errors.
Let's go take a look at the entire script.
This is all of the script.
This should show us everything.
Let's jump back into Unity.
And now if we go select our player, we should see that is grounded field.
Remember that I said that public fields and serialized fields both show up in the inspector, but public ones you want to use a little bit differently.
Let's go check it out.
We should see our public field showing up any second now.
as soon as it finishes compiling our is grounded.
Let's press play.
There we go.
And I fall down.
When I'm on the ground, the is grounded is checked, which means true.
And when I jump in the air, it's not checked.
As soon as I hit the ground, it's true.
And checked.
As soon as I jump off the ground, it's not checked.
Pretty cool, right? Now, we can tell whether or not our player is grounded.
The last thing that we need to do for our jump modification then is go down to the jump code where we check to see if they've pressed the button down.
And we just need to check if uh they're grounded as well.
So if they're not grounded, then we can't allow them to continue to to fly up and or to start a jump, not to fly up.
We don't want to stop them from continuing a jump, just from starting a jump.
So here on line 36, if they pressed fire one and so remember we got to add the double amperand in between the two parentheses and is grounded.
So what that's going to say is if they're grounded on the ground and they've pressed the button, they can start the jump.
Otherwise, this will never return true.
The and means that both statements have to be true.
Let's go jump back into Unity.
I'm going to press play.
Okay.
And now I should only be able to jump if I'm on the ground.
Jump.
Oh, look at that.
I can only jump when I'm on the ground.
I can hold a jump, but I can't uh or I can kind of continue a jump.
So, watch.
If I'm already jumping, I can I can continue it, but I can't start a new jump.
So, I can't get to the top and and keep jumping.
That's looking pretty good.
We've got our raycast working.
We've got our grounding working.
I think it's time for us to go into plastic and commit our changes.
So here we've added a grounding check for our jump to the player.
So added grounding or let's say added is grounded to the player and made the jump check for grounding state.
And then we'll check in.
Now that we can jump, let's give our player something to jump on and stabilize things just a little bit.
Notice that when we jump around, we kind of tip over and fall to the side.
That's something that we can actually control.
First, let's reproduce it.
Let's jump.
Okay, I jump, jump, jump.
And if I fall, I kind of start rolling to the side.
That's actually controlled in the rigid body.
If we expand out our rigid body component, and remember if you don't see this, you can just select your alien over here on the left in the hierarchy and then find your rigid body and expand it out and then expand out the constraints section.
Notice the freeze rotation option.
If I click this now, well, it's not perfect because I'll stay frozen upside down.
That's not really what I want.
But if I stop playing, let that uncheck itself automatically, which happens.
All of your changes that you make while you're playing are going to get undone.
So don't make changes while you're playing and expect them to stay around.
Now that it's not playing though, I can freeze rotation by clicking that box, that little Z there.
Save my scene with Ctrl S.
Get rid of the star.
Press play.
And I should stop tipping over.
Let's see if that's the case.
So, do I tip? Nope.
No more tipping.
Looking good.
So, the tipping is fixed.
What about giving us something to jump onto? Well, let's zoom out a little bit and let's select our ground platform.
We've got this nice giant ground platform that we know we can walk on.
Let's just make another one of them.
We've got a couple ways that we could do that.
We could go down to our project.
We could go find our ground, our grass, and find the grass um where was it? Grass uh mid right here at the bottom.
And I could drag that out into the scene view.
Take it, drag it out, and recreate it.
Or I can go to my grass mid object here and just hit control or command and D.
That's going to duplicate it.
Now I have two of them.
But you can't tell I have two of them because they're stacked on top of each other.
Let's move the selected one right here.
This one that's already got selected automatically.
I'm going to hold control, hit the click the green arrow, and drag it up.
And look at that.
I've got two pieces of ground.
I'm going to drag this up to about here so that it's at 0 0 and zero.
And then I'm going to shrink it down.
It's way too large.
I don't want this thing stretched out nearly that long.
So I'm going to select the sprite renderer and expand it out.
And remember that tiling width that we had set to 20 before.
I'm going to set this one down to three.
Oops.
Let's hit num lock and a three.
So now I've got this nice small block here in the center.
I'm going to save my scene.
press the play button and see if I can jump up onto that platform or not.
Might be a little bit too high.
Let's see.
Can I make it? Oh, not quite.
So, I can't quite make that jump.
So, I've got a couple options.
I can either move that platform down or increase the player's jump height.
Remember, we can modify that jump height by going over here to the player, collapse down some of these other components.
Look at the player component, and just change that jump velocity to six.
So, I jump up six meters or six blocks per second.
And that'll probably cover it so I can just about make that jump.
It's not quite the feeling that I want, though.
So, I'm going to stop playing and instead go grab my block here, my grass mid, and I'll move the Y value down to negative 1.
I got a couple ways I could do that.
Hold control and drag the green down or just type it in here.
I know I want a negative one there.
Bring it down to about the height that I want.
Let's press play one more time.
Make sure that I can jump on it.
Oops.
Let's see.
Can I make that jump? Just barely.
Oh, almost.
The jump is not quite making it.
And I'm getting a little bit stuck on the edge.
Let's see.
I'm going to give myself a tiny little bit more jump power.
So, we'll go up to our jump velocity to maybe a 5.5.
We'll press play one more time.
And this should get me enough power to jump up onto there.
But I still move so slow that it's it's very very difficult to kind of get around.
So let's stop playing and do one final change.
Let's go back to our player.
And when we're moving our player, instead of just going from zero or negative one to one for our speed and our velocity on the horizontal axis, let's give our player some actual speed control.
And in fact, let's give ourselves some speed control in the inspector.
Let's go up and do this a slightly different way than we've done it in the past.
So, scroll to the top and I'm going to go find my jump velocity line right here, line 8.
I'm going to hit control D to duplicate that line or command D if you're on a Mac.
And I'm going to rename this first one up here to um move velocity or let's call this horizontal horizontal velocity.
So, we now have a horizontal velocity of five.
I think I want to change this to about a three for the default though.
I'll copy horizontal velocity by double clicking on it.
Ctrl + C.
And then scroll down to the part where we set our velocity on line 43.
Right now, we set the velocity of our character to the horizontal value, which we've read directly from the inputs, and the vertical value that we've done some actual calculation on.
So all we need to do now is calculate something for our horizontal so that it is modified by our speed variable.
To do that we can just say horizontal times our speed or right here on line 42 and say horizontal star equals and then paste in our horizontal velocity.
Star equals means that it will multiply itself by this value.
So if we do a value star equals another one, it's going to take that value and then multiply itself by the other one.
So if we have a horizontal of one, it's going to multiply by that three and it's going to give us a three.
If we have a negative one, it's going to give us a negative three.
If we have a horizontal of.5, if I'm pushing just halfway on my little controller here, then we're going to get a value of.5 * 3, which is 1.5.
So this is how we can give ourselves some nice speed controls.
Let's save.
jump over to Unity and try them out.
We should now be able to control how fast our player moves left and right, how far they jump or how fast they jump, and how long they jump for.
We'll press play.
Oh, there we go.
We've got our horizontal velocity variable.
Let's hit play and see if it works.
So, now I can see that I'm moving quite a bit faster.
I still get stuck, but that's okay.
That's part of the collision stuff.
We're going to talk about that in a moment.
We can jump around and yep, I can make it up up and probably onto another platform.
I'll stop playing.
I'm going to go select this little small platform, duplicate it one more time, and grab it right here, holding control, and just move one up to right about here.
5.5 and two, and then save again.
And now I should be able to make a double kind of jump across those two.
Go ahead and play around a little bit with placing platforms.
Don't put too many of them down.
Two or three is good.
Um, we're going to talk about a couple more things before we dive into lots of platform placement.
You don't want to put down a whole bunch and spend a lot of time on them because you're going to end up wanting to delete them.
Also, notice that we can kind of jump off the camera right now.
We can disappear and get away relatively easily.
That's something that we'll be addressing soon.
But for now, just play with your variables.
Play with your horizontal velocity.
Try moving it like a six.
Oh, see it starts to get a little bit faster.
I kind of like a a six a little bit more than the three.
But you can play around.
see what you like.
Um, come up with some variables and then reset back to the defaults.
So, let's go to three, five.
Let's put that back at a five.
And the jump duration of 5.5.
I'll just hit the reset button.
And then we'll go into plastic and commit our changes.
Say that we added velocity controls and new platforms.
And checking our changes.
It's time for us to start playing with graphics.
Specifically, we're going to add a jump graphic to our character for when we're jumping so our player can tell when they're jumping and we can debug things a lot easier and figure out what we're doing as well.
I think it's an easy, nice thing to get in.
And it's going to show us quite a few interesting concepts.
The first thing that we want to do is take a look at our sprite renderer.
If I expand out the sprite renderer, it has a few fields on it.
It's got the sprite, a color that allows me to tint it if I want to change the color.
It kind of not the really the way that you want to change the color of your sprite most of the time, but you can modify it there.
You got a flip option that allows us to flip it upside down or left and right, which is something we'll get into shortly.
And then a couple other options like the draw mode for tiling that we've already looked at.
What we want to do though is change the sprite.
So, if we select the sprite by clicking on it, we can see all of our different alien sprites.
I'm going to hold control and use the mouse wheel.
You can also use this slider right here to get a big view of all of our sprites.
And what I want is our jump sprite to appear when we're jumping.
So, let's find our jump sprite.
Click and drag it right in here.
And there we go.
We can see our jump sprite is there.
But if I press play now, we're just going to have our jump sprite on permanently.
And obviously, I can't jump and then click and drag the sprite out there uh at runtime.
That would probably be pretty hard if I was trying to like Oh, here now I'm in climbing.
Oh, now I just took a hit.
I got to drag him out.
So, that's not what we're going to do.
Instead, we're going to stop playing.
We're going to change it back to being the default one, which I believe was named front uh alien blue front.
So, we'll drag that back into the sprite so he's got that default on.
And we're going to write a little bit of code here that can change this sprite dynamically for us.
Let's open up our player script.
And first things first, at the top, we're going to need to get a reference to a sprite.
We're going to need to know what sprite we want to put in.
So, we're going to add another serialized field.
I'm going to do that right here after line 10.
We'll add a serialized field.
In fact, I'll just let that autocomplete for me.
But instead of it being a private float, we're going to add a sprite.
And we're going to call this underscore jump sprite with a semicolon at the end.
And so we have a serialized field sprite jump sprite.
Now notice that we don't have the private keyword here.
That's because this private keyword is redundant and just doesn't need to be here.
I could put it there, but I don't need it.
In fact, because I don't need it, I'm going to delete all three of these other ones.
And that fourth one.
Let's delete the first one by double clicking on it.
Hit delete and delete.
Now for these other three, I can do it a couple different ways, but check out this cool trick.
If you hold down alt, click.
So I've got my cursor here already.
So, let's click the cursor there, then hold down alt, click and drag over the private keywords.
I can block select them, and then just hit delete, and hit delete one more time, and I'm good to go.
Now, make sure that you click away so that everything else you type in the future doesn't go to all three of those lines.
It's a neat little trick, though, to get rid of things or to past things in when you want to kind of batch update.
So, now we have our jump sprite.
Let's save, go back into Unity, see what that looks like, and then figure out how we're going to hook it up and write the code for it in a moment.
So, we'll minimize the code.
Go make sure our alien is selected and our player should show up in the inspector with a new field, the jump sprite option.
Now, we just need to go find our sprite.
And I can click this little circle to pop up every sprite in the game.
That's probably well actually surprisingly it's finding the one that I want right here.
Jump blue.
But if you find that there are too many, you can always just search.
So, I can just search for jump and find my blue jump right here and just double click on it.
Notice there are two of them.
I want the one that matches.
I used the fulls size one.
So, I'm going to use the fulls size one here.
I'm going to pick the one that's 128x 256, not the one that's 135x 191.
I just got to make sure that I'm using the same set of sprites.
So, I'll double click on that one.
Now, I've got my sprite here, and I need to go into the code and make it actually set it or switch it at runtime when we're playing or when we're jumping.
So, to do that, we're going to go back to our player script, and then let's find the spot where we set our grounding.
So is grounded is equal true or is grounded is equal to false.
And we essentially want to set the sprite based on whether or not is ground were grounded or not.
We have a couple ways that we could do this.
The first way that we could do it and the way that we're going to start is by adding some curly braces.
So right after the hit if hit.colider, we're going to add a curly brace on a new line.
And then after the is grounded is true, going to add another curly brace.
So what that's going to do is allow me to write more than one statement after this if.
So the if check before was only running one line of code.
Now it'll run all of the code that's inside of these braces.
Right now that's one line, but let's add another line.
So if they are on the ground, we want to set our sprite to its default sprite value.
So let's say sprite renderer.sprite equals and we need a our default sprite.
We don't have that yet.
So, let's just say underscore default sprite.
We'll add that in a moment.
We'll fix that error up.
Now, let's go down to our else section.
After the word else, we'll add a new line and again a squiggly brace.
Now, I'm going to delete this other closing squiggly brace here because I want to go down two lines and read it.
I just wanted to move that so that the is grounded was inside of the two squiggly braces.
After that is grounded check or is grounded line being set, sorry.
We'll add a new line and we'll say sprite renderer.sprite equals jump sprite.
So, what's this doing? If we're on the ground, it's going to say is grounded is true or set is grounded to be equal to true and set our sprite to the default one, which we haven't figured out yet, but we're going to do that in a moment.
If we're not on the ground, it's going to set us to the jump sprite and set is grounded to false so that we can use that for our jump checks.
All right.
So, how are we going to get our default sprite? Well, first we need to create a field for it.
So, I'll select it and hit alt enter and let it generate a field.
Remember, I can hit F12 to go up here and see my field.
But this field doesn't have a value.
So, if I play right now, my character is going to disappear.
Let's try it out.
Let's save.
Go into Unity and press play.
And look at that.
Our player just totally disappeared.
The other interesting thing to note is that if I try to jump and have my player appear, it doesn't actually show back up.
And the reason for that, if we look at our little gizmo here, is that our sprite renderer no longer has an extent.
It no longer has a bottom.
So it doesn't have a bottom to draw the ground from it and thinks that the ground is at our center.
So we're going to have to make some small changes here.
That's so the first change that we're going to do is get the actual default sprite.
So we're going to stop playing.
We'll go back to our player script and we're going to do something called caching.
We're going to cache this default sprite when our object is created in or awakened or our level has started.
To do that, we're going to add in a new method, a new one of the Unity methods, one of the special ones that we get from the MonoBehavior class.
We're going to add two new lines here right above on gizmos.
And I'm going say void awake.
This is a special method that gets called at the start of the object's life.
So, at the start of our player's life, when this level first loads, this awake method will get called.
And what I want to do in the awake method is get the sprite that's already on our sprite renderer.
So, I'll say default sprite equals.
And now I've got to get my sprite renderer and get the comp get the sprite from it.
So, I'd say get component sprite renderer.sprite.
And this will get the sprite renderer.
Then get the sprite and save that off to this default sprite variable.
Let's save that and see if it works real quick.
Go back into Unity and we should be able to press play and see our sprite changing and our grounding continuing to work.
There we go.
So, we're on the ground.
We jump and it goes to a jump.
And as soon as we hit the ground, we're back to the ground sprite.
So far, I think it's looking pretty good.
But there is something there that you might have thought about or might have noticed, especially if you're experienced in development at all.
And that's that we're getting this sprite renderer component a lot.
And we could probably cache that too in awake.
While we're caching things, if we're going to get a component and it's something that we're going to get often when the update frame is every single frame of our game, so that's pretty often, then we should just cache that component.
So let's do that.
Let's take line 31 and I'm going to copy the entire line here.
Copy.
I'm going to put it up here on line 16 and paste.
I'm going to hit the home key to go to the beginning of the line and then delete out the sprite renderer by holding shift delete.
Oops, no, wrong key.
Sorry, Z.
Control delete.
I hit shift delete is the line.
Control delete is the word.
So, I got rid of that uppercase sprite renderer.
And then I'm going to add a underscore to the beginning of this.
So add shift and the minus to get my underscore.
I'll generate a field for it by hitting alt enter.
It's going to give us a nice field right up at the top right by the sprite.
And then we'll just start using this sprite renderer instead of all these get component sprite renderer calls.
So I'm going to copy sprite renderer onto my clipboard.
We'll take this line right here and this part right here on line 19, the git component call, and paste in the sprite renderer because we don't need to get it anymore.
We'll just use the one that we've already saved off.
And the reason for this, by the way, is that getting components is an expensive, slow thing to do.
Now, we're going to go down to the update method and just get rid of line 33.
And that's going to expose two errors that we've got the sprite renderer referenced now on line 33.
Oh, sorry, three errors and 38 and 43 that don't exist.
And that's because when I recreated this, I renamed it with an underscore.
So, we just need to add the underscore so that we're using that cached sprite renderer.
So, I'll go add the underscore to all three of them and we're good to go.
Now, if you're looking at this thinking, what about this big blaring on draw gizmos one? Why haven't we changed that? Shouldn't we use the sprite renderer? The answer to that is actually no.
And there's a very important special reason for this.
The way that Unity works, it has an object life cycle.
objects are created, they run their methods and then every frame they run another set of methods.
So they run the awake method, the start method, and some other ones.
They run their update, their gizmos, and a whole bunch of other ones.
And then if they're destroyed, they'll run a destroy method.
In fact, after this section, I recommend that you take a look at the Unity execution order documentation.
It's right here.
I'll make sure that it's linked and maybe even go print it out.
But I have a print out of this available for me pretty much at all times.
So I can look at it, see the order things are getting called in and where they are and get an idea of a lot of the methods that I occasionally forget about.
But it's important to know that this ondraw gizmos one doesn't necessarily mean that the awake has been called.
Even though it's after all of these other things, awake and start don't always get called um in edit mode.
It's kind of inconsistent.
Don't expect them to be there.
And it's okay to do that get component call in an ond draw gizmos.
Just expect to regrab everything in the gizmos most of the time.
All right, let's double check that code one more time and then let's go try this out.
Actually, we've got these private keywords here.
Let's go get rid of those two.
two.
two.
Just talked about those.
Do the batch update or the alt and drag to select and then delete them.
And then let's go look at the code one more time.
Here it all is.
It'll all be on the page as well.
But once it looks good, let's jump over to Unity.
Let's make sure we've saved and then try it out.
We should still have the exact same functionality.
We've just switched that sprite renderer over to be cached.
Assuming that we didn't mess anything up, our character should switch between our jump and grounded or idle front states.
So there he is.
He's grounded.
He's in the air.
And let's see if I can get up.
I don't think I can get up to that platform with my value of five.
Oh, there we go.
Going a little bit on my jump.
I made it.
So there we go.
Let's stop playing.
Go back into plastic.
And let's say that we've added a jump icon or jump graphic, not an icon, jump sprite to the player.
And check in.
Now that our player's jump sprit's working, I want to address something with the direction.
And by the way, if your player's jump sprite isn't working, just make sure that you've actually got it assigned, that you've got the right values assigned, and that you're using the correct collider type.
If you used something else, you're going to see weird results up until the point where we get to the actually switching of those things.
So, make sure that your everything matches and there's code always down below to copy if you need to grab that.
So, let's take a look at what we can do for our player to make them jump and face the right way.
Instead of always facing to the right, if I'm going left, I want them to face to the left.
Let's stop playing and we're going to open up our player script again.
And down here in the update, we're going to do something kind of different.
and interesting.
We're going to refactor and create a new method.
I want to have a method here that just deals with the sprite.
Right now, we have this update method, and it's feeling really, really large.
This is probably looking like a lot of code to some people, and to me, this is just a little bit more than I like to have in a method.
So, my update method shouldn't be this long.
I'd like to shrink it down.
So, what we're going to do is add a new method down here at the bottom.
And that method is going to update our sprite.
But we're going to do that by typing in the bottom of our update method.
So right here at the end of line 57, I'm going to hit enter.
And then I'm going to type update sprite open parenthesis close parenthesis and a semicolon.
I'll hit the home key to go to the beginning of the line so that my cursor is right at the beginning of update sprite.
Hit alt enter and hit generate method.
Now this gave me a private void method right below my update method.
So if I collapse my update method, you can see it's right here down below.
And this is just my own method.
This is a method that I've written that's not going to be called by Unity automatically.
It's not like on draw gizmos update and awake that are all special unity messages.
Notice that this says Unity message.
These are actually methods that are called by Unity from a messaging system that it uses.
So update sprite is not.
It's a method that I've created myself.
And right now, by default, all it does is throw an exception, which really just means put an error message into the log.
At least at least for this use case, that's all it means.
It'll drop an error into the log and do pretty much nothing else.
So, we'll break execution of our program.
But that's not really an important part right here based on where it's at.
So, we want to change this.
We don't want it to throw an exception, write an error, or do anything bad.
We'll delete that out.
And we're going to go into the update method.
and instead we're just going to figure out how we can take this sprite renderer stuff and move it into the update sprite.
So what I want is to check to see well first what I want to do is take these lines 39 and 44 out.
So I'm going to take line 39 I'm going to cut it with controll X and then I'm going to paste it down here into line 64.
I'm going to do the same with line 44 cut it with Ctrl X and paste it down here on line 65.
I know I want this stuff to happen here.
Right now, it doesn't make any sense.
It's going to set it to the first sprite and immediately set it to the second sprite.
We'll work on the logic for that in a moment.
The next thing I want to do is get rid of these braces because now I'm only doing one thing.
I'm going to get rid of these extra lines here to make it more obvious and add a space.
But I'm only doing one thing in my if and one thing in the else.
So, I don't need these braces.
They're just making my code a little bit bigger.
In fact, I'm making it quite a bit bigger.
It's making something that could be four lines into eight lines.
So, let's delete it with shift delete.
Go down to the closing brace there.
Shift delete.
Got to make sure that I get the closing brace.
If I have messed up braces, if I just delete one here, it's going to break everything.
Look, my update now thinks that this is the end of the update and my code is all ruined.
But if I shift delete and get rid of that extra extraneous uh closing brace, everything will work better.
All right, so our collider check is now shrunk back down, got rid of the braces, and our update sprite check or our update sprite method is ready to be worked on some more.
So, what do we want to do in here? Well, if we're jumping or if we're grounded, we want to use the default sprite.
So, we can just say if is grounded.
Look at that.
It autocomp completed for us.
And then we'll go down to the next line on line 62 and say else or 61.
So, now we've got that same logic recreated right here in our update sprite.
And this is starting to shrink down.
It's getting a little bit smaller.
We're not having to add more to it.
Let's hit the line 60 and hit the tab here to just indent that.
and hit the tab here to indent that as well.
Now, it's important to note that indentation and spacing doesn't really matter in C.
It's not like uh some other programming languages where it's very important, but it is important for your sanity and for being able to understand and read the code.
So, I want to make sure that my indentation is always pretty good or perfect ideally.
You don't want to have it wild and crazy like this.
And you got this thing over here that's way way harder to read.
And you can hold down control K and then hold down control and hit D and have it automatically format the entire document for you to fix the formatting up.
So if you have a hard time with that, hold control, hit K D while you're still holding control.
It'll fix that all up.
Now our update sprite method works and we've refactored and moved that code out.
But we still haven't adjusted the sprite to face the correct direction.
Now to change the direction, we need to use that flip X property.
Let's go back to Unity and take a real quick look at it.
Remember, we've got the flip X that switches the sprites, and it's kind of uh not showing us much because our front sprite doesn't have a much of a difference, but you can see the dots are switching which side they're on.
Our jump sprite, though, will be totally different.
So, we're going to want to modify that flip X.
Now, let's go down to the bottom of our update sprite.
And here, what we want to do is flip the sprite if they're moving off to the um left.
So if they're moving to the left, that means that the horizontal value is something negative.
Remember zero is if we're not touching it at all.
To the left is negative point whatever to negative one.
And to the right is positive all the way up to positive one.
So we want to check to see if the input is going negative.
And if so, we want to flip the sprite.
Otherwise, we want to maybe if the input's positive, we want to make sure that it's set to the right.
So how are we going to do that? Well, we could reread this input here, this axis stuff, or we could just kind of hold on to it, which I think is probably a better idea.
We just store this horizontal as a variable instead of trying to read it again.
So, to do that, we're going to delete this var keyword in front of horizontal and we're going to turn this into a field.
So, I'll hit alt enter and we'll hit generate field.
That's going to give us a field up top.
We'll hit F12.
And remember that in the way that I like to make my fields, I like to add an underscore to the front of it.
And this one doesn't have an underscore.
So I'm actually going to use a hotkey here.
Control-r, which just the same key twice.
Hit control R twice.
So control and hit R two times.
It'll bring up the rename.
F2 might be your hotkey as well.
Or you can right click and find the rename if it's something different.
But I'm in the rename mode.
I'm going to hit home and go add an underscore right to the beginning of it.
If I hit enter now, it's going to rename all instances of that horizontal that were down here that didn't have an underscore to have an underscore.
If that didn't work for you, you can always go through and manually do that.
Just adjust each one.
Now, what are we doing? We're setting the horizontal value right here.
We're logging it out and then we're using it here in the um in our velocity setting.
Now, this horizontal is going to have our speed calculation in there.
And that's totally fine with me.
It doesn't matter.
We just want to check if it's greater than zero or less than zero.
So, we're going to go down to our update sprite method and add our if statement.
We'll say if and we want to check horizontal.
If it's greater than zero, so if we're pushing to the right, then our sprite render, let's go to a new line.
Sprite renderer.flip x should be equal to false.
We don't want it to be flipped.
If we're pushing to the right, now the alternative is that we're pushing to the left.
So, we'll say else, but we don't want to just say else.
If we want to say else if horizontal is less than zero then sprite renderer.flip x is equal to true.
Look at that.
It autocomp completed for me.
Now why can't we just say else? The reason for that is if we let go and we're not pushing anything.
Horizontal would be zero.
And we don't want to have a default direction.
It would if we did that with just the else, it would just instantly flip to the left as soon as we weren't pushing any direction.
That's not the behavior we want.
We want to face the last direction that I was pressing.
So let's save with control S.
Get rid of the little star there.
We'll take a look at the entire script one more time.
So there it is.
We've got everything here.
We've got our update sprite method.
Update sprites being called right here at the end of the update method.
And we'll go back into Unity and try it out.
So now when I jump, we should be able to see that I'm jumping to the left or to the right at least slightly more visually than we were able to before.
And this is going to work for our moving and all of our other sprites that come along after this.
So once we start running.
So there we go.
I can go left and right.
Look at that.
It's looking pretty good.
So let's stop playing.
Go back into plastic.
Make sure that we've saved our scene and say that we've added um jump or let's say added sprite directions.
Added sprite direction based on movement inputs.
and we'll check in our change.
Now, we're going to talk about animation in Unity.
Our current setup requires us to swap out the sprite based on what's happening.
And while that works fine for a single sprite swap like we've got here, having it to do it for running and climbing and swimming and all kinds of things wouldn't really be feasible.
In fact, having to do it just for walking alone would mean that we'd have to constantly switch out the sprite every frame or every couple frames at whatever speed we wanted.
There's an easier way to do that and there's a built-in system for doing it using the animation system.
So, I'm going to stop playing and we're going to create some new animations for our character.
To do that, I'm going to rightclick on my assets folder.
So, first down in my project view, go to the assets root folder.
I'm going to rightclick and I'm going to create a new folder.
And I'm going to call this animation.
This is just where I want to store my animations.
I'm going to now go over to the animation window.
So go to window and look for animation and animation or you can hit control 6 or command 6 is probably your hotkey for it.
So you hit that button and you'll get a new animation window.
It's going to look like this and not be super useful by default.
That's okay.
We're going to take it.
We're going to drag it down here and dock it onto the bottom of our animations or our bottom of our our bottom window.
So, it's locked in with our game view, the plastic window, the console, and the project.
Now, I'm going to go select my alien.
And notice that this create button appeared because it knows that, hey, there's some stuff on here.
I could create an animation for this.
Before I create an animation for my player, though, I'm going to rename him.
So, instead of having this be Alien Blue Front and having a bunch of animations that are named after Alien Blue Front, I'm going to rename him to player.
So, hit the click the left click on him and type in player.
Or again, you can go up here into the inspector and just type in player.
Then, we'll hit the create button down here with him selected.
And we're going to get some new animations for our player.
We'll go to the animation folder to save it in.
And the first one is going to just be a walk animation.
So, I'll just replace the text down here with walk with a capital W.
In fact, I'm going to put player walk so that I've got a nice player specific animation name.
I've got my player walk animation.
And look at this.
I've now got this weird little timeline with nothing in it that does nothing when I drag.
What I want to animate is the sprite renderers sprite.
So to do that, I've got a couple different options.
I can either go in here, hit record, and then change out the sprite partway through, or I can take the shortcut, which is to take it the sprite files from our project view.
So, if I go select my sprite, let's go to the project view first.
I go to project view, click on my sprite renderer, the sprite right here, to go select it and find it.
And I can see I've got my walk one and walk two.
I'm going to turn this into a list view.
I've got my walk one and walk two.
And then I'm going to put this side by side with the animation window.
So, to do that, I'll just take my animation window, drag it right over here.
So, it's kind of side by side.
And I'm going to take walk one, click on it.
Take walk two, hold shift and click so that they're both selected.
And then I'm going to drag them right over here to the right onto the animation window.
And then we'll hit sprite renderer.
And that's going to create an animation for the sprite renderer.
Now, if you're wondering why it had a popup there to say player, that's actually something kind of new.
And it'll allow me to animate the jump sprite of the player.
It was looking for a sprite that it could animate, and it saw that, too.
So, it gave us two options, but what we wanted to choose was sprite renderer, which is what I did.
And you can see now the sprite has changed to alien blue walk one.
Let's zoom in a little bit by holding the control key.
Oh, and zoom in.
And zooming just a little bit with the mouse wheel.
You can see I've got this two frame animation.
It's not very useful.
If I click here, I can drag back and forth between the two frames.
And I can hit the play button and watch them go very, very fast.
That's way too fast of an animation, though.
So, I'm going to zoom out here and look at this timeline.
When I get to the 1 col 0 0, that's 1 second.
So, if I take the second dot here, just drag it out.
Let's see if I can get it.
Oh, Z.
Let's take the line here and drag it out to 1 second.
Now, it's going to switch frames once per second.
But notice that at the end of the frame, it goes right back to the first walk state.
So, let's let's stop playing.
Drag this out.
See, right here, it's on walk one.
When it gets over to here, it goes to walk two, and then it instantly bounces back to walk one.
So, I want to make it go through all of these.
I want it to go to this one, then to this one, and stay on this one for a little while before it switches back.
So, I'll drag this over to about the 02 area.
Then, I'll select this first pixel right here, this first little dot.
Go select it and hit Ctrl + C.
Go over to the 04 area and hit Ctrl +V.
That's going to give me another key frame that's of walk one.
So, notice this one selected.
It's on walk one.
If I go over to here, it's on walk two.
It goes walk one, walk two.
And if I hit play now, I've got an animation that switches between the two.
If I want to speed this animation up, I select all of these key frames, grab this little line right here at the end to just scale it down.
Now, it's a faster walk at half the speed or or half the time and double the speed.
It's a little bit less than half.
I think I went over a tiny bit further than intended.
There we go.
So, now I've got my walk animation on here.
Let's press play and see what this looks like in game.
I should expect to see my character walking and animating pretty much all the time.
There we go.
He's animating.
He's walking.
I run back and forth.
And now when I jump, look at that.
My sprite is no longer in a jump sprite.
It's being overridden by this animation system.
So, we're going to have to do something with that.
But so far, it's kind of good, right? Like, we're walking.
We're getting the sprite kind of showing.
I think that this is probably too fast for us.
It's not really the speed that I want to be at.
I think I want to scale that back up.
So, let's zoom out.
I've got the character selected.
Go select the player.
Go to the animation.
If you don't see the animation, make sure you select it right there.
Zoom out with the mouse wheel and drag this out to about that point four.
Let's see.
We walk.
Now, that's kind of closer.
Let's go to the three right there.
Yeah, that looks that's probably about where I want it for now.
So, now that I've got it at a level that I think I like, I'll stop playing and let's examine what's happening here.
How is this all working? How is this animation playing? And why is it taking over? The animation is playing automatically because of this animator component that was added to the player.
When we added the animation and created it on here, it automatically added this animator component.
It created this player animation controller and it assigned the player walk animation to it.
If I double click on this controller, it pops up the animator window.
And this is where some people tend to get confused in Unity with animations and the animator.
Really, what's going on is the animations are individual animations.
So, think of like a jump movement or a running movement or a shooting movement.
Those are the individual movements.
The animator is the thing that ties them together and controls which one is playing at any specific time.
The animator here is just playing this play or walk animation.
I can zoom out on the animator and zoom in with my mouse wheel.
I can use the left mouse to pan around and I can click and drag to move things around and select them.
Right here you can see that on entry.
So, when this animation or animator starts up, the first thing it does is go right into the player walk animation, and then that thing just sits there and plays over and over and over.
It never switches out of the player walk state.
So, we're going to have to figure out a way to modify the state, change it, and switch between different animations, whether it's an idle animation, a climbing, a running, a swimming, a jumping, or anything else.
But for now, we need to know that this is here, and this is what's starting it.
So, let's save, go into plastic, commit our animation and our new animator controller, and then start to think about what we can do to tie into this animation system to make our player a little bit cooler.
So, we'll go to the plastic SCM folder, make sure that we've saved that we added walk animation to the player and commit or check in.
Now that we have access to this animator and its cool system, let's see what it can do and see if it can maybe handle our jumping and some other things for us.
So, we're going to go back to the animator window.
If you don't remember how to find that, just go select your player, find the animator, and then go double click on the controller.
That'll bring up the animator window, which allows us to modify an animator controller.
And what we want to do is add a jump animation into this canvas and a way to switch back and forth between it.
Now, if we go look at our jump, let's go select the player and then click on the sprite so that our project view shows us all of our sprites.
There's only one sprite for jump.
So, it's not much of an animation, but we could theoretically have a player that's a 3D character or a 2D character with better animations that has some jumping going on or better animations, but actually like moving jumping animations.
We're not going to have one for this character, but we're going to create an animation anyway.
To do that, we're going to select our character with our animation window open here.
We're going to click the drop down here that says player walk and choose create new clip.
We want to create a jump animation and I want to do that in my jump folder.
So, I'll go up to the assets folder.
Oops, I can click right and then go to my animation folder and I'm going to call this player jump.
Now, in this player jump, we're going to add a single frame.
That's going to be my alien blue jump.
I'll click and drag that over to my animator right at the beginning and choose sprite renderer.
And now I've got an animation that just plays a single frame.
You haven't seen it yet, but we're going to see it in action in just a moment.
Also notice up here in the animator controller, we have a player jump option.
This has appeared automatically as soon as we created the animation because it knows that this is an animation for our character.
I'm going to click on it and drag it so that it's directly below the player walk just so that it's nicely lined up.
position doesn't really matter, but having it nice and clean, I think, is important.
And then we're going to go over to this layers and parameters section, and we're going to click on parameters, and we're going to add in a new parameter.
What we want to do is switch between these states depending on whether or not our player is grounded, just like we were doing in our code, but we're going to do it in the animator instead.
We'll click on the plus and choose that we want a boolean parameter or a bool, and we'll name it is grounded.
exactly the same way that we did in code with a capital I and a capital G, no spaces.
So, we've got an is grounded parameter and then we're going to want to use that parameter to switch back and forth between these two states.
So, to do that, we'll go to the player walk.
We're going to right click on it and hit make transition.
That's going to give us an arrow that we can drag around and snap onto anything here.
Well, really the only options are exit and player jump that we could snap to, but if we had more things, we could snap to them.
We're going to go to player jump and click.
We'll get a nice line going straight down to play or jump.
Then we're going to click on that.
This is called a transition and it transitions between one trans one one animation to another.
So we're going to click on it and we're going to add a condition here.
If I hit the preview here, you kind of see it.
It doesn't really show very well, but you can kind of see what it's doing.
It goes into this animation for this part of the transition.
It tries to kind of blur them.
So we don't want that blur really happening.
We want it to be instant.
So we're going to uncheck has exit time.
And then we're going to check the condition because we only want this to happen when is grounded is well not true but when it's false.
So we'll click the false.
Click the dropown and choose false.
So when we're not grounded we'll go into the player jump animation.
Now we also want to be able to go back into the walk animation when we are grounded.
So we're going to go to the player jump animation right here.
Right click, hit make transition, drag this arrow, and of course you probably guessed put it right onto the player walk.
Then we'll click on the transition for going up to player walk.
This not not this one but this one over here to the right.
And we're going to add a condition for this as well.
Is grounded is equal to true.
It kind of default got it because that was our only option.
Also uncheck the has exit time.
If you don't do that, you're going to see a delay between your animations.
It's going to feel weird and laggy like it's not working.
All right, we'll save.
Go into our code now and start hooking this up.
So, well, actually, before we go into our code, let's take our animator and let's drag it down here next to the animation window so that we can see it.
And I'll use the right mouse or middle mouse button to pan this around.
And then let's press the play button.
Let's just kind of manually control this for a moment before we tell Code to do something with it.
So, we'll play and we should be able to if our player is selected see this animation kind of in progress or see the animator and get a kind of a preview of what it's doing.
So, you can see it's playing the player jump animation constantly.
If I jump, then it's not switching.
So, what's going on here? The transition out isn't working.
Why is the transition out of player jump not working? Oh, because it's ground.
It's never changing.
Ah, so that was the problem.
I I forgot this is exactly what we're looking at.
So is grounded changing will switch between our two different animations either constantly in player jump or in player walk if they're grounded.
So how are we going to set this from code? Well, let's go back over to our player script.
So select the player, open up the script, and in our update sprite, instead of changing the sprite between our default sprite and our jump sprite, let's delete that code.
We'll take lines 60 through line 63.
Hit delete and we'll say get component and we'll get our animator and we're going to set a parameter on it, a boolean parameter specifically.
So we'll do set bool and we need our open parenthesis.
Then we have to give it the name of the boolean which is is grounded capital I and capital G.
And then we got to go to the end of that quotation mark, add a comma, and pass in the value which is either going to be true or false, which is our is grounded.
Now that alone with the semicolon at the end will control passing in that is grounded state to check or to match whatever our game state is or our player state is and have our animation update.
Let's go try it out.
So I've saved, got rid of the star.
We'll jump back in.
We're going to leave the animator window showing here and the game window over here on the left.
And then when we jump, you should see that is grounded becomes unchecked.
It switches animations and when we land, it switches back.
Let's try that out.
Looking good.
So, we've got two animation types.
We're going from jump to walk.
And so far, I think this is looking pretty pretty nice.
All right, let's stop playing and let's add in one more state.
Let's say we want to have an idle state where we're not moving at all.
We're going to go to our animation in our project view again.
We're going to create one more animation.
So, first I'll go find our idle sprite, which is the alien blue front, and go to project view.
Click on this sprite right here.
So, it gets selected.
And then we'll go create a new animation.
So, honor animation again with the player selected.
Hit create new clip.
We'll choose player idle as the name.
And I want to make sure that I put this into my animations folder as well.
And save.
So, we've got a player idle animation.
We'll take the idle sprite or the front sprite.
Where is that at? And drag it right out onto here.
So, we have a single instance or a single sprite animation.
Drop that to sprite renderer.
Then, we'll go back to our animator controller.
And look at that.
We've got the player idle option.
I'm going to take this and drag it up.
Um, let's say right over to the let's let's go over here to the left.
just to the left of player jump and player walk.
And what I want to do now is make a transition between player walk and player idle based on how fast my player is moving or whether or not my player is moving.
So, we're going to need another parameter like a is moving or a speed.
What I'd like to add is a horizontal speed.
So, let's add a new float.
So, we'll hit plus and call this horizontal speed or horizontal velocity.
We could call it either one, but we need to be consistent with it.
I'm going to call it horizontal speed.
We're going to make a transition from player walk.
Right click, make transition down to player idle.
And then we'll make a condition on that.
So, select that transition here.
And we'll add a condition that the speed is greater than or less, sorry, less than 0.1.
So, if it's less than 0.1, then we're probably not moving.
We're going to stop.
If we get that value greater than 0.1 or greater than zero though, I want to move back into walking.
So, we're going to add another transition from idle or right click, hit make transition, go back to player walk, click on that transition, and add the condition that the horizontal speed is greater than zero.
So, just choose horizontal speed and greater than zero is the default.
I'm going to uncheck has exit time on both of these transitions.
I don't want any blending happening.
and then we'll save our scene off.
The last thing we need to do is modify this horizontal speed from code.
Now, if you remember what our code looks like, this should seem relatively simple, but let's go take a look and maybe we'll have this be a little challenge.
So, in our update sprite method, what should we do to keep that speed or get that speed into here? I want you to think about it for a moment.
See if you can figure it out and then go ahead and write the code.
If you can't figure it out, don't worry.
I'm going to show you in just a second.
So, go ahead and see if you can figure that out.
out.
out.
And let's go through the results.
So, it's actually relatively simple.
What we need to do is set a float on the animator.
I'm going to take line 60.
I'm going to duplicate it with command or control D.
We're going to change set bool to set float.
We'll change the variable name to horizontal speed.
And we'll change the value that we pass in to be r underscore horizontal.
This should work alone.
Now, we might want to cache our animator.
We probably should.
We'll talk about that in a little bit, but for now, this is good enough.
And this should work.
It should update our animator.
Let's go try it out.
Jump back into Unity.
I expect now that when we're not moving, we stand still.
And when we are moving, we start to play our walk animation.
Let's check.
So, there we are.
When we're not moving, we don't play an animation.
We're moving.
We play an animation.
Oh, but only when we're moving to the right.
So, if we move to the left, it doesn't work.
Look at that.
So, how are we going to fix this? Well, there's one thing that we can do.
And well, first, let's talk about why this is happening.
Look at that horizontal speed variable.
It's -3.G3 is less than 0.1.
So, it's probably not going to work.
Now, there are a couple ways that we could change this.
We could go in here and modify the um the condition.
We could add in a way to maybe add in some condition.
Well, we really can't even add in a condition.
Say like it's greater than three and less than zero or something weird.
But really what we want to do is just have it be not negative in here so that we never get a negative value.
We always get the positive representation of that or the absolute value of our number which is just the number without the negative sign.
So to do that, we can make a one simple simple code change.
We'll go back to our player script and right here where we pass in the horizontal, we'll pass in math.ABS and then add in an open parenthesis and then add a closing parenthesis at the end of the horizontal.
So what this is going to do is give us the absolute value of the horizontal and pass that in.
It's essentially saying if there's a minus in front of it, remove the minus and just use that value to pass in.
That's all the absolute value is really doing.
So, math.ABS or math.absolute is what it's doing.
All right, let's jump back into Unity.
We should now be able to see our animation working.
If we go left, right, jump, or well, just about anything else.
Let's see.
So, we play, we go to the left, we're animating.
We go to the right, we're animating.
And if we jump, let's see.
There we go.
But we're animating as well.
Now, one issue that we have is that we don't go from idle into jump.
Notice this.
If we're not moving, we're not walking, we don't make a transition from the idle state into the jump state.
And that's because we only have transitions from walk into jump.
So, we're going to need to add in transitions from idle into jump as well.
So, we'll right click on idle, hit make a transition over to jump, and we want to select this condition.
And notice that it's going through them automatically because we don't have a condition anymore.
We want to add a condition here that is grounded is equal to false.
And then we want to make a transition back out of here into player idle and set the condition that is grounded is equal to true and horizontal speed is less than 0.1.
So we only want to go back to idle if we're not moving.
So let's try that out.
Now I can jump.
I can walk.
And I can jump and walk.
And it's for the most part looking pretty good.
There's one little issue when I switch states where the speed I think gets a little bit weird that I don't like.
But we'll talk about how we're going to address that in a moment where you kind of get that like quick face to the front for a quarter or tenth of a second or so.
But this is looking good.
And notice that we were able to modify our animator when we were playing.
I to show that specifically because the animator is not in our scene.
The animator is part of the project.
If I go down here and select the controller, it's actually this asset down here that we've modified.
And while you can't modify scene assets or scene placed things at runtime and have that stay, you can do that with project level things, which can be confusing and sometimes cause problems because sometimes people think that it's not going to save because it's a on something they got to through the scene view and pulled up, but it's actually a project level thing.
So, the animator changes did save even though we did them while we were playing.
So, let's go back into plastic SCM and say that we've added animator controls for uh walking walking idle.
Yeah.
Well, it's really jump and idle and check in.
Oh, and if you get this error, just like I said before, just hit check in again.
It happens.
It pops up every now and then.
Now, we're going to do some modification to our animator.
Let's drag the animator up and make it a little bit bigger.
I want to show you some more of the power that we have here.
Right now, we're doing some animation transitions between our walk and jump and our idle and our walk and our idle.
And it's a little bit confusing.
I feel like when you start to build up these animators, it can be very easy to just get confused and make things that don't make a lot of sense.
And that's exactly what happens here relatively quick.
So, what we're going to do now is delete out our player idol.
So, we're going to select the player idle and delete it completely.
Get rid of all of those transitions that we just created.
Don't worry, we're going to do something even cooler.
Now, we're going to go into our player walk.
We're going to rightclick on it and hit create new blend tree and state.
This is going to allow us to create something that will blend between or mix between different animations based on a variable.
Kind of like our transitions here, but a little bit different.
Now, it might look like nothing has happened, but if I click on this and double click it, you'll see that we now have this weird blend tree thing.
It doesn't make any sense.
If I click on it, it doesn't do anything.
Just has a slider here.
It's a little bit confusing, but what we need to do is click the blend tree and add some motions to it.
We're going to hit plus, add a motion field, and plus and add another motion field.
We're going to add our two animations, our walking animation and our idle animation.
To do that, we'll hit the little search box here and find player idle for the first one.
And then hit the search button again and find our player walk for the second one.
Now, what this will do is it's going to blend between the two animations based on what our horizontal value is.
So, if our horizontal is greater than zero, it's going to go to that one.
If it's lower than zero, it's going to go to the other one.
What does this mean for us? It means that we don't need to have all of those confusing transitions out here.
We just need to have this one player walk with a blend tree in it that will blend between our player locomotion stuff and our jump.
And that also means that I want to select this node right here in our animator controller.
And I want to rename it.
Instead of player walk, I'm going to call this player motion.
This is going to be the one that handles idle and walk.
So that's what I'll give it a more generic name.
And then we've got our jump down here that we transition into out of there.
We don't have so many states.
Let's hit play and try that out.
We should see the exact same behavior.
See? So, I run, I stop, and I run, and I stop.
And if I run and I do the switch back and forth now, though, notice that we don't get that weird mixed up frame in the middle.
And our animator controller is drastically simpler.
I can still jump while I'm running.
I can still jump while I'm standing still.
And the correct animation is applied when I land.
either the idle animation if I'm not moving or the running animation if I am moving.
So things are looking quite a bit better.
There's another change I'd like to make though to our player code.
Let's go into the player script and let's take a look at this area where we do our update sprite.
I mentioned in the last section that we could cache that animator and that's what I'd like to do, but I'd like to present that again as a small little challenge.
See if you can figure out how to cache that animator.
Go ahead and try it on your own.
pause the video and then resume on and I'll show you the steps in case you got lost or had any questions.
All right, let's go through it.
So, to finish our animator or to cache our animator, we need to take this get component animator call and we're just going to cut it.
So, I'm going to hit crl x.
Select that, hit crl x.
We're going to add in the word underscorean animator and then hit escape and then I'm going to hit alt enter and we're going to generate well it wants me to generate a field or a readon field.
We want to go with a generate field.
So we're going to create a new field and it's not going to know the type.
So this is where things get weird, right? Let's hit F12.
Make sure that you're on the word animator and go up to the top.
And here you'll see that we have a private object animator.
What this is is well a little bit confusing.
What's actually happened is the code editor didn't know what type of object we want to create.
We were getting an animator before, but I deleted that code before I put this variable in here.
and it doesn't know that just because it's called animator there's a thing that matches that.
So it just uses the most generic object type that it can.
And in C that's object which actually means that everything in C is an object.
Um it's not a specific type of thing though.
So it's not very useful.
We need to give it the type over here.
We need to replace object with what we want which is our animator.
So we'll just replace that with animator with a capital A.
And now we have our animator reference that we can use down here.
But we haven't saved it off yet.
So we need to save off our animator.
And we're going to do that in the awake.
So in awake where we get our sprite renderer, we'll just add a new line above it.
Say, "Oh, look at that.
It already knows what I want.
Underscorean animator equals get component animator." Got to love the AI that's coming in the code editors.
Now it's making things quite a bit easier.
It already is predicting exactly what I'm going to type in there.
Now I also want to get rid of my private keywords up here because I don't need them.
So, I'll go select them, double click them, hit delete, and delete to get rid of that extra space.
I'll do the same for the one on awake.
Now, we've got our animator cached, and we're using it down here in the update sprite, but you might have noticed that we're not using it on the second line in update sprite on line 63.
So, I'm going to copy it, replace the get animator part all the way up to the end of the parenthesis, and paste with ctrl +v.
Save with control s.
Remember, control shiftb will do a build, and it will show me any errors.
It will highlight anything that's errored or causing a problem.
We don't have anything like that yet.
So, let's jump into Unity and see if it still works.
Should still work.
Ideally, when we make these changes, we haven't broken anything.
That's why we want to test it, though, just to make sure because if you add an extra brace, typo, a name, or something else, it's very easy to make a small error that breaks stuff.
So, we got to test relatively regularly.
All right, we jump.
Looks good.
I can run around, run back and forth.
Everything is looking yep, exactly as I expect.
Let's stop playing, go into our plastic SCM, and say that we modified our animator and cached the modified and cached our animator.
Maybe cleaned up and cached our animator.
Make sure our scene saved.
It is saved.
Yep.
And oh, need to go into file and save project.
We've got to up.
If we don't save project, this is a very important part.
If we don't save our project, our animator player or our player controller won't get updated.
The project level files, the stuff down here doesn't get saved when we hit file save.
That just saves our local scene.
We have to go to save project to save all of the changes to our project and have this update.
Now, there are other times where that just kind of happens automatically, but before we commit, we want to make sure that we do a save project.
So, we've cleaned up our animator controller with a blend tree or a blend state and cached animator in the player and then we'll check in our changes.
In this section, we're going to dive deeper into the Unity physics system.
We're going to take a look at some interesting bugs that you may have already noticed and make it so that our character's jump and movement feels nice and fluid.
The first thing that I want to show you is an issue that you might have run into where your character can kind of hang from one of these platforms.
You can see it represented right here.
I can't actually jump.
I'm just kind of stuck hanging from that platform.
And if I go to the scene view, you can kind of see what's going on here.
If you look at our character, he's got this little green collider showing up and it's landing on top of this box right here.
Let me turn off the sprite renderers for both of those so you can see it better.
Here's our player and you can see that he is just barely touching right here on this little line.
It's not actually touching, but the physics system is counting it as close enough and counting it as a touch.
So, that's causing a big problem for me because our player doesn't really slide off of there.
And our player can't jump because this center line here isn't in the ground.
Let's turn those sprite renderers back on.
You can see it a little bit better.
And now go back over to my game view.
And if I try to jump, remember, nothing happens.
I can still kind of move off to the the right and fall down a little bit, but I don't like the way that that feels.
And I don't like that I can easily get stuck on there.
So, we're going to make a couple of minor changes to fix this.
The first thing that I want to do is go to the scene view.
Double click on the player to select them.
And we're going to replace this polygon collider.
The polygon collider will match up exactly with your sprite so that it lines up and outlines your exact sprite and gives you a very perfect collider, but that's not usually what we use with a player.
Most of the time with a player, we want to use something a little bit smoother that moves quite a bit more fluidly.
And in our case, in this specific scenario, we're going to want to go with a capsule collider 2D.
So, I'm going to hit add component with the player selected, go to physics 2D, and choose a capsule collider 2D.
By default, this is going to be way too large because of the sprite that I'm using.
If I go select my sprite here and go click on it, remember that it's a fulls size sprite.
It's going all the way up to there.
There's lots of extra transparent edge, so it's not properly calculating that top part of the sprite.
We can modify that, though.
And you need to do this almost every time you set up a collider anyway.
We can do that by going to our colliders properties.
Let's collapse everything else.
Find the capsule collider and look right here at the size value.
The size right now is a two.
If I change this to a one, you see it goes to about half the size.
And I think the value I want is more like a 1.2.
A 1.2 there.
Grab the Y and just drag it down so that it lines up.
And I think that the correct value here is going to be a0.4.
This gives me a nice capsule where the very bottom of it lines up exactly with my feet and it's going to be good for nice fluid movement.
Now, if I just save like this though and go back and play, we're going to run into an issue.
Let's save and see what that issue is.
So, I save.
I press play.
Remember, we moved removed the polygon collider, added that capsule collider.
No other changes yet.
Now, I can run around still.
Looks good.
Okay, let's jump up on a platform.
Okay, that looks good.
And it feels kind of smooth.
and I can kind of fall down off the edge there.
But watch what happens if I try to jump multiple times.
I keep jumping in the air like that.
I've got unlimited jumps.
Now, the reason for this, if we go look at our player, is that that grounded variable that is grounded is always true.
And the reason that that is grounded is always true is well, let's let's jump and watch this.
I'm going to jump and then click pause while I'm falling.
Go over to my scene view, double click on the player, and just take a quick peek at them.
So, what's actually happening, and I just wanted that so that I could see the player kind of up in the air, not actually on the ground.
What's actually happening here is that this ray is technically intersecting this circle or this collider because it lines up exactly with the collider.
So, we have a couple of options.
We could um maybe move the collider up a little bit so that the ray isn't there.
Maybe go to like a 39 and then the ray is right below it.
But that's not really the best option.
The other option that the one that I think we should use is to add a layer mask.
And we're going to dive into how to use layers in Unity and how you can use a layer mask to make it so that this collision check right here, this grounding check ignores a player.
To do that, we're going to need to stop playing.
We're going to go to the player and then we'll go to the layer section in the inspector.
By default, you should have a default layer, transparent effects, ignore raycast, water, and UI.
These haven't really changed the defaults, but we need to add in our own layer.
And to do that, we're going to hit the add layer button.
This will bring up the tags and layers inspector, which allows us to create up to, well, 31 layers, not counting the couple built-in ones.
I'm going to use layer 6, and we're going to name this player with a capital P.
This is going to be a layer for our players.
And we're going to talk a lot about layers in a little bit, but you're going to see how these work.
For now, just remember that we need to create a player one and then go rightclick on the player because look, his layer is still set to default.
When you create a new layer, it doesn't automatically assign that layer.
So, you need to go click the character and then reassign the layer.
This happens every time you make a new layer.
Remember that it doesn't actually assign that one because brings up that menu and then you have to pick which one you're modifying.
Okay, so we've added our player layer to the player.
And if I save now and just press play, nothing is going to be different.
All I've really done is tell the physics system, hey, this player, um, treat them separate se separately if I tell you to, or just know that it's on a specific layer.
So, if I want to avoid collisions with things with my player, or I want to just check specific things, I can ignore that player or only check against players.
Let's dive into the actual code, though, because I think it'll make a lot more sense once we put the code together.
So to write our code, we're going to open up the player script and we're going to add a new serialized field here.
Right after our jump sprite, we're going to add a serialized field and it's going to be a layer mask.
That's a capital L and a capital M and we'll name it underscore layer mask.
So we've got a layer mask here named underscore layer mask.
Now we're going to take this layer mask.
I'm going to copy the underscore layer mask.
And in the part where we do our ray casting right here on line 39, we assign a hit or we get back the first thing that that little ray is hitting.
Remember we have the red visualization of the ray.
What we can do here is go to the end of our raycast call.
So after the one f and right before that parenthesis and we can actually add in another comma.
And the reason for this is that our raycast has eight different overloads.
Um, we're only seeing, and when I say eight different overloads, it's eight different ways that this thing can be called.
And I wish it wasn't cut off right there.
But if you hit the arrow right here, you can actually bounce through all of the different ways that it can be called.
And the reason that it can be called different ways is sometimes you want to pass in different parameters.
You want to have different special conditions or um sometimes you want to get back out multiple results.
You want the array to go through multiple things and give you all of those back.
But the one that we're going to use, I hit the comma and add a space, is that we can add a layer mask as the fourth parameter.
So I do underscore layer mask.
And what this is going to do is make it so that our raycast will now only work against the layers that we have selected in this layer mask.
Let's go take a look at what that looks like in the inspector, though.
It'll probably make a whole lot more sense.
Minimize.
Go select our player.
And in the player script, we should get a nice layer mask for our jump or for Yeah, there we go.
Layer mask.
And we'll choose everything except for player.
So, I'm going to choose everything.
And then uncheck player.
Press play.
And this should resolve our jumping problem.
So now our ray is no longer going to look at the player.
There we go.
I can't jump multiple times.
I can jump once, but no more jumps after that.
So, it is working.
Our array is checking properly.
If I look at the player here and I watch the is grounded variable, you see that it's changing properly.
If I change this mask back to player though at runtime, watch.
I stay grounded forever.
So, now I can jump indefinitely.
Luckily, if I stop playing because I changed that at runtime, it'll go away and reset back to the correct value.
So, let's save this off and do a quick commit because we've added a new layer, added the player layer.
We've assigned the player to it, and we've swapped out the capsule collider or the polygon collider with a capsule collider.
So, say swapped polygon collider with capsule collider.
And the final change that we did was add a layer mask check to the player.
Added layer mask check to player.
And I'm going to split these all into new lines in my commit.
So I've got three lines of messages for my check-in and hit the check-in button.
Now we're going to take a look at another jump issue, which is that we can get kind of stuck on these ledges and still not be able to jump.
And if we go look at our player again, let's go to the scene view.
Double click on the player.
Remember that our ray cast is happening from the center of our body.
This little red imaginary line that we shoot down to see if we're on the ground.
And since we're not hitting the ground here, our center of our body is kind of hanging off.
Our character is not marked as grounded.
So, they can't jump.
We can't even click it to do it because it'll get set to false.
So, what we need to do is modify our code a little bit.
Instead of just checking at the center point, we want to check underneath each of the feet.
And we'll do that in addition to checking in the center point just so that if we ever end up on a little tiny ledge where both of our feet are off the edge but the center's on, we can still jump.
So we want to keep doing this raycast at the center but add some additional ones to each of these feet.
And before I do that, I want to do the visualization for it.
I want to make sure that I can see what I'm doing, see where that's going to be, and that it all kind of makes sense.
It makes it a lot easier for me to track down things, debug it, and understand what I'm what I'm writing and how it's working.
So, let's open up the player script and in our ond draw gizmos, let's make some minor modifications.
The first thing I want to do is take line 31 and just move it up.
So, I'm going to actually select that entire line.
So, I go to the end of it and I hold shift, hit the home key on my keyboard, and still holding shift I just hit delete.
Go up, enter, up, enter, controlV to paste.
Or if you're using the correct editor, if you're using Jet Brains Writer, you can actually select a line, do control altshift, and just do the up arrow and down arrow.
You can't do that in here.
Although, there may be a way to rebind hotkeys and make that possible.
Let's save though.
I've moved that line up.
And let's talk about what I want to do next.
So, line 31 and 33, let's add a little spacing here.
Line 32 and 33 are responsible for determining where the line starts and ends.
and that or or really determining where the line starts and then line 33 does the drawing and determines where it ends.
So I want to just have it start in three places instead of doing one line in the center.
I do one line in the center, one on the left and one on the right.
So I'm going to copy lines 33, 32, and 33.
Or actually, let's hit control or command D to just duplicate them.
Go to the beginning of this new line here, which is kind of in the end middle of line 33, and hit enter.
So we get a fresh line.
And the first thing I'm going to call out is that we now have an error here.
It says a local variable fun or function named origin is already defined in this scope.
What's happening here is that on line 32, we have vector 2 origin defining origin.
Not assigning it, but defining it and then assigning it to be equal to this value.
Then on line 34, we're trying to redefine origin.
So imagine we had this as a vector 2 up here and then we tried to change it to a vector 3 or some other thing.
The game engine is going to be all kinds of confused and not know what to do with this.
So we can't do that.
We can't reassign an object.
In fact, we can't even reassign it with or redeclare it with the specific type.
We just have to delete that declaration and then we can reassign the value without redeclaring the variable.
So we only have one origin value.
It's just getting changed here on line 32.
So, it's set to this position.
On line 35, it's set to this position, which is actually the exact same position, but we're going to make a small modification to it.
So, on line 35, instead of using the default origin, we're going to use the default origin plus some little offset to the left.
So, let's say minus and let's add in a variable here and call this underscore foot 