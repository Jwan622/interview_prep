require 'spec_helper'

describe Messages do
  it "should describe the introduction message" do
    full_intro_message_with_graphic = "===================================================================\n              __       __   __            __     _____   __     \n\\    /\\    / |    |   |    |  | |\\    /| |         |    |  |    \n \\  /  \\  /  |--  |   |    |  | | \\  / | |--       |    |  |    \n  \\/    \\/   |__  |__ |__  |__| |  \\/  | |__       |    |__|    \n                    ___    ___     ____                           \n                    |  )  |   |   |                               \n                    |_)   |___|   |                               \n                    |\\    |       |____                           \n                    | \\   |            |                          \n                    |  \\  |       _____|                          \n===================================================================\nYou are playing against strategy favorite."

    expect(Messages.introduction("favorite")).to eql(full_intro_message_with_graphic)
  end

  it "should describe the display options" do
    expect(Messages.display_options).to eql("Type 'r', 'p' or 's'. Or type 'q' to quit.")
  end

  it "should describe invalid input" do
    expect(Messages.invalid_input).to eql("Your input is invalid.")
  end

  it "should output end_game" do
    expect(Messages.end_game).to eql("Thanks for playing. Goodbye!")
  end

  it "should state the play and the winner" do
    expect(Messages.computer_play_and_eval(:s, "You win!")).to eql("I chose s. You win!")
    expect(Messages.computer_play_and_eval(:p, "Computer wins!")).to eql("I chose p. Computer wins!")
    expect(Messages.computer_play_and_eval(:r, "It's a tie!" )).to eql("I chose r. It's a tie!")
  end

  it "should announce score" do
    user_score = 2
    computer_score = 3
    tie_score = 0

    expect(Messages.announce_score(user_score, computer_score, tie_score)).to eql("You won 2 times.\nYou lost 3 times.\nWe tied 0 times.\n")
  end
end
