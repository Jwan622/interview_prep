## Instructions

In order to run the game, clone this repo and type this in the command line inside the root folder:

```ruby
ruby rbs.rb
```

or with a selected strategy:

```ruby
ruby rbs.rb favorite
```

or

```ruby
ruby rbs.rb last
```

```ruby
ruby rbs.rb champ
```

You can also supply input and output streams:

```ruby
ruby rbs.rb favorite $stdin $stdout
```

If you input an invalid strategy or stream, defaults will be chosen for you. Currently the only input and output streams supported at $stdin and $stdout. The only strategies supported right now are favorite, last, and champ. Good luck!


### Rock Paper Scissors

Write a Rock Paper Scissors game. The game can be instantiated with various strategies. Below are two strategies for you to write, and an example of how players interact with the game.

**Strategy 1: Beat Their Last Move.**
Here you will play the move that beats their last move.

**Strategy 2: Beat Their Favorite.**
Here you will play the move that beats their most frequent move.

**Strategy 3: Extra Credit.**
Come up with your own strategy if you have time.

Interacting with your game
The example below is a Ruby script, though feel free to use another language.

```
$ruby rps.rb favorite
You are playing against strategy 'favorite'.
Type 'r', 'p' or 's'.
>r
I chose 's'. You win!
you won 1 times.
you lost 0 times.
we tied 0 times.
Type 'r', 'p' or 's'.
>p
I chose 'p'. It's a tie!
you won 1 times.
you lost 0 times.
we tied 1 times.
>
```

### Notes

1. Write tests for your implementation.
2. Focus on clean, clear code. Your code should exhibit strong Object Oriented design. However, if you decide to pursue another design strategy, please explain.


### Questions

Try not to ask any questions about the above. If something feels unclear, take it in any direction you like.
