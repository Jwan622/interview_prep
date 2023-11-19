require 'spec_helper'

describe ComputerChamp do
  attr_reader :computer

  before :each do
    @computer = ComputerChamp.new
  end

  it "should return a move that always beats a user's last move" do
    computer_decision = computer.make_decision({ r: 1, p: 0, s: 0 })
    expect(computer_decision).to eql(:p)

    computer_decision = computer.make_decision({ r: 1, p: 1, s: 0 })
    expect(computer_decision).to eql(:s)

    computer_decision = computer.make_decision({ r: 1, p: 1, s: 1 })
    expect(computer_decision).to eql(:r)

    computer_decision = computer.make_decision({ r: 1, p: 1, s: 2 })
    expect(computer_decision).to eql(:r)
  end
end
