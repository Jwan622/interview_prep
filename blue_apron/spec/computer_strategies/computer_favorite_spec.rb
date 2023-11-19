require 'spec_helper'

describe ComputerFavorite do
  attr_reader :computer

  before :each do
    @computer = ComputerFavorite.new
  end

  it "should return a random move if there is no second to last move" do
    user_plays_only_one_move = { r: 1, p: 0, s: 0 }
    computer_decision = computer.make_decision(user_plays_only_one_move)

    expect([:p, :r, :s]).to include(computer_decision)
  end

  it "should return a move that beats a user's favorite move" do
    computer.make_decision({ r: 1, p: 0, s: 0 })
    computer_decision = computer.make_decision({ r: 1, p: 1, s: 0 })

    expect([:p, :s]).to include(computer_decision)
    expect(computer_decision).not_to eql(:r)

    computer_decision = computer.make_decision({ r: 1, p: 2, s: 0 })
    expect(computer_decision).to eql(:s)
  end
end
