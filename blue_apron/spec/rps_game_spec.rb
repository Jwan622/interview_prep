require 'spec_helper'

describe RpsGame do

  it "has a strategy selector" do
    rps = RpsGame.new("favorite")

    expect(rps.strategy_selector).to be_truthy
  end

  it "has a score" do
    rps = RpsGame.new("favorite")

    expect(rps.scorer).to be_truthy
  end

  it "has a score_keeper" do
    rps = RpsGame.new("favorite")

    expect(rps.score_keeper).to be_truthy
  end

  it "has a scorer" do
    rps = RpsGame.new("favorite")

    expect(rps.scorer).to be_truthy
  end

  it "has a moves tracker" do
    rps = RpsGame.new("favorite")

    expect(rps.moves_tracker).to be_truthy
  end

  it "has an input evaluator" do
    rps = RpsGame.new("favorite")

    expect(rps.input_evaluator).to be_truthy
  end

  it "has a switchable input and output stream" do
    rpsGame1 = RpsGame.new("favorite")
    rpsGame2 = RpsGame.new("last", "game controller", :television)

    expect(rpsGame1.input_stream).to eql($stdin)
    expect(rpsGame1.output_stream).to eql($stdout)
    expect(rpsGame2.input_stream).to eql("game controller")
    expect(rpsGame2.output_stream).to eql(:television)
  end

  it "can play rps" do
    $stdout = StringIO.new
    rps = RpsGame.new("favorite", $stdin, $stdout)
    allow_any_instance_of(ComputerFavorite).to receive(:make_decision).and_return(:s, :r, :s, :s, :s)
    allow(STDIN).to receive(:gets).and_return('s', 'p', 'p', 'r', 'p', 'q')
    full_game_texts = "===================================================================\n              __       __   __            __     _____   __     \n\\    /\\    / |    |   |    |  | |\\    /| |         |    |  |    \n \\  /  \\  /  |--  |   |    |  | | \\  / | |--       |    |  |    \n  \\/    \\/   |__  |__ |__  |__| |  \\/  | |__       |    |__|    \n                    ___    ___     ____                           \n                    |  )  |   |   |                               \n                    |_)   |___|   |                               \n                    |\\    |       |____                           \n                    | \\   |            |                          \n                    |  \\  |       _____|                          \n===================================================================\nYou are playing against strategy favorite.\nType 'r', 'p' or 's'. Or type 'q' to quit.\nI chose s. It's a tie!\nYou won 0 times.\nYou lost 0 times.\nWe tied 1 times.\nType 'r', 'p' or 's'. Or type 'q' to quit.\nI chose r. You win!\nYou won 1 times.\nYou lost 0 times.\nWe tied 1 times.\nType 'r', 'p' or 's'. Or type 'q' to quit.\nI chose s. Computer wins!\nYou won 1 times.\nYou lost 1 times.\nWe tied 1 times.\nType 'r', 'p' or 's'. Or type 'q' to quit.\nI chose s. You win!\nYou won 2 times.\nYou lost 1 times.\nWe tied 1 times.\nType 'r', 'p' or 's'. Or type 'q' to quit.\nI chose s. Computer wins!\nYou won 2 times.\nYou lost 2 times.\nWe tied 1 times.\nType 'r', 'p' or 's'. Or type 'q' to quit.\nThanks for playing. Goodbye!\n"

    rps.play

    expect($stdout.string).to eql(full_game_texts)
  end
end
