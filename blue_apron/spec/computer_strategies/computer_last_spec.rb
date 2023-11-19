require 'spec_helper'

describe ComputerLast do
  attr_reader :computer

  before :each do
    @computer = ComputerLast.new
  end

  it "should initialize with a nil last tally" do
    expect(computer.last_tally).to eql(r:0, s:0, p:0)
  end

  it "should initialize with a second to last move" do
    expect(computer.second_to_last_move).to eql(nil)
  end

  it "should update last tally if passed a tally" do
    computer.make_decision({ r: 1, p: 0, s: 0 })

    expect(computer.last_tally).to eql({ r: 1, p: 0, s: 0 })
  end

  it "should return a random move if there is no second to last move" do
    user_plays_only_one_move = { r: 1, p: 0, s: 0 }
    computer_decision = computer.make_decision(user_plays_only_one_move)

    expect([:p, :r, :s]).to include(computer_decision)
  end

  it "should be able to calculate the player's second to last move" do
    user_plays_rock_first = { r: 1, p: 0, s: 0 }
    computer.make_decision(user_plays_rock_first)

    expect(computer.second_to_last_move).to eql(:r)

    user_then_plays_paper = { r: 1, p: 1, s: 0 }
    computer.make_decision(user_then_plays_paper)

    expect(computer.second_to_last_move).to eql(:p)

    user_then_plays_paper_again = { r: 1, p: 2, s: 0 }
    computer.make_decision(user_then_plays_paper_again)

    expect(computer.second_to_last_move).to eql(:p)
  end

  it "should return a move that beats a user's second to last move" do
    computer.make_decision({ r: 1, p: 0, s: 0 })
    computer_decision = computer.make_decision({ r: 1, p: 1, s: 0 })

    expect(computer_decision).to eql(:p)

    computer_decision = computer.make_decision({ r: 1, p: 1, s: 1 })
    expect(computer_decision).to eql(:s)

    computer_decision = computer.make_decision({ r: 2, p: 1, s: 1 })
    expect(computer_decision).to eql(:r)
  end
end
